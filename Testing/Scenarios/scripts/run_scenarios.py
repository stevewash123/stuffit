"""Runs the Scenarios against a running API: signs up a throwaway account, adds the test card, uploads each
scenario's email(s) and receipt in order, and prints what landed in New Items and which coverage the page would tick.
Usage: python scripts/run_scenarios.py [numbers...]   (API on http://localhost:5259, log at api.log beside this file)"""
import base64, hashlib, hmac, json, os, re, struct, subprocess, sys, time, uuid, urllib.request, urllib.error

BASE = "http://localhost:5259/api"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))   # the Scenarios folder
TICKED_FROM = 0.8
OWN_ACCOUNT_FROM = 15   # 18 is handled by run_claims
# Answer keys for scenarios 15 to 17: same store and return policy, same maker, a different Milwaukee warranty line each (months).
EXPECT = {15: ("Heated gear", 12), 16: ("Digital levels", 36), 17: ("Portable generators", 24)}


def check(n, ticked):
    """PASS/FAIL against the answer key: one 90-day return window ticked, exactly one maker warranty ticked and it is the item's own line, both card benefits ticked."""
    line, months = EXPECT[n]
    on = [c for c, t in ticked if t]
    ret = [c for c in on if c["kind"] == "return"]
    mk = [c for c in on if c["kind"] == "manufacturer"]
    card = [c for c in on if c["kind"] == "card"]
    problems = []
    if len(ret) != 1 or days(ret[0]) != 90: problems.append(f"expected one 90-day return window ticked, got {[(c['label'], days(c)) for c in ret]}")
    if len(mk) != 1: problems.append(f"expected one Milwaukee warranty ticked ({line}, {months} months), got {len(mk)}")
    elif round(days(mk[0]) / 30.4) != months: problems.append(f"Milwaukee warranty ticked is {round(days(mk[0]) / 30.4)} months, expected {months} ({line})")
    if len(card) != 2: problems.append(f"expected 2 card benefits ticked, got {len(card)}")
    print("    CHECK", "PASS" if not problems else "FAIL: " + "; ".join(problems))


def call(method, path, body=None, token=None, raw=None, ctype="application/json"):
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    req = urllib.request.Request(BASE + path, data=data, method=method)
    if data is not None: req.add_header("Content-Type", ctype)
    if token: req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            t = r.read().decode()
            return json.loads(t) if t else None
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{method} {path} -> {e.code} {e.read().decode()[:400]}")


def upload(token, files):
    b = "----b" + uuid.uuid4().hex
    parts = []
    for p in files:
        name = os.path.basename(p)
        parts.append(f'--{b}\r\nContent-Disposition: form-data; name="files"; filename="{name}"\r\nContent-Type: application/octet-stream\r\n\r\n'.encode() + open(p, "rb").read() + b"\r\n")
    raw = b"".join(parts) + f"--{b}--\r\n".encode()
    return call("POST", "/pending-items/upload", token=token, raw=raw, ctype="multipart/form-data; boundary=" + b)


def sign_in():
    email = f"scenarios+{int(time.time())}@example.test"
    pw = "Scenario-Run-2026!x"
    call("POST", "/auth/signup", {"email": email, "password": pw, "displayName": "Sam Sample", "timezone": "America/New_York", "acceptedTerms": True})
    time.sleep(1)
    log = open(os.environ.get("API_LOG") or os.path.join(HERE, "api.log"), encoding="utf-8", errors="replace").read()
    token = re.findall(r"verify-signup\?token=([^\s\"<]+)", log)[-1]
    auth = call("POST", "/auth/verify-signup", {"token": token})
    return email, pw, auth["accessToken"]


def add_card(tok):
    cat = call("GET", "/card-catalog", token=tok)
    c = next(x for x in cat if x["cardProduct"].lower() == "chase freedom unlimited")
    call("POST", "/payment-methods", {"nickname": "Chase Freedom Unlimited", "issuerPartyId": c["issuerPartyId"], "cardProduct": c["cardProduct"], "last4": "1111"}, token=tok)


def settle(tok):
    for _ in range(40):
        page = call("GET", "/pending-items?pageSize=50", token=tok)
        if not any(i.get("processing") for i in page["items"]): return page["items"]
        time.sleep(2)
    return page["items"]


def days(c):
    if c.get("endDate") and c.get("startDate"):
        a = time.strptime(c["startDate"], "%Y-%m-%d"); b = time.strptime(c["endDate"], "%Y-%m-%d")
        return (time.mktime(b) - time.mktime(a)) // 86400
    return None


