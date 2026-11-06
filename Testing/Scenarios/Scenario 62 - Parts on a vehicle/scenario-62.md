# Scenario 62: Parts on a vehicle, and part warranties by miles from install

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Clock offset 0 (app date **2026-11-06**). Migration `PartsOnAVehicle` applied (staging). `--seed` run (Vehicles category, makers). Reader on for Part D; otherwise note "reader off".
**Time:** 45 min
**Built per:** S3.5.5 (parts on a vehicle), S3.5.6 (part warranties by miles from the day it was installed).
**Why this plan:** a part is an ordinary item that belongs to a vehicle. Its clock starts when it was installed, and its miles are counted from the odometer reading at install, not from the vehicle's lifetime miles.

**Setup:** Test1 adds vehicle "UAT Truck" (Truck, 2024 Ford F-150, new, bought 2025-01-01, odometer 38,000 miles on 2025-01-01) and a reading of 40,000 on 2026-11-06.

**Part A: add and see parts (S3.5.5)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Truck page | A **Parts** section with **Add a part** and **Link an item you already have**. Empty: no parts line |
| 2 | Test1 | Add a part: "UAT Tires", brand Michelin, bought 2026-09-01, installed on 2026-09-01, odometer at install 38,000, warranty 50,000 miles and 72 months | Add form opens with the vehicle already chosen (not asked again) and asks only the two extra facts. No company, plan or insurance is required. The part saves as an item |
| 3 | Test1 | Truck page: Parts list | Row shows name, brand, installed date, coverage ("Warranty until ... or 88,000 miles on the odometer", the mile end = install reading + limit). Summary line like "1 part." |
| 4 | Test1 | My Items | "UAT Tires" appears like any item with a **Part of UAT Truck** tag. A filter for **Parts** shows only parts; **Vehicles only** still shows only vehicles |
| 5 | Test1 | Open the part's page | Its own purchase, receipt, coverages, people and reminders; "Part of UAT Truck" with a link to the truck |
| 6 | Test1 | Add a part with no warranty ("UAT Floor mats") | Listed without a warranty; saves; nothing is asked about a company |
| 7 | Test1 | Truck owner/followers: add a follower on the truck first, then add a part | The new part starts with the truck's owner and followers, and they can be changed |

**Part B: link, unlink, rules**

| # | Persona | Action | Expected |
|---|---|---|---|
| 8 | Test1 | Add an ordinary item "UAT Battery" (not linked). On its page choose **Part of a vehicle**, pick the truck, installed 2026-10-01, reading 39,500 | Linked; appears under the truck; tag in My Items |
| 9 | Test1 | Try to link the truck as a part of "UAT Tires" (or of itself) | Refused with a plain message; a vehicle is never a part |
| 10 | Test1 | Add a second vehicle "UAT Trailer", then on the battery use **Move to another vehicle** | Asks for the new install date (required) and the reading; the earlier stretch is kept as history ("Earlier"); the miles used on the truck come off the limit; a blank reading on leaving is recorded as not known |
| 11 | Test1 | **Take it off the vehicle** (battery) | Asks to confirm; the part stays as an item with its date-only coverage; its mile end is dropped, "Miles no longer watched" with the last known mile end |
| 12 | Test2 | Try to link Test1's items by id (API) | Not found |

**Part C: part coverage by miles from install (S3.5.6)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 13 | Test1 | Tires: look at the coverage | Both limits shown, which comes first when there is a pace, mile end on the **truck's odometer** = 38,000 + 50,000 = **88,000** |
| 14 | Test1 | Add a part with a warranty but **no install date** | Date counts from the purchase date and is marked "start date to confirm"; the miles side says to add the odometer when installed to watch the miles |
| 15 | Test1 | A part with no vehicle and a warranty with miles | Date-only warranty works; the miles side says it needs the vehicle's odometer |
| 16 | Test1 | Add reading on the truck of 89,000 | Tires show **ended by miles** with the reading that did it. An estimate alone never ends a coverage |
| 17 | Test1 | Two-stage battery: add "Free replacement" 36 months and "Prorated" to 72 months as two coverages (prorated flag on the second) | The prorated one is labelled **Prorated: you pay a share** on the item page, in claim guidance and in the list; never shown as full coverage; no share is calculated |
| 18 | Test1 | Something broke on the tires (defect) | Claim guidance shows both limits; prorated stages say you pay a share |

**Part D: delete, dispose, export**

| # | Persona | Action | Expected |
|---|---|---|---|
| 19 | Test1 | Delete the truck while it has parts | Asks: delete the parts with it, or keep them as separate items. Never silently one or the other |
| 20 | Test1 | Mark a vehicle returned/disposed that has parts | The same question |
| 21 | Test1 | Keep the parts | Each keeps its dates and last known mile end, marked "Miles no longer watched" |
| 22 | Test1 | Export (Settings) | The vehicle's parts and each part's coverages are in the export, plus a part history file |

**Part E: warranty reader (reader on)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 23 | Test1 | Upload a tire warranty paper ("50,000 miles ... 72 months, prorated after 36 months") to the tires part, read it, apply | Mile limit, time limit and a separate prorated stage, with quotes. What the document does not say stays empty |
| 24 | Test1 | Same paper applied to an ordinary appliance | No mile limit is stored |

## Not built / known
- A prorated stage read from a document is added when the document is applied on the item page, not on a waiting New Item.
- The stages are separate coverages but are not named "Free replacement"/"Prorated" automatically.
- Exact button wording may differ slightly from the above; report the wording you see.
