# UAT retest: Push 29 — unused hand-made policy notice (S3.2.13)

**Test date:** Friday **Nov 6, 2026** (~2:48 PM–~3:27 PM ET).  
**Live build under test:** API **`6503be1`**, UI **`4b6f46d`**.  
**API `/api/version`:** `commit=6503be1`, `startedAt=2026-11-06T17:45:25.5971589+00:00` → **12:45:25 PM ET** Nov 6, Staging.  
**UI proof:** Notifications page shows **Delete it** / **Keep it** on unused-policy notices; SPA Last-Modified **12:44:21 PM ET**; bundle `main-3AL2TJP7.js`.  
**Migration:** `20261106165951_UnusedPolicyNotice` applied (`unused_notice_dismissed_at` on manufacturer/seller policies).

**Notes:** `CHANGES-push-29-unused-hand-made-policy-notice-2026-11-06.md`  
**Mode:** Targeted S3.2.13 only. Alice account-scoped `run-reminders` + simulated clock (always restored to **offset 0**). Bob UI isolation Batch D. **No** scenario reset, orphan purge, unscoped sweeps, or Push26–28 re-grades.

**Steve approvals used:** Push29 account-scoped reminder checks may send test emails to Alice and Bob if needed (answered ~2:55 PM ET).

**Evidence (box):**  
- Prep: `/workspace/uat/push29-prep/` (prep-brief, readiness, keep/delete/in-use/waiting/bob UI md + screenshots)  
- DB Stager work: `/workspace/work/push29/` (clock/reminder raw txt + phase md)  
- Notes: `/workspace/uat/bot-rules/CHANGES-push-29-unused-hand-made-policy-notice-2026-11-06.md`

## Headline

On API **`6503be1`** + UI **`4b6f46d`**, S3.2.13 unused hand-made maker-policy notices behave as specified for Alice: young sweep creates **no** notice; aged (+8d) creates **one** per unused Manual policy; same-day dedup creates **none**; **Keep it** sets `unused_notice_dismissed_at` and never asks again; **Delete it** retires the policy (`effective_to` yesterday) and the private 12-mo term is no longer offered; maker+category+term **match** counts as in-use without `source_policy_id`; a waiting notice is **Cancelled** when the policy becomes used again. Bob Notifications UI shows **no** Alice unused notices and Alice’s D2 item URL is **Not found** under Bob → UI visibility + item isolation **Pass**; cross-account notice-action API remains **untested** → overall isolation **Partial**. Final clock **offset 0**.

## Totals (graded rows only)

| Check | Result |
|---|---|
| S3.2.13 young sweep (<7d) — no unused-policy notice | **Pass** |
| S3.2.13 aged (+8d) sweep — one Info-needed notice + Delete it / Keep it | **Pass** |
| S3.2.13 same-day dedup — no second notice | **Pass** |
| S3.2.13 Keep it → dismissed; later aged sweep never again | **Pass** |
| S3.2.13 Delete it → policy retired; private 12-mo not offered | **Pass** |
| S3.2.13 in-use by maker/category/term match → no unused notice | **Pass** |
| S3.2.13 waiting notice cancelled when policy reused | **Pass** (DB authoritative; see caveat) |
| S3.2.13 Bob UI: no Alice unused notices; Alice item Not found | **Pass** (UI visibility + item isolation) |
| S3.2.13 Bob cannot Keep/Delete Alice notice via API | **Not run** (cross-account action API untested) |
| S3.2.13 overall Bob / Test2 isolation | **Partial** (UI Pass + action API Not run) |
| Clock restored to offset 0 at end of each clocked phase / final | **Pass** |

**Summary counts (rows above):** **8 Pass**, **1 Partial**, **0 Fail**, **0 Blocked**, **1 Not run**.

---

## Environment

- App: https://stuffit-ui.onrender.com  
- Alice account: `01a1a9d3-e107-73d3-9979-d7f7cd5c2505` (user `01a1a9d3-e02d-774c-a364-a38e5851d8e1`)  
- Bob: vault login as **QA Test 2** / avatar **Q2** (one successful sign-in)  
- Maintenance: Alice-scoped `POST /api/maintenance/run-reminders?accountId=…` + `GET/POST /api/maintenance/clock*` (key not logged)  
- Prior P28 fixtures preserved (incl. Cove 24-mo Manual candidate)

---

## Fixtures created (Alice; prior data preserved)

