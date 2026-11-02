"""Makes scenarios 15 to 17: the same store (Home Depot, one shared return policy) and the same maker (Milwaukee), three items that fall under
three different Milwaukee warranty lines. Each folder gets the order email (.eml) and the register receipt (.pdf and a .jpg twin).
   python make_maker_scenarios.py
Deterministic; re-running rewrites the same files. Dates are close to the run date, so the 90-day return window is open."""
import email.message, email.policy, os, subprocess, tempfile
import pypdfium2 as pdfium

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))   # the Scenarios folder
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TAX = 0.055

SCENARIOS = [
    dict(n=15, folder='Scenario 15 - Maker line - heated gear', slug='homedepot-milwaukee-heated-jacket', order='H23100-51501', date=(2026, 10, 19),
         trans='2310 1019 5150', title='Milwaukee M12 Heated TOUGHSHELL Jacket Kit (Black, Large)', short='MILWAUKEE M12 HEATED JACKET KIT', model='204B-21L', price=179.00,
         sn='M12H26C1501', internet='305112501', sku='1005550015'),
    dict(n=16, folder='Scenario 16 - Maker line - digital levels', slug='homedepot-milwaukee-digital-level', order='H23100-51602', date=(2026, 10, 20),
         trans='2310 1020 5160', title='Milwaukee 48 in. Digital Level', short='MILWAUKEE 48 IN DIGITAL LEVEL', model='MLDIG48', price=119.00,
         sn='MLD26D1602', internet='305112602', sku='1005550016'),
    dict(n=17, folder='Scenario 17 - Maker line - portable generators', slug='homedepot-milwaukee-portable-generator', order='H23100-51703', date=(2026, 10, 21),
         trans='2310 1021 5170', title='Milwaukee 3,500-Watt Gas Powered Portable Generator', short='MILWAUKEE 3500W PORTABLE GENERATOR', model='6010-50', price=549.00,
         sn='MPG26G1703', internet='305112703', sku='1005550017'),
]


def money(x): return f'{x:,.2f}'


def make_email(s, tax, total):
    y, m, d = s['date']
    day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][__import__('datetime').date(y, m, d).weekday()]
    mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][m - 1]
    msg = email.message.EmailMessage(policy=email.policy.SMTP)
    msg['From'] = 'The Home Depot <HomeDepot@email.homedepot.com>'
    msg['To'] = 'Sam Sample <stevewash123.test@gmail.com>'
    msg['Subject'] = f"Your order is confirmed - Pick Up In Store - {s['order']}"
    msg['Date'] = f'{day}, {d:02d} {mon} {y} 08:20:00 -0500'
    msg['Message-ID'] = f"<full-scenario-{s['n']}-homedepot-order@sample.invalid>"
    msg['X-Synthetic-Sample'] = 'true; fictitious data, layout modeled on The Home Depot'
    text = (f"Your order is on its way to the store\n\nWe'll email you when your order is ready for pickup. Order Number: {s['order']}\n\n"
            "Pick Up In Store\nThe Home Depot #2310 - Testville\n300 Hardware Blvd, Testville, ME 04000\n\nPickup person\nSam Sample\n\n"
            f"Order details\n  {s['title']}\n    Model # {s['model']}  |  Internet # {s['internet']}  |  Store SKU # {s['sku']}  Qty: 1   ${money(s['price'])}\n\n"
            f"Subtotal: ${money(s['price'])}\nTax: ${money(tax)}\nTotal: ${money(total)}\n")
    html = ('<!-- SYNTHETIC SAMPLE: fictitious data modeled on The Home Depot layout -->\n<!doctype html><html><head><meta charset="utf-8"><title>THE HOME DEPOT</title></head>\n'
            '<body style="margin:0;background:#f4f4f4;font-family:Arial,Helvetica,sans-serif;color:#222"><table width="600" style="background:#fff;max-width:600px;margin:auto">'
            '<tr><td style="background:#f96302;color:#fff;padding:18px 24px;font-size:22px;font-weight:bold">THE HOME DEPOT</td></tr><tr><td style="padding:24px">'
            f'<h2 style="margin:0 0 8px">Your order is on its way to the store</h2><p style="font-size:14px">We\'ll email you when your order is ready for pickup. Order Number: <b>{s["order"]}</b></p>'
            '<div style="font-size:14px;line-height:1.5">Pick Up In Store<br>The Home Depot #2310 - Testville<br>300 Hardware Blvd, Testville, ME 04000<br><br>Pickup person<br>Sam Sample</div>'
            f'<h3>Order details</h3><table width="100%" style="font-size:14px"><tr><td>{s["title"]}<br><span style="color:#666">Model # {s["model"]} | Internet # {s["internet"]} | Store SKU # {s["sku"]} Qty: 1</span></td>'
            f'<td align="right" valign="top">${money(s["price"])}</td></tr></table><p style="font-size:14px;margin-top:16px">Subtotal: ${money(s["price"])}<br>Tax: ${money(tax)}<br><b>Total: ${money(total)}</b></p>'
            '</td></tr></table></body></html>')
    msg.set_content(text)
    msg.add_alternative(html, subtype='html')
    return msg.as_bytes()


