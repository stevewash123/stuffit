# Scenario 61: Vehicles: add, odometer, time-and-miles coverage

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Clock offset 0 (app date **2026-11-05**). Migrations `VehiclesSlice1` and `VehiclePrivateSale` applied. **Run `--seed` on the database first**: it loads the "Vehicles" category, the vehicle makers (Ford, Honda, Yamaha and so on, as brands) and the seller "Private sale". Reader on for Part D; otherwise note "reader off".
**Time:** 45 min
**Built per:** S3.5.1 (add a vehicle), S3.5.2 (odometer readings and the pace), S3.5.3 (time-and-miles coverage). Branch `vehicles-slice1`.
**Why this plan:** a vehicle's warranty runs by time and miles, whichever comes first. The date is arithmetic; the miles exist only if the person enters them, so every miles figure must show the reading it rests on and an estimate must never end a coverage.

**Part A: add a vehicle (S3.5.1)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | My Items: look beside Add a purchase | **Add a vehicle** is offered |
| 2 | Test1 | Add a vehicle: nickname "UAT Dad's truck", kind Truck, year 2024, make Ford, model F-150, trim XLT, VIN 1M8GDM9AXKP042788, New, bought 2025-01-01, $52,000, odometer 12, miles | Opens its page. Shows Truck, "2024 · XLT · bought new", the VIN, **12 miles on Jan 1, 2025** as the first reading. No order number or card fields were asked |
| 3 | Test1 | Add a boat: kind Boat, unit hours, year 2027 | Label reads **Hull number**; year next year is accepted; no check-digit note |
| 4 | Test1 | Try year 1899 and year 2028, then a date bought of 2026-11-06 | Each refused with a plain message beside the field; nothing half-made in My Items |
| 5 | Test1 | Type VIN 1M8GDM9A1KP042788 (bad check digit) in the form and leave the field | A gentle note "This does not look like a valid VIN. Check it against the paper."; the vehicle still saves |
| 6 | Test1 | Choose Used | Asks for **first put in service**; leave it empty and save. Nothing is guessed; the page says "first put in service: not known" |
| 7 | Test1 | My Items, then the **Vehicles only** filter | Vehicles show a kind badge; the filter leaves a toaster out |
| 8 | Test1 | Attach a bill of sale PDF on the form, save, open the vehicle, **Read it** | The file is on the vehicle; make/model/price/date offered as a suggestion to accept or correct (VIN and year are **not** read: see Not built) |
| 9 | Test1 | Edit the vehicle (pencil, Edit vehicle details): change the unit to kilometres | Refused while it has readings or mile limits |
| 10 | Test1 | Delete the boat | Gone; its readings go with it |
| 10a | Test1 | Add a vehicle bought **1975-06-01** (a classic car) | Accepted: vehicles may be bought back to 1900. The same date on **Add a purchase** for an appliance is still refused (floor 1990-01-01) |
| 10b | Test1 | In the form's Make box type "Fo" and "Hon" | The seeded makers appear as shared brands (no "not yet in the shared list" badge). If none appear, `--seed` was not run |

**Part B: odometer readings (S3.5.2)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 11 | Test1 | Truck page: Add reading 14,000, date left as today | Saved. Newest first. "14,000 miles on Nov 5, 2026" (never without its date). Pace line says "Add another reading a month or more later..." and no estimate is shown |
| 12 | Test1 | Add 7,000 dated 2026-01-01, then 12,500 dated 2026-07-01 | Pace "About N miles a year, from your readings of ..." and an **estimated** "today" figure labelled estimated, smaller than the entered one. Estimated figure is not in the list of readings |
| 13 | Test1 | Add 500 dated 2026-08-01 | Asks once: "This is lower than the reading on Jul 1, 2026. Save it anyway?" Cancel saves nothing. Save it anyway keeps it flagged "lower than an earlier reading"; latest reading and pace ignore it |
| 14 | Test1 | Press "This reading is correct" on it | It now counts as the latest |
| 15 | Test1 | Try a reading dated tomorrow | Refused |
| 16 | Test1 | Edit one reading's value and date; delete one | Both work; the odometer lines follow |
| 17 | Test1 | Set the clock forward 14 months (offset) and look at the page | "last reading 14 months ago" beside the latest reading and beside every miles figure |

