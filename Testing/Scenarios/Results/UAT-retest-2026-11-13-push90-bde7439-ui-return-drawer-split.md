# UAT retest: Push 90, "Mark as returned" drawer is its own component

- **Build tested:** API `bde7439` (/api/version, startedAt 2026-11-13 03:58 UTC); UI Last-Modified **Fri, 13 Nov 2026 12:17:50 UTC (7:17 AM ET)**, re-checked unchanged after the run (7:40 AM ET).
- **Scope:** `CHANGES-push-90-return-drawer-split.md`. Regression only (nothing should look or behave differently). Push 89 passed (4 Pass, 0 Fail). NEXT-REPORT-ADDITIONS.md: none.
- **Tester / account:** QA Controller, box browser, Alice (QA Test 1, "P34-Alice Repairs"), 7:37–7:40 AM ET Nov 13 2026.
- **Test items:** "P90 UAT Return Window" (Walmart/Vizio fixture `push85/30-thermal-walmart-vizio-tv-protection.pdf`, Electronics, Walmart electronics 30-day window, no plan) and "P90 UAT With Plan" (same fixture, plus an Allstate warranty extension typed in on the item page, 24 months). Both deleted afterwards. No new fixtures.
- **Caveat:** a "new version is ready" banner showed on item A's page while the drawer was open (tab loaded before the 7:17 deploy finished). Reload was not clicked; item B and cleanup ran on fresh page loads of the 12:17:50 build.

## Results

| # | Check | Result |
|---|---|---|
| 1 | Drawer on an item with an open return window | **Pass** |
| 2 | Plan question block; Mark returned disabled until answered and with no date | **Pass** |
| 3 | Save, error message in red, Edit return prefilled | **Pass** (1 Info) |
| 4 | Drawer layout | **Pass** |

**4 Pass, 0 Fail, 3 Info.**

### 1. Drawer (item A)
Title "Mark as returned" with Close (×). Date returned defaults to 2026-11-13. Refund amount prefilled with **328** (item price), hint "Leave empty if the money has not come back yet." Paid back by: Not sure / not yet (default), Back to the original payment, Store credit, Gift card, Exchange, Cash, Check, Other. "How hard was it?" radios 1–5, none picked, hint "1 is easy, 5 is very hard." Problems getting paid: empty text box. Button "Mark returned". Shot `02-itemA-drawer-default.png`.

### 2. Plan question (item B) and empty date
Block "Did you return Warranty extension too?" / "Allstate · Nov 10, 2026 to Nov 9, 2028", options Yes, refunded / Yes, no refund / No, I'm keeping it / Not sure (each with its explanation), and "Nothing about a plan changes until you answer." Mark returned disabled until answered, then enabled. On A, clearing Date returned disabled the button; restoring it re-enabled. Shots `08-itemB-plan-question-disabled.png`, `03-itemA-no-date-disabled.png`.

### 3. Save, error, Edit return
- A saved (today, 100.00, Store credit, 3, "P90 test"): status **Returned**; "The return" card shows Returned Nov 13, 2026 · Refund $100.00 · Store credit · How hard 3 of 5 · Some hassle · Problems P90 test; Money recovered "$100.00 · Store refund · Nov 13, 2026 · Store credit · credit, not cash"; header now Edit pencil and "I have it again". Shot `05-itemA-after-save.png`.
- Edit return reopened with every saved value prefilled (title still "Mark as returned"). Shot `06-itemA-edit-return-prefilled.png`.
- Refund -50: red boxed message in the drawer, "The field RefundAmount must be between 0 and 100000000." Closed without saving; item kept $100.00. Shot `07-itemA-negative-refund-error.png`.
- B saved with "No, I'm keeping it", refund 328: green banner "P90 UAT With Plan is marked returned. Warranty extension: kept, with a to-do." (Undo, Dismiss); plan stayed Active; to-do "Warranty extension still covers P90 UAT With Plan, which you returned…". Shot `09-itemB-after-save-banner.png`.

### 4. Layout
Normal in every state (default, plan block, red error): no squashing or overlap, consistent spacing, full-width button aligned at the bottom. Shot `04-itemA-drawer-filled-full.png`.

## Info
- **Info:** after saving A (no plan) no "Return recorded" / success banner was seen at ~3 s; B (with plan) showed its banner. A's tab was on the pre-deploy page (see caveat), so this may be stale-tab or a short-lived toast. Worth a glance against the pre-split behaviour; the saved data and status were correct.
- **Info:** the negative-refund message is the raw server validation text ("The field RefundAmount must be between 0 and 100000000."), not friendly wording. Likely unchanged by this refactor.
- **Info:** Refund amount is prefilled with the item price while the hint says to leave it empty if the money hasn't come back; easy to save a refund that didn't happen. Probably pre-existing.

## Cleanup
Both P90 items deleted (B needed "Cancel the plan too"); My Items search "P90" shows "No items match." Shot `10-cleanup-search-P90-empty.png`.

Screenshots: `/workspace/uat/push90/shots/`.
