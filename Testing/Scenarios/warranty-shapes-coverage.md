# Warranty shapes: what is tested, and what is not

Built 2026-11-04 from `Testing/SampleData/warranties` (README, index.csv), `INVENTORY.md`, the E3 stories, `reference-data/*.json` and Scenarios 1 to 57. "Full scenario" means a numbered scenario here with an answer key and expected coverage. Fixture-only means a sample document exists and the reader is checked (T2 matrix) but no scenario checks what the item page shows.

Status key: ✅ full scenario, runnable now. 🆕 full scenario written 2026-11-04 (not yet run). 🕓 scenario written, DEFERRED until the story is built. 📄 fixture only. ❌ nothing.

## 1. The shapes

### A. How the term is built
| # | Shape | Example | Status |
|---|---|---|---|
| 1 | One flat term | Brightwave 12 mo, Northlink 24 mo | ✅ 1, 7, 13 |
| 2 | Per-line policy under one maker | Milwaukee heated gear 12 / levels 36 / generators 24 | ✅ 15 to 17; 🆕 53 Part C (ambiguous item) |
| 3 | Policy limited to listed models and a purchase window | Samsung 2-year addendum, 65 models, 2022-10-01 to 2023-09-30 | 🆕 53 Part A |
| 4 | Product tree: line and size, nearest wins | Penn Battle IV sizes, Fierce lines | 🆕 53 Part B |
| 5 | Components with separate parts and labor clocks | Fridge 1y / sealed system 5y parts / compressor 10y | 🆕 52 |
| 6 | Full term plus longer limited term, per product, in one document | Hearthstone kitchen suite | 🆕 56 Part D (known gap) |
| 7 | Main product plus accessories on a shorter term | Tool 5y, battery 3y | 🆕 56 Part C |
| 8 | Lifetime (no end date, whose lifetime, transfer) | Penn reel | 🆕 55 (build state of S3.1.8 unknown) |
| 9 | Price tiers inside a plan type | Plan price by item price | ❌ not built |
| 10 | Tiered or limited headline with proration | Emberly "10 years limited" | 🆕 52 step 12 (proration kept as text only) |

### B. When the clock starts
| # | Shape | Status |
|---|---|---|
| 11 | Purchase date | ✅ 1 |
| 12 | Delivery date, DD/MM/YYYY | 🆕 54 Part D; ✅ 10 (delivered email) |
| 13 | Installation date, app asks | 🆕 54 Part A |
| 14 | Registration-dependent term | 🆕 54 Part B |
| 15 | Manufacture date from the serial | 🆕 54 Part C (not built; tests the safe failure) |
| 16 | Installation or purchase + 6 months, whichever first | 🆕 56 Part D |
| 17 | Waiting period, then recurring until cancelled | 🕓 47 |
| 18 | "From signing" vs "from when the maker warranty ends" | 🆕 57 Part C |

### C. Limits
| # | Shape | Status |
|---|---|---|
| 19 | Dollar limit per covered line | 🕓 47, 50 |
| 20 | Age limit on the covered item | 🕓 50 |
| 21 | Claim-count cap, deductible by loss type | 🕓 49; 🆕 57 step 21 ("three paid claims") |
| 22 | Claim limited to the item's purchase price | 🆕 57 step 20 |
| 23 | Service fee, flat or range | ✅ 31 (flat); 🕓 47 (range) |
| 24 | Mileage or usage | ✅ 41 step 12 |
| 25 | Card benefit with caps and eligibility | ✅ 1, 9, 15 to 17, 21; 🆕 57 Part B (the card guide itself) |

### D. Conditions
| # | Shape | Status |
|---|---|---|
| 26 | Residential vs commercial, wear items, voiding conditions, authorized dealer | 🆕 56 Part A |
| 27 | Used item, then "as is" | 🆕 56 Part B |
| 28 | Original purchaser only, ends on sale or gift | 🆕 55, 56 Part A; 🕓 46 |
| 29 | Transferable once for a fee | 🆕 57 step 22 |

### E. Who promises it
| # | Shape | Status |
|---|---|---|
| 30 | Store plan on a receipt, with its own document | ✅ 8, 41, 43, 44 |
| 31 | Third-party plan covering several items | ✅ 31; 🆕 57 Part C (certificate) |
| 32 | Monthly home warranty | 🕓 47 |
| 33 | Phone insurance | 🕓 49 |
| 34 | Warranty only stated on the receipt | ✅ 41 Part B |
| 35 | Return policy plus short store warranty | ✅ 1 to 5 (return); 🆕 57 Part A (the document) |
| 36 | Card benefit | see 25 |

## 2. What is still not covered, rated

**Rating:** Critical = the app could show a wrong date or a wrong "covered" that costs the person money or a claim, and nothing tests it. Medium = a real shape, a plausible wrong answer, no test. Minor = rare, or low harm if wrong. Warning = a test exists but a pass could mislead (deferred, expected to fail, or built on assumptions), so it is not real assurance.

