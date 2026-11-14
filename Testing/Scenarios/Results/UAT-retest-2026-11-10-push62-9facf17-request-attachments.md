# UAT retest — Push 62: photos and papers on a service request (Nov 10, 2026)

- **Build:** API 9facf17, started 10:58:03 PM ET. UI ~10:56 PM ET. Staging. API and UI. **No migration** (notes: a new kind of document owner only). Read-only Neon `__EFMigrationsHistory` newest row was still `20261110224129_PlanTypeLines`.
- **Source:** CHANGES-push-62-request-attachments.md (SHA256 `306718130f929b5bb292a53bef6c6f21788b5ca589d245e682ac0c7c8628167a`); TESTPLAN.md; p62-A-notes.md; p62-B-notes.md; p62-db-notes.md; export `/workspace/uat/push62/warrantycat-export-2026-11-11.zip`.
- **Accounts:** P34 Self personal (vault 3550464) for attach / view / remove / type refusal / cascade / export; Bob (vault 2453777) for isolation. Brief A saw **"A new version of WarrantyCat is ready"** and clicked Reload, then a hard reload. Brief B had no banner; a hard reload was still done. Clock Offset 0 (never moved; confirmed after the run, app time 11:46:29 PM ET Nov 10).
- **Not reported:** items marked **Not built yet** (Money recovered, denial wizard, phone-insurance cost view, three-layer explanation, person-added plan types, receipt-to-type matching, seeded providers). Attaching a file to another plan's request is **N/A** in the UI (each "Attach a photo or paper" only targets that request) and is not counted as a row.

## Results

| Result | Count |
|---|---|
| Pass | 8 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |

Plus **2 Lows, Needs CC:** the delete-request dialog still says **"Nothing else changes"** though the request's files are deleted; export path `<id>` values are 8-character prefixes (and the file name is also prefixed with that id). A5/A6 were Partial in the browser only because a bare tab to `/api/documents/…/content` returns 401 even for the owner (the app uses a header token, not a cookie). Read-only SQL and Bob's authenticated fetch resolve those to **Pass**. Storage blobs were not inspected; only `documents` rows were.

## Per-step results

| # | Check | Result |
|---|---|---|
| 62-attach | Attach one or several files; listed with sizes | **Pass** |
| 62-view | View opens the file in a new tab | **Pass** |
| 62-txt | `.txt` refused with the exact message | **Pass** |
| 62-remove | Remove asks first, then the file is gone | **Pass** |
| 62-cascade-req | Deleting a request deletes its files | **Pass** (Low: dialog wording) |
| 62-cascade-plan | Deleting a plan deletes its files | **Pass** |
| 62-isolate | Another account cannot open the file | **Pass** |
| 62-export | Export zip has the request files under `files/plans/…/requests/…` | **Pass** (Low: 8-char ids) |

**62-attach Pass.** On **UAT P62 Attach Care**, request **Leaking seal** (Nov 10, 2026, Waiting to hear), **"Attach a photo or paper"** accepted several files at once. The picker offers `image/*,application/pdf,.heic`. All five allowed fixtures were attached and listed with sizes (`s62-A-attached.png`):

> uat-p62-broken-part.jpg (5 KB) View Remove
> uat-p62-photo-2.jpg (4 KB) View Remove
> uat-p62-part.png (1 KB) View Remove
> uat-p62-photo.jpg (4 KB) View Remove
> uat-p62-receipt.pdf (570 B) View Remove

**Observation only:** the WebP uploaded as `uat-p62-photo.webp` is listed and stored as **`uat-p62-photo.jpg`**. JPEG sizes are smaller than the originals on disk (the app recompresses them). Neon confirms `original_size_bytes` 8158/7812/1086 vs stored 5039/4547/3614.

**62-view Pass.** **View** on `uat-p62-receipt.pdf` opened a new tab showing the PDF (`s62-A-view.png`). The tab address is a **`blob:`** URL (`blob:https://stuffit-ui.onrender.com/…`), valid only in that session. The underlying request is `https://stuffit-ui.onrender.com/api/documents/01a1c8e4-7141-7379-9c8e-cdc6ef38373d/content`. Opening that URL in a plain tab, even while signed in, returns **401**, because the app sends a token header and does not use a cookie. Isolation was therefore checked with an authenticated fetch (62-isolate).

