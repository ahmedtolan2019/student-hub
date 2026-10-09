"""Static beginner reference. Illustrations are authored diagrams, not screenshots."""
from html import escape as esc

SOURCES = {
    'windows': ('Microsoft · File Explorer', 'https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows'),
    'extensions': ('Microsoft · File extensions', 'https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/common-file-name-extensions-in-windows'),
    'windows-zip': ('Microsoft · ZIP files', 'https://support.microsoft.com/en-gb/windows/experience/storage-filemanagement/zip-and-unzip-files'),
    'mac-folders': ('Apple · Folders', 'https://support.apple.com/en-gb/guide/mac-help/mh26885/mac'),
    'mac-copy': ('Apple · Copy and paste', 'https://support.apple.com/en-us/102553'),
    'mac-rename': ('Apple · Rename files', 'https://support.apple.com/guide/mac-help/rename-files-folders-and-disks-mchlp1144/mac'),
    'mac-zip': ('Apple · ZIP files', 'https://support.apple.com/en-bh/guide/mac-help/mchlp2528/mac'),
    'devcpp': ('Embarcadero · Dev-C++', 'https://github.com/Embarcadero/Dev-Cpp/wiki/Compiling'),
    'pycharm': ('JetBrains · Your first project', 'https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html'),
    'save': ('JetBrains · Save changes', 'https://www.jetbrains.com/help/pycharm/saving-and-reverting-changes.html'),
    '7zip': ('7-Zip · Official download', 'https://www.7-zip.org/download.html'),
}

# Trusted, authored HTML. English UI labels use bdi so Arabic reading order stays clear.
def ui(s):
    return '<bdi class="ui-label" dir="ltr">' + esc(s) + '</bdi>'