| Fixture | Item ID | Policy / notice IDs | Outcome |
|---|---|---|---|
| P29 Keep A (Dyson / Vacuums / typed 12 mo; item deleted) | item `01a1b269-116a-73a2-898c-d9f0c273e815` (deleted) | policy **`01a1b269-f2dd-7ec8-92b7-f7792e1d3e83`**; notice **`01a1b26f-773f-79b1-bc78-cad96bd1f4d1`** | Keep path |
| P29 Delete B (Black+Decker / Power tools / typed 12; item deleted) | item `01a1b276-050a-7bd7-a97c-fb19d4abe5c3` (deleted) | policy **`01a1b277-70ec-7ac0-8628-78b3a43d011e`**; notice **`01a1b279-82fc-719a-aa68-caa966f5b448`** | Delete / retire path |
| P29 InUse C1 / C2 (DeWalt / Power tools / typed 12; both live) | C1 `01a1b27e-b0bc-7041-9683-796a5c984805`; C2 `01a1b280-10b7-76ac-988f-e74b8da1e6d2` | policy **`01a1b27f-845a-718a-96c0-744290c39d39`** (`source_policy_id` null on coverages) | In-use → no notice |
| P29 Waiting D1 (Ryobi / Power tools / typed 12; deleted) then D2 (live) | D1 `01a1b281-f954-7cd3-8b3b-eaeef299535e` (deleted); D2 `01a1b287-7021-799c-88ec-86e5b55fa03a` | policy **`01a1b282-a842-7e01-a7ca-e7f006c898d1`**; notice **`01a1b285-7bd0-72f4-ab7f-cd833af3400e`** | Waiting → cancel by reuse |
| Prior Cove 24 (preserved, not a P29 target) | — | policy `01a1b223-c653-7490-a6a8-8be0aa876e1e`; notice `01a1b26f-773f-702e-a997-7ad5a7c2de79` | Extra aged notice; left Pending |

Shared verified suggestions (Dyson 24, B+D 24, DeWalt 36, Ryobi 36) were left unchecked where noted.

---

## Grade detail

### 1. Young sweep — no notice — **Pass**

Clock offset **0**. Alice `run-reminders` HTTP 200: `UnusedPolicies = 0`. No Dyson unused notice created. Private Dyson12 Manual policy already unused after Keep-A item delete.  
Evidence: `/workspace/uat/push29-prep/young-aged-dedup-alice-2026-11-06.md`, `/workspace/work/push29/run-reminders-young-alice.txt`.

### 2. Aged (+8d) — one notice + UI buttons — **Pass**

`POST clock/advance?days=8` → offset 8. Alice `run-reminders` HTTP 200: `UnusedPolicies = 2` (Dyson12 **new** + prior Cove24). Dyson notice title/body match notes; type `purchase_needs_info`, `reference_type=unused-maker-policy`, Pending, email Sent. UI shows **Needs action**, **Unread**, **Delete it**, **Keep it**. Cove extra distinguished by policy_id — **not** a Dyson fail. Clock reset to **0** + independent GET.  
Evidence: young-aged-dedup md; keep-ui before screenshot.

### 3. Same-day dedup — **Pass**

Second Alice `run-reminders` at offset 8: `UnusedPolicies = 0`; still one notice each for Dyson and Cove.  
Evidence: young-aged-dedup md; `run-reminders-dedup-alice.txt`.

### 4. Keep it → never again — **Pass**

Browser clicked **Keep it** only on Dyson notice. DB: `unused_notice_dismissed_at = 2026-11-06 19:58:26.104601+00`; notice action_status=**Cancelled**, is_read=true. Cove left Pending. Later `advance?days=16` + Alice sweep: `UnusedPolicies = 0`; Dyson notice count 1→1 (no repeat). Unrelated `Sent = 1` Trailblaze warranty reminder at sim Nov 22 — ordinary reminder, not unused-policy. Clock restored **0**.  
Evidence: `keep-ui-2026-11-06.md`, `keep-never-again-alice-2026-11-06.md`.

### 5. Delete it → retire + no private offer — **Pass**

Fresh Black+Decker 12 fixture → delete item → +8 Alice sweep → notice `01a1b279-82fc-719a-aa68-caa966f5b448`. Browser **Delete it** only. DB: policy `effective_to = 2026-11-05` (retired yesterday vs real Nov 6); notice **Completed**/read=true by Alice at 3:09:01 PM ET. Fresh Add (unsaved): only shared Black+Decker **2 year** offered — **no** private 12-mo. Cove/Dyson preserved. Clock **0**.  
Evidence: `delete-fixture-*.md`, `delete-aged-alice-*.md`, `delete-ui-*.md`, `inuse-cancel-investigate-2026-11-06.md` §A.

### 6. In-use match (no notice) — **Pass**

