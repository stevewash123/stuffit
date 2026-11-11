# UAT retest — Push 61: fixes from the push 60 report (Nov 10, 2026)

- **Build:** API 94f58ac, started 7:55:47 PM ET. UI redeployed ~7:54 PM ET. Staging. API and UI. **No migration.**
- **Source:** CHANGES-push-61-push-60-fixes.md (SHA256 `622ff802d513eb94fa6487a39ff50f27b5b3da5ab4d5524ef508db2331ed39b3`); TESTPLAN.md; p61-A-notes.md; p61-B-notes.md.
- **Account:** P34 Self personal (vault 3550464). Brief A saw **"A new version of WarrantyCat is ready"** and clicked Reload, then a hard reload. Brief B had no banner. Clock Offset 0 at the start; Brief B advanced it (365, then 365, then 2 days) and reset. GET after the run: **Offset 0** at 8:45:16 PM ET Nov 10 (reset logged at 8:44:01 PM ET).
- **Fixtures:** none new. No QA fixture files were made for the share.
- **Not reported:** dots in the decision panel's Service requests line (the notes say the commas were wording, not a requirement).

## Results

| Result | Count |
|---|---|
| Pass | 6 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |
| Not checkable in UI | 1 |

The not-checkable row is the no-end plan's **"Cost so far"** (B3): it is **not a Fail**. A plan with no end date never shows a decision panel or Cost so far (at clock 0 or +365 days), so there is no screen to read. **Low / question, Needs CC:** if no-end plans are meant to show cost so far somewhere, it is missing; otherwise it is API-only.

A process note, not an app issue: the first Brief B clock calls used `/workspace/uat/m.sh clock` (POST `/api/maintenance/clock`) and got HTTP 401. The key was fine. `clock/advance?days=N` and `clock/reset` then worked.

## Per-step results

| # | Check | Result |
|---|---|---|
| 61-cost | Decision Care "Cost so far" is About $99.00, not $198.00 | **Pass** |
| 61-loss | Kind of loss fee fills, empties on a range, fills Stolen, typed fee is kept | **Pass** |
| 61-msg | Typeless, no-lines message; it goes away after a type with lines, or a line | **Pass** |
| 61-end | End this plan with today's date shows ended, end date today | **Pass** |
| 61-monthly | One-year monthly plan is twelve payments, not thirteen | **Pass** |
| 61-yearly | Three-year yearly plan is three payments, not four, including past the end | **Pass** |
| 61-noend | A plan with no end date keeps counting | **Not checkable in UI** (Low / question) |

### Decision Care and kind of loss

**61-cost Pass.** UAT P60 Decision Care (`/plans/01a1c7df-81a7-7f18-b115-7b9b045b8763`, $99 a year, Nov 10, 2025 to Nov 20, 2026) at clock 0 (already Nov 10, 2026) (`s61-A-decision-cost.png`):

> This plan ends in 10 days
> Ends on Nov 20, 2026
> Renewal price Not known: ask the company · Enter it
> Service requests 3 requests · fees you paid $150.00 · the company paid $520.00
> Cost so far About $99.00 (worked out from the price and how it is billed)

Not $198.00.

**61-loss Pass.** Device Care Record a request (`s61-A-loss-cracked.png`, `s61-A-loss-range-empty.png`, `s61-A-loss-stolen.png`, `s61-A-loss-typed.png`):

- **Cracked screen:** fee **29**; "The plan lists $29.00 for this. What you were charged is what counts: enter it below."
- **Other damage:** fee **empty**; "The plan lists $29-$199 for this. …"
- **Stolen:** fee **199**; "The plan lists $199.00 for this. …"
- Typed **40** on Stolen, then switched to Cracked screen and to Other damage: **40** stayed.

Cancelled without saving.

### Typeless message and End this plan

**61-msg Pass.** Home Care (typeless, already has lines): the message is **absent** (`s61-A-home-nolines-msg-absent.png`). **UAT P61 Empty Typeless** showed exactly:

> If you pick the kind of plan this is (Edit the plan) and it lists what it covers, you can fill these lines in with one button.

(`s61-A-empty-message.png`). UAT P60 Care Type is only listed under **UAT P54 Shared Care Co**, so the company was switched from American Home Shield to Shared Care Co in order to pick that type. After save: **"Plan type: UAT P60 Care Type"**, button **"Fill in the lines from UAT P60 Care Type"**, message gone (`s61-A-message-gone-type.png`). **UAT P61 Empty Then Line** had the same exact message; after adding line **Widget**, the message was gone (`s61-A-message-gone-line.png`). Device Care and Decision Care (no lines, no type) also show the message, consistent with the rule.

**61-end Pass.** **UAT P61 End Today** (started Nov 10, 2026, had been set to end Nov 10, 2027). Confirm dialog: **"End this plan? / UAT P61 End Today ends on Nov 10, 2026. It will show as ended."** with Cancel | End this plan (`s61-A-end-dialog.png`; the dialog was centred and confirmed cleanly). After: badge **"Ended Nov 10, 2026"**, Term **"Nov 10, 2026 to Nov 10, 2026"** (`s61-A-ended.png`). It did not stay on **"No fixed end date"**.

