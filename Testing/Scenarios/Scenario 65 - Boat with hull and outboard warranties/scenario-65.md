# Scenario 65: Marine-dealer boat package, hull warranty and separate outboard warranty (happy path)

**Accounts:** Test1 (Alice); Test2 (Bob) only for optional isolation check.
**Preconditions:** Test1's **personal account**, clock offset **0**, app date **2026-11-08** (America/New_York). Vehicle kind Boat, hours and parts-on-a-vehicle supported (Scenario 62 / push 27). Reader on or record **reader off**. Preserve all existing business fixtures. The 180-model manifest has **no boat maker or boat model**: type **Tracker / Pro Team 175 TXW** if the form permits custom values; otherwise mark **Blocked: model seed needed** and have the staging owner add that reference data. Do not substitute a car. Mercury / 60ELPT FourStroke is also not in that vehicle-model manifest; enter the engine as a normal part with a typed brand/model, not a new seeded vehicle. No reference-data write was made for this pack.
**Time:** 45 min
**Built per:** Scenario 1 document order; Scenario 61 Boat/hours; Scenario 62 separate part and install date; pushes 25, 27, 28 and 37.
**Why this plan:** a common boat folder has a marine package agreement, one hull warranty, a separate engine-maker warranty and a hull ID photo. A five-year hull term must not become five years on the engine or all equipment.

## The purchase (answer key)

| Fact | Value |
|---|---|
| Vehicle / category / kind | **UAT P38 S65 Tracker Bass Boat** / Vehicles / Boat |
| Make / model / year | **Tracker / Pro Team 175 TXW / 2026**; not in model seed, type or request seed |
| Seller | **UAT Bluewater Marine**, 300 Example Marina Road, Testville, ME 00000; fictional marine dealer |
| Condition / ownership / paid by | New / Bought / Cash or check |
| Purchase / first in service | **2026-11-07 / 2026-11-07** |
| HIN / reading | **UAT65001H526** (synthetic 12-character hull ID) / **0.8 hours on 2026-11-07** |
| Package / allocation / tax / fees / paid total | **$27,000** = hull/equipment **$18,000** + included engine **$9,000**; tax **$1,620**; title **$200** + prep **$180**; **$29,000 total** |
| Vehicle price field | **$27,000 package price**, excluding tax/fees. The engine allocation is not another $9,000 payment |
| Hull warranty provider / type | **Tracker / maker warranty**, Came with the product |
| Hull structure | Welded hull/transom, parts and labor, **2026-11-07 to 2031-11-07**, 60 months; **no hour limit** |
| Factory boat equipment / finish | Non-engine equipment and finish, parts and labor, **2026-11-07 to 2027-11-07**, 12 months; **no hour limit** |
| Part item | **UAT P38 S65 Mercury Outboard**, **Mercury / 60ELPT FourStroke / 2026**, serial **UAT-MER-065-2026**; normal item linked as Part of boat |
| Part purchase / install / reading | **2026-11-07 / 2026-11-07 / 0.8 hours at install**; $9,000 allocation already included in boat package, not an extra purchase outlay |
| Engine provider / warranty | **Mercury**, maker warranty, Came with the product, parts/labor, **2026-11-07 to 2029-11-07**, 36 months, **no operating-hour cap**, $0 deductible |
| Registration / plans | Dealer registered both at handover; no pending registration, separate purchased plan, trailer or lease |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 1 | `01-marine-purchase-agreement.pdf` | One-page package agreement with hull/engine line allocations and totals | Boat form attachment / saved boat |
| 2 | `02-boat-hull-structural-warranty.pdf` | Two-page hull and equipment schedule with clear engine exclusion | Boat > Read it |
| 3 | `03-mercury-outboard-warranty.pdf` | Two-page engine warranty and commissioning record | **Outboard part item**, not the boat's hull warranty |
| 4 | `04-hin-plate-photo.jpg` | Photo-style HIN plate matching the purchase paper | Boat documents/photos as retained evidence; HIN manually entered |

### Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Confirm personal account / clock 0. Add > Vehicle > Boat, New, Bought, hours. Type Tracker and Pro Team 175 TXW if not suggested; use key, attach agreement 1 | One boat, HIN label rather than VIN, year 2026, $27,000 package price, first-service 2026-11-07 and first reading 0.8 hours. If custom make/model is refused, stop with reference-data blocker, not a product/warranty failure |
| 2 | Test1 | Read agreement on the saved boat and inspect suggestions | Target boat maker/model, seller, 2026-11-07 and $27,000 package subtotal; document total $29,000 retained. Engine identity and $9,000 allocation are explicit, but **no promise of automatic part creation**. Do not accept a duplicate boat, a $9,000 second cash outlay, or engine warranty assigned to Tracker. Enter/correct HIN/year/in-service/reading manually |
| 3 | Test1 | Upload/read hull warranty 2; inspect and accept | Hull structure 60 months to 2031-11-07 and factory equipment/finish 12 months to 2027-11-07 with quotes; provider Tracker. Neither term includes Mercury engine. No numeric mileage/hour limit; the 60-month term is not applied to all boat equipment |
| 4 | Test1 | Attach HIN photo 4, open it, compare manually with agreement and vehicle details | Clear **UAT65001H526**, 2026 Pro Team 175 TXW. HIN/year extraction and plate decoding are **Not built** in Scenario 61; photo retention/view is tested, not auto-fill |
| 5 | Test1 | Boat > Parts > Add a part. Add UAT P38 S65 Mercury Outboard, Mercury / 60ELPT FourStroke, serial, 2026-11-07 purchase and install, allocated value $9,000 if required by the form; attach engine paper 3 | A normal part linked to this boat, not another Vehicle; own brand Mercury, not parent Tracker. No new $9,000 payment beyond the package; see accounting verify below. Install date known, no start-date-to-confirm state |
| 6 | Test1 | On the **part**, Read it for engine warranty 3 and apply | Maker Mercury, 36-month parts/labor term **2026-11-07 to 2029-11-07**. Unlimited operating hours in words/no numeric cap; preserve original no-hour-limit quote. No made-up 36,000-hour or 60,000-mile cap; no engine term created on the hull |
| 7 | Test1 | Open boat Parts list, part page and boat coverage details; reload | Link works both ways; **Part of UAT P38 S65 Tracker Bass Boat** shown. Hull/finish remain Tracker, engine remains Mercury. Uploaded-paper source/quotes kept; record **Extracted from receipts** if that is the displayed document-derived source bucket. Earliest boat equipment end 2027-11-07; engine's separate end 2029-11-07 |
| 8 | Test1 | Inspect To do / Notifications, without changing time or running jobs | No overdue registration invented: dealer completion is documented. No lease task, first-service/installation task after dates saved, or expiry reminder due at clock 0. Future date reminders/name-of-component behavior and lead time are **verify**, not clock-tested here |
| 9 | Test2 | Optional direct link from Bob's personal account | Boat, engine and files not accessible; do not perform in the shared business |

## Checked when this was made

- Boat package totals, separate providers, all dates and HIN consistency checked locally. Three real PDFs, retained HIN photo and first-page renders visually inspected. No app/DB modifications or sign-ins.
- Manifest checked: 17 makers, 180 models, **none a boat**. Boat and Mercury brand presence outside that manifest is not asserted or queried.

## Known rough edges (not part of the answer key)

- **Verify custom maker/model entry**; if unavailable, seed Tracker / Pro Team 175 TXW in Vehicles before running. No seed changes in this deliverable.
- Scenario 61 says hours/kilometres wording is unit substitution; do not assume a boat-specific policy reader or automatic HIN/photo recognition. Decimal 0.8-hour reading and a part's fractional install reading are **verify**; if unsupported, leave reading blank rather than invent a rounded value. Warranty is date-only and remains runnable.
- **Verify** how a bundled engine's allocated value is represented without inflating purchase totals. Use the package agreement as the single cash-outlay truth; a $9,000 part item is allocation metadata, not a second bill. Automatic purchase-line-to-part linking is not documented.
- **Verify** reader multi-component/source wording and that "no operating-hour limit" is retained as quote/date-only rather than a bogus numeric mileage cap. All coverage end dates are explicit. Reader misses are Partial and may be corrected against this key.
