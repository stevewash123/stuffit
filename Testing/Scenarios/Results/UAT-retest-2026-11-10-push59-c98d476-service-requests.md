# UAT retest — Push 59: asking for service, and the push 58 plan-line age fix (Nov 10, 2026)

- **Build:** API c98d476, started 5:17:40 PM ET. UI ~5:16 PM ET. Staging. API and UI.
- **Migration (verified read-only before the run, Neon project `square-tree-53585492`, db `stuffit`):** `__EFMigrationsHistory` has `20261110215905_PlanServiceRequests` (product_version `9.0.22`). New table `plan_service_requests`.
- **Source:** CHANGES-push-59-service-requests.md (SHA256 `1e6f14abe9588c32677b9e00d7e2c809336f91a980e84a6a918be8af269450a5`); TESTPLAN.md; p59-A-notes.md; p59-B-notes.md; export `/workspace/uat/push59/export/warrantycat-export-2026-11-10.zip`.
- **Account:** P34 Self personal (vault 3550464). Ops was not used. P34 Self saw **"A new version of WarrantyCat is ready"** and clicked Reload, then a hard reload. Brief B had no banner; a hard reload was still done. Clock Offset 0 (never moved; confirmed after the run).
- **Fixtures:** none new. No QA fixture files were made for the share.
- **Not reported:** items marked **Not built yet** (claim log / Money recovered, photo and email attachments, denial wizard, fees on the plan-decision cost, Request service from a line row, home appliance extras).

## Results

| Result | Count |
|---|---|
| Pass | 9 |
| Partial | 1 |
| Fail | 0 |
| Inconclusive | 0 |

The Partial is **Medium, Needs CC** (plan-year company-paid total includes an earlier-year request). Plus **3 Lows** (list shows the line but not the linked item; stray space before commas; export has no past-cap column and is unsorted). One **note**: the empty "what to have ready" prompt does not mention the waiting period; that is not a miss of the notes' wording. The "line or item that is not the plan's" bad-input sub-check is **N/A** in the UI (pickers only list this plan's lines and items) and is not counted as a row.

## Per-step results

| # | Check | Result |
|---|---|---|
| 59-hide | Linked plan line hides the age estimate and stores none | **Pass** |
| 59-blurb | Lines-card blurb is the same on any plan | **Pass** |
| 59-ready | "Asking for service" / what to have ready | **Pass** |
| 59-record | Record a request, all four decisions, Denied / Partly extra fields | **Pass** |
| 59-list | Request list, newest first, Change, Remove asks first | **Pass** (Lows on item and commas) |
| 59-counts | Plan year counts | **Partial** (Medium) |
| 59-cap | Past the cap is flagged, not blocked | **Pass** |
| 59-used | A line's limit used; Denied and earlier year not counted on the line | **Pass** |
| 59-bad | Bad input refused with a message | **Pass** (not-on-plan **N/A** in the UI) |
| 59-export | `plan_service_requests.csv` in the zip and README; Dishwasher age years empty | **Pass** |

### Push 58 fix

**59-hide Pass.** On Home Care, **Change** on the linked Dishwasher line: with **UAT P58 Dishwasher** chosen, **"About how old, in years"** was hidden (`s59-A-estimate-hidden.png`). Clearing the item to **"None: it has no receipt"** brought the field back, empty (`s59-A-estimate-returns.png`). Re-picking the item hid it again. Saved with limit **$2,000**. The card shows **"about 8 years old (from your purchase date) · limit $2,000.00"** (and the age-limit-of-5 warning), not "your estimate" (`s59-A-dishwasher-after.png`). Read-only SQL: that `plan_lines` row now has **`age_years` = null** and `item_id` = `01a1c762-732a-795d-956c-731f650617ba`. The export **"age years"** cell is empty (see 59-export).

**59-blurb Pass.** Device Care and Home Care both use: **"What the contract lists as covered, with the limit and age limit it states. A system that came with the house needs no receipt. Your contract decides what is really covered."** (`s59-A-device-blurb.png`, `s59-A-home-blurb.png`). Not the old home-warranty-only wording on the phone plan. (The "system that came with the house" sentence is generic and appears on both.)

