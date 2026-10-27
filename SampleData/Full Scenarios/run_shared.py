"""Runs scenarios 19 (shared retailer), 20 (shared manufacturer) and 21 (shared credit card) against a running API, each on new accounts plus an operator account.
Several accounts report the same new thing, an operator verifies it, and the checks look at what happens to the accounts that reported it and to one that comes after.
Usage: python run_shared.py 19 20 21      (API on http://localhost:5259; set API_LOG to the API's log file, as for run_scenarios.py)
Prints PASS or FAIL for each check. Leaves its throwaway accounts and the shared entries it made in the development database: run cleanup (see README) afterwards."""
import os, sys, time
import run_scenarios as rs

call, ROOT = rs.call, rs.ROOT


def paths(n, *prefixes):
    d = os.path.join(ROOT, rs.folder(n))
    return [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.lower().endswith((".eml", ".pdf")) and any(f.startswith(p) for p in prefixes)]


def bring(tok, files, before_accept=None):
    """Upload the files as this account, let New Items settle, optionally change each pending item, accept them, and return the items with their purchases."""
    for f in files: rs.upload(tok, [f])
    out = []
    for i in rs.settle(tok):
        if before_accept: before_accept(i)
        pid = call("POST", f"/pending-items/{i['id']}/accept", token=tok)["purchaseId"]
        det = call("GET", f"/purchases/{pid}", token=tok)
        out += [{**it, "_purchase": det} for it in det["items"]]
    return out


def claims(op, *words):
    return [c for c in call("GET", "/admin/claims", token=op) if any(w.lower() in c["subject"].lower() for w in words)]


def show(label, cs):
    for c in cs: print(f"  {label}: {c['kind']:11} x{c['accounts']} ready={c['ready']}  {c['subject']}  {c['facts'][:70]}")


def proposals(tok, item_id):
    return call("GET", f"/items/{item_id}/proposals", token=tok)


def finish(checks):
    print("\nCHECKS")
    for text, ok in checks: print("  ", "PASS" if ok else "FAIL", text)
    print("\n", sum(1 for _, ok in checks if ok), "of", len(checks), "passed")


def ticked(p): return (p.get("confidence") or 0) >= rs.TICKED_FROM


# ---------------------------------------------------------------- 19: a retailer the shared data does not have
def retailer():
    op, checks, who = rs.operator_token(), [], []
    print("operator signed in with two-step sign-in")
    for k in (1, 2, 3):
        email, pw, tok = rs.sign_in(); rs.add_card(tok)
        print(f"\n--- account {k}: {email} brings in the Gabe's Hardware order")
        items = bring(tok, paths(19, "01", "02"))
        who.append((tok, items))
        cs = claims(op, "gabe"); show("claim", cs)
        store = [c for c in cs if c["kind"] == "store"]
        checks.append((f"after account {k}: one store claim for Gabe's Hardware with {k} account(s), ready only at 3", len(store) == 1 and store[0]["accounts"] == k and store[0]["ready"] == (k >= 3)))
    ready = [c for c in call("POST", "/admin/claims/evaluate", token=op) if "gabe" in c["subject"].lower()]
    checks.append(("evaluate returns the store claim", len(ready) == 1 and ready[0]["kind"] == "store"))
    policy = {"days": 30, "fromDelivery": False, "conditions": "With receipt.", "sourceUrl": "https://example.com/gabes-hardware/returns"}
    done = call("POST", "/admin/claims/approve", {"id": ready[0]["id"], "returnPolicy": policy}, token=op)
    print("\n  approved:", done)
    shared_id = done["sharedId"]
    checks.append(("approved: the claim is gone from the list", not [c for c in claims(op, "gabe") if c["kind"] == "store"]))
    for k, (tok, items) in enumerate(who, 1):
        it = items[0]
        purchase = call("GET", f"/purchases/{it['_purchase']['id']}", token=tok)
        ret = [p for p in proposals(tok, it["id"]) if str(p.get("kind")).lower() == "return"]
        print(f"  account {k}: purchase store {purchase.get('sellerName')!r} ({purchase.get('sellerPartyId')}); return suggestions {[(p.get('label'), p.get('endDate'), p.get('confidence')) for p in ret]}")
        checks.append((f"account {k}: its purchase now points at the shared store", purchase.get("sellerPartyId") == shared_id))
        checks.append((f"account {k}: the verified 30-day return window is suggested and ticked, ending 2026-11-19", any(p.get("endDate") == "2026-11-19" and ticked(p) for p in ret)))
    party = call("GET", f"/parties/{shared_id}", token=who[0][0])["party"]
    checks.append(("the shared store is not any account's own", party.get("isMine") is False))

    print("\n--- a fourth account brings in the order from \"Gabe's Hardware & Home Center\"")
    email, pw, tok = rs.sign_in(); rs.add_card(tok)
    items = bring(tok, paths(19, "03", "04"))
    purchase = items[0]["_purchase"]
    checks.append(("fourth account: the longer name is matched to the shared store on its first words", purchase.get("sellerPartyId") == shared_id))
    aliases = [c for c in claims(op, "gabe") if c["kind"] == "alias"]
    show("claim", aliases)
    checks.append(("an alias claim is offered: \"Gabe's Hardware & Home Center\" for \"Gabe's Hardware\", ready at one account", len(aliases) == 1 and aliases[0]["ready"] and aliases[0].get("target") == party["name"]))
    if aliases:
        call("POST", "/admin/claims/approve", {"id": aliases[0]["id"]}, token=op)
        party = call("GET", f"/parties/{shared_id}", token=tok)["party"]
        print("  aliases now:", party.get("aliases"))
        checks.append(("approved: the longer name is now an alias of the shared store", any("home center" in a.lower() for a in party.get("aliases", []))))
        checks.append(("approved: the alias claim is closed", not [c for c in claims(op, "gabe") if c["kind"] == "alias"]))
    finish(checks)


