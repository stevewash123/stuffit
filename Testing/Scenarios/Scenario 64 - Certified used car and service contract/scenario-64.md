# Scenario 64: Dealer-certified used SUV with a certificate and purchased service contract (happy path)

**Accounts:** Test2 (Bob); Test1 (Alice) only for optional isolation check.
**Preconditions:** Bob's **personal account** selected, not shared P34-Alice Repairs. Clock offset **0**, app date **2026-11-08** (America/New_York). Toyota / RAV4 seeded; vehicle coverage start and Protection plans features deployed (pushes 25, 32, 33, 37). Reader on or record **reader off**. Preserve existing fixtures; use unique name. All dealer/CPO/service-contract terms are fictional specimens, not Toyota's current certified program.
**Time:** 40 min
**Built per:** Full-document Scenario 1; Scenario 61; push 25 certified/dealer-added independent start; pushes 32 and 33 Protection plans.
**Why this plan:** the normal used-car folder separates an included dealer-certified warranty from an optional paid contract. These start at certified delivery, not the original factory in-service date, and the plan premium is not the vehicle price.

## The purchase (answer key)

| Fact | Value |
|---|---|
| Item / kind / category | **UAT P38 S64 Certified RAV4** / Car (SUV) / Vehicles |
| Make / model / year / trim | **Toyota / RAV4 / 2024 / XLE** (seeded model) |
| Seller | **UAT Harbor Auto Toyota**, 200 Example Auto Drive, Testville, ME 00000; fictional dealer |
| Condition / ownership / paid by | Used / Bought / Cash or check |
| Purchase / original first in service | **2026-11-06 / 2024-05-15** |
| VIN / delivery odometer | `1UATW1FV0R0000064` (synthetic) / **28,400 miles on 2026-11-06** |
| Vehicle / separate plan / tax / fees / total | **$26,000 / $1,800 / $1,668 / $232 / $29,700**. Tax = 6% of $27,800. Vehicle price field $26,000 |
| Included CPO provider / origin | **UAT CertifiedCare / Certified or dealer-added**; included at no extra price, **not** Toyota factory coverage |
| CPO comprehensive | Whole vehicle, parts/labor, **2026-11-06 to 2027-11-06**, **12,000 miles from 28,400**, absolute end **40,400 miles**, $0 deductible |
| CPO powertrain | Engine/transmission/drive axle, parts/labor, **2026-11-06 to 2028-11-06**, **24,000 miles from 28,400**, absolute end **52,400 miles**, $0 deductible |
| Purchased protection plan | Provider **UAT RoadGuard Administration**, name **Select mechanical breakdown**, contract **UAT-P38-064-PLAN**, paid **$1,800 one time**; no monthly amount or renewal |
| Plan order / own start / end | **2026-11-06 / 2026-11-06 / 2029-11-06** (36 months). Start answer **Same day as the purchase**. Active; no waiting period |
| Plan scope / fee / mileage | Mechanical/electrical breakdown, parts/labor; **$100 per covered repair visit**. Contract limit **36,000 additional miles** from 28,400 = **64,400 total**; keep in plan terms even if structured plan-mileage fields are unavailable |
| Plan claims | `https://roadguard.example/claims`, (202) 555-0165; fictional, do not call or submit |
| Registration / factory term / returns | No pending enrollment deadline. No original factory warranty term supplied, no invented factory term or return window |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 1 | `01-buyers-order-toyota-rav4-cpo.pdf` | Dealer order with the separate $1,800 contract line | Add > Vehicle / vehicle papers |
| 2 | `02-cpo-warranty-certificate.pdf` | Two-page included certified warranty, separate comprehensive and powertrain clocks | Vehicle papers; reference for **manual certified/dealer-added** coverage |
| 3 | `03-roadguard-service-contract.pdf` | Two-page paid service contract, declaration and terms | Saved vehicle > Read it / Add-on protection, linked to that vehicle |

### Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test2 | Confirm personal account and clock 0. Add > Vehicle; use key and attach file 1 | One 2024 Toyota RAV4, Used, Bought, original first service 2024-05-15, delivery reading 28,400 on 2026-11-06; price **$26,000**, not $27,800 or $29,700. No lease |
| 2 | Test2 | Read the order, inspect suggestions | Target make/model, vehicle line, delivery date, seller, separate protection-plan line and $1,800 premium. Preserve $29,700 gross total in paper, not as vehicle price. Record/correct missed separation; no second RAV4 or $1,800 retail vehicle. Vehicle VIN/year/in-service/reading remain user entry |
| 3 | Test2 | Attach certificate 2. Reference it while adding coverage as **Certified or dealer-added**; create comprehensive and powertrain terms with the explicit starts and start odometer | Two certified terms per key. Their start is **2026-11-06 at 28,400**, not original factory date; end odometers **40,400 / 52,400**, never 12,000 / 24,000 lifetime miles. Provider UAT CertifiedCare, no paid plan created for this included certificate |
| 4 | Test2 | If trying Read it on certificate, inspect but do not accept an incorrect factory classification; record what was offered | Push 25 says the reader **does not recognize certified coverage**. Manual certified/dealer-added entry is the supported happy path, not an extraction failure. Attach the paper as evidence; source remains **entered by the person** for these manual terms, not falsely Extracted from receipts |
| 5 | Test2 | Attach and Read it on contract 3 from the vehicle. Accept Add protection plan, or enter its exact details on the linked plan form if not recognized | Separate purchased plan, provider UAT RoadGuard Administration, Select mechanical breakdown, contract number, price $1,800, $100 service fee, 36-month term, own start 2026-11-06 and end 2029-11-06. Start question answered, never silently assumed. Keep mileage clause in terms; see verify below |
| 6 | Test2 | If the receipt already made a plan draft, complete that draft rather than creating another. Reload vehicle and Protection plans | **One** RoadGuard plan linked to this RAV4, Active in Add-on protection, counted from its own start. Terms explain mechanical/electrical breakdown and primary warranty first. No extra plan for included CPO; no duplicate plan from receipt and contract |
| 7 | Test2 | Check sources, coverage and mileage summaries | Certified terms stay certified/manual and retained alongside the paid plan. Extracted contract terms quote/link their paper; record **Extracted from receipts** if shown for reader-derived content. Contract is not relabelled a Toyota factory warranty. CPO mileage remaining at the dated reading: 12,000 / 24,000; no pace with just one reading |
| 8 | Test2 | Inspect To do / Notifications at clock 0 without jobs or clock changes | No unfinished first-service task, waiting/enrollment task or lease task justified by these papers. No expiration reminder due now. Earliest dated protection ends 2027-11-06; configured reminder lead time **verify**, no future job run here |
| 9 | Test1 | Optional isolation from Alice's personal account | Bob's vehicle/contract not accessible through its direct address; no shared-business isolation claim |

## Checked when this was made

- Locally created/visually reviewed PDFs with declaration tables, terms and signature lines; PDF text extraction succeeded. Receipt sums and additional-vs-absolute mileage calculations checked. No upload or live reader test performed.

## Known rough edges (not part of the answer key)

- **Certified terms are intentionally entered by hand**, per push 25; this is normal supported setup with real paperwork, not an edge-case test.
- **Verify** whether a purchased Protection plan has structured mileage support. Release notes establish structured miles for coverages, not the plan object. Do not silently promise mileage tracking for RoadGuard; retain the exact 64,400 clause as text/evidence if no field exists and record the limitation. Do not create a duplicate maker warranty to force plan miles.
- **Verify** extraction of receipt plan line, contract classification, source wording and line-price/gross-total choice. Reader misses are Partial with raw suggestions, not a claimed live pass. Expected final saved data is the key after review/correction.
- The certificate is a realistic **dealer-certified** variation; it is not presented as the current Toyota manufacturer CPO program. No factory term is inferred from the 2024 model year.
