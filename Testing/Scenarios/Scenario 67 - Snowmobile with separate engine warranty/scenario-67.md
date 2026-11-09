# Scenario 67: Powersports-dealer snowmobile, machine warranty and separate engine warranty (happy path)

**Accounts:** Test1 (Alice); Test2 (Bob) only for optional isolation check.
**Preconditions:** Test1's **personal account**, clock offset **0**, app date **2026-11-09** (America/New_York). Vehicle kind that accepts a snowmobile (Car/Motorcycle/Boat/Other — **verify** which kind the form uses for a sled; if none fits, use Other or the closest powersports kind and record it). Parts-on-a-vehicle supported (Scenario 62 / push 27). Reader on or record **reader off**. Preserve all existing business fixtures. **Ski-Doo** is seeded as a vehicle maker (Make list). There is **no Ski-Doo model** in `product_models`: type **Renegade Adrenaline 900 ACE**. Rotax / 900 ACE is not a seeded vehicle model; enter the engine as a normal part with a typed brand/model, not a new seeded vehicle. No reference-data write was made for this pack.
**Time:** 45 min
**Built per:** Scenario 1 document order; Scenario 62 separate part and install date; Scenario 65 boat+outboard pattern; pushes 25, 27, 28, 37 and 40.
**Why this plan:** a common snowmobile folder has a package agreement, one machine/chassis warranty, a separate longer engine-maker warranty and a VIN plate photo. A one-year machine term must not become one year on the engine.

## The purchase (answer key)

| Fact | Value |
|---|---|
| Vehicle / category / kind | **UAT P40 S67 Ski-Doo Renegade** / Vehicles / **verify** snowmobile kind (Other or Motorcycle if no Snowmobile) |
| Make / model / year | **Ski-Doo / Renegade Adrenaline 900 ACE / 2026**; Ski-Doo in Make list; model typed |
| Seller | **UAT Northwoods Power Sports**, 400 Example Trail Road, Testville, ME 00000; fictional powersports dealer |
| Condition / ownership / paid by | New / Bought / Cash or check |
| Purchase / first in service | **2026-11-08 / 2026-11-08** |
| VIN / reading | **2UATSD900A0000067** (synthetic 17-character VIN) / **12 miles / 0.4 hours on 2026-11-08** |
| Package / allocation / tax / fees / paid total | **$19,000** = chassis/equipment **$14,500** + included engine **$4,500**; tax **$1,140**; title **$185** + prep **$175**; **$20,500 total** |
| Vehicle price field | **$19,000 package price**, excluding tax/fees. The engine allocation is not another $4,500 payment |
| Machine warranty provider / type | **Ski-Doo / maker warranty**, Came with the product |
| Machine / chassis and factory sled equipment | Parts and labor, **2026-11-08 to 2027-11-08**, 12 months; **no hour/mile limit** |
| Cosmetic finish / soft goods | Parts and labor, **2026-11-08 to 2027-05-08**, 6 months; **no hour/mile limit** |
| Part item | **UAT P40 S67 Rotax Engine**, **Rotax / 900 ACE / 2026**, serial **UAT-RTX-067-2026**; normal item linked as Part of snowmobile |
| Part purchase / install / reading | **2026-11-08 / 2026-11-08 / 0.4 hours (12 miles) at install**; $4,500 allocation already included in sled package, not an extra purchase outlay |
| Engine provider / warranty | **Rotax**, maker warranty, Came with the product, parts/labor, **2026-11-08 to 2029-11-08**, 36 months, **no operating-hour cap**, $0 deductible |
| Registration / plans | Dealer registered both at handover; no pending registration, separate purchased plan, trailer or lease |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 1 | `01-snowmobile-purchase-agreement.pdf` | One-page package agreement with chassis/engine line allocations and totals | Sled form attachment / saved vehicle |
| 2 | `02-skidoo-machine-limited-warranty.pdf` | Two-page machine schedule with clear engine exclusion | Vehicle > Read it |
| 3 | `03-rotax-engine-warranty.pdf` | Two-page engine warranty and commissioning record | **Engine part item**, not the sled's machine warranty |
| 4 | `04-vin-plate-photo.jpg` | Photo-style VIN plate matching the purchase paper | Vehicle documents/photos as retained evidence; VIN manually entered |

### Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Confirm personal account / clock 0. Add > Vehicle > choose snowmobile-capable kind (**verify**). New, Bought. Select Ski-Doo from Make; type Renegade Adrenaline 900 ACE; use key, attach agreement 1 | One vehicle, VIN, year 2026, $19,000 package price, first-service 2026-11-08 and first reading 12 miles / 0.4 hours if hours supported. If custom model is refused, stop with reference-data blocker, not a product/warranty failure |
| 2 | Test1 | Read agreement on the saved vehicle and inspect suggestions | Target Ski-Doo maker/model, seller, 2026-11-08 and $19,000 package subtotal; document total $20,500 retained. Engine identity and $4,500 allocation are explicit, but **no promise of automatic part creation**. Do not accept a duplicate sled, a $4,500 second cash outlay, or engine warranty assigned to Ski-Doo chassis. Enter/correct VIN/year/in-service/reading manually |
| 3 | Test1 | Upload/read machine warranty 2; inspect and accept | Machine 12 months to 2027-11-08 and finish/soft goods 6 months to 2027-05-08 with quotes; provider Ski-Doo. Neither term includes Rotax engine. No numeric mileage/hour limit; the 12-month term is not applied to the engine |
| 4 | Test1 | Attach VIN photo 4, open it, compare manually with agreement and vehicle details | Clear **2UATSD900A0000067**, 2026 Renegade Adrenaline 900 ACE. VIN/year extraction and plate decoding are **Not built** in Scenario 61; photo retention/view is tested, not auto-fill |
| 5 | Test1 | Vehicle > Parts > Add a part. Add UAT P40 S67 Rotax Engine, Rotax / 900 ACE, serial, 2026-11-08 purchase and install, allocated value $4,500 if required by the form; attach engine paper 3 | A normal part linked to this sled, not another Vehicle; own brand Rotax, not parent Ski-Doo. No new $4,500 payment beyond the package; see accounting verify below. Install date known, no start-date-to-confirm state |
| 6 | Test1 | On the **part**, Read it for engine warranty 3 and apply | Maker Rotax, 36-month parts/labor term **2026-11-08 to 2029-11-08**. Unlimited operating hours in words/no numeric cap; preserve original no-hour-limit quote. No made-up hour or mile cap; no engine term created on the chassis |
| 7 | Test1 | Open vehicle Parts list, part page and vehicle coverage details; reload | Link works both ways; **Part of UAT P40 S67 Ski-Doo Renegade** shown. Machine/finish remain Ski-Doo, engine remains Rotax. Uploaded-paper source/quotes kept; record **Extracted from receipts** if that is the displayed document-derived source bucket. Earliest machine end 2027-05-08 (finish) / 2027-11-08 (machine); engine's separate end 2029-11-08 |
| 8 | Test1 | Inspect To do / Notifications, without changing time or running jobs | No overdue registration invented: dealer completion is documented. No lease task, first-service/installation task after dates saved, or expiry reminder due at clock 0. Future date reminders/name-of-component behavior and lead time are **verify**, not clock-tested here |
| 9 | Test2 | Optional direct link from Bob's personal account | Sled, engine and files not accessible; do not perform in the shared business |

## Checked when this was made

- Sled package totals, separate providers, all dates and VIN consistency checked locally. PDFs, VIN plate photo and first-page renders produced by the local generator. No app/DB modifications or sign-ins for this pack.
- DB read-only 2026-11-09: **Ski-Doo** (and Polaris, Arctic Cat, Yamaha) flagged `is_vehicle_maker`; **0** Ski-Doo / Polaris / Arctic Cat / Yamaha rows in `product_models`. Maker selectable; model typed. 80 vehicle makers total at check time.

## Known rough edges (not part of the answer key)

- **Verify** which vehicle kind the UI offers for a snowmobile. If none, use Other (or Motorcycle) and record the choice.
- **Verify custom model entry**; Ski-Doo is seeded as maker. If model entry is refused, seed Renegade Adrenaline 900 ACE before running. No seed changes in this deliverable.
- Scenario 61 says hours/kilometres wording is unit substitution; do not assume a snowmobile-specific policy reader or automatic VIN/photo recognition. Decimal 0.4-hour reading and a part's fractional install reading are **verify**; if unsupported, leave reading blank rather than invent a rounded value. Warranty is date-only and remains runnable.
- **Verify** how a bundled engine's allocated value is represented without inflating purchase totals. Use the package agreement as the single cash-outlay truth; a $4,500 part item is allocation metadata, not a second bill. Automatic purchase-line-to-part linking is not documented.
- **Verify** reader multi-component/source wording and that "no operating-hour limit" is retained as quote/date-only rather than a bogus numeric mileage cap. All coverage end dates are explicit. Reader misses are Partial and may be corrected against this key.
