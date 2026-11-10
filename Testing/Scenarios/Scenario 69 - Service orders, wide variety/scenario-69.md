# Scenario 69: Service orders, wide variety (happy path)

**Accounts:** Test1 (Alice) **personal account** only. Do not run this in the shared business P34-Alice Repairs.
**Preconditions:** clock offset **0**, app date **2026-11-09** (America/New_York). **Do not advance or change the shared clock.** All order dates are in the past, from 2025-04-09 to 2026-11-03. The service history feature from push 43 is deployed, with the push 44–48 fixes (`service_entries`, "Service on covered parts" card, left-out jobs that can be ticked, Maintenance panel). Turn the reader on, or record **reader off**. Toyota/Camry, Ford/F-150, Subaru/Outback, Hyundai/Tucson and Harley-Davidson/Street Glide were in the seeded model list on 2026-11-08 (`p37-seed-after`). **Polaris** is a seeded vehicle maker with no seeded sled model, so type **650 INDY XC 137**.
**Time:** about 2.5 hours for all 12 orders. Each vehicle block can run on its own.
**Built per:** Scenario 68 service ROs, pushes 43–48 (service history, left-out jobs, maintenance due), Scenario 62 parts on a vehicle, Scenario 61 odometer readings.
**Why this plan:** owners upload service paperwork from many kinds of shop. The reader has to find the date, odometer, shop, order number and every job on each one. The rules then have to keep the jobs that matter to a warranty and leave out the rest. Tire rotations and oil changes matter most, because they are the upkeep a warranty claim depends on.

> **Two caveats from CC, which still apply:**
> 1. **The answer key is the part that matters.** Without it, a wrong skip is invisible. Check every job row below, not just the totals.
> 2. **Real orders still beat these.** They show what real shops write. This set mostly shows how the rules handle wording we already expect. All 12 are happy path: legible, correct documents a shop would really produce. None are wrong, corrupted or deliberately confusing.

## How to read the answer key

- **Keep:** this should become a service entry. The coverage named is the one that makes it matter. A job that warranty, a recall, goodwill, a service contract or a protection plan paid for is always kept.
- **Leave out:** the job should land under "N other jobs were left out". This covers wear items, inspections, washes, fees, and work with no running coverage and no warranty bearing.
- **Either way:** keeping or leaving out both pass. If it is left out, ticking it by hand (push 46) should also work. Record which one the rules picked, because that tells us where `ServiceRecordRules.cs` draws the line.
- **Service-entry fields** follow `service_entries`: `serviced_on`, `odometer` (**mileage in**, per push 44), `part` (≤120), `work` (≤300), `warranty_repair`, `order_ref`, `shop`, `covered_by`, `customer_paid`. `customer_paid` is that job's customer share **before tax**, with fees and tax left off. `covered_by` labels below use "<coverage name> (to <end date>)". Any label that names the same coverage and end date passes. Wording of `part`/`work` is free: it passes if it names the same part and the same work.
- **Left-out count:** the card counts fees and shop charges as jobs, but not tax (push 44/45). The expected "N other jobs were left out" is a range: Leave-out jobs plus fee lines, up to that plus the Either-way jobs.

## Vehicles and coverages to set up (answer key)

| Item name | Kind | Year / make / model | VIN | In service / odometer | Coverages to add (name, provider, start → end, limit) | Current reading to enter (today) |
|---|---|---|---|---|---|---|
| **UAT S69 Toyota Camry** | Car | 2024 Toyota / Camry LE | `4T1C11AKXRU690101` | 2024-03-15 / 8 mi | Toyota basic (bumper-to-bumper), Toyota, 2024-03-15 → 2027-03-15, 36 mo / 36,000 mi<br>Toyota powertrain, Toyota, 2024-03-15 → 2029-03-15, 60 mo / 60,000 mi | 32,400 mi |
| **UAT S69 Ford F-150** | Car (pickup truck) | 2023 Ford / F-150 XLT SuperCrew 4x4 | `1FTFW1E57PFA69021` | 2023-06-10 / 12 mi | Ford bumper-to-bumper, Ford, 2023-06-10 → 2026-06-10, 36 mo / 36,000 mi<br>Ford powertrain, Ford, 2023-06-10 → 2028-06-10, 60 mo / 60,000 mi | 45,050 mi |
| **UAT S69 Subaru Outback** | Car | 2022 Subaru / Outback Premium | `4S4BTACC5N3690311` | 2021-11-20 / 15 mi | Subaru basic, Subaru, 2021-11-20 → 2024-11-20, 36 mo / 36,000 mi<br>Subaru powertrain, Subaru, 2021-11-20 → 2026-11-20, 60 mo / 60,000 mi | 62,100 mi |
| **UAT S69 Hyundai Tucson** | Car (SUV) | 2025 Hyundai / Tucson SEL AWD | `KM8JB3DE0SU690412` | 2025-04-05 / 9 mi | Hyundai new vehicle limited (bumper-to-bumper), Hyundai, 2025-04-05 → 2030-04-05, 60 mo / 60,000 mi<br>Hyundai powertrain, Hyundai, 2025-04-05 → 2035-04-05, 120 mo / 100,000 mi (original owner) | 21,300 mi |
| **UAT S69 Harley-Davidson Street Glide** | Motorcycle | 2024 Harley-Davidson / Street Glide FLHX | `1HD1KBC18RB690515` | 2024-09-07 / 4 mi | Harley-Davidson limited warranty, Harley-Davidson, 2024-09-07 → 2026-09-07, 24 mo / unlimited miles | 7,900 mi |
| **UAT S69 Polaris INDY** | Snowmobile (verify kind; Other if none) | 2024 Polaris / 650 INDY XC 137 | `SN1PEF6RXRC690616` | 2023-12-02 / 3 mi | Polaris factory limited warranty, Polaris, 2023-12-02 → 2024-12-02, 12 mo, date only<br>Polaris extended service contract, Polaris (service contract), 2024-12-02 → 2026-12-02, 24 mo, date only, $50 deductible per visit | 1,610 mi |
| **UAT S69 F-150 tires (set of 4)** (Part of UAT S69 Ford F-150) | Part | Michelin / Defender LTX M/S2 LT275/65R18 | n/a | installed 2025-07-22 at 26,310 mi | Michelin limited treadwear warranty, Michelin, 2025-07-22 → 2031-07-22, 70,000 tire miles (odometer 96,310) or 6 years<br>Tread Masters road hazard protection, Tread Masters Tire & Auto, 2025-07-22 → 2028-07-22, 36 mo, repair or replace, $0 deductible | n/a |

All six VINs are synthetic, with valid check digits. Customer on every paper: **UAT Sample Buyer**, 69 Example Lane, Testville, ME 00000, (207) 555-0169. All shops are fictional and use 555-01xx numbers and Example addresses.

## Files, in the order to use them

Each order is one PDF plus a JPG of its first page with the same name. Orders 01, 03, 07 and 10 are two pages long.

