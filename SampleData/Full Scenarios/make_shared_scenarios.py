"""Makes the documents for scenarios 19 and 21 (shared-data verification): an order email (.eml) and a register receipt (.pdf and a .jpg twin) per purchase.
   python make_shared_scenarios.py
Scenario 19: a regional store the shared data does not have (Gabe's Hardware), and the same store under a longer name (Gabe's Hardware & Home Center).
Scenario 21: a Home Depot purchase paid with a card the shared data does not have (VISA ending 2468).
Deterministic; re-running rewrites the same files. Dates are close to the run date. Scenario 20 reuses the files of scenarios 4 (Hexaquill) and needs none."""
import datetime, email.message, email.policy, os, subprocess, tempfile
import pypdfium2 as pdfium

ROOT = os.path.dirname(os.path.abspath(__file__))
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TAX = 0.055
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

GABES = dict(sender="Gabe's Hardware", name="Gabe's Hardware", header="GABE'S HARDWARE", addr1='88 Harbor St, Portland, ME 04101', email='Orders@email.gabeshardware.example',
             color='#1f6f43', register='STORE 1  REG 01', policy='RETURNS WITHIN 30 DAYS WITH RECEIPT')
GABES_LONG = dict(GABES, sender="Gabe's Hardware & Home Center", name="Gabe's Hardware & Home Center", header="GABE'S HARDWARE & HOME CENTER", email='Orders@email.gabeshardware.example')
HOMEDEPOT = dict(sender='The Home Depot', name='The Home Depot #2310 - Testville', header='THE HOME DEPOT', addr1='300 Hardware Blvd, Testville, ME 04000', email='HomeDepot@email.homedepot.com',
                 color='#f96302', register='STORE 2310  REG 02', policy='RETURN POLICY 90 DAYS')

SCENARIOS = [
    dict(folder='Scenario 19 - Shared retailer Gabes Hardware', slug='gabes-hardware-makita-xdt16z', shop=GABES, order='GH-20417', date=(2026, 10, 20), trans='0001 1020 4170',
         title='Makita 18V LXT Brushless Cordless Impact Driver (Tool Only)', short='MAKITA 18V LXT IMPACT DRIVER', model='XDT16Z', price=129.00, sn='MKT26D2041', card='1111', num='01'),
    dict(folder='Scenario 19 - Shared retailer Gabes Hardware', slug='gabes-hardware-home-center-makita-xfd131', shop=GABES_LONG, order='GHC-31982', date=(2026, 10, 22), trans='0001 1022 3198',
         title='Makita 18V LXT Brushless Cordless Drill-Driver (Tool Only)', short='MAKITA 18V LXT DRILL DRIVER', model='XFD131', price=119.00, sn='MKT26D3198', card='1111', num='03'),
    dict(folder='Scenario 21 - Shared credit card', slug='homedepot-makita-xrj04z-visa-2468', shop=HOMEDEPOT, order='H23100-52104', date=(2026, 10, 21), trans='2310 1021 5210',
         title='Makita 18V LXT Brushless Cordless Reciprocating Saw (Tool Only)', short='MAKITA 18V LXT RECIP SAW', model='XRJ04Z', price=159.00, sn='MKT26R5210', card='2468', num='01'),
]


def money(x): return f'{x:,.2f}'


