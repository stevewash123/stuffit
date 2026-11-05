# UAT retest: build c6dc314, Scenario 55 (Lifetime and who can use it)
Build: API c6dc314 (Staging, started 11:41 PM ET Nov 4). UI Last-Modified 11:39 PM ET. Mode: Full-only. Tested ~12:09–12:17 AM ET Nov 5.
Push notes: CHANGES-push-16-lifetime-warranties-2026-11-05.md. Scenarios 52–54, 56, 57 not in this push.
Accounts: Alice only (DB Stager scenario reset). Bob (tester2) and Carol (tester3) do not exist → step 17 Not checked. Alice's Stripe fields were wiped by the reset (status none).

## Headline
The reader correctly finds a lifetime term with no end date and no guessed years, and keeps it beside the shared Penn 1-year warranty with an explanation. Home does not treat the lifetime plan as ending soon (checked with Alice's dates staged back 30 years). Missing on this build: the "Lifetime, can end" badge and plain-words line, the end-coverage reason picker, and populated lifetime columns in the export. Claim guidance only loosely mentions the lifetime plan.

## Staging note
The API clock is global and DB Stager cannot set a +30-year offset, so for step 7 Alice's purchase/coverage/plan dates were shifted back 30 years (purchase 1996-06-01; maker warranty ended 1997-06-01; lifetime still no end). Global clock stayed at offset 0. Todo due dates were left current. Noted under Needs CC that a set-offset endpoint would avoid this.

## Scenario 55
| # | Result | Notes |
|---|---|---|
| 1 | Pass | Item "UAT Penn Reel" saved (Penn, BTLIII4000, Jun 1 2026 → later staged to 1996, $119). PDF on Add a purchase attached as Receipt with no warranty suggestion; reader suggestion came via Add-on protection → "I have the paperwork". Reader quotes: lifetime of the product; not transferable; proof of purchase required; exclusions include saltwater corrosion and lost/stolen |
| 2 | Pass | Term "lifetime of the product", End date in "document did not say", form Ends empty with "Leave empty if it has no fixed end." No years guessed. Transfer false |
| 3 | **Partial** | Plan shows "No fixed end date" / "Jun 1, … no fixed end". Missing on item/plan: badge **"Lifetime, can end"**, the plain-words lifetime line, and a **"What could end it"** list. Item header still driven by the 1-year plan ("Until Jun 1, 2027" before the date shift). Known: list/Home badge still "Active" for lifetime-only |
| 4 | Pass | Exclusions on the plan page: saltwater corrosion from failure to rinse; line; lost or stolen reels |
| 5 | Partial | Reader/form: "Proof of purchase is required." Does not demand original paper. Item page has no "Asks for: proof of purchase" line. **List of what WarrantyCat holds as proof: Not built** (per notes) |
| 6 | Pass | Maker 1-year + lifetime plan both shown with sources and explanation: "The maker's warranty runs to …. The PENN Fishing Tackle plan runs … with no fixed end." |
| 7 | Pass | After date staging: Home "0 Ending in 30/60 days"; lifetime not ending soon; 1 Protection plan running. Item: lifetime "No fixed end date", maker "Ended Jun 1, 1997" |
| 8 | Not built | Yearly check-in (per notes) |
| 9 | **Fail** | Cancel/re-open work, but no reason picker ("maker dropped the model" etc.). Only "Cancel it now" / "It already ended" plus optional free-text for *how* you cancelled. After cancel: "Cancelled Nov 5, 2026", item "Expired"/"Coverage ended", history kept. Re-open restores "No fixed end date" |
| 10 | Not built | Given away / sold (per notes) |
| 11 | Not built | Sold + Undo (per notes) |
| 12 | Not built | Dishwasher tub component lifetime (per notes) |
| 13 | Not checked | Depends on step 12 |
| 14 | Pass | No yearly cost, years remaining, days left, or end-date reminder on the lifetime line |
| 15 | Partial | Claim flow ("Start a refund or claim"): protection plan card says it "has no end date we know of" but never says Lifetime / original purchaser / not transferable; lifetime exclusions and "proof of purchase required" not shown. Correct disclaimer: "This is what your document says. The company decides in practice." No promise of acceptance |
| 16 | **Fail** | Export `warrantycat-export-2026-11-05.zip`. `coverage.csv` has columns lifetime, lifetime_scope, transferability, proof_asked, entered_by_you, ended_reason, ended_on — but all blank on the lifetime row. Only the word "Lifetime" survives inside plan name/terms text. Not exported as "Lifetime" with scope and transfer |
| 17 | Not checked | Bob's account does not exist |

## Needs CC
- Item/plan UI for lifetime: "Lifetime, can end" badge, plain-words line, "What could end it" list (step 3).
- End-coverage reason picker (given away/sold, maker dropped the model, worn out, owner died, other) — step 9.
- Populate lifetime / lifetime_scope / transferability / proof_asked on export (step 16).
- Claim guidance should surface the lifetime term, its exclusions, and proof asked (step 15).
- Clock: no set-offset endpoint for DB Stager; step 7 used a per-account date shift instead.
- Recreate Bob (and Carol/Ops if still missing) for isolation steps.

## Not reported (decided)
- "You entered or corrected" source wording after a correction.
- Monthly/Yearly placeholders, no Founders.

**Totals (17 rows):** 6 Pass, 3 Partial, 2 Fail, 4 Not built, 2 Not checked.
