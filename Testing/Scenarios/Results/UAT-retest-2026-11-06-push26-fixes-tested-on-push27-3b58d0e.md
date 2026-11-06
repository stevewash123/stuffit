# UAT retest: Push 26 fixes — tested on Push 27 API `3b58d0e` (not a historical Push 26 run)

**Test date:** Friday **Nov 6, 2026** (~8:53–9:01 AM ET).  
**Live build under test:** API **`3b58d0e`** (Push **27**; `/api/version` match; started **7:48:11 AM ET** Nov 6, Staging). UI Last-Modified **7:46:54 AM ET**; bundle `main-Q465WJ7C.js`.  
**Original Push 26 notes (fixes being retested):** `CHANGES-push-26-typed-coverage-kept-and-superseded-note-2026-11-06.md` (notes claim API `28b0f24` / UI `8e9329b` — **those commits are not the live build**; this report records results on **current** Push 27 `3b58d0e`).  
**Important labeling:** There was **no** prior Push 26 Results filing under `\\DESKTOP-TD3DQ64\Stuffit\Testing\Scenarios\Results`. This is **not** a backdated Push 26 run. Grades are from evidence written **today** on `3b58d0e`.

**Mode:** Full browser, **targeted** (Push 26 Fixed + Retest rows only). Account: **Alice only** (vault-backed UI session). **No** clock advances. **No** sweeps. **No** orphan purge. **No** Bob/API mutations attempted this batch. Push 27 / Scenario 62 is a **separate** report.

**Evidence sources (box):**  
- `/workspace/uat/push26-evidence/p26-1.md`  
- `/workspace/uat/push26-evidence/p26-2.md`  
- `/workspace/uat/push26-evidence/p26-3.md`  
- Notes: `/workspace/uat/bot-rules/CHANGES-push-26-typed-coverage-kept-and-superseded-note-2026-11-06.md`

**Screenshots:** `/cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/` (hashes cited below).

## Headline

On live Push 27 `3b58d0e`, **vehicle typed-coverage keep (P26-2) Passes**, and **90-day end-date arithmetic (P26-3A) Passes** (Jan 18, 2027). The new ordinary-item **“Your own entry may be out of date”** note / amber **“Probably replaced…”** badge (**P26-1**) did **not** appear after a correct typed-then-document sequence — graded **Fail** for the note/badge (typed maker row was replaced by the document’s three policies, matching the appliance replace rule; simultaneous typed+document rows were never observed). Dismissal persistence was **Not run**. Bob dismiss-link isolation remains **Blocked** (no current Bob API auth / no documented dismiss-link contract exercised). Start-date notification finish (**P26-3B**) is **Partial**: notification becomes read / non-actionable and the to-do Done **persist after reload**, but the header badge recount and coverage dates stay **stale until a full page reload**.

## Totals (graded from evidence, not worker blanket Pass)

| Check | Result |
|---|---|
| P26-1 note + amber badge (ordinary appliance) | **Fail** |
| P26-1 dismissal persistence (X stays gone) | **Not run** (no note to dismiss) |
| P26-1 Bob isolation (dismiss link → Not found) | **Blocked** |
| P26-2 three typed maker + document = four kept | **Pass** |
| P26-2 no superseded note/badge on vehicle | **Pass** (absence expected) |
| P26-3A 90-day arithmetic → Jan 18, 2027 | **Pass** (editor still shows Length = 3 months) |
| P26-3B start-date notification finish + badge/coverage refresh | **Partial** |

**Summary counts (rows above):** **3 Pass**, **1 Partial**, **1 Fail**, **1 Blocked**, **1 Not run**.

---

## P26-1 — “Probably replaced” note + amber badge (ordinary appliance)

**Result: Fail** for expected note/X and amber badge. Dismissal **Not run**. Bob isolation **Blocked**.

### Setup (correct sequence)

- Item: **P26-1 Samsung Refrigerator Retest**; category **Refrigerators**; brand **Samsung**; model **RF28R7551SR**; purchase date **Nov 6, 2026**.  
- URL: https://stuffit-ui.onrender.com/items/01a1b11e-97a8-7021-a73f-694d4bd51ef4  
- Before document: **one** hand-typed Manufacturer warranty — provider Samsung; **2026-11-06 → 2027-11-06** (12 months); proof of purchase; original purchaser only / not transferable.  
- Exact typed Terms: `Entire refrigerator (parts and labor): 1 year. Repair or replace defective parts; labor included.`  
- Fixture: `/workspace/uat/sample/standard-appliance-limited-warranty.pdf` (md5 `2b955e94690a817336edbebf46d7d9a1`, 52 KB). Full reader used; proposed warranty accepted.