### Asking for service (S3.4.8)

**59-ready Pass.** The **"Asking for service"** card sits under the lines card on both plans. Device Care, with none of the ready fields, says: **"Add the claim phone, website, contract number and service fee to the plan to see them here."** / **"0 requests this plan year"** / **"No requests recorded."** (`s59-A-device-ready-empty.png`). It does not mention the waiting period (note only: the notes say a plan with none of those says to add them, and those listed in the empty prompt are the four always-shown fields; waiting is a separate, conditional line). After saving contract `UAT-P59-HC-001`, phone `555-010-5901`, website `https://example.com/uat-p59-home-care`, fee 75, and waiting 30 days on Home Care, the card reads (`s59-A-home-ready.png`):

> What to have ready when you ask
> Phone: 555-010-5901 (tel:555-010-5901)
> Website: https://example.com/uat-p59-home-care
> Contract number: UAT-P59-HC-001
> Service fee: $75.00 a visit
> You are inside the waiting period. Claims can start Dec 10, 2026.

The phone is tappable (`tel:555-010-5901`).

**59-record Pass.** Day defaulted to **2026-11-10**. All four decisions were recorded. **"Their reason, in their words"** and **"The contract text it points to"** appeared only for **Denied** and **Partly covered**. Screens: `s59-A-req-waiting.png`, `s59-A-req-covered.png`, `s59-A-req-denied.png`, `s59-A-req-partly.png`.

**59-list Pass.** Newest first (`s59-A-req-list.png`), then Change and Remove-asks-first. After the four same-day requests, the list was:

> 4 requests this plan year · fees you paid $225.00 · the company paid $230.00
> 1. Heating making noise [Partly covered] Nov 10, 2026 · Heating system · Sam Ortiz , 555-010-5904 · you paid $75.00 · the company paid $50.00 / They said: Wear parts only / The contract text: Limited coverage for wear
> 2. Ice maker leaked [Denied] Nov 10, 2026 · Ice maker · you paid $0.00 / They said: Pre-existing condition / The contract text: Does not cover pre-existing damage
> 3. Dishwasher not draining [Covered] Nov 10, 2026 · Dishwasher · Jordan Kim , 555-010-5903 · you paid $75.00 · the company paid $180.00
> 4. Furnace will not ignite [Waiting to hear] Nov 10, 2026 · Heating system · Pat Lee , 555-010-5902 · you paid $75.00 / Follow up: Call back Friday

**Change** on the furnace row reopened **"Change this request"** with the saved values; Cancelled (`s59-A-req-change.png`). **Remove** asked first: **"Remove this request? / Ice maker leaked is taken off the record. Nothing else changes."** Cancel was clicked; four rows remained (`s59-A-req-remove-ask.png`).

**Low, Needs CC (list item):** the notes say the list shows **"the line or item"**. The Covered Dishwasher row shows only the line (**Dishwasher**), not the linked item **UAT P58 Dishwasher**. The export (and the database `item_id`) does include the item.

**Low, Needs CC (commas):** a stray space before commas: **"Pat Lee , 555-010-5902"** and **"limit $5,000.00 , $50.00 of it used this plan year"** (same on the $2,000 Dishwasher line). The notes' expected used-limit text is **"limit $2,000.00, $180.00 of it used this plan year"** with no space before the comma.

**59-used Pass.** After the Covered $180 request, Dishwasher shows used-this-year **$180.00** at limit **$2,000.00**; Heating shows **$50.00** used from the Partly covered request; Ice maker (Denied) added nothing (`s59-B-line-used.png`). An earlier-plan-year Covered request on 2026-10-15 for **"Earlier-year pump"**, company paid **$500**, was accepted (no refusal, even though that day is before the plan start of 2026-11-10). The Dishwasher line still showed **$180.00** used, not $680 (`s59-B-earlier-year.png`). The notes require a future day to be refused, not a day before the plan start; accepting Oct 15 is therefore not a bad-input fail, but it is the row that then skewed the company-paid total (59-counts).