| # | File (.pdf + .jpg) | Shop type / shop | Vehicle | Date on paper → ISO | Odometer in | Pay mix | Upload order |
|---|---|---|---|---|---|---|---|
| 01 | `01-ro-toyota-dealer-camry-oil-rotation-window-warranty` | Franchise dealer (Toyota) / Pine Harbor Toyota | 2024 Toyota Camry | 05/18/2026 → 2026-05-18 | 27,640 | Mixed: customer pay + Toyota warranty | Toyota Camry #1 |
| 02 | `02-receipt-quick-lube-camry-synthetic-oil-change` | Quick-lube chain / QuickTop Lube #214 | 2024 Toyota Camry | Aug 30, 2026  2:47 PM → 2026-08-30 | 31,215 | All customer pay | Toyota Camry #2 |
| 03 | `03-ro-ford-dealer-f150-recall-axle-seal-seat-warranty` | Franchise dealer (Ford) / Granite Ridge Ford | 2023 Ford F-150 | 2026-01-14 → 2026-01-14 | 31,207 | All warranty / recall (customer pays $0.00) | Ford F-150 #2 |
| 04 | `04-invoice-independent-garage-f150-brakes-battery-coolant-belt` | Independent garage / Dunmore's Auto Repair | 2023 Ford F-150 | 11/03/2026 → 2026-11-03 | 44,880 | All customer pay | Ford F-150 #4 |
| 05 | `05-invoice-tire-shop-f150-new-tires-alignment` | Tire shop / Tread Masters Tire & Auto | 2023 Ford F-150 | 7/22/2025 → 2025-07-22 | 26,310 | All customer pay | Ford F-150 #1 |
| 06 | `06-invoice-tire-shop-f150-rotation-flat-repair` | Tire shop / Tread Masters Tire & Auto | 2023 Ford F-150 | 2/11/2026 → 2026-02-11 | 31,890 | Mixed: no-charge rotation, road hazard plan, customer pay wipers | Ford F-150 #3 |
| 07 | `07-ro-subaru-dealer-outback-cvt-goodwill-spark-plugs` | Franchise dealer (Subaru) / Lakeside Subaru | 2022 Subaru Outback | 14-OCT-26 → 2026-10-14 | 61,240 | Mixed: Subaru goodwill (part of the labor paid by the customer) + customer pay | Subaru Outback #2 |
| 08 | `08-invoice-body-shop-tucson-collision-ac-condenser` | Body shop / Precision Collision Center | 2025 Hyundai Tucson | June 3, 2026 → 2026-06-03 | 14,022 | Insurance + customer deductible (no warranty money) | Hyundai Tucson #1 |
| 09 | `09-ro-hyundai-dealer-tucson-warranty-campaign` | Franchise dealer (Hyundai) / Seaport Hyundai | 2025 Hyundai Tucson | 09-16-2026 → 2026-09-16 | 19,880 | All warranty / campaign (customer pays $0.00) | Hyundai Tucson #2 |
| 10 | `10-workorder-harley-dealer-street-glide-5000-service-fork-seals` | Motorcycle dealer / Iron Ridge Harley-Davidson | 2024 Harley-Davidson Street Glide | Saturday, June 14, 2025 → 2025-06-14 | 5,032 | Mixed: customer pay + H-D warranty | Harley-Davidson Street Glide #1 |
| 11 | `11-ticket-snowmobile-dealer-polaris-preseason-fuel-pump-esc` | Snowmobile / powersports dealer (Polaris) / North Country Powersports | 2024 Polaris 650 INDY XC 137 | 2025-11-18 09:12 → 2025-11-18 | 1,486 | Mixed: service contract claim ($50 deductible) + customer pay | Polaris INDY #1 |
| 12 | `12-invoice-independent-ac-shop-outback-cvt-fluid-ac-inspection` | Independent garage (A/C and drivetrain) / Hillside Garage & A/C | 2022 Subaru Outback | Apr 9, 2025 → 2025-04-09 | 41,120 | All customer pay | Subaru Outback #1 |

## Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Confirm personal account and clock **0**. Add the six vehicles from the table (Add > Vehicle, Bought, past purchase/in-service date, odometer at purchase, VIN). Add each listed coverage by hand. There are no warranty papers in this pack. | Six vehicles, each with its coverages and end dates as keyed. Do not move the clock. If a past date is refused, stop and record **Blocked: past purchase date**. |
| 2 | Test1 | On the F-150, Parts > Add a part: **UAT S69 F-150 tires (set of 4)**, Michelin / Defender LTX M/S2, installed 2025-07-22 at 26,310 mi. Add the treadwear and road-hazard coverages to the **part** | The part is linked to the F-150 with its own two terms. Nothing changes on the truck's Ford terms. |
| 3 | Test1 | Enter today's reading on each vehicle (last column of the vehicle table) | Readings are saved. The Outback is now past 60,000 mi, so its powertrain shows ended on miles (or **verify** how an ended-on-miles term is shown). |
| 4 | Test1 | For each vehicle in upload order: attach the PDF to the **vehicle**, Read it, compare the "Service on covered parts" card with that order's key below, then **Add to service history** | Recognised as a repair order (not a purchase, a plan or a new warranty). Header fields: date = ISO date, odometer = mileage **in**, shop, order number. Each job kept or left out as keyed. Either-way jobs may go either way. Warranty, recall, goodwill, service-contract and road-hazard jobs show as **repaired under warranty** with the keyed customer amount. |
| 5 | Test1 | For any **Keep** job the rules left out, tick it and pick the keyed coverage (push 46). Note it as a rules miss with the order and job number | It is added as "added by you". Every rules miss here is a candidate word for `ServiceRecordRules.cs`. |
| 6 | Test1 | Optional: Read it on the **JPG twin** of 2–3 orders on a scratch copy of the vehicle (or Read it again and choose Not now) | Same header fields and job split as the PDF. Reading the same order twice replaces the entries and adds no second reading (push 43/47). |
| 7 | Test1 | Open each vehicle's Service history and reload | Entries are newest first and match the expected-entry tables. Odometer readings come from each order (source: from a document). No coverage end date moved. No claim, plan or coverage was created by any order. The body-shop lifetime guarantee and the new battery's warranty are **not** auto-created. |
| 8 | Test1 | Optional, Maintenance panel (push 45): on the Camry add "Engine oil and filter change, 5,000 mi, 6 months". On the F-150 add "Tire rotation, 7,500 mi" on the tires if parts support it | The Camry counts from order 02 (Aug 30, 2026 at 31,215). Check the quick-lube wording "Full Synthetic Oil Change" matches. If not, record it (push 45 known limit). Tire rotation counts from order 06 (Feb 11, 2026 at 31,890) and shows **Overdue** by miles (31,890 + 7,500 = 39,390 < 45,050). |
| 9 | Test1 | Export data | `service_history.csv` holds every entry with the keyed fields. |

## Answer key, order by order

### Order 01: Franchise dealer (Toyota), 2024 Toyota Camry

