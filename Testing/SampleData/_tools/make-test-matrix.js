// Builds Stories/TESTING/T2-test-matrix.csv: one row per test case, from the plan (Stories/TESTING/T2-document-handling-test-plan.md)
// and the keys. Run:  node make-test-matrix.js
// The Result and Notes columns are NOT kept on regenerate: copy the CSV first if you have entered results.
const fs = require('fs'), path = require('path');
const R = path.join(__dirname, '..');
const rd = (p) => fs.readFileSync(path.join(R, p), 'utf8').replace(/^﻿/, '');
function csv(text) {
  const rows = []; let row = [], cur = '', q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"') { if (text[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += c; }
    else if (c === '"') q = true;
    else if (c === ',') { row.push(cur); cur = ''; }
    else if (c === '\n') { row.push(cur.replace(/\r$/, '')); rows.push(row); row = []; cur = ''; }
    else cur += c;
  }
  if (cur || row.length) { row.push(cur.replace(/\r$/, '')); rows.push(row); }
  const head = rows.shift();
  return rows.filter((r) => r.length > 1).map((r) => Object.fromEntries(head.map((h, i) => [h, r[i] ?? ''])));
}
const base = (f) => f.replace(/\.(pdf|jpg|png)$/i, '');
const num = (f) => { const m = /^(\d+)-/.exec(f); return m ? +m[1] : null; };

const key = csv(rd('receipts/pdf-as-jpg/answer-key-by-item.csv'));
const rc = new Map();
for (const r of key) {
  const id = base(r.file);
  if (!rc.has(id)) rc.set(id, { id, store: r.store, date: r.purchase_date, total: r.total, card: r.payment_last4, lines: [] });
  if (r.line_no) rc.get(id).lines.push(r);
}
const byNum = (n) => [...rc.values()].find((r) => num(r.id) === n);
const returns = new Map(csv(rd('receipts/pdf-series-94-103-returns-manifest.csv')).map((r) => [base(r.file), r]));
const wr = csv(rd('warranties-from-receipts/index.csv'));
const wg = csv(rd('warranties/index.csv'));
const photos = JSON.parse(rd('receipts/paper-photo/truth.json'));
const photoList = Array.isArray(photos) ? photos : Object.entries(photos).map(([k, v]) => ({ file: k, ...v }));

const rows = [];
const add = (o) => rows.push({ id: '', group: '', scenario: '', format: '', file: '', mode: '', before: '', expect: '', runner: '', result: '', notes: '', ...o });
const pad = (n) => String(n).padStart(2, '0');

