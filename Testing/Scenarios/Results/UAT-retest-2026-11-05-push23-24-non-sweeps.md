# UAT retest: Push 23 Vehicles + Private sale (S61) — non-sweeps only
Build: API `1ed55e3` (started 4:34 PM ET Nov 5, verified). UI Last-Modified Thu, 05 Nov 2026 21:37:56 UTC = **4:37 PM ET** (etag `W/"1d2cfd45a5eb42db5409a1a99d517e66"`, bundle `main-MAOTUOD4.js`). Mode: Full-only. Browser run ~5:17–5:53 PM ET Nov 5.
Notes: `CHANGES-push-23-vehicles-slice-1-2026-11-05.md`, `CHANGES-push-24-todo-list-reload-2026-11-05.md`. Plan: [scenario-61.md](sets/browser-plans/scenario-61.md). Alice+Bob scenario-reset by DB Stager before run (migrations `VehiclesSlice1` + `VehiclePrivateSale`, `--seed` makers + Private sale confirmed). Reader on (`item-warranty-v6`). Clock restored to **offset 0** and independently GET-verified by DB Stager on `1ed55e3` at **5:53 PM ET**; Alice items/readings untouched on restore.

**Push 24 UI gate:** `bd82dda` is **not** confirmed. UI Last-Modified remains 4:37 PM ET through filing (~5:55 PM ET); index/main JS carry no `bd82dda` string. See `/workspace/uat/export-s61/verification.md`. Therefore **Scenario 54 step 16b is Blocked (build gate)**. Step 19 (Missed label) already **Pass** on Push 22 / `bb416b8` — **not redone**.

**Sweeps:** intentionally **not run** this report. Separate suite after this delivery.

## Headline
Scenario 61 Vehicles + Private sale mostly works end-to-end: add vehicle, odometer, time-and-miles end/reopen, private-sale defaults, transfer terms, card-benefit suppression, Bob isolation, and export schema. Open issues: bill-of-sale **model** not extracted (A8); generic validation wording (A9, B15); confirmed lower-reading flag does not make that reading the latest (B14, plan contradiction); ended-by-miles date shows **Mar 10** on detail vs **Mar 9** on top (C22); claim screen says **Applies** where plan expects uncertainty for estimate-alone (C27); reader apply removed all 3 hand-entered maker coverages (D29); Ops Admin Private-sale refuse **Blocked** by 2FA (F40). Stale-odometer check (B17) **Partial**. Due-day miles reminder (C26) **Partial** (not verified on due day).

## Push 24 / S54 (non-sweep)
| # | Result | Notes |
|---|---|---|
| 16b. Base-only → Read it optional + Register to-do (no reload) | **Blocked** | Push 24 UI `bd82dda` not proven deployed (Last-Modified still 4:37 PM ET). Not run. |
| 19. Missed label past deadline | **Not run** | Already Pass on Push 22 (`bb416b8`). Per notes: do not redo. |
| 18. 15s Undo toast | **Not checked** | Optional; not caught this pass. |