- **Files:** `01-ro-toyota-dealer-camry-oil-rotation-window-warranty.pdf` / `.jpg`
- **Shop:** Pine Harbor Toyota, 1180 Example Coastal Highway, Testville, ME 00000. **Paper:** Repair Order / Invoice, number **418827** (labelled 'R.O. NUMBER'), 2 pages.
- **Date printed:** "05/18/2026" → **2026-05-18**. **Odometer:** in **27,640** / out 27,643.
- **Vehicle:** UAT S69 Toyota Camry, VIN `4T1C11AKXRU690101`, in service 2024-03-15.
- **Coverages on the service day:** Toyota basic (to Mar 15, 2027) [36 mo / 36,000 mi]: **running**; Toyota powertrain (to Mar 15, 2029) [60 mo / 60,000 mi]: **running**.
- **Pay mix:** Mixed: customer pay + Toyota warranty.

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| A. DRIVER FRONT WINDOW SLOW / STOPS MID-TRAVEL | R&R FRONT DOOR WINDOW REGULATOR & MOTOR ASSY LH (222.60, W)<br>REG & MOTOR ASSY FR DR LH  69802-06290 (412.75, W) | **Keep** | Toyota basic | Factory defect repaired by Toyota at no charge inside 36 mo / 36k. A warranty-paid job is always kept. |
| B. PERFORM ENGINE OIL & FILTER CHANGE | LOF - 0W-16 SYNTHETIC, RESET MAINT REMINDER (39.95)<br>OIL 0W-16 FULL SYN (QT)  00279-0WQTE (41.25)<br>OIL FILTER ELEMENT  04152-YZZA1 (12.40)<br>GASKET, DRAIN PLUG  90430-12031 (2.15) | **Keep** | Toyota powertrain | Engine upkeep. Maintenance proof for the powertrain term. |
| C. ROTATE TIRES | ROTATE TIRES, SET PRESSURES 35 PSI (29.95) | **Either way** | — | Tire upkeep. No tire coverage is set up on the Camry, so it is plain history. The rules currently leave rotations out; keeping it by hand is also fine. |
| D. REPLACE ENGINE AIR FILTER | R&R ENGINE AIR FILTER ELEMENT (14.00)<br>ELEMENT, AIR CLEANER FILTER  17801-F0020 (34.80) | **Either way** | — | Scheduled engine maintenance item, but the rules treat air filters as consumables and leave them out. Either result is fine. |
| E. REPLACE WIPER BLADE INSERTS (CUSTOMER REQUEST) | WIPER INSERT 26/16  85214-06190 (25.90) | **Leave out** | — | Wear item with no warranty bearing. |
| F. MULTI-POINT INSPECTION | COMPLIMENTARY MULTI-POINT INSPECTION - ALL GREEN (0.00, N) | **Leave out** | — | Inspection with no work done. The rules never keep inspections. |
| fee | SHOP SUPPLIES (14.50) | **Leave out** | — | Shop charge. Never kept (push 44). |
| fee | HAZARDOUS WASTE DISPOSAL (4.95) | **Leave out** | — | Shop charge. Never kept (push 44). |

**Expected card:** 2 kept (+ up to 2 either-way); "N other jobs were left out" N = **4**–6.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| A | 2026-05-18 | 27,640 | Front door window regulator and motor, driver side | Replaced window regulator and motor assembly (frayed regulator cable); Toyota warranty claim | true | 418827 | Pine Harbor Toyota | Toyota basic (to Mar 15, 2027) | 0.00 |
| B | 2026-05-18 | 27,640 | Engine oil and filter | Changed engine oil (0W-16 synthetic, 5 qt) and oil filter; replaced drain plug gasket | false | 418827 | Pine Harbor Toyota | Toyota powertrain (to Mar 15, 2029) | 95.75 |
| C *(either)* | 2026-05-18 | 27,640 | Tires (rotation) | Rotated tires and set pressures to 35 psi | false | 418827 | Pine Harbor Toyota | (none) | 29.95 |
| D *(either)* | 2026-05-18 | 27,640 | Engine air filter | Replaced engine air filter element | false | 418827 | Pine Harbor Toyota | Toyota powertrain (to Mar 15, 2029) | 48.80 |

**Totals check:** Customer: labor 83.90 + parts 116.50 + fees 19.45 + tax 5.5% on taxable parts & fees (135.95) 7.48 = **227.33**. Billed to Toyota warranty: labor 222.60 + parts 412.75 = **635.35** (not charged to the customer).

### Order 02: Quick-lube chain, 2024 Toyota Camry

- **Files:** `02-receipt-quick-lube-camry-synthetic-oil-change.pdf` / `.jpg`
- **Shop:** QuickTop Lube #214, 77 Example Plaza Road, Testville, ME 00000. **Paper:** Service Receipt, number **214-0083391** (labelled 'Invoice'), 1 page.
- **Date printed:** "Aug 30, 2026  2:47 PM" → **2026-08-30**. **Odometer:** in **31,215**.
- **Vehicle:** UAT S69 Toyota Camry, VIN `4T1C11AKXRU690101`, in service 2024-03-15.
- **Coverages on the service day:** Toyota basic (to Mar 15, 2027) [36 mo / 36,000 mi]: **running**; Toyota powertrain (to Mar 15, 2029) [60 mo / 60,000 mi]: **running**.
- **Pay mix:** All customer pay.

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| 1. Full Synthetic Oil Change | Full Synthetic Oil Change - service labor (29.99)<br>Oil 0W-16 Full Synthetic (qt) (49.95)<br>Oil Filter QT-7317 (11.99)<br>Coupon QT10 - $10.00 off service labor (-10.00) | **Keep** | Toyota powertrain | Engine upkeep at a quick-lube is still maintenance proof for the powertrain term. The receipt calls it "Full Synthetic Oil Change", not "oil and filter". |
| 2. Cabin Air Filter | Cabin air filter - install (10.00)<br>Cabin Air Filter CF-11182 (39.99) | **Leave out** | — | Comfort item, not on a covered part that needs upkeep. |
| 3. Wiper Blades (front pair) | Wiper Blade 26" (19.99)<br>Wiper Blade 16" (19.99) | **Leave out** | — | Wear item. |
| 4. Courtesy check | Courtesy check: fluids topped, tire pressure set 35/35/35/35 (0.00, N) | **Leave out** | — | Free check, no part serviced. |
| fee | Environmental / oil disposal fee (3.99) | **Leave out** | — | Shop charge. Never kept (push 44). |

**Expected card:** 1 kept; "N other jobs were left out" N = **4**.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-08-30 | 31,215 | Engine oil and filter | Full synthetic oil change, 0W-16 (5 qt) and oil filter | false | 214-0083391 | QuickTop Lube #214 | Toyota powertrain (to Mar 15, 2029) | 81.93 |
- customer_paid 81.93 is after the $10.00 coupon (91.93 before it). Either is acceptable; record which.

**Totals check:** Customer: labor 39.99 + parts 141.91 + fees 3.99 + coupon -10.00 + tax 5.5% on taxable parts & fees (145.90) 8.02 = **183.91**.

### Order 03: Franchise dealer (Ford), 2023 Ford F-150

- **Files:** `03-ro-ford-dealer-f150-recall-axle-seal-seat-warranty.pdf` / `.jpg`
- **Shop:** Granite Ridge Ford, 2400 Example Turnpike, Testville, ME 00000. **Paper:** Repair Order, number **6650291** (labelled 'RO #'), 2 pages.
- **Date printed:** "2026-01-14" → **2026-01-14**. **Odometer:** in **31,207** / out 31,209.
- **Vehicle:** UAT S69 Ford F-150, VIN `1FTFW1E57PFA69021`, in service 2023-06-10.
- **Coverages on the service day:** Ford bumper-to-bumper (to Jun 10, 2026) [36 mo / 36,000 mi]: **running**; Ford powertrain (to Jun 10, 2028) [60 mo / 60,000 mi]: **running**; Michelin treadwear (to Jul 22, 2031) [70,000 tire miles (odometer 96,310) or 6 years]: **running**; Road hazard protection (to Jul 22, 2028) [36 mo, repair or replace, $0 deductible]: **running**.
- **Pay mix:** All warranty / recall (customer pays $0.00).

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| 1. Safety recall 25S99 - rearview camera image software | Reprogram image processing module per recall 25S99 (42.60, R) | **Keep** | — | Ford-paid recall work. Not a coverage term, but the order shows it is done and costs the owner nothing. |
| 2. Customer states fluid leak at rear axle | Replace rear axle pinion seal, refill axle (255.60, W)<br>SEAL - PINION OIL  ML3Z-4676-A (22.40, W)<br>MOTORCRAFT SAE 75W-85 GEAR LUBE (QT)  XY-75W85-QL (42.75, W) | **Keep** | Ford powertrain | Warranty repair on the drive axle, a powertrain part. While both terms run, powertrain should be named. |
| 3. Passenger heated seat inoperative | Replace RH front seat cushion heater element (227.20, W)<br>ELEMENT - SEAT HEATER  ML3Z-14D696-B (168.35, W) | **Keep** | Ford bumper-to-bumper | Warranty repair on a whole-vehicle part, inside 36 mo / 36k. |
| 4. Multi-point inspection | Multi-point inspection (no charge) (0.00, N) | **Leave out** | — | Inspection. |