// ---- A: receipts, each as PDF and as photo scan
const A = [
  ['A1', 'One item, thermal', [17, 18, 36, 41, 1, 2]],
  ['A2', 'One item, A5 or letter layout', [5, 6, 32, 47, 49]],
  ['A3', 'Two or three items', [19, 46, 20, 55, 48, 50]],
  ['A4', 'Long receipt', [12]],
  ['A5', 'Item plus plan line', [15, 26, 28, 81, 82, 33, 85, 86]],
  ['A6', 'Two plans, two items', [83]],
  ['A7', 'Emailed receipt printed to PDF', [21, 23, 56, 57, 58, 59, 60]],
  ['A8', 'Amazon/Apple printouts and invoices', [87, 88, 89, 92, 93, 'amazon-invoice-01', 'apple-invoice-01', 'bestbuy-invoice-01', 'homedepot-receipt-01', 'wayfair-invoice-01']],
  ['A9', 'Trade or contractor invoice', [71, 72, 73, 74, 75, 24]],
  ['A10', 'Discount or reward lines', [25, 76, 77, 78, 79, 80]],
  ['A11', 'Return, exchange or refund', [8, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]],
  ['A12', 'Not a warranty purchase', [9]],
  ['A13', 'Gift receipt, no prices', [11]],
  ['A14', 'Bad capture', [7, 14, 3, 4]],
  ['A17', "Card other than the user's", [3, 8, 82, 101]]
];
for (const [id, sc, items] of A) {
  for (const it of items) {
    const r = typeof it === 'number' ? byNum(it) : rc.get(it);
    if (!r) continue;
    const ret = returns.get(r.id);
    const prods = r.lines.filter((l) => l.kind === 'product').map((l) => [l.brand, l.model_number || l.name].filter(Boolean).join(' '));
    const plan = r.lines.some((l) => l.kind === 'service');
    const expect = ret
      ? `return: ${ret.refund_total} ${ret.refund_method}; ${ret.about}`
      : `${r.store || '(no store)'}; ${r.date}; total ${r.total}; card ${r.card || 'none'}; ${prods.length} product line(s): ${prods.join(', ') || 'none'}${plan ? '; plan line (suggestion only)' : ''}`;
    const n = typeof it === 'number' ? pad(it) : it;
    for (const [fmt, dir, ext] of [['PDF', 'receipts/pdf', 'pdf'], ['photo scan', 'receipts/pdf-as-jpg', 'jpg']]) {
      add({ id: `${id}-${n}-${ext}`, group: 'A receipts', scenario: sc, format: fmt, file: `${dir}/${r.id}.${ext}`, mode: 'New Items upload', before: 'fresh user, card 1212', expect, runner: 'key-viewer.html' });
    }
  }
}
photoList.forEach((p, i) => add({ id: `A15-${pad(i + 1)}`, group: 'A receipts', scenario: 'Real phone photo', format: 'photo (real)', file: `receipts/paper-photo/${p.file}`, mode: 'New Items upload', before: 'fresh user, card 1212', expect: `${p.store}; ${p.purchase_date}; total ${p.total}; card ${p.payment_last4}`, runner: 'key-viewer.html' }));
['cord-paper-01', 'cord-paper-02', 'cord-paper-03', 'cord-paper-04', 'fanzz-paper-01', 'target-paper-01', 'uniqlo-paper-01', 'walmart-paper-01', 'walmart-paper-02', 'walmart-paper-03']
  .forEach((f, i) => add({ id: `A16-${pad(i + 1)}`, group: 'A receipts', scenario: 'Real receipt photos, other shops or countries', format: 'photo (real)', file: `receipts/paper-photo/${f}.jpg`, mode: 'New Items upload', before: 'fresh user', expect: 'Reads without error; probably not a warranty item', runner: 'manual' }));

