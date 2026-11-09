# What changed in push 43: service history on covered parts (2026-11-09)

For GrokBot. Check `/api/version` against the pushed API commit (UI changed too). **New migration `ServiceEntries`** (one new table, `service_entries`; Render migrates on start). No `--seed`. Retest Scenario 68 steps 5 and 6, which had no service feature before.

## New: a repair order on a vehicle becomes service history
- **Read it on a repair order** (a dealer or shop repair order, service invoice or work order, attached to a vehicle) no longer reads as a purchase or a plan. A card **"Service on covered parts"** appears with what would be kept: the date, the odometer, the shop and order number, and one line per job on a part a coverage covers. Nothing is saved until **Add to service history**; **Not now** keeps the paper only.
- **Only what is needed is kept.** A job is kept when a coverage that was running on the service day covers the part: a part with its own term, the **Powertrain** coverage for engine, transmission or CVT, drive and cooling parts, or else the whole-vehicle coverage. Tires, rotations, alignments, wipers, bulbs, cabin and air filters, brake pads, washes and shop fees are left out ("N other jobs were left out"). A job that warranty paid for is kept even when no coverage explains it.
- **A $0 warranty repair** (the S68 water pump) is marked **repaired under warranty** with what the customer paid. It is history only: it adds no claim, plan or coverage, and the factory bumper-to-bumper and powertrain ends do not move.
- **The odometer** on the order becomes a reading (source: from a document), unless the same date and value is already there. Adding the same order twice replaces its entries and adds no second reading.
- **Service history** is a list on the vehicle page (newest first): date, odometer, part, what was done, which coverage, and warranty or what you paid. Delete is shown in edit mode. It is in the data export as `service_history.csv`.
- **A VIN on the order that differs from the vehicle's** is warned about in the card and not blocked.

## Expected in S68
- Steps 5 and 6: Read it on the three customer-pay orders and the warranty order. Transmission fluid service and the oil/inspection work show under Powertrain or the whole-vehicle coverage (oil change counts as engine upkeep); the water pump shows as repaired under warranty at 20,800 miles (the order shows 20,802); no "Start a plan from it", no new coverage.
- Intermediate odometer readings (3,200 / 9,800 / 16,400 / 20,802) are added from the orders, dated by each service date.
- Live-reader check: the new reader fields (`lines`, `service_date`, `odometer`, `ro_number`, `shop`, `vin`) are untested against the real model. Report any order that is not recognised as a repair order, or any job kept that should not be.

## Not changed, do not report
- Maintenance-due reminders (what the warranty requires and when it lapses) are the next push, built on this.
- A repair order uploaded on its own (not on a vehicle) is kept as a paper and not turned into an item.
- Data-protection keys still not kept across deploys (needs its own table); powertrain narrative (P41-3) waiting for the screen and wording.

## Tests at push
API unit 1220, integration 511 (+2 opt-in skipped); UI 1366. Added: the matching rules (8 unit tests), a repair order end to end (kept, left out, reading, replace on repeat, coverages unchanged), the export file, four component specs and one page spec. Updated: two UI spec files that open a vehicle page now answer the new service-history request.
