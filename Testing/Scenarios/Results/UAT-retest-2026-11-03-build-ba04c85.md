# StuffIt retest - build ba04c85 (push 6: receipt plans and polish)
Date: Tue Nov 3 2026, 6:24-6:46 PM ET. API commit ba04c85 (Staging, started 6:10 PM ET), UI 9f2c261, no migration. Alice and Bob reset by DB Stager first (scenario reset, Ops untouched). Clock offset 0. Fixes and new code only, no regression.

**Totals: 44 rows. 38 Pass, 3 Partial, 1 Fail, 2 Not run.**

| Chunk | Pass | Partial | Fail | Not run |
|---|---|---|---|---|
| A receipt plans | 12 | 1 | 0 | 0 |
| B no-company, edit recheck, question | 8 | 0 | 0 | 1 |
| C plan form and card | 8 | 2 | 1 | 0 |
| D update-from-document, guards, hint, isolation | 10 | 0 | 0 | 1 |

## Fail
- **C-3 (C43-8/C43-9 still open):** "I have the paperwork or a photo" opens the file chooser straight away; there's no "Start a plan from it". The file is read and offers "Add this warranty? ... protection plan from Oct 10, 2026 to Oct 10, 2030", and Add makes only a bare "Protection plan" coverage. No plan record is made, there's no company box, and it shows "Paid 299.99" instead of "$299.99 one payment".

## Partial / not run
- **A-5:** after unticking, reloading and ticking again, the Add Details price field showed the old 49.99. The saved plan did keep $54.99, so it's a display issue only.
- **C-8:** a plan ending in 42 days shows "Active" on the item card, not "Ending soon". The Home tile and filter both count it.
- **C-0:** there's no Tablet category, so the tablet half of the device default wasn't tested.
- **B-8:** the subscription/service hide case for the plan question can't be tested, because no subscription or service category or store exists.
- **D-11:** `clock/status` returned HTTP 401 Unauthorized from my computer on this build. No clock steps were needed this run.

## Other findings
1. A renewal to-do was made for a plan that had already ended: "UAT Old Ended Plan ends on Jan 1, 2025. Renew or replace it." It shows "Overdue since Jan 1, 2025".
2. The fee-only update shows the new value as "95", not "$95.00".
3. The Lowe's row still says "Pick the company on the item page after you add it", but the item page has no picker. This is wording only; the decided list says the to-do carries it.
4. The Allstate plan page has no "not verified" marker, though the receipt row had one.
5. The headphones still say "2 suggested policies to review" after the plan was added.
6. Alice's session dropped once without warning.

