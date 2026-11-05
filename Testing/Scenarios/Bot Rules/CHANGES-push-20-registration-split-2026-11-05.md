# What changed in push 20: a registration condition splits a warranty into two coverages (2026-11-05)

For GrokBot. API and UI; check `/api/version` and record it. The migration `ConditionalCoverage` is applied to the staging database. Story S3.1.13. Run **Scenario 54 Part B** (rewritten for this; steps 14 to 19c). The reader prompt changed (version 5): please also re-open **one plain warranty document you have used before** (for example Scenario 53 or 55) and say whether anything reads differently from last time.

## What you should see
| Where | What |
|---|---|
| Upload `edge-registration-required.pdf` (item page, Add a purchase, or New Items) | Two coverages proposed: the **90-day** term, **ticked**, and "3 years if you register within 30 days", **not ticked**, with the document's condition quoted. A quick add never attaches the optional one |
| Item page, optional coverage not yet earned | "3 years if you register by <date>. Not counted yet." It is left out of days left, the item's status, Home counts, end-date reminders and claim guidance. The 90 days counts on its own |
| The to-do | "Register <item> by <date> to extend the warranty to 3 years", due three days before the deadline, with the usual reminder. No to-do for an unticked optional coverage |
| **I registered** | Asks for the date (today by default). The 3-year term becomes active and replaces the 90 days for counts and reminders; the 90-day coverage stays in the list marked "replaced by ...". **Undo** brings the 90 days back. The to-do is finished |
| After the deadline | "Not earned: the registration window ended <date>"; the to-do is closed as missed (kept). **I registered** then asks you to confirm you registered in time, with a date on or before the deadline; a later date is refused |
| A document with a longer term but **no stated condition** (or a condition with no length) | Nothing is split: one coverage, as before |
| Export (`coverage.csv`) | Seven new columns: condition text and kind, deadline, met-on, confirmed-after-deadline, and more |

## Not built, mark Not built (not Fail)
- Shared (community) policies with a registration rule: the item gets the long term alone, as before.
- Adding the optional coverage by hand: it is added only by re-reading the stored document from the item page (Read it).
- The old "Not sure" answer is gone: the to-do and its deadline do that job.

## Also noted
- The base term reads "90 days" as 3 months, so it ends 2027-01-20, two days after the key's 2027-01-18. Report only if the two coverages disagree with each other.
- A fix inside this push: ticked suggestions in Add Details on a New Item used to create nothing for some document suggestions; they now do. Report anything odd there.

## Decided, do not report
- Items list and Home "Active" for a lifetime-only item; yearly check-in, given away or sold, the proof-held list and a lifetime on one component are not built.
