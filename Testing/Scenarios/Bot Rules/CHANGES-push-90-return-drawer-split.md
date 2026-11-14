# Push 90: the "Mark as returned" drawer is its own component (S9.10.10, step 3)

UI only (API unchanged at bde7439). Push 89 (the Suggested coverage and People components) was tested and passed. This is the next step of the same split: the "Mark as returned" drawer on the item page is now `ItemReturnDrawerComponent`. Nothing should look or behave differently. The production build was checked locally before this push.

## What to check (item page, regression)
1. On an item with an open return window, "Mark returned" opens the drawer titled "Mark as returned": Date returned, Refund amount (with the "Leave empty if the money has not come back yet." hint), Paid back by (Not sure / not yet plus the refund methods), "How hard was it?" 1 to 5, Problems getting paid.
2. For an item with a protection plan, the plan question block appears ("Nothing about a plan changes until you answer.") and "Mark returned" stays disabled until it is answered; with no date it is disabled.
3. Saving marks the item returned (status, "Return recorded" banner and the entered refund/dates as before). A failed save shows its message in red in the drawer. Re-opening via "Edit return" shows the saved values.
4. Layout of the drawer unchanged.
