/* ECE122 Guide: one page per question, in the order a novice needs it.
   What the question says → predict (optional) → on the board → plan → write →
   run the recorded program → on your own. Every section is reachable at any
   time; only answers (model plan lines, code, recorded run, explanations) wait
   until the learner asks for them, and asking never marks a question practised. */
(() => {
'use strict';
const D = window.LEARNING_DATA, S = D.sheet;
const KEY = 'ece122-sheet' + S + '-learning-v2', OLD = 'ece122-sheet' + S + '-learning-v1', UIKEY = KEY + '-ui';
const FIELDS = ['have', 'want', 'plan', 'predict', 'explain', 'changed', 'mistake', 'run'];
const EVIDENCE = ['explain', 'changed', 'mistake', 'run'];
const REVEALS = ['trace', 'code', 'bug', 'transfer'];
const PLANKEYS = ['WANT', 'HAVE', 'CONVERT', 'RELATE', 'CHECK'];
const A = document.getElementById('app');
let lang = 'ar', n = 1, dirty = false, notice = '';
let ui = {};          // per question: {board, steps:{}, variant:{}, ci, fi, mine:{}}
const B = (ar, en) => lang === 'ar' ? ar : en, T = v => v == null ? '' : typeof v === 'string' ? v : (v[lang] != null ? v[lang] : v.en);
const esc = s => String(s).replace(/[&<>"']/g, k => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[k]));

/* ---------- records ---------- */
function blankQ() { return { fields: Object.fromEntries(FIELDS.map(k => [k, ''])), practised: false, reveals: [], predict: null, planShown: [], blocksShown: 0 }; }
function blank() { return { app: KEY, version: 2, sourceHash: D.sourceHash, savedAt: new Date().toISOString(), questions: Object.fromEntries(D.lessons.map(q => [q.n, blankQ()])) }; }
function validate(o) {
  if (!o || o.app !== KEY || o.version !== 2 || o.sourceHash !== D.sourceHash || !Number.isFinite(Date.parse(o.savedAt)) || Object.keys(o.questions || {}).length !== D.lessons.length) throw Error('Wrong workbook, source or schema');
  for (const q of D.lessons) {
    const r = o.questions[q.n];
    if (!r || !r.fields || Object.keys(r.fields).length !== FIELDS.length || !FIELDS.every(k => typeof r.fields[k] === 'string' && r.fields[k].length <= 20000)) throw Error('Invalid question record');
    if (typeof r.practised !== 'boolean' || !Array.isArray(r.reveals) || !r.reveals.every(x => REVEALS.includes(x))) throw Error('Invalid question record');
    if (!(r.predict === null || (Number.isInteger(r.predict) && r.predict >= 0 && r.predict < q.predict.opts.length))) throw Error('Invalid prediction');
    if (!Array.isArray(r.planShown) || !r.planShown.every(k => PLANKEYS.includes(k)) || !Number.isInteger(r.blocksShown) || r.blocksShown < 0 || r.blocksShown > q.blocks.length) throw Error('Invalid reveal state');
    if (r.practised && EVIDENCE.some(k => !r.fields[k].trim())) throw Error('Missing independent practice evidence');
  }
  return o;
}
/* Version 1 records (the six-tab Guide) carry over: same eight fields, same
   evidence rule. Hint counts have no place in the new layout and are dropped. */
function migrate(o) {
  if (!o || o.app !== OLD || o.version !== 1 || o.sourceHash !== D.sourceHash || typeof o.questions !== 'object') throw Error('Not a version 1 record for this sheet');
  const out = blank();
  out.migratedFrom = 'v1';
  for (const q of D.lessons) {
    const r = o.questions[q.n];
    if (!r || !r.fields) continue;
    const t = out.questions[q.n];
    for (const k of FIELDS) if (typeof r.fields[k] === 'string') t.fields[k] = r.fields[k].slice(0, 20000);
    t.reveals = Array.isArray(r.reveals) ? r.reveals.filter(x => ['trace', 'code', 'bug'].includes(x)) : [];
    if (t.reveals.includes('code')) t.blocksShown = q.blocks.length;
    t.practised = r.practised === true && EVIDENCE.every(k => t.fields[k].trim());
  }
  return validate(out);
}
function readAny(text) { const o = JSON.parse(text); return o && o.version === 1 ? migrate(o) : validate(o); }
const get = k => { try { return localStorage.getItem(k); } catch { return null; } };
const put = (k, v) => { try { localStorage.setItem(k, v); return localStorage.getItem(k) === v; } catch { return false; } };

let record = blank();
try {
  if (get(KEY)) record = validate(JSON.parse(get(KEY)));
  else if (get(OLD)) { record = migrate(JSON.parse(get(OLD))); if (put(KEY, JSON.stringify(record))) notice = 'migrated'; }
} catch (e) { notice = 'unreadable'; }
try {
  const u = JSON.parse(get(UIKEY) || '{}');
  if (['ar', 'en'].includes(u.lang)) lang = u.lang;
  if (u.n === 0 || D.lessons.some(q => q.n === u.n)) n = u.n;
  if (u.q && typeof u.q === 'object') ui = u.q;
} catch {}
const hashN = (location.hash.match(/^#q(\d+)$/) || [])[1];
if (hashN !== undefined && (+hashN === 0 || D.lessons.some(q => q.n === +hashN))) n = +hashN;

const Q = () => D.lessons.find(q => q.n === n), R = () => record.questions[n];
function U() { const k = String(n); if (!ui[k] || typeof ui[k] !== 'object') ui[k] = {}; const u = ui[k]; u.steps = u.steps || {}; u.variant = u.variant || {}; u.mine = u.mine || {}; u.board = Number.isInteger(u.board) ? u.board : 0; u.ci = Number.isInteger(u.ci) ? u.ci : 0; u.fi = Number.isInteger(u.fi) ? u.fi : 0; return u; }
function saveUI() { put(UIKEY, JSON.stringify({ lang, n, q: ui })); }
function mark() { dirty = true; record.savedAt = new Date().toISOString(); put(KEY + '-draft', JSON.stringify(record)); status(); }
function status() { const e = document.getElementById('status'); if (e) e.textContent = dirty ? B('تعديلات مش محفوظة', 'Unsaved changes') : B('السجل محفوظ على المتصفح ده', 'Record saved in this browser'); }
function save() {
  const old = get(KEY);
  if (old && !put(KEY + '-snapshot', old)) return statusFail();
  record.savedAt = new Date().toISOString();
  if (put(KEY, JSON.stringify(validate(record)))) { dirty = false; put(KEY + '-draft', JSON.stringify(record)); document.getElementById('status').textContent = B('اتحفظ واتقرا تاني', 'Saved and read back'); }
  else statusFail();
}
function statusFail() { document.getElementById('status').textContent = B('التخزين مش متاح: نزّل نسخة JSON', 'Storage unavailable: export JSON'); }
function reveal(k) { if (!R().reveals.includes(k)) R().reveals.push(k); mark(); }

/* ---------- DOM helpers ---------- */
function h(tag, attrs, ...kids) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) { if (v == null || v === false) continue; if (k.startsWith('on')) e.addEventListener(k.slice(2), v); else if (k === 'html') e.innerHTML = v; else e.setAttribute(k, v === true ? '' : v); }
  for (const v of kids.flat(Infinity)) if (v !== null && v !== undefined && v !== false) e.append(v.nodeType ? v : document.createTextNode(String(v)));
  return e;
}
const btn = (label, fn, cl = '', attrs = {}) => h('button', Object.assign({ type: 'button', class: cl, onclick: fn }, attrs), label);
const P = (t, cl) => h('p', cl ? { class: cl } : {}, t);
const html = (tag, s, cl) => h(tag, { class: cl, html: s });
function dialog(title) { const d = h('dialog', { class: 'dlg' }, h('h2', {}, title)); d.append(btn(B('إغلاق', 'Close'), () => d.close(), 'ghost')); document.body.append(d); d.addEventListener('close', () => d.remove()); d.showModal(); return d; }
function download(name, text, type = 'application/json') { const url = URL.createObjectURL(new Blob([text], { type })); const a = h('a', { href: url, download: name }); document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000); }

/* ---------- source pane with highlights ---------- */
let activeMark = null;
function setMark(id) {
  activeMark = id || null;
  document.querySelectorAll('.src-mark').forEach(m => m.classList.toggle('on', m.dataset.mark === activeMark));
  const first = document.querySelector('.src-mark.on');
  const pane = document.querySelector('.src-scroll');
  if (first && pane) { const r = first.getBoundingClientRect(), pr = pane.getBoundingClientRect(); if (r.top < pr.top || r.bottom > pr.bottom) pane.scrollTop += r.top - pr.top - 40; }
}
function sourcePane() {
  const q = Q();
  const box = h('div', { class: 'src-scroll' });
  q.sourceParts.forEach(part => {
    const fig = h('figure', { class: 'src-fig' });
    const wrap = h('div', { class: 'src-img', role: 'button', tabindex: '0', title: B('كبّر', 'Enlarge'), onclick: () => { const d = dialog('Sheet ' + S + ' · Q' + q.n); const big = wrap.cloneNode(true); big.classList.add('big'); d.append(big); } },
      h('img', { src: part.image, alt: 'Sheet ' + S + ' Q' + q.n + ', PDF page ' + part.page }));
    for (const [id, rects] of Object.entries(part.marks)) rects.forEach(r => wrap.append(h('span', { class: 'src-mark', 'data-mark': id, style: `left:${r[0] * 100}%;top:${r[1] * 100}%;width:${(r[2] - r[0]) * 100}%;height:${(r[3] - r[1]) * 100}%` })));
    fig.append(h('figcaption', {}, 'PDF ' + B('ص ', 'p. ') + part.page, ' ', btn(B('الصفحة كاملة', 'Full page'), () => { const d = dialog('Sheet ' + S + ' · PDF ' + part.page); d.append(h('img', { src: 'assets/page-' + part.page + '.png', alt: 'Full page ' + part.page, class: 'fullpage' })); }, 'small')), wrap);
    box.append(fig);
  });
  return h('aside', { class: 'source', 'aria-label': B('السؤال الأصلي', 'Original question') },
    h('div', { class: 'src-head' }, h('b', {}, B('السؤال الأصلي', 'Original question')), h('span', { class: 'muted' }, 'Sheet ' + S + ' · Q' + q.n)),
    box,
    h('p', { class: 'src-links' }, h('a', { href: 'sheet-' + String(S).padStart(2, '0') + '.pdf', target: '_blank' }, B('الشيت الأصلي PDF', 'Original sheet PDF')),
      D.lecture ? h('a', { href: D.lecture.file, target: '_blank' }, B('محاضرة 4 PDF', 'Lecture 4 PDF')) : null),
    h('p', { class: 'muted small' }, B('الإطار البرتقالي بيوري الجزء اللي بنشرحه دلوقتي.', 'The orange frame shows the part being explained right now.')));
}

/* ---------- the board ---------- */
function boardSection(boards, title, sid) {
  const u = U();
  const sec = h('section', { id: sid, class: 'sec' }, h('h3', {}, title));
  const host = h('div', { class: 'board-host' });
  sec.append(host);
  function paint() {
    host.replaceChildren();
    const bi = Math.min(u.board, boards.length - 1);
    let b = boards[bi];
    const pickBoard = i => { u.board = i; saveUI(); paint(); host.scrollIntoView({ block: 'start' }); };
    if (boards.length > 4) {
      /* A long sequence (the primer): one board at a time, grouped by topic, never a wall of tabs. */
      const sel = h('select', { 'aria-label': B('اختار سبورة', 'Choose a board'), onchange: e => pickBoard(+e.target.value) });
      let group = null, last = null;
      boards.forEach((x, i) => { const g = T(x.sectionTitle); if (g !== last) { group = h('optgroup', { label: g }); sel.append(group); last = g; } group.append(h('option', { value: i }, (i + 1) + '. ' + T(x.title))); });
      sel.value = String(bi);
      host.append(h('div', { class: 'board-nav' }, btn('◀ ' + B('السبورة اللي قبلها', 'Previous board'), () => pickBoard(bi - 1), 'ghost', { disabled: bi === 0 }), sel,
        h('span', { class: 'muted count' }, (bi + 1) + ' / ' + boards.length), btn(B('السبورة اللي بعدها', 'Next board') + ' ▶', () => pickBoard(bi + 1), 'ghost', { disabled: bi === boards.length - 1 })));
    } else if (boards.length > 1) host.append(h('div', { class: 'chips', role: 'tablist' }, boards.map((x, i) => btn((i + 1) + '. ' + T(x.title), () => pickBoard(i), 'chip', { 'aria-pressed': String(i === bi), role: 'tab' }))));
    if (b.variants) {
      const vi = u.variant[b.id] != null ? u.variant[b.id] : 2;
      host.append(h('div', { class: 'chips' }, h('span', { class: 'muted' }, B('اختار حالة: ', 'Choose a case: ')), b.variants.map((v, i) => btn(T(v.label), () => { u.variant[b.id] = i; saveUI(); paint(); }, 'chip', { 'aria-pressed': String(i === vi) }))));
      b = Object.assign({}, b, { sketch: b.variants[vi].sketch, rows: b.variants[vi].rows });
    }
    if (b.cite) host.append(h('p', { class: 'cite' }, h('a', { href: '../' + b.cite.file + '#page=' + b.cite.page, target: '_blank' }, T(b.cite.t))));
    const el = Board.build(b, lang, 'guide');
    const N = Board.steps(b);
    let k = Math.min(u.steps[b.id] != null ? u.steps[b.id] : 0, N);
    const mine = u.mine[b.id];
    el.addEventListener('click', e => { const o = e.target.closest('.wb-opt'); if (!o) return; u.mine[b.id] = +o.dataset.n; saveUI(); el.querySelectorAll('.wb-opt').forEach((x, i) => x.classList.toggle('wb-mine', i === +o.dataset.n)); });
    if (mine != null) el.querySelectorAll('.wb-opt').forEach((x, i) => x.classList.toggle('wb-mine', i === mine));
    const list = h('ol', { class: 'steps' });
    const back = btn('◀ ' + B('خطوة لورا', 'Back'), () => go(k - 1), 'ghost');
    const next = btn('', () => go(k + 1), 'primary');
    const reset = btn(B('امسح السبورة', 'Wipe the board'), () => go(0), 'ghost');
    const count = h('span', { class: 'muted count' });
    function go(x) {
      k = Math.max(0, Math.min(N, x));
      u.steps[b.id] = k; saveUI();
      Board.set(el, k, false);
      back.disabled = k === 0; next.disabled = k === N;
      next.textContent = k < N ? B('التالي: ', 'Next: ') + stripTags(T(b.steps[k].ask)) + ' ▶' : B('السبورة اكتملت', 'Board complete');
      count.textContent = B('خطوة ', 'step ') + k + ' / ' + N;
      list.querySelectorAll('li').forEach((li, i) => { li.classList.toggle('done', i < k); li.classList.toggle('now', i === k - 1); });
      const src = k > 0 ? b.steps[k - 1].src : null;
      setMark(src);
    }
    b.steps.forEach((st, i) => list.append(h('li', {}, btn((st.vote ? '🗳 ' : '') + stripTags(T(st.ask)), () => go(i + 1), 'linklike'))));
    el.addEventListener('keydown', e => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); const fwd = (e.key === 'ArrowRight') !== (lang === 'ar'); go(k + (fwd ? 1 : -1)); } });
    el.tabIndex = 0;
    host.append(h('div', { class: 'board-frame' }, el), h('div', { class: 'board-controls' }, back, next, reset, count),
      h('details', { class: 'step-list' }, h('summary', {}, B('أسئلة السبورة دي (اضغط على أي سؤال)', 'This board’s questions (jump to any)')), list));
    go(k);
  }
  paint();
  return sec;
}
const stripTags = s => { const d = document.createElement('div'); d.innerHTML = s; return d.textContent; };

