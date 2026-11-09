# UAT retest — Push 45: maintenance due (Nov 9, 2026)

- **Build:** API ef44688, started 3:02:38 PM ET. UI ~3:00 PM ET. Staging. Migration `MaintenanceRequirements` (applied on start). No seed.
- **Source:** CHANGES-push-45-maintenance-due-2026-11-09.md; HANDOFF-push45-ef44688-retest.txt; p45-ui-findings.md.
- **Account:** P34 Self personal (vault 3550464). Run ~3:38–4:05 PM ET. Clock Offset 0.
- **Item:** https://stuffit-ui.onrender.com/items/01a1c209-fcba-7030-b6e9-5d5fd70c94d0 (P45 Honda CR-V)
- **Not changed (do not report as fails):** SMS opt-in still to come; wording-mismatch matches; Edit drawer Cancel; Read it on Add-vehicle; P41-3 powertrain narrative.

## Results

| Result | Count |
|---|---|
| Pass | 9 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 2 |

## Per-step results

| # | Check | Result |
|---|---|---|
| 1 | S68-04 left-out count ("3 other jobs were left out") | **Pass** (push 44 Partial fixed) |
| 2 | Coolant seepage diagnosis → powertrain to Nov 8, 2029 | **Pass** (push 44 Partial fixed) |
| 3 | Maintenance due dates from service history (oil / trans / tire) | **Pass** |
| 4 | Delete a requirement sticks after reload | **Pass** |
| 5 | Re-read warranty keeps owner's own requirements; no duplicates | **Pass** |
| 6 | Panel shows only in edit mode on an empty vehicle | **Pass** |
| 7 | `maintenance.csv` in export with correct columns | **Pass** |
| 8 | "Maintenance due" notification preference (email+in-app on; text off) | **Pass** |
| 9 | Reader adds no requirement when S68 Honda paper states none (negative) | **Pass** |
| 10 | Positive path: paper that lists required maintenance | **Inconclusive** (needs fixture) |
| 11 | Reminder email / in-app when oil is overdue | **Inconclusive** (job timing not driven) |

### Details

**1 — Left-out count: Pass.** S68-04 card: **"3 other jobs were left out: not on a covered part."** (cabin air filter, 10k inspection, shop supplies). Push 44 Partial fixed.

**2 — Coolant assignment: Pass.** S68-06: coolant seepage diagnosis, water-pump assembly, and coolant refill/bleed all show **Manufacturer warranty (to Nov 8, 2029)** (powertrain). Push 44 Partial fixed.

**3 — Due dates from service history: Pass.**
- **Oil** (7,500 mi / 12 mo): **Overdue.** Exact reason: "Last done Aug 15, 2025 at 9,800 miles. Was due by Aug 15, 2026 or 17,300 miles, whichever comes first."
- **Transmission fluid** (30,000 mi / 36 mo): **On track.** Settled by Mar 20, 2026 CVT job at 16,400. "Next due by Mar 20, 2029 or 46,400 miles…"
- **Tire rotation** (7,500 mi / 6 mo): **Overdue.** No matching job; counted from coverage start with the 22-mile delivery reading: "Was due by May 8, 2025 or 7,522 miles…"

**4 — Delete sticks: Pass.** Tire rotation deleted; absent after reload. Screenshot: `/workspace/uat/s67-68/screenshots/p45-maintenance.webp`.

**5 — Re-read keeps owner's: Pass.** Warranty re-applied; oil and transmission stayed; no duplicates; tire rotation stayed deleted; still exactly two coverage rows.

**6 — Empty-vehicle panel: Pass.** Before any rules, Maintenance was hidden on the normal item view and appeared in edit mode. After rules were added, the panel was visible in normal view too (expected once requirements exist).

**7 — Export: Pass.** New ~75 KB ZIP includes `maintenance.csv` with columns `id,item_id,vehicle,task,every_distance,unit,every_months,from_warranty_paper`. Two rows (oil, transmission); both `from_warranty_paper=no`. Staged at `/tmp/p45x/maintenance.csv`.

**8 — Notification preference: Pass.** Settings → Notifications has **Maintenance due**; email and in-app checked by default; text coming soon / disabled.

**9 — Negative reader path: Pass.** S68 Honda warranty dialog showed bumper + powertrain only. No "It asks for N kinds of maintenance" line; no invented requirements. Apply text: "Applied to this item: 3 years from 2024-11-08, to 2027-11-08, and 1 parts with their own terms."

**10 — Positive reader path: Inconclusive / Needs fixture.** No fixture paper lists required maintenance, so the "It asks for N kinds…" path and auto-fill from paper were not exercised. **Suggest CC: new scenario warranty paper that states required maintenance** (e.g. oil every 7,500 / 12 months).

**11 — Reminders: Inconclusive.** Oil is overdue, but no Maintenance-due email or in-app notice appeared. The reminder job's "at the owner's local time" timing was not driven with the test clock in this run. **Suggest CC confirm when the job runs** (and optionally a clock-driven reminder retest).

### Low notes

- Buyer's-order order number → HTTP 409 ("You already have a purchase from this store with that order number.") — same fixture order reused; known. Store and total entered manually; order number not saved; payment blank.
- Synthetic fixture VIN `1UATHRW50S0000068` rejected as invalid and cleared — expected.

## Needs code / product follow-up

1. **New scenario paper (CC):** a warranty that lists required maintenance, so the positive reader path can be UAT'd.
2. **Reminder job timing (CC):** confirm when Maintenance-due email / in-app fire for an overdue requirement; consider a clock-driven retest.

## Evidence

- `/workspace/uat/p45-ui-findings.md`
- `/workspace/uat/push45/CHANGES-push-45-maintenance-due-2026-11-09.md`
- `/workspace/uat/s67-68/screenshots/p45-maintenance.webp`
- `/tmp/p45x/maintenance.csv` (from warrantycat-export-2026-11-09 (2).zip)