**62-txt Pass.** Attaching `uat-p62-notes.txt` was refused with **"Use a PDF, JPEG, PNG, WebP or HEIC file."** Nothing new was attached (`s62-A-txt-refused.png`).

**62-remove Pass.** Remove on `uat-p62-part.png` asked first: **"Remove this file? / uat-p62-part.png is removed from this request. This cannot be undone. / Cancel | Remove file"** (`s62-A-remove-ask.png`). After confirm, the PNG was gone and the other four stayed (`s62-A-removed.png`). Neon: no `documents` row remains with `file_name = 'uat-p62-part.png'` (hard delete; there is no soft-delete column).

**62-cascade-req Pass.** A second request **"Request to delete"** on Attach Care, with `uat-p62-part.png`, was removed (`s62-A-request-deleted.png`). Dialog: **"Remove this request? / Request to delete is taken off the record. Nothing else changes."** The request disappeared; Leaking seal was left intact. Neon: no `plan_service_requests` row for "Request to delete", and no `documents` row for `01a1c8e5-5d82-728e-9299-73aecb5e2c29`. The file is also absent from the export. **Low, Needs CC:** the dialog still says **"is taken off the record. Nothing else changes"** even though the request's files are deleted; it should mention the files.

**62-cascade-plan Pass.** **UAT P62 Delete Plan Care** (`01a1c8e5-e590-7402-a32b-e425ccfbda9f`) with request **"Plan to delete"** and `uat-p62-broken-part.jpg` was deleted. The dialog mentions contract files: **"This removes UAT P62 Delete Plan Care, its contract files and the plan coverage on 0 items. The items themselves stay."** The plan URL then showed **"Not found."** (`s62-A-plan-deleted.png`). Neon: no `warranty_plans` row, no "Plan to delete" request, and no `documents` row for `01a1c8e5-fc0a-794e-9311-568dc30fdb5a`. The file is absent from the export. Storage blobs were not inspected, only the database rows.

**62-isolate Pass.** Bob opening P34 Self's Attach Care plan gets **"Not found."** (`s62-B-plan.png`). An authenticated GET of `/api/documents/01a1c8e4-7141-7379-9c8e-cdc6ef38373d/content` returns **404** for Bob and **200** for P34 Self (`s62-B-fetch.png`, `s62-B-owner-fetch.png`). (The fetch reused the app's own signed-in request; no token was copied or recorded.)

**62-export Pass (Low, Needs CC).** Settings > Privacy & data > Prepare my download produced `/workspace/uat/push62/warrantycat-export-2026-11-11.zip` (UTC date in the filename). It contains the four remaining Leaking seal files and not the removed PNG or the deleted request/plan files. The notes promise:

`files/plans/<plan name>_<id>/requests/<date>_<what broke>_<id>/<file>`

The zip has:

```
files/plans/UAT P62 Attach Care_01a1c8e4/requests/2026-11-10_Leaking seal_01a1c8e4/01a1c8e4_uat-p62-broken-part.jpg
files/plans/UAT P62 Attach Care_01a1c8e4/requests/2026-11-10_Leaking seal_01a1c8e4/01a1c8e4_uat-p62-photo-2.jpg
files/plans/UAT P62 Attach Care_01a1c8e4/requests/2026-11-10_Leaking seal_01a1c8e4/01a1c8e4_uat-p62-photo.jpg
files/plans/UAT P62 Attach Care_01a1c8e4/requests/2026-11-10_Leaking seal_01a1c8e4/01a1c8e4_uat-p62-receipt.pdf
```