/* ---------- sections ---------- */
function field(k, label, rows = 3) {
  const t = h('textarea', { rows: String(rows), maxlength: '20000', dir: 'auto', id: 'field-' + k });
  t.value = R().fields[k];
  t.oninput = () => { R().fields[k] = t.value; if (EVIDENCE.includes(k) && R().practised) { R().practised = false; const c = document.getElementById('practised'); if (c) c.checked = false; } mark(); };
  return h('label', { class: 'field', for: 'field-' + k }, h('span', {}, label), t);
}
const SECTIONS = () => [
  ['sec-words', B('السؤال بيقول إيه', 'What the question says')], ['sec-predict', B('توقّع الأول (اختياري)', 'Predict first (optional)')],
  ['sec-board', B('على السبورة', 'On the board')], ['sec-plan', B('خطتك', 'Your plan')], ['sec-code', B('من الخطة للكود', 'From plan to code')],
  ['sec-run', B('تشغيل مسجّل', 'Recorded run')], ['sec-own', B('لوحدك', 'On your own')]];

function entry() {
  const go = id => () => { document.getElementById(id).scrollIntoView({ behavior: 'smooth', block: 'start' }); };
  return h('div', { class: 'entry' },
    btn(h('span', {}, h('b', {}, B('أول مرة تشوف الفكرة؟', 'Is the idea new to you?')), h('span', {}, B('ابدأ بالسبورة: رسم، وبعدين علاقة، وبعدين Python.', 'Start on the board: a drawing, then the relation, then Python.'))), go('sec-board'), 'card'),
    btn(h('span', {}, h('b', {}, B('فاهم الفكرة؟', 'Do you know the idea?')), h('span', {}, B('اكتب خطتك، وبعدين قارنها والكود جزء جزء.', 'Write your plan, then compare it and the code part by part.'))), go('sec-plan'), 'card'),
    btn(h('span', {}, h('b', {}, B('عندك برنامج؟', 'Have a program?')), h('span', {}, B('قارنه بتشغيل مسجّل وتمرين جديد.', 'Compare it with a recorded run and a new task.'))), go('sec-run'), 'card'));
}

