# UAT retest: Push 28 — typed maker warranty stays with the maker (+ P26/P27 fixes)

**Test date:** Friday **Nov 6, 2026** (~1:15–1:54 PM ET).  
**Live build under test (actual):** API **`6503be1`**, `/api/version` `startedAt=2026-11-06T17:45:25.5971589+00:00` → **12:45:25 PM ET** Nov 6, Staging.  
**Push 28 notes commit (prep target):** API `02cca5d` / UI `6d037ce` — **not** the live commit when this run executed.  
**Attribution rule:** Every grade below is observed on **`6503be1`**. The notes/live commit mismatch is recorded; it is **not** used to hide, soften, or reassign observed defects. Failures and Partials on `6503be1` stand as written.

**Notes:** `CHANGES-push-28-typed-maker-warranty-stays-with-the-maker-2026-11-06.md`  
**Mode:** Full browser, **targeted** Push 28 Fixed + new S3.2.12 Alice steps only. Account: **Alice only** (vault-backed UI session). **No** Bob/Test2. **No** clock advances. **No** sweeps. **No** orphan purge. **No** scenario reset. Only new `P28 …` fixture items created/updated.

**Evidence sources (box):**  
- `/workspace/uat/push28-prep/prep-brief-2026-11-06.md`  
- `/workspace/uat/push28-prep/interim-Push28-S62-23-13-14-2026-11-06.md`  
- `/workspace/uat/push28-prep/interim-batch2-2026-11-06.md`  
- `/workspace/uat/push28-prep/interim-batch3-2026-11-06.md`  
- Notes: `/workspace/uat/bot-rules/CHANGES-push-28-typed-maker-warranty-stays-with-the-maker-2026-11-06.md`

**Screenshots:** `/cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/` (hashes cited below).

## Headline

On live API **`6503be1`**, the Push 27 reader/prorated and mileage-wording fixes **Pass** (S62.23 / .13 / .14 / .17 / .11). Auth logo eye-check **Pass**. Start-date refresh **Passes** from the To do page and Notifications, but remains **Partial** from the item To do card (stale notification action + badge). Document-first superseded amber badge **Passes**; My Items list note is still absent → **Partial** for P26-1 revised (and prior typed-before-document Fail is **by design**, not re-failed). Typed private maker-policy offers for Cove **did not appear** on a second item or Add a purchase → **Fail** on this build for the private-offer path. Bob privacy was **Not run** (dependency gap: Alice private offer never exposed, so privacy cannot be claimed Pass). Mixed-confidence offer sorting and waiting New Item re-check were **Not testable / Not run**.

## Totals (graded rows only — no invented full completion)

| Check | Result |
|---|---|
| Auth logo (`/login` RockyCarBall) | **Pass** |
| S62.23 free + prorated stages from synthetic tire PDF | **Pass** |
| S62.13 “ends at 88,000 miles on the odometer” | **Pass** |
| S62.14 no-install → start-date to confirm; finish on install entry | **Pass** |
| S62.17 My Items “Prorated: you pay a share” | **Pass** |
| S62.11 detach → date-only + Miles no longer watched | **Pass** |
| P26-3B A item To do card refresh | **Partial** |
| P26-3B B To do page refresh | **Pass** |
| P26-3B C Notifications refresh | **Pass** |
| P26-1 revised amber “Probably replaced…” (document first, then typed) | **Pass** |
| P26-1 revised My Items “Your own entry may be out of date” list note | **Partial** (absent) |
| P26-1 dismissal persistence | **Not run** (no list note/X to dismiss) |
| S3.2.12 Alice creator typed 12-mo Cove (item shows coverage) | **Pass** (creator coverage only) |
| S3.2.12 second same maker/category private typed offer | **Fail** |
| S3.2.12 Add a purchase / New Items typed offer | **Fail** (only verified/shared Cove 2-year shown) |
| S3.2.12 retype 12 → no duplicate; edit 12→24 on item | **Pass** (item-level); private-policy update **not proved** |
| S3.2.12 waiting New Item re-check | **Not run** (0 waiting) |
| Offers sorted by confidence (mixed verified+typed) | **Not testable** |
| S3.2.12 delete coverage / maker-policy retention | **Inconclusive** |
| S3.2.12 vehicle negative (no offer to later vehicles) | **Pass** (unrelated Honda Lawn & garden placeholder noted) |
| S3.2.12 Bob/Test2 not offered Alice’s entry | **Not run** (dependency gap) |
| S62.14 optional: link item that already has coverage → not newly marked | **Not run** |
| S62.23 export/`prorated_you_pay_a_share` flag | **Not run** |
| S62.12 Bob API isolation | **Not run** (out of scope; still blocked historically) |