**Expected card:** 3 kept; "N other jobs were left out" N = **1**.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-01-14 | 31,207 | Rearview camera image processing module | Safety recall 25S99: reprogrammed image processing module software | true | 6650291 | Granite Ridge Ford | (none) - recall | 0.00 |
| 2 | 2026-01-14 | 31,207 | Rear axle pinion seal | Replaced leaking rear axle pinion seal and refilled gear lube (3 qt); Ford warranty | true | 6650291 | Granite Ridge Ford | Ford powertrain (to Jun 10, 2028) | 0.00 |
| 3 | 2026-01-14 | 31,207 | Front passenger seat heater element | Replaced RH front seat cushion heater element; Ford warranty | true | 6650291 | Granite Ridge Ford | Ford bumper-to-bumper (to Jun 10, 2026) | 0.00 |
- covered_by: no coverage, or a recall label. Must not be pinned to bumper-to-bumper as if it were a defect claim.
- serviced_on: the RO was opened 2026-01-14 08:05 and closed 2026-01-15 11:30. The opened/invoice date is keyed. The close date is acceptable.

**Totals check:** Customer: labor 0.00 + parts 0.00 + fees 0.00 + tax 5.5% on taxable parts & fees (0.00) 0.00 = **0.00**. Billed to Ford warranty + recall: labor 525.40 + parts 233.50 = **758.90** (not charged to the customer).

### Order 04: Independent garage, 2023 Ford F-150

- **Files:** `04-invoice-independent-garage-f150-brakes-battery-coolant-belt.pdf` / `.jpg`
- **Shop:** Dunmore's Auto Repair, 16 Example Mill Street, Testville, ME 00000. **Paper:** Repair Invoice, number **004417** (labelled 'No.'), 1 page.
- **Date printed:** "11/03/2026" → **2026-11-03**. **Odometer:** in **44,880** / out 44,882.
- **Vehicle:** UAT S69 Ford F-150, VIN `1FTFW1E57PFA69021`, in service 2023-06-10.
- **Coverages on the service day:** Ford bumper-to-bumper (to Jun 10, 2026) [36 mo / 36,000 mi]: **ended Jun 10, 2026 (time)**; Ford powertrain (to Jun 10, 2028) [60 mo / 60,000 mi]: **running**; Michelin treadwear (to Jul 22, 2031) [70,000 tire miles (odometer 96,310) or 6 years]: **running**; Road hazard protection (to Jul 22, 2028) [36 mo, repair or replace, $0 deductible]: **running**.
- **Pay mix:** All customer pay.

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| 1. Front brakes - pads & rotors | Front pads & rotors, lube slides (177.00)<br>Front brake pads, ceramic (89.99)<br>Front brake rotor (193.00) | **Leave out** | — | Wear items, and the bumper-to-bumper term had already ended. |
| 2. Battery | Test & replace battery (59.00)<br>Battery DuraStart H7-AGM 850CCA (249.99) | **Either way** | — | New battery with its own 36-month replacement warranty from today. No running coverage on the truck covers the battery. Keep as history or as the start of a battery coverage. |
| 3. Cooling system flush | Coolant flush & fill, pressure test (118.00)<br>Motorcraft Orange coolant, gal (69.90) | **Keep** | Ford powertrain | Cooling-system upkeep counts as powertrain work, and powertrain still runs to Jun 10, 2028 / 60k. |
| 4. Serpentine belt | Replace serpentine belt (70.80)<br>Serpentine belt 6K-1040 (52.40) | **Either way** | — | Engine accessory belt. It is a wear item that warranties exclude, but it is engine upkeep. Either result is fine. |
| fee | Shop supplies (18.00) | **Leave out** | — | Shop charge. Never kept (push 44). |
| fee | Waste disposal (6.00) | **Leave out** | — | Shop charge. Never kept (push 44). |

**Expected card:** 1 kept (+ up to 2 either-way); "N other jobs were left out" N = **3**–5.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| 2 *(either)* | 2026-11-03 | 44,880 | Battery (12V) | Tested and replaced 12V battery with DuraStart H7-AGM 850CCA; terminals cleaned | false | 004417 | Dunmore's Auto Repair | (none) | 308.99 |
| 3 | 2026-11-03 | 44,880 | Engine coolant | Coolant flush and fill (2 gal Motorcraft Orange); pressure tested cooling system | false | 004417 | Dunmore's Auto Repair | Ford powertrain (to Jun 10, 2028) | 187.90 |
| 4 *(either)* | 2026-11-03 | 44,880 | Serpentine (accessory drive) belt | Replaced serpentine belt | false | 004417 | Dunmore's Auto Repair | Ford powertrain (to Jun 10, 2028) | 123.20 |

**Totals check:** Customer: labor 424.80 + parts 655.28 + fees 24.00 + tax 5.5% on taxable parts & fees (679.28) 37.36 = **1,141.44**.

### Order 05: Tire shop, 2023 Ford F-150

- **Files:** `05-invoice-tire-shop-f150-new-tires-alignment.pdf` / `.jpg`
- **Shop:** Tread Masters Tire & Auto, Store #08 | 455 Example Commerce Drive, Testville, ME 00000. **Paper:** Sales Invoice, number **08-552190** (labelled 'Invoice #'), 1 page.
- **Date printed:** "7/22/2025" → **2025-07-22**. **Odometer:** in **26,310**.
- **Vehicle:** UAT S69 Ford F-150, VIN `1FTFW1E57PFA69021`, in service 2023-06-10.
- **Coverages on the service day:** Ford bumper-to-bumper (to Jun 10, 2026) [36 mo / 36,000 mi]: **running**; Ford powertrain (to Jun 10, 2028) [60 mo / 60,000 mi]: **running**; Michelin treadwear (to Jul 22, 2031) [70,000 tire miles (odometer 96,310) or 6 years]: **running**; Road hazard protection (to Jul 22, 2028) [36 mo, repair or replace, $0 deductible]: **running**.
- **Pay mix:** All customer pay.

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| 1. New tires | MICHELIN DEFENDER LTX M/S2 LT275/65R18 123/120R  DOT 3HB2 XLM9 2325 (1,159.96) | **Keep** | Michelin treadwear (tire part) | Four new tires are the parts the tire maker's treadwear term covers. This order is the purchase proof that term needs. Rule watch: push 43 lists tires as left out. The F-150 tire part has its own term, so it should keep this. Record a miss if it does not. |
| 2. Mount & balance | MOUNT & COMPUTER BALANCE (100.00) | **Either way** | — | Labor to fit the new tires. Fine on its own row or folded into the tire row. |
| 3. TPMS service kits | TPMS SERVICE KIT (VALVE CORE/SEAL/NUT) (27.96) | **Leave out** | — | Small seal kits that come with a tire change. |
| 4. 4-wheel alignment | ALIGNMENT - 4 WHEEL (THRUST ANGLE) (129.99) | **Either way** | — | Tire treadwear terms expect correct alignment, so it can back up a tire claim. It is not a covered part. |
| 5. Road hazard protection | ROAD HAZARD PROTECTION 36 MO (PER TIRE) (128.00) | **Leave out** | — | A purchased protection plan, not service work. Add it as a coverage on the tire part in setup. |
| fee | TIRE DISPOSAL FEE (4 TIRES @ 3.50) (14.00) | **Leave out** | — | Shop charge. Never kept (push 44). |
| fee | SHOP SUPPLIES (9.95) | **Leave out** | — | Shop charge. Never kept (push 44). |