LESSONS = [
    dict(id='start', title='Meet your files & folders', ar='نبدأ من الأساسيات', tag='START HERE',
         intro='الفايل هو ملف زي كود أو PDF. الفولدر مكان بتحط فيه ملفاتك وتجمعها مع بعض. جرّب الخطوات على الكمبيوتر وإنت بتقرأ من الموبايل.',
         steps=[
             ('Click', 'ضغطة واحدة بالزر الشمال بتختار الملف. ضغطتين ورا بعض بسرعة بتفتح الملف أو الفولدر.'),
             ('Right-click', 'الزر اليمين بيظهر قائمة أوامر. على تاتش باد Mac تقدر تعمل '+ui('Control + click')+' عشان تفتحها.'),
             ('Find your files', 'على Windows افتح '+ui('File Explorer')+' باختصار '+ui('Windows + E')+'. على Mac افتح '+ui('Finder')+' من الشريط اللي تحت. هتلاقي '+ui('Documents')+' و'+ui('Downloads')+' في القائمة الجانبية.')],
         note='الصور هنا رسومات تعليمية مبسطة، مش لقطات شاشة فعلية. شكل القوائم ممكن يختلف حسب إصدار جهازك ولغة البرنامج.',
         scene=('Files & folders', 'Documents  >  My labs', ['Lab 01', 'hello.cpp', 'hello.py', 'Guide.pdf'], ['1 click = select', '2 clicks = open', 'Right-click = menu']), sources=['windows']),
    dict(id='folder', title='Create a folder', ar='اعمل فولدر لشغلك', tag='FILES',
         intro='خلّي لكل كورس فولدر، وجواه فولدر لكل لاب. كده هتعرف تلاقي شغلك بعد ما تقفل البرنامج.',
         steps=[
             ('Choose a place', 'افتح '+ui('Documents')+' من '+ui('File Explorer')+' أو '+ui('Finder')+'.'),
             ('Windows', 'اضغط بالزر اليمين في مساحة فاضية، واختار '+ui('New → Folder')+'. اكتب '+ui('My labs')+' واضغط '+ui('Enter')+'. الاختصار: '+ui('Ctrl + Shift + N')+'.'),
             ('Mac', 'من القائمة فوق اختار '+ui('File → New Folder')+'، أو '+ui('Shift + Command + N')+'. اكتب الاسم واضغط '+ui('Return')+'.'),
             ('Make it yours', 'افتح الفولدر الجديد بضغطتين، واعمل جواه فولدر للكورس، وبعدين '+ui('Lab 01')+'. الأسماء دي للتجربة؛ في التسليم استخدم الأسماء المطلوبة في الشيت.')],
         note='المكان اللي ظاهر فوق النافذة هو عنوان الفولدر الحالي. افتكره عشان ترجع لنفس المكان وقت الحفظ.',
         scene=('File Explorer · Windows', 'Documents  >  My labs', ['Lab 01'], ['Right-click empty space', 'New  >  Folder', 'Name: Lab 01', 'Enter']), sources=['mac-folders']),
    dict(id='copy', title='Copy, paste & move', ar='انسخ ملف أو انقله', tag='FILES',
         intro='Copy بيعمل نسخة وبيسيب الأصل مكانه. Move بينقل الملف من المكان القديم للجديد.',
         steps=[
             ('Copy', 'اختار الملف بضغطة واحدة. على Windows اضغط '+ui('Ctrl + C')+'، وعلى Mac '+ui('Command + C')+'.'),
             ('Paste', 'افتح فولدر تاني، واضغط '+ui('Ctrl + V')+' على Windows أو '+ui('Command + V')+' على Mac. دلوقتي فيه نسخة في كل مكان.'),
             ('Move instead', 'على Windows: '+ui('Ctrl + X')+'، افتح المكان الجديد، ثم '+ui('Ctrl + V')+'. على Mac: '+ui('Command + C')+' ثم في المكان الجديد '+ui('Option + Command + V')+'.'),
             ('Check the result', 'لو ظهر إن فيه ملف بنفس الاسم، اختار '+ui('Cancel')+' لو مش متأكد. افتح الملفين واتأكد من محتواهم قبل ما تستبدل واحد بالتاني.')],
         note='اختصارات نسخ الملفات بتشتغل لما تكون محدد الملف في File Explorer أو Finder. لو جوه محرر الكود، هتنسخ النص المحدد.',
         scene=('Copy a file · Windows', 'Documents  >  Lab 01', ['hello.cpp'], ['1. Select hello.cpp', '2. Ctrl + C', '3. Open another folder', '4. Ctrl + V']), sources=['mac-copy']),
    dict(id='rename', title='Rename & keep the extension', ar='غيّر الاسم وسيب نوع الملف', tag='FILES',
         intro='في اسم زي '+ui('hello.cpp')+'، الجزء '+ui('.cpp')+' هو امتداد ملف C++. و'+ui('.py')+' لملف Python. تغيير الامتداد مش بيحوّل نوع الملف.',
         steps=[
             ('Show extensions', 'Windows 11: من '+ui('View → Show → File name extensions')+'. Windows 10: افتح تبويب '+ui('View')+' وعلّم على '+ui('File name extensions')+'.'),
             ('Windows', 'اختار الملف، واضغط '+ui('F2')+' أو بالزر اليمين اختار '+ui('Rename')+'. غيّر '+ui('hello')+' بس، وسيب '+ui('.cpp')+' زي ما هي، ثم '+ui('Enter')+'.'),
             ('Mac', 'في Finder اختار الملف واضغط '+ui('Return')+'، عدّل الاسم ثم '+ui('Return')+' تاني. لإظهار الامتدادات: '+ui('Finder → Settings → Advanced → Show all filename extensions')+'؛ في الإصدارات الأقدم اسمها '+ui('Preferences')+'.')],
         note='hello.cpp.txt مش ملف C++ بالامتداد المطلوب. ارجع للبرنامج واحفظه كملف C++، واتأكد من الاسم الكامل في فولدر الحفظ.',
         scene=('Rename a source file', 'Documents  >  Lab 01', ['practice.cpp'], ['Before: hello.cpp', 'Rename: practice.cpp', 'Keep .cpp', 'Do not add .txt']), sources=['extensions', 'mac-rename']),
    dict(id='download', title='Download & find your materials', ar='حمّل ملفات اللاب وافتحها', tag='STUDENT HUB',
         intro='لينك الكورس بيجمع الأسابيع كلها. زرار Open بيفتح الملف أونلاين، وزرار Get أو Download بينزّله على جهازك.',
         steps=[
             ('Choose your week', 'افتح صفحة الكورس، واختار الأسبوع. افتح السلايدز أو الـ Guide من '+ui('Open web')+'، أو الشيت من '+ui('Open PDF')+'.'),
             ('Download', 'حمّل ملف لوحده من '+ui('Get HTML')+' أو '+ui('Get PDF')+' حسب المتاح. لو عايز ملفات الأسبوع مع بعض اختار '+ui('Download week ZIP')+'.'),
             ('Find it', 'افتح قائمة التنزيلات في المتصفح، واختار إظهار الملف في فولدره. غالبًا هتلاقيه في '+ui('Downloads')+'، إلا لو اخترت مكان تاني وقت التحميل.'),
             ('Open locally', 'ملف PDF بيتفتح بقارئ PDF أو المتصفح. ملف HTML بيتفتح في المتصفح. لو نزلت ZIP، فكّه الأول بالطريقة اللي تحت، وسيب ملفات الأسبوع مع بعض عشان الروابط تفضل شغالة.')],
         note='لو التحميل لسه شغال أو الملف حجمه صفر، استنى لحد ما يكتمل. السلايدز التفاعلية موجودة في نسخة HTML.',
         scene=('Find your download', 'Downloads', ['GEN241-Week-01.zip', 'Guide.pdf'], ['Open web = read online', 'Get PDF = save one file', 'Week ZIP = all week files']), sources=[]),
    dict(id='cpp', title='Save C++ from Dev-C++', ar='احفظ ملف الكود نفسه', tag='GEN241 · WINDOWS',
         intro='حفظ الكود مختلف عن تشغيله. المطلوب هنا إن يبقى عندك ملف '+ui('.cpp')+' تعرف مكانه وتقدر تفتحه تاني.',
         steps=[
             ('New source file', 'في Dev-C++ اختار '+ui('File → New → Source File')+'. لو الكود مفتوح عندك بالفعل، كمّل من الخطوة اللي بعدها.'),
             ('Save As', 'اختار '+ui('File → Save As')+'. في نافذة الحفظ ادخل على '+ui('Documents')+' ثم فولدر اللاب اللي عملته.'),
             ('Name & save', 'اكتب '+ui('hello.cpp')+' في '+ui('File name')+'، واختار نوع ملفات '+ui('C++ source files (*.cpp)')+' لو ظاهر، ثم اضغط '+ui('Save')+'.'),
             ('Check it', 'بعد أي تعديل اضغط '+ui('Ctrl + S')+'. افتح فولدر اللاب واتأكد إن '+ui('hello.cpp')+' موجود. افتحه من '+ui('File → Open')+' في Dev-C++ وشوف إن آخر تعديل موجود.')],
         note='الشرح ده لبرنامج Dev-C++ على Windows. على Mac استخدم محرر الكود المحدد في اللاب واحفظ بامتداد .cpp. ملف .exe الناتج من التشغيل أو صورة الشاشة مش بديل لملف الكود.',
         scene=('Dev-C++ · Save As · illustration', 'Documents  >  My labs  >  Lab 01', ['hello.cpp'], ['File name: hello.cpp', 'Type: C++ source (*.cpp)', 'Save', 'Later changes: Ctrl + S']), sources=['devcpp']),
    dict(id='python', title='Save Python from PyCharm', ar='اعرف ملف Python محفوظ فين', tag='ECE122 · WINDOWS / MAC',
         intro='ملفات PyCharm بتكون جوه فولدر المشروع. البرنامج بيحفظ تلقائيًا في مواقف كتير، وتقدر تعمل حفظ يدوي كمان.',
         steps=[
             ('Know the location', 'لو بتعمل مشروع جديد من '+ui('New Project')+'، اختار مكانه في '+ui('Location')+' داخل فولدر شغلك. لو المشروع موجود، استخدم نفس المشروع.'),
             ('Create a Python file', 'في قائمة '+ui('Project')+' على الشمال، اضغط بالزر اليمين على فولدر المشروع واختار '+ui('New → Python File')+'. اكتب '+ui('hello')+'، وهيتعمل '+ui('hello.py')+'.'),
             ('Save All', 'بعد كتابة الكود اختار '+ui('File → Save All')+'. مع الاختصارات الافتراضية: '+ui('Ctrl + S')+' على Windows أو '+ui('Command + S')+' على Mac.'),
             ('Locate & check', 'اضغط بالزر اليمين على '+ui('hello.py')+' في Project. دور على '+ui('Open In → Explorer')+' أو '+ui('Finder')+' حسب جهازك وإصدار البرنامج. أو افتح فولدر المشروع اللي اخترته في Location. اتأكد إن ملف '+ui('.py')+' موجود هناك.')],
         note='للتسليم، خد ملفات .py المطلوبة حسب تعليمات الشيت. فولدر .venv بتاع بيئة Python مش هو كودك، ومش محتاج تضغطه مع الحل إلا لو مطلوب صراحة.',
         scene=('PyCharm · Project · illustration', 'My labs  >  Lab 01', ['hello.py', '.venv'], ['New  >  Python File', 'Name: hello', 'File  >  Save All', 'Your code: hello.py']), sources=['pycharm','save']),
    dict(id='zip', title='Make a ZIP', ar='اجمع ملفاتك في ZIP واحد', tag='WINDOWS / MAC',
         intro='ZIP بيجمع ملفات أو فولدر في ملف واحد سهل تبعته. اعمل فولدر فيه الملفات المطلوبة بس، واحفظ آخر تعديل قبل الضغط.',
         steps=[
             ('Prepare', 'لو هتضغط ملف واحد، اختاره مباشرة. لو عندك كذا ملف، حطهم في فولدر زي '+ui('Lab 01')+'، وارجع خطوة لبرّه الفولدر عشان تختاره.'),
             ('Windows 10', 'اضغط بالزر اليمين على الفولدر، واختار '+ui('Send to → Compressed (zipped) folder')+'. هيتعمل ملف ZIP جنبه.'),
             ('Windows 11', 'اختار '+ui('Compress to ZIP file')+' لو ظاهر، أو '+ui('Show more options → Send to → Compressed (zipped) folder')+'.'),
             ('Mac', 'في Finder اعمل '+ui('Control + click')+' على الفولدر واختار '+ui('Compress “Lab 01”')+'. هتلاقي '+ui('Lab 01.zip')+' في نفس المكان.')],
         note='Windows وMac فيهم ضغط ZIP من غير برنامج إضافي. لو عدّلت الكود بعد ما عملت ZIP، اعمل ZIP جديد عشان يحتوي على آخر نسخة.',
         scene=('Compress a folder', 'Documents  >  My labs', ['Lab 01', 'Lab 01.zip'], ['Windows: Send to', 'Compressed (zipped) folder', 'Mac: Compress “Lab 01”']), sources=['windows-zip','mac-zip']),
    dict(id='extract', title='Extract a ZIP', ar='فك الضغط قبل ما تشتغل', tag='WINDOWS / MAC',
         intro='فتح ZIP مش دايمًا معناه إنك فكّيته. اشتغل من الفولدر العادي اللي بيطلع بعد فك الضغط.',
         steps=[
             ('Windows', 'بالزر اليمين على ملف ZIP اختار '+ui('Extract All…')+'. اختار المكان اللي عايزه واضغط '+ui('Extract')+'.'),
             ('Mac', 'اضغط مرتين على ملف '+ui('.zip')+' في Finder. هتلاقي الملفات أو الفولدر الناتج في نفس المكان.'),
             ('Open the extracted folder', 'افتح الفولدر العادي الناتج، وبعدها افتح السلايدز أو الكود منه. خليك محافظ على ترتيب ملفات الأسبوع.'),
             ('If it fails', 'اتأكد إن التحميل اكتمل. لو ظهر إن الأرشيف تالف، جرّب تنزّله تاني. لو صيغة الملف مش ZIP أو النظام مش قادر يفتحها، شوف خيار 7-Zip تحت.')],
         note='سيب ZIP الأصلي موجود لحد ما تتأكد إن الملفات اتفكت وبتفتح. استخدم فولدر جديد للفك لو عندك نسخة قديمة عشان ما تستبدلش شغلك بالغلط.',
         scene=('Extract a ZIP · Windows', 'Downloads', ['GEN241-Week-01.zip', 'GEN241-Week-01'], ['Right-click ZIP', 'Extract All…', 'Choose destination', 'Extract']), sources=['windows-zip','mac-zip']),
    dict(id='7zip', title='Optional: install & use 7-Zip', ar='لو محتاج برنامج لفك الضغط', tag='OPTIONAL · WINDOWS',
         intro='جرّب طريقة النظام الأول. لو محتاج برنامج إضافي على Windows، استخدم 7-Zip من موقعه الرسمي. على Mac استخدم طريقة Finder اللي فوق لملفات ZIP.',
         steps=[
             ('Choose the installer', 'افتح لينك '+ui('7-Zip · Official download')+' تحت. اعرف نوع جهازك من '+ui('Settings → System → About → System type')+'. اختار '+ui('x64')+' لجهاز Intel/AMD بنظام 64-bit، أو '+ui('ARM64')+' لجهاز ARM، أو '+ui('x86')+' لنظام 32-bit.'),
             ('Install', 'نزّل ملف '+ui('.exe')+' المناسب، افتحه من Downloads، واتبع خطوات '+ui('Install')+' ثم '+ui('Close')+'. على جهاز المعمل لو التثبيت محتاج صلاحيات، اطلب المساعدة من مسؤول المعمل.'),
             ('Create a ZIP', 'بالزر اليمين على الفولدر اختار '+ui('7-Zip → Add to archive…')+'؛ ممكن تحتاج '+ui('Show more options')+' في Windows 11. اختار '+ui('Archive format: zip')+' ثم '+ui('OK')+'.'),
             ('Extract', 'بالزر اليمين على الأرشيف اختار '+ui('7-Zip → Extract files…')+'، وحدد فولدر جديد ثم '+ui('OK')+'. لو قائمة 7-Zip مش ظاهرة، افتح '+ui('7-Zip File Manager')+' من Start وحدد الملف واستخدم زر '+ui('Extract')+'.')],
         note='اختار zip لو المطلوب ZIP؛ امتداد .7z مختلف. مش محتاج تثبّت WinRAR و7-Zip مع بعض عشان تمشي مع الشرح ده.',
         scene=('7-Zip · Add to Archive · illustration', 'Documents  >  My labs', ['Lab 01.zip'], ['Archive: Lab 01.zip', 'Archive format: zip', 'OK']), sources=['7zip']),
    dict(id='check', title='Before you send your work', ar='مراجعة سريعة قبل التسليم', tag='FINAL CHECK',
         intro='دقيقة مراجعة بتوفر عليك إنك تبعت ملف غلط أو نسخة قديمة.',
         steps=[
             ('Save', 'احفظ آخر تعديل، وافتح ملف الكود من مكانه واتأكد إن ده شغلك الحالي.'),
             ('Match the instructions', 'راجع أسماء الملفات والفولدرات المطلوبة في الشيت، والامتدادات '+ui('.cpp')+' أو '+ui('.py')+'. الأسماء اللي في الشرح هنا للتجربة بس.'),
             ('Check the ZIP', 'لو التسليم ZIP، فك نسخة منه في فولدر جديد وافتح الملفات اللي طلعت. اتأكد إنك حاطط ملفات الكود المطلوبة فعلًا، مش اختصار للفولدر أو ملفات التشغيل بس.'),
             ('Keep a copy', 'احتفظ بنسخة من شغلك في مكان تقدر ترجع له، خصوصًا لو شغال على جهاز المعمل. اتبع طريقة وموعد التسليم المعلنين للكورس.')],
         note='لو خطوة مش ماشية، ابعت اسم البرنامج، وصورة للمشكلة، والرسالة اللي ظهرت. كده نقدر نساعدك أسرع.',
         scene=('Ready to submit?', 'Lab 01.zip  >  extracted copy', ['hello.cpp', 'hello.py'], ['Latest changes saved', 'Required names checked', 'Code files open correctly', 'Submission rules checked']), sources=[]),
]


