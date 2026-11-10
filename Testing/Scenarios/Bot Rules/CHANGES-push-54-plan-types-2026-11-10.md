# Push 54: plan types, and the push 53 wipers row (2026-11-10)

Story S3.4.5, first slice. API and UI. Migration `PlanTypes` (reshapes the unused `plan_types` table; adds `plan_type_id` and `serviced_by_party_id` to `warranty_plans`).

## Push 53 Partial: the wipers row
| Change | What to check |
|---|---|
| A job already added by hand still shows on the card when it is the only job left out | F-150 order 06: after adding the wipers by hand, Read it again: the wipers appear as "Wiper blades ... already added by you" (no tick box). The "N other jobs were left out" sentence appears only when something is still left out |

## Known, not fixed in this build
- Push 53 order 08 (Tucson collision repair) still lists no jobs. The reader was re-run with the new wording (the stored reading is keyed by the prompt, so it was not reused) and returned no jobs. Waiting on a live reader check before changing the wording again.

## Plan types
| Change | What to check |
|---|---|
| **Operator page:** Admin > Companies > type "Extended warranty plans (plan types)" | Lists plan types (default "Needs confirming"). **Add a plan type**: choose the company that sells it, name, what it covers, exclusions, waiting days, fee range, billing, published price note, cancelling, optional "claims serviced by" company. Save with no page address: it shows "Not confirmed yet". **Confirm** needs the address of the company's own page (https). A bad or empty address is refused |
| A plain account cannot use the operator page or endpoints | Sign in as a normal user: `/admin/companies` is not available |
| **Plan form picker:** Add a plan, choose a company that has plan types | A "What kind of plan is it?" select appears under the company, listing the company's types. Unconfirmed ones read "(not checked yet)". With no types for the company there is no select |
| Picking a type fills only what is blank | Type your own "What it covers" first, then pick: yours stays; the exclusions, waiting period and kind fill in, with a note "Filled in ... from <company>'s record ..., not from your contract" and, when set, "Claims are handled by <company>" |
| Your contract wins | The contract's dates, price, contract number and fee are never filled from a type |
| The pick is saved on the plan | Save, reopen: the same type is selected. Change the company: the type is cleared |
| A change to a type that people's plans use becomes a new version | Operator: Change a type that a plan uses: a note says "N plans use this. Saving makes a new version from the date below". Pick a start date. Afterwards the old version still has the old words and the plan keeps pointing at it |
| A type nobody uses is corrected in place | Change a type with no plans: no new version |

## Not built yet (do not report)
- "Plans they sell" on each company's page, the person-facing "add my own plan type" screen (the API for it exists), the candidate queue for people's own types, a seeded list of providers, and matching a plan read from a receipt to a type.
- The company picker on both pages only offers companies with the warranty-provider role; stores and makers selling plans come next.
- Phone and device insurance and home appliance plans (S3.4.19, S3.4.20).
