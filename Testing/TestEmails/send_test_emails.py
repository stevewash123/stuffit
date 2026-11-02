#!/usr/bin/env python3
"""
Send FAKE order/receipt emails to a test Gmail mailbox so StuffIt's mailbox scan has something to read.

Every email is clearly labelled FAKE (subject tag, banner line, X-StuffIt-Test header). Nothing here is a real order.
StuffIt does not check who an order email came from (the store is read from the From display name), so sending
from the mailbox to itself is accepted for any company.

Scenarios cross three coverage dimensions, each in four states:
  store  : verified policy | unverified policy | in the system, no policy | not in the system
  brand  : verified policy | unverified policy | in the system, no policy | not in the system   (brand = maker of the item)
  card   : benefits verified | benefits unverified | in the system, no benefits | no card on the email
plus single-item vs multi-item orders. The names below were chosen from the dev database report
(dotnet run --project src/StuffIt.Api -- --coverage-report Testing/TestEmails/coverage-report.json) after
--seed-placeholders and --seed-test-cards; re-check the report if the seed data changes.

The test cards on the account (added by --seed-test-cards) end in 1111 (verified), 2222 (unverified), 3333 (none).

Usage:
  python send_test_emails.py --list                 show the cross table, send nothing
  python send_test_emails.py                        prompt for the Gmail APP password, send everything
  python send_test_emails.py --fresh                new order numbers (so StuffIt does not treat them as repeats)
  python send_test_emails.py --only 5,6,7           send just those scenario numbers
Password: environment variable STUFFIT_TEST_GMAIL_APP_PASSWORD, else a hidden prompt. It is never stored.
"""
import argparse
import getpass
import itertools
import os
import random
import smtplib
import sys
import time
import zlib
from datetime import date, datetime, timedelta, timezone
from email.message import EmailMessage
from email.utils import formataddr, format_datetime, make_msgid
from pathlib import Path

MAILBOX = "stevewash123.test@gmail.com"
HERE = Path(__file__).resolve().parent

STATES = ["verified", "unverified", "none", "absent"]
STATE_WORDS = {
    "verified": "verified policy", "unverified": "unverified policy",
    "none": "in system, no policy", "absent": "not in system",
}
CARD_WORDS = {
    "verified": "benefits verified", "unverified": "benefits unverified",
    "none": "in system, no benefits", "absent": "no card on email",
}

# Stores (From display name). The first three states exist in the dev database; "absent" ones do not.
STORES = {
    "verified": ["Best Buy", "Amazon", "Target", "Home Depot", "Lowe's", "Walmart", "Costco"],
    "unverified": ["Newegg", "Wayfair", "Macy's", "Kohl's", "B&H Photo"],
    "none": ["Micro Center", "Zappos", "Tractor Supply"],
    "absent": ["Quillfeather Mercantile", "Blorpt Outlet", "Zanzibar Gadget Depot"],
}

# Items by the state of the BRAND's policy. Each name starts with the brand so the brand matcher can find it.
ITEMS = {
    "verified": [
        "Samsung 28 cu. ft. French Door Refrigerator", "LG 4.5 cu. ft. Front Load Washer", "Whirlpool 30 in. Electric Range",
        "Milwaukee M18 FUEL 1/2 in. Hammer Drill Kit", "Penn Battle IV 4000 Spinning Reel", "Pflueger President 2500 Spinning Reel",
        "DeWalt 20V MAX Cordless Drill Combo Kit", "Dyson V15 Detect Cordless Vacuum", "Sonos Beam Soundbar",
        "KitchenAid Artisan 5-Qt Stand Mixer", "Bosch 800 Series Dishwasher", "Garmin Forerunner 265 Watch",
        "GE Appliances 1.7 cu. ft. Over-the-Range Microwave", "Makita 18V LXT Circular Saw", "Black+Decker 20V Hedge Trimmer",
    ],
    "unverified": [
        "Sony WH-1000XM5 Wireless Headphones", "Bose QuietComfort Ultra Earbuds", "Nikon Z6 III Camera Body",
        "Vitamix E310 Explorer Blender", "Yeti Tundra 45 Cooler", "Traeger Pro 575 Pellet Grill",
        "Ninja Foodi 8-Qt Air Fryer", "Shark Navigator Lift-Away Vacuum", "Keurig K-Elite Coffee Maker",
        "Canon EOS R10 Camera Body", "Dell XPS 15 Laptop", "HP Envy 6500 Printer",
    ],
    "none": [
        "Fitbit Charge 6 Fitness Tracker", "Nintendo Switch OLED Console", "Roku Ultra Streaming Player",
    ],
    "absent": [
        "Zorblax ProMax 3000 Widget", "Quillfeather Studio Desk Lamp", "Brontomek Smart Air Fryer",
        "Glimmerfox Trail Backpack", "Hexaquill Cordless Screwdriver Set",
    ],
}

# What a card line looks like for each card state ("absent" = no card line at all).
CARDS = {"verified": ("Visa", "1111"), "unverified": ("Discover", "2222"), "none": ("Mastercard", "3333"), "absent": None}