**Expected card:** 1 kept (+ up to 2 either-way); "N other jobs were left out" N = **4**–6.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2025-07-22 | 26,310 | Tires (set of 4) Michelin Defender LTX M/S2 LT275/65R18 | Installed four new tires | false | 08-552190 | Tread Masters Tire & Auto | Michelin treadwear (to Jul 22, 2031) | 1,159.96 |
| 2 *(either)* | 2025-07-22 | 26,310 | Tires (mount and balance) | Mounted and computer balanced four tires | false | 08-552190 | Tread Masters Tire & Auto | Michelin treadwear (to Jul 22, 2031) | 100.00 |
| 4 *(either)* | 2025-07-22 | 26,310 | Wheel alignment | Four-wheel alignment | false | 08-552190 | Tread Masters Tire & Auto | Michelin treadwear (to Jul 22, 2031) | 129.99 |

**Totals check:** Customer: labor 229.99 + parts 1,315.92 + fees 23.95 + tax 5.5% on taxable parts & fees (1,211.87) 66.65 = **1,636.51**.

### Order 06: Tire shop, 2023 Ford F-150

- **Files:** `06-invoice-tire-shop-f150-rotation-flat-repair.pdf` / `.jpg`
- **Shop:** Tread Masters Tire & Auto, Store #08 | 455 Example Commerce Drive, Testville, ME 00000. **Paper:** Sales Invoice, number **08-561077** (labelled 'Invoice #'), 1 page.
- **Date printed:** "2/11/2026" → **2026-02-11**. **Odometer:** in **31,890**.
- **Vehicle:** UAT S69 Ford F-150, VIN `1FTFW1E57PFA69021`, in service 2023-06-10.
- **Coverages on the service day:** Ford bumper-to-bumper (to Jun 10, 2026) [36 mo / 36,000 mi]: **running**; Ford powertrain (to Jun 10, 2028) [60 mo / 60,000 mi]: **running**; Michelin treadwear (to Jul 22, 2031) [70,000 tire miles (odometer 96,310) or 6 years]: **running**; Road hazard protection (to Jul 22, 2028) [36 mo, repair or replace, $0 deductible]: **running**.
- **Pay mix:** Mixed: no-charge rotation, road hazard plan, customer pay wipers.

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| 1. Rotation & balance | ROTATE & BALANCE - LIFETIME (ORIG INV 08-552190) (0.00, N) | **Keep** | Michelin treadwear (tire part) | Rotation proof for the Michelin treadwear term. This is the "tires rotated" record the tire claim needs. The rules currently leave rotations out, so check that the tire part's own term keeps it. Rule watch: push 43 lists rotations as left out. This is the case Steve cares about: rotation proof for a tire warranty. |
| 2. Flat repair RR | FLAT REPAIR RR - PLUG/PATCH (NAIL IN TREAD) (34.99, RH) | **Keep** | Road hazard protection (tire part) | Repair paid by the road hazard plan on the tires. Keep it as a covered repair. The customer paid $0. Rule watch: paid by a protection plan, not the maker. It should count as "paid by coverage" (customer $0). |
| 3. Wiper blades | WIPER BLADE 22" ALL-SEASON (49.98) | **Leave out** | — | Wear item. |

**Expected card:** 2 kept; "N other jobs were left out" N = **1**.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-02-11 | 31,890 | Tires (rotation and balance) | Rotated and balanced four tires (lifetime rotation, no charge) | false | 08-561077 | Tread Masters Tire & Auto | Michelin treadwear (to Jul 22, 2031) | 0.00 |
| 2 | 2026-02-11 | 31,890 | Tire, right rear | Plug-patch repair, nail in tread; paid by road hazard protection | true | 08-561077 | Tread Masters Tire & Auto | Road hazard protection (to Jul 22, 2028) | 0.00 |
- warranty_repair: **true** (plan-paid, $0 customer).

**Totals check:** Customer: labor 0.00 + parts 49.98 + fees 0.00 + tax 5.5% on taxable parts & fees (49.98) 2.75 = **52.73**. Billed to road hazard plan: labor 34.99 + parts 0.00 = **34.99** (not charged to the customer).

### Order 07: Franchise dealer (Subaru), 2022 Subaru Outback

- **Files:** `07-ro-subaru-dealer-outback-cvt-goodwill-spark-plugs.pdf` / `.jpg`
- **Shop:** Lakeside Subaru, 900 Example Lake Road, Testville, ME 00000. **Paper:** Service Invoice, number **77031** (labelled 'RO'), 2 pages.
- **Date printed:** "14-OCT-26" → **2026-10-14**. **Odometer:** in **61,240** / out 61,248.
- **Vehicle:** UAT S69 Subaru Outback, VIN `4S4BTACC5N3690311`, in service 2021-11-20.
- **Coverages on the service day:** Subaru basic (to Nov 20, 2024) [36 mo / 36,000 mi]: **ended Nov 20, 2024 (time)**; Subaru powertrain (to Nov 20, 2026) [60 mo / 60,000 mi]: **ended at 60,000 mi (miles)**.
- **Pay mix:** Mixed: Subaru goodwill (part of the labor paid by the customer) + customer pay.

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| A. CVT judder / shudder on light acceleration 15-30 mph | Diagnose & replace CVT control valve body, CVTF exchange, learn (705.60, G)<br>CONTROL VALVE BODY ASSY  31825AA (1,184.00, G)<br>SUBARU HIGH TORQUE CVTF (QT)  K0425Y0711 (100.80, G) | **Keep** | — | CVT repair paid mostly by Subaru as goodwill, 1,240 mi past the 60k powertrain limit. A maker-paid job is always kept. No coverage was running, because powertrain ended on miles before its date. |
| B. 60,000 mile service - spark plugs | Replace spark plugs (218.40)<br>SPARK PLUG  22401AA811 (75.80) | **Either way** | — | Engine upkeep, but powertrain ended at 60,000 mi, so no coverage is running. Plain history. Kept with no coverage, or left out: both are fine. |
| C. Brake fluid exchange | Brake fluid exchange (117.60)<br>BRAKE FLUID DOT3 (32 OZ) (14.25) | **Leave out** | — | Brake upkeep. Brakes have no running coverage and are not on a covered part. |
| D. Multi-point inspection & complimentary wash | MPI - ALL OK; COMPLIMENTARY CAR WASH (0.00, N) | **Leave out** | — | Inspection and car wash. |
| fee | SHOP SUPPLIES (16.00) | **Leave out** | — | Shop charge. Never kept (push 44). |
| fee | HAZMAT / DISPOSAL (4.50) | **Leave out** | — | Shop charge. Never kept (push 44). |

