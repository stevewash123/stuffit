# UAT retest: Push 33 item changes and plan form

- **Test date:** Nov 7, 2026 (ET).
- **Build:** API `bd40de6`, started Nov 6 at 10:35:25 PM ET. UI Last-Modified Nov 6 at 10:34:17 PM ET; notes cite UI `67b9071` (UI commit not independently verified). Migration ItemReplacedAndPlanAnswers recorded applied in the handoff.
- **Accounts:** Alice (customer, Settings label QA Test 1) and Ops (F3 admin). No Bob or Carol tests.
- **Clock:** maintenance endpoint GET `/api/maintenance/clock` verified **Offset 0** at 8:53 AM ET. Browser workers could not see the offset in Settings but made no clock changes. No clock move needed.
- **Scope:** targeted only, not regression: Push 33 S3.4.16 / S3.4.18 steps 1–8 plus Push 32 fixes F1–F3. This consolidates the completed browser findings; no new test run was performed while writing it.
- **Evidence:** findings reproduced below and screenshots in `/workspace/uat/push33-shots/`. F3 has written observations only, no saved screenshots.
- **Synthetic fixture:** F2 reused `fixtures/P32-synthetic-test-contract-enrolment-60d-gap-75d.pdf`, fictional QA material, not a real policy.

## Summary
18 result rows: F1–F3 once each, Gate once, 1a–1d, 2a–2b, 3 Carry/End/Restart, and 4–8.
- **Pass: 14:** F1, F2, F3; 1b, 1c, 1d, 2a, 2b, 3 Carry, 4, 5, 6, 7, 8.
- **Partial: 1:** 1a (Yes, refunded preselected on a manually added plan; required amount, refund recording and cancellation worked).
- **Fail: 3:** replacement gate, 3 End, 3 Restart. These are three failed checks of the same observed auto-carry gap, not three confirmed independent causes.
- F3's **7/7** sub-checks are included as one summary row, not seven extra passes.
- Optional 360px check **Not run**. F1 Sub-Zero retest **Pass supersedes** Batch A/B's initial absent-card/transition-not-run finding.

## Needs CC
1. **Fail — replacement bypasses explicit plan answer (Gate, 3 End, 3 Restart).** On Alice create an item with a running manually added single-item plan, as for P33-Plan-Repl-End / P33-Plan-Repl-Restart. Open **Replaced by the plan**, enter replacement details and complete the flow. Expected: require a plan answer and offer Carry on / End / Restart from replacement date, honoring the chosen answer. Actual: no plan question, End or Restart; both flows auto-carried. Toast: “Vacuum is marked replaced by Vacuum. P33-Plan-Repl-End: carries on with the replacement.” Restart produced the corresponding P33-Plan-Repl-Restart toast. Evidence: `3-end-auto-carry.jpg`, `3-restart-auto-carry.jpg`. Carry itself passes. The restart fixture used the same replacement date as the original plan start, so dates alone cannot distinguish restart; absence of the choice is the demonstrated failure. Retest with distinct dates after the choice is fixed.
2. **Partial — manual plan defaults to Yes, refunded (1a).** Create an item and add a plan manually, not from a receipt. Open **Mark returned** and inspect “Did you return [plan] too?” before choosing. Expected: Yes, refunded preselected only for a plan read from the item's receipt. Actual: already selected on manual P33-Plan-Ret-Refund. Blank amount was correctly blocked; $49 then cancelled the plan Nov 7 and recorded the refund. Evidence: `1a-no-amount.jpg`, `1a-result.jpg`.
3. **Follow-up observation, not an extra failed summary row:** the Restart replacement page retained original model/serial after replacement values were attempted. Enter distinct replacement model/serial, complete replacement, and inspect the new page. Attempted values were not recorded in the findings; confirm in a focused retest before claiming a root cause. Evidence: `3-restart-auto-carry.jpg`.

## Fixtures left in place
- P33-* test data on Alice, including returned/disposed items, retained plans, replacement histories and auto-carried plans, document-plan fixture and initial start-notice fixture. The delete-test items were deleted as part of their tests; remaining plan records are retained.
- `P33 Sub-Zero StartNotice Fridge`, item `01a1b64b-209a-7060-a403-9ca45fc1d250`, has the completed start-date reminder.
- P33-Multi-A deleted; P33-Multi-B remains on active P33-Plan-Multi. P33-Only deleted; P33-Plan-Only kept empty. P33-Undo is owned/active again with original plan dates. P33-Form has no plan.
- **P33-ClaimsCo** left as test data: website `https://p33claimsco.example`, claims `https://claims.othersite.com/`, own-site returns `https://p33claimsco.example/returns`, source `https://p33claimsco.example`. Off-site support was rejected. No edits to other shared companies are recorded.
- These are end-of-test states before any later DB Stager reset; this report does not claim a reset occurred.