# ---------------------------------------------------------------- 20: a manufacturer the shared data does not have
def manufacturer():
    op, checks, who = rs.operator_token(), [], []
    print("operator signed in with two-step sign-in")
    warranty = next(os.path.join(ROOT, rs.folder(4), f) for f in os.listdir(os.path.join(ROOT, rs.folder(4))) if "warranty" in f.lower() and f.lower().endswith(".pdf"))
    for k in (1, 2, 3):
        email, pw, tok = rs.sign_in(); rs.add_card(tok)
        print(f"\n--- account {k}: {email} brings in scenario 4 (Hexaquill) and adds the brand as its own")
        brand = call("POST", "/parties", {"name": "Hexaquill", "isManufacturer": True, "isSeller": False, "isCardIssuer": False, "isWarrantyProvider": False}, token=tok)
        items = bring(tok, paths(4, "01", "02"), before_accept=lambda i, b=brand: call("PATCH", f"/pending-items/{i['id']}", {"manufacturerPartyId": b["id"]}, token=tok))
        res = rs.form("/document-facts/warranty", tok, {"itemId": items[0]["id"], "origin": "CameWithProduct"}, [warranty])
        print("  warranty:", res.get("status"), res.get("summary"), "shared:", res.get("shared"), "match:", res.get("match"))
        who.append((tok, items[0], brand["id"]))
        show("claim", claims(op, "hexaquill"))
    cs = claims(op, "hexaquill")
    brands = [c for c in cs if c["kind"] == "brand"]
    policies = [c for c in cs if c["kind"] == "policy"]
    checks.append(("before the brand is verified: one brand claim with 3 accounts, ready", len(brands) == 1 and brands[0]["accounts"] == 3 and brands[0]["ready"]))
    checks.append(("before the brand is verified: each account's warranty is its own claim of 1 (each is about its own private brand)", len(policies) == 3 and all(c["accounts"] == 1 for c in policies)))
    done = call("POST", "/admin/claims/approve", {"id": brands[0]["id"]}, token=op)
    shared_id = done["sharedId"]
    print("\n  brand approved:", done)
    cs = claims(op, "hexaquill"); show("claim", cs)
    policies = [c for c in cs if c["kind"] == "policy"]
    checks.append(("after the brand is verified: the three warranty claims become one claim of 3 accounts, ready", len(policies) == 1 and policies[0]["accounts"] == 3 and policies[0]["ready"]))
    for k, (tok, item, private_brand) in enumerate(who, 1):
        item_now = call("GET", f"/purchases/{item['_purchase']['id']}", token=tok)["items"][0]
        checks.append((f"account {k}: its item now points at the shared brand", item_now.get("manufacturerPartyId") == shared_id and not item_now.get("manufacturerUnverified")))
    if policies:
        done = call("POST", "/admin/claims/approve", {"id": policies[0]["id"], "sourceUrl": "https://example.com/hexaquill/warranty"}, token=op)
        print("  warranty approved:", done)
    print("\n--- a fourth account brings in scenario 4 afterwards")
    email, pw, tok = rs.sign_in(); rs.add_card(tok)
    items = bring(tok, paths(4, "01", "02"))
    it = items[0]
    attached = [c for c in (call("GET", f"/purchases/{it['_purchase']['id']}", token=tok)["items"][0].get("coverages") or []) if str(c.get("kind")).lower() == "manufacturer"]
    print(f"  maker {it.get('manufacturerName')!r} shared id {it.get('manufacturerPartyId')}; coverage added on accept {[(c.get('providerName'), c.get('startDate'), c.get('endDate')) for c in attached]}")
    checks.append(("fourth account: Hexaquill is the shared brand", it.get("manufacturerPartyId") == shared_id))
    checks.append(("fourth account: the verified 24-month Hexaquill warranty was ticked and added on its own, ending 2028-09-19", any(c.get("endDate") == "2028-09-19" for c in attached)))
    finish(checks)


