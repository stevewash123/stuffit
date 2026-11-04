# What changed in push 7: the paperwork route and the push 6 retest fixes (2026-11-03)

For GrokBot. Push 7 is API `bbc006b` / UI `5245689`. It follows your retest of `ba04c85`. Check `/api/version` shows `bbc006b` (UI `5245689`) and record it. No migration. **Before you start, add the two categories in `DATA-categories-tablets-and-services-2026-11-03.md`** (they are in the seed, which runs only with `--seed`, not on a normal start; use the SQL there). Use Alice and Bob after a DB Stager scenario reset.

Run the rows below; the data rows for C-0 and B-8 are in the data file.

## Changes
| Change | What you should see | Your row |
|---|---|---|
| Paperwork route | Item page > Add-on protection > Add > **I have the paperwork or a photo** now opens the **plan form** (`/plans/new?item=...&paperwork=1`), not edit mode, with the file picker open. Choose the file: it is read at once, the plan is ticked for this item, the company is matched or filled in with "add as new", and the file is kept as the plan's proof. Add makes a real plan (it appears under Protection plans), not a bare coverage | C-3 / C43-8 |
| One payment label | A price paid once reads "$299.99 one payment" on the plan form note and in the reading review. "Paid 299.99" and "a year" do not appear on this route | C-3 / C43-9 |
| Edited receipt plan values stay | On Add Details: edit a receipt plan's price (49.99 to 54.99), untick, reload, tick again: the field shows **54.99** (kept per browser, same browser only) | A-5 |
| Not verified on the plan | A plan whose company you added yourself (not in our list) shows an **Unverified** marker on the plan page and on the Protection plans list. A company from the shared list shows none | B-7 note |
| Money in updates | "Update from a newer document" shows new money values as `$95.00`, matching "Saved now: $75.00" | D-3 |
| Lowe's row wording | The no-company plan row says "Add the company in Add Details, or from the to-do after you add it." | B-1 |
| No renewal to-do for an ended plan | A plan (or insurance policy) whose end day has already passed gets **no** "Renew or replace it" to-do, and an existing one is removed. Plans ending today or later behave as before | Other finding 1 |
| New categories | **Tablets** (under Electronics) and **Subscriptions and services** (top level) exist; see the data file for the rows to run | C-0, B-8 |

## Not changed, checked
- **"2 suggested policies to review" on the headphones (finding 5)** is not a bug. The count is the unreviewed suggestions that remain after the plan is made: the maker's warranty (and any card benefit), which are separate from the plan. Setting aside or accepting them takes the count to 0. A plan made from the receipt adds no suggestion of its own. If you saw a count that did not drop after you acted on those suggestions, say which two it listed.
- **Item card "Active" at 42 days (C-8)** is as designed: the card's "Ending soon" starts at 30 days; the Home tile and filter use 60 days ("ends within 60 days").
- **`clock/status` 401 (D-11)** is the maintenance key on your side, not this build.

## Decided, do not report
- Everything in "Decided, do not report" in the push 4, 5 and 6 notes still holds.

## Still open, do not report as new
- Cancel, renew and refund of a plan, a plan bought later, an item returned or replaced under a plan, phone-insurance deductibles and claim caps, appliance-plan limits, home-warranty service requests (Scenarios 45 to 47, 49, 50): not built.
- The quick-add toast does not name the plan; a plan on a multi-item receipt whose line cannot be matched is not attached.
- The paperwork route needs the live reader; a reader miss is Partial, quote what it read.
