# UAT retest: Push 25 vehicle coverage-start (S3.5.4) + S54 16b + S61 targeted — non-sweeps only
Build: API **`2f52761`** (started **8:55:03 PM ET** Nov 5, Staging; `/api/version` match). UI Last-Modified **Fri, 06 Nov 2026 01:53:43 UTC = 8:53:43 PM ET** (etag `W/"06c556c73e9d50769b3eec78ef7d35d3"`, bundle `main-QXK53JY6.js`). Notes claim UI `b7011c1` (unverifiable in bundle); Push 24 To-do card on the item page confirmed during S54 16b. Mode: Full-only, **targeted**. Browser run ~9:03–9:33 PM ET Nov 5.
Notes: `CHANGES-push-25-vehicle-coverage-start-2026-11-05.md`. Plans: Push 25 steps 1–7 (no new scenario number yet); [scenario-54.md](sets/browser-plans/scenario-54.md) step 16b; [scenario-61.md](sets/browser-plans/scenario-61.md) steps 14 / A9 / B15 (updated 7:44 PM ET wording). Reader on (`item-warranty-v6`).

**DB Stager prep:** API `2f52761` match; migration **`VehicleCoverageStart`** (`20261106005554`) applied; prior VehiclesSlice1 + VehiclePrivateSale + seed (Vehicles category, Private sale, **74** makers) verified. Clock **offset 0**. Alice already empty (0 items/vehicles/coverages/todos/docs/odo) — no reset needed. Bob/Carol preserved; Ops 2FA on with 2 tokens; shared baseline unchanged. Evidence: `/workspace/work/push25/prep-result-20261105.md`.

**Sweeps / clock:** intentionally **not run**. No clock advances. No orphan purge. No reminder-send / export-expiry.

## Headline
Push 25 vehicle coverage-start works for new and used vehicles: start-to-confirm / start-not-known flags, in-service date updates, transferability wording, and certified + factory coexistence after a full reader **Add**. S54 step **16b** now **Pass** (was Blocked for missing Push 24 UI). S61 A9/B15 plain refusal wording **Pass** at section-level (not field-adjacent). S61 step **14 Partial** — confirmation and non-newest latest work; interior confirmed reading’s contribution to pace/miles is not independently numerically demonstrated. Step **7 Partial** — Sub-Zero installation spotcheck only (dates correct after navigate; stale header/notification issues). Registration **completion** was not run (distinct from 16b add behavior).