## Scenario 61 — Part A: add a vehicle
| # | Result | Notes |
|---|---|---|
| 1 | **Pass** | My Items offers **Add a vehicle** beside Add a purchase. |
| 2 | **Pass** | Nickname "UAT Dad's truck", Truck, 2024 Ford F-150 XLT, VIN, New, bought 2025-01-01, $52,000, 12 miles. Page shows kind/year/trim/bought new, VIN, first reading **12 miles on Jan 1, 2025**. No order/card fields. Item `01a1adcb-2599-7a31-b709-d8e71fa06290`. |
| 3 | **Pass** | Boat: Hull number label; year next year accepted; no check-digit note. (Deleted in step 10; absent from final export.) |
| 4 | **Pass** | Year 1899 / 2028 and date bought 2026-11-06 refused; nothing half-made in My Items. |
| 5 | **Pass** | Bad check-digit VIN: gentle note; vehicle still saves ("UAT BadVIN Used Car"). |
| 6 | **Pass** | Used → first put in service left empty → "not known"; nothing guessed. |
| 7 | **Pass** | Vehicles only filter; kind badge on vehicles; toaster left out. |
| 8 | **Partial** | Synthetic bill of sale attached + Read it: other fields offered as suggestions; **model not extracted**. VIN/year not read (Not built — correct). Item left: "UAT Bill of Sale Vehicle". |
| 9 | **Partial** | Edit vehicle → change unit to kilometres **refused** while readings/mile limits exist, but wording is **generic** (not a plain field message). |
| 10 | **Pass** | Boat deleted; gone from My Items and from final `vehicles.csv` (7 rows, no boat). |
| 10a | **Pass** | Classic bought 1975-06-01 accepted ("UAT Classic 1975"). Appliance floor 1990 still refused on Add a purchase path (spot-checked via UAT Old Toaster path). |
| 10b | **Pass** | Make box "Fo"/"Hon" shows seeded shared brands (Ford, Honda); no "not yet in the shared list" badge. DB Stager confirmed 74 new makers + Honda. |

## Scenario 61 — Part B: odometer
| # | Result | Notes |
|---|---|---|
| 11 | **Pass** | Reading 14,000 (later edited in sequence) / subsequent adds save newest-first with date; pace needs spacing. |
| 12 | **Pass** | Mid-year readings produce pace "About N miles a year, from your readings of …" and an **estimated** today figure labelled estimated, not in the readings list. Final pace at clockcheck: **about 18,717 miles a year** from Jan 1, 2025–Nov 5, 2026. |
| 13 | **Pass** | Lower reading asks once; Cancel saves nothing; Save anyway keeps flagged "lower than an earlier reading"; latest/pace ignore it until confirmed. |
| 14 | **Partial** | "This reading is correct" / confirmed flag **works**, but the older confirmed reading **cannot become the latest** — contradicts plan expected "It now counts as the latest." Treated as plan/product contradiction, not a silent miss. |
| 15 | **Partial** | Tomorrow's date refused, but with **generic** validation wording (same class as A9). |
| 16 | **Pass** | Edit value/date and delete reading both work; odometer lines follow. Final counted readings on Dad's truck (export): 12 @ 2025-01-01, 16000 @ 2026-03-10, 33000 @ 2026-09-01, 34500 @ 2026-11-05 — all `source=Entered`, `lower_than_earlier=no`, `counted=yes`. |
| 17 | **Partial** | Clock +426 days → app date **Jan 5, 2028** (5:52 PM ET). Headline **34,500 miles on Nov 5, 2026** shows orange **"last reading 14 months ago"**. Estimate **"About 56,330 miles today (estimated)"** lacks the stale label. Historical rows show only "You enter / edit". Pace still dated Jan 1, 2025–Nov 5, 2026. Time-only coverage present; **mileage-coverage stale label unverified**. Shot: `/cursor/stores/store-5417ec58-ea75-4baf-b2e2-a6e69ffc43ca/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/4ade02cde1db2c0fd0241f3cf5a116a1d28ff55cd4930c23fabb85eb7924bf28.png`. Notifications at that clock: export-ready only — no miles reminder (feeds C26). |

