/* Database 1 lab adapter. SQLite executes queries; this parser bounds the teaching dialect. */
(function (root) {
  'use strict';
  const NAME = 'Database1Lab01';
  const FIXTURE = [
    [101,'Python Basics','Computing','A1',1], [102,'Python Basics','Computing','A1',0],
    [103,'Database Design','Computing','A2',1], [104,'Intro to Circuits','Engineering','B1',1],
    [105,'Applied Mathematics','Mathematics','C1',0], [106,'Database Design','Computing','A2',0]
  ];
  const q = s => '"' + s.replace(/"/g, '""') + '"';
  const fail = s => { throw new Error(s); };
  function lex(s) {
    if (s.length > 50000) fail('Keep each run below 50,000 characters.');
    let i = 0, out = [];
    while (i < s.length) {
      if (/\s/.test(s[i])) { i++; continue; }
      if (s.startsWith('--',i)) { while (i<s.length && s[i]!=='\n') i++; continue; }
      if (s.startsWith('/*',i)) {
        i+=2; let depth=1;
        while(i<s.length && depth) {
          if(s.startsWith('/*',i)){depth++;i+=2;}
          else if(s.startsWith('*/',i)){depth--;i+=2;}
          else i++;
        }
        if(depth) fail('Unclosed /* comment.');
        continue;
      }
      // GO is a client separator only when it occupies its own line.
      if (/^GO\b/i.test(s.slice(i)) && /^[ \t\r]*$/.test(s.slice(s.lastIndexOf('\n',i-1)+1,i)) &&
          /^GO[ \t\r]*(?:--[^\n]*)?(?:\n|$)/i.test(s.slice(i))) {
        const m=s.slice(i).match(/^GO[ \t\r]*(?:--[^\n]*)?(?:\n|$)/i)[0];
        out.push({k:'sym',v:';'});i+=m.length;continue;
      }
      if ((s[i]==='N'||s[i]==='n') && s[i+1]==="'") i++;
      if(s[i]==="'") {
        let v='',closed=false;i++;
        while(i<s.length){if(s[i]==="'"){if(s[i+1]==="'"){v+="'";i+=2;}else{i++;closed=true;break;}}else v+=s[i++];}
        if(!closed)fail('Unclosed text literal. Put text between single quotes.');
        out.push({k:'str',v});continue;
      }
      if(s[i]==='['||s[i]==='"') {
        const end=s[i]==='['?']':'"';let v='',closed=false;i++;
        while(i<s.length){if(s[i]===end){if(s[i+1]===end){v+=end;i+=2;}else{i++;closed=true;break;}}else v+=s[i++];}
        if(!closed)fail('Unclosed quoted identifier.');
        out.push({k:'id',v});continue;
      }
      const word=s.slice(i).match(/^[A-Za-z_][A-Za-z_0-9]*/);
      if(word){out.push({k:'word',v:word[0]});i+=word[0].length;continue;}
      const num=s.slice(i).match(/^\d+(?:\.\d+)?/);
      if(num){out.push({k:'num',v:num[0]});i+=num[0].length;continue;}
      const op=s.slice(i).match(/^(?:>=|<=|<>|!=|[(),;.*=<>+-])/);
      if(op){out.push({k:'sym',v:op[0]});i+=op[0].length;continue;}
      fail('Unsupported character: '+s[i]+'. This playground covers the Lab 1 SQL subset.');
    }
    return out;
  }
  class Parser {
    constructor(tokens){this.t=tokens;this.i=0;}
    is(s){const t=this.t[this.i];return !!t && t.k!=='str' && t.k!=='id' && t.v.toUpperCase()===s.toUpperCase();}
    take(s){if(this.is(s)){this.i++;return true;}return false;}
    need(s){if(!this.take(s))fail('Expected '+s+' near '+(this.t[this.i]?.v||'the end')+'.');}
    ident(){const t=this.t[this.i++];if(!t||!['word','id'].includes(t.k))fail('Expected a column or table name.');return t.v;}
    table(){let n=this.ident();if(this.take('.')){if(n.toLowerCase()!=='dbo')fail('Only the dbo schema is available here.');n=this.ident();}if(n.toLowerCase().startsWith('sqlite_'))fail('Internal engine tables are outside this lab.');return n;}
    end(){if(this.i!==this.t.length)fail('Unsupported syntax near '+this.t[this.i].v+'. Use SELECT, CREATE TABLE or INSERT from this lab. End separate statements with a semicolon.');}
    literal(){
      if(this.take('NULL'))return 'NULL';
      let sign='';if(this.take('-'))sign='-';else this.take('+');
      const t=this.t[this.i++];
      if(t?.k==='num')return sign+t.v;
      if(t?.k==='str'&&!sign)return "'"+t.v.replace(/'/g,"''")+"'";
      fail('INSERT values must be numbers, quoted text, or NULL in this playground.');
    }
  }
  class Engine {
    constructor(SQL,bytes){this.SQL=SQL;this.db=new SQL.Database(bytes);this.functions();if(!bytes)this.seed();}
    functions(){this.db.create_function('lab_utf16_length',s=>s==null?null:String(s).length);this.db.create_function('DB_NAME',()=>NAME);}
    seed(){
      this.execute(lex('CREATE TABLE dbo.BookCopies (CopyId INT PRIMARY KEY, Title NVARCHAR(100) NOT NULL, Category NVARCHAR(40) NOT NULL, Shelf NVARCHAR(10) NOT NULL, IsAvailable BIT NOT NULL)'));
      for(const row of FIXTURE)this.db.run('INSERT INTO BookCopies VALUES (?,?,?,?,?)',row);
    }
    reset(){this.db.close();this.db=new this.SQL.Database();this.functions();this.seed();}
    export(){const bytes=this.db.export();this.functions();return bytes;}
    tables(){return this.db.exec("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")[0]?.values.map(r=>({name:r[0],columns:this.columns(r[0])}))||[];}
    columns(table){
      const definition=this.db.exec('SELECT sql FROM sqlite_master WHERE type = ? AND name = ? COLLATE NOCASE',['table',table])[0]?.values[0][0]||'';
      return this.db.exec('PRAGMA table_info('+q(table)+')')[0]?.values.map(r=>{
        let type=r[2];const col=q(r[1]);
        const lengthStart=definition.indexOf('lab_utf16_length('+col+') <= ');
        if(type==='TEXT'&&lengthStart>=0){const tail=definition.slice(lengthStart+('lab_utf16_length('+col+') <= ').length);type='NVARCHAR('+tail.match(/^\d+/)[0]+')';}
        if(type==='INT'&&definition.includes(col+' IN (0,1)'))type='BIT';
        return {name:r[1],type,required:!!r[3],key:!!r[5]};
      })||[];
    }
    known(table){const cols=this.columns(table);if(!cols.length)fail('Table '+table+' does not exist. Run CREATE TABLE first, or check the table name.');return cols;}
    column(name,cols){if(!cols.some(c=>c.name.toLowerCase()===name.toLowerCase()))fail('Unknown column '+name+'. Check the table columns on the left.');return q(name);}
    run(source){
      let tokens;try{tokens=lex(source);}catch(e){return [{error:e.message}];}
      const batches=[[]];for(const t of tokens){if(t.k==='sym'&&t.v===';'){if(batches.at(-1).length)batches.push([]);}else batches.at(-1).push(t);}
      const entries=[];
      for(const t of batches){if(!t.length)continue;try{entries.push(this.execute(t));}catch(e){entries.push({error:e.message});break;}}
      if(!entries.length)entries.push({message:'No statement to run. Type a query first.'});return entries;
    }
    execute(tokens){
      const p=new Parser(tokens);
      if(p.take('USE')){const n=p.ident();p.end();if(n.toLowerCase()!==NAME.toLowerCase())fail('Only '+NAME+' exists in this playground.');return {message:'Current practice database: '+NAME+'.'};}
      if(p.take('SELECT'))return this.select(p);
      if(p.take('CREATE'))return this.create(p);
      if(p.take('INSERT'))return this.insert(p);
      fail('This playground supports SELECT, CREATE TABLE, INSERT, USE '+NAME+' and GO. This command needs SQL Server or a later lab.');
    }
    create(p){
      p.need('TABLE');const table=p.table();if(this.tables().length>=32)fail('Practice limit: 32 tables. Reset the playground to start again.');
      p.need('(');let defs=[],keys=0;
      do {
        const name=p.ident(), col=q(name);let type,checks=[],required=false,key=false;
        if(p.take('INT')||p.take('INTEGER')){type='INT';checks.push('('+col+' IS NULL OR (typeof('+col+") = 'integer' AND "+col+' BETWEEN -2147483648 AND 2147483647))');}
        else if(p.take('BIT')){type='INT';checks.push('('+col+' IS NULL OR (typeof('+col+") = 'integer' AND "+col+' IN (0,1)))');}
        else if(p.take('NVARCHAR')){
          p.need('(');const t=p.t[p.i++];if(t?.k!=='num'||!/^\d+$/.test(t.v)||+t.v<1||+t.v>4000)fail('Use NVARCHAR(n) with n from 1 to 4000.');p.need(')');
          type='TEXT';checks.push('('+col+' IS NULL OR (typeof('+col+") = 'text' AND lab_utf16_length("+col+') <= '+t.v+'))');
        }else fail('Use INT, BIT or NVARCHAR(n) for Lab 1 columns.');
        while(!p.is(',')&&!p.is(')')){
          if(p.take('PRIMARY')){p.need('KEY');key=true;required=true;keys++;}
          else if(p.take('NOT')){p.need('NULL');required=true;}
          else if(p.take('NULL')){if(key)fail('A primary key cannot be nullable.');}
          else fail('Supported column rules: PRIMARY KEY and NOT NULL.');
        }
        if(keys>1)fail('Use one PRIMARY KEY column in this lab.');
        defs.push(col+' '+type+(required?' NOT NULL':'')+(key?' PRIMARY KEY':'')+' CHECK ('+checks.join(' AND ')+')');
        if(defs.length>20)fail('Practice limit: 20 columns per table.');
      }while(p.take(','));p.need(')');p.end();
      this.db.run('CREATE TABLE '+q(table)+' ('+defs.join(',')+')');
      return {message:'Table '+table+' created. It is empty until you INSERT rows.',changed:true};
    }
    insert(p){
      p.need('INTO');const table=p.table(),cols=this.known(table);let list='';
      if(p.take('(')){const names=[];do{names.push(this.column(p.ident(),cols));}while(p.take(','));p.need(')');list=' ('+names.join(',')+')';}
      p.need('VALUES');const rows=[];
      do{p.need('(');const vals=[];do{vals.push(p.literal());}while(p.take(','));p.need(')');rows.push('('+vals.join(',')+')');}while(p.take(','));p.end();
      const count=this.db.exec('SELECT COUNT(*) FROM '+q(table))[0].values[0][0];
      if(count+rows.length>5000)fail('Practice limit: 5,000 rows per table.');
      this.db.run('INSERT INTO '+q(table)+list+' VALUES '+rows.join(','));
      return {message:this.db.getRowsModified()+' row(s) inserted.',affected:this.db.getRowsModified(),changed:true};
    }
    select(p){
      const distinct=p.take('DISTINCT');const projections=[];let dbname=false;
      do{
        let c;
        if(p.take('*'))c={star:true};
        else if(p.take('DB_NAME')){p.need('(');p.need(')');c={fn:true};dbname=true;}
        else c={name:p.ident()};
        if(p.take('AS'))c.alias=p.ident();
        projections.push(c);
      }while(p.take(','));
      let table=null,cols=[];
      if(p.take('FROM')){table=p.table();cols=this.known(table);}
      else if(!dbname||projections.some(c=>!c.fn))fail('SELECT columns needs FROM followed by a table name.');
      const project=projections.map(c=>(c.star?'*':c.fn?'DB_NAME()':this.column(c.name,cols))+(c.alias?' AS '+q(c.alias):'')).join(',');
      let sql='SELECT '+(distinct?'DISTINCT ':'')+project+(table?' FROM '+q(table):'');
      const operand=()=>{
        const t=p.t[p.i];
        if(t && (t.k==='str'||t.k==='num'||p.is('-')||p.is('+')||p.is('NULL')))return p.literal();
        return this.column(p.ident(),cols);
      };
      let depth=0;
      const atom=()=>{
        if(++depth>40)fail('Too many nested conditions.');
        let s;
        if(p.take('NOT'))s='NOT '+atom();
        else if(p.take('(')){s='('+or()+')';p.need(')');}
        else{
          s=operand();
          if(p.take('IS')){s+=' IS '+(p.take('NOT')?'NOT ':'');p.need('NULL');s+='NULL';}
          else if(p.take('LIKE'))s+=' LIKE '+operand();
          else{const t=p.t[p.i++];if(t?.k!=='sym'||!['=','!=','<>','<','>','<=','>='].includes(t.v))fail('Use a comparison such as IsAvailable = 1.');s+=' '+t.v+' '+operand();}
        }
        depth--;return s;
      };
      const and=()=>{let s=atom();while(p.take('AND'))s+=' AND '+atom();return s;};
      const or=()=>{let s=and();while(p.take('OR'))s+=' OR '+and();return s;};
      if(p.take('WHERE'))sql+=' WHERE '+or();
      if(p.take('ORDER')){
        p.need('BY');const terms=[];
        do{const n=p.ident(),alias=projections.some(c=>c.alias?.toLowerCase()===n.toLowerCase());let c=alias?q(n):this.column(n,cols);if(p.take('ASC'))c+=' ASC';else if(p.take('DESC'))c+=' DESC';terms.push(c);}while(p.take(','));
        sql+=' ORDER BY '+terms.join(',');
      }
      p.end();const stmt=this.db.prepare(sql);let columns,rows=[],total=0;
      try{columns=stmt.getColumnNames();while(stmt.step()){total++;if(rows.length<500)rows.push(stmt.get());}}finally{stmt.free();}
      return {columns,rows,total,truncated:total>rows.length,message:total+' row(s) returned.'};
    }
  }
  const api={Engine,lex,NAME};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.LabSQL=api;
})(typeof window==='undefined'?globalThis:window);
