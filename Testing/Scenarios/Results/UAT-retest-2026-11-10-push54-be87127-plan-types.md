# UAT retest — Push 54: plan types and wipers already-added (Nov 10, 2026)

- **Build:** API be87127, started 11:27:20 AM ET. UI ~11:25 AM ET. Staging. API and UI.
- **Migration:** `PlanTypes` (`20261110151104_PlanTypes`, product_version 9.0.22) previously verified on Neon StuffIt (`square-tree-53585492`, db `stuffit`). `plan_types` reshaped; `warranty_plans.plan_type_id` and `serviced_by_party_id` present. No root/series id columns on `plan_types`.
- **Source:** CHANGES-push-54-plan-types-2026-11-10.md (SHA256 `b8ee833ceeb368222cf38cbf1a776cdd9a279b69c0579bdda334817a716aea62`); TESTPLAN.md; p54-findings.md.
- **Accounts:** Ops (vault 2460773, TOTP) for Admin types; P34 Self personal (vault 3550464) for the plan form, `/admin/companies`, and wipers. Clock Offset 0 (never moved; confirmed after the run).
- **Fixtures:** no new fixture files were made for the share.
- **Skipped:** order 08 (known, not fixed). Not built yet: "Plans they sell", person-facing add-type, candidate queue, seeded providers, receipt-to-type matching, stores/makers as sellers, phone and home appliance plans.

## Results

| Result | Count |
|---|---|
| Pass | 9 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |

Plus **2 Medium** (Needs CC) and several Lows, below. The core versioning check passed in the database (old version kept; the plan still points at it), but the Edit-plan type select goes blank after a new version is saved.

## Per-step results

| # | Check | Result |
|---|---|---|
| 54-wipers | Order 06 wipers already added by hand still show on the card, no tick | **Pass** |
| 54-admin | Admin plan-types page: add, "Not confirmed yet", Confirm needs https, bad/empty refused | **Pass** |
| 54-noadmin | P34 Self cannot use `/admin/companies` | **Pass** |
| 54-picker | "What kind of plan is it?" for companies with types; unconfirmed "(not checked yet)"; no select when the company has no types | **Pass** |
| 54-fill | Picking a type fills only blanks, with the "Filled in … not from your contract" note | **Pass** |
| 54-contract | Contract dates, price, contract number and fee are never filled from a type | **Pass** |
| 54-saved | Save, reopen: same type selected; changing company clears the type (on `/plans/new`) | **Pass** |
| 54-version | Change a type that a plan uses: new version from the date below; old words kept; plan still points at the old version | **Pass** (Medium: Edit-plan select goes blank; Low/Medium: admin cannot view the old version) |
| 54-inplace | A type nobody uses is corrected in place | **Pass** |

### Details

**54-wipers Pass.** F-150 order 06, Read it in item Edit mode: wipers (the only left-out job, already added by hand) show **"already added by you"** with no tick box. (`s54-06-card.png`, `s54-06-hist.png`)

**54-admin Pass (A1).** Ops: Admin > Companies > **"Extended warranty plans (plan types)"**. Add a type, save with no page address: **"Not confirmed yet"** (`s54-A1-add-unconfirmed.png`). **Confirm** refuses a bad or empty address (`s54-A1-confirm-refused.png`); a valid https address is accepted (`s54-A1-confirm-ok.png`). **Low:** the empty-address message is **"The SourceUrl field is required."** (internal field name). Types list: `s54-A1-types-list.png`.

**54-noadmin Pass.** P34 Self: `/admin/companies` is not available (`s54-noadmin.png`).

**54-picker / 54-fill / 54-contract / 54-saved Pass (B, `/plans/new`).** After choosing a company that has types, **"What kind of plan is it?"** appears. An unconfirmed type shows **"(not checked yet)"**. Typing your own "What it covers" first, then picking a type: yours stays; exclusions, waiting period and kind fill in, with a note **"Filled in ... not from your contract"** (and claims-handled-by when set). Contract dates, price, contract number and fee are not filled from the type. Save and reopen: the same type is selected. Change the company: the type is cleared. (`s54-B-picker.png`, `s54-B-fill.png`, `s54-B-saved.png`, `s54-B-cleared.png`)

**Low / question:** the item's quick **"Add protection plan"** dialog has no type select (`s54-B-picker-dialog-noselect.png`). **Low:** the plan **view** page does not show the type.