## Scenario 61 — Part C: time-and-miles coverage
| # | Result | Notes |
|---|---|---|
| 18 | **Pass** | Maker Powertrain with mile limit shows "Until … or N miles, whichever comes first", remaining miles at last reading with that reading's date, and (with pace) which comes first. |
| 19 | **Pass** | With readings removed down to one: "Add odometer readings to see which comes first"; miles not watched; reminders use date only. |
| 20 | **Pass** | Bumper-to-bumper and Roadside unlimited each have their own line; unlimited reads "with unlimited miles". |
| 21 | **Pass** | Unlimited miles with no end date refused. |
| 22 | **Partial** | Reading at/over limit ends coverage by miles. **Date inconsistency:** detail says ended by miles on **Mar 10, 2026**; top/summary showed **Mar 9, 2026**. Other coverages unaffected. |
| 23 | **Pass** | Correct/delete the over-limit reading → coverage opens again with its own end date. |
| 24 | **Pass** | Fast pace / estimate past limit with no reading over it: "You have probably passed the limit. Enter your odometer to check." Coverage stays **Active** (estimate alone never ends it). |
| 25 | **Pass** | Home / items list end lines use earlier of date and estimated mile end; estimated labelled when from miles. |
| 26 | **Partial** | Due-day miles reminder **not verified** on the due day. At offset 426, notifications showed export-ready only — no miles reminder observed. Reminder-estimate wording therefore Not fully checked. |
| 27 | **Partial** | Something broke (defect) on the truck: ended-by-miles ruled out with reading named (ok). **Estimate alone shows "Applies"** where the plan expects uncertainty / "maybe". |
| 28 | **Pass** | Appliance warranty unchanged: no miles anywhere; no mile field on its coverage form. |

## Scenario 61 — Part D: warranty reader
| # | Result | Notes |
|---|---|---|
| 29 | **Partial** | Reader recognized **numeric** mile limit, **unlimited** miles, and **absent** distance (empty miles) correctly; document words quoted in terms. **Defect candidate:** applying the reader warranty **removed all 3 hand-entered maker coverages** on the truck. |
| 30 | **Pass** | Same booklet on an appliance → no mile limit stored. |

## Scenario 61 — Part F: Private sale
| # | Result | Notes |
|---|---|---|
| 33 | **Pass** | Seller picker offers shared **Private sale** (no unverified badge). Saved without dealer. |
| 34 | **Pass** | Sentence "Bought in a private sale. WarrantyCat assumes nothing…" shown. No "Not set up yet", no suggested coverage, no store return window, no maker warranty from purchase date. My Items "Nothing applies" (not Needs info); Home needs-info excludes it. |
| 35 | **Pass** | Ordinary toaster with store Private sale: same sentence/behavior. |
| 36 | **Pass** | Staged synthetic **UAT Card** (Chase Sapphire Reserve product; payment method `01a1addc-155a-7dd1-a1c5-8f590fdfc6fb`) with confirmed ReturnProtection (90d) + PurchaseProtection (120d) — copied existing shared benefit terms, structured max null; no ExtendedWarranty. On private-sale purchase: **no return-extension** offered/added; **purchase protection still offered**. (Card fixture staged by DB Stager; not newly researched issuer promises.) |
| 37 | **Pass** | Not-transferable maker booklet on private-sale vehicle: listed with "Original purchaser only. Not transferable.", labelled **Not counted: not transferable**; adds nothing to days left / badge / Home / reminders. Correct transfer term to **Yes** → counts. |
| 38 | **Pass** | Transferable (or silent) booklet counts as normal; hand-added coverage counts as normal. |
| 39 | **Pass** | Private sale not in account's own My stores and brands list; cannot rename/delete. |
| 40 | **Blocked** | Ops (Test4) Admin Companies / Retailers refuse for Private sale **not run**. StuffIt rejected **two** user-supplied two-step codes ("That code is not correct."). No admin checks performed; **no security / 2FA changes** made. |
| 41 | **Pass** | Export `purchases.csv` has `private_sale` column; 5 Private sale rows = **"yes"**. `coverage.csv` marks not-transferable not-counted = **yes** (Private Car 3). See export verification. |

## Scenario 61 — Part E: export and isolation
| # | Result | Notes |
|---|---|---|
| 31 | **Pass** (limits) | Export everything downloaded. `vehicles.csv` 14 cols / 7 vehicle rows; `odometer_readings.csv` 12 cols incl. source / lower_than_earlier / confirmed_by_you / counted_in_pace_and_coverage (4 rows, all counted); `coverage.csv` mile columns present (`mile_limit`, `unlimited_miles`, `mile_start`, `ended_by_miles_on`, `ended_by_miles_at`, `estimated_miles_end`, `date_end_before_miles`, `not_counted_private_sale_not_transferable`). **Limit:** final state did **not** exercise unlimited / ended-by-miles / lower-unconfirmed rows in the CSVs, so those cell values are unproven in export. Evidence: `/workspace/uat/export-s61/verification.md` and `/workspace/uat/export-s61/x/*.csv`. |
| 32 | **Pass** | Bob (Test2) opening Alice vehicle URLs → **Not found** only. |