function wordsSection() {
  const q = Q();
  const rows = q.words.map(w => h('tr', { tabindex: '0', onmouseenter: () => setMark(w.mark), onfocus: () => setMark(w.mark), onclick: () => setMark(w.mark) },
    h('td', { dir: 'ltr', class: 'phrase' }, '“' + w.phrase + '”'), h('td', {}, T(w.meaning)), h('td', { dir: 'ltr' }, w.name ? h('code', {}, w.name) : '—'), h('td', {}, T(w.unit))));
  return h('section', { id: 'sec-words', class: 'sec' }, h('h3', {}, B('السؤال بيقول إيه', 'What the question says')),
    P(B('مرّر على أي سطر عشان تشوف الكلام ده في السؤال الأصلي.', 'Point at a row to see that wording in the original question.'), 'muted'),
    h('table', { class: 'words' }, h('thead', {}, h('tr', {}, h('th', {}, B('كلام الشيت', 'Sheet wording')), h('th', {}, B('معناه', 'Meaning')), h('th', {}, B('في Python', 'In Python')), h('th', {}, B('الوحدة', 'Unit')))), h('tbody', {}, rows)),
    h('div', { class: 'teach-note' }, h('b', {}, B('توضيح تعليمي، مش جزء من الشيت الأصلي', 'Teaching clarification, not part of the original sheet')), P(T(q.note))));
}

