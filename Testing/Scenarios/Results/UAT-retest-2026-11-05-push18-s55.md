# UAT retest: push 18 lifetime reader fix + Scenario 55 redo
Build: API `dca5ccb` (started 2026-11-05T12:11:07Z). UI Last-Modified still Thu, 05 Nov 2026 10:50:29 UTC (API-only push). Mode: Full-only. Tested ~7:12–7:23 AM ET Nov 5.
Notes: `CHANGES-push-18-lifetime-reader-fix-2026-11-05.md`. Alice session (Welcome, QA / Q1). Leftover Penn item from push 17 redo deleted before the run.

## Headline
Push 18 fixed the lifetime extraction on the **item paperwork** door. Scenario 55 steps **2, 3, 5, 9, 13, 15, 16 all Pass** that way. **Add a purchase** still does not show "Manufacturer's warranty found" for `standard-lifetime-limited-reel.pdf` (catalog 1-year only). Registration/transfer "also try" **Fail**: `edge-registration-required.pdf` got "no clear length or end date" and never offered coverage.

## Doors
| Door | Result | Notes |
|---|---|---|
| 1. Add a purchase + lifetime PDF | **Fail** | Attached as "Warranty or terms (PDF)". Toast filled brand Penn / model BTLIII4000. **No "Manufacturer's warranty found".** Only catalog "Penn warranty · Manufacturer · 1 year · Confirmed" plus unconfirmed model variants. No "lifetime" text on the form. Did not save. |
| 2. Item paperwork (Edit → Choose files) | **Pass** | Carrier item saved with catalog 1-year first (no PDF on create). PDF uploaded as "Terms". Modal: "Add this warranty? … Lifetime maker's warranty from Jun 1, 2026, with no end date." After Add: "Applied to this item: Lifetime, from 2026-06-01, with no end date. It replaces the warranty we had suggested." |

## Scenario 55 redo steps
| # | Result | Notes |
|---|---|---|
| 2 | **Pass** | "Lifetime of the product. Original purchaser only. Not transferable. The maker decides when it has worn out." Card: Jun 1, 2026, no end date. Replaced the 1-year. |
| 3 | **Pass** | Badge "Lifetime, can end" (tooltip: "A lifetime warranty has no end date, but it can still end"). "What could end it" lists give away/sell, maker worn-out/refuse claim, maker drops model / goes out of business. |
| 5 | **Pass** | "Asks for: proof of purchase. Nothing says the original paper is required." Document quote: "Proof of purchase is required". |
| 9 | **Pass** | End this coverage → "The maker dropped the model or went out of business". No date picker (date auto). Result: "Ended Nov 5, 2026: …", range Jun 1, 2026 to Nov 4, 2026. Re-open restored "Lifetime, can end" with no end date. |
| 13 | **Pass** | Dishwasher HS-D24: reader did not extract tub lifetime (step 12 Not built — recorded only). Hand-added Manufacturer / HEARTHSTONE, lifetime, whose = original purchaser, transfer = No original purchaser only. Item: "You entered or corrected: that it is a lifetime warranty, whose lifetime, whether it can be passed on." |
| 15 | **Pass** | "Something broke" / It does not work. Best option / Applies. Lifetime + exclusions (saltwater / lost-stolen) + proof. "The company decides in practice" / "no one can promise a request will be approved." No repair promise. |
| 16 | **Pass** | Settings → Privacy & data → Prepare my download. coverage.csv: lifetime=Lifetime, lifetime_scope=Product, transferability=NotTransferable, proof_asked=anyProof, end_date empty, source=Extracted. |

Item (lifetime): https://stuffit-ui.onrender.com/items/01a1aba4-46ee-7ff3-b970-0fd8ea7d3807
Dishwasher (step 13): https://stuffit-ui.onrender.com/items/01a1aba8-cfed-7ef5-9768-b9e49b534fbd

## Also try: registration / transfer notes
| Check | Result | Notes |
|---|---|---|
| `edge-registration-required.pdf` (Trailblaze TB-350: register in 30 days to extend 90d → 3yr) | **Fail** | Create: brand filled as new local TRAILBLAZE; "Nothing found yet." Door 2: "The document does not give one clear length or end date. Add the coverage yourself." No manufacturer offer. No registration / 30-day / 90-vs-3yr / transfer text anywhere (only generic placeholder "For example: register the warranty"). Brand "not in our shared list yet" — may be a factor. Item: https://stuffit-ui.onrender.com/items/01a1aba7-97ab-71d7-8ca2-b59478affadd |

## Decided / not built (not reported as fails)
- Items list/Home "Active" for lifetime-only — decided, do not report.
- Yearly check-in, given away/sold, proof list, lifetime on one component — Not built.

## Needs CC
- **Add a purchase** still never surfaces "Manufacturer's warranty found" / lifetime for `standard-lifetime-limited-reel.pdf` on `dca5ccb` (item paperwork path works).
- **Registration-required PDF** still "no clear length or end date"; registration notes unverifiable. May need a shared-list brand sample or a further reader fix for conditional term length (90 days vs 3 years after register).

## State left
Alice signed in with three items: lifetime Penn (re-opened), Trailblaze (no coverage), Dishwasher (hand lifetime). Export zip on box: `/home/box/Downloads/warrantycat-export-2026-11-05 (2).zip`.

**Totals:** Door 1 Fail; door 2 Pass; S55 steps 2/3/5/9/13/15/16 Pass (7); registration also-try Fail.
