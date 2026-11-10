# UAT retest — Push 58: phone and device insurance, and plan lines (Nov 10, 2026)

- **Build:** API 4377c24, started 4:21:02 PM ET. UI redeployed ~4:19 PM ET. Staging. API and UI.
- **Migrations (verified read-only before the run, Neon project `square-tree-53585492`, db `stuffit`):** `20261110192245_DeviceInsurance` and `20261110194346_PlanLines` (both product_version `9.0.22`) are in `__EFMigrationsHistory`. `warranty_plans` has `device_identifier`, `deductibles_json`, `claim_cap`, `replacement_kind`, `replacement_time`. New table `plan_lines`.
- **Source:** CHANGES-push-58-device-insurance-and-plan-lines.md (SHA256 `8801589721c175fb05aad7b2093826d377f74ca73021b64184e3896e7c8c244c`); TESTPLAN.md; p58-A-notes.md; p58-B-notes.md; export `/workspace/uat/push58/export/warrantycat-export-2026-11-10.zip`.
- **Accounts:** P34 Self personal (vault 3550464) for items, plans, the Best Buy store page, and the export; Ops (vault 2460773, TOTP) for the Admin plan-types link. P34 Self saw **"A new version of WarrantyCat is ready"** and clicked Reload, then a hard reload. Ops had no banner; a hard reload was still done. Clock Offset 0 (never moved; confirmed after the run).
- **Fixtures:** none new. No QA fixture files were made for the share.
- **Not reported:** items marked **Not built yet** (Add to your plan? on a new item, claim counting or caps, service requests, a plan type filling the lines, the upgrade flow, the claim deductible, the cost view, the three-layer explanation, home appliance plans).

## Results

| Result | Count |
|---|---|
| Pass | 13 |
| Partial | 1 |
| Fail | 1 |
| Inconclusive | 0 |

The Partial and the Fail are both **Medium, Needs CC**, and they are the same underlying miss: a linked line still stores (and, on Change, still offers) the typed age estimate, even though the card shows the purchase-date age. The duplicate-loss-kind check is **N/A** in the UI (one fixed row per kind) and was not tried on the API; it is not counted as a row.

## Per-step results

| # | Check | Result |
|---|---|---|
| 58-addon | Fifth Add-on on a phone-named item, not on a dishwasher | **Pass** |
| 58-fields | Device section fields on the plan form | **Pass** |
| 58-save | Saving keeps IMEI, cap, replacement, and filled loss rows | **Pass** |
| 58-empty | Empty deductible rows dropped; untick clears device details | **Pass** |
| 58-bad | Negative amount refused; duplicate kinds | **Pass** (duplicate **N/A** in the UI) |
| 58-card | "What it covers, line by line" on every plan page | **Pass** |
| 58-heat | Heating system, no receipt, $5,000, age 8 estimate | **Pass** |
| 58-dish | Linked Dishwasher age from the purchase date | **Pass** (display) |
| 58-agelimit | Age-limit warning; the line stays | **Pass** |
| 58-leftout | "My contract does not cover this one" struck through | **Pass** |
| 58-change | Change opens the line; an item-linked line shows no estimate | **Fail** (Medium) |
| 58-noname | Empty-name message | **Pass** |
| 58-export | `plan_lines.csv` in the zip and in README.txt | **Partial** (Medium) |
| 58-dot | No stray **"· "** on a plan type with no price note | **Pass** |
| 58-link | "Add or confirm plan types" opens on that company | **Pass** |

### Part 1 — phone and device insurance

**58-addon Pass.** On **UAT P58 Dishwasher**, Add-on protection has four choices ("I have the paperwork or a photo", "I'll type it in", "It covers more than this item", "It came free with my card or store") and no **"Phone or device insurance"** (`s58-A-dishwasher-addon.png`). On **UAT P58 iPhone 16** a fifth choice appears: **"Phone or device insurance — The carrier's, Apple's or another company's plan for a phone, tablet or watch: what a claim costs, how many you get, how fast a replacement comes."** (`s58-A-iphone-addon.png`). Clicking it opened `/plans/new?item=01a1c762-9a10-729f-a1d6-c1b0a2004507&itemName=UAT%20P58%20iPhone%2016&device=1` with **"Covers UAT P58 iPhone 16"** ticked, What is it = **Insurance**, Paid = **a month**, **"It renews automatically"** ticked, and **"This protects a phone or other device"** ticked and open (`s58-A-form-prefilled.png`). Sold-by was set to **Asurion** (required; the brief had not named a company).