function predictSection() {
  const q = Q(), p = q.predict, r = R();
  const sec = h('section', { id: 'sec-predict', class: 'sec' }, h('h3', {}, B('توقّع الأول (اختياري)', 'Predict first (optional)')),
    P(B('سؤال واحد صغير قبل الشرح. مش لازم تعرف الحل: التوقع بيخلّي الشرح يثبت.', 'One small question before the explanation. You do not need the solution: predicting makes the explanation stick.'), 'muted'));
  const body = h('div', { class: 'predict' });
  function paint() {
    body.replaceChildren(P(T(p.q), 'big'));
    p.opts.forEach((o, i) => {
      const chosen = r.predict === i, answered = r.predict !== null;
      body.append(btn(h('span', {}, h('b', {}, 'ABCD'[i] + ' '), T(o)), () => { r.predict = i; mark(); paint(); }, 'opt' + (chosen ? ' chosen' : '') + (answered && i === p.ok ? ' right' : ''), { 'aria-pressed': String(chosen), disabled: answered }));
    });
    if (r.predict !== null) body.append(h('div', { class: 'feedback' }, P((r.predict === p.ok ? B('✓ صح. ', '✓ Right. ') : B('مش بالظبط. ', 'Not quite. ')) + T(p.why[r.predict])),
      r.predict !== p.ok ? P(B('الإجابة: ', 'Answer: ') + 'ABCD'[p.ok] + ' · ' + T(p.why[p.ok])) : null, btn(B('جرّب تاني', 'Try again'), () => { r.predict = null; mark(); paint(); }, 'ghost')));
  }
  paint();
  sec.append(body);
  return sec;
}

function planSection() {
  const q = Q(), r = R();
  const sec = h('section', { id: 'sec-plan', class: 'sec' }, h('h3', {}, B('خطتك قبل الكيبورد', 'Your plan before the keyboard')),
    P(B('اكتب بكلامك. بعدين قارن سطر سطر: كل زرار بيكشف سطر واحد بس من الخطة النموذجية.', 'Write it in your own words. Then compare line by line: each button shows one line of the model plan.'), 'muted'),
    field('want', B('WANT: عايز إيه، وبأنهي وحدة؟', 'WANT: what is the answer, and its unit?'), 2), field('have', B('HAVE: معاك إيه، وبوحداته؟', 'HAVE: what is given, with units?'), 2),
    field('plan', B('CONVERT / RELATE / CHECK: هتحوّل إيه؟ العلاقة؟ هتتأكد إزاي؟', 'CONVERT / RELATE / CHECK: what changes units, what relation, how will you check?'), 3));
  const grid = h('div', { class: 'model-plan' });
  function paint() {
    grid.replaceChildren();
    PLANKEYS.forEach(k => {
      const shown = r.planShown.includes(k);
      grid.append(h('div', { class: 'plan-row' + (shown ? ' shown' : '') }, h('b', { dir: 'ltr' }, k),
        shown ? h('span', {}, T(q.plan[k])) : btn(B('قارن السطر ده', 'Compare this line'), () => { r.planShown.push(k); mark(); paint(); }, 'ghost small')));
    });
    if (r.planShown.length) grid.append(btn(B('اخفي الخطة النموذجية', 'Hide the model plan'), () => { r.planShown = []; mark(); paint(); }, 'ghost small'));
  }
  paint();
  sec.append(h('h4', {}, B('الخطة النموذجية', 'Model plan')), grid);
  return sec;
}

