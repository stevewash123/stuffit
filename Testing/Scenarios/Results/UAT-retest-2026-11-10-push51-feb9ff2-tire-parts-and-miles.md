# UAT retest — Push 51: tire parts and miles (Nov 10, 2026)

- **Build:** API feb9ff2, started 7:08:04 AM ET. UI unchanged since 12:36 AM ET (push 49 env-var rebuild). API only; no migration.
- **Source:** CHANGES-push-51-tire-parts-and-miles-2026-11-10.md (SHA256 `7ce9d75bb38eba8fef5617530a48d1d987856252d02266c320cb55f817c73062`); TESTPLAN.md; p51-findings.md.
- **Account:** P34 Self personal (vault 3550464). Already signed in; no new-version banner. Alice still has only the P34-Alice Repairs business space (flagged again). No Alice reset. Clock Offset 0 (never moved; confirmed after the run).
- **Vehicles:** existing UAT S69 Ford F-150 + tire part, Subaru Outback, Hyundai Tucson.
- **Fixtures:** none new. Re-read Scenario 69 files already on the items (`/workspace/uat/scen69/`). After a mistaken Home upload (see method note), nothing further was uploaded.
- **Not reported (per notes):** decided end-date/badge behavior; stale wording on already-saved entries; Maintenance on parts; missing 06 wiper row as a *new* defect (wipers did appear this run); order 08 N-line; un-keeping a job.

## Results

| Result | Count |
|---|---|
| Pass | 8 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |

The two Scenario 69 High findings (tire-part terms unused; jobs past a mile limit pinned to coverage) look **resolved**. Two Lows, below.

## Per-step results

| # | Check | Result |
|---|---|---|
| 51-05 | Order 05 new tires read as a service order, not a purchase card | **Pass** |
| 51-06 | Rotation on Michelin; flat repair on road hazard, repaired under warranty $0; wipers left out | **Pass** |
| 51-06d | Picker lists tire terms beside the truck's | **Pass** |
| 51-03 | Recall 25S99 kept, no coverage named | **Pass** |
| 51-12 | Order 12 at 41,120 mi still on powertrain (to Nov 20, 2026) | **Pass** |
| 51-07 | Order 07 at 61,240 mi goodwill CVT kept with no coverage | **Pass** |
| 51-end | New labels use "Powertrain (to Nov 20, 2026)", not Oct 14 or Nov 8 | **Pass** |
| 51-09 | Campaign 9ZZ still on powertrain (to Apr 5, 2035) | **Pass** |

### Method note (not a defect)

The first try uploaded 05 from **Home** by mistake (Re-read is in item Edit mode). That path showed a **purchase form** and created two stray New Items (Tire $1,159.96, Four-wheel alignment $129.99), both dismissed (`s51-05-card-home-upload-purchase.png`). Home upload is a different path. After that, each order used **Read it** in Edit mode on the existing files.

### Details

**51-05 Pass.** Edit-mode Read it on the F-150: **"Service on covered parts"** — not a Brand/Date Conflict purchase card. Header: **Jul 22, 2025 · 26,310 miles · Tread Masters Store #08 · order 08-552190**. Kept: four Michelin tires $1,159.96 on **Michelin warranty (to Jul 22, 2031)**; mount/balance $100 Michelin; TPMS kit $27.96 Bumper-to-bumper (to Jun 10, 2026); road hazard 36 mo $128 **Tread Masters road hazard protection (to Jul 22, 2028)**; disposal $14 Michelin. Left out: alignment $129.99, shop supplies $9.95. Added. (`s51-05-card.png`, `s51-05-hist.png`)

**51-06 / 51-06d Pass.** Header: **Feb 11, 2026 · 31,890 miles · order 08-561077**. Rotation $0.00 on **Michelin warranty (to Jul 22, 2031)**. Flat repair **repaired under warranty** on **Tread Masters road hazard protection (to Jul 22, 2028)** (row shows **no amount**, not $0 — Low). Wipers $49.98 **left out**. Picker: **No coverage (history only)**, **Bumper-to-bumper (to Jun 10, 2026)**, **Powertrain (to Jun 10, 2028)**, **Michelin warranty (to Jul 22, 2031)**, **Tread Masters road hazard protection (to Jul 22, 2028)**. Added. (`s51-06-card.png`, `s51-06-picker.png`, `s51-06-hist.png`)

