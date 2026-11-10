# UAT retest — Push 47: keep "added by you" on re-add (Nov 9, 2026)

- **Build:** API 2f54fe5, started 7:29:44 PM ET. UI ~7:28 PM ET. Staging. No migration.
- **Source:** CHANGES-push-47-keep-added-by-you-2026-11-09.md; HANDOFF-push47-2f54fe5-retest.txt; push47/p47-ui-findings.md.
- **Account:** P34 Self personal (vault 3550464). Clock Offset 0 (not moved).
- **Item:** https://stuffit-ui.onrender.com/items/01a1c209-fcba-7030-b6e9-5d5fd70c94d0 (P45 Honda CR-V)
- **Fixtures:** P46-01 / P46-02 under `/workspace/uat/push46/` (re-read via existing Read it on the receipts; no duplicate uploads).
- **Not changed (do not report as fails):** three push 46 Low notes — picker labels lack Powertrain; untick/retick resets picker. (The no-odometer odometer line is now fixed.)

## Results

| Result | Count |
|---|---|
| Pass | 5 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |

Plus **2 Low** notes (1 Needs CC on card wording).

## Per-step results

| # | Check | Result |
|---|---|---|
| 1 | Re-add with nothing ticked keeps Tires/Wipers "added by you"; oil only replaced | **Pass** |
| 2 | Ticking Tires again does not duplicate | **Pass** |
| 3 | P46-02 no-odometer card: no odometer line; says "jobs you added by hand stay" | **Pass** |
| 4 | Nov 2 has a single Tire "added by you" | **Pass** |
| 5 | Oil maintenance On track (next due Oct 20 2027 / 30,400 mi) | **Pass** |

### Details

**1 — Keep "added by you" on re-add: Pass.** After oil + tires + wipers on P46-01, re-read and Add with nothing ticked: Oct 20 2026 still has **3 entries** — oil replaced only; Tires and Wipers still marked **added by you**. Screenshots: `p47-02-after-add-ticked.png`, `p47-03-after-readd-none.png`.

**2 — No duplicate on re-tick: Pass.** Re-read P46-01, ticked Tires (No coverage), Add, reload: Oct 20 still 3 entries, **one** Tires row, Wipers still present. Screenshot: `p47-04-after-retick.png`.

**3 — No-odometer card wording: Pass.** P46-02: "Nothing on this order is service on a covered part." + left-out ticks. **No** "Its odometer reading can still be kept". Card ends: **"This order is already in the service history. Adding it again replaces what it gave; jobs you added by hand stay."** Screenshot: `p47-05-no-odo-card.png`.

**4 — Nov 2 single Tire: Pass.** Add with nothing ticked, reload: one entry — "Tire: Replaced tire… · you paid \$180.00 · **added by you**"; no duplicates.

**5 — Maintenance: Pass.** Engine oil and filter change **On track**: "Last done Oct 20, 2026 at 22,900 miles. Next due by Oct 20, 2027 or 30,400 miles, whichever comes first."

### Low notes

1. **Needs CC — incomplete keep-warning on the with-odometer card.** P46-01 (has odometer) still says only **"This order is already in the service history. Adding it again replaces what it gave."** with **no** "jobs you added by hand stay" — even when that order already has hand-added rows (`p47-01-card.png`). The phrase appears only on the no-odometer card. Suggest the same keep wording on both cards.

2. Re-read card lists jobs already added by hand as unticked left-out rows, with no sign they are already in the history.

### Unchanged Lows (expected)

- Picker labels say "Manufacturer warranty (to Nov 8, 2029/2027)" rather than naming Powertrain / Bumper-to-bumper.
- Unticking and reticking a row resets its picker to No coverage.
- ~~No-odometer "odometer can still be kept"~~ — **fixed** in this push.

## Needs code / product follow-up

1. **Low Needs CC:** show "jobs you added by hand stay" on the with-odometer re-add card as well as the no-odometer card.
2. Low: mark already-in-history left-out rows on the re-read card (or omit them from the tick list).

## Evidence

- `/workspace/uat/push47/p47-ui-findings.md`
- `/workspace/uat/push47/CHANGES-push-47-keep-added-by-you-2026-11-09.md`
- Screenshots: `push47/p47-01-card.png`, `p47-02-after-add-ticked.png`, `p47-03-after-readd-none.png`, `p47-04-after-retick.png`, `p47-05-no-odo-card.png`

## Addendum — fixtures filed (2026-11-09 8:29 PM ET)

Per the updated CHANGES note, the two QA-made PDFs were copied into the Scenario 68 folder (no first-page JPG twins were made):

- `Testing\Scenarios\Scenario 68 - Backdated car with service records\07-service-tires-wipers-2026-10.pdf` (from `P46-01-service-tires-wipers-2026-10.pdf`; SHA256 `139966540b541b22115286e611fa2a740fc58c2c1541eb97adf54176709247d2`)
- `Testing\Scenarios\Scenario 68 - Backdated car with service records\08-counter-tires-wipers-only-2026-11.pdf` (from `P46-02-counter-tires-wipers-only-2026-11.pdf`; SHA256 `2429bc24a9e828894c7e4dc873fb1427c4f2dde2795785af3b5fd66dc15e28e5`)

`Testing\SampleData\` exists and was not used for these (they belong with Scenario 68). Going forward, new fixtures will be saved in the matching `Testing/Scenarios/Scenario N - .../` folder, or in `Testing/SampleData/` for general ones, and named in the report. Claude Code can now add the steps to `scenario-68.md`.
