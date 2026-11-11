# UAT retest — Push 60: plan offers, type lines, replacements, and push 59 fixes (Nov 10, 2026)

- **Build:** API f16f620, started 6:11:19 PM ET. UI ~6:10 PM ET. Staging. API and UI.
- **Migrations (verified read-only before the run, Neon project `square-tree-53585492`, db `stuffit`):** `__EFMigrationsHistory` has `20261110222447_PlanOfferDismissals` and `20261110224129_PlanTypeLines` (both product_version `9.0.22`). Table `plan_offer_dismissals`; `plan_types.lines_json`.
- **Source:** CHANGES-push-60-plan-offers-and-type-lines.md (SHA256 `ca7801d5aea5bb6b8478c81e0939b2dc5444095163b2162508f01eba88e38c6e`); TESTPLAN.md; p60-A-notes.md, p60-B-notes.md, p60-C-notes.md; export `/workspace/uat/push60/export/warrantycat-export-2026-11-10.zip`.
- **Accounts:** P34 Self (vault 3550464); Ops (vault 2460773, TOTP) for the type editor; Bob (vault 2453777) for the other-account offer check. No Alice or Bob reset. P34 Self saw **"A new version of WarrantyCat is ready"** and clicked Reload, then a hard reload. Later sessions had no banner; a hard reload was still done. Clock Offset 0 (never moved; confirmed after the run).
- **Fixtures:** none new. No QA fixture files were made for the share.
- **Not reported:** items marked **Not built yet** (request attachments, claim log / Money recovered, denial wizard, phone-insurance cost view, three-layer explanation, reader-filled limits, seeded providers, receipt-to-type matching, person-added plan types).

## Results

| Result | Count |
|---|---|
| Pass | 15 |
| Partial | 1 |
| Fail | 0 |
| Inconclusive | 0 |

The Partial is **Low, Needs CC** (a typeless plan shows no "fill lines" message; the button is simply missing). Plus **Lows** on a stale kind-of-loss fee, End-this-plan with today's date doing nothing visible, and typography on the decision panel (middle dots vs the notes' commas). The unknown-kind refusal is **N/A** in the UI (kind is a three-option select) and is not counted as a row. "Cost so far About $198.00" on the $99-a-year Decision Care plan is an **observation** only (see below). Within the same date, export row order is not entry order; that is **not** a miss of "ordered by plan, then date."

## Per-step results

| # | Check | Result |
|---|---|---|
| 60-year | Plan-year fee and payout figures, plus an all-years line | **Pass** |
| 60-before | A request dated before the plan started is refused | **Pass** |
| 60-lineitem | The list shows line · item | **Pass** |
| 60-comma | No stray space before a comma | **Pass** |
| 60-export | Past-cap column; ordered by plan, then date | **Pass** |
| 60-offer | "Add this to your plan?" on a matching new item | **Pass** |
| 60-no | No thanks is remembered | **Pass** |
| 60-yes | Yes attaches the item; age from the purchase date | **Pass** |
| 60-never | Never offered for excluded / already-linked / ended / already-on / other account | **Pass** |
| 60-tv | Replacement carries the TV line; undo reverts it | **Pass** |
| 60-phone | Phone plan IMEI follows the replacement; undo restores it | **Pass** |
| 60-typeed | Operator line-by-line editor; repeated name refused; blank rows dropped | **Pass** (unknown kind **N/A**) |
| 60-fill | Fill in the lines from the plan type | **Pass** |
| 60-fillmsg | A typeless plan, or a type with no lines, shows a message instead of filling | **Partial** (Low) |
| 60-decision | Plan decision panel Service requests line | **Pass** |
| 60-loss | Kind of loss fills the fee; a range shows | **Pass** (Low: fee stays at 29 when the kind changes) |

### 0. Push 59 fixes

**60-year Pass.** Home Care **"Asking for service"** (`s60-A-year-summary.png`):

> 4 requests this plan year · fees you paid $225.00 this plan year · the company paid $230.00 this plan year · all years together: fees $225.00, the company paid $730.00

The leftover Oct 15 $500 no longer inflates this year's figure. Decision Care later confirmed the same split: this-year **$420.00** vs all-years **$520.00** after an older-year $100 request, while the decision panel stayed all-time on purpose (see 60-decision).