## Limits / not reported as new
- Optional **360px** check not run. Undo was observed through returned-state render, not a timed whole-session test.
- F2 conditional typed-end check not applicable: parsed end matched start plus term. Optional thrown-away wording and Add-items-after-Keep not documented as run.
- Ended-plan end-date versus last-covered-day wording is **by design**, not a new defect. Known gaps / unchanged Push 26–32 behavior excluded; no regression or new scenario plan.
- Superseded source status: Batch A/B's F1 absent card, F3 deferred, and C/D not yet run are historical worker-scope notes, not final run outcomes. The initial Dryer did not trigger an installation-start notice; the Sub-Zero retest did. Worker inability to verify clock is superseded by the parent maintenance check above.

## Detailed results and exact observations
The following source findings retain exact messages, dates and evidence paths. Historical worker-scope notes have been removed where later batches supersede them.

### F1 — final retest (superseding initial attempt)

# Push 33 — start-date notification retest (F1b)

**Result: Pass.** The installation-start notice appeared before a start date was entered. After saving the date, the item’s To do reminder was marked Done. A full reload of `/notifications` showed the same notification with the shortcut **Open** (not **Enter the date**); clicking it opened the fixture’s item page.

## Fixture
- Item: `P33 Sub-Zero StartNotice Fridge`
- Brand/category: Sub-Zero / Major appliances
- Purchase date: 2026-11-07
- Kept the checked, confirmed 2-year Sub-Zero manufacturer warranty. Its offered notice read exactly: **“Counted from today until you give the date.”**
- The notification card title was exactly: **“Enter the start date of your Sub-Zero warranty”**.
- Card body: **“The warranty on P33 Sub-Zero StartNotice Fridge starts when it is installed, not when you bought it. Until you enter the installation date we count from the purchase date.”**

## Checks and evidence
1. Opened `/notifications` in a second tab before entering any start date; after the fixture was saved, reloaded that tab. The card showed **Needs action**, **Unread**, and shortcut **Enter the date**. Screenshot: `/workspace/uat/push33-shots/F1b-01-notifications-enter-date.png`
2. On the item page, entered `2026-11-07` and clicked **Save the start date**. Expanded the hidden completed reminders; the To do reminder displayed **Done**. Screenshot: `/workspace/uat/push33-shots/F1b-02-item-todo-done.png`
3. Fully reloaded `/notifications`. The card remained and its shortcut was **Open**, not **Enter the date**; no **Needs action** badge or date-entry controls were present. Screenshot: `/workspace/uat/push33-shots/F1b-03-notifications-open.png`
4. Clicking **Open** navigated to `https://stuffit-ui.onrender.com/items/01a1b64b-209a-7060-a403-9ca45fc1d250` (`P33 Sub-Zero StartNotice Fridge`).

Note: the notification card itself did not render a literal “Done” label; completion was shown on the item page’s completed-reminders list, while the reloaded notification’s shortcut changed to **Open**.

### F2 and steps 1–4

### F2 — Counted from start: **Pass**
- Expected: PDF parsing keeps the 12-month term when end = start + term; the plan page, item Add-on protection card, and edit form display the counted-from-start sentence. The PDF-upload/start-from-document path was used to create the plan.
- Observed: Parsed start `Oct 15, 2026`, end `Oct 15, 2027`; all three views showed **“The end date was counted from the start, Oct 15, 2026, plus 12 months.”** The source document's 75-day purchase-to-order gap also produced the UI warning **“Your plan says ‘within 60 days of purchase of the covered item’; your dates are 75 days apart. Check the contract.”** Since parsed end equaled start + term, the conditional typed-end test was not applicable.
- Evidence: `/workspace/uat/push33-shots/A-F2-plan.jpg`, `/workspace/uat/push33-shots/A-F2-item.jpg`, `/workspace/uat/push33-shots/A-F2-edit.jpg`

## Batch B