def diagram(lesson):
    """Create precise, zoomable SVG UI diagrams with real text and explicit captions."""
    if lesson['id'] in ('cpp', '7zip'):
        return dialog_diagram(lesson['id'])
    title, path, files, actions = lesson['scene']
    def text(x,y,value,size=17,fill='#334155',weight=400):
        return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}">{esc(value)}</text>'
    s = ['<svg xmlns="http://www.w3.org/2000/svg" width="840" height="510" viewBox="0 0 840 510" role="img" aria-labelledby="title desc">',
         f'<title id="title">{esc(lesson["title"])}</title><desc id="desc">Simplified instructional illustration. {esc(path)}. {esc(". ".join(actions))}.</desc>',
         '<rect width="840" height="510" rx="20" fill="#eef2ff"/>',
         '<g font-family="system-ui, sans-serif"><rect x="24" y="24" width="792" height="456" rx="12" fill="white" stroke="#cbd5e1"/>',
         '<path d="M36 24h768a12 12 0 0 1 12 12v34H24V36a12 12 0 0 1 12-12" fill="#e2e8f0"/>',
         text(44,54,title,19,weight=600), text(44,104,path,17),
         '<path d="M24 122h792M185 122v358" stroke="#e2e8f0"/>',
         text(43,165,'Documents',16), text(43,204,'Downloads',16), text(43,243,'My labs',16),
         '<rect x="199" y="137" width="265" height="326" rx="8" fill="#f8fafc"/>']
    for i,name in enumerate(files):
        y = 174+i*70
        folder = '.' not in name or name=='.venv'
        if folder or name.endswith('.zip'):
            s += [f'<path d="M216 {y-22}h16l7 6h25v30h-48Z" fill="#fbbf24" stroke="#d99b20"/>']
            if name.endswith('.zip'):
                s += [f'<path d="M245 {y-16}v27" stroke="#475569" stroke-width="5" stroke-dasharray="3 2"/>']
        else:
            s += [f'<path d="M222 {y-25}h26l10 10v33h-36Z" fill="#e0e7ff" stroke="#818cf8"/>',f'<path d="M248 {y-25}v10h10M229 {y-5}h20m-20 8h16" fill="none" stroke="#6366f1"/>']
        # Long download filenames wrap into two readable lines.
        if len(name)>19:
            s += [text(279,y-3,name[:16],14),text(279,y+17,name[16:],14)]
        else:
            s += [text(279,y+3,name,17,weight=500)]
    s += ['<rect x="482" y="137" width="314" height="326" rx="8" fill="white" stroke="#c7d2fe"/>',text(503,170,'ACTION GUIDE',12,'#4f46e5',700)]
    for i,a in enumerate(actions):
        y=210+i*62
        s += [f'<circle cx="510" cy="{y-5}" r="12" fill="#4f46e5"/>', text(506,y,str(i+1),13,'white',600)]
        # Keep each caption legible at full size, without tiny simulated UI text.
        words=a.split(); lines=['']
        for word in words:
            if len(lines[-1]+' '+word)>28: lines.append(word)
            else: lines[-1]=(lines[-1]+' '+word).strip()
        for j,line in enumerate(lines): s += [text(531,y+j*20,line,15)]
    s += [text(26,501,'ILLUSTRATION · Menus and appearance vary by version.',12,'#607087'),'</g></svg>']
    return ''.join(s)