**60-lineitem Pass.** The Covered Dishwasher row is **"Nov 10, 2026 · Dishwasher · UAT P58 Dishwasher · Jordan Kim, 555-010-5903 · you paid $75.00 · the company paid $180.00"** (`s60-A-line-item.png`).

**60-comma Pass.** **"Pat Lee, 555-010-5902"** and **"limit $5,000.00, $50.00 of it used this plan year"** (Dishwasher used-limit the same way, no space before the comma) (`s60-A-commas.png`).

**60-before Pass.** A new Home Care request dated **2026-10-15** was refused with **"That is before the plan started."** Cancelled; the existing Earlier-year pump row remains (`s60-A-before-start.png`).

**60-export Pass.** `plan_service_requests.csv` is in the zip and listed in README.txt. Header includes **"past the claim cap"**. Device Care: First and Second cracked screen = **no**; Third claim past cap = **yes**. Rows are grouped by plan name, then date (Device Care, then Home Care, then Decision Care). Within the same date they are not in entry order; the notes only require plan, then date.

### 1. Add this to your plan?

**60-offer / 60-no / 60-yes Pass.** A **Refrigerator** line (no item, limit $2,000) was added to Home Care. **UAT P60 Fridge No** showed:

> Add this to your plan?
> Your plan UAT P58 Home Care lists a Refrigerator. Is this the one? Your contract still decides whether it is covered.
> Yes, add it to the plan / No thanks

(`s60-B-offer-no-item.png`). **No thanks** hid the card; it did not return after a hard reload (`s60-B-no-remembered.png`). Read-only SQL: `plan_offer_dismissals` has one row (`01a1c7d5-898a-762d-b921-c2ea37b9c370`) for that item and Home Care, created 6:40:22 PM ET Nov 10.

**UAT P60 Samsung refrigerator** (bought Jun 1, 2020): **Yes, add it to the plan** toasted **"Added to UAT P58 Home Care."** The line reads **"Refrigerator Appliance / about 6 years old (from your purchase date) · limit $2,000.00 · UAT P60 Samsung refrigerator"** (`s60-B-yes-attached.png`).

**60-never Pass.** No offer on **UAT P60 Ice maker** (excluded line), **UAT P60 Extra fridge** and **UAT P60 Extra dishwasher** (lines already have items), **UAT P58 Dishwasher** (already on the plan), **UAT P60 Washer** after **UAT P60 Ended Care** was cancelled on Nov 10, 2026, or **UAT P60 Bob Refrigerator** on Bob's account (`s60-B-never-*.png`, `s60-C-bob-never.png`).

**Low, Needs CC (End this plan):** on Ended Care, **"End this plan"** with date **2026-11-10** did nothing visible (the plan still said **"No fixed end date"**). **"Cancel this plan > Cancel it now"** worked: **"Cancelled Nov 10, 2026, refund not recorded yet"**. The never-offered check still ran via Cancel.

### 2. Replacement

**60-tv Pass.** **UAT P60 TV Care** line was tied to **UAT P60 Old TV** (**"about 6 years old (from your purchase date)"**). Replace used the **"Replaced by the plan"** dialog (Carry on / End the plan / Start a new term, none pre-ticked, Save disabled until one is chosen). **Carry on** to **UAT P60 New TV**: the line showed **"about 0 years old (from your purchase date) · UAT P60 New TV"**. **Undo** restored the Old TV line and age; the New TV item became **"Not found."** (`s60-B-tv-before.png`, `s60-B-tv-carried.png`, `s60-B-tv-undo.png`).

**60-phone Pass.** Before: IMEI **UAT-P59-SERIAL-001**, cap 2, deductibles Cracked screen $29.00 / Other damage $29-$199 / Stolen $199.00 (`s60-B-phone-before.png`). Replace the iPhone with **UAT P60 New iPhone**, serial **UAT-P60-NEW-IMEI**, Carry on: Device Care IMEI became **UAT-P60-NEW-IMEI**; cap and deductibles unchanged; it covered the new phone (`s60-B-phone-carried.png`). **Undo** restored IMEI **UAT-P59-SERIAL-001** and coverage of **UAT P58 iPhone 16**; the new iPhone is **"Not found."** (`s60-B-phone-undo.png`). Read-only SQL after the run: `device_identifier` = **UAT-P59-SERIAL-001**, `claim_cap` = 2, deductibles still present.