### Gate — no unanswered plan action: **Fail overall**
- Return: With no plan answer selected, the form named **“Did you return P33-Plan-Ret-Refund too?”**, said **“Nothing about a plan changes until you answer.”**, and disabled **“Mark returned”**. Pass for this action. Evidence: `/workspace/uat/push33-shots/gate-return.jpg`
- Delete: The dialog said **“A protection plan covers Fan”**, **“Fan and its coverage and files will be deleted. This cannot be undone. Nothing about the plan changes until you answer.”**, and **“What about P33-Plan-Del-Drop?”**; **“Delete item”** was disabled. Pass. Evidence: `/workspace/uat/push33-shots/gate-delete.jpg`
- Dispose: With Q1 and the plan answer unanswered, the dialog named P33-Plan-Disp and kept **“Mark disposed”** unavailable. Pass. Evidence: `/workspace/uat/push33-shots/gate-dispose.jpg`
- Replace: The replacement flow did not present an unanswered plan question; it committed to carry and showed **“Vacuum is marked replaced by Vacuum. P33-Plan-Repl-End: carries on with the replacement.”** Fail: replacement was not gated on an explicit plan choice.

### 1a — Return, yes/refunded: **Partial**
- Expected: A manual plan should not have “Yes, refunded” preselected; saving without an amount is blocked; with $49 entered, plan cancels on return date and refund is recorded.
- Observed: **“Yes, refunded”** was preselected even though the plan was manual (unexpected). Saving with the amount blank displayed **“Enter the amount that came back.”** After entering `$49`, the toast read **“Toaster is marked returned. P33-Plan-Ret-Refund: cancelled, refund recorded.”** The plan was cancelled on Nov 7, 2026 and showed refunded `$49.00`; return details also said **“Not paid yet.”**
- Evidence: `/workspace/uat/push33-shots/1a-no-amount.jpg`, `/workspace/uat/push33-shots/1a-result.jpg`

### 1b — Return, yes/no refund: **Pass**
- Observed: Toast **“Kettle is marked returned. P33-Plan-Ret-NoRefund: cancelled.”** Plan ended Nov 7, 2026 without a refund.
- Evidence: `/workspace/uat/push33-shots/1b-no-refund.jpg`

### 1c — Return, keeping plan: **Pass**
- Observed: Toast **“Blender is marked returned. P33-Plan-Ret-Keep: kept, with a to-do.”** Plan remained active. The plan page showed **“Covers an item you no longer have”** and **“Blender: returned”**, with a to-do/action to take it off the plan or cancel it.
- Evidence: `/workspace/uat/push33-shots/1c-keep.jpg`, `/workspace/uat/push33-shots/1c-plan.jpg`

### 1d — Return, not sure: **Pass**
- Observed: Toast **“Mixer is marked returned. P33-Plan-Ret-NotSure: left as it is, with a to-do.”** Plan remained active/unchanged. The plan list also labeled it **“covers an item you no longer have”** while the uncertainty to-do remained.
- Evidence: `/workspace/uat/push33-shots/1d-not-sure.jpg`

### 2a — Delete, drop item from plan: **Pass**
- Observed: The dialog named **P33-Plan-Del-Drop** and offered **“Drop Fan from the plan”**. After deletion, the running plan showed **“Covers nothing”** / **“No items are on this plan now. Nothing about it changes unless you choose.”**
- Evidence: `/workspace/uat/push33-shots/2a-dialog.jpg`, `/workspace/uat/push33-shots/2a-plan-running.jpg`

### 2b — Delete, cancel plan too: **Pass**
- Observed: The dialog named **P33-Plan-Del-Cancel** and selected **“Cancel the plan too”**. The plan was cancelled on Nov 7, 2026; its page offered **“Re-open this plan”**. Reopening succeeded; it was active again and showed **“Covers nothing.”**
- Evidence: `/workspace/uat/push33-shots/2b-dialog.jpg`, `/workspace/uat/push33-shots/2b-plan-cancelled.jpg`, `/workspace/uat/push33-shots/2b-reopened.jpg`

### 3 Carry — replacement: **Pass**
- Observed: Plan carried to the replacement; toast **“Vacuum is marked replaced by Vacuum. P33-Plan-Repl-Carry: carries on with the replacement.”** The old item displayed **“Replaced”** and a replacement link/history.
- Evidence: `/workspace/uat/push33-shots/3-carry.jpg`, `/workspace/uat/push33-shots/3-carry-old.jpg`