### After document apply

Reader UI: **“Applied to this item: 1 year from 2026-11-06, to 2027-11-06, and 2 parts with their own terms. It replaces the warranty we had suggested.”** Also: **“This differs from the warranty we have on file. Your item uses your document…”**

Item Policies after accept: **Covered — 3 policies** (all document-derived):  
1. Samsung Manufacturer warranty (1 year)  
2. Sealed refrigeration system (parts 5 years / labor 1 year)  
3. Digital inverter compressor (parts only 10 years)  

**Typed-row persistence:** the original typed Terms text was **no longer shown separately**; UI treated the document as replacing the suggested/typed maker warranty (matches Push 26 Fixed table: appliances unchanged — document maker warranty still replaces ordinary-item maker warranty). Simultaneous **typed + document maker** rows were **not** observed after accept.

### Expected Push 26 New UI — absent

- **Your items** after reload: exact note **“Your own entry may be out of date”** and its **X** — **absent**.  
- Item page typed/amber badge **“Probably replaced by the policy read from your document”** — **absent** (no typed row left to badge).  

**Grade rationale:** Retest goal was appearance of the list note + amber badge after typed-then-document on an ordinary item. Correct setup was used; after full reader accept those UI elements were missing. Graded **Fail** for note/badge (not Pass/Partial-as-pass). Because the appliance replace rule cleared the typed row, the New feature’s “typed AND document both exist” precondition never held after apply — called out transparently; still not a Pass.

### Sub-checks

| Sub-check | Result | Notes |
|---|---|---|
| List note + X after reload | **Fail** | Absent on Your items. Shot: `bf77eac7c6ded46ef3535aaf3df355b6ea500285d5b46598bd4f3026d474ef5b.png` |
| Amber badge on typed row | **Fail** | Absent; 3 document policies only. Shot: `4a5998647e6b7f88ea716829b2a53b7113c8ecec3a6db9baff04bba863f23dce.png` |
| Dismissal persistence | **Not run** | No note to dismiss; no sign-out/sign-in dismissal check |
| Bob opens dismiss link → Not found | **Blocked** | Undocumented dismiss-link HTTP contract; current Bob API password unavailable (`QA_PASSWORD_BOB` absent; `QA_NEW_PASSWORD_BOB` unconfirmed — **not tried**). Zero Bob login / probe attempts this batch. |

No vehicle created in this batch; no deletes/resets/clock/sweeps.

---

## P26-2 — S61 D29 / step 29: typed maker coverages kept on a vehicle

**Result: Pass** (3 typed + document = **4** preserved). **Pass** for expected absence of superseded note/badge on the vehicle.

### Setup

- Vehicle: **UAT P26 Typed Warranty Truck** (Truck, 2024 Ford F-150, bought new **Jan 1, 2025**, odometer at purchase **12** miles). First put in service **2025-01-01** (page: “in service Jan 1, 2025”; Needs info → Active).  
- URL: https://stuffit-ui.onrender.com/items/01a1b123-ff84-73ef-9d18-852058e93aa9  
- Alice session already signed in (browser only).

### Before document — 3 hand-typed Manufacturer warranty · Ford (all start Jan 1, 2025)

1. Powertrain: 60 months, Jan 1 2025–Jan 1 2030, 60,000 mi. Terms: `P26 typed Powertrain: 60 months / 60,000 miles`  
2. Bumper-to-bumper: 36 months, Jan 1 2025–Jan 1 2028, 36,000 mi. Terms: `P26 typed Bumper-to-bumper: 36 months / 36,000 miles`  
3. Roadside: 60 months, Jan 1 2025–Jan 1 2030, no mile limit. Terms: `P26 typed Roadside: 60 months, no mile limit`  

After reload: **Covered · 3 policies**.

### Document

Attached `/workspace/uat/sample/vehicle-five-year-60000.pdf` (md5 `f8e6c2c74f02f89e7e3904a3141b98a9`). Path: toast “Nothing to update…” then **Not now**; then file **Read it** → dialog “Add this warranty? … 5 years, maker’s warranty from Jan 1, 2025 to Jan 1, 2030.” Clicked **Add**. Ford stayed as provider. No separate full reader conflict “keep Ford” panel beyond that dialog.

