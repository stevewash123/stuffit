# Scenario 73: Leased vehicle — end date, mileage notices, GAP note

**Accounts:** one **personal** account only (P34 Self, or Alice's personal account if it exists). Do not run this in the shared business P34-Alice Repairs.
**Preconditions:** clock offset **0**, app date **2026-11-11** (America/New_York). Honda / **CR-V** is in the seeded model list (push 37 `--seed`). Type the dealer **UAT Riverstone Honda** (it is not a seeded dealer; a typed dealer is saved as the person's own). **QA Controller must OK the clock advances.** They are large and global: +124 days, then a jump to +947 days. A lease-mileage point missed by more than 14 days is skipped (push 37), so the year-2 halfway point is **expected to be skipped** on that second jump. Reset the clock to **0** at the end. Reader on, or record **reader off**. Lease-agreement **reading is not built** (push 37: "Payment-plan details and lease-agreement reading are not built"); enter the lease fields by hand and keep the PDF as an item document.
**Time:** about 30 min, plus the clock steps.
**Built per:** push 37 (leased vehicles, lease-end to-do, lease mileage notices, GAP / refund note); push 38 (lease line shows "$0.25 per mile over"; Paid by is shown on the vehicle page; in-service date on Add).
**Why this plan:** people miss lease-end dates and over-mileage fees. If they bought GAP coverage or an extended warranty and the lease ends early, they may be owed a refund and need a prompt to check with the dealer or lender.

## The story (answer key)

| Fact | Value |
|---|---|
| Item name | **UAT S73 Honda CR-V lease** |
| Year / make / model / trim | 2026 Honda / CR-V EX-L AWD (Honda and CR-V are seeded; type the trim if the list has no EX-L) |
| VIN | `5J6RW2H80TL007741` (synthetic, valid check digit) |
| Dealer | **UAT Riverstone Honda**, 173 Example Auto Mile, Testville, ME 00000, (207) 555-0173 |
| Customer on paper | UAT Sample Buyer, 73 Example Lane, Testville, ME 00000, (207) 555-0173 |
| Date obtained / in service | **2026-09-15** (odometer at delivery: 12 miles) |
| You have it | **Leased** (not Bought) |
| Lease ends | **2029-09-15** (36 months) |
| Allowed per year | **12,000** miles |
| Fee per mile over | **$0.25** |
| Paid by | **Payment plan** |
| Contract / stock | UL-073-36-260915 / RS-260915-073 |
| Halfway through year 1 | **2027-03-15** (offset **124** from 2026-11-11) |
| Halfway through year 2 | **2028-03-15** — **skipped** on this run (the jump to 2029-06-15 misses it by more than 14 days; push 37) |
| Three months before the end | **2029-06-15** (offset **947**) |
| 90 days before the end (to-do nudge) | **2029-06-17** (offset **949**) |

## Files, in the order to use them

Each file is one PDF plus a JPG of its first page with the same name. The lease agreement is **optional** as a document on the item; the lease fields are still typed on the form.

| # | File (.pdf + .jpg) | What it is | Who uploads it, and when | Where it goes |
|---|---|---|---|---|
| 01 | `01-lease-agreement-honda-crv` | One-page closed-end lease dated 09/15/2026, 36 months, 12,000 miles a year, $0.25 over | The tester, step 1, offset 0 | Vehicle document. **Do not expect Read it to fill the lease fields** (not built, push 37) |

## Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Tester | Confirm the **personal** account and offset **0**. Add > Vehicle. Make **Honda**, model **CR-V** (trim EX-L if asked), year 2026, **Leased**, lease ends **2029-09-15**, allowed **12,000** a year, fee **$0.25**, date obtained / in service **2026-09-15**, odometer 12, VIN from the key, dealer **UAT Riverstone Honda**, **Paid by: Payment plan**. Name it **UAT S73 Honda CR-V lease**. Attach PDF **01** as a document (no need to accept extracted lease terms) | The vehicle is saved. If a past date is refused, stop and record **Blocked: past purchase date**. A lease that ends before the date obtained is refused (400, `leaseEndDate`) (push 37) |
| 2 | Tester | Open the vehicle page | The lease line reads along the lines of **"Leased until Sep 15, 2029 · 12,000 miles a year allowed"** and **"$0.25 per mile over"** (push 38). **Paid by payment plan** is shown (push 38). The GAP note is present, wording from push 37: **"If you bought GAP coverage or an extended warranty with this car, you may be owed a partial refund. Check with your dealer or lender."** To do has one item: **"<vehicle>: your lease ends soon"** (or equivalent), **due on 2029-09-15**, not yet nudging (90-day nudge starts 2029-06-17). WarrantyCat does **not** try to track miles against the allowance (push 37, deliberate) |
| 3 | QA Controller / Tester | **With QA Controller's OK:** `POST /api/maintenance/clock/advance?days=124`. Offset **124**, app date **2027-03-15**. After reminder time, run reminders. Run them again the same day. Reload Notifications and mail | **One** "halfway through a lease year" **lease mileage** notice, once per owner per point (push 37). A second run the same day sends **none**. Category is Expiring; the type can be turned off for email in Settings, but the in-app notice still appears if that channel is on. The lease-end to-do is still in the future |
| 4 | QA Controller / Tester | Advance to offset **947** (`advance?days=823` from 124, or the equivalent from the current offset). App date **2029-06-15**. After reminder time, run reminders | **One** mileage-check notice **three months before the end**. **No** late year-2 halfway notice (2028-03-15 was missed by more than 14 days and must be skipped, push 37). The lease-end to-do is two days short of its 90-day nudge. Optional: advance **2** more days (offset **949**, 2029-06-17) and confirm the to-do is now nudging |
| 5 | Tester | Still on the advanced clock, **Edit** the vehicle and change **You have it** to **Bought**. Save. Reload the vehicle and To do | The lease line, overage fee, GAP note and the lease-end to-do **go away** (push 37: choosing Bought or clearing the end date finishes the to-do). The vehicle and the attached lease PDF remain. Then ask QA Controller to `POST /api/maintenance/clock/reset` to **offset 0** |
| 6 | Test2 (optional) | From Bob's personal account, paste the vehicle address | Not found or no access |

## What to check, in short

1. Lease fields, the lease line, **$0.25 per mile over**, Paid by, and the **GAP / refund note** all show as in pushes 37 and 38.
2. One lease-end to-do, due on the end date, nudging from 90 days before.
3. Mileage notices once at first-year halfway and once three months before the end; a missed point is skipped; no duplicates the same day.
4. Changing to Bought clears the lease line and the to-do.
5. Reset the clock to 0.

## Cleanup

- Delete **UAT S73 Honda CR-V lease** and its document, notices and to-dos, in the personal account only. The typed dealer **UAT Riverstone Honda** is account-owned test data; leave it for DB Stager.
- **Clock must be offset 0.** The second jump lands in June 2029 until it is reset. Ask QA Controller if it is not already 0.

## Checked when this was made

- Built 2026-11-11 on the box (`generate_all.py` in `/workspace/uat/scen-71-74/`). Contract number, VIN, lease start and end, 12,000 miles, $0.25 per mile, dealer and customer names were found in the PDF text layer (`validation.json`). The JPG twin was checked by eye. The VIN check digit was computed (it is 0).
- The date obtained, 2026-09-15, is in the past at step 1 (app date 2026-11-11).
- No app, database write, mail or sign-in was used to build the pack.

## Known rough edges and open questions for CC (not part of the answer key)

- **Lease-agreement reading is not built** (push 37). If a later build starts filling lease fields from file 01, record what it picks up; do not fail this pack for leaving them to hand entry.
- **Halfway vs calendar months.** This pack treats 2026-09-15 + 6 months as 2027-03-15. If the job uses 182 days or another rule, land within 14 days of the actual point or the notice will be skipped.
- **90-day nudge vs three-month mileage notice** fall two days apart (2029-06-17 vs 2029-06-15). Confirm they are two different things: a to-do vs a mileage-check notice.
- **Wording** of the mileage notice and the to-do title may differ slightly from the push 37 examples. Pass if the meaning matches.
- **Clock:** +947 days moves every account into mid-2029 and will break other time-sensitive tests until reset. Run this one alone, with QA Controller's OK, and reset to 0.
