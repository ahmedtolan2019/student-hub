#!/usr/bin/env python3
"""Build the student site from the explicit catalog. Python standard library only."""
import base64
import hashlib
import html
import json
import re
import shutil
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from computer_basics import build_basics

ROOT = Path(__file__).resolve().parents[1]
TEACHING = ROOT.parent
OUT = ROOT / '.build'
CATALOG = json.loads((ROOT / 'catalog.json').read_text())
ESC = html.escape

ICONS = {
    'book': '<path d="M12 5c-3-2-7-2-10-1v15c3-1 7-1 10 1 3-2 7-2 10-1V4c-3-1-7-1-10 1Z"/><path d="M12 5v15"/>',
    'slides': '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8m-4-4v4"/>',
    'sheet': '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 7h8M8 11h8M8 15h6"/>',
    'down': '<path d="M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5"/>',
    'arrow': '<path d="M4 12h16m-6-6 6 6-6 6"/>',
    'folder': '<path d="M3 6V4h6l2 3h10v13H3Z"/>',
    'external': '<path d="M14 3h7v7m0-7L10 14M10 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-5"/>',
}

def icon(name):
    return f'<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'

def read_source(course, week, source):
    path = (TEACHING / course['source'] / week['folder'] / source).resolve()
    course_root = (TEACHING / course['source']).resolve()
    if not path.is_relative_to(course_root) or not path.is_file():
        raise ValueError(f'Missing or out-of-course source: {path}')
    if any(part in ('textbook', 'reference-codes', 'sheet-01-reference-solutions') for part in path.parts):
        raise ValueError(f'Not a student publication source: {path}')
    return path

def public_gen_slides(source, guide_name, allowed_pdfs):
    """Same student behavior as the course exporter, with an explicit PDF allowlist.

    The textbook button is omitted. No textbook bytes enter the public build.
    PDF buttons embed the approved sheets/lectures for standalone downloads.
    """
    page = source.read_text()
    pdfs = {}
    def rewrite_open(match):
        links = json.loads(match[1])
        public = []
        for label, target in links:
            path, _, fragment = target.partition('#')
            suffix = '#' + fragment if fragment else ''
            if path == '../guide/index.html':
                public.append([label, guide_name + suffix])
            elif '/textbook/' in path:
                continue
            elif path.endswith('.pdf'):
                full = (source.parent / path).resolve()
                if full not in allowed_pdfs:
                    raise ValueError(f'Unlisted PDF button: {full}')
                pdfs[full.name] = base64.b64encode(full.read_bytes()).decode()
                public.append([label, 'pdf:' + full.name + suffix])
            else:
                raise ValueError(f'Unsupported slide link: {target}')
        return 'open: ' + json.dumps(public, ensure_ascii=False)
    page, count = re.subn(r'open:\s*(\[\s*\[.*?\]\s*\])', rewrite_open, page)
    if not count:
        raise ValueError(f'No slide links found: {source}')
    opener = '''<script>(function(){
const pdfs=__PDFS__, urls={};
document.addEventListener('click',function(e){
const a=e.target.closest('a.openbtn[href^="pdf:"]'); if(!a)return;
e.preventDefault(); const ref=a.getAttribute('href').slice(4),name=ref.split('#')[0],frag=ref.includes('#')?ref.slice(ref.indexOf('#')):'';
if(!urls[name]){const bytes=Uint8Array.from(atob(pdfs[name]),c=>c.charCodeAt(0));urls[name]=URL.createObjectURL(new Blob([bytes],{type:'application/pdf'}));}
window.open(urls[name]+frag,'_blank');
},true);})();</script>'''.replace('__PDFS__', json.dumps(pdfs))
    page = page.replace('</body>', opener + '</body>')
    return page.replace('</head>', '<style>/* Student copy */ .kicker > span:not(.pill) { display:none!important; }</style></head>', 1)