**Part C: time-and-miles coverage (S3.5.3)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 18 | Test1 | Truck: Add coverage, Maker's warranty "Powertrain", 2025-01-01 to 2030-01-01, mile limit 60000 | Shown as "Until Jan 1, 2030 or 60,000 miles, whichever comes first", remaining miles at the last reading with that reading's date, and (with a pace) which comes first and the month the miles run out |
| 19 | Test1 | Remove all but one reading | "Add odometer readings to see which comes first"; a note that the miles are not being watched and reminders use the date only |
| 20 | Test1 | Add Bumper-to-bumper "3 years or 36,000 miles" and Roadside with unlimited miles | Each has its own line; unlimited miles reads "with unlimited miles" |
| 21 | Test1 | Try unlimited miles with no end date | Refused (a coverage with neither is not a vehicle coverage) |
| 22 | Test1 | Enter a reading at or over a limit (e.g. 61,000 on 2026-03-10) | That coverage shows **ended by miles on Mar 10, 2026** with the reading that did it, and is expired like any coverage; the others are unaffected |
| 23 | Test1 | Correct the reading to 16,000 (or delete it) | The coverage opens again with its own end date |
| 24 | Test1 | Make the pace fast enough that the estimate passes the limit but enter no reading over it | "You have probably passed the limit. Enter your odometer to check." The coverage stays **Active** |
| 25 | Test1 | Home and the items list | Ending-soon counts and the row's end line use the earlier of the date and the estimated mile end, labelled **estimated** when it comes from miles |
| 26 | Test1 | Reminders (Settings, or the to-do/notification list at the due day) | A miles reminder says it is an estimate and asks for a fresh odometer reading; with no pace, reminders use the date |
| 27 | Test1 | Something broke (defect) on the truck | The option shows the date and the miles check; an ended-by-miles coverage is ruled out with the reading named; an estimate alone gives a "maybe" |
| 28 | Test1 | An appliance with a warranty | Unchanged: no miles anywhere, no mile field in its coverage form |

**Part D: the warranty reader (reader on)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 29 | Test1 | Upload a vehicle warranty booklet ("5 years or 60,000 miles") to the truck, Read it, apply | Coverage with 60,000 miles and the document's words quoted in the terms. A booklet with "unlimited miles" keeps it as unlimited, not a number. A booklet with no distance leaves the miles empty |
| 30 | Test1 | Apply the same booklet to an appliance | No mile limit is stored |

**Part F: Private sale (fixed seller)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 33 | Test1 | Add a vehicle, "Bought from": type "Private" | The shared seller **Private sale** is offered, with no unverified badge. Pick it and save (no dealer needed) |
| 34 | Test1 | Open it: the coverage area | The sentence **"Bought in a private sale. WarrantyCat assumes nothing: if the maker's warranty passes to a new owner, or you bought a plan, add it."** is shown. No "Not set up yet" alert, no suggested coverage, no store return window, no maker warranty counted from the purchase date. My Items shows it as "Nothing applies", not "Needs info"; Home's needs-info count does not include it |
| 35 | Test1 | Add a purchase of an ordinary item (a toaster), store **Private sale** | Same: the sentence, no return window, no suggestions. Any item can use it, not only vehicles |
| 36 | Test1 | Choose a credit card with Return protection and Purchase protection confirmed, on a private-sale purchase | No return-extension (return protection) coverage is offered or added. Purchase protection is still offered as usual. The same card on a store purchase offers both |
| 37 | Test1 | Upload a maker warranty booklet that says it is **not transferable** to the private-sale vehicle, apply it | Listed with the transfer term "Original purchaser only. Not transferable." and labelled **Not counted: not transferable**; it adds nothing to days left, the badge, Home or reminders. Correct the transfer term to Yes and it counts |
| 38 | Test1 | Upload a booklet that is transferable (or says nothing about it) to the same kind of item | It counts as normal. Coverage added by hand also counts as normal |
| 39 | Test1 | Try to change or delete the Private sale seller (My stores and brands, Settings) | It is not in the account's own list; it cannot be renamed or deleted by an account |
| 40 | Operator (Test4) | Admin Companies: Retailers list; try to add a return policy or warranty to Private sale (any route) | It is not in the Retailers list; any attempt is refused with "Private sale is a purchase from a person, not a store or a maker. It cannot have a return policy or a warranty." `--seed-placeholders` gives it no placeholder policy |
| 41 | Test1 | Export everything | `purchases.csv` has a `private_sale` column ("yes") beside the store name; `coverage.csv` marks a coverage not counted for being not transferable |

**Part E: export and isolation**

| # | Persona | Action | Expected |
|---|---|---|---|
| 31 | Test1 | Export everything | `vehicles.csv`, `odometer_readings.csv` (source, flag, whether it counts) and the mile columns in `coverage.csv` |
| 32 | Test2 | Open Test1's vehicle addresses | Not found |

**Not built (this slice):** VIN decoding and the door-sticker photo (S2.7.15); the VIN, year and in-service date are never read from a document, so every vehicle field is "entered by the person"; hours/kilometres wording is by unit only; readings mined from service invoices or dash photos (the source value exists, nothing sets it); prompts to update the odometer (come with maintenance); S3.5.4 start rules (in-service date is stored and shown only); S3.5.5 parts and the "delete a vehicle that has parts asks first" check (no parts exist); S3.5.6 part clocks from install odometer (the mile start field exists, always 0); changing a purchase's seller to Private sale afterwards does not re-check coverage already saved (the not-transferable mark is worked out when a coverage is saved).

Also record: any miles figure shown without the date of its reading, any estimate shown as if entered, and any place an estimated mile end ended a coverage.