### 3. Plan types and fill

**60-typeed Pass** (unknown kind **N/A**). Ops added **UAT P60 Care Type** sold by UAT P54 Shared Care Co, confirmed at `https://example.com/uat-p60-care-type`. The editor is **"What this plan covers, line by line"**. A fourth row named refrigerator was refused: **"Each line can be listed once."** Kind is a three-option select (Appliance / System / Add-on), so an unknown kind cannot be entered in the UI. A blank fourth row was dropped on save; Change showed only the three good rows (`s60-C-type-editor.png`, `s60-C-type-refused.png`). Read-only SQL `lines_json` (type `01a1c7dd-bef3-7b70-a5f3-f5e2c8ba69d8`): Refrigerator appliance $2,000, "Up to $2,000 per claim", age limit 15; Heating system $5,000; Water filter add-on $200.

**60-fill Pass.** **UAT P60 Filled plan** (type UAT P60 Care Type) showed **"Fill in the lines from UAT P60 Care Type"** (`s60-C-fill-button.png`). A hand-added **"refrigerator"** line at $999 was left untouched (case-insensitive match). Fill added Heating system $5,000 and Water filter $200. The button then went away. Water filter was marked **"My contract does not cover this one"** and shows **"Left out of your contract"** (`s60-C-filled.png`).

**60-fillmsg Partial (Low, Needs CC).** The notes say: **"A plan with no plan type, or whose type lists no lines, shows the message instead of filling."** On typeless Home Care the fill button is simply **absent**; the card has only **Add a line**. No message is shown (`s60-C-fill-message.png`). Nothing was wrongly filled. A type that lists no lines was not separately tested.

### 4. Decision panel

**60-decision Pass.** **UAT P60 Decision Care** (American Home Shield, Nov 10, 2025 to Nov 20, 2026, $99 a year) showed the decision panel with **no** Service requests line while it had no requests (`s60-C-decision-empty.png`). After two this-year requests (fees $150, company $420):

> Service requests
> 2 requests · fees you paid $150.00 · the company paid $420.00

(`s60-C-decision-requests.png`). After a **2025-12-01** request with company paid $100, the panel became **"3 requests · fees you paid $150.00 · the company paid $520.00"** (all-time), while Asking for service kept **"2 requests this plan year"** / company **$420.00 this plan year** / all years together company **$520.00** (`s60-C-decision-alltime.png`). That matches **"the plan decision panel's Service requests line stays all-time on purpose."** The notes' example uses commas (**"2 requests, fees you paid $150.00, the company paid $420.00"**); the UI uses **" · "**. Low typography only, not a functional miss.

**Observation (not a push 60 fail):** the same empty decision panel also showed **"Cost so far About $198.00 (worked out from the price and how it is billed)"** on a **$99 a year** plan running **2025-11-10 to 2026-11-20** (one year and ten days). Push 60 does not define that figure. It is the same shape as the push 50 cost ODD, where a yearly price was doubled once a second billing anniversary had been reached.

### 5. Kind of loss

**60-loss Pass.** Deductibles had to be restored first (`deductibles_json` was null after push 59). After save, the Device Care card lists Cracked screen **$29.00**, Other damage **$29-$199**, Stolen **$199.00** (`s60-A-deductibles.png`). **Record a request** has **"Kind of loss (to see what the plan says a claim costs you)"**. **Cracked screen:** **"The plan lists $29.00 for this. What you were charged is what counts: enter it below."** and the fee filled with **29** (`s60-A-loss-cracked.png`). **Other damage:** **"The plan lists $29-$199 for this. What you were charged is what counts: enter it below."** (`s60-A-loss-range.png`). Home Care has no Kind of loss choice. The request was cancelled; Device Care still has three requests.

**Low, Needs CC:** after switching from Cracked screen to the range kind, the fee box **kept 29** (the earlier auto-fill) rather than clearing or updating. The range text itself was correct. "Unless you typed one" in the notes covers a value the user entered, not a previous kind's auto-fill.

