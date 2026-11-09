# Scenario 68: Backdated new car with factory warranty still active, plus dealer service records (happy path)

**Accounts:** Test1 (Alice); Test2 (Bob) only for optional isolation check.
**Preconditions:** Test1's **personal account**, clock offset **0**, app date **2026-11-09** (America/New_York). **Do not advance or change the shared clock** — only the purchase and document dates are in the past. Vehicle kind Car. **Honda / CR-V** are seeded. Reader on or record **reader off**. Preserve all existing business fixtures. There is **no dedicated service-history / maintenance / repair-order table** in the deployed schema (read-only check 2026-11-09: `documents` attach to items via `owner_type`/`owner_id`; items have `notes` and `odometer_at_install` only). Service ROs are uploaded as **item documents / receipts** on the vehicle. No reference-data write was made for this pack.
**Time:** 50 min
**Built per:** Scenario 1 document order; Scenario 63 new-car factory terms; Scenario 61 odometer readings; pushes 25, 27, 37 and 40.
**Why this plan:** owners often add a car they bought years ago and keep the buyer's order, factory warranty and a stack of dated dealer service records. The records should show rising odometer, routine maintenance on covered assemblies, and at least one $0 customer-pay warranty repair on a covered powertrain part — without moving the global clock.

## The purchase (answer key)

| Fact | Value |
|---|---|
| Vehicle / category / kind | **UAT P40 S68 Honda CR-V** / Vehicles / Car (SUV) |
| Make / model / year | **Honda / CR-V / 2025** (EX-L trim in paperwork); both maker and model **seeded** |
| Seller | **UAT Riverbend Honda**, 500 Example River Road, Testville, ME 00000; fictional franchise dealer |
| Condition / ownership / paid by | New (at purchase) / Bought / Cash or check — entered today as an owned vehicle with past purchase date |
| Purchase / first in service | **2024-11-08 / 2024-11-08** (about 2 years before the run date) |
| VIN / delivery reading | **1UATHRW50S0000068** / **22 miles on 2024-11-08** |
| Current reading (enter today) | **~22,000 miles on 2026-11-09** (last RO shows 20,802; enter a realistic current reading ≥ 20,802, e.g. **22,000**) |
| Vehicle price | **$36,500** excluding tax/fees; document total **$38,950** |
| Bumper-to-bumper | **Honda**, maker warranty, Came with the product, **2024-11-08 to 2027-11-08**, 36 months **or** 36,000 miles absolute; still active at clock 0 |
| Powertrain | **Honda**, maker warranty, **2024-11-08 to 2029-11-08**, 60 months **or** 60,000 miles absolute; still active |
| Service records | Four dealer ROs (docs 3–6) attached as item documents; not a separate maintenance feature |
| Registration / plans | No pending registration, lease or purchased protection plan in this pack |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 1 | `01-buyers-order-honda-crv.pdf` | One-page 2024 buyer's order | Vehicle form attachment / saved vehicle |
| 2 | `02-honda-new-vehicle-warranty.pdf` | Two-page factory bumper-to-bumper + powertrain schedule | Vehicle > Read it |
| 3 | `03-service-oil-change-2025-02.pdf` | RO 2025-02-10 oil change @ 3,200 mi; customer pay | Vehicle documents / receipts |
| 4 | `04-service-oil-inspection-2025-08.pdf` | RO 2025-08-15 oil + inspection @ 9,800 mi; customer pay | Vehicle documents / receipts |
| 5 | `05-service-transmission-2026-03.pdf` | RO 2026-03-20 CVT fluid service @ 16,400 mi; customer pay on covered assembly | Vehicle documents / receipts |
| 6 | `06-warranty-water-pump-2026-09.pdf` | RO 2026-09-12 water pump warranty repair @ 20,800 mi; **$0 customer pay** | Vehicle documents / receipts |

### Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Confirm personal account / clock **0** (do not time-travel). Add > Vehicle > Car, Bought. Select Honda / CR-V / 2025. Enter purchase and first-service **2024-11-08**, delivery odometer 22, price $36,500, seller UAT Riverbend Honda, VIN from key; attach buyer's order 1 | One car with past purchase date. Bumper/powertrain not yet applied. Clock remains 0. If the form rejects a past purchase date, stop and record **Blocked: past purchase date** — do not move the clock |
| 2 | Test1 | Read agreement 1 on the saved vehicle; inspect suggestions | Honda / CR-V, seller, 2024-11-08, $36,500 vehicle price; document total $38,950 retained. VIN/year/in-service/odometer may need manual entry (Scenario 61: not built as document extraction) |
| 3 | Test1 | Upload/read factory warranty 2; inspect and accept both terms | Bumper-to-bumper 36 months / 36,000 miles ending **2027-11-08**; powertrain 60 months / 60,000 miles ending **2029-11-08**; provider Honda; start odometer 22. Both still active at ~22,000 miles and clock 0. Push 40: a powertrain part may carry its own mile limit — **verify** whether the UI shows powertrain as a coverage line, a vehicle part, or both; correct to the key |
| 4 | Test1 | Enter / update an odometer reading near **22,000** miles dated today (clock 0). Optionally add intermediate readings from the ROs (3,200; 9,800; 16,400; 20,802) if the readings UI allows past dates without moving the clock | Current reading saved. Past RO odometer figures are evidence in the papers; whether the app stores a multi-point reading history is **verify**. Do not change the shared clock |
| 5 | Test1 | Upload service ROs 3, 4 and 5 as item documents/receipts on the vehicle. Open each; Read it if offered | Documents retained on the vehicle. Reader may suggest dates, odometer and amounts — **verify**; correct to the key. These are customer-pay maintenance, not new warranties. Transmission fluid RO shows maintenance on a covered powertrain assembly without creating a claim |
| 6 | Test1 | Upload warranty RO 6; open / Read it if offered | Clear **$0.00 customer pay**, manufacturer pay ~$604, water pump under powertrain warranty, odometer 20,800. Do not invent a new maker warranty or restart clocks. Record whether Read it creates a claim, a note, a coverage, or only stores the document (**verify** — no service-history feature found) |
| 7 | Test1 | Open the vehicle documents list and coverage details; reload | Buyer's order, warranty schedule and four ROs all present. Active bumper-to-bumper and powertrain remain Honda with original end dates. Uploaded-paper source/quotes kept where Read it was used |
| 8 | Test1 | Inspect To do / Notifications without changing time | No overdue registration invented. No expiry reminder due at clock 0 (bumper ends 2027-11-08; powertrain 2029-11-08). Reminder lead time is **verify**, not clock-tested here |
| 9 | Test2 | Optional direct link from Bob's personal account | Car and files not accessible; do not perform in the shared business |

## Checked when this was made

- Purchase totals, warranty date/mile boundaries, RO odometer sequence (22 → 3,200 → 9,800 → 16,400 → 20,802 → ~22,000) and VIN consistency checked locally. PDFs and first-page JPG copies produced by the local generator. No app/DB modifications or sign-ins for this pack.
- DB read-only 2026-11-09: **Honda / CR-V** present in `product_models`. No `service_*`, `maintenance_*` or `repair_*` tables; `documents` is the attachment store for item paperwork.

## Known rough edges (not part of the answer key)

- **No service-record feature found.** Steps upload ROs as item documents/receipts. If a newer UI label exists (Service history, Maintenance, etc.), use it and record the label; do not invent structured service rows the API does not store.
- **Verify** past purchase-date entry and past odometer readings without clock changes. The shared clock is global and forward-only — never advance it for this scenario.
- **Verify** Read it behavior on a repair order: may extract date/odometer/amount, may no-op, or may mis-classify as a warranty. Reader misses are Partial; correct to this key. A $0 warranty RO must not restart or replace the factory powertrain term.
- Push 40 powertrain-as-part mile limits: **verify** display shape; both terms must remain active and date-correct.
- Final covered-day labels may differ by one day from end boundaries; keys use start-plus-calendar-month boundary dates as existing scenarios do.