def show(i):
    print(f"  ITEM {i.get('name')!r} | store {i.get('storeText')!r} -> {i.get('sellerName')} | maker {i.get('manufacturerName')} | model {i.get('modelNumber')} | "
          f"{i.get('purchaseDate')} | ${i.get('total')} | card {i.get('cardLast4')} {i.get('cardNickname')} | order {i.get('orderRef')}")
    print(f"    docs: {[(d.get('fileName'), d.get('type')) for d in i.get('documents', [])]}  missing: {i.get('missing')}  stage: {i.get('stage')}")
    cov = i.get("coverage", [])
    ticked = []
    for c in cov:
        oc = c.get("overallConfidence")
        on = (oc if oc is not None else 1) >= TICKED_FROM
        ticked.append((c, on))
        why = (c.get('confidenceReason') or '')[:160]
        print(f"    [{'x' if on else ' '}] {c['label']}  ({c['kind']}, {days(c)} d, ends {c.get('endDate')}, overall {None if oc is None else round(oc, 2)}, {c.get('confidenceBand')}) why: {why}")
    r = [c for c, on in ticked if on and c["kind"] == "return"]
    if len(r) > 1: print("    !! more than one return window ticked")
    if not cov: print("    (no coverage)")
    return ticked


# ---- scenario 18: three accounts report the same shared data; an operator verifies it (S6.1.4) ----
Q_JS = os.environ.get("Q_JS") or os.path.join(HERE, "tools", "q.js")   # runs one SQL statement against the development database (run `npm install` in tools once)


def form(path, tok, fields, files):
    b = "----b" + uuid.uuid4().hex
    parts = [f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode() for k, v in fields.items()]
    for p in files:
        parts.append(f'--{b}\r\nContent-Disposition: form-data; name="files"; filename="{os.path.basename(p)}"\r\nContent-Type: application/octet-stream\r\n\r\n'.encode() + open(p, "rb").read() + b"\r\n")
    return call("POST", path, token=tok, raw=b"".join(parts) + f"--{b}--\r\n".encode(), ctype="multipart/form-data; boundary=" + b)


