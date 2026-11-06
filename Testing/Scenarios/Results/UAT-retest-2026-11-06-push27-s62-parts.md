# UAT retest: Push 27 / Scenario 62 — Parts on a vehicle (S3.5.5 + S3.5.6) — non-sweeps only

Build: API **`3b58d0e`** (Push 27; started **7:48:11 AM ET** Nov 6, Staging; `/api/version` match). UI Last-Modified **7:46:54 AM ET**; bundle `main-Q465WJ7C.js`. UI deploy proof: **Parts** section on a vehicle page (after SPA reload — see Setup note). Notes: `CHANGES-push-27-parts-on-a-vehicle-2026-11-06.md`. Plan: [scenario-62.md](sets/browser-plans/scenario-62.md) steps **1–24**. Mode: Full-only, **targeted** (new code + listed gaps only). Browser run ~8:15–8:47 AM ET Nov 6. **Push 26 fixes are NOT in this report** (separate concurrent / later report on the same build).

**DB Stager prep:** API `3b58d0e` match; migration **`PartsOnAVehicle`** (`20261106114100_PartsOnAVehicle`) applied; prior VehiclesSlice1 + VehiclePrivateSale + VehicleCoverageStart present; seed unchanged (Vehicles category, Private sale, **74** makers; parties 636 / seller 176 / manufacturer 404 / categories 55). Clock **offset 0** pre/post. Alice+Bob scenario-reset (**115** rows); Alice/Bob **0** items/vehicles/parts/installs/coverages/todos. Carol preserved; Ops 2FA on with **2** tokens; shared baseline unchanged. Evidence: `/workspace/uat/push27-prep/prep-result-dbstager-20261106.md`, staging `push27-prep-20261106.md`.

**Sweeps / clock:** intentionally **not run**. No clock advances. No orphan purge. No reminder-send / export-expiry. One **normal customer Settings export** (step 22) plus a post-action export after dispose/delete KEEP flows — not maintenance.

## Headline

Parts-on-a-vehicle core paths work after the live SPA reload: add/link parts, filters, move/detach history, dispose/delete KEEP prompts, and customer export with `part_history.csv`. Mileage expiry by an **actual** 89,000 reading works. Reader applied the synthetic tire PDF’s time+mile limits onto an existing tires part, but **did not create a separate prorated stage** (**Fail** on step 23). Narrow gaps remain on people inheritance UI, displayed truck-odometer endpoint wording, missing “start date to confirm”, ordinary-item mile input, Nov 5 vs Nov 6 end-date display, and My Items prorated labeling.

## Setup / stale-UI note (excluded from Fail totals)

