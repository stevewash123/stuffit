# What changed in push 40: Read it fixes (2026-11-09)

For GrokBot. Check `/api/version` against the pushed API commit. API only. No migration, no `--seed`. Targeted retest only: S63, S64, S65. The reader prompt changed, so these are live-reader checks.

## Fixed from the push 37 reports
- **S63 powertrain mile limit (item 1):** a part of a vehicle warranty can carry its own mile limit. Read it on the Ford warranty should give the whole vehicle 36 months / 36,000 miles and the Powertrain part 60 months / 60,000 miles ("59,982 left" at 18 miles). The reader writes a part as `name | parts months | labor months | mile limit`. The limit only counts on a vehicle.
- **S64 protection plan (item 2):** Read it on a protection plan paper from the item page now makes a plan record, covering the item, with Company, Plan name, Contract number, Price, Service fee, claim phone and website, and the start answer ("Same day as the purchase" when it starts on the purchase date, otherwise "Another date"). It no longer leaves a bare coverage under "Needs details". A paper that names no company still makes the bare coverage. The coverage keeps the document's wording and its mile limit.
- **S64 certificate with two terms (item 3):** Read it on a certificate that gives separate terms (Comprehensive 12 months / 12,000 miles, Powertrain 24 months / 24,000 miles, from 28,400) makes one certified coverage per term, each with its own end date, mile limit and start odometer (ends at 40,400 and 52,400 miles). They are labelled certified or dealer-added, never merged into the factory coverages, and are not offered to shared data. New reader fields: `terms` and `certified`.
- **S65 model name (item 4):** "Pro Team 175 TXW" should stay whole in the model, with no Size "175" and Model number "TXW" split (prompt change).

## Not changed, do not report
- The Certified box is still not offered when a Protection plan is added by hand: a plan record cannot carry it. Enter a certified coverage as a manufacturer or dealer coverage, or use Read it.
- Part form: no year field and no "came with the boat" option (not built).
- Push 38 finding 2 (boat in-service date showing 2025): not reproduced from the code; retest as in the push 39 notes.
- The other Read it items: model and trim suggestions on S63, and Read it before saving on Add.

## Tests at push
API unit 1212. Integration 509 (+2 opt-in skipped) passed on the branch before the last prompt-only commit. Added: part mile limit and term parsing, plan from a document (S64 plan), certificate with two terms.