**Expected card:** 1 kept (+ up to 1 either-way); "N other jobs were left out" N = **4**–5.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| A | 2026-10-14 | 61,240 | CVT control valve body | Replaced CVT control valve body and exchanged CVT fluid (6 qt); Subaru goodwill, customer paid 50% of labor | true | 77031 | Lakeside Subaru | (none) - goodwill; powertrain ended at 60,000 mi | 352.80 |
| B *(either)* | 2026-10-14 | 61,240 | Spark plugs | Replaced spark plugs (4) at 60,000-mile service | false | 77031 | Lakeside Subaru | (none) | 294.20 |
- warranty_repair: **true** preferred (maker-paid goodwill). false is acceptable if the app keeps "warranty" for running coverages only. Record which.
- serviced_on: the RO was opened 14-OCT-26 07:58 and closed 15-OCT-26 16:20. The opened/invoice date is keyed. The close date is acceptable.

**Totals check:** Customer: labor 688.80 + parts 90.05 + fees 20.50 + tax 5.5% on taxable parts & fees (110.55) 6.08 = **805.43**. Billed to Subaru goodwill: labor 352.80 + parts 1,284.80 = **1,637.60** (not charged to the customer).

### Order 08: Body shop, 2025 Hyundai Tucson

- **Files:** `08-invoice-body-shop-tucson-collision-ac-condenser.pdf` / `.jpg`
- **Shop:** Precision Collision Center, 3 Example Industrial Way, Testville, ME 00000. **Paper:** Final Repair Invoice, number **PCC-26-0412** (labelled 'Repair Order'), 1 page.
- **Date printed:** "June 3, 2026" → **2026-06-03**. **Odometer:** in **14,022** / out 14,031.
- **Vehicle:** UAT S69 Hyundai Tucson, VIN `KM8JB3DE0SU690412`, in service 2025-04-05.
- **Coverages on the service day:** Hyundai bumper-to-bumper (to Apr 5, 2030) [60 mo / 60,000 mi]: **running**; Hyundai powertrain (to Apr 5, 2035) [120 mo / 100,000 mi (original owner)]: **running**.
- **Pay mix:** Insurance + customer deductible (no warranty money).

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| 1. Front bumper cover | Bumper cover, front  86511-N9000 (412.00, I)<br>Body labor - front bumper cover R&R/replace (148.80, I)<br>Absorber, front bumper  86520-N9000 (58.40, I)<br>Refinish front bumper cover (3-stage) (161.20, I) | **Leave out** | — | Collision body and paint work, no warranty bearing. The shop's own lifetime workmanship guarantee is a new coverage, not service. |
| 2. A/C condenser | Condenser assy, A/C  97606-N9000 (OEM) (336.90, I)<br>Mechanical labor - R&R A/C condenser (200.00, I) | **Either way** | — | Collision damage, not a warranty defect. Still, an OEM part on the A/C system that bumper-to-bumper covers was replaced, which helps if the A/C later fails. |
| 3. Evacuate & recharge A/C | Mechanical labor - evacuate & recharge A/C (100.00, I)<br>Refrigerant R-1234yf (lb) (93.00, I) | **Either way** | — | Goes with the condenser. Same reasoning. |
| 4. Front radar calibration | Sublet - front radar (ADAS) calibration, static (295.00, I) | **Either way** | — | A required step after bumper work, on a factory driver-assist system. Collision-related. |
| 5. Four-wheel alignment | Sublet - four wheel alignment (149.00, I) | **Leave out** | — | Collision check. No tire coverage is set up on the Tucson. |
| 6. Paint materials | Paint / materials (2.6 refinish hrs @ $42.00) (109.20, I) | **Leave out** | — | Materials charge. |
| fee | Hazardous waste removal (7.50) | **Leave out** | — | Shop charge. Never kept (push 44). |

**Expected card:** 0 kept (+ up to 3 either-way); "N other jobs were left out" N = **4**–7.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| 2 *(either)* | 2026-06-03 | 14,022 | A/C condenser | Replaced A/C condenser (OEM 97606-N9000) after front collision; insurance claim | false | PCC-26-0412 | Precision Collision Center | Hyundai bumper-to-bumper (to Apr 5, 2030) | 0.00 |
| 3 *(either)* | 2026-06-03 | 14,022 | A/C system | Evacuated and recharged A/C (R-1234yf, 1.5 lb) after condenser replacement | false | PCC-26-0412 | Precision Collision Center | Hyundai bumper-to-bumper (to Apr 5, 2030) | 0.00 |
| 4 *(either)* | 2026-06-03 | 14,022 | Front radar sensor (ADAS) | Static calibration of front radar after bumper replacement | false | PCC-26-0412 | Precision Collision Center | Hyundai bumper-to-bumper (to Apr 5, 2030) | 0.00 |
- serviced_on: completion date 2026-06-03 is keyed. The drop-off date 2026-05-21 is acceptable. The odometer in (14,022) was read at drop-off.

**Totals check:** labor 610.00 + parts 900.30 + sublet 444.00 + paint materials 109.20 + hazardous waste 7.50 + tax 5.5% on parts & materials 55.52 = **2,126.52** grand total; less insurance **1,626.52** = customer deductible **500.00**.

### Order 09: Franchise dealer (Hyundai), 2025 Hyundai Tucson

- **Files:** `09-ro-hyundai-dealer-tucson-warranty-campaign.pdf` / `.jpg`
- **Shop:** Seaport Hyundai, 610 Example Harbor Boulevard, Testville, ME 00000. **Paper:** Warranty Repair Order, number **5590184** (labelled 'RO No.'), 1 page.
- **Date printed:** "09-16-2026" → **2026-09-16**. **Odometer:** in **19,880** / out 19,884.
- **Vehicle:** UAT S69 Hyundai Tucson, VIN `KM8JB3DE0SU690412`, in service 2025-04-05.
- **Coverages on the service day:** Hyundai bumper-to-bumper (to Apr 5, 2030) [60 mo / 60,000 mi]: **running**; Hyundai powertrain (to Apr 5, 2035) [120 mo / 100,000 mi (original owner)]: **running**.
- **Pay mix:** All warranty / campaign (customer pays $0.00).

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| A. Coolant smell, wet hose at reservoir | Replace coolant reservoir hose, top off, pressure test (90.00, W)<br>HOSE - RESERVOIR  25450-N9100 (31.85, W)<br>HYUNDAI LONG LIFE COOLANT (GAL)  00232-19055 (26.90, W) | **Keep** | Hyundai powertrain | Warranty repair on the cooling system, which counts as powertrain (push 45). |
| B. Liftgate will not stay open | Replace liftgate lift strut LH (45.00, W)<br>LIFTER ASSY - TAIL GATE LH  81770-N9000 (89.60, W) | **Keep** | Hyundai bumper-to-bumper | Warranty repair on a whole-vehicle part. |
| C. Service campaign 9ZZ (test) - transmission control software | Perform service campaign 9ZZ: update TCM software (75.00, R) | **Keep** | Hyundai powertrain | Hyundai-paid campaign on the transmission control software. |
| D. Multi-point inspection / complimentary wash | MPI (green) + complimentary wash (0.00, N) | **Leave out** | — | Inspection and wash. |