First open of [UAT Truck](https://stuffit-ui.onrender.com/items/01a1b101-6512-7546-8da9-516ea3830fa6) showed the teal banner **“A new version of WarrantyCat is ready. Reload”** and **no Parts section** (stale cached SPA). After **Reload**, Parts / Add a part / Link an item you already have appeared empty as expected. **Not graded as a product Fail.** Evidence: asset `0e97154ea69624d55bda8a125c87eb37634a166878783c182c1955139795bb7e.png` (pre-reload banner); `b27c8309cc9cc4214c4651ae498c283a54904fb82a79b5d493935ee104026a03.png` (post-reload Parts empty).

Truck setup (browser-created): Truck / 2024 Ford F-150 / new / bought **2025-01-01** / odometer **38,000** on purchase; reading **40,000** on **2026-11-06** (later replaced by **89,000** for step 16).

## Synthetic fixture (transparent)

No real SampleData tire-warranty PDF matched step 23 (only invoice `06-half-letter-invoice-tires.pdf`). Created labeled synthetic:

- `/workspace/uat/retest-3b58d0e/tire-warranty-50000-72mo-prorated-after-36-SYNTHETIC.pdf`
- `/workspace/uat/sample/tire-warranty-50000-72mo-prorated-after-36-SYNTHETIC.pdf`
- **md5** `e6ed2d0620b25ddc49086fecb1d4db53`
- `pdftotext` phrases verified: `50,000 miles`, `72 months`, `prorated after 36 months`, free-replacement through 36 months; header says **SYNTHETIC UAT TEST DOCUMENT — NOT A REAL MANUFACTURER WARRANTY**.
- **Not** a fake of a real Michelin/BFG PDF. Applied on existing item pages only (known rule: prorated stage from document is added on item-page apply, not waiting New Item).

## Scenario 62 — steps 1–24

| # | Result | Notes |
|---|---|---|
| 1. Truck Parts section empty + Add/Link | **Pass** | After SPA Reload: **Parts** “No parts yet.” with **Add a part** and **Link an item you already have**. Shot: asset `b27c8309…png`. |
| 2. Add part UAT Tires (Michelin, install 2026-09-01 @ 38,000; 50k mi / 72 mo) | **Pass** | Form opened with vehicle already chosen; only install extras; no company/plan/insurance required; saved as item [UAT Tires](https://stuffit-ui.onrender.com/items/01a1b107-7a9f-719f-89ff-0f2e42e91f21). Shot: asset `5dcc07f0…png`. |
| 3. Truck Parts list mile end 88,000 | **Pass** | Truck showed **2 parts** after mats: Tires “Installed Sep 1, 2026 at 38,000 miles”; warranty until Sep 2032 or 50,000 miles; first-batch record: mile end **38,000+50,000=88,000** on truck odometer. Shot: asset `c64e7aa4…png`. Later step 13 notes the **88,000 truck-odometer endpoint is not literally displayed** as that number — see step 13 nuance. |
| 4. My Items Part-of tag + Parts / Vehicles filters | **Pass** | **Part of UAT Truck** tag; Parts filter shows only parts; Vehicles only shows vehicles. Evidence also in steps7–11 pack `step8-items-tag.png`. |
| 5. Open part page | **Pass** | Own purchase/coverages; **Part of UAT Truck** with install 38,000. Shot: `5dcc07f0…png`. |
| 6. Add UAT Floor mats, no warranty | **Pass** | Listed without warranty; no company asked. Shot: truck Parts row in `c64e7aa4…png`. |
| 7. Follower inheritance on new part | **Gap / not testable** | Truck normal view, Edit mode, Edit item dialog, and Add a part form expose **no owner/follower/people controls**. Could not add in-app follower; inheritance check not executed. Evidence: `/workspace/uat/s62-steps7-11-evidence/step7-truck-edit.png` + `report.md`. |
| 8. Link ordinary UAT Battery as part | **Pass** | Created ordinary battery; **Part of a vehicle** → Truck; installed 2026-10-01 @ 39,500. Truck Parts + My Items tag. Mile limit set after link (Add coverage dialog lacked miles until linked). Evidence: `s62-steps7-11-evidence/step8-*.png`. |
| 9. Refuse vehicle-as-part | **Gap** (safe UI exclusion; explicit refusal not exercised) | Truck has no **Part of a vehicle** action. Link picker after Battery detach offered only ordinary items (Battery); excluded Truck and Trailer. No supported action to attempt linking Truck as a part of Tires/itself, so plain refusal message was **not triggered**. Evidence: `step9-link-picker.png`, `step7-truck-edit.png`. |
| 10. Move Battery Truck→Trailer | **Partial** | Trailer created. Move required new install date; blank leaving reading left Move enabled after date+new odo; history: “The miles on that stretch are not known.” After move: **12,000 left** at Trailer 5,000 (was 11,500 on Truck) — blank leaving reading makes historical consumption unknown, so **known-mile deduction cannot be graded Pass**. Evidence: `step10-required-date.png`, `step10-moved-history.png`. |
| 11. Take Battery off vehicle | **Pass** (wording caveat) | Confirm copy kept date coverage; **Miles no longer watched**; last known mile end **17,000**. Caveat: leading sentence still says “or 12,000 miles, whichever comes first” while reminders are date-only. Evidence: `step11-confirm.png`, `step11-detached.png`. |
| 12. Bob API link Alice items by id | **Blocked** | No documented part-link HTTP contract (path/body). Bob current API password unavailable (`QA_PASSWORD_BOB` absent; `QA_NEW_PASSWORD_BOB` unconfirmed — **not tried**). **Zero login / link attempts.** Evidence: `/workspace/uat/retest-3b58d0e/api-contracts-investigation-2026-11-06.md`; staging `s62-step12-auth-investigation-20261106.md`. |
| 13. Tires coverage both limits / 88,000 endpoint | **Partial** | Show policies: both limits; remaining **48,000** at last reading 40,000 on Nov 6 (arithmetic consistent with 88,000). **GAP:** literal **88,000** truck-odometer endpoint never displayed (first-batch “88,000” was the computed end, not an on-screen endpoint label). Truck Parts row: “Warranty until Sep 2032 or 50,000 miles”. Evidence: `/workspace/uat/results/scenario62-steps13-18-2026-11-06.md`; shot asset `965bb580…png`. |
| 14. Part with warranty, no install date | **Partial** | [UAT No Install Date Part](https://stuffit-ui.onrender.com/items/01a1b10f-b194-725a-996f-61d39439ae53): “Installed: day not known”; miles prompt to add odometer; purchase-basis dates Sep 1, 2026–Sep 1, 2032. **GAP:** no **“start date to confirm”** label; dates shown definite. Month-only length initially said “No fixed end date” until Ends set explicitly. Shot: asset `20d032a8…png`. |
| 15. Never-linked ordinary + miles warranty | **Partial** | [UAT Unlinked Mileage Item](https://stuffit-ui.onrender.com/items/01a1b110-d477-7745-8681-7bdedc63fbfa): Add coverage dialog has **no Miles / mile-limit input** even for Manufacturer warranty. Date-only coverage Active. Did not bypass by linking. Detached-battery history case corroborates “was a part keeps miles” separately. Shot: asset `d2476c9e…png`. |
| 16. Truck reading 89,000 ends tires by miles | **Partial** | Replaced same-day 40,000 with **89,000** on Nov 6. Tires **Expired**; narrative “Ended by miles on **Nov 6, 2026**: … 89,000 miles”. Estimate alone never ends. **GAP:** badge/span **“Ended Nov 5, 2026”** / “Sep 1, 2026 to Nov 5, 2026” conflict with Nov 6 narrative (also in export `end_date=2026-11-05` vs `ended_by_miles_on=2026-11-06`). Shot: asset `038a85e5…png`. |
| 17. Two-stage Battery Free + Prorated | **Partial** | Free 36 mo + Prorated 72 mo (flag checked). Item policy list labels **“Manufacturer warranty (Prorated: you pay a share)”**; claim guidance says you pay a share; no share calculated. **GAP:** My Items row shows only “Manufacturer warranty until Oct 1, 2027” — **no prorated label** in the list. Shots: assets `177d66cc…png`, `9192040a…png`, `b57380bd…png`. |
| 18. Tires defect claim guidance | **Pass** | Guidance shows both limits / ended-by-miles with install 38,000 and actual 89,000; goodwill only suggested. Battery prorated guidance already verified in 17. Shot: asset `add61dec…png`. |
| 19. Delete truck with parts — explicit choice | **Pass** | Truck Edit→Delete alertdialog: “UAT Truck has 3 parts”; buttons **Keep them as separate items** / **Delete them too** / **Cancel**. Cancelled on live truck. Actual KEEP deletion exercised on isolated disposable vehicle+part fixture (vehicle deleted; part retained Owned, blank vehicle id). Shots: `/workspace/uat/push27-evidence/19-truck-delete-choice.png`, `19-fixture-delete-choice.png`, `19-fixture-part-retained.png`. Cascade-delete-parts branch inspected as choice only, not executed. |
| 20. Dispose truck with parts — KEEP | **Pass** | Same explicit question; selected KEEP. Truck **Disposed**; Parts “No parts yet.”; three parts retained separately. Shots: `20-truck-dispose-choice.png`, `20-truck-disposed-no-parts.png`. |
| 21. Retained parts dates + last known mile end | **Pass** (pre-existing date nuance) | Tires: both coverages retained; UI “last known mile end was **88,000** …”; “Miles no longer watched.” No-install part: last known **50,000**. Floor mats: no warranty labels N/A. Pre-existing Nov 5 vs Nov 6 expiry display discrepancy retained (not introduced by KEEP). Removal odometer not prompted; stretch miles unknown in history. Shots: `21-tires-retained.png`, `21-floor-mats-retained.png`, `21-no-install-retained.png`. |
| 22. Settings export parts + coverages + part history | **Pass** | Normal customer export **before** mutations preserved; second export after KEEP flows. Both ZIPs contain `items.csv` (part link columns), `coverage.csv`, `part_history.csv`, `vehicles.csv`, `odometer_readings.csv`. Independent inspection below. ZIPs: `/workspace/uat/push27-export/warrantycat-export-2026-11-06.zip`, `post-actions-export-2026-11-06.zip`. |

### Part E — warranty reader (steps 23–24)

| # | Result | Notes |
|---|---|---|
| 23. Apply synthetic tire PDF on existing tires part | **Fail** | Uploaded/applied `tire-warranty-50000-72mo-prorated-after-36-SYNTHETIC.pdf` on existing UAT Tires (item-page apply). Extracted coverage stored **50,000** mile limit + **72** months / UAT Tire Co terms with quotes. **Separate prorated stage after 36 months was NOT created** — only one Extracted coverage; Edit coverage “This is the prorated stage…” unchecked; export `prorated_you_pay_a_share` blank on that row. Full synthetic PDF text includes free-replacement through 36 months and prorated after. Shots: assets `509ceae0…png`, `feb45ae6…png`. |
| 24. Same PDF on ordinary appliance | **Partial** | [S62 Step24 SYNTHETIC UAT Toaster](https://stuffit-ui.onrender.com/items/01a1b117-78de-7b4d-ab90-e5a8183a5b6e): UI Edit coverage shows **no structured mile-limit field**; terms text still mentions 50,000 miles in prose. Browser run did **not** independently prove backend `mile_limit` null at grade time. **Post-hoc export inspection (this report):** toaster Extracted coverage has **blank `mile_limit`** (and blank `prorated_you_pay_a_share`). Shots: assets `22066ce4…png`, `3dbb1cd7…png`. |

## Independent export verification (not assumed from browser writeup)

Inspected both ZIPs on disk (sha256 below); read extracted CSVs directly.

**Pre-action ZIP** `warrantycat-export-2026-11-06.zip` (14,332 B) sha256 `db932e03fd92e836131627501807cbfc73cb8fc60703c64e59535fc3de352245`

- Truck **Owned**; three linked parts (Tires installed 2026-09-01 @ 38000; Floor mats; No Install Date Part).
- Tires coverages: User Michelin + Extracted UAT Tire Co; both `mile_limit=50000`, `mile_start=38000`, `ended_by_miles_on=2026-11-06`, `ended_by_miles_at=89000`, `end_date=2026-11-05`, `date_end_before_miles=2032-09-01`, `part_installed_on=2026-09-01`; **prorated blank** (confirms step 23 Fail independently).
- Battery: three coverages including prorated=`yes` on 72-mo stage; detached stretch history Truck+Trailer in `part_history.csv` with blank removal odometer/distance.
- Toaster: Extracted coverage `mile_limit` **blank**.
- Readings: Truck 38000 @ 2025-01-01 and **89000** @ 2026-11-06.

**Post-action ZIP** `post-actions-export-2026-11-06.zip` (14,691 B) sha256 `750b15b8e12fb82634f382b53bc8cdd3abbb119d38ca87525addb1d376550afd`

- Truck **Disposed**; former Truck parts **Owned** with blank `part_of_vehicle_id` / `installed_on`.
- Tires + No-install coverages: `miles_not_watched=yes`; original mile starts / date_end_before_miles preserved.
- `part_history.csv` adds Truck removal stretches for Tires / Floor mats / No Install Date Part + disposable fixture part stretch; removal odometer/distance blank.
- **No `last_known_mile_end` column** in `coverage.csv` — last-known **88,000 / 50,000** values verified from live UI screenshots (`21-tires-retained.png`, `21-no-install-retained.png`), not from a CSV field.
- Disposable fixture vehicle absent; retained fixture part present.

Extracted trees: `/workspace/uat/push27-export/extracted/`, `/workspace/uat/push27-export/post-actions-extracted/`.

## Open issues / notes for dev

1. **S62.23 Fail** — Reader does not add a **separate prorated stage** from a document that clearly states free replacement through 36 months then prorated after, even on item-page apply of a full synthetic PDF.
2. **S62.16 / export** — Coverage `end_date` / UI badge **Nov 5** vs ended-by-miles narrative **Nov 6**.
3. **S62.13** — Computed mile end **88,000** is not shown as a truck-odometer endpoint label (remaining-miles arithmetic works).
4. **S62.14** — Missing **“start date to confirm”** when install day unknown; dates look definite.
5. **S62.15** — Never-linked ordinary item cannot enter a structured mile limit in Add coverage (may match “not built / appliances drop miles” rule — still a scenario Gap vs the written step).
6. **S62.17** — Prorated label missing on **My Items** list row (present on item policy list + claim guidance).
7. **S62.7** — No people/follower UI on vehicle or part forms → inheritance untestable.
8. **S62.9** — UI safely prevents vehicle-as-part without surfacing the plain refusal string.
9. **S62.10** — Known-mile deduction unprovable when leaving reading left blank (unknown branch works).
10. **S62.12** — Needs documented part-link API contract + confirmed Bob password (or Bob browser substitute clearly labeled not-API).
11. **Export** — No `last_known_mile_end` column; UI copy is the only retained last-known proof.
12. **Stale SPA** — Parts UI absent until Reload banner honored (operational, not product Fail).

## Not in this report

- **Push 26** typed-coverage / superseded-note / S61.29 / S54 days retests — **separate report** (running independently; do not mix).
- Sweeps (`export-expiry`, `reminder-send`).
- Clock advances / orphan purge / full regression.
- Push 25 partials (S61.14, Sub-Zero notification) unless re-encountered — not re-run here.

## State left

- Alice: UAT Truck **Disposed**; Trailer Owned; Battery / Tires / Floor mats / No-install / Unlinked / Toaster Owned (parts detached); disposable fixture vehicle deleted, its part retained. No scenario reset after run.
- Bob / Carol / Ops: untouched for mutations (Ops 2FA still on). No Bob auth attempts.
- Global clock: **offset 0**. No sweeps.

## Totals (from graded rows above only)

| Block | Pass | Partial | Fail | Blocked | Gap / not testable |
|---|---:|---:|---:|---:|---:|
| S62 steps 1–24 | **13** (1–6, 8, 11, 18–22) | **7** (10, 13–17, 24) | **1** (23) | **1** (12) | **2** (7, 9) |

Stale-UI pre-reload absence of Parts **excluded** from Fail totals.

## Evidence paths

- Report (box): `/workspace/uat/retest-3b58d0e/UAT-retest-2026-11-06-push27-s62-parts.md`
- Batch writeups: `/workspace/uat/s62-steps7-11-evidence/report.md`; `/workspace/uat/results/scenario62-steps13-18-2026-11-06.md`; `/workspace/uat/push27-evidence/results.md`
- Screenshots (7–11): `/workspace/uat/s62-steps7-11-evidence/`
- Screenshots (19–21): `/workspace/uat/push27-evidence/`
- Screenshots (13–18, 23–24, early Parts): `/cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/` (hashes cited in table)
- Exports: `/workspace/uat/push27-export/`
- Prep: `/workspace/uat/push27-prep/`
- Final Results (UNC): `\\DESKTOP-TD3DQ64\Stuffit\Testing\Scenarios\Results\UAT-retest-2026-11-06-push27-s62-parts.md`
- Library: `uat-library/runs/UAT-retest-2026-11-06-push27-s62-parts.md` + INDEX entry
