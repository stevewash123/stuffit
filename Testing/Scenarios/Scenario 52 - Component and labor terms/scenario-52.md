# Scenario 52: One warranty, several parts, parts and labor on different clocks

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Test1 has the Chase Freedom Unlimited card ending 1111. Clock offset 0 (app date 2026-11-04). The reader is on the real model, so a miss on a document step is **Partial** with what it did read, not Fail.
**Time:** 55 min
**Built per:** S3.2.8 phase 1 (component terms, parts vs labor, `ManufacturerPolicyTerm`, `Coverage.Component`, `LaborEndDate`), S2.4.1 (document reader), S4.1.1 (reminder names the part). Sample documents: `Testing/SampleData/warranties/standard-appliance-limited-warranty.pdf`, `warranties-from-receipts/{12,14,15}-*.pdf`; receipts `receipts/pdf/{51,53,55,81}-*.pdf`.
**Why this plan:** this is the most common real warranty shape and the one most easily flattened to a single number. A person told "10 years" for a fridge whose whole-product term is 1 year will skip a claim or expect one that is refused. Until now only the reader was checked (T2 B4); this checks what the **item page** says.

**Answer key (dates count from the purchase date)**

| Item | Purchase | Whole product | Component lines (parts / labor) |
|---|---|---|---|
| A: Samsung RF28R7551SR, from the document | 2026-10-10 | 1 year, parts and labor: ends **2027-10-10** | Sealed refrigeration system: parts **2031-10-10**, labor only to **2027-10-10** (labor after the first year is the owner's cost). Digital inverter compressor: **2036-10-10**, replacement compressor only |
| B: Samsung RF28T5001SR (receipt 81), shared data, no document | 2026-08-15 | 12 months: ends **2027-08-15** | Ice maker 24 months (**2028-08-15**); sealed system 60 / 60 (**2031-08-15**); digital inverter compressor parts 120 (**2036-08-15**), labor 60 (**2031-08-15**) |
| C: Frostline FL18-HP (receipt 51 + doc 15) | 2026-06-18 | not 5 years | Compressor 5 years (**2031-06-18**); parts 1 year (**2027-06-18**) |
| D: Mitsubishi MSZ-GL12NA (receipt 53 + doc 12) | 2026-07-30 | not 7 years | Compressor 7 years (**2033-07-30**); parts 5 years (**2031-07-30**); registration condition (deadline 2026-09-28) |
| E: Emberly EP40 (receipt 55 + doc 14) | 2026-10-09 | headline "10 years limited, tiered" | Components shorter than the headline; nothing shows 10 years on every part |

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Add by hand: "UAT Samsung Fridge A", brand Samsung, model RF28R7551SR, bought 2026-10-10, $1,899, card 1111. Open it | Maker warranty proposed or absent; record which. This item has no shared-data match for the model, so the terms in the next steps come from the document |
| 2 | Test1 | On the item, upload `standard-appliance-limited-warranty.pdf` | "Reading your document..."; model RF28R7551SR matches the item; terms listed per part with quotes; nothing saved until accepted |
| 3 | Test1 | Read the suggestion before accepting | **Three lines**: whole refrigerator 1 year; sealed refrigeration system 5 years (parts only, labor stops after year 1); digital inverter compressor 10 years (replacement compressor only). **No single "5 years" or "10 years" for the whole product.** Start is the purchase date, 2026-10-10 |
| 4 | Test1 | Accept and open the item page | One line for the whole product plus one line per part, each with its own end date per the key. The sealed system line says parts and labor differ (for example "parts to 2031, labor to 2027"). Record the exact wording |
| 5 | Test1 | Check Next to end on the item and on Home | It is the **whole product** (2027-10-10), not a component and not 2036 |
| 6 | Test1 | Check the card extension | The Chase extended warranty adds 12 months to the **whole-product** term only if the card rules say so (ends 2028-10-10). It is not stacked onto the 10-year compressor line. Record what it did |
| 7 | Test1 | From receipt 81 (`81-letter-homedepot-samsung-fridge-protection-plan.pdf`) add "Samsung RF28T5001SR" with no document | Shared Samsung refrigerator policy proposes the whole product plus three parts, dates per row B. The ice maker line appears here (the shared data lists it) and not in item A (the document does not) |
| 8 | Test1 | Quick add the item from step 7 | Quick add attaches only coverage at 80% or more. Record whether the component lines came with it or only the whole-product line |
| 9 | Test1 | On item B upload `standard-appliance-limited-warranty.pdf` (model RF28R7551SR, not this fridge) | **Mismatch warning** (document is for another model). Nothing applied silently. Item B's coverage is unchanged |
| 10 | Test1 | Upload receipt 51 (`51-thermal-downeast-heating-frostline-18k.pdf`), add the unit and then upload `15-frostline-18k-minisplit-5yr-compressor.pdf` | Two terms read: compressor 5 years, parts 1 year. **No single term for the unit.** Dates per row C. The "installation not included" line on the receipt is not a warranty |
| 11 | Test1 | Upload receipt 53 and add the indoor unit, then `12-mitsubishi-minisplit-7yr-compressor.pdf` | Compressor 7 years, parts 5 years, dates per row D. The registration condition is shown; the app **asks** whether the unit was registered by 2026-09-28 (a date already past) and does not assume it was. Record the question and what each answer does |
| 12 | Test1 | Upload receipt 55, add the stove, then `14-emberly-pellet-stove-10yr.pdf` | Read as a limited, tiered warranty on the stove line (the other line is not given it). The 10 years is **not** applied to every part. If proration after year 5 is mentioned, it is kept as text, not turned into a date. Medium confidence is expected |
| 13 | Test1 | Move the clock to 2027-10-03 (T1-simulating-time) | A reminder for item A names the **part**, "whole refrigerator" (ends in 7 days). No reminder yet for the sealed system or compressor |
| 14 | Test1 | Move the clock to 2027-10-11 | Item A whole product shows ended; the sealed system and compressor lines still show active (parts). The item page does not say "expired" for the item as a whole while parts are still covered. Record the wording |
| 15 | Test1 | Move the clock to 2031-10-11 (reset to 0 afterwards) | Sealed system ended, compressor still active until 2036-10-10 |
| 16 | Test1 | Edit the purchase date of item A to 2026-10-20 | Every component end date moves by 10 days; labor end date moves too |
| 17 | Test1 | Delete item B's whole-product coverage | Component lines are removed or reattached with it. Record which; no orphan "Compressor" line remains pointing at nothing |
| 18 | Test2 | Open Test1's items by address | Not found; nothing visible |

Also record: any component line with no source, any date that disagrees with the key by a day or more, any place the whole product is shown as 5 or 10 years, and any wording that says "covered" for a part whose labor term has ended.