## Needs code / product follow-up

1. **Low, Needs CC (60-fillmsg):** a typeless plan should **"show the message instead of filling."** Home Care has no message; the fill button is only missing.
2. **Low, Needs CC (60-loss):** changing Kind of loss should not leave the previous kind's auto-filled fee (29) in the box when the new kind is a range (or a different amount).
3. **Low, Needs CC:** **"End this plan"** with today's date did nothing visible; Cancel on the same plan worked.
4. **Low typography:** the decision panel uses **" · "** rather than the notes' commas. Functional all-time totals are correct.

## Test data created or reused

Reused:

- Item **UAT P58 Dishwasher** — `/items/01a1c762-732a-795d-956c-731f650617ba`
- Item **UAT P58 iPhone 16** — `/items/01a1c762-9a10-729f-a1d6-c1b0a2004507`
- Plan **UAT P58 Home Care** — `/plans/01a1c766-d0aa-77b4-9d31-0e7b58326814` (Refrigerator line added and tied to the Samsung refrigerator; Ice maker still excluded)
- Plan **UAT P58 Device Care** — `/plans/01a1c763-e8b9-7ee8-b83b-857beb3fef88` (deductibles restored; IMEI **UAT-P59-SERIAL-001** after undo; cap 2)

Created:

- Items: **UAT P60 Fridge No** `/items/01a1c7d5-3449-7b2c-be5a-25f662e61470` (No thanks; dismissal `01a1c7d5-898a-762d-b921-c2ea37b9c370`); **UAT P60 Samsung refrigerator** `/items/01a1c7d5-f087-7c12-832c-c4eff7becf0f` (bought Jun 1, 2020; Yes, attached); **UAT P60 Ice maker** `/items/01a1c7d6-76dd-7a0f-a08f-b2150e7b5214`; **UAT P60 Extra fridge** `/items/01a1c7d6-8d09-7035-afaf-8034ad557b65`; **UAT P60 Extra dishwasher** `/items/01a1c7d6-a479-7e36-b9ba-b045f66169ad`; **UAT P60 Washer** `/items/01a1c7d8-504f-7397-89c2-820c0ca57726`; **UAT P60 Old TV** `/items/01a1c7d8-a416-7550-98f7-d31c4da12d55`; **UAT P60 Bob Refrigerator** `/items/01a1c7e1-0727-7aec-9b57-173faad132f6`. Replacement items **UAT P60 New TV** (`01a1c7d9-a4a6-7857-b97d-b6d2e18dd300`) and **UAT P60 New iPhone** (`01a1c7da-a907-7164-8f3c-860ce15a98e9`) were removed by Undo (**Not found.**).
- Plans: **UAT P60 Ended Care** `/plans/01a1c7d7-88cf-7388-a3bf-93344e340892` (cancelled Nov 10, 2026); **UAT P60 TV Care** `/plans/01a1c7d8-c94c-7269-b2ca-e74a6e8e0210`; **UAT P60 Filled plan** `/plans/01a1c7de-7d2b-7a91-b21c-45738376c30e`; **UAT P60 Decision Care** `/plans/01a1c7df-81a7-7f18-b115-7b9b045b8763` (Nov 10, 2025 to Nov 20, 2026, $99 a year).
- Type: **UAT P60 Care Type** `01a1c7dd-bef3-7b70-a5f3-f5e2c8ba69d8` (sold by UAT P54 Shared Care Co, confirmed, https://example.com/uat-p60-care-type).

No QA fixture files were made for the share.

## Evidence

- `/workspace/uat/push60/p60-A-notes.md`, `/workspace/uat/push60/p60-B-notes.md`, `/workspace/uat/push60/p60-C-notes.md`, `/workspace/uat/push60/TESTPLAN.md`
- `/workspace/uat/push60/CHANGES-push-60-plan-offers-and-type-lines.md`
- Screenshots under `/workspace/uat/push60/shots/`
- Export: `/workspace/uat/push60/export/warrantycat-export-2026-11-10.zip`
- Neon read-only: `plan_offer_dismissals` for Fridge No; `plan_types.lines_json` for UAT P60 Care Type; Device Care `device_identifier` = `UAT-P59-SERIAL-001`
