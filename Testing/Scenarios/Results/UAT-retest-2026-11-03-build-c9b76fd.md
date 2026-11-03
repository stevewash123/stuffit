# StuffIt retest report: build c9b76fd (Staging)
- **Date:** Tue Nov 3, 2026, about 3:05 to 4:05 PM ET
- **API:** /api/version commit `c9b76fd`, Staging, started 2026-11-03 19:18:48 UTC (2:18 PM ET). **UI:** `76a7bbf` expected. The first Protection plans view came from a cached old UI, and a hard reload showed "Protection plans".
- **Scope:** push 3 fixes (A-20, A-17, D-9, D-4, B-13) and push 4 add-on protection: Scenarios 43 and 48 in full, Scenario 44 steps 1-10 and 15, the listed FS-31/40/41 steps and the 49-1 default. **No regression.** Deferred, not run: Scenarios 45-47, 49 (except 49-1) and 50. 44-11 to 44-14 are not built.
- **Accounts:** Alice and Bob. DB Stager ran a scenario reset of Alice and Bob after the PlanKind migration. Ops two-step is intact, and the clock was reset to 0 at the end.
- All steps are Full-only (browser UI).

## 2. Totals
| Chunk | Pass | Partial | Fail | Not run | Setup/housekeeping (not counted) |
|---|---|---|---|---|---|
| P3 (push 3 fixes) | 7 | 1 | 0 | 0 | PF-1, PF-3 pass; P3-9 done |
| C43 | 8 | 7 | 0 | 0 | 2 |
| C44 | 6 | 3 | 3 | 0 | 0 |
| C31 (plan form) | 5 | 5 | 0 | 0 | 1 |
| C48 | 4 | 5 | 0 | 0 | 2 |
| CBOB (Bob) | 3 | 0 | 0 | 0 | 0 |
| **Overall** | **33** | **21** | **3** | **0** | |
The keyboard part of C48-7 wasn't run, and the row is graded Partial.

## 3. Fails and main issues to fix
**Fails**
- **C44-1:** a plan matched by SKU only still says "matches this item", and the row shows "Covers Covers".
- **C44-4:** a plan read from a receipt becomes a bare coverage on the item, not a plan in Protection plans. *The push 4 notes don't clearly list receipt-to-plan records, so this may be out of scope. Steve to confirm.*
- **C44-15:** after the pending item is edited, the plan stays ticked and there's no "check this is for the item above" note. A reload also reverted the name.

**Key partials**
- **P3-6 (D-9):** a negative or empty amount only disables Save and shows no message. The future-date message is fixed.
- **C31-4:** Add purchase has no unsaved-changes guard. The plan form has one.
- **C31-5:** an `https://` website is flagged "not a web address starting with http or https".
- **C31-6/7:** "Update from a newer document" lists fields that haven't changed and doesn't show old against new.
- **C31-9 / C48-5:** an ended plan reads "Cancelled" on the item instead of "Ended". The plan page still offers "Stop covering".
- **C43-3:** required fields aren't marked, and the "only company, what it is and start are needed" line is missing.
- **C43-7:** the laptop (Computers) defaults to Warranty extension with one payment, not Insurance with monthly payments. Only the phone gets the 49-1 default.
- **C43-8/9:** on the item-page paperwork route, "Start a plan from it" doesn't carry the file over. After the reader runs, Company stays blank, and a one-payment price shows as "$299.99 a year".
- **C43-10:** the item to be covered shows as a sentence, not a ticked item control.
- **C48-0:** the type-it-in dialog has no service fee, claim phone or website fields.
- **C48-1:** Copy contract gives no feedback, and the status word is "Backup" (no waiting, active or ending soon).
- **C44-6:** the TV plan from quick add is a bare coverage only, with no plan record and no "Add your Geek Squad plan" to-do.
- **C44-8b:** the Lowe's plan has no company note on the item page.
- Smaller items: C43-6 has no "N end within 60 days" line (the count may be 0), C43-15's to-do still says "extended warranty plan", and C44-2 Add Details shows one line with no plan fields.