function codeSection() {
  const q = Q(), r = R();
  const sec = h('section', { id: 'sec-code', class: 'sec' }, h('h3', {}, B('من الخطة للكود: جزء جزء', 'From plan to code, one part at a time')),
    P(B('كل جزء جاي من سطر في الخطة. حاول تكتبه في PyCharm الأول، وبعدين اكشفه.', 'Each part comes from one plan line. Try writing it in PyCharm first, then reveal it.'), 'muted'));
  const body = h('div', {});
  function paint() {
    body.replaceChildren();
    q.blocks.slice(0, r.blocksShown).forEach((b, i) => body.append(h('div', { class: 'block' }, h('span', { class: 'tag', dir: 'ltr' }, B('من سطر ', 'from ') + b.tag),
      html('pre', Board.hl(b.code), 'codeblock'))));
    const nx = q.blocks[r.blocksShown];
    const row = h('div', { class: 'row' });
    if (nx) row.append(btn(B('اكشف الجزء ', 'Reveal part ') + (r.blocksShown + 1) + ' · ' + nx.tag, () => { r.blocksShown++; mark(); paint(); }, 'primary'), btn(B('اكشف البرنامج كله', 'Reveal the whole program'), () => { r.blocksShown = q.blocks.length; mark(); paint(); }, 'ghost'));
    if (r.blocksShown) row.append(btn(B('اخفي الكود', 'Hide the code'), () => { r.blocksShown = 0; mark(); paint(); }, 'ghost'));
    body.append(row);
    if (r.blocksShown === q.blocks.length) body.append(h('p', {}, h('a', { class: 'button', href: q.file, download: '' }, B('نزّل ملف Python', 'Download the Python file')), ' ',
      h('span', { class: 'muted small' }, B('الملف فيه الخطة وعناوين الأجزاء. بيستخدم eval(input(...)) زي المادة: اكتب أرقام بس.', 'The file contains the plan and the part labels. It uses eval(input(...)) like the course: type numbers only.'))));
  }
  paint();
  sec.append(body);
  return sec;
}