def receipt_html(s, tax, total):
    y, m, d = s['date']
    lines = [('c', '<b>THE HOME DEPOT</b>'), ('c', 'Store 2310'), ('c', 'Testville, ME'), ('r', '-'),
             ('l', 'STORE 2310', 'REG 02'), ('l', 'TRANS #', s['trans']), ('l', 'ORDER #', s['order']), ('l', 'ONLINE ORDER PICK UP', ''),
             ('l', f'{m:02d}/{d:02d}/{y}', '11:05'), ('r', '-'),
             ('l', s['short'], money(s['price'])), ('t', f"  MODEL {s['model']}"), ('t', f"  SN {s['sn']}"), ('r', '-'),
             ('l', 'SUBTOTAL', money(s['price'])), ('l', 'TAX 5.5%', money(tax)), ('l', '<b>TOTAL</b>', f'<b>{money(total)}</b>'), ('l', 'VISA', '****1111'), ('r', '-'),
             ('c', 'RETURN POLICY 90 DAYS'), ('c', 'PICKED UP IN STORE'), ('c', '*************************')]
    rows = []
    for ln in lines:
        k = ln[0]
        if k == 'c': rows.append(f'<div class="c">{ln[1]}</div>')
        elif k == 'r': rows.append('<div class="t">' + '-' * 38 + '</div>')
        elif k == 't': rows.append(f'<div class="t">{ln[1].replace(" ", "&nbsp;")}</div>')
        else: rows.append(f'<div class="l"><span>{ln[1]}</span><span>{ln[2]}</span></div>')
    return ('<!doctype html><meta charset="utf-8"><style>@page{size:80mm 125mm;margin:0}body{margin:0;padding:7mm 5mm;width:80mm;font:13px/1.45 "Courier New",monospace;color:#111;background:#fff}'
            '.c{text-align:center}.l{display:flex;justify-content:space-between;gap:8px}.t{white-space:pre}</style>' + ''.join(rows))


for s in SCENARIOS:
    tax = round(s['price'] * TAX + 1e-9, 2)
    total = round(s['price'] + tax, 2)
    out = os.path.join(ROOT, s['folder'])
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, f"01-email-{s['slug']}.eml"), 'wb').write(make_email(s, tax, total))
    pdf = os.path.join(out, f"02-receipt-{s['slug']}.pdf")
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, 'r.html')
        open(src, 'w', encoding='utf-8').write(receipt_html(s, tax, total))
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf}', 'file:///' + src.replace('\\', '/')], check=True, capture_output=True)
    pdfium.PdfDocument(pdf)[0].render(scale=2.6).to_pil().convert('RGB').save(pdf[:-4] + '.jpg', 'JPEG', quality=90)
    print('made', s['folder'], f"${money(s['price'])} + ${money(tax)} = ${money(total)}")