// ---- B: documents built from receipts, each as PDF and as photo scan
const exp = (w) => `${w.kind}; ${w.product} (${w.model}); plan ${w.plan_no || '-'}; ${w.start_or_purchase} to ${w.end || '(from term: ' + w.term + ')'}; price ${w.plan_price || '-'}; confidence ${w.confidence}`;
const fm = [['PDF', 'warranties-from-receipts', 'pdf'], ['photo scan', 'warranties-from-receipts-photo', 'jpg']];
for (const w of wr) {
  const d = pad(num(w.file)), maker = w.kind === 'manufacturer';
  for (const [fmt, dir, ext] of fm) {
    const f = `${dir}/${base(w.file)}.${ext}`;
    add({ id: `B1-${d}-W-${ext}`, group: 'B documents', scenario: maker ? 'Maker warranty to waiting item' : 'Plan to waiting item', format: fmt, file: f, mode: 'W: to item waiting in New Items', before: `receipt ${num(w.source_receipt)} uploaded, item waiting`, expect: exp(w), runner: 'warranty-viewer.html' });
    add({ id: `B1-${d}-K-${ext}`, group: 'B documents', scenario: maker ? 'Maker warranty to kept item' : 'Plan to kept item', format: fmt, file: f, mode: 'K: to item kept in My Items (popup)', before: `receipt ${num(w.source_receipt)} uploaded and accepted`, expect: exp(w) + '; popup asks Add / Not now', runner: 'warranty-viewer.html' });
  }
}
const loose = [
  ['LW', 'Loose, item waiting', [3, 12, 7], 'item waiting in New Items', 'added as a suggestion at reduced confidence'],
  ['LK', 'Loose, item kept', [4, 11], 'item kept in My Items', 'proposed; nothing added until confirmed'],
  ['LN', 'Loose, no item', [1, 9], 'no matching item', "Unable to find this item. If this is a new item, use Add Item. If not, upload the document from that item's detail page."]
];
for (const [m, sc, docs, before, ex] of loose) {
  for (const dn of docs) {
    const w = wr.find((x) => num(x.file) === dn);
    for (const [fmt, dir, ext] of fm) add({ id: `B5-${m}-${pad(dn)}-${ext}`, group: 'B documents', scenario: sc, format: fmt, file: `${dir}/${base(w.file)}.${ext}`, mode: `${m}: ${sc.toLowerCase()}`, before, expect: ex, runner: 'warranty-viewer.html' });
  }
}
// generic warranties
const special = {
  'standard-power-tool-5yr': ['K', 'item from receipt 41 (Milwaukee 2904-20) kept', 'Milwaukee 2904-20; 5y tool, 3y battery/charger; start = purchase date; updates the maker coverage, no duplicate'],
  'standard-appliance-limited-warranty': ['K', 'item from receipt 81 (Samsung RF28T5001SR) kept', 'MISMATCH: document is model RF28R7551SR; warning shown, not applied silently']
};
for (const g of wg) {
  const file = path.basename(g.path), name = base(file), sp = special[name];
  const gap = /multi-item|retailer-return|card-benefit/.test(name);
  for (const [fmt, dir, ext] of [['PDF', 'warranties', file.split('.').pop()], ['photo scan', 'warranties-photo', 'jpg']]) {
    if (fmt !== 'PDF' && file.endsWith('.png')) continue;
    add({
      id: `B9-${name}-${fmt === 'PDF' ? 'orig' : 'photo'}`, group: 'B documents',
      scenario: /^edge-|^multi-|^retailer-/.test(name) ? 'Edge or non-item document' : 'Generic maker warranty',
      format: file.endsWith('.png') ? 'photo (card)' : fmt, file: `${dir}/${name}.${ext}`,
      mode: sp ? sp[0] : 'LN: loose, no item (to test the reading, add the item by hand and use K)',
      before: sp ? sp[1] : 'no matching item in the sample receipts',
      expect: sp ? sp[2] : `${g.expected}${gap ? ' (known gap or not an item warranty)' : ''}; with no item: the rejection message`,
      runner: 'warranty-viewer.html (loose modes) or manual'
    });
  }
}
add({ id: 'B12-10', group: 'B documents', scenario: 'One document, two items (KNOWN GAP)', format: 'PDF and photo', file: 'warranties-from-receipts/10-homedepot-whirlpool-washer-dryer-5yr.pdf', mode: 'K', before: 'receipt 83 accepted (washer and dryer kept)', expect: 'Expected to FAIL until built: reads as one plan with no price; should be two plans, one per item', runner: 'warranty-viewer.html' });
add({ id: 'B10-16', group: 'B documents', scenario: 'Registration-dependent term (KNOWN GAP)', format: 'PDF and photo', file: 'warranties-from-receipts/16-fujitsu-12rls3-12yr-compressor.pdf', mode: 'K', before: 'receipt 54 accepted', expect: 'Expected 12y compressor if registered; reader gives 5y. Should ask about registration', runner: 'warranty-viewer.html' });