### 3 End — replacement: **Fail**
- Expected: Plan ends.
- Observed: No End choice was available; flow auto-carried the plan and showed **“Vacuum is marked replaced by Vacuum. P33-Plan-Repl-End: carries on with the replacement.”**
- Evidence: `/workspace/uat/push33-shots/3-end-auto-carry.jpg`

### 3 Restart — replacement: **Fail**
- Expected: Plan restarts on the replacement date.
- Observed: No Restart choice was available; flow auto-carried the plan and showed **“Vacuum is marked replaced by Vacuum. P33-Plan-Repl-Restart: carries on with the replacement.”** The replacement page still displayed the original model/serial after replacement values were attempted, so that detail also needs follow-up. The replacement date was the same as the original plan start date, so a changed start date could not otherwise be distinguished.
- Evidence: `/workspace/uat/push33-shots/3-restart-auto-carry.jpg`

### 4 Sold, leave plan with new owner: **Pass**
- Observed: Q1 **“I sold it”** was answered before the plan question; **“Leave it with the new owner”** was selected. Neutral wording: **“Stops covering this item. Whether a plan can be passed on is in its contract. The plan carries on for anything else it covers.”** Result toast: **“Speaker is marked disposed of. P33-Plan-Disp: no longer covers it.”**
- Evidence: `/workspace/uat/push33-shots/4-sold-dialog.jpg`, `/workspace/uat/push33-shots/4-sold-result.jpg`


### Steps 5–8

## Check 5 — Pass

**Expected:** Delete P33-Multi-A using “drop”; P33-Multi-B remains covered and P33-Plan-Multi remains running.

**Observed:** The delete confirmation said “A protection plan covers P33-Multi-A” and “P33-Multi-A and its coverage and files will be deleted. This cannot be undone. Nothing about the plan changes until you answer.” Under “What about P33-Plan-Multi?” it said “It also covers P33-Multi-B. That one keeps the plan whatever you choose.” I selected “Drop P33-Multi-A from the plan” / “The plan stays for the other items.” After deletion, P33-Plan-Multi remained active through Nov 7, 2028, cost `$49.00 one payment`, and covered P33-Multi-B only.

**Screenshots:**
- `/workspace/uat/push33-shots/CD-05-delete-choice.png`
- `/workspace/uat/push33-shots/CD-05-plan-remains.png`

## Check 6 — Pass

**Expected:** Delete P33-Only using “drop”; the now-empty P33-Plan-Only offers Add items / Cancel / Keep; Keep persists after reload without repeating the prompt.

**Observed:** P33-Only was created with Router / RT1 / P33S13, then deleted using “Drop P33-Only from the plan” / “The plan stays, covering nothing. You can add items or cancel it later.” The plan page showed “Covers nothing” and “No items are on this plan now. Nothing about it changes unless you choose.” I pressed Keep; after reload it showed “No items are on this plan. You chose to keep it as it is.” The choices did not repeat. Plan remains uncancelled.

**Screenshots:**
- `/workspace/uat/push33-shots/CD-06-delete-choice.png`
- `/workspace/uat/push33-shots/CD-06-empty-plan-choices.png`
- `/workspace/uat/push33-shots/CD-06-kept-after-reload.png`

## Check 7 — Pass

**Expected:** Mark P33-Undo returned; choose Yes, no refund (cancel); Undo restores ownership and the original active plan dates.

**Observed:** The returned form asked “Did you return P33-Plan-Undo too?” The selected option was “Yes, no refund” with “Ends the plan on Nov 7, 2026 without a refund.” The result message was “P33-Undo is marked returned. P33-Plan-Undo: cancelled.” The Undo bar was visible through the returned-state render; pressing Undo produced an “Undone.” toast. P33-Undo returned to Active/owned and P33-Plan-Undo returned to Active with its original Nov 7, 2026–Nov 6, 2028 dates. No return-specific to-do remained. The pre-existing “Add the rest of your Asurion plan” reminder (visible before the return) remained.

**Screenshots:**
- `/workspace/uat/push33-shots/CD-07-return-plan-question.png`
- `/workspace/uat/push33-shots/CD-07-before-undo.png`
- `/workspace/uat/push33-shots/CD-07-after-undo.png`

## Check 8 — Pass (optional 360px check not run)