## Confirmed fixed
C44-1 (Covers text), C44-4 and C44-6 (receipt plans become plan records with the receipt as proof), 44-5 (no second plan), C44-8b (Lowe's to-do, no bare coverage), C44-15 (edit kept, plan unticked "Check this is for the item above"), push 5 `?addPlan=1`, push 5 "receipt shows a plan" hide case, C43-7 (laptop defaults), C43-3/C43-10/C48-0 (required marks, More details, ticked covers row), C48-1 (status word, Backup badge, Copied), C43-6 (Home tile), C31-9/C48-5 (Ended, no Cancelled, Delete only), C31-4 (leave guard), C31-5 (https), C31-6/C31-7 (only real differences), P3-6 (amount messages), C43-15 (to-do wording), Account hint on the Account page.

---
# Chunk detail
# Chunk A results (ba04c85) - 12 Pass, 1 Partial (A-0 setup counted)
A-0 Pass clean baseline. A-1 Pass (headphones plan read, no Covers line/claim). A-2 Pass ("Covers QN65Q80: matches this item." on made-up 99 receipt).
A-3 Pass Add Details plan fields editable (Company, Plan name, Length, Price, Plan or contract number, Starts). A-4 Pass price 49.99->54.99.
A-5 Partial: untick + reload stays unticked, but re-ticking showed price 49.99 (edit not shown after reload). Yet A-7 saved plan at $54.99, so the edit was kept server-side; the field displays the old value after untick/reload/tick.
A-6 Pass second tab shows plan ticked. A-7 Pass: real plan record "Geek Squad Protection - 2-Year Plan / Until Oct 6, 2028 / Warranty extension ... $54.99 one payment", receipt attached as proof, item plan card, no SKU in terms (C44-4 fixed). Toast doesn't name plan (decided).
A-8 Pass stale tab: "This item has already been added to My Items." still 1 plan.
A-9 Pass: Geek Squad TV receipt with plan -> plan question NOT shown on Add Details (push 5 hide case). Quick add made plan "Geek Squad Protection 4YR ... $299.99 one payment", contract GS-88104471, receipt as proof (C44-6 fixed).
A-10 Pass Target kettle shows question (control). A-11 Pass dishwasher plan unticked -> no plan, no bare coverage; install line neither item nor plan.
A-12 Pass 3 items, 2 plans, nothing dropped.
Odd: session dropped once mid A-9; Add Details Category empty (saved "Not sure"); Store/Brand boxes look empty in accessibility snapshot; headphones still says "2 suggested policies to review" after plan added.
# Chunk B results (ba04c85) - 8 Pass, 1 Not run
B-1 Pass Lowe's no-company: no bare coverage, to-do "Add your Lowe's Protection Plan 3-Year plan: check its term" (once, dismissible, opens item) - C44-8b fixed. Note: row text still says "Pick the company on the item page after you add it" while the item page has no picker (decided: to-do/Add Details carry it) - wording mismatch only.
B-2 Pass Add Details: typed company "Lowe's" -> real plan "Lowe's Protection Plan 3-Year ... $99.00 one payment". Company box is plain text (no list).
B-3 Pass Allstate "not in our list yet: not verified". B-4 Pass name/model edit kept after reload; plan unticked "does not match ... Check this is for the item above" - C44-15 fixed.
B-5 Pass held back from quick add. B-6 Pass named back -> matches, stays unticked until ticked.
B-7 Pass untick-all message; Allstate plan created with contract AS-66120934 and receipt. Note: plan page has no "not verified" marker for Allstate.
B-8 Not run: no subscription/service category or store exists (category list has none) - cannot test the hide case.
B-9 Pass ?addPlan=1 gone from the address, reload doesn't reopen the sheet; no plan/to-do left - push 5 finding fixed.
# Chunk C results (ba04c85) - 8 Pass, 2 Partial, 1 Fail (C-0 setup counted)
C-0 Partial setup: no Tablet category, so UAT Tablet skipped (fridge, laptop, phone, washer made).
C-1 Pass type-it-in defaults Insurance, a month for Laptop (Computers) and Phone - C43-7 fixed.
C-2 Pass "Company (required)", "What it is (required)", "Starts (required)", "Only company, what it is and start are needed.", "More details (optional)" with fee/phone/website; ticked "Covers UAT Laptop" - C43-3/C43-10/C48-0 fixed.
C-3 FAIL paperwork route: "I have the paperwork or a photo" opens the file chooser straight away; no "Start a plan from it". The file read, offered Brand/Model, then "Add this warranty? ... 4 years, protection plan from Oct 10, 2026 to Oct 10, 2030." Add made only a bare "Protection plan" coverage (no plan record; plans stayed 4), no company box, "Paid 299.99" not "$299.99 one payment". Same as C43-8/C43-9.
C-4 Pass card "Active" status word with separate "Backup" badge - C48-1 fixed. C-5 Pass "Copied" ~2 s plus toast "Contract number copied".
C-6 Pass "Waiting: starts Dec 1, 2026". C-7 Pass Home tile "6 running." with no 0-count clause - C43-6 fixed.
C-8 Partial: plan ending Dec 15 2026 - Home tile and filter agree (UAT Phone, 42 days) but the item card status says "Active", not "Ending soon".
C-9 Pass Jan 3 2027 edge plan (61 days) counted by neither tile nor filter - they agree.
C-10 Pass past-dated plan reads "Ended Jan 1, 2025" on list, plan page and card; no "Cancelled"; no "Stop covering", Delete offered - C31-9/C48-5 fixed.
# Chunk D results (ba04c85) - 10 Pass, 1 Not run
D-1 Pass https:// claim website not flagged, kept - C31-5 fixed. D-2 Pass same document: "Nothing in that document differs from what you have saved." - C31-6 fixed.
D-3 Pass fee-only update lists only "Service call fee ... Saved now: $75.00 · New: 95"; applied only that - C31-7 fixed (minor: new value shows "95" not "$95.00").
D-4 Pass bare www.example.com/shield offered as https://www.example.com/shield, ticked (company not read; typed new company).
D-5 Pass Add purchase cancel guard "Leave without saving? ..." Keep editing / Leave without saving - C31-4 fixed.
D-6 Pass empty/0/-5 -> "Enter an amount greater than zero.", Save enabled - P3-6/D-9 fixed. D-7 Pass "Enter the date you received it."
D-8 Pass renewal to-do "UAT Soon Plan ends on Dec 15, 2026. Renew or replace it. ... From your protection plan." (run-reminders not needed).
D-9 Pass Account page: "Protection plans — Warranty extensions, accident cover and other plans you bought on top of what an item already has."
D-10 Pass Bob sees no plans/to-dos/items; Alice's plan and item paths "Not found."
D-11 Not run: clock/status returned HTTP 401 from the box (maintenance key no longer accepted on ba04c85?). No clock changes made all run; DB Stager reported offset 0 at reset.
Odd: renewal to-do created for an already-ended plan: "UAT Old Ended Plan ends on Jan 1, 2025. Renew or replace it." Overdue since Jan 1, 2025.