**Summary counts (rows above):** **12 Pass**, **3 Partial**, **2 Fail**, **0 Blocked**, **1 Inconclusive**, **1 Not testable**, **5 Not run**.

---

## Environment / UI proof

- App: https://stuffit-ui.onrender.com  
- After in-app “A new version of WarrantyCat is ready.” → **Reload**, `/api/version` returned `commit=6503be1`, `startedAt=2026-11-06T17:45:25.5971589+00:00` (**12:45:25 PM ET**), Staging.  
- Prep brief had matched `02cca5d` at ~10:41 AM ET; this execution ran after a later deploy.  
- Auth logo: Rocky lying with four round icons above the WarrantyCat wordmark.  
- Shot: `file:///cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/6fdd95e525b8113517e8a358f5bfc866475a3329294f3125766bbe4793d08bad.png`

## Fixtures created (Alice; prior data preserved)

| Fixture | URL |
|---|---|
| P28 Truck (2024 Ford F-150, new Jan 1 2025, 38k @ purchase; reading 40k Nov 6 2026) | https://stuffit-ui.onrender.com/items/01a1b20e-81cf-710a-8f40-8d6673d2f412 |
| P28 Tires (Michelin, install Sep 1 2026 @ 38k; synthetic PDF applied) | https://stuffit-ui.onrender.com/items/01a1b210-280e-79ee-977b-5b97717fd455 |
| P28 No Install (Michelin; install entered Oct 15 2026) | https://stuffit-ui.onrender.com/items/01a1b213-4312-7c18-9192-ec31740acc86 |
| P28 Battery (linked then taken off truck) | https://stuffit-ui.onrender.com/items/01a1b21a-169f-710b-8ccf-d8d087197943 |
| P28 SubZero A / B / C (start-date refresh paths) | https://stuffit-ui.onrender.com/items/01a1b21b-6161-7de9-82c8-d87fda37db63 · https://stuffit-ui.onrender.com/items/01a1b21b-ec6c-7326-96f0-583a67d22eeb · https://stuffit-ui.onrender.com/items/01a1b21c-1b0a-7ce8-84a6-a69e5298b1f1 |
| P28 NoteAfterDoc Reader (document first, then typed) | https://stuffit-ui.onrender.com/items/01a1b22f-c547-732b-9b68-14e4bccad125 |
| P28 Maker Policy A / B / C dishwasher (Cove) | https://stuffit-ui.onrender.com/items/01a1b222-e3f3-7c3d-8d31-425e6c071bd9 · https://stuffit-ui.onrender.com/items/01a1b225-08bb-7f90-941a-cca9d2852d75 · https://stuffit-ui.onrender.com/items/01a1b226-504c-760c-9a80-e5d86d1e6723 |
| P28 Maker Vehicle Honda / Later Honda | https://stuffit-ui.onrender.com/items/01a1b229-9dc6-7e92-836a-c58b1297cdf7 · https://stuffit-ui.onrender.com/items/01a1b22a-d703-7c1d-b1c3-2b1ea2d7c681 |

Fixture PDFs:  
- `/workspace/uat/sample/tire-warranty-50000-72mo-prorated-after-36-SYNTHETIC.pdf` (md5 `e6ed2d0620b25ddc49086fecb1d4db53`)  
- `/workspace/uat/sample/standard-appliance-limited-warranty.pdf` (md5 `2b955e94690a817336edbebf46d7d9a1`)

---

## A. Push 26/27 fix retests (on `6503be1`)

### S62.23 — free 36 mo + prorated stage from synthetic tire PDF — **Pass**

Applied `tire-warranty-50000-72mo-prorated-after-36-SYNTHETIC.pdf` to saved **P28 Tires** (item-page apply, not New Item). Two coverages:

1. `Manufacturer warranty · UAT Tire Co`, Sep 1 2026–Sep 1 2029 (free stage). Text: “Until Sep 1, 2029 or 50,000 miles, whichever comes first.” Quotes 50,000 miles / 72 months from install; endpoint **88,000 miles on the odometer**; 48,000 miles left at last reading 40,000.  
2. `Manufacturer warranty (Prorated: you pay a share) · UAT Tire Co`, Sep 1 2029–Sep 1 2032. Quotes: “After 36 months and through the end of the 72-month / 50,000-mile term, coverage is prorated.”

Shot: `9019f83eeee8162cedd13d7e5b607ddb14800c46c111431dc72ebd4b96856cb0.png`  
Export/`prorated_you_pay_a_share` column: **Not run** this batch.

### S62.13 — 88,000-mile odometer endpoint wording — **Pass**

On P28 Tires coverage: “It ends at 88,000 miles on the odometer.”  
Truck Parts row: `Warranty until Sep 2029 or 50,000 miles, ends at 88,000 miles on the odometer`.  
Shot: `708a15cec1be846a1fee3784b98d4808fdc461bb360b1f92f3be4a073bb1095d.png`

### S62.14 — no install day → start-date to confirm; finish on entry — **Pass**

Before install: `Installed: day not known`; warning `Add the day it was installed so its warranty counts from then.`; typed Michelin counted from purchase Oct 1 2026 with start-confirm text; to-do `Enter the start date of your Michelin warranty on P28 No Install`.  
After Oct 15 2026 install: warning gone; coverage Oct 15 2026–Oct 15 2027; to-do Done **without reload**.  
Shots: `6349805cdef3c69dce748a3cb9735f9cf0e0fb3b10ba779b8232beca09a936f6.png`, `2e447d4b10863a655c49132b80c6961be3f85de92ba495727fe323a0434da40b.png`  
Optional “link item that already has coverage → not newly marked”: **Not run**.

### S62.17 — My Items prorated chip — **Pass**

My Items row for P28 Tires: “Part of P28 Truck” + chip **“Prorated: you pay a share”**; row line “Manufacturer warranty until Sep 1, 2029” (free stage).  
Shot: `09e17877af5d7667ede37a129c15c5a49b5636763d4ee8167a693e043a7a9b96.png`

### S62.11 — detach wording — **Pass**

P28 Battery linked to truck (install Oct 1 2026 @ 39,000; Michelin 12 mo + 12,000 mi with “whichever comes first” while attached — expected). After **Take it off**: “Until Oct 1, 2027, counted by date. … Miles no longer watched. The last known mile end was 51,000 miles … Reminders use the date only.” **No** “whichever comes first.” History: “Earlier P28 Truck: Oct 1, 2026 (39,000 miles) to Nov 6, 2026”.  
Shot: `1a7e1100e1c8e0fca19599cca1c1e2d4139367173dd586a59149edde42a01eca.png`

### P26-3B — start-date refresh without reload

| Path | Result | Evidence |
|---|---|---|
| A. Item To do card (SubZero A) | **Partial** | Dates updated immediately (Until Nov 6 2028 → Oct 15 2028); to-do card cleared. Header badge stayed “2 unread, 1 to do” (start-date tasks not counted in “to do”; unread unchanged). Notifications list still showed “Enter the date” action afterward. Item: `01a1b21b-6161-7de9-82c8-d87fda37db63` |
| B. To do page (SubZero B) | **Pass** | Saved Oct 15 2026: card removed; unread 4→3 immediately; coverage Until Oct 15 2028. Shot: `f702a20d0dda7413932e37c4a96d75ad714052ea13cc98d008854a01ffa6046f.png` |
| C. Notifications (SubZero C) | **Pass** | Saved Oct 15 2026: unread 3→2 immediately; coverage Until Oct 15 2028. Shot: `ac369207381b2d6e537fa3cd5b250f1993db67151ceb5c1dc8dbbce35fcab53d.png` |

Note: Add-coverage dialog dropped the 12-month length once (no end date); Starts/Ends set manually — operational observation, not graded as product Fail.

### P26-1 revised — document first, then typed maker — amber **Pass**; list note **Partial**; dismissal **Not run**

**Clarification vs prior Push 26 Fail:** Push 28 notes state typed-before-document replacement on an ordinary item is **by design**. That earlier Fail is **not** reasserted. This retest used the prescribed **document-first** sequence.

