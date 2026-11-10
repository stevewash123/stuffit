# Push 57: Plans they sell, stores and makers as plan sellers, and collision orders (2026-11-10)

Story S3.4.5 (UI) and one repair-order rule (API). No migration.

| Change | What to check |
|---|---|
| **Plans they sell** on a company's page | Open a company that has plan types (the Hearthside-style company you made in push 54), either through Admin > Shared data > the company, or Settings > Stores & brands. A "Plans they sell" card lists each plan type: name, status ("Confirmed from the company's page" / "Not checked yet"), price note, "claims go to <company>", waiting period, service fee range, what it covers, cancelling, and a "Where this was read" link when there is one |
| A company with no plan types | A person sees no "Plans they sell" card. An operator (Admin > Shared data > the company) sees the card with "No plans recorded for this company yet." and "Add or confirm plan types" linking to Admin > Companies > plan types |
| **Stores and makers can sell plans** | In the plan form (Add a plan) and in the operator plan type form, the company picker now finds stores, makers and warranty companies together. Search for a store (for example Best Buy) in "Sold by": it is offered. Adding a brand-new company from either picker makes it a warranty company |
| A plan type from a store | Operator: add a plan type sold by a store, with a servicing company; confirm it with a page address. Add a plan sold by that store: the "What kind of plan is it?" select lists it |

## Push 55 Medium: a collision repair is not warranty service
| Change | What to check |
|---|---|
| On a collision or body-shop order, jobs are no longer kept under the factory warranty | Tucson order 08 (Precision Collision Center): Read it. The card now keeps **nothing** and lists every job under "N other jobs were left out" with tick boxes (bumper cover, refinish, A/C condenser, recharge, radar calibration, alignment, paint materials, hazardous waste). The odometer reading is still offered. A job the order says warranty paid for would still be kept |
| An ordinary dealer order is unchanged | Orders 03, 06, 07, 09, 12: same keeps as push 56. A single paint job on a dealer order does not turn it into a collision repair |
How an order counts as collision work: the shop name says collision or body shop, or two or more of its jobs are paint, refinish or body panels.

## Not built yet (do not report)
- A person adding their own plan type from the app (the API exists), matching a receipt's plan line to a type, a seeded provider list, the item quick-add dialog's type select.
- Phone and device insurance and home appliance plans (S3.4.19, S3.4.20).
