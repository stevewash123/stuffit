# UAT retest — Push 44: report-43 fixes (Nov 9, 2026)

- **Build:** API a4b6d4c, started 1:13:50 PM ET. UI ~1:12 PM ET. Staging. No migration.
- **Source:** CHANGES-push-44-report-43-fixes-2026-11-09.md; HANDOFF-push44-a4b6d4c-retest.txt; p44-ui-findings.md.
- **Account:** P34 Self personal (vault 3550464). Clock Offset 0.
- **Not changed (do not report as fails):** odometer-in 20,800 is correct; P41-3 powertrain narrative; Edit drawer no Cancel; Read it on Add-vehicle files; duplicate RO upload stored twice.

## Results

| Result | Count |
|---|---|
| Pass | 4 |
| Partial | 2 |
| Fail | 0 |
| Inconclusive | 0 |

## Per-step results

| # | Check | Result |
|---|---|---|
| 1 | Left-out line on S68-04 ("N other jobs were left out") | **Partial** |
| 2 | Coverage named with its end date | **Pass** |
| 3 | Coverage assignment (cooling → powertrain) | **Partial** |
| 4 | Two-tab reload race stays signed in | **Pass** |
| 5 | Back after sign-out → sign-in (no bfcache item) | **Pass** |
| 6 | Back after a failed sign-in → sign-in | **Pass** |

### Details

Item P44: https://stuffit-ui.onrender.com/items/01a1c197-bb1a-7b3e-b0a3-f0b3b91d72d8 (second tab used P43 item `01a1c149-…`).

**1 — Left-out line: Partial.** S68-04 shows **"2 other jobs were left out: not on a covered part."** The RO has **3** non-covered lines (cabin air filter \$48, 10k inspection \$0, shop supplies \$6.05). Notes example expects 3. Likely the \$0 inspection was dropped by the reader.

**2 — Coverage named with end date: Pass.** Lines show e.g. "Manufacturer warranty **(to Nov 8, 2029)**" / "(to Nov 8, 2027)" as appropriate. Service history list shows coverage per row.

**3 — Coverage assignment: Partial.** Oil/engine and CVT go to the 2029 powertrain term (correct). Water-pump assembly and coolant refill/bleed → 2029. **Coolant-seepage diagnosis → 2027** (bumper term) while the other cooling lines are on 2029; notes say cooling work goes to powertrain.

**4 — Two-tab race: Pass.** Three simultaneous double reloads (18:45:08, 18:45:41, 18:46:08Z) plus one ~+79s after fresh sign-in (18:48:09Z): both tabs stayed on their items. Render logs: all `/api/auth/refresh` during those reloads returned **200**; **no refresh 401** in the double-reload window.

**5 / 6 — Back after sign-out / failed sign-in: Pass.** Back 1–3 land on sign-in with no item details. Same after one failed login ("Invalid email or password."). Stale P43 tab reloads to /login.

### Low notes

- Order-number conflict: "You already have a purchase from this store with that order number." (P43 Honda already used the same order; expected).
- One `/login` at **18:46:28Z** between batch 3 and the fresh sign-in at 18:46:50Z — most likely the deliberate sign-out. No `/api/auth/refresh` call at that instant; next refresh activity is 18:47:00Z (200s). A lone refresh **401** at **18:48:59Z** is after the race checks (post-test).

### Render log check (StuffIt_API `srv-db9p27mq1p3s7392ovh0`, 18:44:30Z–18:49:00Z, refresh only)

| UTC | Outcome |
|---|---|
| 18:45:09 (×2) | refresh **200** / **200** |
| 18:45:41 (×2) | refresh **200** / **200** |
| 18:46:08 (×2) | refresh **200** / **200** |
| 18:46:28 | **no refresh** (UI /login — likely deliberate sign-out) |
| 18:47:00 (×2) | refresh **200** / **200** |
| 18:48:09 (×2) | refresh **200** / **200** |
| 18:48:59 | refresh **401** (after tests) |

No refresh 401 during the double-reload batches.

## Needs code changes

1. Left-out count on S68-04 should include all non-covered lines (2 vs 3).
2. Coolant-seepage diagnosis should assign to the powertrain term (2029), not bumper (2027), with the other cooling lines.

## Evidence

- /workspace/uat/p44-ui-findings.md
- /workspace/uat/push44/CHANGES-push-44-report-43-fixes-2026-11-09.md
- Screenshots under /workspace/uat/s67-68/screenshots/ (p44-service-history.png, etc.)
