# Scenario 41: A receipt's protection plan and stated warranty are read and attached (DRAFT)

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25) and are clean (empty New Items and My Items). The reader is on the real model (`Ai:Provider=anthropic`), so exact readings can vary: where a step says "expected" and the reader misses it, mark **Partial** and quote what it did read, not Fail. The sample receipts are in `Testing/SampleData/receipts/pdf` (the answer key is `receipts/pdf-as-jpg/answer-key-by-item.csv`). Upload each receipt through New Items.
**Time:** 50 min
**Built per:** S2.4.7 (a protection plan on a receipt is its own record, not an item or part of its name) and S2.4.8 (a warranty the receipt only states becomes a low-confidence "stated on receipt" coverage). **DRAFT:** the exact wording on New Items ("Includes: …", "Receipt says: …") is confirmed once the build is deployed; record what you see. NOT built, so not planned: reading a plan from a contract upload, several items per receipt each with its own plan, adding plan companies as shared data.
**Why this plan:** a person who paid for a plan, or whose receipt states a warranty, loses that coverage if the app drops it; and the app must never say something is covered only because a phrase was printed.

**Part A: protection plans (S2.4.7)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Upload `21-letter-bestbuy-email-marketing-geek-squad.pdf` (Sony WH-1000XM5 $349.99, "Geek Squad Protection - 2-Year Plan" $49.99, covers SKU 6505727, starts on delivery) | One New Item: the Sony headphones, price **349.99** (not 399.98 and not 421.98). The plan is **not** a second item and is **not** in the item's name. The row says what was found, for example "Includes: Geek Squad 2-year plan, $49.99", with the company and the term |
| 2 | Test1 | Look at the plan on the row | It shows the plan name as printed, the company, the price, the term (24 months), and that it **covers SKU 6505727** and matches the item. A way to edit or remove it before adding |
| 3 | Test1 | Remove the plan from the row, then reload | Gone. Reupload the same receipt (or use "undo" if offered) to bring it back; record how |
| 4 | Test1 | **Add** the item (not a quick add) with the plan kept | The item page shows the plan as coverage: provider Geek Squad, a 24-month term, with the start taken from "starts on delivery" if a delivery date is known, otherwise blank or the purchase date; record which and the end date shown. Nothing is invented. The plan also appears on **Extended warranties** (`/plans`) |
| 5 | Test1 | Upload `15-thermal-bestbuy-tv-geek-squad.pdf` ("GEEK SQUAD PROTECTION 4YR $299.99", no start date printed) | The TV and the plan (4 years, $299.99) are found; the plan has **no start date** and the row says so. A **quick add** does **not** attach this plan (a missing start or a doubtful plan is held back); add by hand and enter or confirm the start |
| 6 | Test1 | Upload `16-a5-bestbuy-dishwasher-geek-squad-install.pdf` (dishwasher $1,099.00, "Geek Squad Protection 3-Year" $229.99, "Geek Squad Standard Install" $129.99) | The dishwasher is the item. The 3-year plan is a plan ($229.99, 36 months). The **install line is not a plan and not an item** (a service). No warning about the totals (item + plan is not more than the total) |
| 7 | Test1 | Upload `30-thermal-walmart-vizio-tv-protection.pdf` and `33-a5-lowes-bosch-dishwasher-protection.pdf` | A protection plan is found at each store (the logic is not Best Buy specific). Record the company names as read. An unfamiliar company is kept as private to the account and marked **not verified** |
| 8 | Test1 | Open the plan company on `/plans` or the plan page | A known company shows its claim phone and website marked as coming from the company's record; an unlisted one shows neither |
| 9 | Test1 | Upload a receipt with **no** plan (any from Scenario 33) | No "Includes:" line; nothing about a plan invented |

**Part B: stated warranties (S2.4.8)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 10 | Test1 | Upload `17-thermal-unknown-store-generator-single.pdf` (footer "2 YR MFR WARRANTY") | The generator row says what the receipt states, for example "Receipt says: 2 YR MFR WARRANTY", with provider **maker** and a 24-month term, as **may apply / stated on receipt** (low confidence) |
| 11 | Test1 | Do a **quick add** of that row | The stated warranty is **not** attached by a quick add (only coverage at 80% or more is). Add by hand: confirm it. The item page shows a coverage labelled **Stated on receipt** (provider unconfirmed if unclear) |
| 12 | Test1 | Upload `06-half-letter-invoice-tires.pdf` ("Road hazard warranty 50,000 mi") | Shown as stated: "Receipt says: Road hazard warranty 50,000 mi". The mileage is shown **as stated, never turned into an end date**. The provider is **unconfirmed** (road hazard is usually the shop's program, tread life the maker's) |
| 13 | Test1 | Upload `20-thermal-unknown-maker-heat-pump-two-items.pdf` ("5 YR COMPRESSOR / 1 YR PARTS", a unit and another line) | The statement belongs to the **heat pump unit**, not the other line; the parts it names (compressor 5 years, parts 1 year) are recorded as stated |
| 14 | Test1 | Upload `13-a5-handwritten-style-repair-invoice.pdf` ("Repair warranty: 90 days parts and labor") | Read as a stated warranty of 90 days, parts and labor, on the repair line |
| 15 | Test1 | Upload `55-thermal-northeast-pellet-stove-two-items.pdf` ("10 YR LIMITED WARRANTY") | A 10-year limited stated warranty on the stove line; the second line is not given it |
| 16 | Test1 | Upload a receipt that only states a **return window** ("returns within 90 days") or a vague "may carry a manufacturer warranty" (for example a Home Depot receipt from the sample set) | **No** stated warranty is created from a return window or from a vague phrase |
| 17 | Test1 | Remove a stated warranty on a row before adding, then add the item | The item has no such coverage |
| 18 | Test1 | If a known maker or store policy exists for the item and agrees with the statement | The row shows it corroborates: for example "the receipt says 2 years; the maker's policy says 2 years". If the term differs, the difference is shown, never silently replaced. Record which cases you saw |
| 19 | Test2 | Open New Items and My Items | Nothing from Test1's uploads |

Also record: for each receipt, what was printed against what was read (store, item, price, plan name, price, term, stated warranty and term), any plan or warranty the reader invented that is not printed, any that it missed, and which receipts took over 20 seconds to read. Leave test data for the next plan unless told to clean it.
