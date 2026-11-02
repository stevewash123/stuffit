"""Builds the answer key the eval reads (truth.json) from answer-key-by-item.csv.

The CSV has one row per line item; the receipt-level columns (store, order number, dates, total, tax, card) repeat on every row of a receipt.
Edit the CSV, then run:
    python make-truth.py                 -> truth.draft.json  (every entry marked _unverified: the eval refuses it)
    python make-truth.py --verified      -> truth.json        (use only after the CSV has been checked against the paper)
"""
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RECEIPT = ['document_class', 'store', 'order_number', 'purchase_date', 'delivery_date', 'total', 'payment_last4']
verified = '--verified' in sys.argv

rows = list(csv.DictReader(open(os.path.join(HERE, 'answer-key-by-item.csv'), encoding='utf-8-sig')))
by_file = {}
for r in rows:
    by_file.setdefault(r['file'], []).append(r)

truth = {}
for file, lines in by_file.items():
    lines.sort(key=lambda r: int(r['line_no']))
    head = lines[0]
    e = {k: head[k].strip() for k in RECEIPT if head[k].strip()}
    names = [(l['name'] or l['line']).strip() for l in lines if l['kind'] != 'fee']
    if names: e['items'] = '; '.join(names)
    first = next((l for l in lines if l['kind'] == 'product'), None)
    if first:
        e['item_line'] = first['line'].strip(); e['item_price'] = first['price'].strip()
        for src, dst in (('brand', 'brand'), ('name', 'product_name'), ('model_number', 'model_number')):
            if first[src].strip(): e[dst] = first[src].strip()
    products = []
    for l in lines:
        if l['kind'] in ('product', 'repair'):
            products.append({'kind': l['kind'], 'line': l['line'].strip(), 'brand': l['brand'].strip(), 'name': l['name'].strip(),
                             'model_number': l['model_number'].strip(), 'price': l['price'].strip()})
        else:
            products.append({'kind': l['kind'], 'line': l['line'].strip()})
    e['products'] = json.dumps(products, ensure_ascii=False, separators=(',', ':'))
    if not verified: e['_unverified'] = 'check every value against the paper, then delete this line'
    truth[file] = e

out = os.path.join(HERE, 'truth.json' if verified else 'truth.draft.json')
json.dump(truth, open(out, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
print(f'{len(truth)} receipts, {len(rows)} line rows -> {os.path.basename(out)}')
