# UAT retest: push 67 (API 7051bb3), match log counts a decision once

- **Build:** API `7051bb3`, started 6:32 PM ET Nov 11 2026. UI unchanged since 3:25 PM ET.
- **Run:** 6:37 to 6:40 PM ET, as Alice. The app clock was not moved and is at offset 0.
- **Scope:** CHANGES-push-67-match-log-no-repeats.md only. The QuickTop Lube add-purchase question is logged by CC as a follow-up and was not tested.

## Summary: 2 Pass, 0 Fail

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | One receipt logs each decision once | **Pass** | I counted `match_decisions` rows read-only in Neon before and after one upload of `homedepot-receipt-01.pdf` as Alice at 6:37 PM ET. "THE HOME DEPOT" (store / key / high) went from 4 to 5, with one new row at 6:38:05 PM ET. "Milwaukee" (brand / key / high) went from 4 to 5, with one new row at 6:38:04 PM ET. In push 66 each had risen by 4 for one upload. DeWalt and "Prime stud" got no new rows; this run accepted no New Item. The Ops summary reads these same rows. I didn't call it this run because the browser run stopped at the Ops authenticator code. It was already verified in push 66 (Ops 200, Alice 403). |
| 2 | Same store and brand as before | **Pass** | Proposed store "Home Depot", brand "Milwaukee", item "Hammer Drill", 08/15/2026, $199, order 3456. Ticked coverage: "Home Depot return policy · Merchant · 90 days · Confirmed" and "Milwaukee warranty · Manufacturer · 5 years · Confirmed". The same five unticked Milwaukee "Likely" lines appeared. This is identical to push 66. The Circular Saw New Item suggestion (Home Depot, DeWalt) appeared again and was left alone. |

## Cleanup
"Hammer Drill" was deleted at about 6:40 PM ET, and Alice's My Items shows "Nothing here yet". The Circular Saw suggestions are still in Alice's New Items list.

## Fixtures
None new. I used `reg-982952c/rcpt/homedepot-receipt-01.pdf`.
