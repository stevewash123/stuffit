# UAT retest: Push 92, a drawer's old error goes away when you edit the form

- **Build tested:** API `bde7439`; UI Last-Modified **Fri, 13 Nov 2026 13:44:01 UTC (8:44 AM ET)**, confirmed before and after the run. Fresh page load, no new-version banner.
- **Scope:** `CHANGES-push-92-stale-drawer-errors.md` (fix for the Push 91 Low). Push 91 is 4 Pass, 0 Fail after the Name re-check.
- **Tester / account:** QA Controller, box browser, Alice ("P34-Alice Repairs"), 9:01–9:05 AM ET Nov 13 2026. Real keyboard and mouse input; button states read from the real `disabled` property.
- **Test items:** "P92 UAT Item" (Walmart/Vizio fixture, Electronics) with an Allstate warranty extension typed in (24 months), and its replacement "P92 UAT Replacement". Both deleted. No new fixtures.

## Results

| # | Check | Result |
|---|---|---|
| 1 | Replaced by the plan: future-date error appears, clears on fixing the date, fresh error on retry, save works | **Pass** |
| 2 | Mark as returned: negative-refund error appears, clears on typing a valid amount | **Pass** |
| 3 | Rest of both drawers unchanged (fields, plan questions, disabled states, saving) | **Pass** |

**3 Pass, 0 Fail, 2 Info.**

### 1. Replaced by the plan
Plan answered "Carry on with the replacement". Replaced on 2027-06-01 > Make the replacement: red **"The replacement date cannot be in the future."** (shot 04). Typing 2026-11-13: message gone at once, before any click (05). Future date again + click: the same message appeared fresh; cleared again on today. Real save (Name "P92 UAT Replacement", today, Carry on): banner "P92 UAT Item is marked replaced by P92 UAT Replacement. Warranty extension: carries on with the replacement."; new item has the Allstate plan Aug 29 2026 – Aug 28 2028, Active; old item "Replaced" (08, 09).

### 2. Mark as returned
Plan answered "Not sure". Refund -50 > Mark returned: red **"The field RefundAmount must be between 0 and 100000000."** (01). Typing 100: message gone at once (02). Closed with × without saving; item stayed Active.

### 3. Unchanged behaviour
- Mark as returned: Date returned (today), Refund amount (prefilled 328, hint "Leave empty if the money has not come back yet."), Paid back by (8 options), How hard 1–5, Problems getting paid; plan block "Did you return Warranty extension too?" with 4 options and "Nothing about a plan changes until you answer."; `disabled` true until the plan question is answered and with no date (03).
- Replaced by the plan: Name, Brand, Model prefilled, Serial empty, Replaced on today; 3 plan options; `disabled` true before answering, with Name cleared (07), and with date cleared; false when restored.
- Returning the replacement (Not sure, 100, Store credit, How hard 2): status Returned, banner "P92 UAT Replacement is marked returned. Warranty extension: left as it is, with a to-do.", card "Returned Nov 13, 2026 · Refund $100.00 · Store credit · How hard 2 of 5 · Fairly easy", to-do "Decide what to do about Warranty extension on P92 UAT Replacement" (10).

## Info (not from this push)
- **Info (as Push 90):** the negative-refund message is the raw server text, not friendly wording.
- **Info (as Push 91):** the "Add the rest of your Allstate Protection Plans plan" to-do stays on the replaced item after the plan moves to the replacement.
- Not counted: typing a 5-digit year (12027) showed "The input field is required." (shot 06); that was a typing slip, and the server message is the raw default.

## Cleanup
Both P92 items deleted ("Cancel the plan too" on the replacement); My Items search "P92" shows "No items match." (11).

Screenshots: `/workspace/uat/push92/shots/`.
