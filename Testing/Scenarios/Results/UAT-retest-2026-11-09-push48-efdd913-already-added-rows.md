# UAT retest — Push 48: already-added rows on re-read (Nov 9, 2026)

- **Build:** API efdd913, started 8:26:10 PM ET. UI ~8:25 PM ET. Staging. No migration.
- **Source:** CHANGES-push-48-already-added-rows-2026-11-09.md; HANDOFF-push48-efdd913-retest.txt; push48/p48-ui-findings.md.
- **Account:** P34 Self personal (vault 3550464). Clock Offset 0 (not moved).
- **Item:** https://stuffit-ui.onrender.com/items/01a1c209-fcba-7030-b6e9-5d5fd70c94d0 (P45 Honda CR-V)
- **Fixtures (reused, no new files this run):**
  - `Testing\Scenarios\Scenario 68 - Backdated car with service records\07-service-tires-wipers-2026-10.pdf` (P46-01 / RO5)
  - `Testing\Scenarios\Scenario 68 - Backdated car with service records\08-counter-tires-wipers-only-2026-11.pdf` (P46-02 / RO6)
- **Not changed (do not report as fails; not retested):** push 46 Lows — picker labels lack Powertrain / Bumper-to-bumper; untick/retick resets the coverage picker.

Graded results are from the **After new-version reload** pass. A first pass ran on the previous UI bundle (see Low/info).

## Results

| Result | Count |
|---|---|
| Pass | 4 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |

Both push 47 Lows are **fixed**.

## Per-step results

| # | Check | Result |
|---|---|---|
| 1 | P46-01 re-read: already-added rows (no tick); shop supplies tickable; count is 1 | **Pass** |
| 2 | With-odometer card says "jobs you added by hand stay" (push 47 Low 1) | **Pass** (fixed) |
| 3 | P46-02: Tire already added; count 2; hand-added line; no odometer line | **Pass** |
| 4 | Re-add with nothing ticked keeps the 3 Oct 20 entries | **Pass** |

### Details

**1 — Already-added on P46-01: Pass.** After the new-version reload, Tires and Wipers read **"already added by you"** with **no tick box**. Shop supplies remains tickable. Count: **"1 other job was left out: not on a covered part. Tick any that should be kept."** Odometer line: "The odometer (22,900 miles) is added as a reading." Screenshots: `p48-01b-card-ro5.png`, `p48-04b-card-ro5.png`.

**2 — Odometer card wording (push 47 Low 1): Pass.** P46-01 card ends: **"This order is already in the service history. Adding it again replaces what it gave; jobs you added by hand stay."** Same wording as the no-odometer card. Push 47 Low 1 fixed.

**3 — P46-02 already-added: Pass.** "Nothing on this order is service on a covered part." Count: **"2 other jobs were left out…"** Tire: **"already added by you"** (no tick). Rear wiper and shop supplies remain tickable. Hand-added keep line present. **No odometer line.** Screenshot: `p48-02b-card-ro6.png`.

**4 — Re-add with nothing ticked: Pass.** Oct 20, 2026 still has exactly **3 entries** — oil (Manufacturer warranty to Nov 8, 2029); Tires **added by you**; Wipers Manufacturer warranty (to Nov 8, 2029) · **added by you**. Nov 2 Tire **added by you** still present. Screenshot: `p48-03-history.png`.

Push 47 Low 2 (re-read listed hand-added jobs as unticked left-out rows with no sign they were in history) is also **fixed** by the "already added by you" treatment.

### Low / info (not a defect)

The first pass ran on the previous UI bundle. A hard reload did not load the new build; the **"A new version of WarrantyCat is ready"** banner had to be clicked first. Checks 1, 2, and 4 failed on that stale bundle (tick boxes still present, no "already added" label) and are **superseded** by the 1b / 2b / 4b pass after banner Reload. Check 3 (re-add keeps 3 entries) already passed on the first pass.

## Needs code / product follow-up

None from this push's scope. Unchanged push 46 Lows (picker names; picker reset on retick) remain outstanding and were not retested.

## Evidence

- `/workspace/uat/push48/p48-ui-findings.md`
- `/workspace/uat/push48/CHANGES-push-48-already-added-rows-2026-11-09.md`
- Screenshots (graded): `push48/p48-01b-card-ro5.png`, `p48-02b-card-ro6.png`, `p48-03-history.png`, `p48-04b-card-ro5.png`
- First-pass (superseded): `p48-01-card-ro5.png`, `p48-02-card-ro6.png`