**54-version Pass, with Medium / Low findings (A2).** The Change form on the in-use Basic shows, verbatim: **"1 plan uses this. Saving makes a new version from the date below; their plans keep the terms they were bought under."** (`s54-A2-version-note.png`). After saving, the admin list shows a **single** Basic row (**"Confirmed · $99.00 a year · from 2026-11-10"**); the "plans use it" count is gone, and Admin has **no way to view the old version** (Low/Medium). (`s54-A2-old-version.png`)

P34 Self's plan still shows the **old exclusions** text (`s54-A2-plan-still-old.png`). However, Edit plan's **"What kind of plan is it?"** select is now **blank**: the options list only the new Basic, so the plan's old-version pointer matches nothing. If the user saves that form, the type link may be cleared. **Medium, Needs CC** (confirmed in the database: the plan still points at the old row).

**54-inplace Pass.** The Unused type was corrected in place (`s54-A2-inplace.png`).

### Database check (read-only, Neon StuffIt)

No root or series id columns on `plan_types`. Rows named `UAT P54 Care%`:

| id | name | effective_from | effective_to | exclusions |
|---|---|---|---|---|
| `01a1c670-13e7-7aba-b44d-1fbca91d91f3` | UAT P54 Care Basic | (null) | **2026-11-09** | **UAT P54 excludes cosmetic damage and consumables** |
| `01a1c67e-efd7-7cd9-958f-c4bae33766e9` | UAT P54 Care Basic | **2026-11-10** | (null) | UAT P54 Basic version 2 exclusions |
| `01a1c671-9002-75b1-ad99-ef2a7baca47c` | UAT P54 Care Unconfirmed | (null) | (null) | (null) |
| `01a1c671-afde-75cf-8721-c25a0d7dbef3` | UAT P54 Care Unused | (null) | (null) | UAT P54 unused revised exclusions |

`warranty_plans` `01a1c67c-83a5-7060-8109-02657e8c4838` (**UAT P54 Demo plan**) has **`plan_type_id` = `01a1c670-13e7-7aba-b44d-1fbca91d91f3`**. The old Basic version **still exists** with the original exclusions and `effective_to` set, and the plan **points at it**.

## Other findings

1. **Medium, Needs CC:** unverified, creator-only companies added through the Sold-by Add cannot be verified or shared from Admin (`s54-A1-shared-add.png`, `s54-A1-verify.png`, `s54-A1-types-list-shared.png`).
2. **Medium, Needs CC:** after a type is versioned, Edit plan's type select does not include the old version the plan still points at, so the control is blank and a save may clear `plan_type_id`.
3. **Low/Medium:** old versions are not visible in Admin after the new version is saved.
4. **Low / question:** the item quick "Add protection plan" dialog has no type select.
5. **Low:** the plan view page does not show the type.
6. **Low:** empty-address validation: **"The SourceUrl field is required."**

## Test data created

- Parties: UAT P54 Care Co (`01a1c66f-70f3-7d16-b062-d32056bdccd3`), UAT P54 Claims Co (`01a1c66f-abc7-7b19-90e8-a24a82c989c2`), UAT P54 Shared Care Co (`01a1c677-dc79-7b44-aac8-dea0722b550a`; types are attached here), UAT P54 Shared Claims Co (`01a1c677-f090-7374-a0f8-b01000b3dded`).
- Types: UAT P54 Care Basic (two rows: old `01a1c670-…` and new `01a1c67e-…`), UAT P54 Care Unconfirmed, UAT P54 Care Unused (see table above).
- Item: UAT P54 Kettle (`01a1c673-2e40-7d02-a9b9-b28e8451eaf7`).
- Plan: UAT P54 Demo plan (`01a1c67c-83a5-7060-8109-02657e8c4838`).

No new fixture files were made for the share.

## Needs code / product follow-up

1. **Medium, Needs CC:** keep the plan's selected type visible after versioning (list or label the version the plan points at) so a later save cannot drop `plan_type_id`.
2. **Medium, Needs CC:** allow Ops to verify or share a creator-only company that was added through Sold-by, or document another path.
3. **Low/Medium:** let Admin view (or at least indicate) superseded type versions.
4. Lows: type select on the item quick-add dialog (question); show the type on the plan view page; replace "SourceUrl" in the validation message.

## Evidence

- `/workspace/uat/push54/p54-findings.md`
- `/workspace/uat/push54/CHANGES-push-54-plan-types-2026-11-10.md`
- Screenshots under `/workspace/uat/push54/shots/`
- Neon read-only SELECTs on `plan_types` and `warranty_plans` (project `square-tree-53585492`, db `stuffit`)