## 4. Fixed in this build
- A-20: delete and re-upload works, the export drops deleted files, and stated warranties show "Stated on receipt".
- A-17: the stove shows its stated 10-year warranty, and the pipe kit shows "No warranty found yet."
- D-9: a future date gives "That date is in the future."
- D-4: the Recovered card shows $50.00 on first load.
- B-13: a soft-closed return window has a working courtesy override.
- C44-8: the Lowe's "not verified" note now shows (previously open).
- C44-9: the Allstate "not in our list yet" note works.
- New in push 4 and working: the Add-on protection section, the four-way "How did you get the plan?", plan creation with a to-do, upgrading a bare coverage (C43-13), the card-benefit redirect, field errors, the end-before-start "Did you mean", End this plan, the stack line and the order after the clock jump, no reminders for an ended plan, and Bob's isolation.

## 5. Row tables

### P3
| Row | Result | Evidence |
|---|---|---|
| P3-1 A-20a | Pass | Quick add "Inverter Generator added to My Items."; stated warranty held back with quick-add note; export lists files/..._17-thermal-unknown-store-generator-single.pdf (15 entries) |
| P3-2 A-20b | Pass | "Delete this item? Inverter Generator and its coverage and files are removed. This cannot be undone."; newest export 14 entries, no files/ |
| P3-3 A-20c | Pass | Re-upload: "Added 1 receipt. Open it to add what is on it." No "already added" |
| P3-4 A-20d | Pass | Coverage "Stated on receipt", Jul 19 2026 to Jul 19 2028, "Receipt says: 2 YR MFR WARRANTY." (store typed by hand) |
| P3-5 A-17 | Pass | Stove: "Try first: Stated on receipt … Oct 9, 2026 to Oct 9, 2036 … Receipt says: 10 YR LIMITED WARRANTY"; pipe kit "No warranty found yet." Minor: My Items row still says "Manufacturer warranty until Oct 9, 2036" |
| P3-6 D-9 | Partial | Future date: "That date is in the future." (fixed). Negative/empty amount: Save disabled, no message |
| P3-7 D-4 | Pass | Home Recovered card "$50.00 on 1 item / $50.00 in cash" on first load |
| P3-8 B-13 | Pass | After +31 days: Expired, "Return window closed" notice; Refund/Mark returned/Start a return hidden. Confirm "Show the return actions" -> Start a return, Refund, Mark returned back with "Courtesy return" note. |
| P3-9 | done | New Items empty; clock reset to 0 |
| (setup note) | Best Buy has no 30-day policy; ticked Best Buy 15-day window (to Nov 18). Before: Expiring soon, 15 days left, Start a return etc. visible |
Notes: Odd: export list newest-first, first Download can be older file; store field blank on Add Details for generator and stove; reader read store in capitals.

### C43
| Row | Result | Evidence |
|---|---|---|
| C43-0a | Pass (setup) | UAT TV, Best Buy, Cuisinart, TVs, $800, Oct 14 2026 |
| C43-0b | Pass (setup) | UAT Laptop, Computers, $1,200, Oct 29 2026, receipt small-receipt.pdf |
| C43-1 | Pass | "Add-on protection" + Add, "A plan you bought on top of what the item already has: an extended warranty, accident cover or insurance." |
| C43-2 | Pass | "How did you get the plan?" four choices as specified |
| C43-3 | Partial | Fields present; optional ones marked "(optional)", but no "Only company, what it is and start are needed" and required not marked |
| C43-4 | Pass | Toast "Geek Squad plan added to your UAT TV"; listed under Protection plans "UAT TV 2-Year / Until Nov 2, 2028 / Warranty extension · Geek Squad · 1 item" |
| C43-5 | Pass | "Add the rest: price, contract number, claim contact" opens edit; one to-do "Add the rest of your Geek Squad plan"; dismissed stays gone |
| C43-6 | Partial | Home tile "Protection plans / 1 running." links /plans; no "N end within 60 days" (count 0, may be hidden at 0) |
| C43-7 | Partial | Add coverage kind "Protection plan (extended warranty, accident cover, insurance)" opens plan form; other kinds unchanged. Laptop (Computers) defaults Warranty extension / one payment, not Insurance / monthly (49-1 default only works on phone) |
| C43-8 | Partial | Item-page paperwork route reads into generic panel; "Start a plan from it" opens empty /plans/new, file not carried. On /plans/new reader read Geek Squad plan (contract, dates, price, phone) in 9.3 s; Company left blank |
| C43-9 | Partial | Plan via /plans route covers UAT Laptop with contract and "Call (555) 555-0140"; plan file under Terms; one-payment price shown "$299.99 a year" |
| C43-10 | Partial | "This plan will cover UAT TV once you save it." sentence, not a ticked item control |
| C43-11 | Pass | "A benefit, not a plan / Nothing is added as a plan..." with Credit cards link; plan count unchanged |
| C43-13 | Pass | Bare Geek Squad coverage upgraded: toast "Geek Squad plan added to your UAT Old Plan Item"; 1 policy, no bare line, one plan listed (company box opened empty) |
| C43-15 | Partial | Names updated on item/plans/menu/Home tile/wizard; to-do still "From your extended warranty plan."; Home "Ending in 30 days / Warranties and plans" (known); email Not run |
| C43-16 | Pass | Phone defaults Insurance / a month (49-1); new company "UAT Phone Cover Co UNVERIFIED", no set-up screen; "$168.00 a year" |
| C43-17 | Pass | No duplicate company; Add the rest + one to-do; filling details marks to-do done ("Plan saved. Every item it covers is updated.") |
Notes: Odd: Company blank after reader fill and on upgrade form; one-payment price labelled "a year"; "Nov 3, 2026 , no fixed end" stray space; maker warranty on TV shows category "SMALL APPLIANCES".