**Expected card:** 3 kept; "N other jobs were left out" N = **1**.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| A | 2026-09-16 | 19,880 | Coolant reservoir hose | Replaced leaking coolant reservoir hose, topped off coolant, pressure tested; Hyundai warranty | true | 5590184 | Seaport Hyundai | Hyundai powertrain (to Apr 5, 2035) | 0.00 |
| B | 2026-09-16 | 19,880 | Liftgate lift strut, left | Replaced left liftgate lift strut; Hyundai warranty | true | 5590184 | Seaport Hyundai | Hyundai bumper-to-bumper (to Apr 5, 2030) | 0.00 |
| C | 2026-09-16 | 19,880 | Transmission control module (software) | Service campaign 9ZZ: updated TCM software | true | 5590184 | Seaport Hyundai | Hyundai powertrain (to Apr 5, 2035) | 0.00 |

**Totals check:** Customer: labor 0.00 + parts 0.00 + fees 0.00 + tax 5.5% on taxable parts & fees (0.00) 0.00 = **0.00**. Billed to Hyundai warranty + campaign: labor 210.00 + parts 148.35 = **358.35** (not charged to the customer).

### Order 10: Motorcycle dealer, 2024 Harley-Davidson Street Glide

- **Files:** `10-workorder-harley-dealer-street-glide-5000-service-fork-seals.pdf` / `.jpg`
- **Shop:** Iron Ridge Harley-Davidson, 1 Example Thunder Road, Testville, ME 00000. **Paper:** Service Work Order, number **WO-35512** (labelled 'Work Order'), 2 pages.
- **Date printed:** "Saturday, June 14, 2025" → **2025-06-14**. **Odometer:** in **5,032** / out 5,041.
- **Vehicle:** UAT S69 Harley-Davidson Street Glide, VIN `1HD1KBC18RB690515`, in service 2024-09-07.
- **Coverages on the service day:** H-D limited warranty (to Sep 7, 2026) [24 mo / unlimited miles]: **running**.
- **Pay mix:** Mixed: customer pay + H-D warranty.

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| 1. 5,000 mi service - engine oil & filter | Change engine oil & filter (87.00)<br>SCREAMIN EAGLE SYN3 20W50 (QT) (89.75)<br>OIL FILTER, CHROME  62700296 (15.95) | **Keep** | H-D limited warranty | Engine upkeep required by the limited warranty. |
| 2. Primary chaincase fluid | Drain & refill primary chaincase (58.00)<br>FORMULA+ PRIMARY CHAINCASE LUBE (QT) (19.95) | **Keep** | H-D limited warranty | Drivetrain upkeep, part of the 5,000-mile service. |
| 3. Transmission fluid | Drain & refill transmission (58.00)<br>FORMULA+ TRANSMISSION LUBE (QT) (19.95) | **Keep** | H-D limited warranty | Transmission upkeep. |
| 4. 5,000 mi scheduled inspection | 5,000 mi scheduled maintenance inspection (72.50) | **Either way** | — | Inspection in the maker's schedule. The rules never keep inspections. Leaving it out is the default and is fine. |
| 5. Rear tire | R&R rear wheel, mount & balance tire (174.00)<br>DUNLOP D407T 180/65B16 REAR (289.95) | **Leave out** | — | Tires are not covered by the H-D warranty, and no tire coverage is set up. |
| 6. Front fork seals leaking (warranty) | Replace front fork oil seals both legs, refill fork oil (261.00, W)<br>FORK SEAL KIT  45400058 (48.90, W) | **Keep** | H-D limited warranty | Warranty repair inside 24 months. |
| fee | Shop supplies (12.00) | **Leave out** | — | Shop charge. Never kept (push 44). |
| fee | Environmental / disposal (5.00) | **Leave out** | — | Shop charge. Never kept (push 44). |

**Expected card:** 4 kept (+ up to 1 either-way); "N other jobs were left out" N = **3**–4.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2025-06-14 | 5,032 | Engine oil and filter | Changed engine oil (SYN3 20W50, 5 qt) and oil filter at 5,000-mile service | false | WO-35512 | Iron Ridge Harley-Davidson | H-D limited warranty (to Sep 7, 2026) | 192.70 |
| 2 | 2025-06-14 | 5,032 | Primary chaincase | Drained and refilled primary chaincase lubricant | false | WO-35512 | Iron Ridge Harley-Davidson | H-D limited warranty (to Sep 7, 2026) | 77.95 |
| 3 | 2025-06-14 | 5,032 | Transmission | Drained and refilled transmission lubricant | false | WO-35512 | Iron Ridge Harley-Davidson | H-D limited warranty (to Sep 7, 2026) | 77.95 |
| 4 *(either)* | 2025-06-14 | 5,032 | Scheduled maintenance inspection | 5,000-mile scheduled maintenance inspection | false | WO-35512 | Iron Ridge Harley-Davidson | H-D limited warranty (to Sep 7, 2026) | 72.50 |
| 6 | 2025-06-14 | 5,032 | Front fork seals | Replaced leaking front fork oil seals (both legs) and refilled fork oil; H-D warranty | true | WO-35512 | Iron Ridge Harley-Davidson | H-D limited warranty (to Sep 7, 2026) | 0.00 |

**Totals check:** Customer: labor 449.50 + parts 435.55 + fees 17.00 + tax 5.5% on taxable parts & fees (452.55) 24.89 = **926.94**. Billed to H-D warranty: labor 261.00 + parts 48.90 = **309.90** (not charged to the customer).

### Order 11: Snowmobile / powersports dealer (Polaris), 2024 Polaris 650 INDY XC 137

- **Files:** `11-ticket-snowmobile-dealer-polaris-preseason-fuel-pump-esc.pdf` / `.jpg`
- **Shop:** North Country Powersports, 88 Example Snowmobile Trail, Testville, ME 00000. **Paper:** Service Ticket, number **ST-11847** (labelled 'Ticket'), 1 page.
- **Date printed:** "2025-11-18 09:12" → **2025-11-18**. **Odometer:** in **1,486** | hour meter 52.3 h.
- **Vehicle:** UAT S69 Polaris INDY, VIN `SN1PEF6RXRC690616`, in service 2023-12-02.
- **Coverages on the service day:** Polaris factory (to Dec 2, 2024) [12 mo, date only]: **ended Dec 2, 2024 (time)**; Polaris extended service contract (to Dec 2, 2026) [24 mo, date only, $50 deductible per visit]: **running**.
- **Pay mix:** Mixed: service contract claim ($50 deductible) + customer pay.

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| 1. Pre-season inspection | Pre-season inspection (lights, controls, track, skis) (96.00) | **Leave out** | — | Inspection. |
| 2. Drive belt | Replace drive belt (36.00)<br>POLARIS DRIVE BELT  3211202 (159.99) | **Either way** | — | Wear item that service contracts exclude, but it is clutch and drivetrain upkeep. Either result is fine. |
| 3. Spark plugs | Replace spark plugs (48.00)<br>SPARK PLUG NGK PZFR6Z (28.98) | **Keep** | Polaris extended service contract | Engine upkeep. Maintenance proof the service contract asks for. |
| 4. Chaincase oil | Change chaincase oil (48.00)<br>POLARIS SYNTHETIC CHAINCASE LUBE (QT) (21.99) | **Keep** | Polaris extended service contract | Drivetrain upkeep. |
| 5. Clutch service | Clean & inspect primary/secondary clutch (96.00) | **Either way** | — | Upkeep on the drive clutches, with no part replaced. |
| 6. Carbide runners | Replace carbide runners (48.00)<br>CARBIDE RUNNER 6" (PAIR = 2) (129.98) | **Leave out** | — | Wear item. |
| 7. Hard start / low fuel pressure (service contract) | Diagnose & replace fuel pump assembly (180.00, ESC)<br>FUEL PUMP ASSY  2521549 (412.50, ESC)<br>Service contract deductible (per visit) (50.00) | **Keep** | Polaris extended service contract | A repair paid by the service contract. The customer paid only the $50 deductible. |
| fee | Shop supplies (9.50) | **Leave out** | — | Shop charge. Never kept (push 44). |