The folder shape matches (`files/plans/…/requests/…`, plan name, date, what broke). It does **not** match the notes in two ways: every `<id>` is an **8-character prefix**, not the full uuid, and the file name is `<8-char-id>_<file>` rather than the bare `<file>`. Because these ULID-style ids were minted together, the plan (`01a1c8e4-282f-…`), the request (`01a1c8e4-4b02-…`), and the files (receipt `01a1c8e4-7141-…`) all share the prefix **`01a1c8e4`**, so the path does not tell those items apart. `plan_service_requests.csv` has the Leaking seal row only.

## Needs code / product follow-up

1. **Low, Needs CC:** the delete-request confirm still says **"Request to delete is taken off the record. Nothing else changes."** The files are deleted; the wording should say so.
2. **Low, Needs CC:** export path ids are 8-character prefixes, and the file name is also prefixed with that id. The notes describe `<id>` and a bare `<file>`. The shared `01a1c8e4` prefix on plan, request, and files does not distinguish them.

## Fixtures

Created for this run and copied to `\\DESKTOP-TD3DQ64\Stuffit\Testing\SampleData\push62-attachments\` (SHA256 verified against the box copies). The computerUse picker used `/workspace/uat/push62/fixtures/`. No HEIC (no writer on the box). The notes do not name a size limit, so no oversized file was made.

| File | SHA256 | Size |
|---|---|---|
| uat-p62-broken-part.jpg | `6419225d5685d0f1d823491493a8db55e821c2c6328ef565d96192e64ce52121` | 8158 |
| uat-p62-photo-2.jpg | `8d6005718a891338075121a6e857acad4e6ec8db0f32dcaf222cc350f40931e7` | 7812 |
| uat-p62-part.png | `abce5b9e4f4de4713e800289cf004237aba18f16d7a67622a1f41ea3a13b2318` | 2535 |
| uat-p62-photo.webp | `73622d5166c13a473bd5d093967aad355d57f1d90d925768edaf6167ac6f6837` | 1086 |
| uat-p62-receipt.pdf | `fb563b7b87e878d6b0ceb8d5031ac90844f32cefa6e726659258171099ea5194` | 570 |
| uat-p62-notes.txt | `f905e8154d5af5fc0d1336302fae8c8a15cd7a905053d6f709b1387545ab94eb` | 42 |

## Test data

Left in place:

- Plan **UAT P62 Attach Care** — https://stuffit-ui.onrender.com/plans/01a1c8e4-282f-7ba1-8c38-a40a41baab80
- Request **Leaking seal** — `01a1c8e4-4b02-7379-a459-739f7e391a70`, with four remaining `documents` (`owner_type = PlanRequest`, `type = Claim`): `uat-p62-broken-part.jpg` (`01a1c8e4-657a-…`), `uat-p62-photo-2.jpg` (`01a1c8e4-6a55-…`), `uat-p62-photo.jpg` (`01a1c8e4-6e26-…`, the WebP stored as JPEG), `uat-p62-receipt.pdf` (`01a1c8e4-7141-7379-9c8e-cdc6ef38373d`)

Removed during the run (hard-deleted in Neon; not in the export):

- PNG `uat-p62-part.png` removed from Leaking seal
- Request **"Request to delete"** and document `01a1c8e5-5d82-728e-9299-73aecb5e2c29`
- Plan **UAT P62 Delete Plan Care** `01a1c8e5-e590-7402-a32b-e425ccfbda9f`, request **"Plan to delete"**, and document `01a1c8e5-fc0a-794e-9311-568dc30fdb5a`

No P58–P61 plans or requests were modified. No QA scenario fixture files were added beyond the SampleData attachments folder above.

## Evidence

- `/workspace/uat/push62/p62-A-notes.md`, `/workspace/uat/push62/p62-B-notes.md`, `/workspace/uat/push62/p62-db-notes.md`, `/workspace/uat/push62/TESTPLAN.md`
- `/workspace/uat/push62/CHANGES-push-62-request-attachments.md`
- Screenshots under `/workspace/uat/push62/shots/`
- Export: `/workspace/uat/push62/warrantycat-export-2026-11-11.zip`
- Neon read-only: `documents` / `plan_service_requests` / `warranty_plans` for the remaining and deleted rows