### C44
| Row | Result | Evidence |
|---|---|---|
| C44-1 | Fail | Headphones row "Includes: Geek Squad Protection - 2-Year Plan, $49.99 · Geek Squad · 24 months . Covers Covers: matches this item." SKU not on row but a match claim is made for a SKU-only plan; item page later shows "Covers: Covers SKU 6505727". Also doubled "Covers Covers". 20.8 s |
| C44-2 | Partial | Add Details lists plan ticked "… · Plan · 2 years · Highly Likely · Covers Covers: matches this item."; single line, no company/name/contract/start fields |
| C44-3 | Pass | Untick persists across reload (same browser) |
| C44-4 | Fail | Toast "All required fields are filled in. Wireless Noise Cancelling Headphones was added to your items list." (item only). No plan record in Protection plans; item has bare "Protection plan · Geek Squad" coverage + "Add the plan's details"; receipt on item only. (Scenario 44-4 expects a plan record; CHANGES-push-4 doesn't list receipt->plan record explicitly - confirm if built) |
| C44-5 | Pass | Re-upload "…: already added to My Items." no duplicate |
| C44-6 | Partial | TV quick add "OLED TV added to My Items."; plan only as bare coverage (GS-88104471), not a plan record; no "Add your Geek Squad plan" to-do. 26.6 s |
| C44-7 | Pass | Dishwasher row with Geek Squad 3-Year $229.99, "Covers dishwasher: matches this item."; install line not item/plan. 18.2 s |
| C44-8 | Pass | Lowe's: "No company on the receipt, so this plan is not verified. Pick the company on the item page after you add it." (previous open item fixed). 17.8 s |
| C44-8b | Partial | Lowe's plan kept on item as bare coverage; no company note on the item page, only "Add the plan's details" |
| C44-9 | Pass | "Allstate is not in our list yet: not verified. It stays on your account until we check it." 20.7 s |
| C44-10 | Pass | "…Tick at least one policy to add it." |
| C44-15 | Fail | After editing pending item to "UAT Edited Mixer"/"ZZ-100", plan still ticked, "Covers TV: matches this item", no "check this is for the item above"; reload reverted the name to "4K TV" |
Notes: Odd: plans from a receipt never become plan records (only the Protection plans page / Add-on form create them); HDMI Cable left in Smaller things.

### C31
| Row | Result | Evidence |
|---|---|---|
| C31-0 | Pass (setup) | UAT Washer $600, UAT Dryer $300 |
| C31-1 | Pass | Field messages: "Choose the company that sold the plan, or type its name and add it." / "Give the plan a name." / "Enter the date the plan starts."; no generic banner; focus Company |
| C31-2 | Pass | Form takes all values; items covered afterwards via Cover items (no item picker on new-plan form) |
| C31-3 | Pass | "The end date is before the start date. Did you mean Aug 1, 2027?" on End; focus End |
| C31-4 | Partial | Plan form guard "Leave without saving? You have changes that have not been saved..." Keep editing / Leave without saving works (Cancel, account menu, unaccepted read). Add purchase (/add/new) with typed text leaves on Cancel with NO dialog (twice) |
| C31-5 | Partial | Website offered and saved as https://www.example.com/shield ("Make a claim online"), but suggestion unticked with "That is not a web address starting with http or https." although it starts with https; had to tick it; company picked by hand |
| C31-6 | Partial | Same document: no "nothing differs"; listed covers (commas->semicolons) and exclusions as different |
| C31-7 | Partial | Fee-only document: listed fee 95 plus covers and exclusions; no old vs new shown; applying rewrote covers/exclusions text |
| C31-8 | Pass | "End this plan? UAT Home protection ends on Nov 3, 2026 and stops covering 2 items from that day. It will show as ended." Plan "Ended Nov 3, 2026"; totals updated |
| C31-9 | Partial (rule to confirm) | Items show plan "Cancelled Sep 3, 2026 to Nov 2, 2026" (last day Nov 2 intended), but says "Cancelled" not "Ended"; badge/Next to end follow the return window |
| C31-10 | Pass | Home "6 Protection plans, 6 running", ended plan excluded; "0 Ending in 60 days" |
Notes: Odd: ended plan row still shows "2 items · $360.00 a year" and sorts first.

### C48
| Row | Result | Evidence |
|---|---|---|
| C48-00 | Pass (setup) | Fridge added in UI with return window, Cuisinart maker (offered "1 year · Unconfirmed"), card extended warranty; Purchase protection (120 days) was pre-ticked and unticked by tester |
| C48-0 | Partial | Type-it-in dialog has no service fee / claim phone / website fields; saved, then "Add the rest: claim contact"; filled on plan edit page. Term Nov 3 2026 to Nov 2 2028; "$99.00 one payment ($49.53 a year)" |
| C48-1 | Partial | Card: "Geek Squad / Geek Squad 2-Year / Warranty extension / Backup / Until Nov 2, 2028 / ... / Service fee $49.00 per call / Contract UAT-GS-0001 [Copy] / Call 800-555-0150 / Make a claim online / Open the plan"; tel and https links work. Copy gives no visible feedback; status word is "Backup", no Waiting/active/ending soon |
| C48-2 | Partial | "The maker's warranty runs to Nov 3, 2027. Your card extended warranty (Chase) runs to Nov 3, 2028. The Geek Squad plan runs from Nov 3, 2026 to Nov 2, 2028." Real dates, "card extended warranty", no advice. The "plan starts the day after the maker's warranty ends" clause wasn't exercised because the plan start was typed as today (test setup), so it's not graded as a Fail |
| C48-3 | Pass | Return window "Try this first"; Geek Squad plan "Backup" |
| C48-4a | Pass | Home tile "7 Protection plans / 7 running", "0 Ending in 60 days"; matches plans page |
| C48-4 | Pass | After +366 days (Nov 4 2027): "Try first: Protection plan · Geek Squad"; plan "Try this first", no Backup; maker "Ended Nov 3, 2027"; card extension still counted to Nov 3 2028; stack line "The maker's warranty ran to Nov 3, 2027. Your card extended warranty (Chase) runs to Nov 3, 2028. The Geek Squad plan runs from Nov 3, 2026 to Nov 2, 2028." |
| C48-5 | Partial | End saved (ended on Nov 4 2027); plan page "Ended Nov 4, 2027", term to Nov 4 2027; item: plan row "Ended Nov 3, 2027" (day before, intended) but plan card says "Cancelled"; Try first and Next to end move to Card extended warranty, badge/Next to end agree. Confirmation text not captured (session drop). Plan page still offers "Stop covering" after end |
| C48-6 | Pass | After +1 day and run-reminders (Sent=0, Cancelled=33, Todos=0): no reminder about the ended plan; plan stays "Ended Nov 4, 2027" |
| C48-7 | Partial | ~390 px: Company error beside field in red, no horizontal scroll/overlap, full-width buttons; fridge plan card fits. Only Company error (Starts pre-filled). Keyboard part Not run |
| C48-8 | done | clock reset to 0, window restored, signed out |
Notes: Odd: Alice's session dropped after the 366-day clock jump (likely token expiry at the simulated time; not graded).

### CBOB
| Row | Result | Evidence |
|---|---|---|
| CBOB-1 (43-12) | Pass | Empty state: "No plans yet. One item: a plan bought for a single thing (a TV, a phone) is added from that item, under Add-on protection. [Open My Items] Many items: a home warranty or any plan that covers several things is added here once... [Add a plan that covers many items] [I have paperwork or a photo]. Came free with a credit card? That is a card benefit, not a plan. [Credit cards]"; no Home tile |
| CBOB-2 (43-14) | Pass | Alice's TV plan and item URLs show "Not found." for Bob |
| CBOB-3 (48-14) | Pass | Alice's fridge plan and item show "Not found." for Bob |
Notes: Odd: Bob's first sign-in bounced back to /login with no error (second worked); Notifications timestamps follow real time, not the test clock.

## 6. Odd items not asked about
- Export list is newest-first, but the first Download can be an older file. The store field is blank on Add Details for the generator and stove. The reader reads the store name in capitals.
- The My Items row for the stove still says "Manufacturer warranty until Oct 9, 2036".
- Company is blank after a reader fill and on the upgrade form. There's a stray space in "Nov 3, 2026 , no fixed end". The TV maker warranty shows the category "SMALL APPLIANCES".
- HDMI Cable is left in Smaller things.
- An ended plan row still shows "2 items · $360.00 a year" and sorts first.
- Alice's session dropped after the 366-day clock jump, likely token expiry at the simulated time.
- Bob's first sign-in bounced back to /login with no error. Notifications timestamps follow real time, not the test clock.

## 7. Seed data (for CC)
- **DB Stager couldn't seed UAT Fridge.** There was no app-written example of the card extended warranty coverage shape, and it wasn't clear whether the Cuisinart maker coverage should link to a policy. **Alice added it through the UI instead (C48-00).**
- DB Stager took a read-only snapshot of the app-written rows to use as the pattern for future seeds. The files are in the bot store: `staging/patterns/uat-fridge-c9b76fd-20261103.json` (full rows) and `staging/patterns/uat-fridge-c9b76fd-20261103.md` (seed pattern).
- **Caveat:** the snapshot was read at clock +366 days, after End this plan. The plan and plan-coverage rows are therefore in their post-end state: end_date and ended_on are 2027-11-04, the coverage source is User, and the reminders are Cancelled. The plan's original end date and the coverage's original source can't be recovered from these rows.
- How the app wrote the coverages, as created:
  - **Return:** source Default, Nov 3 to Nov 18 2026, linked to the Best Buy 15-day policy, with no holiday extension. Reminders 7/3/1.
  - **Manufacturer:** source Default, 12 months from Nov 3 2026 to Nov 3 2027, linked to the Cuisinart policy. Reminders 60/30/7.
  - **Card extended warranty:** source Default, benefit_kind ExtendedWarranty, provider Chase, Nov 3 2027 to Nov 3 2028. It starts when the maker warranty ends, has no benefit-row id or policy link, and the 48-month cap isn't applied.
  - On all four coverages, end_date_latest and pending_start are null and user_edited is false.
  - **Purchase and plan:** the purchase is Manual/Exact, linked to the card through purchases.payment_method_id, and the item price is 900.00. The plan is "Geek Squad 2-Year", kind WarrantyExtension, contract UAT-GS-0001, 99.00 OneTime with a 49.00 service fee, and it has 1 plan_items row. The app also wrote a System to-do, "Add the rest of your Geek Squad plan", status Done.
- **What Alice saw:**
  - The Return window is "Try this first".
  - The stack line read: "The maker's warranty runs to Nov 3, 2027. Your card extended warranty (Chase) runs to Nov 3, 2028. The Geek Squad plan runs from Nov 3, 2026 to Nov 2, 2028."
  - The plan "Geek Squad 2-Year", Warranty extension, read "Until Nov 2, 2028". After End this plan, it read "Ended Nov 3, 2027" on the item and "Ended Nov 4, 2027" on the plan page.
  - After the clock jump, the maker warranty read "Ended Nov 3, 2027".
  - Purchase protection (120 days) was pre-ticked, and the tester unticked it.
- DB Stager flagged that the plan coverage ends Nov 3, 2027 while the plan ends Nov 4. That's the intended day-before rule, not a bug.

## 8. Rules to confirm (Steve)
1. 44-4 and C44-6: should a plan read from a receipt or quick add create a plan record in Protection plans? Is that in push 4?
2. C31-9 and C48-5: should an ended plan read "Ended" rather than "Cancelled" on the item? Should "Stop covering" still show after a plan has ended?
3. C43-7 / 49-1: should the Insurance with monthly default apply to laptops (Computers) as well as phones?
4. C48-2: the "plan starts the day after the maker's warranty ends" clause wasn't exercised, because the plan start was typed as today.
5. C43-6: should the "N end within 60 days" line stay hidden at 0?
6. Card extended warranty seeding: is the 48-month cap meant to be applied? It wasn't, on the fridge.
