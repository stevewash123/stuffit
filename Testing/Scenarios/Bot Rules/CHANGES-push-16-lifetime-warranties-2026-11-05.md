# What changed in push 16: lifetime warranties and the proof a warranty asks for (2026-11-05)

For GrokBot. API and UI commits are named in the push message; check `/api/version` and record it. Stories S3.1.8 and S3.1.9. The migration `LifetimeCoverage` is already applied to the staging database. Run **Scenario 55** (updated; its header lists what is not built). Scenarios 52 to 54, 56 and 57 are not part of this push.

## What you should see
| Where | What |
|---|---|
| Add a warranty from a document that says "lifetime" with no number of months | The suggestion is **Lifetime**, with **no end date** (not 0, not a number of years). It carries whose lifetime (the product, the product line, the original purchaser, or **not stated**) and whether it can be passed on (transferable, not transferable, once or for a fee, or **not stated**). Nothing is guessed: a document that is silent shows "not stated" |
| Item page, lifetime coverage | A **Lifetime, can end** badge (not a permanent green tick); plain words such as "Lifetime of the product. Original purchaser only. Not transferable. The maker decides when it has worn out."; a **What could end it** list; no end date, years remaining, days left or yearly cost; no reminder is ever created for it |
| Item page, proof | "Asks for: proof of purchase. Nothing says the original paper is required." or, when the document says so, "Asks for the original receipt. Keep the paper." The original-receipt wording is never softened to "any proof" |
| Edit a coverage | A lifetime checkbox (hides Ends and Length); whose lifetime, transfer and proof can be corrected. A corrected value reads "You entered or corrected: ..." and a later re-read of the document never overwrites it |
| **End this coverage** (item page) | Choose a reason (given away or sold, the maker dropped the model, the claim was refused as worn out, the owner died, other) and a date. It then shows as expired with the reason, keeps its history, and its last covered day is the day before the date. **Re-open** brings it back |
| Claim guidance ("Something broke") | Shows the lifetime term, the exclusions and the proof asked, with "This is what your document says. The company decides in practice." No promise of acceptance |
| Export (`coverage.csv`) | New columns: lifetime ("Lifetime"), lifetime_scope, transferability, proof_asked, entered_by_you, ended_reason, ended_on |

## Not built, mark Not built (not Fail)
- The yearly "still covered? still have the receipt?" check-in (Scenario 55 step 8).
- Given away or sold, and Undo (steps 10 and 11): there is no such flow. "Mark disposed" means thrown out, which is not the same.
- The list of what WarrantyCat holds that could serve as proof (part of step 5).
- A lifetime on one component, for example the dishwasher tub "lifetime against rust-through" in the kitchen-suite document (step 12): expect it to stay as text or be missed.
- The items list and Home badge for an item with only a lifetime coverage still read "Active"; "Lifetime, can end" shows on the item page only.

## Report, in the usual way
- Any end date, years-remaining or number of years on a lifetime line; "Lifetime" shown as permanent; any claim of transferability the document does not make; a lifetime coverage that shows as expired without being ended; wording that promises a repair.
- The real reader's output varies from day to day: where a step relies on the document being read, say what you saw and grade Partial rather than Fail if the wording differs but nothing is guessed.

## Decided, do not report
- After a correction, the source reads "You entered or corrected", not "document did not say" (the document's original value is not kept once corrected).
- Monthly and Yearly plans are placeholders; no Founders option yet.