def make_email(s, tax, total):
    shop = s['shop']
    y, m, d = s['date']
    day = DAYS[datetime.date(y, m, d).weekday()]
    msg = email.message.EmailMessage(policy=email.policy.SMTP)
    msg['From'] = f"{shop['sender']} <{shop['email']}>"
    msg['To'] = 'Sam Sample <stevewash123.test@gmail.com>'
    msg['Subject'] = f"Your order is confirmed - Pick Up In Store - {s['order']}"
    msg['Date'] = f'{day}, {d:02d} {MONTHS[m - 1]} {y} 08:20:00 -0500'
    msg['Message-ID'] = f"<shared-scenario-{s['slug']}@sample.invalid>"
    msg['X-Synthetic-Sample'] = 'true; fictitious data'
    text = (f"Your order is on its way to the store\n\nWe'll email you when your order is ready for pickup. Order Number: {s['order']}\n\n"
            f"Pick Up In Store\n{shop['name']}\n{shop['addr1']}\n\nPickup person\nSam Sample\n\n"
            f"Order details\n  {s['title']}\n    Model # {s['model']}  Qty: 1   ${money(s['price'])}\n\n"
            f"Subtotal: ${money(s['price'])}\nTax: ${money(tax)}\nTotal: ${money(total)}\n")
    html = ('<!-- SYNTHETIC SAMPLE: fictitious data -->\n<!doctype html><html><head><meta charset="utf-8"><title>' + shop['header'] + '</title></head>\n'
            '<body style="margin:0;background:#f4f4f4;font-family:Arial,Helvetica,sans-serif;color:#222"><table width="600" style="background:#fff;max-width:600px;margin:auto">'
            f'<tr><td style="background:{shop["color"]};color:#fff;padding:18px 24px;font-size:22px;font-weight:bold">{shop["header"]}</td></tr><tr><td style="padding:24px">'
            f'<h2 style="margin:0 0 8px">Your order is on its way to the store</h2><p style="font-size:14px">We\'ll email you when your order is ready for pickup. Order Number: <b>{s["order"]}</b></p>'
            f'<div style="font-size:14px;line-height:1.5">Pick Up In Store<br>{shop["name"]}<br>{shop["addr1"]}<br><br>Pickup person<br>Sam Sample</div>'
            f'<h3>Order details</h3><table width="100%" style="font-size:14px"><tr><td>{s["title"]}<br><span style="color:#666">Model # {s["model"]} Qty: 1</span></td>'
            f'<td align="right" valign="top">${money(s["price"])}</td></tr></table><p style="font-size:14px;margin-top:16px">Subtotal: ${money(s["price"])}<br>Tax: ${money(tax)}<br><b>Total: ${money(total)}</b></p>'
            '</td></tr></table></body></html>')
    msg.set_content(text)
    msg.add_alternative(html, subtype='html')
    return msg.as_bytes()


def receipt_html(s, tax, total):
    shop = s['shop']
    y, m, d = s['date']
    lines = [('c', f"<b>{shop['header']}</b>"), ('c', shop['addr1']), ('r', '-'),
             ('l', *shop['register'].split('  ', 1)), ('l', 'TRANS #', s['trans']), ('l', 'ORDER #', s['order']), ('l', 'ONLINE ORDER PICK UP', ''),
             ('l', f'{m:02d}/{d:02d}/{y}', '11:05'), ('r', '-'),
             ('l', s['short'], money(s['price'])), ('t', f"  MODEL {s['model']}"), ('t', f"  SN {s['sn']}"), ('r', '-'),
             ('l', 'SUBTOTAL', money(s['price'])), ('l', 'TAX 5.5%', money(tax)), ('l', '<b>TOTAL</b>', f'<b>{money(total)}</b>'), ('l', 'VISA', f"****{s['card']}"), ('r', '-'),
             ('c', shop['policy']), ('c', 'PICKED UP IN STORE'), ('c', '*************************')]
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
    n = int(s['num'])
    open(os.path.join(out, f"{n:02d}-email-{s['slug']}.eml"), 'wb').write(make_email(s, tax, total))
    pdf = os.path.join(out, f"{n + 1:02d}-receipt-{s['slug']}.pdf")
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, 'r.html')
        open(src, 'w', encoding='utf-8').write(receipt_html(s, tax, total))
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf}', 'file:///' + src.replace('\\', '/')], check=True, capture_output=True)
    pdfium.PdfDocument(pdf)[0].render(scale=2.6).to_pil().convert('RGB').save(pdf[:-4] + '.jpg', 'JPEG', quality=90)
    print('made', s['folder'], s['slug'], f"${money(s['price'])} + ${money(tax)} = ${money(total)}")
