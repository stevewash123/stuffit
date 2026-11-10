# Push 51: tire and part terms on repair orders, jobs past a mile limit (2026-11-10)

API only. No migration. Answers the two High findings in the Scenario 69 report (UAT-run-2026-11-09-scenario69-efdd913). The reader prompts changed (triage-v5, document-v24, service-record-v4), so **read the files again** (a document read before this build keeps its old reading).

## What changed
| Change | What to check |
|---|---|
| A tire shop or parts-and-labor invoice that names the vehicle (VIN, year and model, or mileage in) and bills tires mounted, balanced, rotated, aligned or repaired is read as a **service order**, not a purchase | Scenario 69 order 05 (new tires): Read it on the F-150. It should now offer the "Service on covered parts" card, not the "Brand Conflict / Date Conflict" purchase card that proposes overwriting the truck |
| The repair-order card matches work to the vehicle's **parts' own terms** (the tires' Michelin treadwear term and the road hazard plan), and the coverage picker offers them | Order 06: the rotation is kept on the treadwear term, the flat repair on the road hazard plan, wipers stay left out. The picker (when you tick a left-out job) lists the tire terms beside the truck's. Part terms are named for who gave them ("Michelin warranty (to Jul 22, 2031)", "Tread Masters protection plan (to Jul 22, 2028)") |
| A job paid by a **protection plan, road hazard plan or service contract** counts as paid by coverage | Order 06 flat repair shows "repaired under warranty" (customer $0) |
| A job done **past a coverage's mile limit** is not pinned to that coverage, even if its date still runs | Order 07 (Outback, 61,240 mi, goodwill CVT): kept, but with **no coverage named**. Order 12 (41,120 mi) still goes to the powertrain term |
| Work the order calls a **recall** or **goodwill** names no coverage | Order 03 recall (rearview camera module): kept as repaired under warranty, no bumper-to-bumper named. Order 09's warranty **campaign** is unchanged (still goes to the powertrain term) |
| Coverage names in the history use the **document's own end date**, not the date the miles moved the end to | After a high reading ends the Outback powertrain on miles, the card, the picker and new history entries say "Powertrain (to Nov 20, 2026)", the date on the paper, not "(to Oct 14, 2026)" |

## Decided, do not report
- The powertrain end date moving earlier when an earlier over-limit reading is added (order 07's 61,240 on Oct 14 beats the Nov 9 reading): an entered reading at or over the limit ends the coverage the day before it. The first such reading wins, so an older one can move the end earlier. It is evidence, not instability.
- The badge date after a high reading is the day before the first reading at or over the limit, not the date the 60,000th mile passed: the app only knows the readings it was given.
- Entries already saved (including the "Manufacturer warranty (to Nov 8, 2026)" ones from earlier runs) keep the wording they were saved with; only new ones use the new names. Re-adding an order replaces the entries the rules kept, so re-reading and adding it again refreshes those labels.

## Not done (do not report as new)
- A Maintenance panel on parts (the tire rotation "7,500 mi" check), the missing wiper row on order 06's left-out list, order 08's missing "N other jobs were left out" line, and the other Low items in the report.
- Un-keeping a job on the card. Use Not now and add the right jobs, or delete the entry from the history.
