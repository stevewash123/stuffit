# UAT retest — Push 43: service history + sign-in investigation (Nov 9, 2026)

- **Build:** API e44da4e, started 11:46:28 AM ET. UI Last-Modified 11:45:16 AM ET. Staging. Migration ServiceEntries applied ~12:04 PM ET.
- **Source:** CHANGES-push-43-service-history-2026-11-09.md; HANDOFF-push43-e44da4e-retest.txt; p43-ui-findings.md; p43-signin-findings.md; NEXT-REPORT-ADDITIONS.md.
- **Account:** **P34 Self** personal (vault 3550464). Bob vault login (2453777) was not available to the browser subagent (tried twice); substitution noted.
- **Clock:** Offset 0 (no moves).
- **Skip / Not changed:** maintenance-due reminders; standalone RO; data-protection keys; **powertrain narrative (P41-3) carried forward, not reported as new**.

## Results

| Result | Count |
|---|---|
| Pass | 5 |
| Partial | 1 |
| Fail | 0 |
| Inconclusive | 0 |

Sign-in investigation is a separate section (not in the Pass/Partial counts above).

## Service history (S68 retest)

Item: https://stuffit-ui.onrender.com/items/01a1c149-a486-71fc-9ef1-9f848efde55f (fresh P43 CR-V). Setup: buyer's order + Honda warranty; B2B → 2027-11-08 / 36k; Powertrain → 2029-11-08 / 60k.

| # | Check | Result |
|---|---|---|
| 1 | S68 step 5 — three customer-pay ROs → service history | **Partial** |
| 2 | S68 step 6 — water-pump $0 RO → repaired under warranty | **Pass** |
| 3 | Live reader — all 4 orders recognised; no wrong jobs kept | **Pass** |
| 4 | Vehicle Service history list + delete in edit | **Pass** |
| 5 | Export `service_history.csv` | **Pass** |
| 6 | Re-add same order replaces entries / no second reading | **Pass** |

### Step details

**1 — S68 step 5: Partial.**
- S68-03 oil: kept under Manufacturer warranty; reading 3,200; PASS for that order.
- S68-04 oil+inspection: oil kept; cabin filter / inspection / shop supplies correctly **left out**, but **no "N other jobs were left out" line**.
- S68-05 CVT fluid: kept; PASS.
- Coverage on every kept line shows only **"Manufacturer warranty"** — never Powertrain or bumper-to-bumper (both Honda terms share that title).

**2 — S68 step 6: Pass.** Water pump at **20,800** miles; three lines "repaired under warranty"; no plan/claim/coverage change; factory ends unchanged. Re-add: "already in the service history… replaces"; still one reading set. **Note for CC:** PDF odometer in/out **20,800 / 20,802**; app consistently uses **odometer-in** (also 9,800/9,801 and 16,400/16,401 on other ROs). Notes expected 20,802 — confirm which is intended. Export has `customer_paid=0.00`.

**3 — Live reader: Pass.** All four ROs recognised as repair orders; no wrong jobs kept.

**4 — List + delete: Pass.** Newest-first list (6 rows before delete). Delete in edit removes the entry; RO stays attached; reading kept.

**5 — Export: Pass.** `service_history.csv` with columns id, item_id, vehicle, date, odometer, unit, order_number, shop, part, work, covered_by, warranty_repair, customer_paid.

**6 — Re-add: Pass.** Replaces prior entries; no duplicate reading. Low: PDF stored twice on re-upload.

---

## Sign-in redirect investigation

Testers: A = P34 Self (3550464), B = P34 Employee (3549233). Bob vault unavailable.

### Timeline (selected)

| UTC | ET | Event |
|---|---|---|
| 17:17:44 | 12:17:44 | Failed B login (wrong password once) → 401 |
| 17:17:59 / 17:18:28 | 12:17–12:18 | F5 on bfcache-stale A pages → /login (refresh 401) |
| 17:19:24 | 12:19:24 | Open A item URL while signed out → /login |
| 17:20:50 | 12:20:50 | Sign-in A |
| **17:22:05** | **12:22:05** | **Unexplained +75s F5 → /login** |
| 17:22:04.55 | | API: POST /api/auth/refresh → **200** |
| 17:22:04.69 | | API: POST /api/auth/refresh → **401** (~134 ms later) |
| 17:22:05.64 | | API: POST /api/auth/refresh → **401** |
| 17:33:03 | 12:33:03 | Two tabs F5 ~same time; tab 1 → /login |
| 17:33:03.63 | | API: refresh **200** |
| 17:33:03.64 | | API: refresh **401** (~17 ms later) |
| 17:33:06 | 12:33:06 | Second double reload; tab 2 → /login |
| 17:33:06.44 / .45 | | API: refresh **401**, **401** |
| 17:53:35 | 12:53:35 | 20-min idle then F5 — stayed signed in |

### Conclusions

1. **Steve's Back repro — Medium privacy (not a live session):** After sign-out, Back shows A's Home / Honda item / Edit drawer from the **bfcache**. F5 or direct URL while signed out goes to /login; no server data once signed out. Same without the failed login. Fix ideas: Cache-Control: no-store; pageshow(persisted) reload/clear; clear state + replace history on sign-out.
2. **Two-tab simultaneous reload — reproduced (Medium/High):** Both tabs end the session. Logs show refresh **200 then 401 within ~17 ms** (token rotation race). Needs **single-flight refresh** in the UI plus a **reuse grace window** on the API.
3. **One unexplained +75s redirect** after sign-in 17:20:50 → F5 17:22:05. Same 200→401 pair in logs. Not reproduced in the next two timing runs.
4. **User switch — Pass:** B opening A's item → Not found; B header correct.
5. **Idle — Pass:** 20+ min idle then F5 stayed signed in.

Render logs pulled for StuffIt_API `srv-db9p27mq1p3s7392ovh0`, 17:16Z–17:35Z (auth/refresh); no tokens printed.

---

## Needs code changes

1. **"N other jobs were left out"** missing when jobs are omitted (S68-04).
2. **Coverage name per job** — show Powertrain vs bumper-to-bumper (or distinct titles), not only "Manufacturer warranty".
3. **Odometer in vs out** — confirm whether history/reading should use 20,800 (in) or 20,802 (out).
4. **bfcache stale pages after sign-out** — Cache-Control: no-store / pageshow handler / clear state on sign-out.
5. **Single-flight token refresh + reuse grace window** (two-tab race).
6. **Unexplained +75s redirect** (same race pattern once).
7. **Low:** Edit drawer has no Cancel (only X).
8. **Low:** Read it doesn't auto-run on files attached in the Add a vehicle form.

Carried forward (not new): powertrain narrative (P41-3).

## Evidence

- /workspace/uat/p43-ui-findings.md
- /workspace/uat/p43-signin-findings.md
- Screenshots under /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/ (listed in findings)
- Export: /workspace/uat/export/ (from warrantycat-export zip)
