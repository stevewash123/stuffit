#!/usr/bin/env python3
"""
Send the emails of one or more Full Scenarios (Testing/Scenarios/Scenario N ...) to the StuffIt test mailbox, so Check Emails can pick them up.

It asks for the Gmail APP password of the test mailbox (hidden; never stored or written anywhere), logs in, and sends each scenario's .eml files in file-name order
(order, then shipped, then delivered). Like the earlier test emails, each is labelled FAKE: a "[FAKE TEST]" subject tag and an X-StuffIt-Test header. The From display
name (the store, which is how the app learns the store) and the date are kept; the From address becomes the mailbox itself, because Gmail only sends as the account
that logs in. Anything attached to the .eml (a PDF receipt) is sent as is. Every send gets a fresh Message-ID.

Usage (run it in your own terminal so the password prompt can be typed):
  python send_scenario.py --list          what each scenario would send, nothing is sent
  python send_scenario.py 3               send scenario 3's email(s)
  python send_scenario.py 3 4 5           several, one after another
  python send_scenario.py 1 --no-tag      without the [FAKE TEST] subject tag
Password: environment variable STUFFIT_TEST_GMAIL_APP_PASSWORD if set, else a hidden prompt.
"""
import argparse
import getpass
import glob
import os
import re
import sys
import time
from email import policy
from email.parser import BytesParser
from email.utils import formataddr, getaddresses, make_msgid

from send_test_emails import MAILBOX, open_smtp

HERE = os.path.dirname(os.path.abspath(__file__))
SCENARIOS = os.path.normpath(os.path.join(HERE, "..", "Scenarios"))


def folder_of(n: int) -> str | None:
    hits = sorted(glob.glob(os.path.join(SCENARIOS, f"Scenario {n}")) + glob.glob(os.path.join(SCENARIOS, f"Scenario {n} - *")))
    return hits[0] if hits else None


def emails_of(folder: str) -> list[str]:
    return sorted(glob.glob(os.path.join(folder, "*.eml")))


def describe(path: str) -> str:
    with open(path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)
    name = (getaddresses([msg["From"]])[0][0] or "").strip()
    attached = [p.get_filename() for p in msg.iter_attachments()]
    return f"{os.path.basename(path)}  |  from '{name}'  |  {msg['Subject']}" + (f"  |  attached: {', '.join(attached)}" if attached else "")


def main() -> int:
    ap = argparse.ArgumentParser(description="Send Full Scenario emails to the StuffIt test mailbox.")
    ap.add_argument("scenarios", nargs="*", type=int, help="scenario numbers to send (1, 2, ...)")
    ap.add_argument("--list", action="store_true", help="show what would be sent and stop")
    ap.add_argument("--no-tag", action="store_true", help="leave the subject as it is (no [FAKE TEST] tag)")
    ap.add_argument("--to", default=MAILBOX, help="mailbox to send to (also the Gmail login); default %(default)s")
    args = ap.parse_args()

    if args.list or not args.scenarios:
        for folder in sorted(glob.glob(os.path.join(SCENARIOS, "Scenario *")), key=lambda f: int(re.search(r"Scenario (\d+)", os.path.basename(f)).group(1))):
            files = emails_of(folder)
            print(os.path.basename(folder))
            for f in files:
                print("    " + describe(f))
            if not files:
                print("    (no email)")
        return 0

    plan = []
    for n in args.scenarios:
        folder = folder_of(n)
        if folder is None:
            print(f"No folder for scenario {n} under {SCENARIOS}", file=sys.stderr)
            return 2
        files = emails_of(folder)
        if not files:
            print(f"Scenario {n} has no email to send (its documents are uploaded by hand).", file=sys.stderr)
            continue
        plan += [(n, f) for f in files]
    if not plan:
        return 0

    password = os.environ.get("STUFFIT_TEST_GMAIL_APP_PASSWORD") or getpass.getpass(f"Gmail APP password for {args.to} (not your normal password; hidden): ")
    password = "".join(password.split())
    sent = 0
    try:
        with open_smtp(args.to, password) as smtp:
            for n, path in plan:
                with open(path, "rb") as f:
                    msg = BytesParser(policy=policy.default).parse(f)
                name = (getaddresses([msg["From"]])[0][0] or "").strip()
                subject = str(msg["Subject"] or "")
                for h in ("From", "To", "Message-ID", "Subject"):
                    del msg[h]
                msg["From"] = formataddr((name, args.to))
                msg["To"] = args.to
                msg["Message-ID"] = make_msgid(domain="stuffit-test.invalid")
                msg["Subject"] = subject if args.no_tag or subject.startswith("[FAKE TEST]") else f"[FAKE TEST] {subject}"
                msg["X-StuffIt-Test"] = "fake"
                smtp.send_message(msg)
                sent += 1
                print(f"sent {sent:2d}: scenario {n}: {msg['Subject']}  (from '{name}')")
                time.sleep(0.6)
    except Exception as e:  # a wrong password, a blocked login, a network drop: say it plainly
        print(f"Nothing more was sent. {type(e).__name__}: {e}", file=sys.stderr)
        return 1
    print(f"\nSent {sent} email(s) to {args.to}. Run Check Emails in StuffIt to pick them up.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
