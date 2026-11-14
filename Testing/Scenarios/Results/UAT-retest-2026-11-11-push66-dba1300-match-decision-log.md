# UAT retest: push 66 (API dba1300), match decision log (S2.8.1)

- **Build:** API `dba1300`, started 4:39 PM ET Nov 11 2026. UI unchanged since 3:25 PM ET.
- **Migration:** the `match_decisions` table exists in the dev database (checked read-only at 4:45 PM ET).
- **Run:** 4:46 to 4:56 PM ET, as Alice and Ops. The app clock was not moved and is at offset 0.
- **Scope:** CHANGES-push-66-match-decision-log.md only. "Not built yet" items were skipped.

## Summary: 2 Pass, 1 Partial, 0 Fail, 1 Not testable

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Receipt upload, same matches as before | **Pass** | `homedepot-receipt-01.pdf` gave store "Home Depot", brand "Milwaukee", item "Hammer Drill", 08/15/2026, $199, order 3456. Ticked coverage: "Home Depot return policy · Merchant · 90 days · Confirmed" and "Milwaukee warranty · Manufacturer · 5 years · Confirmed". The log rows bind "THE HOME DEPOT" to shared party `01a0f4e4-458d-7b8b…`, the same verified Home Depot as in earlier runs. No duplicate store or brand was created. |
| 2 | Accept a New Item | **Pass** | The same receipt suggested "Circular Saw · Home Depot · $149.00" with store Home Depot, brand DeWalt, "Home Depot return policy · Merchant · 90 days · Confirmed" and "DeWalt warranty · Manufacturer · 3 years · Confirmed". DeWalt bound to `01a0f4e4-458d-7ae7…` by rule key, band high. Saving it was refused with "You already have a purchase from this store with that order number." That is the existing duplicate-order guard and is unrelated to push 66. |
| 3 | Add a purchase with a document | **Partial** | `02-receipt-quick-lube-camry-synthetic-oil-change.pdf` (the scenario 69 QuickTop Lube receipt) on a hand-added purchase gave "Nothing to update: what you have already matches the document." Store, brand and item stayed blank, and no `match_decisions` row was written for it, so matching never ran. There's no earlier baseline for this file on this path; in scenario 69 it was read as a vehicle service order. **Question for CC:** should the add-purchase document read propose "QuickTop Lube" as the store? |
| 4 | Operator summary | **Pass** | Ops `GET /api/admin/match-decisions/summary?days=30` returned 200 with `{"days":30,"total":12,"counts":[{"field":"brand","rule":"key","band":"high","count":6},{"field":"brand","rule":"none","band":"low","count":2},{"field":"store","rule":"key","band":"high","count":4}]}`. Alice gets 403 on the same call. The notes' example said "store / exact / high"; the rule is actually named `key`. The brand/none/low rows are "Prime stud" (no brand match, from the Home Depot receipt's accessory line). |
| 5 | A failure to log never fails a receipt | Not testable | Covered by CC's test. |

## Observations (Low)
- **Repeated rows:** each receipt read writes the same decision several times. "THE HOME DEPOT" was logged 4 times and "Milwaukee" 4 times within about one second of a single upload. If the summary is meant to count decisions per receipt, these counts are inflated.
- **Leftover suggestion:** the Circular Saw New Item suggestion is still in Alice's New Items list.

## Cleanup
"Hammer Drill" and "P66 Synthetic oil change" were deleted at 4:55 PM ET.

## Fixtures
None new. I used existing files: `reg-982952c/rcpt/homedepot-receipt-01.pdf` and the scenario 69 fixture `02-receipt-quick-lube-camry-synthetic-oil-change.pdf`.

Screenshots and notes are on my computer in `/workspace/uat/push66/`.