**Expected card:** 3 kept (+ up to 2 either-way); "N other jobs were left out" N = **3**–5.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| 2 *(either)* | 2025-11-18 | 1,486 | Drive belt | Replaced drive belt | false | ST-11847 | North Country Powersports | Polaris extended service contract (to Dec 2, 2026) | 195.99 |
| 3 | 2025-11-18 | 1,486 | Spark plugs | Replaced spark plugs (2) | false | ST-11847 | North Country Powersports | Polaris extended service contract (to Dec 2, 2026) | 76.98 |
| 4 | 2025-11-18 | 1,486 | Chaincase | Changed chaincase oil | false | ST-11847 | North Country Powersports | Polaris extended service contract (to Dec 2, 2026) | 69.99 |
| 5 *(either)* | 2025-11-18 | 1,486 | Primary and secondary clutch | Cleaned and inspected primary and secondary clutch | false | ST-11847 | North Country Powersports | Polaris extended service contract (to Dec 2, 2026) | 96.00 |
| 7 | 2025-11-18 | 1,486 | Fuel pump assembly | Diagnosed low fuel pressure; replaced fuel pump assembly under the Polaris extended service contract ($50 deductible) | true | ST-11847 | North Country Powersports | Polaris extended service contract (to Dec 2, 2026) | 50.00 |
- customer_paid: **50.00** (the deductible).
- odometer: miles (1,486). The 52.3 h hour meter is extra. Do not swap hours in for miles.

**Totals check:** Customer: labor 372.00 + parts 340.94 + fees 9.50 + deductible 50.00 + tax 5.5% on taxable parts & fees (350.44) 19.27 = **791.71**. Billed to service contract: labor 180.00 + parts 412.50 = **592.50** (not charged to the customer).

### Order 12: Independent garage (A/C and drivetrain), 2022 Subaru Outback

- **Files:** `12-invoice-independent-ac-shop-outback-cvt-fluid-ac-inspection.pdf` / `.jpg`
- **Shop:** Hillside Garage & A/C, 240 Example Hill Road, Testville, ME 00000. **Paper:** Invoice, number **HG-24518** (labelled 'Invoice'), 1 page.
- **Date printed:** "Apr 9, 2025" → **2025-04-09**. **Odometer:** in **41,120** / out 41,126.
- **Vehicle:** UAT S69 Subaru Outback, VIN `4S4BTACC5N3690311`, in service 2021-11-20.
- **Coverages on the service day:** Subaru basic (to Nov 20, 2024) [36 mo / 36,000 mi]: **ended Nov 20, 2024 (time)**; Subaru powertrain (to Nov 20, 2026) [60 mo / 60,000 mi]: **running**.
- **Pay mix:** All customer pay.

| Job | Lines on the paper (amount) | Answer | Coverage it matters under | Why |
|---|---|---|---|---|
| 1. A/C not cold - performance check & recharge | A/C performance test, evacuate, vacuum hold & recharge (125.00)<br>Refrigerant R-1234yf (lb) (89.00)<br>UV leak dye (9.95) | **Leave out** | — | The A/C is under bumper-to-bumper, which ended Nov 20, 2024, so no coverage is running for it. |
| 2. CVT fluid exchange | CVT fluid exchange (drain/fill x2), temp check (150.00)<br>Subaru High Torque CVTF (qt) (132.00) | **Keep** | Subaru powertrain | Transmission upkeep on a covered powertrain assembly. Powertrain runs to Nov 20, 2026 / 60k. |
| 3. Rear differential fluid | Rear differential fluid change (62.50)<br>Gear oil 75W-90 GL-5 (qt) (27.00) | **Keep** | Subaru powertrain | Drive-axle upkeep, which is powertrain. |
| 4. Headlamp bulb | Replace headlamp bulb LH low (25.00)<br>Bulb H11 low beam (18.99) | **Leave out** | — | Bulb. |
| 5. State inspection | State safety inspection (sticker #0000-TEST) (18.50) | **Leave out** | — | Inspection fee. |
| fee | Shop supplies (10.00) | **Leave out** | — | Shop charge. Never kept (push 44). |

**Expected card:** 2 kept; "N other jobs were left out" N = **4**.

Expected service entries (Keep rows required; Either-way rows only if kept or ticked):

| Job | serviced_on | odometer | part | work | warranty_repair | order_ref | shop | covered_by | customer_paid |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 2025-04-09 | 41,120 | CVT (transmission fluid) | CVT fluid exchange (8 qt Subaru High Torque CVTF) | false | HG-24518 | Hillside Garage & A/C | Subaru powertrain (to Nov 20, 2026) | 282.00 |
| 3 | 2025-04-09 | 41,120 | Rear differential | Changed rear differential gear oil (75W-90, 2 qt) | false | HG-24518 | Hillside Garage & A/C | Subaru powertrain (to Nov 20, 2026) | 89.50 |

**Totals check:** Customer: labor 362.50 + parts 276.94 + fees 28.50 + tax 5.5% on taxable parts & fees (286.94) 15.78 = **683.72**.

## Totals

- 12 orders, 58 jobs: **23 Keep**, **22 Leave out**, **13 Either way**. Another 14 fee lines are always left out.
- Every total was recomputed from the line items and found in each PDF's text layer (`validation.json`, kept with the generator on the build box in `/workspace/uat/scen-69-service-orders/`, not copied to the share). VIN check digits, odometer order per vehicle, past dates and "coverage running on the day" for every Keep job were also checked.

## Checked when this was made

- Built 2026-11-09 on the box from one data file (`s69_data.py`). The PDFs, JPG twins, this answer key and `validation.json` all come from it, so the amounts cannot drift. No app, database, mail or sign-in was used.
- Coverage windows were worked out against app date 2026-11-09. The F-150 bumper-to-bumper ended Jun 10, 2026, so order 04 has only powertrain. The Outback basic ended Nov 20, 2024 (order 12 A/C is left out). Its powertrain ended on **miles** before its date (order 07 is goodwill, not warranty).

## Known rough edges (not part of the answer key)

- **Tires and rotations (05, 06):** push 43 lists tires and rotations as left out, while a part with its own term should keep its work. Record which rule wins. A miss is the main finding this pack exists to catch.
- **Coverage ended on miles before its date (07):** **verify** the app does not treat Subaru powertrain as running on Oct 14, 2026 at 61,240 mi.
- **Recall / campaign / goodwill / road hazard / service contract** are all "paid by someone else". **Verify** each shows as repaired under warranty, or an equivalent, with the keyed customer amount. Record the label used.
- **Body shop (08):** collision work, with insurance paying and a deductible. No warranty money. **Verify** it is still read as a repair order and not as a purchase. The lifetime workmanship guarantee and the new battery's warranty in 04 are new coverages the owner may add by hand, not something the reader should create.
- **Snowmobile (11):** **verify** the vehicle kind used. Hours are printed alongside miles. Only miles go in `odometer`.
- **Quick-lube wording (02)** "Full Synthetic Oil Change" and the H-D "Change engine oil & filter" vs a typed maintenance task name: push 45 says matching needs the same words. Record any miss.
- **Either-way jobs** are judgment calls. Record what the rules chose. Both outcomes pass.
