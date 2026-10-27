(function(){
  'use strict';
  const $=id=>document.getElementById(id), DBKEY='db1-playground-db-v1', EDITKEY='db1-playground-editor-v1';
  let language='en',engine=null,entries=[],previous=null,storageOK=true,runSelection=false;
  const t=(en,ar)=>language==='ar'?isolateArabicLabel(ar):en;
  // Directional isolates keep English tokens and following Arabic punctuation apart.
  function isolateArabicLabel(text){
    return text.replace(/[A-Za-z0-9]+(?:[._/+\-–][A-Za-z0-9]+)*(?:(?:[ \t]+|[ \t]*[+=<>][ \t]*)[A-Za-z0-9]+(?:[._/+\-–][A-Za-z0-9]+)*)*/g,term=>'\u2066'+term+'\u2069');
  }
  const examples=[
    ['All copies','كل النسخ','SELECT *\nFROM BookCopies\nORDER BY CopyId;'],
    ['Available copies','النسخ المتاحة','SELECT CopyId, Title, Shelf\nFROM BookCopies\nWHERE IsAvailable = 1\nORDER BY CopyId;'],
    ['Two conditions','شرطين مع بعض',"SELECT CopyId, Title, Shelf\nFROM BookCopies\nWHERE Category = N'Computing'\n  AND IsAvailable = 1\nORDER BY CopyId;"],
    ['Current database','قاعدة البيانات الحالية','USE Database1Lab01;\nGO\nSELECT DB_NAME() AS CurrentDatabase;'],
    ['Create a wishlist · run once','إنشاء جدول رغبات · مرة واحدة','CREATE TABLE ReadingWishlist (\n    WishId INT PRIMARY KEY,\n    Title NVARCHAR(100) NOT NULL\n);'],
    ['Insert two wishes · run once','إضافة رغبتين · مرة واحدة',"INSERT INTO ReadingWishlist (WishId, Title)\nVALUES (1, N'Learning SQL');\n\nINSERT INTO ReadingWishlist (WishId, Title)\nVALUES (2, N'تصميم قواعد البيانات');"],
    ['Read the wishlist','قراءة جدول الرغبات','SELECT WishId, Title\nFROM ReadingWishlist\nORDER BY WishId;'],
    ['Try a duplicate key · after inserting','جرّب مفتاح متكرر · بعد الإضافة',"INSERT INTO ReadingWishlist (WishId, Title)\nVALUES (1, N'Another title');"],
    ['Try NULL · after creating','جرّب NULL · بعد إنشاء الجدول','INSERT INTO ReadingWishlist (WishId, Title)\nVALUES (3, NULL);']
  ];
  function get(key){try{return localStorage.getItem(key);}catch(e){storageOK=false;return null;}}
  function set(key,val){try{localStorage.setItem(key,val);return true;}catch(e){storageOK=false;return false;}}
  function notice(en,ar){$('notice').textContent=t(en,ar);$('notice').hidden=false;}
  function storageStatus(){
    $('storage').textContent=storageOK?t('Database and editor saved in this browser.','البيانات والكود محفوظين في المتصفح ده.'):t('Browser storage is unavailable. Changes last only until you close or reload this page. Save your SQL file.','تخزين المتصفح مش متاح. التغييرات هتضيع عند القفل أو إعادة التحميل. احفظ ملف SQL.');
  }
  function persist(){
    if(!engine)return;
    try{const bytes=engine.export();let s='';for(let i=0;i<bytes.length;i+=8192)s+=String.fromCharCode(...bytes.subarray(i,i+8192));set(DBKEY,btoa(s));}catch(e){storageOK=false;}
    set(EDITKEY,$('sql').value);storageStatus();
  }
  function setLanguage(lang){
    language=lang;document.documentElement.lang=lang==='ar'?'ar-EG':'en';document.documentElement.dir=lang==='ar'?'rtl':'ltr';
    document.querySelectorAll('[data-en]').forEach(el=>el.textContent=lang==='ar'?isolateArabicLabel(el.dataset.ar):el.dataset.en);
    $('en').setAttribute('aria-pressed',lang==='en');$('ar').setAttribute('aria-pressed',lang==='ar');set('db1-lab-language',lang);
    const selected=$('examples').value;$('examples').replaceChildren();examples.forEach((x,i)=>{const o=document.createElement('option');o.value=i;o.textContent=x[lang==='ar'?1:0];$('examples').append(o);});$('examples').value=selected||'0';
    if(engine){renderSchema();renderOutput();storageStatus();}
  }
  function loadSQL(sql){
    previous=$('sql').value;set(EDITKEY+'-previous',previous);$('undo').hidden=false;$('sql').value=sql;set(EDITKEY,sql);storageStatus();$('sql').focus();$('sql').setSelectionRange(0,0);
  }
  function renderSchema(){
    const target=$('schema');const openNames=new Set([...target.querySelectorAll('details[open]')].map(d=>d.dataset.name));target.replaceChildren();
    for(const table of engine.tables()){
      const d=document.createElement('details');d.dataset.name=table.name;d.open=table.name==='BookCopies'||openNames.has(table.name);
      const s=document.createElement('summary');const name=document.createElement('bdi');name.textContent=table.name;s.append(name);d.append(s);
      const ul=document.createElement('ul');table.columns.forEach(c=>{const li=document.createElement('li'),code=document.createElement('code'),type=document.createElement('span');code.textContent=c.name;type.className='column-type';type.textContent=' · '+c.type+' · '+(c.key?'PK · ':'')+(c.required?'NOT NULL':'NULL');li.append(code,type);ul.append(li);});d.append(ul);
      const b=document.createElement('button');b.textContent=t('Load SELECT','حمّل SELECT');b.onclick=()=>loadSQL('SELECT *\nFROM ['+table.name.replace(/]/g,']]')+'];');d.append(b);target.append(d);
    }
  }
  function tab(id){for(const name of ['results','messages']){$(name).hidden=name!==id;$(name+'-tab').setAttribute('aria-selected',name===id);$(name+'-tab').tabIndex=name===id?0:-1;}}
  function errorHint(error){
    if(/UNIQUE constraint failed/i.test(error))return t('That primary key is already used. Choose a new ID.','المفتاح الأساسي ده موجود. اختار ID جديد.');
    if(/NOT NULL constraint failed/i.test(error))return t('A required column is missing a value. NULL means no value.','عمود مطلوب ملوش قيمة. NULL معناها قيمة مش موجودة.');
    if(/CHECK constraint failed/i.test(error))return t('The value does not fit the column: check the whole-number range, text length, or BIT 0/1.','القيمة مش مناسبة للعمود. راجع مدى العدد الصحيح أو طول النص أو BIT صفر وواحد.');
    if(/already exists/i.test(error))return t('The table already exists. CREATE runs once; continue with INSERT or SELECT.','الجدول موجود. CREATE بيتشغّل مرة واحدة؛ كمّل INSERT أوSELECT.');
    return t('The statement did not run. Read the detail below and check your SQL.','الأمر ده ما اتنفّذش. اقرأ التفاصيل وراجع SQL.');
  }
  function renderOutput(){
    $('results').replaceChildren();$('messages').replaceChildren();let sets=0,total=0,hasError=false;
    entries.forEach((entry,i)=>{
      const li=document.createElement('div');li.className='message';
      if(entry.error){hasError=true;li.className='message error';li.textContent=t('Statement ','الأمر ')+(i+1)+': '+errorHint(entry.error);const raw=document.createElement('span');raw.className='raw-error';raw.textContent=entry.error;li.append(raw);}
      else li.textContent=t('Statement ','الأمر ')+(i+1)+': '+(language==='ar'?(entry.columns?entry.total+' صف رجع.':entry.affected!==undefined?entry.affected+' صف اتضاف.':entry.changed?'الجدول اتعمل بنجاح.':entry.message.startsWith('No statement')?'مفيش أمر للتشغيل. اكتب query الأول.':'قاعدة التدريب الحالية: Database1Lab01.'):entry.message);
      $('messages').append(li);
      if(!entry.columns)return;sets++;total+=entry.total;
      const container=document.createElement('div');container.className='result';const label=document.createElement('div');label.className='result-label';label.textContent=t('Statement ','الأمر ')+(i+1)+' · '+entry.total+t(' row(s)',' صف')+(entry.truncated?t(' · first 500 shown',' · أول 500 صف بس'):'');container.append(label);
      const wrap=document.createElement('div');wrap.className='grid';wrap.tabIndex=0;wrap.setAttribute('role','region');wrap.setAttribute('aria-label',t('Query result table','جدول نتيجة الاستعلام'));
      const table=document.createElement('table'),head=document.createElement('thead'),tr=document.createElement('tr');entry.columns.forEach(c=>{const th=document.createElement('th');th.scope='col';th.textContent=c;tr.append(th);});head.append(tr);table.append(head);
      const body=document.createElement('tbody');entry.rows.forEach(row=>{const tr=document.createElement('tr');row.forEach(v=>{const td=document.createElement('td');td.textContent=v===null?'NULL':v;if(v===null)td.className='null';tr.append(td);});body.append(tr);});table.append(body);wrap.append(table);container.append(wrap);
      if(!entry.total){const empty=document.createElement('div');empty.className='empty';empty.textContent=t('No rows match. The table still exists; this query returned an empty result.','مفيش صفوف مطابقة. الجدول لسه موجود؛ الاستعلام ده رجّع نتيجة فاضية.');container.append(empty);}
      $('results').append(container);
    });
    if(!sets){const empty=document.createElement('p');empty.className='empty';empty.textContent=t('Run a SELECT to see rows here. CREATE and INSERT report in Messages.','شغّل SELECT عشان تشوف صفوف هنا. CREATE وINSERT بتظهر رسائلهم في الرسائل.');$('results').append(empty);}
    $('summary').textContent=hasError?t('Stopped at an error','وقف عند خطأ'):total+t(' row(s) returned',' صف رجع');
    if(runSelection)$('summary').textContent+=' · '+t('selection','الجزء المحدد');
  }
  function run(){
    if(!engine)return;const el=$('sql');runSelection=el.selectionStart!==el.selectionEnd;const source=runSelection?el.value.slice(el.selectionStart,el.selectionEnd):el.value;
    entries=engine.run(source);persist();renderSchema();renderOutput();tab(entries.some(e=>e.error)||!entries.some(e=>e.columns)?'messages':'results');
  }
  $('run').onclick=run;$('sql').addEventListener('keydown',e=>{if((e.metaKey||e.ctrlKey)&&e.key==='Enter'){e.preventDefault();run();}});
  $('sql').addEventListener('input',()=>{set(EDITKEY,$('sql').value);storageStatus();});
  $('load').onclick=()=>loadSQL(examples[+$('examples').value][2]);
  $('undo').onclick=()=>{if(previous!==null){const current=$('sql').value;$('sql').value=previous;previous=current;set(EDITKEY,$('sql').value);set(EDITKEY+'-previous',previous);}};
  $('en').onclick=()=>setLanguage('en');$('ar').onclick=()=>setLanguage('ar');
  $('results-tab').onclick=()=>tab('results');$('messages-tab').onclick=()=>tab('messages');
  document.querySelector('.tabs').addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight','Home','End'].includes(e.key)){e.preventDefault();const target=e.key==='Home'?'results':e.key==='End'?'messages':$('results').hidden?'results':'messages';tab(target);$(target+'-tab').focus();}});
  $('helpLink').onclick=()=>{$('help').open=true;};
  $('reset').onclick=()=>{
    if(!confirm(t('Remove all practice tables and restore the six book copies? Your SQL text will stay.','تمسح كل جداول التدريب وترجع نسخ الكتب الستة؟ الكود المكتوب هيفضل موجود.')))return;
    engine.reset();entries=engine.run(examples[0][2]);runSelection=false;$('notice').hidden=true;persist();renderSchema();renderOutput();tab('results');
  };
  $('download').onclick=()=>{const url=URL.createObjectURL(new Blob([$ ('sql').value],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='database1-lab01.sql';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
  async function start(){
    setLanguage(get('db1-lab-language')==='ar'?'ar':'en');$('sql').value=get(EDITKEY)??examples[0][2];previous=get(EDITKEY+'-previous');$('undo').hidden=previous===null;
    try{
      const SQL=await initSqlJs();const saved=get(DBKEY);let recovered=false;
      if(saved){try{const bytes=Uint8Array.from(atob(saved),c=>c.charCodeAt(0));engine=new LabSQL.Engine(SQL,bytes);engine.known('BookCopies');engine.tables();}catch(e){engine=null;recovered=true;set(DBKEY+'-recovery',saved);notice('The saved database could not be read. A recovery copy was kept in browser storage where available; the six starter rows have been restored.','قاعدة البيانات المحفوظة ما اتقريتش. اتحفظت نسخة للاسترجاع في المتصفح لو التخزين متاح، وبدأنا بالصفوف الستة.');}}
      if(!engine)engine=new LabSQL.Engine(SQL);persist();
      entries=engine.run(examples[0][2]);renderSchema();renderOutput();$('run').disabled=false;$('reset').disabled=false;
    }catch(e){notice('Could not start the SQL engine. Keep playground.html beside its assets folder and open the file in a browser. Detail: '+e.message,'محرك SQL ما اشتغلش. خلّي playground.html جنب فولدر assets وافتح الملف في المتصفح. التفاصيل: '+e.message);}
  }
  start();
})();