/* ---------- recorded run ---------- */
function runSection() {
  const q = Q(), r = R(), u = U();
  const sec = h('section', { id: 'sec-run', class: 'sec' }, h('h3', {}, B('تشغيل مسجّل: سطر بسطر', 'A recorded run, statement by statement')),
    P(B('ده تسجيل لتشغيل حقيقي على ' + D.python + '. المتصفح مش بيشغّل Python جديد: لمدخلاتك، شغّل الملف على جهازك.', 'A recording of a real run on ' + D.python + '. The browser does not run new Python: for your own inputs, run the file on your computer.'), 'muted'),
    field('predict', B('توقعك للـoutput قبل ما تشوف التسجيل', 'Your prediction of the output before the recording'), 2));
  const body = h('div', {});
  sec.append(body);
  function paint() {
    body.replaceChildren();
    if (!r.reveals.includes('trace')) { body.append(btn(B('اعرض التشغيل المسجّل', 'Show the recorded run'), () => { reveal('trace'); paint(); }, 'primary')); return; }
    u.ci = Math.min(u.ci, q.cases.length - 1);
    const C = q.cases[u.ci];
    u.fi = Math.min(u.fi, C.frames.length - 1);
    body.append(h('div', { class: 'chips' }, h('span', { class: 'muted' }, B('الحالة: ', 'Case: ')), q.cases.map((c, i) => btn(T(c.label), () => { const old = C.frames[u.fi].step; u.ci = i; u.fi = Math.max(0, q.cases[i].frames.findIndex(f => f.step >= old)); saveUI(); paint(); }, 'chip', { 'aria-pressed': String(i === u.ci) }))));
    body.append(h('pre', { class: 'inputs', dir: 'ltr' }, B('المدخلات بالترتيب:\n', 'Inputs, in order:\n') + C.inputs.join('\n') + (C.draws ? '\n' + B('سحبات اختبار ثابتة: ', 'Fixed test draws: ') + C.draws.join(', ') : '')));
    const f = C.frames[u.fi], st = q.steps[f.step], before = u.fi ? C.frames[u.fi - 1] : { values: {}, output: '' };
    const ctl = () => h('div', { class: 'row trace-ctl' }, btn('◀ ' + B('السابق', 'Previous'), () => { u.fi--; saveUI(); paint(); }, 'ghost', { disabled: u.fi === 0 }),
      h('span', { class: 'count' }, (u.fi + 1) + ' / ' + C.frames.length), btn(B('نفّذ اللي بعده', 'Execute next') + ' ▶', () => { u.fi++; saveUI(); paint(); }, 'primary', { disabled: u.fi === C.frames.length - 1 }));
    body.append(ctl());
    const why = q.meanings[st.target] ? T(q.meanings[st.target]) : st.kind === 'condition' ? B('بنسأل السؤال بالقيم الحالية. True يدخل البلوك، False يتخطاه. السؤال نفسه مش بيغيّر أي متغير.', 'Ask the question with the current values. True enters the block; False skips it. Asking changes no variable.')
      : st.kind === 'import' ? B('بنجهّز المكتبة. مفيش output.', 'Make the module available. No output.') : st.kind === 'print' ? B('بنبعت للـOutput. format بيغيّر شكل العرض بس.', 'Send to the output. format changes only the display.')
      : st.expr.includes('input(') ? B('البرنامج بيسأل ويقرا اللي اتكتب.', 'The program asks and reads what was typed.') : st.expr.includes('randint') ? B('سحبة اختبار ثابتة؛ الملف العادي عشوائي.', 'A fixed test draw; the normal file is random.')
      : B('بنحسب الطرف اليمين بالقيم الحالية، وبعدين نخزّن في ', 'Evaluate the right side with the current values, then store in ') + st.target + '.';
    const stage = h('div', { class: 'trace' });
    stage.append(h('div', { class: 'trace-why' }, h('b', {}, B('سطر ', 'Line ') + st.line + ': '), why));
    if (st.expr) { const sub = st.expr.replace(/\b[A-Za-z_]\w*\b/g, t => Object.hasOwn(before.values, t) ? '(' + before.values[t] + ')' : t); stage.append(h('pre', { class: 'subst', dir: 'ltr' }, st.expr + '\n' + sub + (st.target && Object.hasOwn(f.values, st.target) ? '\n' + st.target + ' = ' + f.values[st.target] : ''))); }
    if (f.condition !== null) stage.append(h('div', { class: 'branch ' + (f.condition ? 'T' : 'F') }, (f.condition ? 'True' : 'False') + ' · ' + B(f.condition ? 'هندخل البلوك' : 'هنتخطى البلوك', f.condition ? 'enter the block' : 'skip the block')));
    stage.append(h('div', { class: 'trace-body' }, codeView(q, C, u.fi), h('div', { class: 'trace-side' }, memory(q, f, before), route(q, C, u.fi),
      h('div', { class: 'console' }, h('div', { class: 'label' }, 'Output'), h('pre', { dir: 'ltr' }, before.output, h('mark', {}, f.output.slice(before.output.length)))))));
    body.append(stage, ctl());
    requestAnimationFrame(() => { const cv = stage.querySelector('.codeview'), row = cv && cv.querySelector('.now'); if (row) cv.scrollTop = Math.max(0, row.offsetTop - cv.clientHeight / 3); });
  }
  paint();
  return sec;
}
function codeView(q, C, fi) {
  const frame = C.frames[fi], cur = q.steps[frame.step], done = new Set(), skipped = new Set();
  C.frames.slice(0, fi).forEach(f => { const s = q.steps[f.step]; for (let i = s.line; i <= s.end; i++) done.add(i); });
  C.frames.slice(0, fi + 1).forEach(f => { const s = q.steps[f.step], rg = f.condition === true ? s.elseLines : f.condition === false ? s.thenLines : null; if (rg) for (let l = rg[0]; l <= rg[1]; l++) skipped.add(l); });
  if (fi === C.frames.length - 1) { const ran = new Set(C.frames.map(f => f.step)); q.steps.filter(s => !ran.has(s.id)).forEach(s => { for (let l = s.line; l <= s.end; l++) skipped.add(l); }); }
  const wrap = h('div', { class: 'codeview', dir: 'ltr', tabindex: '0', 'aria-label': 'Python' });
  q.code.trimEnd().split('\n').forEach((l, i) => { const num = i + 1, cl = num >= cur.line && num <= cur.end ? 'now' : done.has(num) ? 'done' : skipped.has(num) ? 'skipped' : ''; wrap.append(h('div', { class: 'cl ' + cl }, h('span', { class: 'ln' }, num), html('code', Board.hl(l) || ' '))); });
  return wrap;
}
function memory(q, f, before) {
  const rows = q.vars.filter(k => Object.hasOwn(f.values, k) || Object.hasOwn(before.values, k)).map(k => h('tr', { class: before.values[k] !== f.values[k] ? 'changed' : '' }, h('td', {}, k), h('td', {}, before.values[k] ?? '—'), h('td', {}, f.values[k] ?? '—')));
  return h('table', { class: 'memory', dir: 'ltr' }, h('thead', {}, h('tr', {}, h('th', {}, 'Variable'), h('th', {}, 'Before'), h('th', {}, 'After'))), h('tbody', {}, rows));
}
/* Which questions have been asked so far, and what each answered. */
function route(q, C, fi) {
  const conds = q.steps.filter(s => s.kind === 'condition');
  if (!conds.length) return null;
  const last = {};
  C.frames.slice(0, fi + 1).forEach(f => { if (f.condition !== null) last[f.step] = f.condition; });
  return h('div', { class: 'route' }, h('div', { class: 'label' }, B('الأسئلة لحد دلوقتي', 'Questions so far')),
    h('ol', { dir: 'ltr' }, conds.map(s => h('li', { class: s.id in last ? (last[s.id] ? 'T' : 'F') : 'unasked' }, h('code', {}, s.expr), ' → ', s.id in last ? (last[s.id] ? 'True' : 'False') : B('لسه ما اتسألش', 'not asked')))),
    P(B('else مالهاش سؤال: بتتنفذ لما كل الأسئلة اللي قبلها في نفس السلسلة تبقى False.', 'else has no question: it runs when every question above it in the same chain was False.'), 'muted small'));
}

