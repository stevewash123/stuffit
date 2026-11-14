# UAT retest — Push 63: Push 62 fixes, and asking for service from a line (Nov 11, 2026)

- **Build:** API `8f862a3`, started 10:12:38 AM ET. UI Last-Modified 10:11 AM ET (15:11:22 UTC). Staging. API and UI. **No migration** (notes: "No migration"). Read-only Neon `__EFMigrationsHistory` newest row remains `20261110224129_PlanTypeLines`. This retest ran at the end of the Scenarios 70–74 pass, on the same build (all browser work after 10:15 AM ET).
- **Source:** `CHANGES-push-63-push-62-fixes-and-ask-from-a-line.md` (SHA256 `4f6f20edd02d387ca64361f4ceb68300330bae058aa686ebbb3f4b5438e5424b`), written in Bot Rules at 10:10:30 AM ET. Notes: `/workspace/uat/scen70-74/p63-notes.md`. Screenshots: `s63-01`–`s63-04` in `/workspace/uat/scen70-74/shots/`. Export: `/workspace/uat/scen70-74/p63-export.zip` (777,919 bytes).
- **Account:** P34 Self personal (`vault_3550464_*`). Clock Offset 0 (not moved in this retest; confirmed after the 70–74 run, 11:29:14 AM ET). No new-version banner; a hard reload was done.
- **Not reported:** the same "Not built yet" list as push 62 (joining requests to Money recovered; claim wizard on a denial; phone-insurance cost view; three-layer explanation; a person adding their own plan type; receipt-to-plan-type matching; a seeded provider list).

## Results

| Result | Count |
|---|---|
| Pass | 3 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |

## Per-step results

| # | Check | Result |
|---|---|---|
| 63-dialog | Delete-request dialog mentions the files | **Pass** |
| 63-export | Export ids are the last 8 characters; plan, request, and file prefixes differ | **Pass** |
| 63-ask | Ask for service from a covered line; excluded lines have no button; pressing again resets the form | **Pass** |

**63-dialog Pass.** On **UAT P62 Attach Care**, a request **"UAT P63 delete me"** (Nov 11, 2026) was recorded and `01-receipt-amazon-instant-pot-duo.pdf` (83 KB, the Scenario 72 fixture, reused — QA made no new fixture) was attached. Remove asked:

> Remove this request?
> UAT P63 delete me is taken off the record, along with any photos and papers attached to it. The plan itself stays.
> [Cancel] [Remove]

That matches the notes wording. After Remove, only **Leaking seal** (4 files) remained; "1 request this plan year." Shot `s63-01-delete-dialog.png`.

**63-export Pass.** Settings > Privacy & data > Prepare my download produced a zip ready until Nov 18, 2026, saved as `p63-export.zip` (777,919 bytes). Plan folder **`UAT P62 Attach Care_41baab80`** is the last 8 of plan id `…a40a41baab80`. Request folder **`2026-11-10_Leaking seal_7e391a70`**. File prefixes **`cc8683bb`**, **`8eaf2851`**, **`11b48025`**, **`ef38373d`** all differ. The deleted "UAT P63 delete me" request is absent, as expected. This is the push 62 Low (first-8 id collision) marked fixed.

**63-ask Pass.** On **UAT P58 Home Care**, "What it covers, line by line": Heating system, Dishwasher (UAT P58 Dishwasher), and Refrigerator (UAT P60 Samsung refrigerator) each have **Ask for service**. **Ice maker** is struck through, "Left out of your contract", and has only Change / Remove — **no Ask for service**. Ask for service on Dishwasher scrolled to "Record a request" with line = Dishwasher and item = UAT P58 Dishwasher already chosen. After typing "typed junk" and fee 12, Ask for service on Heating system **reset** the form (What broke empty, fee empty, line = Heating system, item = None — no linked item). The form was cancelled; nothing was submitted. Shots `s63-02-lines.png`, `s63-03-ask-dishwasher.png`, `s63-04-ask-heating-reset.png`.

## Fixtures used

QA made **no new fixtures**. The only file attached in this retest was the existing Scenario 72 receipt `01-receipt-amazon-instant-pot-duo.pdf`, used temporarily on the request that was then removed.

## Data left

**UAT P62 Attach Care** (Leaking seal and its four files) and **UAT P58 Home Care** were not deleted. The temporary "UAT P63 delete me" request was removed. P34 Self's earlier P58–P62 plans remain. Clock Offset 0.