**58-fields Pass.** The section has **"IMEI or serial number (optional, but it helps with a claim)"**; **"What a claim costs you, by kind of loss"** with a hint for an amount or a range in words (**"$29-$199"**); one row each for **Cracked screen**, **Other damage**, **Lost**, **Stolen**, **Anything else**; **"Claims allowed in 12 months"**; **"A replacement is"** (Not stated / A new one / A refurbished one / The same model or an equivalent); and **"How fast, in the plan's words"**.

**58-save Pass.** After save, plan **UAT P58 Device Care** (`/plans/01a1c763-e8b9-7ee8-b83b-857beb3fef88`) shows a **"Phone or device insurance"** card (`s58-A-device-card.png`):

> Phone or device insurance
> IMEI or serial / UAT-P58-SERIAL-001
> Claims allowed / Up to 2 in 12 months
> A replacement is / A refurbished one · Within 2 business days
> What a claim costs you
> Cracked screen: $29-$199
> Other damage: $99.00
> Stolen: $199.00

Lost and Anything else (left empty) do not appear. Edit kept the section open with those values (`s58-A-edit-values.png`).

**58-empty Pass.** Only the three filled loss rows showed on the card. After unticking **"This protects a phone or other device"** and saving, the view has no device card and no serial; Edit has the checkbox off and the fields hidden (`s58-A-cleared.png`). Read-only SQL: `warranty_plans` `01a1c763-e8b9-7ee8-b83b-857beb3fef88` has `device_identifier`, `deductibles_json`, `claim_cap`, `replacement_kind`, and `replacement_time` all **null**.

**58-bad Pass** (duplicate **N/A** in the UI). The Lost amount (min=0) and range accepted typing `-10` / `-$10`; **Save** was refused with **"A deductible is an amount of zero or more."** (`s58-A-negative.png`). The notes say the form's inputs stop a negative amount and the API checks too; refusal on Save is enough for Pass. Duplicate kinds: the form has exactly one fixed row per kind, with no add-row or kind picker, so two rows of the same kind cannot be created in the UI. That sub-check is **N/A** here. The notes also say "the API checks too"; the API path was not tried.

### Part 2 — what it covers, line by line

**58-card Pass.** **UAT P58 Home Care** (`/plans/01a1c766-d0aa-77b4-9d31-0e7b58326814`; American Home Shield, covers the Dishwasher; no plan-decision box) shows **"What it covers, line by line"** with **Add a line**, the appliances-and-systems blurb, and **"Nothing listed yet."** (`s58-B-empty-card.png`). The same card also appears on UAT P58 Device Care and on Tread Masters road hazard protection (every plan). Note: the blurb is home-warranty wording even on a phone-insurance plan.

**58-noname Pass.** Saving a line with a blank name shows **"Say what it is, for example Refrigerator or Heating system."** (`s58-B-no-name.png`). The line was not kept.

**58-heat Pass.** **"Heating system [System] / about 8 years old (your estimate) · limit $5,000.00"** with no item (`s58-B-heating.png`). No suggestion list appeared while typing "Heating".

**58-dish Pass (display) / 58-agelimit Pass.** Linked to UAT P58 Dishwasher (bought Nov 10, 2018), with a typed estimate of 3 and a contract age limit of 5 (`s58-B-dishwasher.png`):

> Dishwasher [Appliance] / about 8 years old (from your purchase date) · limit $1,000.00 · UAT P58 Dishwasher
> This is older than the contract's age limit of 5 years, so the contract may not cover it. Check the contract's words.

The line stayed. The Add form still showed the estimate field after the item was picked (that is how 3 was typed). The card correctly ignored 3 for display.

**58-change Fail (Medium, Needs CC).** The notes say: **"Change opens the line (an item-linked line shows no estimate)"**. Change on the Dishwasher line opened **"Change this line"** with the item, limit 1000, and age limit 5, but **"About how old, in years"** was still shown (empty) (`s58-B-change.png`). Cancelled; the line was not edited. The card already shows the purchase-date age, so this is not a display miss — the form still offers an estimate the notes say should be absent, and that is how a stale estimate can be stored (see 58-export and the SQL below).

**58-leftout Pass.** Ice maker is struck through: **"[Add-on] Left out of your contract"** / "age not known" (`s58-B-leftout.png`).

**Remove (B7) Pass.** Remove opened **"Remove this line?"** / **"Ice maker is taken off what this plan lists. The plan and your items are not changed."** with Cancel and Remove (`s58-B-remove-ask.png`). **Cancel** was clicked; no line was actually removed. (Two earlier script clicks on Remove appeared to do nothing because the modal sits outside `<main>`.)

