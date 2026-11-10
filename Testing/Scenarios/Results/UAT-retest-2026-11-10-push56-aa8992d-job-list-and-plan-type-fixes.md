# UAT retest — Push 55+56: low-confidence job list and plan-type fixes (Nov 10, 2026)

- **Build:** API aa8992d, started 1:33:29 PM ET. Staging. Push 55 is API only (no prompt change). Push 56 is API and UI. **No migration.**
- **Source:** CHANGES-push-55-low-confidence-job-list.md (SHA256 `8a75e00cb073dbe4b2a5c86eb4f4856c38d648bc6d86fece9d5acc545f92da9a`); CHANGES-push-56-plan-type-fixes.md (SHA256 `ff0c0b91d6cf8c5c61358d37322fd1bfc7a4584fe0ffda30c8fccf419a022502`); p56-findings.md.
- **Accounts:** P34 Self personal (vault 3550464) and Ops as needed for Admin types. The **"A new version of WarrantyCat is ready"** banner appeared; Reload was clicked. Clock Offset 0 (never moved; confirmed after the run).
- **Fixtures:** none new. Tucson order 08 used **Read it in item Edit mode** on the existing file on **UAT S69 Hyundai Tucson** (https://stuffit-ui.onrender.com/items/01a1c3ac-2e79-7ccd-979d-c676a961710d).
- **Not reported as new (known, not done):** Sold-by Add companies cannot be verified from this page; the item's quick "Add protection plan" dialog has no type select.

## Results

| Result | Count |
|---|---|
| Pass | 7 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |

Plus **1 Medium** (Needs CC) on how order 08 jobs are assigned, and **1 Low** (pre-existing odometer reading). Orders 03, 06, 07 and 12 were not re-read (spot-check was 08 + 09 only).

## Per-step results

### Push 56 — plan-type fixes

| # | Check | Result |
|---|---|---|
| 56-view | Plan page names its type | **Pass** |
| 56-edit | Edit plan still shows the earlier version after versioning; save keeps the link | **Pass** |
| 56-typeless | A plan with no type shows no Plan type line | **Pass** |
| 56-versions | Admin "Show earlier versions" lists the old Basic, no Change/Confirm | **Pass** |
| 56-empty-url | Empty-address Confirm message | **Pass** |

**56-view.** Opening UAT P54 Demo plan (`01a1c67c-83a5-7060-8109-02657e8c4838`) shows **"Plan type: UAT P54 Care Basic (an earlier version)"** under the plan name. (`s56-view.png`)

**56-edit.** Edit plan selects **"UAT P54 Care Basic (earlier version, the one you bought under)"**. Options: **"Not on the list, or not sure"**, **"UAT P54 Care Basic"**, **"UAT P54 Care Unconfirmed (not checked yet)"**, **"UAT P54 Care Unused (not checked yet)"**, and the earlier-version entry. Saving with What it covers set to **"My own coverage text stays (p56 save)"** keeps the earlier-version selection after a reload. (`s56-edit.png`, `s56-after-save.png`)

Read-only SQL after that save: `warranty_plans` `01a1c67c-83a5-7060-8109-02657e8c4838` still has **`plan_type_id` = `01a1c670-13e7-7aba-b44d-1fbca91d91f3`** (the old Basic). The link was kept.

**56-typeless.** Tread Masters road hazard protection (`01a1c3b1-d020-7a74-a10c-58b5aa47e5d0`) and UAT P50 Auto-renew care (`01a1c3fb-2dae-7133-992e-e1df41faaf69`) show **no** Plan type line. (`s56-typeless.png`, `s56-typeless-autorenew.png`)

**56-versions.** Admin > Companies > Extended warranty plans: **unticked**, only the current Basic (**"from 2026-11-10"**). **Ticked**, an extra row: **"…Confirmed · $99.00 a year · 1 plan uses it · an earlier version, ended 2026-11-09; plans bought under it keep these terms"**, with **no Change or Confirm** button. (`s56-versions-off.png`, `s56-versions-on.png`)

**56-empty-url.** Confirm with an empty address now reads **"Enter the address of the page you read it on."** (`s56-empty-url.png`)

### Push 55 — low-confidence job list

| # | Check | Result |
|---|---|---|
| 55-08 | Tucson order 08 lists its jobs (kept or left out with ticks) | **Pass** (Medium on coverage assignment) |
| 55-09 | Order 09 spot-check still matches the prior result | **Pass** |

**55-08 Pass (the fix).** The card now lists the jobs. No low-confidence wording appeared. Odometer **14,022**. Observed card (`s55-order08.png`):

- 7 kept jobs, all **"you paid $0.00 · Bumper-to-bumper (to Apr 5, 2030)"**: the bumper cover and absorber replacement; the bumper refinish; the A/C condenser; the A/C evacuate and recharge; the front radar ADAS calibration sublet; paint materials; and hazardous waste.
- 1 job left out, **"not on a covered part"**: **"Wheels: Four wheel alignment (sublet) · $0.00"**.

**Medium, Needs CC:** order 08 is a body-shop collision repair (probably insurance-paid), but every kept job is pinned to the factory Bumper-to-bumper warranty. Collision damage is not a warranty repair, so these jobs probably should not be offered as kept warranty service, or should at least carry no coverage. No row says **"repaired under warranty"**. It is also inconsistent that the radar calibration sublet is kept while the alignment sublet is left out as "not on a covered part".

**Low/note:** a 14,022 mi odometer reading for Jun 3, 2026 with **"Repair order PCC-26-0412"** already existed before this read.

**55-09 Pass.** Hose on **Powertrain (to Apr 5, 2035)**; strut on **Bumper-to-bumper (to Apr 5, 2030)**; campaign 9ZZ on **Powertrain (to Apr 5, 2035)**; each **"repaired under warranty · you paid $0.00"**. MPI left out. The "already in the service history" note is shown. (`s55-order09.png`)

### document_readings (read-only, context)

Latest 3 rows where `kind = 'service_record'` (all `prompt_version` **service-record-v5**, model **claude-sonnet-5-5**; `lines.issue` is null on all three):

| Time (ET) | Order | `lines` Confidence | Header fields |
|---|---|---|---|
| 2026-11-10 1:41:21 PM ET | 09 (5590184, Seaport Hyundai) | **medium** | date / odometer / shop / RO **high** |
| 2026-11-10 11:04:26 AM ET | 08 (PCC-26-0412, Precision Collision Center) | **low** | date / odometer / shop / RO **high** |
| 2026-11-10 11:03:25 AM ET | 12 (HG-24518, Hillside Garage & A/C) | **high** | odometer / shop / RO **high**; date **medium** |

There is **no new stored 08 reading** this afternoon. The 11:04:26 AM ET row is the push 53 read (same prompt, so it was reused). Its `lines` Confidence was **low**, with no Issue — which is why push 53 listed no jobs. This run still offered the list, which is the push 55 change (a low-confidence job list is still offered when date, odometer, order number and shop are sure).

## Needs code / product follow-up

1. **Medium, Needs CC:** body-shop / collision jobs on order 08 should not be auto-kept under the factory Bumper-to-bumper term (no coverage, or left out for the owner to tick). Also review why the radar sublet is kept and the alignment sublet is left out.

## Evidence

- `/workspace/uat/push56/p56-findings.md`
- `/workspace/uat/push56/CHANGES-push-55-low-confidence-job-list.md`
- `/workspace/uat/push56/CHANGES-push-56-plan-type-fixes.md`
- Screenshots under `/workspace/uat/push56/shots/`
- Neon read-only: `warranty_plans.plan_type_id` after save; `document_readings` latest three `service_record` rows (Confidence/Issue only)