- Route that worked: **Add a purchase** → Choose File `standard-appliance-limited-warranty.pdf` → keep “Add this warranty…” → Refrigerators / Samsung RF28R7551SR → Save. (Initial item-page attach on `P28 Note After Doc` returned “That document doesn't read as a warranty…”)  
- Item `P28 NoteAfterDoc Reader` (`01a1b22f-c547-732b-9b68-14e4bccad125`): 3 document policies, then hand-added Samsung Manufacturer 12 months → **4** policies.  
- Typed row shows amber **“Probably replaced by the policy read from your document”** → **Pass**. Shot: `4389dc925dc8ff04e133f16c7beb57d1c6082d012cb8c7f79f70d46ff3b95d03.png`  
- My Items row (`/items?q=P28%20NoteAfterDoc%20Reader`): Active / Samsung / “Manufacturer warranty until Nov 6, 2027” — **no** “Your own entry may be out of date” → **Partial**. Shot: `49455c73d817d078f087345aeceb8fab777ad50992b4b4de3624ce7ab5b8d766.png`  
- Dismissal persistence: **Not run** (no list note/X).

---

## B. Push 28 new behavior (S3.2.12 + confidence + logo)

### Auth logo — **Pass**

`/login` after Reload: Rocky lying with four round icons above wordmark. Shot cited above.

### Offers sorted by confidence — **Not testable**

No mixed verified + typed (“typed in by hand”) offer list appeared. Actual Cove offers observed were only the single verified/shared **Cove Manufacturer warranty, 2 years**. No card/extended-benefit fixture used. Conservative: **Not testable**, not Pass.

### S3.2.12 — Alice typed maker policy (Cove / Major appliances)

Whirlpool dishwasher was unsuitable (shared list already holds a verified 1-year). Used allowed similar listed maker/category: **Cove / Major appliances**.

| Sub-check | Result | Notes |
|---|---|---|
| Creator A: type 12-mo Cove Manufacturer | **Pass** (item coverage) | `01a1b222-e3f3-7c3d-8d31-425e6c071bd9` shows one active coverage. No self-offer on creator (expected). No explicit self-exclusion message shown. |
| Second item B: private typed offer | **Fail** | `01a1b225-08bb-7f90-941a-cca9d2852d75` Review showed only verified/shared **Cove Manufacturer warranty, 2 years**, checked/Confirmed, source `https://haven.subzero.com/AssetLink/t7v1tx47i2bb7246u6p3d3263d0j7ex0.pdf`. **No** 12-month offer; **no** “typed in by hand” reason. Shot: `e3665e4fea647457c4d6b22ca767641ad6227a86d061baf3c3246b03e58fe210.png` |
| Add a purchase / New Items offer after 12- and 24-mo entries | **Fail** | Only verified/shared Cove 2-year with source link; no typed/private offer. Shot after deletion: `77f07105da560d21df1a72f52a70c3e300a9c95ce79a2940eb66b5faad661108.png` |
| Item C: retype 12 (no duplicate); edit 12→24 | **Pass** (item-level) | One coverage row; edited to 24 months ends `2028-11-06`. Private-policy/offer update **not proved** because 24 months **matches** the shared Cove 2-year term, so a later shared-only offer cannot establish a private update. |
| Waiting New Item re-check | **Not run** | New Items `/add` showed **0 waiting**. Shot: `0c6b7340bde5f356643ad932dac9fcc9d1bc64e114378cbc0d0fc9a3099b5ef2.png` |
| Delete coverage / retention | **Inconclusive** | Removed 24-mo coverage from C (item retained); after reload Needs info / no confirmed coverage. Fresh Add purchase still only shared Cove 2 years. Private offer was never visible before removal, and 24 mo equals shared term → retention of a **separate** maker policy could not be confirmed. **No item deleted.** A’s 12-mo evidence left intact. |
| Vehicle negative | **Pass** | Creator Honda Civic typed 12-mo Honda Manufacturer. Later Honda Accord Review: only unrelated shared **Honda Lawn and garden 2-year** placeholder (different category, unconfirmed). **No typed 12-month Honda vehicle policy offered.** Shot: `7fa5315e4cfc8e4af1995acb99a6c9b8c2ba7cca15bc534f571b7e007e6acba4.png` |
| Bob/Test2 not offered Alice’s entry | **Not run** | **Dependency gap:** Alice’s private typed offer was never exposed on second-item / Add-purchase paths, so a Bob privacy Pass cannot be claimed. Bob session was **not** executed. Do **not** treat as Pass by inference. |

**Conservative note on Fail:** Notes also say a term the shared list already holds is not copied (shared wins). The **12-month** Cove entry differs from the shared **2-year** term, so a private 12-mo offer was still expected on B / Add purchase. Graded **Fail** on `6503be1` for missing private offer — not excused by the commit mismatch.

---

## Coverage matrix vs Push 28 prep scope

| Prep scope item | Status this run |
|---|---|
| Auth logo eye-check | **Pass** |
| S62.23 | **Pass** (export flag Not run) |
| S62.17 | **Pass** |
| S62.14 core | **Pass** (optional already-covered link Not run) |
| S62.13 | **Pass** |
| S62.11 | **Pass** |
| P26-3B A/B/C | **Partial / Pass / Pass** |
| P26-1 revised (doc first) | Amber **Pass**; list note **Partial**; dismissal **Not run** |
| Offers by confidence | **Not testable** |
| S3.2.12 Alice typed policy / second offer / Add purchase | Creator coverage **Pass**; offers **Fail** |
| S3.2.12 12→24 / no duplicate | Item **Pass**; private update unproved |
| S3.2.12 waiting re-check | **Not run** |
| S3.2.12 retention | **Inconclusive** |
| S3.2.12 vehicle negative | **Pass** |
| S3.2.12 Bob privacy | **Not run** (dependency gap) |
| S62.12 Bob API | Out of scope / historically Blocked — **Not run** |
| Full S62 / S54 / S61 regression | **Out of scope** |
| Sweeps / clock / reset | **Not run** (forbidden this batch) |

---

## Open issues / outstanding (for next build)

1. **Fail — S3.2.12 private typed Cove 12-mo offer missing** on second same maker/category item and on Add a purchase / New Items (only verified shared 2-year shown). Observed on **`6503be1`**.  
2. **Partial — P26-1 My Items list note** “Your own entry may be out of date” still absent after document-first + typed (amber badge works). Dismissal untestable until note appears.  
3. **Partial — P26-3B item To do card path:** coverage/to-do card update, but header badge unread unchanged and Notifications still actionable.  
4. **Not run / dependency — Bob privacy** until Alice private offer is visible.  
5. **Not run — waiting New Item re-check** (needed a pre-existing waiting candidate).  
6. **Not testable — mixed-confidence offer sorting** without a typed offer alongside verified.  
7. **Inconclusive — maker-policy retention** after coverage remove (private offer never observed).  
8. **Not run — S62.23 export prorated flag; S62.14 already-covered link leave-alone.**  
9. **Operational:** Add-coverage dialog once dropped typed length (manual Starts/Ends needed).

## Clarifications (do not re-open as new fails)

- Prior **P26-1 typed-before-document Fail** → Push 28 **by design** (document replaces typed maker on ordinary item). Retest path is document-first (this report).  
- S62.16 Nov5/Nov6 end-date display, S62.15 never-linked mile field, S62.7/9/12 followers / vehicle-as-part / Bob API — Push 28 **by design / out of scope**; not re-failed here.

## State left

- Alice: new `P28 …` fixtures retained (truck/parts/appliances/vehicles as above). No scenario reset.  
- Bob / Carol / Ops: untouched. No Bob auth attempts.  
- Clock: **offset 0** (no advances). No sweeps.

## Evidence paths

- Report (box): `/workspace/uat/retest-6503be1/UAT-retest-2026-11-06-push28-typed-maker-and-p26p27-fixes.md`  
- Interims: `/workspace/uat/push28-prep/interim-*.md`  
- Prep brief: `/workspace/uat/push28-prep/prep-brief-2026-11-06.md`  
- Screenshots: `/cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/`  
- Final Results (UNC): `\\DESKTOP-TD3DQ64\Stuffit\Testing\Scenarios\Results\UAT-retest-2026-11-06-push28-typed-maker-and-p26p27-fixes.md`  
- Library: `uat-library/runs/UAT-retest-2026-11-06-push28-typed-maker-and-p26p27-fixes.md` + INDEX entry  

**Downloadable path (box):** `/workspace/uat/retest-6503be1/UAT-retest-2026-11-06-push28-typed-maker-and-p26p27-fixes.md`