**58-export Partial (Medium, Needs CC).** Settings > Privacy & data > Prepare my download produced `warrantycat-export-2026-11-10.zip`. `plan_lines.csv` is in the zip. README.txt lists it: **"plan_lines.csv          what each plan covers, line by line: appliances, systems and add-ons, with limits, age limits and exclusions"**. Header: `plan,kind,covers,brand,model,age years,limit,limit in the contract's words,age limit years,exclusions,linked item,left out of my contract`. Rows:

```
UAT P58 Home Care,system,Heating system,,,8,5000.00,,,,,no
UAT P58 Home Care,appliance,Dishwasher,,,3,1000.00,,5,,UAT P58 Dishwasher,no
UAT P58 Home Care,addon,Ice maker,,,,,,,,,yes
```

The notes say a linked item **"shows 'about N years old (from your purchase date)'; the estimate you typed is ignored."** The card shows about **8** years from the 2018-11-10 purchase date, but the export writes **age years 3** — the typed estimate. Read-only SQL confirms the Dishwasher `plan_lines` row stores **`age_years` = 3** alongside **`item_id` = `01a1c762-732a-795d-956c-731f650617ba`**. The estimate was not ignored in the database or the export. The presence of the file and the README line would otherwise be a Pass.

### Push 57 Lows

**58-dot Pass.** Best Buy's **UAT P57 Best Buy Care** line is **"claims go to UAT P54 Shared Claims Co"** with **no leading "· "** (`s58-A-bestbuy-line.png`). **UAT P54 Care Unused** shows **"Not checked yet"** and **no** details line (`s58-A-care-unused.png`).

**58-link Pass.** From Admin > Shared data > UAT P54 Shared Care Co, **"Add or confirm plan types"** goes to `/admin/companies?type=plans&party=01a1c677-dc79-7b44-aac8-dea0722b550a`. The page has Show = **"Everything"**, the text **"Showing the plan types of one company. Show every company"**, and only that company's types, confirmed or not: UAT P54 Care Basic (Confirmed · $99.00 a year · from 2026-11-10), UAT P54 Care Unconfirmed (Not confirmed yet), UAT P54 Care Unused (Not confirmed yet) (`s58-A-company-filter.png`).

## Needs code / product follow-up

1. **Medium, Needs CC (58-change):** Change on an item-linked line still shows **"About how old, in years"**. The notes require **"an item-linked line shows no estimate"**.
2. **Medium, Needs CC (58-export / stored estimate):** For a linked Dishwasher, `plan_lines.age_years` is **3** (the typed estimate) even though the UI shows **"about 8 years old (from your purchase date)"**. The export writes that 3. The estimate should be ignored when an item supplies the age — not stored or exported.

## Test data created

- Item **UAT P58 Dishwasher** — https://stuffit-ui.onrender.com/items/01a1c762-732a-795d-956c-731f650617ba (bought Nov 10, 2018)
- Item **UAT P58 iPhone 16** — https://stuffit-ui.onrender.com/items/01a1c762-9a10-729f-a1d6-c1b0a2004507 (bought Nov 10, 2026)
- Plan **UAT P58 Device Care** (Asurion) — https://stuffit-ui.onrender.com/plans/01a1c763-e8b9-7ee8-b83b-857beb3fef88 (device details cleared after the untick)
- Plan **UAT P58 Home Care** (American Home Shield) — https://stuffit-ui.onrender.com/plans/01a1c766-d0aa-77b4-9d31-0e7b58326814, with three lines: Heating system (`01a1c767-4855-72f9-ae90-565bac16d257`, `age_years` 8, no item), Dishwasher (`01a1c767-97ed-7e29-bdb0-039a9c614d43`, `age_years` 3, `item_id` the dishwasher, `age_limit_years` 5), Ice maker (`01a1c768-1077-7316-9f97-62a34d0a2319`, `excluded` true)

No QA fixture files were made for the share.

## Evidence

- `/workspace/uat/push58/p58-A-notes.md`, `/workspace/uat/push58/p58-B-notes.md`, `/workspace/uat/push58/TESTPLAN.md`
- `/workspace/uat/push58/CHANGES-push-58-device-insurance-and-plan-lines.md`
- Screenshots under `/workspace/uat/push58/shots/`
- Export: `/workspace/uat/push58/export/warrantycat-export-2026-11-10.zip` (`plan_lines.csv`, `README.txt`)
- Neon read-only: `plan_lines` for Home Care; `warranty_plans` device columns for Device Care
