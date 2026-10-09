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

ROOT = Path(__file__).resolve().parents[1]
TEACHING = ROOT.parent
OUT = ROOT / '.build'
CATALOG = json.loads((ROOT / 'catalog.json').read_text())
ESC = html.escape

ICONS = {
    'book': '<path d="M12 5c-3-2-7-2-10-1v15c3-1 7-1 10 1 3-2 7-2 10-1V4c-3-1-7-1-10 1Z"/><path d="M12 5v15"/>',
    'slides': '<path d="M14 2H5a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V9Z"/><path d="M14 2v7h7"/>',
    'sheet': '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 7h8M8 11h8M8 15h6"/>',
    'down': '<path d="M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5"/>',
    'arrow': '<path d="M4 12h16m-6-6 6 6-6 6"/>',
    'folder': '<path d="M3 6V4h6l2 3h10v13H3Z"/>',
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
        name = path.name
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
    readme = f"{course['code']} - Week {week['number']:02}: {week['title']}\n\nOpen {names['slides']} in a browser for the interactive slides.\nRead {names['guide']} for the study guide.\nPractice with {names['sheet']}.\n\nExtract the ZIP first and keep its files together so the slides and guide can link to each other.\nHTML contains the interactive activities. PDFs are reading and printing copies where available.\nThese are teaching materials. Follow the submission instructions and deadline announced in class.\n"
    (directory / 'README.txt').write_text(readme)
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
    name = names[kind]
    path = prefix + week['_directory'] + '/' + name
    is_pdf = name.endswith('.pdf')
    pdf = names.get(kind + '_pdf')
    context = f"{title}, week {week['number']}"
    format_label = 'PDF' if is_pdf else ('HTML + PDF' if pdf else ('Interactive HTML' if kind == 'slides' else 'HTML'))
    opener = link(path, 'Open ' + icon('arrow'), aria=f'Open {context}')
    if pdf:
        pdf_path = prefix + week['_directory'] + '/' + pdf
        downloader = f'<details class="download-menu"><summary>{icon("down")} Download</summary><div class="download-options">{link(path,"HTML file",True,aria=f"Download {context} HTML")}{link(pdf_path,"PDF file",True,aria=f"Download {context} PDF")}</div></details>'
        pdf_open = link(pdf_path, 'PDF', css='pdf-open', aria=f'Open {context} PDF')
    else:
        downloader = link(path, icon('down') + 'Download', True, aria=f'Download {context}')
        pdf_open = ''
    return f'<div class="resource"><span class="resource-icon">{icon(symbol)}</span><div><h4>{title}</h4><p class="format">{format_label}</p><div class="actions">{opener}<span class="separator" aria-hidden="true"></span>{downloader}{pdf_open}</div></div></div>'

def week_panel(course, week, prefix):
    number = f"{week['number']:02}"
    download = link(prefix+week['_zip'], icon('down') + 'Download week ZIP', True, 'button', f"Download {course['code']} week {number} ZIP")
    items = ''.join(resource(week,*args,prefix) for args in [('slides','Slides','slides'),('guide','Study guide','book'),('sheet','Practice sheet','sheet')])
    extra = ''
    if week.get('_starter_zip'):
        starters = ''.join(link(prefix + week['_directory'] + '/starter-files/' + Path(s).name, ESC(Path(s).name), True) for s in week['starters'])
        extra += f'<details class="starter-list"><summary>{icon("folder")} Starter files</summary><div class="starter-downloads">{link(prefix+week["_starter_zip"],"Download starter ZIP",True)}{starters}</div></details>'
    for entry, name in week['_extras']:
        path = prefix + week['_directory'] + '/' + name
        extra += f'<span class="extra-file">{link(path,ESC(entry["label"]))}{link(path,icon("down"),True,aria="Download "+entry["label"])}</span>'
    if extra:
        extra = f'<div class="extras">{extra}</div>'
    return f'<article class="week" id="week-{number}"><div class="week-header"><div><a class="week-number" href="#week-{number}">Week {number}</a><h3>{ESC(week["title"])}</h3><p>{ESC(week["description"])}</p></div>{download}</div><div class="resources">{items}</div>{extra}</article>'

def page(course, nested=True):
    prefix = '../' if nested else ''
    cards = ''
    for c in CATALOG['courses']:
        selected = ' aria-current="page"' if c['id'] == course['id'] else ''
        count = len(c['weeks'])
        cards += f'<a class="course-card" href="{prefix}{c["id"]}/"{selected}><strong>{c["code"]}</strong><span>{ESC(c["title"])}</span><small>{ESC(c["language"])} · {count} {"week" if count == 1 else "weeks"}</small></a>'
    panels = ''.join(week_panel(course,w,prefix) for w in sorted(course['weeks'],key=lambda w:w['number'],reverse=True))
    course_zip = link(prefix+f'downloads/{course["code"]}-All-weeks.zip',icon('down')+'Download course ZIP',True,'course-download')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{ESC(course['title'])} lab slides, study guides and practice sheets. Ahmed Tolan, 2026/2027 semester 1.">
<meta name="theme-color" content="#10263f"><title>{course['code']} | Ahmed Tolan · Teaching resources</title>
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/style.css"></head>
<body><a class="skip-link" href="#weeks">Skip to weekly materials</a><div class="container">
<header class="site-header"><a class="brand" href="{prefix}index.html">{icon('book')}<span><b>Ahmed Tolan</b><small>Teaching resources</small></span></a><p>2026 / 2027 · Semester 1</p></header>
<main><section class="intro" aria-labelledby="page-title"><h1 id="page-title">Your lab, week by week.</h1><p>Slides, guides and practice sheets. Open online or download for later.</p></section>
<nav class="courses" aria-label="Choose your course">{cards}</nav>
<section id="weeks" aria-labelledby="course-title"><div class="section-heading"><div><h2 id="course-title">{ESC(course['title'])}</h2><p>Choose a week to get started.</p></div>{course_zip}</div>{panels}</section>
</main><footer><p>Keep this link. New weeks appear here.</p><p>Ahmed Tolan · 2026 / 2027</p></footer></div></body></html>'''

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
        for match in re.finditer(r'open:\s*(\[\s*\[.*?\]\s*\])', contents):
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