Live C1+C2 DeWalt/Power tools typed 12 (`source_policy_id` null). After +8 Alice sweep: DeWalt unused notices **0→0**; `UnusedPolicies = 1` was the separate Ryobi waiting fixture only. Match by maker+category+term is sufficient; explicit `source_policy_id` not required. Clock **0**.  
Evidence: `inuse-waiting-fixtures-*.md`, `inuse-waiting-aged-alice-2026-11-06.md`.

### 7. Waiting notice cancelled on reuse — **Pass** (with documented discrepancy)

Pending Ryobi notice after D1 delete + aged sweep. Browser added live D2 Ryobi/Power tools typed 12 (match; `source_policy_id` null). Alice `run-reminders` at clock **0** HTTP 200: summary `Cancelled = 0`, `UnusedPolicies = 0`. **DB transition verified:** notice `01a1b285-7bd0-72f4-ab7f-cd833af3400e` Pending→**Cancelled**, is_read=**true**, action_completed_at=`2026-11-06T20:25:34.742Z`, completed_by=**null** (system); no new Ryobi notice; policy not retired.  

**Caveat / discrepancy:** `ReminderSendSummary.Cancelled` does **not** reflect unused-policy notice cancellations; DB `action_status` is authoritative for this grade. Do not treat summary `Cancelled=0` as a product Fail when the notice row cancelled. Clock remained **0** (no advance/reset needed).  
Evidence: `waiting-reuse-ui-2026-11-06.md`, `waiting-cancel-alice-2026-11-06.md`.

### 8. Bob / Test2 isolation — **Partial**

**UI visibility + item isolation — Pass:** One successful Bob login (QA Test 2 / Q2). Notifications empty of Alice Dyson/Cove/B+D/Ryobi unused notices. Opening Alice D2 URL `…/items/01a1b287-7021-799c-88ec-86e5b55fa03a` as Bob → **Not found.** No notice actions attempted.  
Evidence: `/workspace/uat/push29-prep/bob-isolation-ui-2026-11-06.md` (+ screenshots).

**Cross-account notice-action API — Not run:** No Bob-authenticated Keep/Delete (or equivalent API) against Alice’s notice IDs. Schema/docs/data also showed Bob unused-policy notice count 0 and no Alice notice/policy refs on Bob’s `account_id` (guardrail only; not runtime action proof).

**Overall isolation grade: Partial** (UI Pass + action API Not run). Not Fail / Not Blocked.

---

## Caveats (observed — not blanket Pass)

1. Aged Alice sweeps can emit **extra** unused notices for prior unused Manual policies (Cove24) and ordinary warranty reminders (`Sent>0` at advanced clock). Distinguish by policy_id / reference_type.  
2. Waiting-cancel: summary `Cancelled=0` vs DB `action_status=Cancelled` — document, do not false-fail.  
3. Push28 private typed-offer UI Fail on this same API commit is **out of scope**; creator typing + match-in-use path was used instead.  
4. Restricted maker policies may lean “in use” by maker+category+term only (notes: known not-a-bug) — not exercised.  
5. Store/seller Manual unused path — **Not run** (optional stretch).  
6. Bob cross-account **action** authorization — **Not run**.  
7. Final clock after all clocked phases: **offset 0** (independent GETs recorded per phase).

## Out of scope (not graded as Push29 new)

Full Scenario 62/54/61; Push26–28 Fixed rows; orphan purge; digest; export-expiry; Alice wipe; schema edits.

## Evidence index

| Phase | Paths |
|---|---|
| Prep / readiness | `push29-prep/prep-brief-2026-11-06.md`, `readiness-s3.2.13-2026-11-06.md` |
| Young / aged / dedup | `push29-prep/young-aged-dedup-alice-2026-11-06.md` + `work/push29/run-reminders-*-alice.txt`, `clock-*.txt` |
| Keep UI + never-again | `keep-ui-2026-11-06.md` (+png), `keep-never-again-alice-2026-11-06.md` |
| Delete fixture / aged / UI | `delete-fixture-2026-11-06.md`, `delete-aged-alice-2026-11-06.md`, `delete-ui-2026-11-06.md` |
| In-use / waiting | `inuse-waiting-fixtures-*.md`, `inuse-waiting-aged-alice-*.md`, `waiting-reuse-ui-*.md`, `waiting-cancel-alice-*.md` |
| Bob isolation | `bob-isolation-ui-2026-11-06.md` (+png) |

## Delivery

- Box working copy: `/workspace/uat/retest-6503be1/UAT-retest-2026-11-06-push29-unused-hand-made-policy-notice.md`  
- UNC Results: `\\DESKTOP-TD3DQ64\Stuffit\Testing\Scenarios\Results\UAT-retest-2026-11-06-push29-unused-hand-made-policy-notice.md`  
- Library: `uat-library/runs/` + INDEX entry  