# ---------------------------------------------------------------- 21: a credit card the shared data does not have
def card():
    op, checks, who = rs.operator_token(), [], []
    print("operator signed in with two-step sign-in")
    for k in (1, 2, 3):
        email, pw, tok = rs.sign_in(); rs.add_card(tok)
        print(f"\n--- account {k}: {email} adds Gabe's Credit Union Rewards Visa as its own card, then brings in the Home Depot order paid with it")
        issuer = call("POST", "/parties", {"name": "Gabe's Credit Union", "isCardIssuer": True, "isSeller": False, "isManufacturer": False, "isWarrantyProvider": False}, token=tok)
        pm = call("POST", "/payment-methods", {"nickname": "Rewards Visa", "issuerPartyId": issuer["id"], "cardProduct": "Gabe's Rewards Visa", "last4": "2468"}, token=tok)
        call("PUT", f"/payment-methods/{pm['id']}/benefits", {"benefits": [{"kind": "extendedWarranty", "extendsMonths": 12, "maxTotalMonths": 48}]}, token=tok)
        items = bring(tok, paths(21, "01", "02"))
        who.append((tok, pm["id"], items[0]))
        show("claim", claims(op, "gabe"))
    cs = claims(op, "gabe")
    issuers = [c for c in cs if c["kind"] == "issuer"]
    checks.append(("before the issuer is verified: one card issuer claim with 3 accounts, ready", len(issuers) == 1 and issuers[0]["accounts"] == 3 and issuers[0]["ready"]))
    checks.append(("before the issuer is verified: no card or benefit claim yet (they wait for a shared issuer)", not [c for c in cs if c["kind"] in ("cardProduct", "cardBenefit")]))
    done = call("POST", "/admin/claims/approve", {"id": issuers[0]["id"]}, token=op)
    issuer_id = done["sharedId"]
    print("\n  issuer approved:", done)
    cs = claims(op, "gabe"); show("claim", cs)
    product = [c for c in cs if c["kind"] == "cardProduct"]
    benefit = [c for c in cs if c["kind"] == "cardBenefit"]
    checks.append(("after the issuer: a card claim of 3 accounts, ready", len(product) == 1 and product[0]["accounts"] == 3 and product[0]["ready"]))
    checks.append(("after the issuer: a benefit claim of 3 accounts, ready (extended warranty +12 months, up to 48)", len(benefit) == 1 and benefit[0]["accounts"] == 3 and benefit[0]["ready"]))
    for k, (tok, pm_id, item) in enumerate(who, 1):
        card_now = call("GET", f"/payment-methods/{pm_id}", token=tok)
        checks.append((f"account {k}: its card now points at the shared issuer", card_now.get("issuerPartyId") == issuer_id))
    if product: print("  card approved:", call("POST", "/admin/claims/approve", {"id": product[0]["id"]}, token=op))
    if benefit:
        no_source = None
        try: no_source = call("POST", "/admin/claims/approve", {"id": benefit[0]["id"]}, token=op)
        except SystemExit as e: no_source = str(e)
        checks.append(("a benefit is refused without the page the card's terms were read on", isinstance(no_source, str) and "400" in no_source))
        print("  benefit approved:", call("POST", "/admin/claims/approve", {"id": benefit[0]["id"], "sourceUrl": "https://example.com/gabes-credit-union/rewards-visa-terms"}, token=op))
    checks.append(("everything ready is decided: nothing left to review", not [c for c in claims(op, "gabe") if c["ready"]]))

    print("\n--- a fourth account picks the card from the list, then brings in the same order")
    email, pw, tok = rs.sign_in()
    catalog = call("GET", "/card-catalog", token=tok)
    entry = next((c for c in catalog if c["cardProduct"].lower() == "gabe's rewards visa"), None)
    checks.append(("fourth account: the card is in the card list under the shared issuer", entry is not None and entry["issuerPartyId"] == issuer_id))
    if entry:
        call("POST", "/payment-methods", {"nickname": "Rewards Visa", "issuerPartyId": entry["issuerPartyId"], "cardProduct": entry["cardProduct"], "last4": "2468"}, token=tok)
        items = bring(tok, paths(21, "01", "02"))
        cards = [c for c in (call("GET", f"/purchases/{items[0]['_purchase']['id']}", token=tok)["items"][0].get("coverages") or []) if str(c.get("kind")).lower() == "card"]
        print(f"  card coverage added on accept {[(c.get('providerName'), c.get('endDate')) for c in cards]}")
        checks.append(("fourth account: the card's published extended warranty was ticked and added on its own, ending 2028-10-21, without having confirmed anything", any(c.get("endDate") == "2028-10-21" for c in cards)))
    finish(checks)


if __name__ == "__main__":
    runs = {19: retailer, 20: manufacturer, 21: card}
    for n in [int(a) for a in sys.argv[1:]] or list(runs):
        print(f"\n===== Scenario {n}")
        runs[n]()
