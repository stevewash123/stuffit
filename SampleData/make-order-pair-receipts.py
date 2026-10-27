"""Receipts made to pair with a sample order email (same store, same order number), so the order-then-receipt flow can be tested with brands that
have a verified policy.  python make-order-pair-receipts.py   -> receipts/pdf/104-*.pdf and receipts/pdf-as-jpg/104-*.jpg  (plain render, like the other twins)
Pair 105: the mailbox test email FK-A-001 (Best Buy, Samsung French Door refrigerator, $397.56, Visa 1111, 2026-10-09), made to join it.
Pair 104: emails/order-confirmation/homedepot-order-confirmation-02.eml (order H12345-67890, Milwaukee 2904-22 + DeWalt DCS565B, pickup in store)."""
import os, subprocess, tempfile
import pypdfium2 as pdfium

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

RECEIPTS = [{
    'name': '104-thermal-homedepot-pickup-order-milwaukee-dewalt',
    'lines': [
        ('c', '<b>THE HOME DEPOT</b>'), ('c', 'Store 0999'), ('c', 'Testville, ME'), ('r', '-'),
        ('l', 'STORE 0999', 'REG 02'), ('l', 'TRANS #', '0999 0812 3304'), ('l', 'ORDER #', 'H12345-67890'), ('l', 'ONLINE ORDER PICK UP', ''),
        ('l', '08/12/2026', '14:41'), ('r', '-'),
        ('l', 'MILWAUKEE M18 FUEL HAMMER DRILL', '199.00'), ('t', '  MODEL 2904-22'),
        ('l', 'DEWALT 20V MAX CIRC SAW', '149.00'), ('t', '  MODEL DCS565B'), ('r', '-'),
        ('l', 'SUBTOTAL', '348.00'), ('l', 'TAX 5.5%', '19.14'), ('l', '<b>TOTAL</b>', '<b>367.14</b>'), ('l', 'VISA', '****4242'), ('r', '-'),
        ('c', 'RETURN POLICY 90 DAYS'), ('c', 'PICKED UP IN STORE'), ('c', '*************************'),
    ],
}, {
    'name': '105-thermal-bestbuy-fk-a-001-samsung-fridge',
    'lines': [
        ('c', '<b>BEST BUY</b>'), ('c', 'Store 0123'), ('c', 'Testville, ME'), ('r', '-'),
        ('l', 'ORDER #', 'FK-A-001'), ('l', '10/09/2026', '11:20'), ('r', '-'),
        ('l', 'SAMSUNG 28CF FRENCH DOOR FRIDGE', '375.06'), ('t', '  MODEL RF28T5001SR'), ('r', '-'),
        ('l', 'SUBTOTAL', '375.06'), ('l', 'TAX 6%', '22.50'), ('l', '<b>TOTAL</b>', '<b>397.56</b>'), ('l', 'VISA', '****1111'), ('r', '-'),
        ('c', 'RETURN POLICY 15 DAYS'), ('c', '*************************'),
    ],
}]

def html(lines):
    rows = []
    for ln in lines:
        k = ln[0]
        if k == 'c': rows.append(f'<div class="c">{ln[1]}</div>')
        elif k == 'r': rows.append('<div class="t">' + '-' * 38 + '</div>')
        elif k == 't': rows.append(f'<div class="t">{ln[1].replace(" ", "&nbsp;")}</div>')
        else: rows.append(f'<div class="l"><span>{ln[1]}</span><span>{ln[2]}</span></div>')
    return ('<!doctype html><meta charset="utf-8"><style>@page{size:80mm 125mm;margin:0}body{margin:0;padding:7mm 5mm;width:80mm;font:13px/1.45 "Courier New",monospace;color:#111;background:#fff}'
            '.c{text-align:center}.l{display:flex;justify-content:space-between;gap:8px}.t{white-space:pre}</style>' + ''.join(rows))

for r in RECEIPTS:
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, 'r.html'); open(src, 'w', encoding='utf-8').write(html(r['lines']))
        pdf = os.path.join(HERE, 'receipts', 'pdf', r['name'] + '.pdf')
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf}', 'file:///' + src.replace('\\', '/')], check=True, capture_output=True)
    page = pdfium.PdfDocument(pdf)[0]
    page.render(scale=2.6).to_pil().convert('RGB').save(os.path.join(HERE, 'receipts', 'pdf-as-jpg', r['name'] + '.jpg'), 'JPEG', quality=90)
    print('made', r['name'])
