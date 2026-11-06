# What changed in push 26: a typed coverage is kept on a vehicle; "probably replaced" note; a term in days ends on that day (2026-11-06)

For GrokBot. API `28b0f24` and UI `8e9329b`. Check `/api/version` (`commit` must be `28b0f24`); the UI has no version marker, so record its Last-Modified and use the "Your own entry may be out of date" note (below) as proof it is deployed. Migration `CoverageSupersededDismissal` is applied to staging. No reference seed change.

## Fixed (from your push 23 and push 25 results)
| Where | What |
|---|---|
| Vehicle, **Read it / apply a warranty document** (S61 D29) | Coverages you typed in yourself (Powertrain, Bumper-to-bumper, Roadside...) are **kept**. The document's warranty is added beside them. Before, applying a document removed all of them. Appliances are unchanged: a document's maker warranty still replaces the maker warranty on an ordinary item |
| A warranty given in **days** (S54 16b, "90 days" vs Jan 20) | "90 days" now ends 90 days after the start: bought Oct 20, 2026 ends **Jan 18, 2027** (it was Jan 20, three calendar months). Only a term whose words say days; "3 months" and "1 year" are unchanged |
| Entering a warranty **start date** (S3.5.4 / S54 step 7) | The Notifications badge in the header is counted again at once. The "Enter the date..." notification is finished when you save the date |

## New: "probably replaced" note for a coverage you typed in
A maker warranty you **typed** (or typed and then changed), on an ordinary item (not a vehicle), when a maker warranty **read from a document you attached** also exists for the same item.
- **Your items** (the list): under the item card, a note **"Your own entry may be out of date"** with an **X** to dismiss it. The dismissal is saved: reload the page and it stays gone; sign in elsewhere and it is still gone. It comes back only if a different, newer document warranty appears.
- **Item page**: on the typed coverage's row, an amber badge **"Probably replaced by the policy read from your document"**. It has no X.
- **Not shown on a vehicle** (a vehicle keeps both), and not for a coverage that came from a document itself.
- Steps: add an appliance, add a maker warranty **by hand** (Edit > Add coverage), then attach a warranty paper and accept its warranty. Open Your items: the note is under the card. Press X, reload: it stays gone. Open the item page: the amber badge is on the typed row. Repeat on a vehicle: neither shows.
- Another account opening the dismiss link for your coverage gets Not found.

## Retest
1. The note and the badge above (steps in that section).
2. Scenario 61 step 29/D29 again: on the truck with three hand-typed maker coverages, apply a warranty document. Expect four maker coverages (your three, plus the document's).
3. Scenario 54 step 16b: base coverage for `edge-registration-required.pdf` now ends on Jan 18, 2027 when bought Oct 20, 2026 (it said "90 days").

## Not changed, do not report as new
- The application receipt text ("Applied ... from 2026-01-01") still shows the purchase-based dates after an in-service date is entered.
- A to-do due "in 15 days" where the plan says 14 (a one-day difference in counting).
- Add a purchase and New Items do **not** show this note: neither screen shows a coverage you typed. A verified shared warranty will trigger the note later; it does not yet.
- Bill-of-sale reader missing the model; the "last reading 14 months ago" label on the estimated-miles line; certified coverage length not auto-calculating an end date (the end date is worked out when you save).
