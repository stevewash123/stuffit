# UAT full run — Scenario 69: Service orders, wide variety (Nov 9, 2026)

- **Build:** Push 48, API efdd913 (started 8:26:10 PM ET). UI ~8:25 PM ET. Staging. No migration. Reader on.
- **Plan:** scenario-69.md (SHA256 `2ce8498267e7ba9575ddc7c2859453079c777e99ba09672e87365c13e25545e8`); RUNPLAN.md. Mode: Full-only.
- **Account:** **P34 Self personal** (vault 3550464), not Alice. See deviation below. Clock Offset 0 (never moved; confirmed after the run).
- **Fixtures:** QA made no new fixtures. The run used Scenario 69's own 12 PDF + JPG twins under `/workspace/uat/scen69/` (and the share folder `Testing\Scenarios\Scenario 69 - Service orders, wide variety\`).
- **Evidence:** `/workspace/uat/scen69/s69-findings.md`; screenshots in `/workspace/uat/scen69/shots/`; export `/home/box/Downloads/warrantycat-export-2026-11-10.zip` (`service_history.csv`, 34 UAT S69 rows).

## Account deviation — Needs CC (plan)

The plan says **Test1 (Alice) personal account only** and **"Do not run this in the shared business P34-Alice Repairs."** Alice's login opens only that business (header "P34-Alice Repairs"; Settings > Profile "Business P34-Alice Repairs"; People: QA Test 1 Owner, QA Test 2 Employee). There is no personal space or account switcher. Chunk A was blocked on Alice and rerun as **P34 Self**, a confirmed personal account. The plan's account assumption does not match the data. **Flag for Claude Code:** either give Alice a personal account, or rewrite Scenario 69 to name a personal test user that actually has one (P34 Self / p34self).

## Results

| Result | Count |
|---|---|
| Pass | 5 |
| Partial | 4 |
| Fail | 3 |
| Inconclusive | 0 |

Orders 02, 04 (required keep), 08 (repair-order read), 09 (required keeps), 10 passed. 01, 03, 11, 12 are Partial. 05, 06, 07 failed. Past dates were accepted. History is newest first. No claim, plan or coverage was created by any order. Clock stayed at 0.

## Per-order results

| # | Vehicle / order | Result | Notes |
|---|---|---|---|
| 01 | Camry · 418827 · 2026-05-18 · 27,640 | **Partial** | Header, oil $95.75, N=5 all pass. Window regulator kept as warranty but pinned to powertrain (to Mar 15, **2029**) instead of basic (**2027**). Rotation left out (either way). |
| 02 | Camry · 214-0083391 · 2026-08-30 · 31,215 | **Pass** | Quick-lube "Full Synthetic Oil Change" mapped to Engine oil and filter; **$81.93** after coupon; N=4. Maintenance later counted from this visit. |
| 03 | F-150 · 6650291 · 2026-01-15 · 31,207 | **Partial** | Close date acceptable. Axle → powertrain 2028; seat heater → B2B 2026; N=1. **Recall 25S99 pinned to bumper-to-bumper** (to Jun 10, 2026), not "(none) - recall". |
| 04 | F-150 · 004417 · 2026-11-03 · 44,880 | **Pass** | Required coolant flush **$187.90** on powertrain (to Jun 10, 2028). Brakes left out; N=3. Belt either-way kept. **No battery warranty created.** Battery (either-way) was wrongly pinned to powertrain — Medium, below. |
| 05 | F-150 · 08-552190 · 2025-07-22 · 26,310 | **Fail** | Read as a **purchase card** on the truck and again on the tire part. No service card, no jobs, no history rows. Tire-term keep could not be tested. Not now clicked; truck brand/date unchanged. |
| 06 | F-150 · 08-561077 · 2026-02-11 · 31,890 | **Fail** | Header pass. Rotation and road-hazard flat repair **left out** (rules misses). Picker offers only Ford truck terms / No coverage — **not** treadwear or road hazard. Ticked both as No coverage. Wiper row missing. N=2 vs 1. |
| 07 | Outback · 77031 · 2026-10-15 · 61,240 | **Fail** | Close date acceptable. Goodwill CVT kept as warranty but **pinned to ended powertrain** (to Nov 8, 2026), not "(none) - goodwill". Brake fluid wrongly kept. Adding the 61,240 reading **moved the powertrain end from Nov 8 to Oct 14**; saved history still says (to Nov 8, 2026). Export has customer_paid **352.80** (UI hid it). |
| 08 | Tucson · PCC-26-0412 · 2026-06-03 · 14,022 | **Pass** | Read as a **repair order**, not a purchase. 0 kept (either-way left out). **No lifetime guarantee created.** Odometer kept from the document. Low: no "N other jobs were left out" line, so jobs cannot be ticked. |
| 09 | Tucson · 5590184 · 2026-09-16 · 19,880 | **Pass** | Required keeps: hose → 2035 (powertrain), strut → 2030 (B2B), campaign 9ZZ → 2035; all repaired under warranty; N=1. Low: part lines became three extra entries; hose **part** on 2030 vs job on 2035. |
| 10 | Street Glide · WO-35512 · 2025-06-14 · 5,032 | **Pass** | Oil $192.70, primary $77.95, trans $77.95, fork seals repaired under warranty, all (to Sep 7, 2026). Inspection left out (either way). N=4. |
| 11 | Polaris INDY · ST-11847 · 2025-11-18 · **1,486 miles** (not hours) | **Partial** | Required keeps on Protection plan (to Dec 2, 2026): plugs $76.98, chaincase $69.99, fuel pump warranty + export **$50.00**. Drive belt / clutch either-way kept. **Carbide runners wrongly kept** ($177.98). N=2 vs 3–5. Kind was Other (no Snowmobile). |
| 12 | Outback · HG-24518 · 2025-04-09 · 41,120 | **Partial** | Required CVT $282.00 and rear diff $89.50 kept. **A/C wrongly kept** ($223.95) on the (later stale) powertrain label. N=3 vs 4. All three still say (to Nov 8, 2026). |

