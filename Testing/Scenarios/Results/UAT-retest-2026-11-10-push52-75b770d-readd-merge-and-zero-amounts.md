# UAT retest — Push 52: re-add merge and $0 amounts (Nov 10, 2026)

- **Build:** API 75b770d, started 8:52:26 AM ET. UI ~8:51 AM ET. Staging. API and UI. No migration.
- **Source:** CHANGES-push-52-readd-merge-and-zero-amounts-2026-11-10.md (SHA256 `ef00cc3a8df3dc57c5726f7652ad8599db0693a195c8e92e2127cb2717bd3890`); p52-findings.md.
- **Account:** P34 Self personal. Already signed in. No new-version banner, even after a reload (`s52-01-banner.png`). The new `$0.00` wording rendered, so the new UI was live.
- **Clock:** Offset 0 (never moved; confirmed after the run).
- **Fixtures:** none new. Nothing was uploaded; each order was re-read with **Read it** in item Edit mode on the existing S69 / push 51 files (F-150 orders 06 and 03, Outback 07, Tucson 09).
- **Not reported:** everything under "Decided, do not report" in the push 51 note (end-date/badge behavior; stale wording on already-saved entries).

## Results

| Result | Count |
|---|---|
| Pass | 1 |
| Partial | 0 |
| Fail | 1 |
| Inconclusive | 0 |

## Per-step results

| # | Check | Result |
|---|---|---|
| 52-merge | Re-add of F-150 order 06 merges hand-added rotation and flat-repair rows; each job once, no longer "added by you" | **Fail** (Medium, Needs CC) |
| 52-zero | Warranty / plan-paid rows on 03, 06, 07, 09 show the customer amount on the card and in history | **Pass** |

### 52-merge — Fail (Medium, Needs CC)

F-150 order 06 history **before** the re-read already had four Feb 11, 2026 / 31,890 mi rows (`s52-06-hist-before.png`):

1. "Rear right tire: Flat repair plug/patch (nail in tread) · repaired under warranty · you paid $0.00 · Tread Masters road hazard protection (to Jul 22, 2028)"
2. "Rear tire: Flat repair - plug/patch (nail in tread), billed to road hazard plan RH-08-552190 · you paid $0.00 · added by you"
3. "Tires: Rotate & balance - lifetime (no charge) · you paid $0.00 · added by you"
4. "Tires: Rotate & balance (lifetime, original invoice 08-552190) · you paid $0.00 · Michelin warranty (to Jul 22, 2031)"

The card kept the rotation and flat repair with those same (rules) labels, left out the wipers ($49.98), and showed the "already in the service history… jobs you added by hand stay" note (`s52-06-card.png`). After Add, all four rows were **unchanged** (`s52-06-hist-after.png`): each job still appears twice, and the hand copies are still **"added by you"**.

Likely cause (**inference**): the hand rows' part and description text differs from the reader's ("Rear tire" vs "Rear right tire"; "Rotate & balance - lifetime (no charge)" vs "(lifetime, original invoice 08-552190)"), so the match may be by exact text. Those hand rows were made in push 46 / S69 and survived the push 51 re-read.

The notes' "jobs the rules still leave out stay as hand-added" path was **not testable** — no hand-added wiper row exists.

### 52-zero — Pass

Card and history matched word for word. Existing rows already showed the new amounts **before** the re-read. No new duplicates.

- **03:** recall **"repaired under warranty · you paid $0.00"** with no coverage; pinion **you paid $0.00** on Powertrain (to Jun 10, 2028); seat heater **you paid $0.00** on Bumper-to-bumper (to Jun 10, 2026). (`s52-03-card.png`, `s52-03-hist.png`)
- **06:** flat repair **"repaired under warranty · you paid $0.00"**. (`s52-06-card.png`, `s52-06-hist-after.png`)
- **07:** goodwill CVT valve body **"repaired under warranty · you paid $352.80"**, no coverage. (`s52-07-card.png`, `s52-07-hist.png`)
- **09:** hose, strut, and campaign 9ZZ each **"repaired under warranty · you paid $0.00"**, on Powertrain (to Apr 5, 2035) / Bumper-to-bumper (to Apr 5, 2030) / Powertrain (to Apr 5, 2035). (`s52-09-card.png`, `s52-09-hist.png`)

## Needs code / product follow-up

1. **Medium, Needs CC:** when re-adding an order, merge a hand-added row with the rules' copy of the **same job** even when part/work wording differs (e.g. "Rear tire" vs "Rear right tire"). After the merge, the remaining row should not stay "added by you". The leftover-only "stay hand-added" path still needs a fixture (a hand-added left-out job such as wipers) to be verified.

## Evidence

- `/workspace/uat/push52/p52-findings.md`
- `/workspace/uat/push52/CHANGES-push-52-readd-merge-and-zero-amounts-2026-11-10.md`
- Screenshots under `/workspace/uat/push52/shots/`