// ---- C: journeys
const J = [
  ['J1', 'TV with Geek Squad', 'receipts/pdf-as-jpg/15-thermal-bestbuy-tv-geek-squad.jpg, then warranties-from-receipts/01-geek-squad-lg-oled-4yr.pdf', 'accept 15, upload doc 01, popup Add; item shows a 4-year plan to 2030-09-27'],
  ['J2', 'TV, plan waits in New Items', 'receipts/pdf/26-thermal-bestbuy-samsung-oled-geek-squad.pdf, then warranties-from-receipts/02-geek-squad-samsung-oled-3yr.pdf', 'doc added to the waiting item as a suggestion; accept; tick it on the item page'],
  ['J3', 'Fridge: photo receipt, PDF plan, wrong-model maker document', 'receipts/pdf-as-jpg/81-letter-homedepot-samsung-fridge-protection-plan.jpg, warranties-from-receipts/04-home-depot-samsung-fridge-5yr.pdf, warranties/standard-appliance-limited-warranty.pdf', 'plan added; maker document flagged as another model'],
  ['J4', 'Power tool, two maker documents', 'receipts/pdf/41-thermal-homedepot-milwaukee-hammer-drill.pdf, warranties-from-receipts/18-milwaukee-m18-hammer-drill.pdf, warranties/standard-power-tool-5yr.pdf', 'one manufacturer coverage; the second document updates rather than duplicates (5y tool, 3y battery)'],
  ['J5', 'Generators', 'receipts/pdf/36-thermal-kestrel-marine-inverter-generator-2200.pdf + warranties-from-receipts/11-kestrel-inverter-generator-2yr.pdf; receipts/pdf/38-thermal-coastal-equipment-honda-generator.pdf + warranties-from-receipts/13-honda-eu2200i-3yr.pdf', 'each item gets its own maker term: 2 years and 3 years'],
  ['J6', 'Plan before receipt (out of order)', 'warranties-from-receipts/01-geek-squad-lg-oled-4yr.pdf, then receipts/pdf/15-thermal-bestbuy-tv-geek-squad.pdf, then doc 01 again', 'first upload rejected with the standard message; after the receipt it is found and added'],
  ['J7', 'Receipt, accept, then return it', 'receipts/pdf/15-thermal-bestbuy-tv-geek-squad.pdf, then receipts/pdf/95-thermal-bestbuy-return-tv-and-geek-squad-plan.pdf', 'recognised as a return (no new item); what happens to the kept TV and its plan is NOT built: record the actual behaviour'],
  ['J8', 'Same receipt twice', 'receipts/pdf/18-thermal-homedepot-style-single.pdf, then receipts/pdf-as-jpg/18-thermal-homedepot-style-single.jpg', 'second is flagged duplicate; no second item'],
  ['J9', 'Batch of ten mixed', 'receipts/pdf: 12, 15, 19, 26, 41, 46, 55, 81, 83, 09 dropped together', 'each handled alone; 09 (grocery) does not stop the rest'],
  ['J10', 'Repair invoice years later (NOT BUILT)', 'receipts/pdf/13-a5-handwritten-style-repair-invoice.pdf to an existing item', 'gap: record what it does today']
];
for (const [id, sc, file, ex] of J) add({ id, group: 'C journeys', scenario: sc, format: 'mixed', file, mode: 'sequence', before: 'fresh user, card 1212', expect: ex, runner: 'manual (or a scripted mode later)' });

// ---- D: refusals
[
  ['D1', 'Corrupt or password-protected PDF', 'make one (truncate a PDF)', 'clear message, nothing saved'],
  ['D2', 'Blank page or blank photo', 'make one', 'could not read this'],
  ['D3', 'Photo that is not a receipt', 'supply one (none in SampleData)', 'rejected plainly'],
  ['D4', 'Wrong file type (.docx, .txt)', 'make one', 'refused with the allowed types'],
  ['D5', 'Over the size limit', 'make one', 'refused with the limit'],
  ['D6', 'Over the daily AI cap', 'lower the cap in test config', 'told when it resets, nothing lost']
].forEach(([id, sc, f, ex]) => add({ id, group: 'D refusals', scenario: sc, format: '-', file: f, mode: 'New Items upload', before: 'fresh user', expect: ex, runner: 'manual' }));

const cols = ['id', 'group', 'scenario', 'format', 'file', 'mode', 'before', 'expect', 'runner', 'result', 'notes'];
const q = (s) => '"' + String(s).replace(/"/g, '""') + '"';
const out = path.join(R, '..', '..', 'Stories', 'TESTING', 'T2-test-matrix.csv');
fs.writeFileSync(out, '﻿' + cols.join(',') + '\n' + rows.map((r) => cols.map((c) => q(r[c])).join(',')).join('\n') + '\n');
const tally = rows.reduce((a, r) => (a[r.group] = (a[r.group] || 0) + 1, a), {});
console.log('wrote', out, rows.length, JSON.stringify(tally));
