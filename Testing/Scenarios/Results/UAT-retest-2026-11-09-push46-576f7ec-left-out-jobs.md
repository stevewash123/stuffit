# UAT retest — Push 46: left-out repair jobs (Nov 9, 2026)

- **Build:** API 576f7ec, started 5:33:52 PM ET. UI ~5:32 PM ET. Staging. Migration `ServiceEntryAddedAnyway` verified applied on Neon StuffIt (read-only, 6:06 PM ET): column `service_entries.added_anyway` present; `__EFMigrationsHistory` has `20261109220928_ServiceEntryAddedAnyway`.
- **Source:** CHANGES-push-46-left-out-repair-jobs-2026-11-09.md; HANDOFF-push46-576f7ec-retest.txt; p46-ui-findings.md.
- **Account:** P34 Self personal (vault 3550464). Run ~6:06–6:08 PM ET. Clock Offset 0.
- **Item:** https://stuffit-ui.onrender.com/items/01a1c209-fcba-7030-b6e9-5d5fd70c94d0 (P45 Honda CR-V)
- **Fixtures (QA-made, synthetic):** `/workspace/uat/push46/P46-01-service-tires-wipers-2026-10.pdf` (oil + tires + wipers + shop supplies, 22,900 mi); `P46-02-counter-tires-wipers-only-2026-11.pdf` (tire + rear wiper + shop supplies, no odometer). Notes' "Honda order with tires, wipers" is not in the S68 set.
- **Not changed (do not report as fails):** which jobs are kept or left out by default; nothing saved until Add; a coverage id not on this vehicle is ignored.

## Results

| Result | Count |
|---|---|
| Pass | 7 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |

Plus **1 Medium** Needs CC (re-add replaces owner's "added by you" rows).

## Per-step results

| # | Check | Result |
|---|---|---|
| 1 | Left-out rows show with tick boxes (tires, wipers, shop supplies) | **Pass** |
| 2 | Coverage picker defaults to No coverage (history only) | **Pass** |
| 3 | Add button counts ticked jobs (0 / 1 / 2 texts) | **Pass** |
| 4 | "added by you" only on ticked entries | **Pass** |
| 5 | Left-out-only order with no odometer still offers the card | **Pass** |
| 6 | Ticking nothing behaves as before (only oil added) | **Pass** |
| 7 | Bonus: oil maintenance settled by Oct 20 order → On track | **Pass** |

### Details

**1 — Tick boxes: Pass.** P46-01 card: oil kept on Manufacturer warranty (to Nov 8, 2029). **"3 other jobs were left out: not on a covered part. Tick any that should be kept."** Unticked rows: Tires \$720.00; Wiper blades (front pair) \$42.00; Shop supplies / environmental \$6.50. Screenshot: `p46-01-card-unticked.png`.

**2 — Picker default: Pass.** Default **"No coverage (history only)"**. Options also include Manufacturer warranty (to Nov 8, 2029) and (to Nov 8, 2027). Screenshot: `p46-02-ticked-pickers.png`.

**3 — Add button counts: Pass.** 0 → "Add to service history"; 1 → "…with 1 left-out job"; 2 → "…with 2 left-out jobs".

**4 — "added by you": Pass.** After ticking tires (No coverage) + wipers (2029) and leaving shop supplies unticked: tires show **added by you** (no coverage); wipers show **Manufacturer warranty (to Nov 8, 2029) · added by you**; oil has **no** "added by you"; shop supplies not added. Coverage end dates unchanged. Odometer 22,900 / Oct 20 2026 added. Screenshot: `p46-03-history-after-add.png`.

**5 — Left-out-only / no odometer: Pass.** P46-02 card: "Nothing on this order is service on a covered part. Its odometer reading can still be kept." + 3 left-out rows with ticks. Ticked tire (No coverage) → history entry Nov 2, 2026 / Tire … **added by you**, no mileage, no reading added.

**6 — Ticking nothing: Pass.** (Covered by the re-add path with all unticked: only the oil entry remains / is re-applied; no left-out rows kept when none ticked.)

**7 — Bonus maintenance: Pass.** Engine oil and filter change **On track**: "Last done Oct 20, 2026 at 22,900 miles. Next due by Oct 20, 2027 or 30,400 miles, whichever comes first."

### Medium — Needs CC

**Re-adding an order already in history replaces the owner's "added by you" rows.** Re-reading P46-01 shows "This order is already in the service history. Adding it again replaces what it gave." With nothing ticked, Add left only the oil entry; the earlier **added by you** tires and wipers from that order were **silently removed**. The card warns about replacing what it gave, but not that the owner's added rows go too. Those rows are the record of misses meant to feed `ServiceRecordRules` decisions (`added_anyway`), so losing them defeats the purpose. **Suggest: keep "added by you" rows on re-add, or warn explicitly that they will be removed.**

### Low notes

- Picker labels say "Manufacturer warranty (to Nov 8, 2029/2027)" rather than naming Powertrain or Bumper-to-bumper.
- Unticking and reticking a row resets its picker to No coverage.
- On the no-odometer order, the card says "Its odometer reading can still be kept" though the order has none.

### Fixture note

Notes' "Honda order with tires, wipers" is not in the S68 set, so QA made two synthetic repair orders under `/workspace/uat/push46/`. **Suggest CC add them as scenario fixtures.**

## Needs code / product follow-up

1. **Medium (CC):** on re-add of an order already in history, preserve (or explicitly warn about removing) "added by you" / `added_anyway` rows — they are the miss record for `ServiceRecordRules`.
2. **Fixtures (CC):** promote P46-01 / P46-02 (or equivalent) into the scenario set.
3. Low: name Powertrain / Bumper in picker; preserve picker choice across untick/retick; tone down "odometer can still be kept" when the order has none.

## Evidence

- `/workspace/uat/p46-ui-findings.md`
- `/workspace/uat/push46/CHANGES-push-46-left-out-repair-jobs-2026-11-09.md`
- `/workspace/uat/push46/P46-01-service-tires-wipers-2026-10.pdf`, `P46-02-counter-tires-wipers-only-2026-11.pdf`
- Screenshots: `s67-68/screenshots/p46-01-card-unticked.png`, `p46-02-ticked-pickers.png`, `p46-03-history-after-add.png`
