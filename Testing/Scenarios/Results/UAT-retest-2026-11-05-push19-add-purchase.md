# UAT retest: push 19 lifetime offer on Add a purchase
Build: API `afc90db` (started 2026-11-05T12:54:35Z / ~7:54 AM ET). UI Last-Modified unchanged Thu, 05 Nov 2026 10:50:29 UTC (API-only). Mode: Full-only. Tested ~8:07–8:09 AM ET Nov 5.
Notes: `CHANGES-push-19-lifetime-offer-on-add-purchase-2026-11-05.md`. Alice scenario-reset by DB Stager just before the run (0 items).

## Headline
Add a purchase now shows **Manufacturer's warranty found** for `standard-lifetime-limited-reel.pdf`. Saved item matches the item-paperwork door. A grocery non-warranty PDF offered nothing (no invented length/lifetime); it did not say the words "no clear length".

## Retest rows
| # | Result | Notes |
|---|---|---|
| 1. Add a purchase + lifetime PDF | **Pass** | Box **"Manufacturer's warranty found"** with exact text "PENN Fishing Tackle: Lifetime, with no end date, counted from the purchase date." Ticked checkbox "Add this warranty to the item when I save". Brand auto-filled Penn. Catalog 1-year Penn also ticked by default on the form (not saved — see #2). |
| 2. Save → item page | **Pass** | Item https://stuffit-ui.onrender.com/items/01a1abd3-2cbf-7997-b8fc-532c3f9489a1. Badge **Lifetime, can end**; start Jun 1, 2026; no end date. "Lifetime of the product. Original purchaser only. Not transferable. The maker decides when it has worn out." Proof: "Asks for: proof of purchase. Nothing says the original paper is required." Matches paperwork door. **Difference to note:** form had catalog 1-year ticked too, but item shows only the lifetime ("Covered · 1 policy"); catalog 1-year was not saved. Looks intended; confirm if needed. |
| 3. Doc with neither length nor lifetime | **Partial** | Attached `09-thermal-grocery-nonwarranty.pdf` as Receipt. No Manufacturer's warranty found, no lifetime, no length invented. Coverage area: "Nothing found yet. Pick the store, brand, category and card to see what applies." Toast filled store/price/date from receipt. Page never said "no clear length" in words — offered nothing, so no false coverage. Not saved. |

## Do not report as new (per notes)
- `edge-registration-required.pdf` gap (conditional term) — known, not in this push.
- Not built: yearly check-in, given away/sold, proof list, component lifetime.
- Items/Home "Active" for lifetime-only.

## State left
Alice signed in with 1 item (UAT Penn Reel, lifetime). Unsaved grocery Add a purchase form may still be open in the browser.

**Totals:** 2 Pass, 1 Partial, 0 Fail.