def totp(secret):
    key = base64.b32decode(secret.replace(" ", "").upper() + "=" * (-len(secret.replace(" ", "")) % 8))
    h = hmac.new(key, struct.pack(">Q", int(time.time()) // 30), hashlib.sha1).digest()
    o = h[-1] & 15
    return f"{(struct.unpack('>I', h[o:o + 4])[0] & 0x7fffffff) % 1000000:06d}"


def operator_token():
    email, pw, tok = sign_in()
    subprocess.run(["node", Q_JS, f"update users set is_operator = true where email = '{email}'"], cwd=os.path.dirname(Q_JS), check=True, capture_output=True)
    setup = call("POST", "/auth/2fa/setup", token=tok)
    return call("POST", "/auth/2fa/enable", {"code": totp(setup["sharedKey"])}, token=tok)["accessToken"]


def folder(n):
    return next(d for d in os.listdir(ROOT) if re.match(rf"Scenario {n}\b", d))


def bring_in(tok, n):
    """Upload scenario n's email and receipt as this account, accept what lands, and return the purchases' items."""
    d = os.path.join(ROOT, folder(n))
    for f in sorted(f for f in os.listdir(d) if f.lower().endswith((".eml", ".pdf")) and "warranty" not in f.lower()):
        upload(tok, [os.path.join(d, f)])
    items = []
    for i in settle(tok):
        pid = call("POST", f"/pending-items/{i['id']}/accept", token=tok)["purchaseId"]
        det = call("GET", f"/purchases/{pid}", token=tok)
        items += [{**it, "_purchase": det} for it in det["items"]]
    return items


def claim_line(c):
    return f"{c['kind']:6} x{c['accounts']} ready={c['ready']}  {c['subject']}  [{c.get('category')}]  {c['facts'][:60]}"


def run_claims():
    SHOWN = ("Quillfeather", "Hexaquill", "Sony")
    op = operator_token()
    print("operator signed in with two-step sign-in")
    checks = []

    def mine(): return [c for c in call("GET", "/admin/claims", token=op) if any(w.lower() in c["subject"].lower() for w in SHOWN)]

    base = {(c["kind"], c.get("category")): c["accounts"] for c in mine()}   # accounts that already reported it (the test client's own uploads count); a policy is counted per category
    print("already counted before this run:", base or "nothing")
    for k in range(1, 4):
        email, pw, tok = sign_in(); add_card(tok)
        print(f"\n--- account {k}: {email}")
        for n in (3, 4): bring_in(tok, n)
        sony = bring_in(tok, 6)[0]
        w = next(f for f in os.listdir(os.path.join(ROOT, folder(6))) if "warranty" in f.lower() and f.lower().endswith(".pdf"))
        res = form("/document-facts/warranty", tok, {"itemId": sony["id"], "origin": "CameWithProduct"}, [os.path.join(ROOT, folder(6), w)])
        print("  warranty applied:", res.get("status"), res.get("summary"), "shared:", res.get("shared"), "match:", res.get("match"))
        for c in mine(): print("  claim", claim_line(c))
        now = {(c["kind"], c.get("category")): c for c in mine()}
        checks.append((f"after account {k}: the store, brand and policy claims each went up to {k} new account(s)", all(now.get(key, {}).get("accounts") == base.get(key, 0) + k for key in (("store", None), ("brand", None), ("policy", "Audio")))))
        checks.append((f"after account {k}: each is ready exactly when it has 3 accounts", all(c["ready"] == (c["accounts"] >= 3) for c in now.values())))
        if k == 1: first = (email, pw, tok)

    ready = [c for c in call("POST", "/admin/claims/evaluate", token=op) if any(w.lower() in c["subject"].lower() for w in SHOWN)]
    print("\nevaluate returned", len(ready), "ready")
    for c in ready: print("  ", claim_line(c))
    checks.append(("evaluate returns the three ready claims", len(ready) == 3))

    for c in ready:
        body = {"id": c["id"]}
        if c["kind"] == "policy": body["sourceUrl"] = "https://www.sony.com/electronics/support"
        print("  approve", c["subject"], "->", call("POST", "/admin/claims/approve", body, token=op)["outcome"])
    checks.append(("nothing is left to review", not [c for c in mine() if c["ready"]]))

    email, pw, tok = sign_in(); add_card(tok)
    print(f"\n--- a fourth account afterwards: {email}")
    got = {n: bring_in(tok, n) for n in (3, 4, 6)}
    for n, its in got.items():
        for it in its:
            pu = it["_purchase"]
            cov = [(c["kind"], c.get("providerName"), c.get("endDate")) for c in (it.get("coverages") or it.get("coverage") or [])]
            print(f"  scenario {n}: {it.get('name')} | store {pu.get('sellerName')} (shared: {pu.get('sellerPartyId') is not None and not pu.get('sellerUnverified')}) | maker {it.get('manufacturerName')} (shared: {it.get('manufacturerPartyId') is not None and not it.get('manufacturerUnverified')}) | coverage {cov}")
    p3, i4, i6 = got[3][0]["_purchase"], got[4][0], got[6][0]
    checks.append(("fourth account: Quillfeather Mercantile is now a shared store (not marked unverified)", p3.get("sellerPartyId") is not None and not p3.get("sellerUnverified")))
    checks.append(("fourth account: Hexaquill is now a shared brand (not marked unverified)", i4.get("manufacturerPartyId") is not None and not i4.get("manufacturerUnverified")))
    checks.append(("fourth account: the Sony warranty now comes from shared data and is added", any(c["kind"] == "manufacturer" for c in (i6.get("coverages") or i6.get("coverage") or []))))
    print("\nCHECKS")
    for text, ok in checks: print("  ", "PASS" if ok else "FAIL", text)


def main():
    want = [int(a) for a in sys.argv[1:]]
    if want == [18]: return run_claims()
    email, pw, tok = sign_in()
    print("account", email)
    add_card(tok)
    try:
        folders = sorted((d for d in os.listdir(ROOT) if d.startswith("Scenario")), key=lambda d: int(re.search(r"\d+", d).group()))
        for d in folders:
            n = int(re.search(r"\d+", d).group())
            if want and n not in want: continue
            if n >= 18: continue   # 18 is run_claims; 19 to 21 are run_shared.py (python scripts/run_shared.py 19 20 21): they need several accounts and an operator
            print(f"\n=== {d}")
            files = sorted(f for f in os.listdir(os.path.join(ROOT, d)) if f.lower().endswith((".eml", ".pdf")) and "warranty" not in f.lower())
            for f in files:
                res = upload(tok, [os.path.join(ROOT, d, f)])
                for r in res:
                    print(f"  upload {f}: dup={r['duplicate']} updated={r['updated']} err={r['error']} note={r.get('note')} left_out={r.get('leftOut')}")
            for i in settle(tok):
                ticked = show(i)
                if n in EXPECT: check(n, ticked)
                try:
                    pid = call("POST", f"/pending-items/{i['id']}/accept", token=tok)["purchaseId"]
                    det = call("GET", f"/purchases/{pid}", token=tok)
                    for it in det["items"]:
                        cov = it.get("coverages") or it.get("coverage") or []
                        print("    ADDED to My Items with:", [(c["kind"], c.get("providerName"), c.get("endDate")) for c in cov])
                except SystemExit as e:
                    print("    accept failed:", e)
                    call("POST", f"/pending-items/{i['id']}/dismiss", token=tok)
    finally:
        print("\n(throwaway account left in the dev database:", email + ")")


if __name__ == "__main__":
    main()
