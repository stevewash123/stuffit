# Scenario 63: New dealer car, buyer's order and separate factory warranty (happy path)

**Accounts:** Test1 (Alice); Test2 (Bob) only for optional isolation check.
**Preconditions:** Use Test1's **personal account**, not P34-Alice Repairs. No reset required; names below are unique. Clock offset **0**, app date **2026-11-08** (America/New_York). Push 37 vehicle form and vehicle coverage migrations applied. Ford / Bronco is in the shared model seed. Reader on; otherwise record **reader off**. Documents here are synthetic test transactions, not official current manufacturer policies.
**Time:** 25 min
**Built per:** Scenario 1 full-document format; Scenario 61; pushes 23, 25, 26 and 37.
**Why this plan:** a normal new-car purchase supplies the money and identity on one paper and the two standard factory clocks on another. Neither the tax-inclusive receipt total nor the longer powertrain term should replace the vehicle price or whole-car term.

## The purchase (answer key)

| Fact | Value |
|---|---|
| Item / category / kind | **UAT P38 S63 New Bronco** / Vehicles / Car (SUV) |
| Make / model / year / trim | **Ford / Bronco / 2026 / Big Bend**; maker and model confirmed in `p37-vehicle-seed-manifest.json` |
| Seller | **UAT Pine Ridge Ford**, fictional franchise dealer; 100 Example Dealer Way, Testville, ME 00000 |
| Condition / ownership / payment | New / Bought / Cash or check |
| Purchase / first in service | **2026-11-07 / 2026-11-07** |
| VIN / first reading | `1UATB1BH0T0000063` (synthetic, 17 characters, not a registered VIN); **18 miles on 2026-11-07** |
| Vehicle price / tax / fees / paid total | **$42,500.00 / $2,550.00 / $250.00 / $45,300.00**. Enter vehicle price $42,500, excluding tax and fees; retain gross paid total on the paper |
| Provider / coverage origin | **Ford / Came with the product**, manufacturer's limited warranty |
| Bumper-to-bumper | Whole vehicle, parts and labor: **2026-11-07 to 2029-11-07**, or **36,000 total odometer miles**, whichever first; $0 deductible |
| Powertrain | Engine, transmission, drive axle, parts and labor: **2026-11-07 to 2031-11-07**, or **60,000 total odometer miles**, whichever first; $0 deductible |
| Distance arithmetic | At delivery, **35,982** and **59,982** miles remain respectively. Limits are not 36,018 / 60,018 |
| Transfer / registration / plans | Transferable remaining term; registration not required; no purchased plan or stated return window |

## Files, in the order to use them

Paths below are relative to this scenario folder. Do not upload text sidecars or preview PNGs.

| # | File | What it is | Where it goes |
|---|---|---|---|
| 1 | `01-buyers-order-ford-bronco.pdf` | One-page dealer delivery order with tax, fees and signature lines | Add > Vehicle attachment; or attach to the saved vehicle |
| 2 | `02-ford-new-vehicle-warranty.pdf` | Two-page factory specimen: schedule, coverage terms and service procedure | Saved vehicle > papers > Read it |
| 2a | `02-ford-new-vehicle-warranty-scan.jpg` | Alternate phone/scan image of the **first page only**, not a third warranty | Optional separate image-reader run instead of the PDF; full PDF remains the terms reference |

### Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Confirm personal account and clock 0. My Items > **Add** > **Vehicle** | Vehicle form, Vehicles category; no old separate-header-button assumption |
| 2 | Test1 | Enter answer-key item, kind, year, make/model, trim, VIN, New, Bought, date, price, first reading, dealer and Paid by. Attach file 1; save | One vehicle, exact identity and $42,500 vehicle price; file attached. If first-service field is not offered for New, enter 2026-11-07 in vehicle details before reading the warranty. No lease fields/to-do |
| 3 | Test1 | On the attached buyer's order use **Read it**, inspect suggestions before applying | Extraction target: Ford, Bronco, 2026-11-07, seller UAT Pine Ridge Ford and vehicle line $42,500; $45,300 is the gross document total. Record/correct a total-vs-line-price suggestion, not a hidden change. VIN/year/in-service date and odometer are manually entered, **not claimed to be extracted** |
| 4 | Test1 | Upload file 2 on this vehicle, Read it, inspect and accept the warranty | Whole-car 36 months / 36,000 miles and powertrain 60 months / 60,000 miles, with document quotes. Provider Ford; factory warranty, not purchased add-on protection. Accept/correct suggestions against the key; do not accept a single five-year whole-car term |
| 5 | Test1 | Open coverage details and item page; reload | Both dated terms and scopes agree with key. Source links to the uploaded paper; record the UI source wording, including **Extracted from receipts** if that is the source bucket displayed. Document-derived is not a human-verified shared policy. No duplicate hand/shared/document term counting the same protection |
| 6 | Test1 | Check odometer and coverage summaries | Latest entered reading **18 miles on Nov 7, 2026**, remaining miles per key; only one reading means no invented pace or estimated expiry. Both terms active at clock 0. Earliest dated coverage is bumper-to-bumper, not powertrain |
| 7 | Test1 | Open To do and Notifications, without running jobs or moving time | No unfinished first-in-service task once date is set; no registration deadline, lease-end task or lease-mileage reminder from these documents. No end-date reminder is due now. Future lead-time behavior is **verify**, not tested by clock travel here |
| 8 | Test2 | Optional: from Bob's own personal account, open this vehicle's address | Not found/no access; do not use their shared business for an isolation assertion |

## Checked when this was made

- Created real PDFs and image fixture locally; extracted PDF text, checked arithmetic and rendered/visually inspected first pages. No live reader, app sign-in, database writes, emails or reminder runs.
- Dates follow house arithmetic: start plus 36/60 calendar months, not a fresh term from upload. Display of the final covered day may differ from stored boundary; record wording, do not silently change the key.

## Known rough edges (not part of the answer key)

- Reader misses are **Partial**, with exact suggestions recorded, as in Scenario 52; deterministic manual entry still gives the answer key. VIN warnings on a synthetic VIN are not the subject of this happy path.
- Exact coverage component labels, source badge text and line-price-vs-total extraction are **verify**. The alternate JPG contains the declaration page only; use the PDF to test the transfer/registration prose.
- Reminder rules in Scenario 61 use dates without an odometer pace. Scenario 52 demonstrates a seven-day component reminder; Scenario 24 says to record the app's configured lead time. Do not assume a universal seven-/30-day rule and do not change the clock for this pack.