function ownSection() {
  const q = Q(), r = R(), t = q.transfer;
  const sec = h('section', { id: 'sec-own', class: 'sec' }, h('h3', {}, B('لوحدك: مسألة جديدة', 'On your own: a new case')),
    P(B('اقفل الحل. اكتب البرنامج بنفسك وشغّله على المدخلات دي. اكتب توقعك الأول.', 'Close the solution. Write the program yourself and run it on these inputs. Write your prediction first.'), 'muted'),
    h('div', { class: 'transfer' }, P(T(t.task), 'big'), h('pre', { class: 'inputs', dir: 'ltr' }, t.inputs.join('\n'))));
  const out = h('div', {});
  const paintOut = () => { out.replaceChildren(r.reveals.includes('transfer') ? h('div', {}, P(B('الـoutput المسجّل لنفس المدخلات:', 'The recorded output for the same inputs:'), 'muted'), h('pre', { class: 'console-out', dir: 'ltr' }, t.printed.trim())) : btn(B('قارن بالـoutput المسجّل', 'Compare with the recorded output'), () => { reveal('transfer'); paintOut(); }, 'ghost')); };
  paintOut();
  sec.append(out, field('run', B('تشغيلك: المدخلات، الـoutput، وإيه اللي صلّحته', 'Your run: inputs, output and what you fixed'), 3),
    field('explain', B('اشرح بكلامك ليه الخطوات بالترتيب ده', 'Explain in your own words why the steps come in this order'), 3),
    h('div', { class: 'prompt' }, P(T(q.challenge))), field('changed', B('توقعك للتغيير وسببه', 'Your prediction for the change, and why'), 2),
    h('div', { class: 'prompt' }, P(T(q.mistake))), field('mistake', B('شخّص الغلط وصلّحه', 'Diagnose and fix the mistake'), 2));
  const bug = h('div', {});
  const paintBug = () => bug.replaceChildren(r.reveals.includes('bug') ? h('div', { class: 'teach-note' }, P(T(q.answer))) : btn(B('اعرض تفسير الغلط', 'Show the explanation of the mistake'), () => { reveal('bug'); paintBug(); }, 'ghost'));
  paintBug();
  const chk = h('input', { type: 'checkbox', id: 'practised' });
  chk.checked = r.practised;
  chk.onchange = () => {
    if (chk.checked && EVIDENCE.some(k => !r.fields[k].trim())) { chk.checked = false; const d = dialog(B('لسه ناقص دليل', 'Evidence missing')); d.append(P(B('كمّل تشغيلك وشرحك والتغيير والغلط.', 'Complete your run, explanation, change and mistake.'))); return; }
    r.practised = chk.checked; mark();
  };
  sec.append(bug, h('label', { class: 'practised', for: 'practised' }, chk, B(' اتمرنت لوحدي وكتبت الدليل', ' I practised on my own and wrote the evidence')),
    P(B('سجل شخصي، مش درجة ولا تسليم. فتح أي حل أو تسجيل مش بيعلّم السؤال «اتحل».', 'A personal record, not a grade or a submission. Opening a solution or a recording never marks a question practised.'), 'muted small'));
  return sec;
}