def build_scenarios():
    """40 scenarios: every store x brand pair twice (single and multi item), card state cycling, then extras on the verified/verified/verified path."""
    rows = []
    pairs = list(itertools.product(STATES, STATES))              # (store state, brand state)
    for pass_no in (0, 1):
        for i, (s, b) in enumerate(pairs):
            rows.append({"store": s, "brand": b, "card": STATES[(i + pass_no * 2 + i // 4) % 4], "multi": bool(pass_no)})
    # The most important path again, across every card state and both sizes.
    for card, multi in itertools.product(STATES, (False, True)):
        rows.append({"store": "verified", "brand": "verified", "card": card, "multi": multi})
    rng = random.Random(20261012)
    used = {k: 0 for k in ITEMS}
    store_used = {k: 0 for k in STORES}
    for n, r in enumerate(rows, 1):
        r["no"] = n
        r["store_name"] = STORES[r["store"]][store_used[r["store"]] % len(STORES[r["store"]])]
        store_used[r["store"]] += 1
        count = rng.choice([2, 3]) if r["multi"] else 1
        names = []
        for _ in range(count):
            pool = ITEMS[r["brand"]]
            names.append(pool[used[r["brand"]] % len(pool)])
            used[r["brand"]] += 1
        # extra lines in a multi-item order come from the same brand state (a cart rarely holds one brand only, but this keeps the cell meaningful)
        r["items"] = [(name, round(rng.uniform(19, 899) + rng.choice([0.0, 0.49, 0.99]), 2), 1) for name in names]
    return rows


def money(x):
    return f"${x:,.2f}"


def body_for(r, order_ref, order_date, stage):
    items = r["items"]
    subtotal = sum(p * q for _, p, q in items)
    tax = round(subtotal * 0.055, 2)
    shipping = 0.0 if subtotal > 35 else 5.99
    total = round(subtotal + tax + shipping, 2)
    lines = [
        "*** FAKE TEST EMAIL - NOT A REAL ORDER OR RECEIPT - GENERATED FOR STUFFIT TESTING ***",
        "",
    ]
    if stage == "confirmation":
        lines += [f"Thanks for your order, {r['store_name']} customer!", ""]
    elif stage == "receipt":
        lines += [f"Your receipt from {r['store_name']}", ""]
    elif stage == "shipped":
        lines += ["Good news - your order has shipped.", ""]
    else:
        lines += ["Your package has been delivered.", ""]
    lines += [f"ORDER #{order_ref}", f"Order date: {order_date.isoformat()}", ""]
    if stage in ("confirmation", "receipt"):
        lines += ["Your order", ""]
        for name, price, qty in items:
            lines += [name, f"Style: FAKE-{zlib.crc32(name.encode()) % 90000 + 10000}", f"Price: {money(price)}", f"Quantity: {qty}", ""]
        lines += [f"Subtotal {money(subtotal)}", f"Shipping {money(shipping)}", f"Tax {money(tax)}", f"Order Total: {money(total)}", ""]
        card = CARDS[r["card"]]
        if card:
            lines += [f"Paid with {card[0]} ending in {card[1]}", ""]
        else:
            lines += ["Paid with: store gift balance", ""]
        lines += [f"Estimated delivery: {(order_date + timedelta(days=5)).strftime('%b %d, %Y')}", ""]
    elif stage == "shipped":
        lines += [f"Estimated delivery: {(order_date + timedelta(days=4)).strftime('%b %d, %Y')}", ""]
    else:
        lines += [f"Delivered: {(order_date + timedelta(days=4)).strftime('%b %d, %Y')}", ""]
    lines += ["-----", "This message is a FAKE test email. Nothing was ordered and nothing was charged."]
    return "\n".join(lines)


def make_message(r, order_ref, stage, order_date, sender_addr):
    subjects = {
        "confirmation": f"[FAKE TEST] Order confirmation #{order_ref} from {r['store_name']}",
        "receipt": f"[FAKE TEST] Your receipt for order #{order_ref} from {r['store_name']}",
        "shipped": f"[FAKE TEST] Your order #{order_ref} has shipped",
        "delivered": f"[FAKE TEST] Your order #{order_ref} has been delivered",
    }
    msg = EmailMessage()
    msg["From"] = formataddr((f"{r['store_name']} Orders", sender_addr))
    msg["To"] = sender_addr
    msg["Subject"] = subjects[stage]
    msg["Date"] = format_datetime(datetime.combine(order_date, datetime.min.time(), tzinfo=timezone.utc) + timedelta(hours=15))
    msg["Message-ID"] = make_msgid(domain="stuffit-test.invalid")
    msg["X-StuffIt-Test"] = "fake"
    msg.set_content(body_for(r, order_ref, order_date, stage))
    return msg


def cross_table(rows, a, b, words_a, words_b, title):
    out = [f"### {title}", "", "| " + " | ".join([f"{a} \\ {b}"] + [words_b[s] for s in STATES]) + " |",
           "|" + "---|" * (len(STATES) + 1)]
    for sa in STATES:
        cells = []
        for sb in STATES:
            nums = [str(r["no"]) for r in rows if r[a] == sa and r[b] == sb]
            cells.append(f"{len(nums)} ({','.join(nums)})" if nums else "0")
        out.append("| " + " | ".join([words_a[sa]] + cells) + " |")
    return "\n".join(out)


def matrix_markdown(rows, sent_note):
    parts = [
        "# StuffIt test emails: what was sent", "", sent_note, "",
        "Cell = number of emails (scenario numbers). Brand = maker of the item. All emails are labelled FAKE.", "",
        cross_table(rows, "store", "brand", STATE_WORDS, STATE_WORDS, "Store x brand"), "",
        cross_table(rows, "store", "card", STATE_WORDS, CARD_WORDS, "Store x card"), "",
        cross_table(rows, "brand", "card", STATE_WORDS, CARD_WORDS, "Brand x card"), "",
        "### Every email", "",
        "| # | Store | Store state | Items (brand state) | Card | Single/multi | Order # |", "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        card = CARDS[r["card"]]
        parts.append(f"| {r['no']} | {r['store_name']} | {STATE_WORDS[r['store']]} | {'; '.join(n for n, _, _ in r['items'])} ({STATE_WORDS[r['brand']]}) | "
                     f"{('ending ' + card[1]) if card else 'none'} ({CARD_WORDS[r['card']]}) | {'multi' if r['multi'] else 'single'} | {r['order_ref']} |")
    parts += ["", "Order-history emails (shipped, delivered) were also sent for scenarios " + ", ".join(str(n) for n in FOLLOW_UPS) + " to test merging into the same item."]
    return "\n".join(parts)


FOLLOW_UPS = [1, 17]   # these orders also get a "shipped" and a "delivered" email with the same order number


def open_smtp(user: str, password: str):
    """Log in on 465 (SSL); if Gmail drops the connection during login, try 587 (STARTTLS) before giving up."""
    last = None
    for port in (465, 587):
        try:
            smtp = smtplib.SMTP_SSL("smtp.gmail.com", port, timeout=30) if port == 465 else smtplib.SMTP("smtp.gmail.com", port, timeout=30)
            if port == 587:
                smtp.ehlo(); smtp.starttls(); smtp.ehlo()
            smtp.login(user, password)
            return smtp
        except smtplib.SMTPServerDisconnected as e:
            last = e
            print(f"port {port}: Gmail closed the connection during login; trying the next way in...", file=sys.stderr)
    raise last


def main():
    ap = argparse.ArgumentParser(description="Send FAKE receipts to the StuffIt test mailbox.")
    ap.add_argument("--to", default=MAILBOX, help="mailbox to send to (also the Gmail login); default %(default)s")
    ap.add_argument("--list", action="store_true", help="print the cross table and stop")
    ap.add_argument("--fresh", action="store_true", help="new order numbers so a re-send is not a repeat")
    ap.add_argument("--only", help="comma-separated scenario numbers to send")
    args = ap.parse_args()

    rows = build_scenarios()
    tag = datetime.now().strftime("%m%d%H%M") if args.fresh else "A"
    today = date(2026, 10, 12)
    for r in rows:
        r["order_ref"] = f"FK-{tag}-{r['no']:03d}"
        r["order_date"] = today - timedelta(days=(r["no"] * 3) % 40)
    chosen = rows
    if args.only:
        wanted = {int(x) for x in args.only.split(",")}
        chosen = [r for r in rows if r["no"] in wanted]

    if args.list:
        print(matrix_markdown(rows, "(listing only: nothing sent)"))
        return 0

    password = os.environ.get("STUFFIT_TEST_GMAIL_APP_PASSWORD") or getpass.getpass(f"Gmail APP password for {args.to} (not your normal password; hidden): ")
    password = "".join(password.split())
    sent = 0
    try:
        with open_smtp(args.to, password) as smtp:
            for r in chosen:
                stages = ["confirmation" if r["no"] % 2 else "receipt"]
                if r["no"] in FOLLOW_UPS:
                    stages += ["shipped", "delivered"]
                for stage in stages:
                    smtp.send_message(make_message(r, r["order_ref"], stage, r["order_date"], args.to))
                    sent += 1
                    print(f"sent {sent:3d}: #{r['no']:02d} {stage:12s} {r['store_name']:26s} {r['items'][0][0][:40]}")
                    time.sleep(0.4)
    except smtplib.SMTPServerDisconnected:
        print("Gmail hung up during login on both ports. This is not a wrong-password message (that is a refusal). Check: the app password was made "
              "for stevewash123.test@gmail.com while signed in to THAT account; 2-Step Verification is on; try again in a few minutes; "
              "try another network (a VPN, firewall or antivirus can cut mail logins).", file=sys.stderr)
        return 1
    except smtplib.SMTPAuthenticationError:
        print("Gmail refused the login. Use a 16-character app password made for this account (needs 2-Step Verification).", file=sys.stderr)
        return 1

    note = f"Sent {sent} emails ({len(chosen)} scenarios) to {args.to} on {datetime.now():%Y-%m-%d %H:%M}."
    (HERE / "sent-matrix.md").write_text(matrix_markdown(rows, note), encoding="utf-8")
    print(note)
    print(f"Cross table written to {HERE / 'sent-matrix.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