def archive(target, files, base, prefix):
    """Fixed ZIP metadata keeps unchanged publications byte-for-byte stable."""
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
        for file in sorted(files):
            entry = zipfile.ZipInfo(prefix + '/' + file.relative_to(base).as_posix(), (2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o644 << 16
            z.writestr(entry, file.read_bytes())
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None

def build_week(course, week):
    directory = OUT / 'materials' / course['id'] / f"week-{week['number']:02}"
    directory.mkdir(parents=True)
    if week['kind'] == 'bundle':
        bundle = course['bundles'][week['bundle']]
        if week['folder'] != bundle['folder']:
            raise ValueError('Bundle folder must match its reviewed source')
        for item in bundle['files']:
            relative = Path(item)
            if relative.is_absolute() or '..' in relative.parts:
                raise ValueError(f'Unsafe bundle path: {item}')
            path = read_source(course, week, item)
            target = directory / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
        for key in ('slides', 'guide', 'sheet'):
            if key in week and week[key] not in bundle['files']:
                raise ValueError(f'Unlisted bundle resource: {week[key]}')
    resolved = {k: read_source(course, week, week[k]) for k in ('slides','guide','guide_pdf','sheet','sheet_pdf') if k in week}
    # Detect old student HTML rather than silently publishing an earlier lesson.
    if week['kind'] == 'student':
        for key in ('slides', 'guide'):
            master = TEACHING / course['source'] / week['folder'] / key / 'index.html'
            if master.stat().st_mtime > resolved[key].stat().st_mtime + 1:
                raise ValueError(f'Refresh the student {key} export first: {resolved[key]}')
    extras = [(entry, read_source(course, week, entry['source'])) for entry in week.get('extras', [])]
    names = {}
    for key, path in resolved.items():
        name = week[key] if week['kind'] == 'bundle' else path.name
        if week['kind'] == 'gen241' and key in ('slides','guide'):
            name = f"GEN241 Week {week['number']:02} - {key.title()}.html"
        names[key] = name
        if week['kind'] == 'gen241' and key == 'slides':
            allowed = {p for p in resolved.values() if p.suffix == '.pdf'} | {p for _, p in extras if p.suffix == '.pdf'}
            (directory / name).write_text(public_gen_slides(path, f"GEN241 Week {week['number']:02} - Guide.html", allowed))
        else:
            shutil.copyfile(path, directory / name)
    for _, path in extras:
        shutil.copyfile(path, directory / path.name)
    for item in week.get('starters', []):
        path = read_source(course, week, item)
        target = directory / 'starter-files' / path.name
        target.parent.mkdir(exist_ok=True)
        shutil.copyfile(path, target)
    if week.get('workbook'):
        key = week['workbook']
        workbook = course['workbooks'][key]
        workbook_dir = directory / f'{key}-workbook'
        # Copy only individually reviewed public files from the catalog.
        for item in workbook['files']:
            relative = Path(item)
            if relative.is_absolute() or '..' in relative.parts:
                raise ValueError(f'Unsafe workbook path: {item}')
            path = read_source(course, {'folder': workbook['folder']}, item)
            if not path.is_relative_to((TEACHING / course['source'] / workbook['folder']).resolve()):
                raise ValueError(f'Workbook source escapes its public folder: {item}')
            target = workbook_dir / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
        if not (workbook_dir / 'index.html').is_file():
            raise ValueError('Workbook allowlist must include index.html')
        workbook_zip = OUT / 'downloads' / f"{course['code']}-{key}-Workbook.zip"
        archive(workbook_zip, [workbook_dir / f for f in workbook['files']], workbook_dir,
                f"{course['code']}-{key}-Workbook")
        week['_workbook'] = {**workbook, 'path': (workbook_dir/'index.html').relative_to(OUT).as_posix(),
                             'zip': workbook_zip.relative_to(OUT).as_posix()}
    if 'guide' not in names and 'sheet' not in names:
        readme = f"{course['code']} - Week {week['number']:02}: {week['title']}\n\nOpen {names['slides']} in a browser for the complete interactive whiteboard lesson.\nRead START-HERE.txt for setup, worked code and practice instructions.\nThe practice tasks are inside the whiteboard; there is no separate sheet.\n\nExtract the ZIP first and keep code/ and practice/ beside the HTML file.\nNo third-party Python libraries are needed.\nFollow the submission instructions and deadline announced in class.\n"
    elif 'slides' not in names:
        readme = f"{course['code']} - Week {week['number']:02}: {week['title']}\n\nOpen {names['guide']} for the question-by-question study guide.\nPractice with {names['sheet']}.\n\nThe guide includes the original question images, background, C++ explanations, worked examples and common mistakes.\nHTML contains the interactive steps; the PDF is a reading copy.\nExtract the ZIP first and keep its files together. Follow the submission instructions and deadline announced in class.\n"
    else:
        readme = f"{course['code']} - Week {week['number']:02}: {week['title']}\n\nOpen {names['slides']} in a browser for the interactive slides.\nRead {names['guide']} for the study guide.\nPractice with {names['sheet']}.\n\nExtract the ZIP first and keep its files together so the slides and guide can link to each other.\nHTML contains the interactive activities. PDFs are reading and printing copies where available.\nThese are teaching materials. Follow the submission instructions and deadline announced in class.\n"
    (directory / 'README.txt').write_text(readme)
    if week.get('_workbook'):
        with (directory / 'README.txt').open('a') as f:
            f.write(f"\nOpen {week['workbook']}-workbook/index.html for illustrated foundations and recorded C++ traces. Keep that folder intact.\n")
    files = [p for p in directory.rglob('*') if p.is_file()]
    bundle = OUT / 'downloads' / f"{course['code']}-Week-{week['number']:02}.zip"
    archive(bundle, files, directory, f"{course['code']}-Week-{week['number']:02}")
    week['_names'] = names
    week['_directory'] = directory.relative_to(OUT).as_posix()
    week['_zip'] = bundle.relative_to(OUT).as_posix()
    week['_extras'] = [(entry, path.name) for entry, path in extras if not entry.get('hidden')]
    if week.get('starters'):
        starter_zip = OUT / 'downloads' / f"{course['code']}-Week-{week['number']:02}-Starter-files.zip"
        archive(starter_zip, list((directory/'starter-files').glob('*')), directory/'starter-files', 'starter-files')
        week['_starter_zip'] = starter_zip.relative_to(OUT).as_posix()

def link(path, label, download=False, css='', aria=None):
    attributes = ' download' if download else ' target="_blank" rel="noopener"'
    if aria:
        attributes += f' aria-label="{ESC(aria, quote=True)}"'
    return f'<a class="{css}" href="{quote(path, safe="/#")}"{attributes}>{label}</a>'

def resource(week, kind, title, symbol, prefix):
    names = week['_names']
    path = prefix + week['_directory'] + '/' + names[kind]
    is_pdf = names[kind].endswith('.pdf')
    pdf = names.get(kind + '_pdf')
    context = f"{title}, week {week['number']}"
    format_label = 'PDF document' if is_pdf else ('HTML + PDF' if pdf else 'Interactive HTML')
    open_label = 'Open PDF' if is_pdf else 'Open web'
    save_label = 'Get PDF' if is_pdf else 'Get HTML'
    actions = link(path, open_label + icon('external'), css='pill pill-open', aria=f'Open {context}')
    if week['kind'] == 'bundle' and not is_pdf:
        actions += link(prefix + week['_zip'], icon('down') + 'Get ZIP', True, 'pill', f'Download {context} with supporting files')
    else:
        actions += link(path, icon('down') + save_label, True, 'pill', f'Download {context}')
    if pdf:
        pdf_path = prefix + week['_directory'] + '/' + pdf
        actions += link(pdf_path, 'Open PDF' + icon('external'), css='pill', aria=f'Open {context} PDF')
        actions += link(pdf_path, icon('down') + 'Get PDF', True, 'pill', f'Download {context} PDF')
    return f'''<div class="resource-row flex flex-wrap items-center justify-between gap-4">
      <div class="resource-label flex items-center gap-3"><span class="resource-icon">{icon(symbol)}</span>
        <div><h4>{title}</h4><p>{format_label}</p></div>
      </div><div class="resource-actions flex flex-wrap gap-2" role="group" aria-label="{ESC(context)} files">{actions}</div>
    </div>'''


def week_panel(course, week, prefix):
    number = f"{week['number']:02}"
    download = link(prefix + week['_zip'], icon('down') + 'Download week ZIP', True, 'button button-secondary', f"Download {course['code']} week {number} ZIP")
    rows = [('slides','Interactive slides','slides'),('guide','Study guide','book'),('sheet','Practice sheet','sheet')]
    items = ''.join(resource(week, kind, week.get('resource_titles', {}).get(kind, title), symbol, prefix)
                    for kind, title, symbol in rows if kind in week['_names'])
    if week.get('_workbook'):
        wb = week['_workbook']
        actions = link(prefix + wb['path'], 'Open workbook' + icon('external'), css='pill pill-open',
                       aria=f"Open Sheet 2 workbook, week {week['number']}")
        actions += link(prefix + wb['zip'], icon('down') + 'Workbook ZIP', True, 'pill',
                        f"Download Sheet 2 workbook, week {week['number']}")
        items = f'''<div class="resource-row flex flex-wrap items-center justify-between gap-4">
          <div class="resource-label flex items-center gap-3"><span class="resource-icon">{icon('book')}</span>
          <div><h4>{ESC(wb['title'])}</h4><p>{ESC(wb['description'])}</p></div></div>
          <div class="resource-actions flex flex-wrap gap-2">{actions}</div></div>''' + items
    extras = ''
    if week.get('_starter_zip'):
        starters = ''.join(link(prefix + week['_directory'] + '/starter-files/' + Path(s).name, ESC(Path(s).name), True, 'file-link') for s in week['starters'])
        starter_zip = link(prefix + week['_starter_zip'], icon('down') + 'Starter ZIP', True, 'pill')
        extras += f'<div class="starter-heading"><span>{icon("folder")} Starter files</span>{starter_zip}</div><div class="starter-files">{starters}</div>'
    for entry, name in week['_extras']:
        path = prefix + week['_directory'] + '/' + name
        extras += f'<div class="extra-row"><span>{icon("sheet")}{ESC(entry["label"])}</span><div class="resource-actions">{link(path,"Open PDF" + icon("external"),css="pill",aria="Open "+entry["label"])}{link(path,icon("down")+"Get PDF",True,"pill","Download "+entry["label"])}</div></div>'
    if extras:
        extras = f'<div class="extras">{extras}</div>'
    return f'''<article class="week-card grid" id="week-{number}" aria-labelledby="title-{number}">
      <div class="week-context"><a class="week-badge" href="#week-{number}">Week {number}</a>
        <h3 id="title-{number}">{ESC(week['title'])}</h3><p>{ESC(week['description'])}</p>{download}
      </div>
      <div class="week-resources">{items}{extras}</div>
    </article>'''


def site_header(prefix, current):
    course_links = ''
    for c in CATALOG['courses']:
        selected = ' aria-current="page"' if c['id'] == current else ''
        course_links += f'<a class="course-link" href="{prefix}{c["id"]}/"{selected} aria-label="{ESC(c["code"]+": "+c["title"])}">{c["code"]}</a>'
    selected = ' aria-current="page"' if current == 'computer-basics' else ''
    course_links += f'<a class="course-link basics-nav" href="{prefix}computer-basics/"{selected}>Computer basics</a>'
    return f'''<header class="site-header sticky top-0 z-50">
    <div class="nav-container mx-auto flex items-center justify-between gap-6">
      <a class="brand flex items-center gap-3" href="{prefix}index.html">{icon('book')}<span><b>Ahmed Tolan</b><small>Teaching resources</small></span></a>
      <nav class="course-switcher flex items-center gap-1" aria-label="Courses and computer help">{course_links}</nav>
      <p class="term">2026 / 2027<span>Semester 1</span></p>
    </div>
  </header>'''


def page(course, nested=True):
    prefix = '../' if nested else ''
    basics_help = ''
    if course['id'] in ('ece122', 'gen241'):
        basics_help = f'''<a class="basics-callout" href="{prefix}computer-basics/">
          <span class="resource-icon">{icon('slides')}</span><span><b>New to using a computer?</b>
          <span lang="ar" dir="rtl">ابدأ هنا: شرح بالصور للفولدرات، حفظ الكود، وفك ملفات ZIP.</span>
          <small>Introduction to Basic Computer · Windows &amp; Mac</small></span>{icon('arrow')}</a>'''
    weeks = sorted(course['weeks'], key=lambda w: w['number'], reverse=True)
    panels = ''.join(week_panel(course, week, prefix) for week in weeks)
    week_links = ''.join(f'<a class="toc-link" href="#week-{w["number"]:02}"><span>Week {w["number"]:02}</span><small>{ESC(w["title"])}</small></a>' for w in weeks)
    count = len(weeks)
    course_zip = link(prefix + f'downloads/{course["code"]}-All-weeks.zip', icon('down') + 'Download Course ZIP', True, 'button button-primary')
    styles = (ROOT / 'assets/style.css').read_text().replace('url("fonts/', 'url("' + prefix + 'assets/fonts/')
    scroll_script = (ROOT / 'assets/navigation.js').read_text()
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="{ESC(course['title'])} lab slides, study guides and practice sheets. Ahmed Tolan, 2026/2027 semester 1.">
  <meta name="theme-color" content="#f8fafc">
  <title>{course['code']} | Ahmed Tolan · Teaching resources</title>
  <link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4.3.3"></script>
  <style>{styles}</style>
</head>
<body>
  <a class="skip-link" href="#weeks">Skip to weekly materials</a>
  {site_header(prefix, course['id'])}
  <main>
    <section class="hero" aria-labelledby="page-title">
      <div class="hero-inner mx-auto">
        <div class="hero-meta flex items-center gap-3"><span class="course-badge">{course['code']}</span><span>{ESC(course['language'])} <span aria-hidden="true">·</span> {count} {'week' if count == 1 else 'weeks'}</span></div>
        <h1 id="page-title">{ESC(course['title'])}</h1>
        <div class="hero-bottom flex flex-wrap items-center justify-between gap-6"><p>Slides, guides and practice sheets.<br>Everything you need for the next lab.</p>{course_zip}</div>
      </div>
    </section>
    <div class="materials-layout mx-auto grid" id="weeks">
      <aside class="week-sidebar" aria-label="Weekly table of contents">
        <nav class="week-nav sticky" aria-label="Jump to a week"><h2>On this page</h2>{week_links}<p>New weeks appear here.<br>Keep this link handy.</p></nav>
      </aside>
      <section class="weekly-materials" aria-labelledby="materials-title">{basics_help}<div class="materials-heading flex items-center justify-between gap-4"><h2 id="materials-title">Weekly materials</h2><span>Newest first</span></div>{panels}</section>
    </div>
  </main>
  <footer class="site-footer"><div class="footer-inner mx-auto flex flex-wrap items-center justify-between gap-3"><span>Ahmed Tolan <span aria-hidden="true">·</span> Teaching resources</span><span>2026 / 2027 <span aria-hidden="true">·</span> Semester 1</span></div></footer>
  <script>{scroll_script}</script>
</body>
</html>'''

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src','href') and value:
                self.links.append(value)

def validate_site():
    count = 0
    for path in OUT.rglob('*.html'):
        parser = Links(); contents = path.read_text(); parser.feed(contents)
        # Includes navigation targets declared inside the slide data, not just HTML anchors.
        targets = list(parser.links)
        for match in re.finditer(r'(?:\bopen|"open"):\s*(\[\s*\[.*?\]\s*\])', contents):
            targets.extend(target for _, target in json.loads(match[1]))
        for target in targets:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(OUT.resolve()) or not dest.exists():
                raise ValueError(f'Broken local link in {path.relative_to(OUT)}: {target[:180]}')
            count += 1
        if 'file:///' in contents or '/Users/' in contents:
            raise ValueError(f'Local machine path in {path}')
    for file in OUT.rglob('*'):
        if file.is_file() and file.stat().st_size > 90*1024*1024:
            raise ValueError(f'File too large for this publication: {file}')
    print(f'Validated {count} local links; all ZIPs passed integrity checks.')

def main():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT/'assets', OUT/'assets')
    for course in CATALOG['courses']:
        for week in course['weeks']: build_week(course,week)
        base = OUT/'materials'/course['id']
        archive(OUT/'downloads'/f"{course['code']}-All-weeks.zip",[p for p in base.rglob('*') if p.is_file()],base,course['code'])
        dest = OUT/course['id']; dest.mkdir(); (dest/'index.html').write_text(page(course))
    (OUT/'index.html').write_text(page(CATALOG['courses'][0],nested=False))
    build_basics(ROOT, OUT, site_header('../', 'computer-basics'))
    (OUT/'.nojekyll').touch()
    validate_site()
    # Only replace the served output after the whole build passes.
    manifest = {str(p.relative_to(OUT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.rglob('*')) if p.is_file()}
    (OUT/'checksums.json').write_text(json.dumps(manifest,indent=2)+'\n')
    destination = ROOT/'docs'
    if destination.exists(): shutil.rmtree(destination)
    OUT.rename(destination)
    print(f'Built {len(CATALOG["courses"])} courses, {sum(len(c["weeks"]) for c in CATALOG["courses"])} weeks, {len(manifest)} files into docs/.')

if __name__ == '__main__':
    main()