## Setup correction (excluded from product Fail totals)
First attempt used **Add a purchase** (regular item) plus a **dated** booklet (`vehicle-five-year-60000.pdf` with printed Jan 1, 2025–Jan 1, 2030). Vehicle-specific coverage-start UI did not appear, and printed document dates correctly won over purchase/in-service arithmetic. Item left: [UAT Push25 New Truck](https://stuffit-ui.onrender.com/items/01a1ae98-ad1d-7d37-9097-a085b4ad22bc). **Not graded as a product Fail.** Corrected path: **Add a vehicle** + date-free booklet `vehicle-three-year-36000-datefree.pdf`. Evidence: `evidence/setup-invalid-dated-pdf-regular.png`.

## Push 25 — S3.5.4 vehicle coverage start (steps 1–7)
| # | Result | Notes |
|---|---|---|
| 1. New vehicle, no in-service; apply maker doc | **Pass** | [UAT Push25 Dedicated Truck](https://stuffit-ui.onrender.com/items/01a1aea0-0741-7861-81d8-bcfe617f3b3f). Bought new Jan 1, 2026; date-free 3yr/36k applied. Coverage counted from purchase; **Start date to confirm** prompt + to-do “Enter the date UAT Push25 Dedicated Truck was first put in service” (Due in 15 days). Badge Until Jan 1, 2029. Shot: `evidence/step1-dedicated-start-to-confirm.png`. |
| 2. Enter in-service on coverage | **Pass** (limitation) | In-service **Jan 15, 2026** saved. Coverage moved to Jan 15, 2026–Jan 15, 2029; vehicle shows “in service Jan 15, 2026”; to-do **Done**. **Limitation:** parts/component date lines are **not separately visible** on the coverage card, so parts update is not fully verified — only whole-product dates. **Note:** document application receipt still shows “Applied … from 2026-01-01, to 2029-01-01” after the in-service update (stale). Shot: `evidence/step2-dedicated-after-inservice.png`. |
| 3. Used vehicle, no in-service; apply doc | **Pass** | [UAT Push25 Used Truck](https://stuffit-ui.onrender.com/items/01a1aea4-e10d-756c-9220-18a1a3a92196). Page: first put in service not known. Coverage **Start not known — no end date yet**; item **Needs info**; to-do due in 15 days. Shot: `evidence/step3-used-start-not-known.png`. |
| 4. Enter in-service via vehicle details | **Pass** (limitation) | In-service **Jan 15, 2025**. Coverage dated Jan 15, 2025–Jan 15, 2028; 24,000 miles left at 12,000 reading; status Active. Same parts-visibility limitation as step 2. Shot: `evidence/step4-used-after-inservice.png`. |
| 5. Transferability (used) | **Pass** | **Not transferable:** [UAT Push25 NT Used Truck](https://stuffit-ui.onrender.com/items/01a1aea7-cdcf-73ef-b8d8-fecd0f4a958e) + `vehicle-three-year-36000-datefree-not-transferable.pdf` → **Not counted: not transferable**; document original-owner wording. Shot: `evidence/step5-nt-not-transferable.png`. **Transferable:** [UAT Push25 T Used Truck](https://stuffit-ui.onrender.com/items/01a1aea4-e10d-756c-9220-18a1a3a92196) (same used truck after rename/reuse path) + transferable PDF → “Transfers to the next owner.” / “Can be transferred.” |
| 6. Certified/dealer-added + factory read | **Pass** | Hand-added **Certified or dealer-added** with own start and start odometer. **Note:** entering length **12 months** did **not** calculate an end date; end set manually to **Jan 1, 2027**. Certified showed **10,000 miles remaining** from its start odometer (12,000 purchase reading). Factory doc then applied via full reader **Add** (Keep All after brand conflict Ford vs UAT Motors): **both coverages remained**; no duplicate. Earlier “Not added” reoffer path resolved by completing the Add. Shot: `evidence/step6-certified-plus-factory.png`; Add modal: asset `22edd51cb4c7a235d1c15428c68bc6f316502f3b7927d2eac9c510cbdf1bbde5.png`. |
| 7. Appliance registration / installation | **Partial** | **Registration path covered by S54 16b** (below) — add optional + Register to-do. **Registration completion** (pressing “I registered” / counting the longer term) **not run**. **Installation spotcheck (Sub-Zero only; Wolf/Cove not required for this targeted pass):** [item](https://stuffit-ui.onrender.com/items/01a1aeb1-55ed-7680-af10-6c2480628440) bought **Nov 5, 2026**; installation entered **Oct 15, 2026**. After SPA navigate away/back: whole-product **24 mo → Oct 15, 2028**; sealed parts **144 mo → Oct 15, 2038**; labor **60 mo → Oct 15, 2031**. To-do **Done**; pending start form gone. **Issues:** immediate coverage/header stale until navigate; Notifications still shows “Enter date …” after to-do Done; due showed **15 days** vs plan **14**; source-of-start wording not visible. No email / editor / dismiss / delete / quick-add / Wolf / Cove expanded checks (out of targeted scope). Shots: `evidence/step7-subzero-after-nav.png`, `evidence/step7-subzero-todo-done.png`, `evidence/step7-subzero-notification-stale.png`. |

## Scenario 54 — step 16b (Push 24 UI gate cleared)
| # | Result | Notes |
|---|---|---|
| 16b. Base-only → Read it → optional + Register to-do (no reload); no duplicate | **Pass** | [Trailblaze TB350 power station](https://stuffit-ui.onrender.com/items/01a1aeab-a8d2-75f1-be15-fd8fc7807faf), bought Oct 20, 2026; `edge-registration-required.pdf`. Unticked optional on first accept → later **Read it** added optional **3 years if you register by Nov 19, 2026** (Not counted yet) + to-do “Register … by Nov 19, 2026” **Due in 11 days**, without reload. Re-read reoffer: optional shows **Not added** until the red “already has” / “Nothing to update: what you have already matches the document” banner. **Note (pre-existing, not a Push 25 fix):** base text says **90 days** but dates are **Oct 20, 2026 → Jan 20, 2027** (3 calendar months; 90-day arithmetic would be Jan 18). Shots: `evidence/s54-16b-optional-and-todo.png`, `evidence/s54-16b-reoffer-banner.png`. |
| 19. Missed label | **Not run** | Already Pass on Push 22; per notes do not redo. |

## Scenario 61 — targeted (step 14, A9, B15 only)
Vehicle: [https://stuffit-ui.onrender.com/items/01a1ae9c-d293-7db2-aaa6-4befe26713e9](https://stuffit-ui.onrender.com/items/01a1ae9c-d293-7db2-aaa6-4befe26713e9). Exact evidence: `/workspace/uat/push25-s61-targeted/results.md` (copied under `evidence/` for screenshots).

Setup for chronology: initial 12 miles reading date changed to **Jan 1, 2025**; purchase Jan 1, 2026 and in-service Jan 15, 2026 left unchanged. Added 14000 @ 2026-11-05, 7000 @ 2026-01-01, 12500 @ 2026-07-01, 500 @ 2026-08-01 (Save it anyway). No clock / other-account / powerstation changes.

| # | Result | Notes |
|---|---|---|
| 14. Confirm lower reading | **Partial** | Before: flagged “lower than an earlier reading”; exclusion + “This reading is correct”. After confirm: “lower than an earlier reading, confirmed by you”; exclusion/button removed. Latest stayed **“14,000 miles on Nov 5, 2026”** (non-newest confirmation Pass). Pace before **and** after: “About 7,592 miles a year, from your readings of Jan 1, 2025 and Nov 5, 2026.” Coverage miles figures unchanged (22,000 left at last reading). Final descending: 14000 2026-11-05; 500 2026-08-01 confirmed; 12500 2026-07-01; 7000 2026-01-01; 12 2025-01-01. Counts-toward-pace consistent with removed exclusion, **not independently numerically proven** (confirmed interior reading does not change oldest/newest endpoints). Newest-date positive branch not tested. Evidence: `evidence/step14-before.png`, `evidence/step14-after.png`. |
| A9. Unit change while readings/mile limits exist | **Pass** (section-level) | Kilometres → Save refused exactly: “The unit cannot change while this vehicle has readings or mile limits: the numbers would mean something else. Remove them first.” No “One or more validation errors occurred.” Unit remained miles. Message is a **section-level** alert below Add reading, **not** adjacent to the unit select (strict field placement not met). Evidence: `evidence/a9-unit-validation.png`. |
| B15. Future reading date | **Pass** (section-level) | 15000 dated 2026-11-06 refused exactly: “A reading cannot be dated in the future.” No generic validation string. No sixth reading persisted. Alert below reading form. Evidence: `evidence/b15-future-validation.png`. |

## Open issues / notes for dev
1. **S61.14** Confirmed interior lower reading: confirmation UX works; numerical contribution to pace/miles not proven when endpoints unchanged.
2. **A9/B15 placement** Plain wording Pass; still section-level, not beside the field.
3. **Step 2/4 limitation** Parts/component dates not shown separately on coverage card.
4. **Application receipt stale** after in-service date update (still shows purchase-based applied range).
5. **Certified length 12 mo** did not auto-calculate end date (manual Jan 1, 2027).
6. **Step 7** Coverage/header stale until navigate; Notifications still prompts Enter date after to-do Done; due 15 days vs plan 14; source-of-start wording not visible.
7. **S54 base 90 days vs Jan 20** (3-month) date math — pre-existing, not introduced by Push 25.
8. Still open from Push 23 (unchanged here): bill-of-sale model miss; reader apply can wipe hand-typed maker coverages; “14 months ago” missing on estimate line.

## Not in this report
- Sweeps (`export-expiry`, `reminder-send`) — separate.
- Full S61 A–F — already reported on `1ed55e3`.
- S54 step 19 — already Pass; not redone.
- Registration completion / clock Missed-label path.
- Wolf / Cove installation; Sub-Zero email / editor / dismiss / delete / quick-add.

## State left
- Alice: Push25 vehicles + Trailblaze + Sub-Zero + S61 chronology vehicle retained. No scenario reset after run. No sweeps. No orphan purge.
- Bob / Carol / Ops: untouched (Ops 2FA still on).
- Global clock: **offset 0** (DB Stager verified at prep; no advances this run).

## Totals (from graded rows above only)
| Block | Pass | Partial | Fail | Blocked | Not run |
|---|---:|---:|---:|---:|---:|
| Push25 steps 1–7 | 5 (1–6) | 1 (7) | 0 | 0 | 0 |
| S54 | 1 (16b) | 0 | 0 | 0 | 1 (19) |
| S61 targeted | 2 (A9, B15) | 1 (14) | 0 | 0 | 0 |

Invalid dated-PDF / regular-item attempt **excluded** from Fail totals (setup correction).

## Evidence paths
- Report (box): `/workspace/uat/retest-2f52761/UAT-retest-2026-11-05-push25-targeted.md`
- Screenshots: `/workspace/uat/retest-2f52761/evidence/`
- S61 exact writeup: `/workspace/uat/push25-s61-targeted/results.md`
- Final Results (UNC): `\\DESKTOP-TD3DQ64\Stuffit\Testing\Scenarios\Results\UAT-retest-2026-11-05-push25-targeted.md`
- Library: `uat-library/runs/UAT-retest-2026-11-05-push25-targeted.md` + INDEX entry