### Export note (not a Fail by itself)
`purchases.csv` non-private-sale rows leave `private_sale` **blank** (not `"no"`). Spec only requires `"yes"` beside private-sale purchases — blank on others is **not necessarily a defect**. `my_stores_and_brands.csv` also blanks `private_sale` for brand rows (no store/private-sale seller rows listed there).

## Open issues for dev
1. **A8** Bill-of-sale reader: model not extracted (other fields ok). Synthetic fixture.
2. **A9 / B15** Refusals use generic validation wording instead of plain beside-field messages.
3. **B14** Confirmed lower reading does not become latest (plan says it should) — confirm intended behavior.
4. **B17** Stale label on estimate / mileage-coverage figures incomplete; historical rows lack "14 months ago".
5. **C22** Ended-by-miles date Mar 10 (detail) vs Mar 9 (top).
6. **C26** Miles reminder on due day not observed (needs dedicated due-day pass or `run-reminders`).
7. **C27** Estimate-alone claim route says **Applies** instead of uncertainty/"maybe".
8. **D29** Applying reader warranty removed all 3 hand-entered maker coverages.
9. **F40** Ops 2FA blocked Admin Private-sale refuse check (codes rejected twice).

## Not built / decided (not graded Fail)
VIN decoding / door-sticker photo; VIN/year/in-service never read from documents; readings mined from invoices/photos; S3.5.4–6; parts; odometer prompts. Decided: late earlier-dated reading does not flag a later lower one; unit locked once readings/mile limits exist; coverage start before 1990 still refused; changing seller to Private sale later does not re-check saved coverage.

## State left
- Alice: S61 vehicles/items retained (Dad's truck + private-sale cars/toaster, bill-of-sale vehicle, classic, BadVIN, appliance, staged UAT Card). No scenario reset after the run. No sweeps. No orphan purge.
- Bob: isolation probe only; unchanged otherwise.
- Carol / Ops: untouched (Ops 2FA still on; no admin mutations).
- Global clock: **offset 0**, GET-verified on API `1ed55e3` at 5:53 PM ET by DB Stager.
- Export zip retained under `/workspace/uat/export-s61/`.

## Not in this report
- Sweeps (`export-expiry.md`, `reminder-send.md`) — **separate report next**, per Steve.
- Scenario 54 step 16b — Blocked pending proven Push 24 UI.
- Scenario 54 step 19 — already Pass; not redone.

## Totals (computable from rows above)
| Block | Pass | Partial | Fail | Blocked | Not run / Not checked |
|---|---:|---:|---:|---:|---:|
| S54 (Push 24 gate) | 0 | 0 | 0 | 1 (16b) | 2 (19 Not run; 18 Not checked) |
| S61 Part A (1–10b) | 10 | 2 (8, 9) | 0 | 0 | 0 |
| S61 Part B (11–17) | 4 | 3 (14, 15, 17) | 0 | 0 | 0 |
| S61 Part C (18–28) | 8 | 3 (22, 26, 27) | 0 | 0 | 0 |
| S61 Part D (29–30) | 1 | 1 (29) | 0 | 0 | 0 |
| S61 Part F (33–41) | 8 | 0 | 0 | 1 (40) | 0 |
| S61 Part E (31–32) | 2 | 0 | 0 | 0 | 0 |
| **S61 A–F graded** | **33** | **9** | **0** | **1** | **0** |
| **All rows this file** | **33** | **9** | **0** | **2** | **2** |

