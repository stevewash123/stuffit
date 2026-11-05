# What changed in push 23: Vehicles (add one, odometer readings, coverage by time and miles) and Private sale (2026-11-05)

For GrokBot. API `1ed55e3` and UI `0aba32b`; check `/api/version` and record the `commit` you see (it must be `1ed55e3`) and the UI build time. Migrations `VehiclesSlice1` and `VehiclePrivateSale` are applied to staging, and `--seed` has been run there (it loads the Vehicles category, the vehicle makers and the seller "Private sale"). Stories S3.5.1 to S3.5.3. New plan: **Scenario 61 - Vehicles slice 1**, Part A to F, Full only. Reader prompt is now `item-warranty-v6` (it also reads a mile limit): please also re-open **one plain warranty document you have used before** and say whether anything reads differently from last time.

## What you should see
| Where | What |
|---|---|
| My Items | **Add a vehicle** beside Add a purchase. A kind badge on vehicles, and a **Vehicles only** filter |
| Add a vehicle | Nickname, kind (car, truck, motorcycle, boat, RV and so on), year, make (shared brands: Ford, Toyota, Harley-Davidson...), model, trim, VIN (boats: hull number), new or used, bought on (any date back to 1900), price, odometer at purchase, miles, kilometres or hours, where bought. A bad VIN check digit gives a gentle note and still saves. A year outside 1900 to next year, or a date bought later than today, is refused |
| Vehicle page | Kind, year, VIN, "first put in service" (not known stays not known), the latest reading **with its date**, papers, **Read it** on an attached paper |
| Odometer readings | The odometer at purchase is the first reading. Add, edit, delete. A reading lower than an earlier one asks once and is kept flagged, not counted until confirmed. Pace needs two readings 30 or more days apart; otherwise "Add another reading a month or more later to estimate your pace". An estimate is labelled and never saved |
| Coverage with a mile limit | Both limits show, and which comes first. "N miles left at your last reading (value on date)" and separately "About N miles left today (estimated)". An entered reading at or over the limit ends it **by miles**; an estimate alone never ends it ("You have probably passed the limit. Enter your odometer to check"). Unlimited miles and miles with no date are accepted. A mile limit is refused on a non-vehicle item. Reminders, Home and the badge use the earlier end, labelled estimated |
| Reader | A warranty document's mile limit fills with its quote; "unlimited" stays unlimited; no distance in the document leaves it empty |
| **Private sale** | A shared seller, offered in the seller picker everywhere (vehicle form, Add a purchase). Any item can use it. The item page says: "Bought in a private sale. WarrantyCat assumes nothing: if the maker's warranty passes to a new owner, or you bought a plan, add it." No missing-coverage alert (the badge reads "Nothing applies"), no return window, no maker warranty from shared data, no card return protection offered. Card purchase protection and extended warranty are unchanged. A maker's warranty the reader marks not transferable is listed and labelled "Not counted: not transferable"; coverage from a document or added by hand otherwise counts as normal |
| Export | `vehicles.csv`, `odometer_readings.csv`, mile columns in `coverage.csv`, a `private_sale` column in `purchases.csv` and `my_stores_and_brands.csv`, and a not-counted mark for a not-transferable coverage |

## Decided, do not report
- A reading added late and dated earlier does not flag a later, lower reading; only a new reading lower than an earlier one is flagged.
- The odometer unit cannot be changed once a vehicle has readings or mile limits.
- Coverage start dates before 1990 are still refused, for vehicles too (only the date bought goes back to 1900).
- Changing an existing purchase's seller to Private sale later does not re-check coverage already saved.
- Price protection from a card is not changed by Private sale.

## Not built, mark Not built (not Fail)
- VIN decoding and the door-sticker photo (S2.7.15). The VIN, year and in-service date are never read from a document.
- Readings mined from service records or dash photos.
- Start rules for vehicle coverage (S3.5.4), parts on a vehicle (S3.5.5), part warranties by miles from install (S3.5.6), odometer prompts, maintenance and repairs.
- Deleting a vehicle that has parts asks first: there are no parts yet.

## Also in this build
- The Scenario 54 Part B fixes from push 22 are already out; this build does not change them.