**Expected:** Empty save shows field-specific messages, focuses and scrolls the first required field into view, with no generic validation summary; future start shows “Not started yet”; unsaved changes can be kept or discarded; no plan is created. Optional end-before-start check included.

**Observed:** Empty submit displayed each required-field message separately:
- Company: “Choose the company that sold the plan, or type its name and add it.”
- Plan name: “Give the plan a name.”
- Start date: “Say when the plan started.”

Focus was on the Company field, visible after scrolling. No “One or more validation errors occurred.” wording appeared. For Nov 7, 2026 + 30 days (Dec 7, 2026), the form showed “Not started yet: the plan starts on Dec 7, 2026. It is listed, and does not count as coverage until then.” Navigating away opened “Leave without saving?” / “You have changes that have not been saved. If you leave this page now they will be lost.” with “Keep editing” and “Leave without saving.” Keep editing preserved the entered plan name and start date. The optional end-before-start message appeared exactly as “The end date is before the start date. Did you mean Dec 6, 2027?” I then chose Leave without saving; P33-Form still showed “Not set up yet” and no plan.

**Optional 360px width:** Not run.

**Screenshots:**
- `/workspace/uat/push33-shots/CD-08-empty-validation.png`
- `/workspace/uat/push33-shots/CD-08-future-start.png`
- `/workspace/uat/push33-shots/CD-08-unsaved-warning.png`
- `/workspace/uat/push33-shots/CD-08-end-before-start.png`
- `/workspace/uat/push33-shots/CD-08-discarded-no-plan.png`


### F3 — admin claims and Edit pages

# Push 33 Fix F3 — UAT Findings

**Environment:** Test admin UI at `https://stuffit-ui.onrender.com/admin`  
**Target:** P33-ClaimsCo only  
**Date:** Nov 7, 2026  
**Outcome:** All seven requested sub-checks passed.

## Results

| Sub-check | Result | Finding / exact message | Field location |
|---|---|---|---|
| 1. Website | **PASS** | Website was blank. Set to `https://p33claimsco.example`; save completed and website link appeared on P33-ClaimsCo. | Shared data → P33-ClaimsCo → Edit details → Website |
| 2a. Claims page `http://example.com` | **PASS** | Rejected. Exact text: `The claims or support page must be an https address of a real website (for example https://www.example.com/returns).` | Edit details dialog → Claims or support page; alert also appeared at page level |
| 2b. Claims page `not a website` | **PASS** | Rejected. Exact text: `The claims or support page must be an https address of a real website (for example https://www.example.com/returns).` | Edit details dialog → Claims or support page; alert also appeared at page level |
| 2c. Claims page `https://claims.othersite.com` | **PASS** | Accepted; saved and reopened to confirm. Reopened value normalized to `https://claims.othersite.com/` (trailing slash). | Edit details dialog → Claims or support page |
| 3. Returns off-site `https://claims.othersite.com/returns` | **PASS** | Rejected. Exact text: `The returns page must be on the company's own site (https://p33claimsco.example), not another website.` | Companies tab → search P33-ClaimsCo → Company pages → Edit pages → Returns page (https) |
| 3. Support off-site `https://claims.othersite.com/support` | **PASS** | Rejected. Exact text: `The customer support page must be on the company's own site (https://p33claimsco.example), not another website.` | Companies tab → search P33-ClaimsCo → Company pages → Edit pages → Customer support page (https) |
| 3. Own-site returns `https://p33claimsco.example/returns` | **PASS** | Accepted and confirmed in the company list as `Returns page: https://p33claimsco.example/returns · confirmed Nov 7, 2026 · read on this page`. Source page entered: `https://p33claimsco.example`; optional words left blank. | Companies tab → P33-ClaimsCo → Company pages → Edit pages → Returns page (https); source field “Address of the page you read the link on” |

## Companies tab check

The Companies tab does not contain the “Claims or support page” field. It has the separate Company pages editor for Returns page and Customer support page. Claims or support page is in the P33-ClaimsCo Shared data Edit details dialog.


## Source files
- HANDOFF-push33-retest.txt
- CHANGES-push-33-when-the-item-changes-and-plan-form-2026-11-06.md
- push33-browser-checklist.md
- push33-findings-batchAB.md
- push33-findings-batchCD.md
- push33-findings-F1b.md
- push33-findings-F3.md

Markdown report only; no Canvas/Page used.