/* ---------- page ---------- */
function backups() {
  const d = dialog(B('السجل والنسخ الاحتياطية', 'Records and backups'));
  d.append(P(B('السجل على المتصفح ده بس. نزّل نسخة قبل ما تغيّر الجهاز أو مكان الملفات. النسخ القديمة من الـGuide السابق بتتقبل.', 'The record lives in this browser only. Export a copy before changing computers or moving the files. Copies from the previous Guide are accepted.')),
    btn(B('نزّل JSON', 'Export JSON'), () => download('ECE122-Sheet' + S + '-progress.json', JSON.stringify(validate(record), null, 2)), 'primary'));
  function preview(text) {
    let incoming;
    try { incoming = readAny(text); } catch (e) { d.append(P(B('الملف اترفض، والسجل ما اتغيرش. ', 'Rejected; the record is unchanged. ') + e.message, 'error')); return; }
    const c = dialog(B('مراجعة الاسترجاع', 'Review restore'));
    c.append(P(incoming.savedAt + (incoming.migratedFrom ? B(' · منقول من النسخة القديمة', ' · carried over from the previous version') : '')), P(B('هيستبدل السجل الحالي، بعد حفظ نسخة منه.', 'This replaces the current record after saving a snapshot of it.')),
      btn(B('استرجع النسخة', 'Restore backup'), () => {
        if (!put(KEY + '-snapshot', JSON.stringify(record))) { c.append(P(B('تعذّر حفظ النسخة؛ السجل ما اتغيرش.', 'Snapshot failed; record unchanged.'))); return; }
        if (!put(KEY, JSON.stringify(incoming))) { c.append(P('Storage failed')); return; }
        record = incoming; dirty = false; put(KEY + '-draft', JSON.stringify(record)); c.close(); d.close(); render();
      }, 'primary'));
  }
  const inp = h('input', { type: 'file', accept: '.json,application/json', 'aria-label': B('استرجاع JSON', 'Import JSON') });
  inp.onchange = async () => { const f = inp.files[0]; if (f && f.size < 4000000) preview(await f.text()); else d.append(P('File too large')); };
  d.append(h('label', { class: 'field' }, h('span', {}, B('استرجع من ملف', 'Restore from a file')), inp));
  for (const [k, label] of [['-draft', B('استرجع المسودة', 'Restore draft')], ['-snapshot', B('استرجع النسخة السابقة', 'Restore snapshot')]]) { const v = get(KEY + k); if (v) d.append(btn(label, () => preview(v), 'ghost')); }
}
function choose(v) { n = v; location.hash = 'q' + n; saveUI(); render(); window.scrollTo(0, 0); }
function render() {
  document.documentElement.lang = lang === 'ar' ? 'ar-EG' : 'en';
  document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
  saveUI();
  const pick = h('select', { 'aria-label': B('اختار سؤال', 'Choose a question'), onchange: e => choose(Number(e.target.value)) });
  pick.append(h('option', { value: 0 }, '★ ' + T(D.primer.title)));
  D.lessons.forEach(q => pick.append(h('option', { value: q.n }, 'Q' + q.n + ' · ' + T(q.title) + (record.questions[q.n].practised ? ' ✓' : ''))));
  pick.value = String(n);
  const top = h('header', { class: 'top' },
    h('div', { class: 'brand' }, h('b', {}, 'ECE122 · Sheet ' + S + ' Guide'), h('span', { class: 'muted' }, B('افهم، خطط، اكتب، جرّب، واشرح', 'Understand, plan, write, test, explain'))),
    pick, btn(lang === 'ar' ? 'English' : 'عربي', () => { lang = lang === 'ar' ? 'en' : 'ar'; render(); }, 'ghost'),
    btn(B('حفظ تقدّمي', 'Save progress'), save, 'primary'), btn(B('السجل والنسخ', 'Records and backups'), backups, 'ghost'),
    h('span', { id: 'status', 'aria-live': 'polite', class: 'muted small' }),
    h('nav', { class: 'toplinks' }, h('a', { href: '../slides.html' }, B('السبورة (سلايدز)', 'Board slides')), h('a', { href: '../index.html' }, B('البداية', 'Start'))));
  let page;
  if (n === 0) {
    page = h('main', { class: 'primer' }, h('div', { class: 'kicker' }, 'Sheet ' + S), h('h2', {}, T(D.primer.title)),
      P(S === 3 ? B('نفس سبورات السكشن: سؤال آه/لأ، مقارنة، الحد، and/or/not، وبعدين بس if و elif و else. كل خطوة بتجاوب سؤال واحد.', 'The same boards as the lab: a yes/no question, a comparison, the boundary, and/or/not, and only then if, elif and else. Each step answers one question.')
        : B('أدوات بنحتاجها في الشيت: الراديان، نسب المثلث القائم، و ln.', 'Tools the sheet needs: radians, right-triangle ratios, and ln.'), 'muted'),
      boardSection(D.primer.boards, B('على السبورة', 'On the board'), 'sec-board'),
      h('p', {}, btn(B('ابدأ Q1', 'Start Q1') + ' ▶', () => choose(1), 'primary')));
    A.replaceChildren(top, h('div', { class: 'layout one' }, page));
  } else {
    const q = Q();
    const nav = h('nav', { class: 'path', 'aria-label': B('أجزاء السؤال', 'Parts of the question') }, h('ol', {}, SECTIONS().map(([id, t]) => h('li', {}, h('a', { href: '#' + id, onclick: e => { e.preventDefault(); document.getElementById(id).scrollIntoView({ behavior: 'smooth', block: 'start' }); } }, t)))));
    page = h('main', { class: 'work' }, h('div', { class: 'kicker' }, 'Sheet ' + S + ' · Q' + q.n), h('h2', {}, T(q.title)), entry(),
      wordsSection(), predictSection(), boardSection(q.boards, B('على السبورة', 'On the board'), 'sec-board'), planSection(), codeSection(), runSection(), ownSection(),
      h('div', { class: 'row end' }, n > 1 ? btn('◀ Q' + (n - 1), () => choose(n - 1), 'ghost') : btn('◀ ' + T(D.primer.title), () => choose(0), 'ghost'), n < D.lessons.length ? btn('Q' + (n + 1) + ' ▶', () => choose(n + 1), 'primary') : null));
    A.replaceChildren(top, h('div', { class: 'layout' }, h('div', { class: 'side' }, sourcePane(), nav), page));
    const links = [...nav.querySelectorAll('a')];
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) links.forEach(a => a.classList.toggle('here', a.getAttribute('href') === '#' + e.target.id)); }), { rootMargin: '-30% 0px -60% 0px' });
    SECTIONS().forEach(([id]) => io.observe(document.getElementById(id)));
  }
  status();
  if (notice === 'migrated') { const d = dialog(B('سجلك القديم اتنقل', 'Your earlier record was carried over')); d.append(P(B('الـGuide اتجدد. كل اللي كتبته اتنقل، والنسخة القديمة لسه محفوظة على المتصفح زي ما هي.', 'The Guide has been redesigned. Everything you wrote was carried over, and the old copy is still stored in this browser unchanged.'))); notice = ''; }
  else if (notice === 'unreadable') { const d = dialog(B('السجل المحفوظ مش مقروء', 'The saved record could not be read')); d.append(P(B('ابدأنا سجل جديد ومسحناش أي حاجة. افتح «السجل والنسخ» لاسترجاع نسخة.', 'A new record was started and nothing was deleted. Open “Records and backups” to restore a copy.'))); notice = ''; }
}
window.addEventListener('beforeunload', e => { if (dirty) { e.preventDefault(); e.returnValue = ''; } });
document.addEventListener('keydown', e => { if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 's') { e.preventDefault(); save(); } });
render();
if (!notice && get(KEY + '-draft') && get(KEY + '-draft') !== get(KEY) && get(KEY)) { const d = dialog(B('فيه مسودة محفوظة', 'A saved draft exists')); d.append(P(B('ممكن يكون فيه شغل أحدث من آخر حفظ. افتح السجل لاسترجاعه.', 'There may be newer work than the last save. Open Records to restore it.')), btn(B('السجل', 'Records'), () => { d.close(); backups(); }, 'primary')); }
window.workbookQA = { validate, blank, migrate, readAny, getState: () => ({ n, lang, ui: U(), record }), choose, setLang: l => { lang = l; render(); } };
})();