def dialog_diagram(kind):
    cpp = kind == 'cpp'
    title = 'Dev-C++ · Save As' if cpp else '7-Zip · Add to Archive'
    label1, value1 = ('File name:', 'hello.cpp') if cpp else ('Archive:', 'Lab 01.zip')
    label2, value2 = ('Save as type:', 'C++ source files (*.cpp)') if cpp else ('Archive format:', 'zip')
    button = 'Save' if cpp else 'OK'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="840" height="510" viewBox="0 0 840 510" role="img" aria-labelledby="title desc">
    <title id="title">{title} · simplified illustration</title><desc id="desc">Choose your lab folder, enter {value1}, select {value2}, then click {button}.</desc>
    <rect width="840" height="510" rx="20" fill="#eef2ff"/><g font-family="system-ui, sans-serif" fill="#334155">
    <rect x="24" y="24" width="792" height="456" rx="12" fill="white" stroke="#cbd5e1"/>
    <path d="M36 24h768a12 12 0 0 1 12 12v34H24V36a12 12 0 0 1 12-12" fill="#e2e8f0"/>
    <text x="44" y="54" font-size="20" font-weight="600">{title}</text>
    <circle cx="55" cy="108" r="15" fill="#4f46e5"/><text x="50" y="114" fill="white" font-size="17">1</text>
    <rect x="86" y="85" width="704" height="45" rx="5" fill="#f8fafc" stroke="#a5b4fc"/>
    <text x="101" y="114" font-size="20">Documents  ›  My labs  ›  Lab 01</text>
    <path d="M45 151h750M203 151v112" stroke="#e2e8f0"/>
    <text x="48" y="190" font-size="17">Documents</text><text x="48" y="231" font-size="17">Downloads</text>
    <text x="237" y="193" font-size="17" fill="#607087">Your lab folder</text>
    <text x="237" y="230" font-size="16" fill="#607087">Save your work in a place you can find again.</text>
    <circle cx="55" cy="304" r="15" fill="#4f46e5"/><text x="50" y="310" fill="white" font-size="17">2</text>
    <text x="88" y="312" font-size="19">{label1}</text><rect x="240" y="279" width="548" height="48" rx="5" fill="white" stroke="#6366f1" stroke-width="2"/>
    <text x="256" y="311" font-size="22">{value1}</text>
    <text x="88" y="371" font-size="19">{label2}</text><rect x="240" y="341" width="548" height="45" rx="5" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="256" y="371" font-size="20">{value2}</text><path d="m758 359 7 8 7-8" fill="none" stroke="#64748b" stroke-width="2"/>
    <circle cx="501" cy="433" r="15" fill="#4f46e5"/><text x="496" y="439" fill="white" font-size="17">3</text>
    <rect x="535" y="411" width="117" height="43" rx="6" fill="#4f46e5"/><text x="571" y="439" font-size="20" fill="white">{button}</text>
    <rect x="672" y="411" width="116" height="43" rx="6" fill="#f8fafc" stroke="#cbd5e1"/><text x="698" y="439" font-size="18">Cancel</text>
    <text x="26" y="501" font-size="12" fill="#607087">ILLUSTRATION · Layout and labels can vary by version.</text></g></svg>'''


def build_basics(root, out, header):
    target=out/'computer-basics'; target.mkdir()
    illustrations=out/'assets'/'basics'; illustrations.mkdir(exist_ok=True)
    cards=[]; toc=[]
    for n,lesson in enumerate(LESSONS,1):
        number=f'{n:02}'
        (illustrations/(lesson['id']+'.svg')).write_text(diagram(lesson))
        mac_image = ''
        if lesson['id'] in ('zip', 'extract'):
            mac = dict(lesson)
            mac['scene'] = ('Finder · Mac · illustration', 'Documents  >  My labs', ['Lab 01', 'Lab 01.zip'],
                            ['Control-click Lab 01', 'Compress “Lab 01”', 'Result: Lab 01.zip'] if lesson['id'] == 'zip' else
                            ['Double-click Lab 01.zip', 'Open the new Lab 01 folder', 'Work from this folder'])
            (illustrations/(lesson['id']+'-mac.svg')).write_text(diagram(mac))
            mac_image = f'<a class="mac-illustration" href="../assets/basics/{lesson["id"]}-mac.svg" target="_blank" rel="noopener" aria-label="Enlarge Mac illustration"><span>Mac · Finder</span><img src="../assets/basics/{lesson["id"]}-mac.svg" width="840" height="510" loading="lazy" alt="Mac Finder: {esc(". ".join(mac["scene"][3]))}"></a>'
        toc.append(f'<a class="toc-link" href="#{lesson["id"]}"><span>{number} · {esc(lesson["title"])}</span></a>')
        steps=''.join(f'<li><bdi class="step-label" dir="ltr">{esc(label)}</bdi><p>{body}</p></li>' for label,body in lesson['steps'])
        sources=''.join(f'<a href="{SOURCES[key][1]}" target="_blank" rel="noopener">{esc(SOURCES[key][0])} ↗</a>' for key in lesson['sources'])
        cards.append(f'''<article class="lesson-card" id="{lesson['id']}" aria-labelledby="title-{lesson['id']}">
          <div class="lesson-top"><span class="week-badge">{number} / {lesson['tag']}</span><h2 id="title-{lesson['id']}">{esc(lesson['title'])}</h2>
          <h3 lang="ar" dir="rtl">{lesson['ar']}</h3><p lang="ar" dir="rtl">{lesson['intro']}</p></div>
          <div class="lesson-body"><div class="lesson-instructions" lang="ar" dir="rtl"><ol>{steps}</ol></div>
          <figure class="lesson-figure"><a href="../assets/basics/{lesson['id']}.svg" target="_blank" rel="noopener" aria-label="Enlarge illustration: {esc(lesson['title'])}"><img src="../assets/basics/{lesson['id']}.svg" width="840" height="510" loading="lazy" alt="{esc(lesson['scene'][0]+'. '+'. '.join(lesson['scene'][3]))}"></a>{mac_image}<figcaption>Illustration · Tap to enlarge<span lang="ar" dir="rtl">رسم توضيحي مبسط — اضغط للتكبير</span></figcaption></figure></div>
          <p class="lesson-note" lang="ar" dir="rtl">{lesson['note']}</p><div class="lesson-sources">{sources}</div></article>''')
    styles=(root/'assets/style.css').read_text().replace('url("fonts/','url("../assets/fonts/')
    script=(root/'assets/navigation.js').read_text()
    contents=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Introduction to Basic Computer | Ahmed Tolan</title><meta name="description" content="A visual beginner guide to folders, copying files, saving C++ and Python code, and ZIP files on Windows and Mac. Simple Arabic explanations with English interface labels.">
    <meta name="theme-color" content="#f8fafc"><link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4.3.3"></script><style>{styles}</style></head><body>
    <a class="skip-link" href="#start">Skip to the guide</a>{header}<main>
    <section class="hero"><div class="hero-inner basics-hero"><div><div class="hero-meta"><span class="course-badge">COMPUTER BASICS</span><span>A visual reference</span></div>
    <h1>Introduction to<br>Basic Computer</h1><p class="basics-intro" lang="ar" dir="rtl">أول مرة تتعامل مع ملفات على الكمبيوتر؟ خدها خطوة خطوة.<br>ده مرجع بسيط يساعدك في اللاب، مش كورس إضافي ولا عليه تسليم.</p>
    <div class="basics-hero-actions"><a class="button button-primary" href="#start">Start with the basics ↓</a><a class="button button-secondary" href="#download">Find my lab files</a></div><p class="basics-platforms">Windows &amp; Mac · Arabic steps · English button names</p></div>
    <figure class="basics-cover"><img src="../assets/basics/files-and-folders.png" width="1536" height="1024" alt="Illustration of a laptop with a lab folder, C++ and Python files, and a ZIP archive."><figcaption>AI-generated illustration · رسم توضيحي مولّد</figcaption></figure></div></section>
    <div class="materials-layout basics-layout" id="guide"><aside class="week-sidebar"><nav class="week-nav" aria-label="Guide contents"><h2>Find a task</h2>{''.join(toc)}<p>Try one task at a time.<br>Keep this page beside you.</p></nav></aside>
    <div class="weekly-materials"><div class="basics-route"><b>Here for a lab?</b><span>Use this whenever you need it.</span><a href="../ece122/">ECE122 · Python ↗</a><a href="../gen241/">GEN241 · C++ ↗</a></div>{''.join(cards)}
    <div class="basics-return"><p lang="ar" dir="rtl">كده جاهز ترجع لملفات اللاب وتجرّب بنفسك.</p><a class="button button-secondary" href="../ece122/">ECE122 materials</a><a class="button button-secondary" href="../gen241/">GEN241 materials</a></div></div></div></main>
    <footer class="site-footer"><div class="footer-inner"><span>Ahmed Tolan · Teaching resources</span><span>Reference checked · 10 October 2026</span></div></footer><script>{script}</script></body></html>'''
    (target/'index.html').write_text(contents)