**59-counts Partial (Medium, Needs CC).** The notes say plan-year counts are **"N requests this plan year"** plus **"fees you paid $X"** and **"the company paid $Y"** when there are any, and **"the plan year starts on the plan's anniversary."** Before the Oct 15 request: **"4 requests this plan year · fees you paid $225.00 · the company paid $230.00"**. After it: **"4 requests this plan year · fees you paid $225.00 · the company paid $730.00"** (`s59-B-home-counts.png`). The request count correctly leaves the earlier-year row out; the company-paid total includes its **$500**. The line-used figure stayed at $180. The money totals are not using the same plan-year window as the count.

**59-bad Pass** (not-on-plan **N/A** in the UI). Blank what-broke: **"Say what broke."** (`s59-B-bad-name.png`). Fee `-10`: **"A fee is an amount of zero or more."** Company paid `-10`: **"What the company paid is an amount of zero or more."** (`s59-B-bad-negative.png`). Day **2026-11-20**: **"That date is in the future."** (`s59-B-bad-future.png`). Pickers list only this plan's lines (Not one of the lines / Heating system / Dishwasher / Ice maker) and items (None / UAT P58 Dishwasher), so a line or item that is not the plan's cannot be chosen in the UI. Nothing bad was saved.

**59-cap Pass.** Device Care re-ticked **"This protects a phone or other device"**, serial `UAT-P59-SERIAL-001`, claims allowed **2**. Before any requests: **"0 requests this plan year · 0 of 2 claims used; resets Nov 10, 2027"** (`s59-B-device-cap.png`). Three requests this plan year all saved. The third ("Third claim past cap") shows **"This was past the plan's limit of 2 claims a year. It may not be covered. Check the contract."** Counts after: **"3 requests this plan year · 3 of 2 claims used; resets Nov 10, 2027"** (no fees/paid totals; none were entered) (`s59-B-past-cap.png`, `s59-B-device-counts.png`).

**59-export Pass.** Settings > Privacy & data > Prepare my download produced `warrantycat-export-2026-11-10.zip`. README lists **"plan_service_requests.csv  each request for service on a plan: what broke, the fee, the company's decision and what it paid"**. Header: `plan,date,what broke,line,item,who was sent,phone,fee paid,decision,paid by the company,reason if denied,contract text,follow up`. The eight rows are present. The Home Care Dishwasher request includes item **UAT P58 Dishwasher**. In `plan_lines.csv`, the linked Dishwasher row has empty **"age years"** (Heating system is still 8, as an unlinked estimate):

```
UAT P58 Home Care,system,Heating system,,,8,5000.00,,,,,no
UAT P58 Home Care,appliance,Dishwasher,,,,2000.00,,5,,UAT P58 Dishwasher,no
UAT P58 Home Care,addon,Ice maker,,,,,,,,,yes
```

**Low, Needs CC (export completeness):** the notes' export row only requires the file and the README line (that Passes). The CSV has **no past-cap flag column** (the third Device Care request is flagged only in the UI) and the rows are **not sorted** by plan or date (Home Care's furnace row comes after two Device Care rows).

### Read-only SQL (after the run)

`plan_lines` Dishwasher (`01a1c767-97ed-7e29-bdb0-039a9c614d43`): **`age_years` is null**, `limit_amount` 2000.00, `age_limit_years` 5, `item_id` `01a1c762-732a-795d-956c-731f650617ba`.

`plan_service_requests` — 8 rows (5 Home Care, 3 Device Care):