### After — **4** Manufacturer warranty · Ford

All **3 typed terms preserved exactly**, plus document row: “From a warranty document you added. UAT Motors Limited New Vehicle Warranty. 5 years from purchase or 60,000 miles, whichever comes first…” Jan 1 2025–Jan 1 2030. Read-only: **Covered · 4 policies**.

### Absence checks (expected on vehicle)

- My Items: no **“Your own entry may be out of date”** on the vehicle.  
- Vehicle page: no amber **“Probably replaced by the policy read from your document”** on any typed row (edit + read-only).  

**Screenshots:** dialog `50134c89e1f7df9380311981023653baa9d92843e2d851d626835e5200b3db01.png`; 4 policies `7c351fe253d52d0186faa614c9e8103a72faf0b25092b4af747e7b7277a43b40.png`; My Items `7287fe6f98ed6a620418402664b6a29334c087583bcbc11bbdca97a44f367839.png`.

---

## P26-3A — S54 “90 days” arithmetic (bought Oct 20, 2026 → Jan 18, 2027)

**Result: Pass** (end date **Jan 18, 2027**, not Jan 20). Limitation: structured editor still stores/displays **Length (months) = 3**, not “90 days”.

### Setup / apply

- Item: **UAT P26 Trailblaze TB350** (regular; bought **Oct 20, 2026**). Brand Trailblaze added as new/Unverified; Category Major appliances; Model TB350.  
- URL: https://stuffit-ui.onrender.com/items/01a1b127-cf4a-79a8-94e2-5e51e289db68  
- Fixture: `/workspace/uat/sample/edge-registration-required.pdf` (md5 `4540ed9c0ed55d878cc439800a74d2c9`).  
- Model conflict TB350 vs doc TB-350 → **Keep yours**.  
- Add dialog: base **“3 months, maker’s warranty from Oct 20, 2026 to Jan 18, 2027. Counted from the purchase date.”** (ticked); optional **“3 years if you register by Nov 19, 2026”** **UNTICKED** / Not added. Add with base only.

### Result

- Coverage: Manufacturer warranty · Trailblaze, **Oct 20, 2026 to Jan 18, 2027 · Until Jan 18, 2027** (**not** Jan 20).  
- Terms text includes **“TRAILBLAZE Outdoor Gear. 90 days.”** Only 1 policy.  
- Application note: “Applied to this item: 3 months from 2026-10-20 to 2027-01-18.”  
- Editor: lifetime unchecked; Starts 10/20/2026; Ends **01/18/2027**; **Length (months) = 3** (stored as 3 months, not 90 days); transferable “document does not say”.  

**Screenshots:** coverage `b19ad6c0f4de6b10e3dd28721812c1552cf6b0b018589a6f33d6eac503789f00.png`; dialog `1894a21fdc2c168063b7c53ca341ca50a194ea9c03dd5d5f98aa629ea628d210.png`; editor `a90a203dcf447115a638d33751df439bf17c1f6d84dbc4616b5ba597ceef3822.png`.

---

## P26-3B — Entering warranty start date finishes notification; badge recount

**Result: Partial** — notification becomes read / non-actionable and to-do Done **persist**, but **immediate** header badge recount and coverage dates remain **stale until full page reload**. Do **not** treat as both Pass.

### Setup

- Item: **UAT P26 Start Notification** (Sub-Zero; bought **Nov 6, 2026**). Category Major appliances; brand Sub-Zero from shared list; shared suggestion “Sub-Zero warranty, Manufacturer, 2 years, Confirmed; Counted from today until you give the date” kept ticked.  
- URL: https://stuffit-ui.onrender.com/items/01a1b129-5186-7bd5-a785-9504099ebfa1  

### Before create

Badge: **“Notifications, 2 unread, 1 to do”**. List: credit-card to-do + 2× “Your data export is ready”.

### After create (before start date)

- Coverage Until **Nov 6, 2028**.  
- To-do: “Enter the start date of your Sub-Zero warranty on UAT P26 Start Notification” (Due in 14 days; installation-not-purchase copy; field “The day it started”).  
- Badge in SPA stayed **“2 unread, 1 to do”** (stale) until reload → **“3 unread, 1 to do”**.  
- Notifications: new “Enter the start date…” — **Needs action**, Unread, Enter the date / Save / Remind me later / Dismiss; **Nov 6, 2026 9:00 AM**.

