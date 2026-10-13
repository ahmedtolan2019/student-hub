/* Whiteboard renderer shared by the slides and the Guides.

   A board is written step by step, the way it is written on a real board.
   Every row and every sketch layer carries the step `s` at which it is
   written. Nothing written earlier disappears: a value that changes is struck
   through at step `x` and stays visible. Writing that has not happened yet
   keeps its place (visibility: hidden), so earlier work never moves.

   Board data comes from src/boards*.py, written by Python 3.14.6, so every
   number on a board was produced by Python. This file only places it. */
(function () {
'use strict';

function esc(s) {
  return String(s).replace(/[&<>"']/g, function (k) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[k];
  });
}

/* A small Python highlighter: comments, strings, numbers, keywords, built-ins. */
function hl(code) {
  var re = /(#[^\n]*)|("(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*')|(\b\d+(?:\.\d+)?(?:[eE][+-]?\d+)?\b)|([A-Za-z_][A-Za-z0-9_]*)/g;
  var KW = ' if elif else for while def return import from as in and or not True False None ';
  var BI = ' print input eval int float format str round abs len range chr ord math random ';
  var out = '', last = 0, m;
  while ((m = re.exec(code))) {
    out += esc(code.slice(last, m.index));
    var t = m[0], c = '';
    if (m[1]) c = 'tk-c'; else if (m[2]) c = 'tk-s'; else if (m[3]) c = 'tk-n';
    else if (m[4]) { if (KW.indexOf(' ' + t + ' ') >= 0) c = 'tk-k'; else if (BI.indexOf(' ' + t + ' ') >= 0) c = 'tk-p'; }
    out += c ? '<span class="' + c + '">' + esc(t) + '</span>' : esc(t);
    last = re.lastIndex;
  }
  return out + esc(code.slice(last));
}

/* Text fields are either a plain string (language-neutral: math, numbers,
   Python) or {ar, en}. Authored markup is trusted: it comes from the build. */
function T(v, lang) { return v == null ? '' : typeof v === 'string' ? v : (v[lang] != null ? v[lang] : v.en); }

var LETTERS = ['A', 'B', 'C', 'D', 'E'];

function rowHTML(r, lang) {
  var cls = 'wb-row wb-' + r.k + (r.cls ? ' ' + r.cls : '');
  var at = ' data-s="' + (r.s || 0) + '"' + (r.x ? ' data-x="' + r.x + '"' : '');
  switch (r.k) {
    case 'say':
      return '<p class="' + cls + '"' + at + '>' + T(r.t, lang) + '</p>';
    case 'why':
      return '<p class="' + cls + '"' + at + '><span class="wb-arrow" aria-hidden="true">' + (lang === 'ar' ? '⟵' : '⟶') + '</span><span>' + T(r.t, lang) + '</span></p>';
    case 'eq':
      return '<div class="' + cls + '"' + at + ' dir="ltr">' + r.h + '</div>';
    case 'map':
      return '<div class="' + cls + '"' + at + '><span class="wb-words">' + T(r.t, lang) + '</span>' +
        '<span class="wb-to" aria-hidden="true">' + (lang === 'ar' ? '⟵' : '⟶') + '</span><span class="wb-py" dir="ltr">' + r.h + '</span></div>';
    case 'cl':
      return '<div class="' + cls + '"' + at + ' dir="ltr"><pre class="wb-clc">' + hl(r.c) + '</pre><span class="wb-cln" dir="' + (lang === 'ar' ? 'rtl' : 'ltr') + '">' + T(r.t, lang) + '</span></div>';
    case 'code':
      return '<pre class="' + cls + '"' + at + ' dir="ltr">' + hl(r.c) + '</pre>';
    case 'out':
      return '<pre class="' + cls + '"' + at + ' dir="ltr">' + esc(r.c) + '</pre>';
    case 'grid':
      return '<table class="' + cls + '"' + at + '>' + r.rows.map(function (row, i) {
        var tag = r.head && i === 0 ? 'th' : 'td';
        return '<tr' + (r.rs ? ' class="wb-gr" data-s="' + r.rs[i] + '"' : '') + '>' + row.map(function (c) {
          return '<' + tag + (typeof c === 'string' ? ' dir="ltr"' : '') + '>' + T(c, lang) + '</' + tag + '>';
        }).join('') + '</tr>';
      }).join('') + '</table>';
    case 'vote':
      return '<div class="' + cls + '"' + at + '>' + (r.q ? '<p class="wb-vq">' + T(r.q, lang) + '</p>' : '') +
        '<div class="wb-opts">' + r.opts.map(function (o, n) {
          return '<button type="button" class="wb-opt" data-n="' + n + '"><span class="wb-fill"></span><b>' + LETTERS[n] +
            '</b><span class="wb-ot"' + (typeof o === 'string' ? ' dir="ltr"' : '') + '>' + T(o, lang) + '</span><em class="wb-cnt"></em></button>';
        }).join('') + '</div></div>';
    case 'gap':
      return '<div class="' + cls + '"' + at + ' aria-hidden="true"></div>';
  }
  throw new Error('Unknown board row ' + r.k);
}

/* Build a board element. mode is 'slide' or 'guide'. */
function build(b, lang, mode) {
  var el = document.createElement('div');
  el.className = 'wb wb-' + (b.layout || 'split') + ' wb-mode-' + mode;
  el.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
  if (b.ratio) el.style.setProperty('--wb-ratio', b.ratio);
  if (b.clw) el.style.setProperty('--wb-clw', b.clw + 'ch');
  var rows = (b.rows || []).filter(function (r) { return !r.col; }).map(function (r) { return rowHTML(r, lang); }).join('');
  var rows2 = (b.rows || []).filter(function (r) { return r.col; }).map(function (r) { return rowHTML(r, lang); }).join('');
  var h = '';
  if (b.ask) h += '<p class="wb-ask" data-s="0">' + T(b.ask, lang) + '</p>';
  h += '<div class="wb-area">';
  if (b.sketch) h += '<div class="wb-sketch" dir="ltr">' + b.sketch + '</div>';
  var one = '<div class="wb-rows">' + rows + '</div>';
  h += rows2 ? '<div class="wb-pair">' + one + '<div class="wb-rows wb-rows2">' + rows2 + '</div></div>' : one;
  h += '</div>';
  el.innerHTML = h;
  el.wbBoard = b;
  el.wbStep = -1;
  return el;
}

function steps(b) { return (b.steps || []).length; }
function voteRow(b) { return (b.rows || []).filter(function (r) { return r.k === 'vote'; })[0] || null; }

/* Show the board as written up to step k. reveal forces a vote's answer. */
function set(el, k, reveal) {
  var b = el.wbBoard, n = steps(b);
  k = Math.max(0, Math.min(n, k));
  el.wbStep = k;
  el.setAttribute('data-step', k);
  Array.prototype.forEach.call(el.querySelectorAll('[data-s]'), function (e) {
    var s = +e.getAttribute('data-s'), x = e.getAttribute('data-x');
    e.classList.toggle('wb-on', s <= k);
    e.classList.toggle('wb-fresh', s === k && k > 0);
    e.classList.toggle('wb-struck', x !== null && +x <= k);
  });
  /* data-m marks writing that is already on the board: from step m it is
     underlined or coloured, the way a teacher circles a word. */
  Array.prototype.forEach.call(el.querySelectorAll('[data-m]'), function (e) {
    e.classList.toggle('wb-mk', +e.getAttribute('data-m') <= k);
  });
  var v = voteRow(b);
  if (v) {
    var shown = reveal || k > v.s;
    Array.prototype.forEach.call(el.querySelectorAll('.wb-opt'), function (o, i) {
      o.classList.toggle('wb-right', shown && i === b.ok);
      o.classList.toggle('wb-other', shown && i !== b.ok);
    });
  }
  return k;
}

/* Votes: counts per option, drawn as bars. Nothing here depends on which
   option is correct; that only shows once the answer step is written. */
function tally(el, counts) {
  var total = counts.reduce(function (a, c) { return a + c; }, 0);
  Array.prototype.forEach.call(el.querySelectorAll('.wb-opt'), function (o, i) {
    o.querySelector('.wb-cnt').textContent = counts[i] ? counts[i] : '';
    o.querySelector('.wb-fill').style.width = total ? (counts[i] / total * 100) + '%' : '0';
  });
}

window.Board = { build: build, set: set, steps: steps, tally: tally, voteRow: voteRow, hl: hl, esc: esc, T: T };
})();