| requested_on | Plan | what_broke | decision | fee_paid | paid_by_company | item_id set |
|---|---|---|---|---|---|---|
| 2026-10-15 | Home Care | Earlier-year pump | covered | null | 500.00 | yes |
| 2026-11-10 | Home Care | Furnace will not ignite | pending | 75.00 | null | no |
| 2026-11-10 | Home Care | Dishwasher not draining | covered | 75.00 | 180.00 | yes |
| 2026-11-10 | Home Care | Ice maker leaked | denied | 0.00 | null | no |
| 2026-11-10 | Home Care | Heating making noise | partial | 75.00 | 50.00 | no |
| 2026-11-10 | Device Care | First cracked screen | pending | null | null | no |
| 2026-11-10 | Device Care | Second cracked screen | pending | null | null | no |
| 2026-11-10 | Device Care | Third claim past cap | pending | null | null | no |

Home Care fees entered this calendar set of rows: $225; company paid 180+50+500 = $730 (the $500 is the earlier-year row). IDs are in the evidence section below if needed; none were shown in the UI.

## Needs code / product follow-up

1. **Medium, Needs CC (59-counts):** **"the company paid $Y"** for this plan year included the **$500** Covered request dated **Oct 15, 2026** (before the 2026-11-10 anniversary and before the plan start). **"4 requests this plan year"** and the Dishwasher **"used this plan year"** figure correctly left that row out. The plan-year money totals should use the same window as the count. The form also accepted a day before the plan start; the notes only require refusing a **future** day, so that is not a separate bad-input fail.
2. **Low, Needs CC:** the request list shows the line but not the linked item, though the notes say **"the line or item"** and the export/DB have the item.
3. **Low, Needs CC:** stray space before commas in the list and in the used-limit text (**"Pat Lee , 555-…"**, **"$5,000.00 , $50.00 of it used"**).
4. **Low, Needs CC (completeness):** `plan_service_requests.csv` has no past-cap column and is not sorted; the required "file is in the zip and listed in README" check still Passes.

## Test data

Reused from push 58, then edited:

- Item **UAT P58 Dishwasher** — https://stuffit-ui.onrender.com/items/01a1c762-732a-795d-956c-731f650617ba
- Plan **UAT P58 Home Care** — https://stuffit-ui.onrender.com/plans/01a1c766-d0aa-77b4-9d31-0e7b58326814 (contract `UAT-P59-HC-001`, phone 555-010-5901, website https://example.com/uat-p59-home-care, fee $75, waiting 30 days; Dishwasher limit $2,000, `age_years` cleared)
- Plan **UAT P58 Device Care** — https://stuffit-ui.onrender.com/plans/01a1c763-e8b9-7ee8-b83b-857beb3fef88 (device section re-ticked, serial `UAT-P59-SERIAL-001`, cap 2)

Requests created (UI showed no ids; from Neon):

- Home Care: Earlier-year pump `01a1c7a0-fff5-7d2c-9a06-52268bcdadde`; Furnace will not ignite `01a1c79d-6331-7ba4-ba2b-c85124a83178`; Dishwasher not draining `01a1c79d-c753-7040-a2c0-e43990e7bda8`; Ice maker leaked `01a1c79e-5b7b-75ff-9f2a-59691a2fddc2`; Heating making noise `01a1c79e-c3bc-7230-a5d4-3700fa31555b`
- Device Care: First cracked screen `01a1c7a2-7faf-7a99-83c5-9ea2f2c1b749`; Second cracked screen `01a1c7a2-957a-7cca-bad1-b637386c63e4`; Third claim past cap `01a1c7a2-aaab-703d-b578-91f6305e8276`

No QA fixture files were made for the share.

## Evidence

- `/workspace/uat/push59/p59-A-notes.md`, `/workspace/uat/push59/p59-B-notes.md`, `/workspace/uat/push59/TESTPLAN.md`
- `/workspace/uat/push59/CHANGES-push-59-service-requests.md`
- Screenshots under `/workspace/uat/push59/shots/`
- Export: `/workspace/uat/push59/export/warrantycat-export-2026-11-10.zip` (`plan_service_requests.csv`, `plan_lines.csv`, `README.txt`)
- Neon read-only: `plan_service_requests` for both plans (8 rows); `plan_lines.age_years` on the Dishwasher line
