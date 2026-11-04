# What changed in push 11: fixes from the push 9 retest of Scenario 51 (2026-11-04)

For GrokBot. API and UI commits are named in the push message; check `/api/version` and record it. No migration. Re-run Scenario 51 steps 11, 12 and 13, and look at Home.

| Change | What you should see | Your step |
|---|---|---|
| Plan refund on the item | On the item a plan covers, **Money recovered** lists the plan's refund ("Plan refund", the amount, the date, the method) with the plan's name as a link, "change it on the plan". It has no edit or remove buttons there; you change or re-open it on the plan page | 11, 12 |
| Home "on N items" | The Home recovered total counts the items the plan covers, so a plan refund over one item reads "on 1 item", not "on 0 items" | 11 |
| Home plan tile | A cancelled plan is no longer counted as running: the tile and its "N running" line leave it out | 13 |

## Decided, do not report
- **Step 1:** the quick "Add protection plan" drawer has no renewal or length fields by design; use the full form (the scenario now says so).
- **Step 7:** Undo is offered for 10 seconds and then goes; the screen does not print the number. "How" is free text on purpose.
- **Step 18:** Bob has no cancel buttons, so only the not-found pages are checkable.
- **"1 suggested policy to review"** on an item with no coverages is the maker's warranty suggestion, as before.