**51-03 Pass.** **Jan 15, 2026** (close date) · 31,207 miles · Granite Ridge Ford · 6650291. Recall 25S99 **repaired under warranty**, **no coverage named** (previously Manufacturer warranty to Jun 10, 2026). Pinion seal **Powertrain (to Jun 10, 2028)**; seat heater **Bumper-to-bumper (to Jun 10, 2026)**. MPI left out. Added. (`s51-03-card.png`, `s51-03-hist.png`)

**51-12 Pass.** **Apr 9, 2025 · 41,120 miles · Hillside Garage & A/C · HG-24518**. CVT fluid $282.00 and rear diff $89.50 on **Powertrain (to Nov 20, 2026)**. Left out: A/C $223.95, headlamp $43.99, inspection $18.50, supplies $10. Re-read **removed** the old wrongly kept A/C row. (`s51-12-card.png`, `s51-12-hist.png`)

**51-07 Pass.** **Oct 15, 2026** (close) · 61,240 miles · Lakeside Subaru · 77031. Goodwill CVT valve body **repaired under warranty**, **no coverage**, no amount shown. Left out: spark plugs $294.20, brake fluid $131.85, MPI, supplies $16, hazmat $4.50. Picker: No coverage; **Bumper-to-bumper (to Nov 20, 2024)**; **Powertrain (to Nov 20, 2026)**. Old spark-plug and brake-fluid rows removed. (`s51-07-card.png`, `s51-07-picker.png`, `s51-07-hist.png`)

**51-end Pass.** New history and picker labels say **"Powertrain (to Nov 20, 2026)"**, not Oct 14 or Nov 8. Note only (decided, not graded): the policy panel still shows the powertrain as ended **Oct 14, 2026** by miles (61,240 on Oct 15), so the service label uses the paper's date limit while the panel shows the miles end. Older pre-push rows had said "Manufacturer warranty (to Nov 8, 2026)".

**51-09 Pass.** **Sep 16, 2026 · 19,880 miles · Seaport Hyundai · 5590184**. Campaign 9ZZ TCM on **Powertrain (to Apr 5, 2035)**; coolant hose also Powertrain (to Apr 5, 2035); liftgate strut **Bumper-to-bumper (to Apr 5, 2030)**. MPI left out. Re-read **removed** the three duplicate part-number rows from S69 (that S69 Partial now looks fixed). (`s51-09-card.png`, `s51-09-hist.png`)

Re-read replaced rule-kept rows; jobs now left out are no longer in history (expected).

### Lows

1. **Needs CC — re-add duplicates hand-added rows.** After adding the new 06 read, the earlier hand-added Feb 11 "added by you" rows (flat repair billed to RH plan $0.00, rotate & balance $0.00) stay beside the new rule-kept rows, so each job appears twice. That matches "jobs you added by hand stay", but it now duplicates once the rules keep the same jobs. (`s51-06-hist.png`)

2. **$0 / warranty jobs still show no amount** on the card or in history (order 06 flat repair, and the warranty rows on 03, 07, 09). Same Low as earlier pushes.

## Needs code / product follow-up

1. **Needs CC (Low):** when a re-read now keeps jobs that were previously added by hand, avoid leaving a duplicate "added by you" row beside the new rule-kept row (merge, or drop the hand-added copy when the rules now keep the same job).
2. Low (known): show $0 on repaired-under-warranty / plan-paid rows.
3. Reminder (plan, not this push): Alice still has no personal account, so Scenario 69 / these retests run as P34 Self.

## Evidence

- `/workspace/uat/push51/p51-findings.md`
- `/workspace/uat/push51/CHANGES-push-51-tire-parts-and-miles-2026-11-10.md`
- Screenshots under `/workspace/uat/push51/shots/`