### After saving start date **2026-10-15** from item-page to-do

**Immediate (SPA, no full reload):**  
- Page still showed Until **Nov 6, 2028**; to-do collapsed under “Show done and dismissed (1)”.  
- Badge still **“3 unread, 1 to do”** even after SPA nav to Notifications.  
- Notification: **no** “Needs action”, no date field/buttons, shows **“Mark unread”** (treated as read); title/text unchanged.

**After full page reload:**  
- Badge **“2 unread, 1 to do”** (recount correct; refresh required). To-do count 1 = credit-card only.  
- Item coverage updated: Manufacturer **Oct 15, 2026 → Oct 15, 2028**; Sealed system **Oct 15, 2026 → Oct 15, 2038** (labor to **Oct 15, 2031**). To-do **Done** with Reopen.

### Grade split

| Aspect | Result |
|---|---|
| Notification finished (read / non-actionable) after save | **Pass** (visible immediately in Notifications SPA) |
| To-do Done persists after reload | **Pass** |
| Header badge recount updates immediately | **Fail** (stale until reload) |
| Coverage dates update immediately | **Fail** (stale until reload) |
| **Overall P26-3B** | **Partial** |

**Screenshots:** before notifs `33a4173e1481ffdec88302949e84d3734ae33b15affa8392bd4d555c18028d2c.png`; item w/ to-do `cacfd3dd8939bd38453efe78d33b4c0bded78bb5614f5187cbc0e53f9e963401.png`; notif needs action `ac4386adfec7b806abf8707f6509c7d7aba9dce453f77f6e5ba8b912f7b150f6.png`; notif finished SPA badge-3 `fcc610fb192c624c7fccee27f51b665e8882eb45a4f944312b0c85b454e2e51c.png`; after reload badge-2 `9751832c61e298d2345804feedd4626db038a1ab0a93492e1b21bd269f67dc32.png`; item after reload `636e2bb2c2c4d96177e8080d5c1f4f67033f16864aafafbc1ce8a7881ca8c64a.png`.

---

## Open issues / notes for dev

1. **P26-1 Fail** — After typed maker coverage + full reader accept on an ordinary appliance, list note **“Your own entry may be out of date”** and amber **“Probably replaced…”** badge never appeared; typed row was replaced by three document policies (appliance replace rule), so the New feature’s simultaneous typed+document state was never visible.  
2. **P26-1 Bob isolation Blocked** — Needs confirmed current Bob credentials (secure) and/or documented dismiss-link contract; not probed.  
3. **P26-3A limitation** — End date Jan 18 is correct, but editor Length remains **3 months** rather than a days representation.  
4. **P26-3B Partial** — Notification/to-do finish works; header badge recount + coverage dates require **full reload** (same class of stale SPA issue seen on Push 25 step 7).  
5. Push 26 notes “Not changed” items (application receipt text, 15 vs 14 day due, etc.) — **not re-graded** as new.

## Not in this report

- Push 27 / Scenario 62 parts — separate file `UAT-retest-2026-11-06-push27-s62-parts.md`.  
- Sweeps (`export-expiry`, `reminder-send`).  
- Clock advances / orphan purge / full regression.  
- Any claim of a historical Push 26 Results run on API `28b0f24`.

## State left

- Alice browser items created for this retest (not scenario-reset after): P26-1 Samsung Refrigerator Retest; UAT P26 Typed Warranty Truck; UAT P26 Trailblaze TB350; UAT P26 Start Notification (plus any prior Push 27 S62 leftovers from the parallel report).  
- Bob / Carol / Ops: **untouched** this batch (no Bob auth attempts).  
- Global clock: **offset 0**. No sweeps.

## Evidence paths

- Report (box): `/workspace/uat/retest-3b58d0e/UAT-retest-2026-11-06-push26-fixes-tested-on-push27-3b58d0e.md`  
- Batch writeups: `/workspace/uat/push26-evidence/p26-1.md`, `p26-2.md`, `p26-3.md`  
- Screenshots: `/cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/`  
- Final Results (UNC): `\\DESKTOP-TD3DQ64\Stuffit\Testing\Scenarios\Results\UAT-retest-2026-11-06-push26-fixes-tested-on-push27-3b58d0e.md`  
- Library: `uat-library/runs/UAT-retest-2026-11-06-push26-fixes-tested-on-push27-3b58d0e.md` + INDEX entry  