## Export cross-check (`service_history.csv`)

Columns: `date,odometer,order_number,shop,part,work,covered_by,warranty_repair,customer_paid`. Quoted S69 rows only. Dates and odometers match the cards (01-15 / 10-15 close dates for 03 and 07 are acceptable per the key).

**01** (418827, 2026-05-18, 27640, Pine Harbor Toyota):
- Front door window regulator… · `Manufacturer warranty (to Mar 15, 2029)` · yes · 0.00 — **wrong term** (keyed 2027 basic)
- Engine oil and filter · (to Mar 15, 2029) · no · **95.75** — pass
- Engine air filter · (to Mar 15, 2029) · no · 48.80 — either way

**02** (214-0083391, 2026-08-30, 31215, QuickTop Lube, Store #214):
- Engine oil and filter · Full synthetic oil change… · (to Mar 15, 2029) · no · **81.93** — pass

**03** (6650291, 2026-01-15, 31207, Granite Ridge Ford):
- Rearview camera… · `Manufacturer warranty (to Jun 10, 2026)` · yes · 0.00 — **recall pinned to B2B**
- Rear axle pinion seal · (to Jun 10, 2028) · yes · 0.00 — pass
- RH front seat cushion heater element · (to Jun 10, 2026) · yes · 0.00 — pass

**04** (004417, 2026-11-03, 44880, Dunmore's Auto Repair):
- Cooling system · (to Jun 10, 2028) · no · **187.90** — pass
- Serpentine belt · (to Jun 10, 2028) · no · 123.20 — either way
- Battery · (to Jun 10, 2028) · no · 308.99 — **should be (none)**

**05:** no rows (never added).

**06** (08-561077, 2026-02-11, 31890, Tread Masters Tire & Auto, Store #08), both added by hand:
- Tires · Rotate & balance… · covered_by **empty** · no · 0.00 — keyed Michelin treadwear, warranty_repair false
- Rear tire · Flat repair… billed to road hazard… · **empty** · **no** · 0.00 — keyed road hazard, warranty_repair **true**

**07** (77031, 2026-10-15, 61240, Lakeside Subaru):
- CVT control valve body · `Manufacturer warranty (to Nov 8, 2026)` · **yes** · **352.80** — amount is in the export, not the UI; term should be (none) - goodwill
- Spark plugs · (to Nov 8, 2026) · no · 294.20 — either way, stale end
- Brake fluid · (to Nov 8, 2026) · no · 131.85 — **should have been left out**

**12** (HG-24518, 2025-04-09, 41120, Hillside Garage & A/C):
- CVT transmission · (to Nov 8, 2026) · no · **282.00** — keep pass, stale end
- Rear differential · (to Nov 8, 2026) · no · **89.50** — keep pass, stale end
- Air conditioning system · (to Nov 8, 2026) · no · 223.95 — **should have been left out**

**08:** no service rows (0 kept). Odometer 14,022 on Jun 3, 2026 was stored from the document.

**09** (5590184, 2026-09-16, 19880, Seaport Hyundai), six rows all warranty_repair yes, 0.00:
- Coolant reservoir hose · (to Apr 5, **2035**)
- Reservoir hose part · (to Apr 5, **2030**) — inconsistent
- Coolant · (to Apr 5, 2035)
- Liftgate lift strut LH · (to Apr 5, 2030)
- Liftgate lifter assembly part · (to Apr 5, 2030)
- Transmission control module software · (to Apr 5, 2035)

**10** (WO-35512, 2025-06-14, 5032, Iron Ridge Harley-Davidson), all (to Sep 7, 2026):
- Engine oil and filter · no · **192.70**; Primary chaincase · no · **77.95**; Transmission · no · **77.95**; Front fork seals · **yes** · 0.00 — all pass

**11** (ST-11847, 2025-11-18, **1486**, North Country Powersports), all `Protection plan (to Dec 2, 2026)`:
- Spark plugs · no · **76.98**; Chaincase oil · no · **69.99**; Fuel pump assembly · **yes** · **50.00** — required keeps pass (amount only in export)
- Drive belt · no · 195.99; Primary/secondary clutch · no · 96.00 — either way
- Carbide runners · no · 177.98 — **should have been left out**

`coverage.csv` confirms Outback powertrain `end_date=2026-10-14`, `ended_by_miles_on=2026-10-15`, `ended_by_miles_at=61240.0` (moved by order 07). Tire treadwear and road-hazard terms exist on the part (`end_date` 2031-07-22 / 2028-07-22) but were never used on a service row.

## Defects

### High — Needs CC

1. **Tire-part terms are never offered or used.** Order 05, the purchase proof the Michelin treadwear term needs, was read as a purchase on both the **vehicle** and the **part**, not as a service order. On the F-150 the card proposed overwriting the truck: "Brand Conflict: choose one / Keep yours: Ford / Use the document's: Michelin (high confidence)" and "Date Conflict … Keep yours: 2023-06-10 / Use the document's: 2025-07-22" (`s69-C-05-card.png`, `s69-C-05part-card.png`). Order 06 then left out both required Keeps: "Nothing on this order is service on a covered part." Left out: "Tires: Rotate & balance - lifetime (no charge) · $0.00" and "Rear tire: Flat repair - plug/patch (nail in tread), billed to road hazard plan RH-08-552190 · $0.00" (`s69-D-06-card.png`). After ticking them, the picker offered only "No coverage (history only)", "Manufacturer warranty (to Jun 10, 2026)", "Manufacturer warranty (to Jun 10, 2028)" — not treadwear (to Jul 22, 2031) or road hazard (to Jul 22, 2028). Export `covered_by` is empty; flat repair `warranty_repair=no` (keyed true). The part page also has **no Maintenance panel**, so the "Tire rotation, 7,500 mi" Overdue check could not run (`s69-H-maint-f150.png`). This is the main finding the pack was built to catch.

2. **Ended-on-miles handling is wrong and unstable.** After the 62,100-mile reading the Outback powertrain badge/range was **"Ended Nov 8, 2026"** / "Nov 20, 2021 to Nov 8, 2026", i.e. the day before today's reading, not the 60,000-mile crossing (`s69-A-outback-coverage-status.png`). Order 07 at 61,240 mi was then treated as running: goodwill CVT "repaired under warranty · Manufacturer warranty (to Nov 8, 2026)" instead of "(none) - goodwill" (`s69-E-07-card.png`). Adding that document reading **moved the coverage end to Oct 14, 2026** ("Ended by miles on Oct 15, 2026: your odometer read 61,240 miles that day…") (`s69-E-07-coverage-after.png`). All six saved Outback entries, including 12 and 07, still say **(to Nov 8, 2026)** in history and in the export (`s69-E-07-hist.png`, `s69-E-12-hist.png`).

### Medium — Needs CC

3. **Coverages have no name field**, so service labels are only "Manufacturer warranty (to \<date\>)" or "Protection plan (to \<date\>)". The card cannot re-pick a kept job's coverage. Order 01 window regulator went to powertrain **(to Mar 15, 2029)** instead of basic **(to Mar 15, 2027)** (`s69-B-01-card.png`).

4. **Order 03 recall is pinned to bumper-to-bumper.** "Rearview camera image processing module: Reprogrammed per safety recall 25S99 · repaired under warranty · Manufacturer warranty (to Jun 10, 2026)" (`s69-C-03-card.png`). Key: `(none) - recall`; "Must not be pinned to bumper-to-bumper as if it were a defect claim." Export confirms the same `covered_by`.

5. **Wrongly kept jobs, and the card cannot un-keep them.**
   - 12 A/C: "Air conditioning system: A/C performance check, evacuate and recharge · you paid $223.95 · Manufacturer warranty (to Nov 8, 2026)" — bumper-to-bumper had already ended (`s69-E-12-card.png`).
   - 07 brake fluid: "Brake fluid: Brake fluid exchange · you paid $131.85 · Manufacturer warranty (to Nov 8, 2026)" (`s69-E-07-card.png`).
   - 11 carbide runners: "Carbide runners: Replace carbide runners · you paid $177.98 · Protection plan (to Dec 2, 2026)" (`s69-G-11-card.png`).

6. **Order 04 battery pinned to powertrain.** "Battery: Tested and replaced battery · you paid $308.99 · Manufacturer warranty (to Jun 10, 2028)" (`s69-D-04-card.png`). Key: `(none)`. (Either-way keep is allowed; the coverage assignment is not.) No battery warranty was auto-created.

### Low

7. **$0 / warranty jobs hide the customer amount** on the card and in history. Export still has order 07 CVT **352.80** and order 11 fuel pump **50.00**. (`s69-E-07-card.png`, `s69-G-11-card.png`)

8. **Order 08** shows "Nothing on this order is service on a covered part…" but **no** "N other jobs were left out" line and no tickable rows (keyed N=4–7) (`s69-F-08-card.png`).

9. **Order 06 wiper row is missing** from the left-out list (`s69-D-06-card.png`).

10. **Order 09 part lines became separate entries** (6 instead of 3). "Reservoir hose part: Hose - reservoir 25450-N9100" is on **(to Apr 5, 2030)** while the hose job is on **2035** (`s69-F-09-card.png`, `s69-F-09-hist.png`).

11. **F-150 bumper-to-bumper** (already ended on time) still shows **"-9,050 miles left at your last reading (45,050 on Nov 9, 2026)"** and "Enter your odometer to check" even though a reading exists (`s69-A-f150.png`). Outback basic has the same pattern.

12. **F-150 Parts list** summarizes the tires as **"Warranty until Jul 2028"** (road hazard) rather than Jul 2031 (treadwear).

13. **Polaris ESC appears twice** (Your coverage and Add-on protection) and creates a to-do **"Add the rest of your Polaris plan"** (`s69-A-polaris.png`).

14. **No Snowmobile kind** (Polaris stored as Other) and **no road-hazard plan type** ("What it is" is only Warranty extension / Accident cover / Insurance).

## Passes (also)

- Order 02, including quick-lube oil wording and Camry maintenance **"Last done Aug 30, 2026 at 31,215 miles. Next due by Feb 28, 2027 or 36,215 miles"** (`s69-H-maint-camry.png`).
- Order 10 (all required keeps and N=4).
- Order 04 required keep; no battery warranty created.
- Order 08 read as a repair order; no workmanship guarantee created.
- Order 09 required keeps (hose, strut, campaign).
- Polaris recorded in **miles (1,486)**, not 52.3 hours.
- JPG twin of 02 matches the PDF (same date, odometer, order, $81.93, N=4); Not now added nothing (`s69-H-jpg02.png`). Shop on the JPG omitted "Store #214".
- Service history newest first; no claims, plans or coverages created by any order; Ford / Hyundai / Camry / Street Glide / Polaris factory end dates unchanged (Outback powertrain is the exception, High #2).
- Past purchase and in-service dates were accepted. VINs accepted (synthetic, valid check digits).

## Needs code / product follow-up

1. **Needs CC (plan):** Alice has no personal account; Scenario 69 cannot be run as written. Give Alice a personal space, or name a personal user that has one.
2. **Needs CC (High):** Service-read invoices that belong to a **part** (new tires, rotation, road-hazard repair); offer the part's terms in the coverage picker; Maintenance panel on parts.
3. **Needs CC (High):** Ended-on-miles: do not backdate the term to the day before a later over-limit reading; do not treat a same-day over-limit visit as running; do not move the end when an earlier over-limit document reading arrives; refresh or avoid stale "(to \<date\>)" labels on saved entries.
4. **Needs CC (Medium):** Coverage name field (or labels that distinguish basic vs powertrain); do not pin recalls to B2B; allow un-keeping a job; do not pin battery / goodwill / ended-term work to a running or ended powertrain when the key is (none).
5. Lows 7–14 as listed.

## Evidence

- `/workspace/uat/scen69/s69-findings.md`
- `/workspace/uat/scen69/shots/` (s69-A-* through s69-H-*)
- `/tmp/s69x/service_history.csv` from warrantycat-export-2026-11-10.zip