### Extra Cost so far (fixed-end and no-end)

**61-monthly Pass.** **UAT P61 Monthly One Year** ($10 a month, Nov 10, 2025 to Nov 10, 2026), at clock 0 (the end date) (`s61-B-monthly-12.png`): **"This plan ends today / Ends on Nov 10, 2026 / Cost so far About $120.00 (worked out from the price and how it is billed)"**. The plan card also shows **"Cost $10.00 a month ($120.00 a year)"**. Twelve payments, not thirteen ($130).

**61-yearly Pass.** **UAT P61 Three Year Yearly** ($99 a year, Nov 10, 2023 to Nov 10, 2026), at clock 0 (the end date): **"Cost so far About $297.00"** — not $396.00 (`s61-B-yearly-3.png`).

The optional live path on **UAT P61 Three Year Live** ($99 a year, Nov 10, 2025 to Nov 10, 2028):

- Clock 0 and Offset 365 (app date Nov 10, 2027): **no decision panel** (badge **"Until Nov 10, 2028"**). The year-2 About $198.00 value is **not visible**. That is **by design** (the panel only appears inside the decision window); note only, not a fail (`s61-B-y2.png`).
- Offset 730 (app date Nov 9, 2028, one day left): **"Cost so far About $297.00"** (`s61-B-y3.png`).
- Offset 732 (past the end): **"Ended Nov 10, 2028"** / **"Did this renew?"** / **"Cost so far About $297.00"** — still not $396.00 (`s61-B-end.png`).

**61-noend — Not checkable in UI (Low / question, Needs CC).** **UAT P61 No End Yearly** ($50 a year, start Nov 10, 2025, no end). At clock 0 and at Offset 365 there is **no decision panel** and **no "Cost so far"** anywhere (badge **"No fixed end date"**; plan card **"Term Nov 10, 2025 , no fixed end / Cost $50.00 a year"**). **"Keeps counting"** cannot be read on a screen (`s61-B-noend-now.png`, `s61-B-noend-plus1y.png`). This is **not a Fail** of the billed-period arithmetic. Question for CC: if no-end plans are meant to show cost so far somewhere, it is missing; otherwise it is API-only.

**Clock.** After the advances, `clock/reset` returned **"Back to real time. Offset 0 day(s); the app's time is 2026-11-11 01:44:01Z"** (8:44:01 PM ET). A later GET was Offset 0 at 8:45:16 PM ET. After a hard reload, Three Year Live was back to **"Until Nov 10, 2028"** with no panel, as at clock 0.

## Needs code / product follow-up

1. **Low / question, Needs CC (61-noend):** a plan with no end date never shows the decision panel or **"Cost so far"**, so "keeps counting" cannot be checked in the UI. Should that figure appear somewhere for open-ended plans, or is it API-only?

## Test data

Reused:

- Plan **UAT P60 Decision Care** — https://stuffit-ui.onrender.com/plans/01a1c7df-81a7-7f18-b115-7b9b045b8763
- Plan **UAT P58 Device Care** — https://stuffit-ui.onrender.com/plans/01a1c763-e8b9-7ee8-b83b-857beb3fef88 (no request was saved)
- Plan **UAT P58 Home Care** — https://stuffit-ui.onrender.com/plans/01a1c766-d0aa-77b4-9d31-0e7b58326814 (contrast only)
- Type **UAT P60 Care Type** (picked on Empty Typeless after switching that plan's company to **UAT P54 Shared Care Co**; **UAT P60 Filled plan** was not edited)

Created:

- **UAT P61 Empty Typeless** — https://stuffit-ui.onrender.com/plans/01a1c840-721a-797d-ab72-b4a3ccc9e190 (company later UAT P54 Shared Care Co, type UAT P60 Care Type)
- **UAT P61 Empty Then Line** — https://stuffit-ui.onrender.com/plans/01a1c841-3e00-7419-85e5-069d1bcdfbf4 (line Widget)
- **UAT P61 End Today** — https://stuffit-ui.onrender.com/plans/01a1c841-abfc-756b-af52-43411c4fbdca (ended Nov 10, 2026)
- **UAT P61 Monthly One Year** — https://stuffit-ui.onrender.com/plans/01a1c843-4f76-711f-99bd-0b926db0197d
- **UAT P61 Three Year Yearly** — https://stuffit-ui.onrender.com/plans/01a1c843-8771-7a62-95a8-256df2f7934f
- **UAT P61 Three Year Live** — https://stuffit-ui.onrender.com/plans/01a1c843-e674-7d3e-b0e8-784e65a3a955
- **UAT P61 No End Yearly** — https://stuffit-ui.onrender.com/plans/01a1c844-27ca-71ef-9171-d893b1ce5dcf

No QA fixture files were made for the share.

## Evidence

- `/workspace/uat/push61/p61-A-notes.md`, `/workspace/uat/push61/p61-B-notes.md`, `/workspace/uat/push61/TESTPLAN.md`
- `/workspace/uat/push61/CHANGES-push-61-push-60-fixes.md`
- Screenshots under `/workspace/uat/push61/shots/`
- Clock: Brief B advance/reset log (Offset only); GET Offset 0 after the run