### Critical
| # | What is missing | Why it matters | Cost to close |
|---|---|---|---|
| X1 | **Date arithmetic edges.** Month-end (Aug 31 + 6 months), leap day (Feb 29 + 12 months), term end day inclusive or exclusive, midnight and time zone at the boundary | An end date wrong by a day or a month, on every item, silently. My search of the test projects was inconclusive, so confirm whether unit tests cover this before writing a scenario | Low: 6 receipts on boundary dates, or a unit test |
| X2 | **A document that states no term.** "Limited warranty" with no period, a card that says only "see our website", terms on the back page that is not photographed | The principle in Scenario 41 is "never say covered only because a phrase was printed". It is tested for receipts (step 16) and never for warranty documents | Low: one new fixture with no period |

### Medium
| # | What is missing | Why |
|---|---|---|
| X3 | A **document vs the shared policy** disagree (document says 90 days, verified policy says 12 months, or the reverse). T2 B3 says the document "replaces" the standard coverage; no run checks it never lowers a verified longer term from a bad reading | Silent downgrade or upgrade |
| X4 | **"Something broke" for a component**, not the whole item (compressor failure in year 3) | Scenario 52 checks the lines; nothing checks the claim wizard picks the right one (F5.1, F5.4) |
| X5 | **Refurbished and open-box** with its own shorter maker warranty (Sears Outlet, receipt 35) | Scenario 41 only checks nothing is invented; the correct shorter term is not tested |
| X6 | **Plan seller is not the administrator** (store takes the money, another company handles claims; Geek Squad under Best Buy) | Claim phone for the wrong company. S3.4.5 written, 41 notes it not built |
| X7 | **Prorated coverage** (after year 5 the owner pays a share; tire road hazard by tread depth) | Shown as full coverage when it is a share |
| X8 | **Warranty held by someone else**: gift, inherited, secondhand, receipt addressed to Pat Sample, warranty for original purchaser only. Household sharing (F1.3) decides who is "original purchaser" | Wrong person assumed able to claim. Check Scenarios 26 and 46 first |
| X9 | **Document that is a web page or an email**, not a file (README "not yet covered") | Common in real life; today the person screenshots it |
| X10 | **Scanned multi-page PDF with a signature page**, terms across pages | The reader may read page 1 only |
| X11 | **Recall notice** mistaken for a warranty, or a recall on a covered item (F6.5) | Different action, different deadline |
| X12 | **Warranty changed after purchase** (maker updates terms; the person keeps the version they bought). S3.2.1 versioned policies | Scenarios 22, 23, 40 touch shared data but I did not verify one that changes a term for an existing item |

### Minor
| # | What is missing |
|---|---|
| X13 | **Non-English-only** document |
| X14 | **Territory limits** ("48 contiguous states", "valid in the EU and UK") beyond what 54 Part D reads |
| X15 | **Lease or subscription** with a service guarantee |
| X16 | **Bundle** (a combo kit with a battery from another brand) |
| X17 | **Price tiers** in a plan type (not built) |
| X18 | **State-specific plan versions** (S3.4.9; 🕓 47 step 14) |
| X19 | **Exclusive remedy wording** ("repair or replace at our option") |

### Warning (a pass or a skip here is not assurance)
| # | Warning |
|---|---|
| W1 | **Deferred scenarios 45 to 50** cover waiting period, limits, claim caps, phone and home plans, and plan lifecycle. They cannot be run until their stories are built. Until then the waiting-period "covered but not yet" risk and the limits shown "with a source" are unverified |
| W2 | **New scenarios contain steps expected to fail or be Not built**: 54 Part C (serial), 55 (S3.1.8 build state unknown), 56 Part D and 57 Part C (T2 B12 known gap, one document with several items). A run with those steps "Not built" is not a clean run |
| W3 | **T2 "known gap" labels hide defects**: "16 reads 5y, not 12y" (Fujitsu 12-year compressor) is recorded as a known gap, not tracked in a scenario. If it stays unfixed, 52 would not catch it (Fujitsu is not in 52) |
| W4 | **Fixtures differ from the real data**: `standard-appliance-limited-warranty.pdf` (1 / 5 / 10, fictional Samsung wording) and `samsung.json` (12 / 24 / 60 / 120, from the real 2022 document) describe the same brand with different tiers. Scenario 52 uses both on different items; a tester may think one is wrong |
| W5 | **Real model, variable readings.** 52, 54 to 57 reader steps run on the real model; the same document can read differently on different days. Partial vs Fail needs the tester's judgment each time |
| W6 | **No runner.** Scenarios 15 to 21 have scripts (`run_scenarios.py`, `run_shared.py`); 52 to 57 are manual browser plans. They will not catch a regression unless someone runs them |
| W7 | **Hard-coded dates.** Expected end dates are fixed for purchase dates in the scenario and for the app date 2026-11-04. Steps that move the clock must reset it to offset 0 afterwards |
| W8 | **Synthetic documents only.** Every fixture is invented text. Real maker documents (the real Samsung PDF, real Geek Squad contracts) are laid out differently and will read differently; S3.2.8 used one real document |
