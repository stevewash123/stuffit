# Push 61: fixes from the push 60 report (2026-11-10)

API and UI. No migration.

| Change | What to check |
|---|---|
| **The plan decision's "Cost so far" no longer counts a payment the term does not hold** | Decision Care ($99 a year, Nov 10, 2025 to Nov 20, 2026): on and after Nov 10, 2026 the panel says About $99.00, not $198.00. A plan with a fixed end counts only as many billing periods as its term has (a three-year plan billed yearly still adds a payment each year; a one-year plan billed monthly is twelve, not thirteen). A plan with no end date keeps counting |
| **Kind of loss no longer leaves the last kind's fee in the box** | On a phone plan, Record a request: pick Cracked screen (fee fills 29), then a kind listed as a range: the box empties. Pick Stolen: its amount fills. If you type what you were charged, changing the kind leaves your number alone |
| **A plan with no plan type explains the missing button** | A plan with no lines and no plan type shows, in the lines card, "If you pick the kind of plan this is (Edit the plan) and it lists what it covers, you can fill these lines in with one button." It goes away once a plan type with lines is picked, or the plan has a line |

## Checked and not changed
- **End this plan with today's date.** The server ends a plan dated today (status "ended", end date today); it is covered by a new test. The confirm dialog opens outside the page area, so a click on the page behind it can miss it. If the plan still says "No fixed end date" after you confirm in the dialog, please report it with a screenshot of the dialog.
- The decision panel's Service requests line uses dots between its parts; the notes' commas were wording, not a requirement.
