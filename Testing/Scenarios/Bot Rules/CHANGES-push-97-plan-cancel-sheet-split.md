# Push 97: the "Cancel this plan" sheet is its own component (S9.10.12, step 1)

UI only (API unchanged at bde7439). Push 96 (plan start asked on Add coverage) passed. The first piece of the plan page split (S9.10.12): the cancel, stop-renewing and refund sheet moved out of the plan page into `PlanCancelSheetComponent`, which owns its own steps, fields and the cancel, undo and refund calls. Nothing should look or behave differently. The production build was checked locally before this push.

## What to check (plan page, regression)
1. "Cancel this plan" (or "Cancel" on a plan that covers nothing, or the one on the gone-items note) opens the sheet: "What do you want to do?" with "Stop it renewing" (only on a plan that auto-renews and is not already set not to renew), "Cancel it now", and "It already ended or I cancelled it" (this one closes the sheet and puts the cursor in the "It ended on" field).
2. Cancel it now > the terms step: "What we hold" (the plan's saved "Cancelling:" lines, or "No cancellation terms saved for this plan."), the contract number with Copy ("Copied" and a toast), the phone and website links, then "Cancelled on" (defaults to today; a date before the plan starts shows "The date is before the plan starts..."), "How did you cancel?", and the button. Back returns to the choice.
3. Confirming shows "Cancelled <date>." with Undo (about 10 seconds), "Record a refund" and Done. Undo brings the plan back with "Cancellation undone." Stop it renewing shows "Done. It ends <date> and will not renew."
4. Record a refund: Amount (must be above zero), Date you got it, How it came back; "Save refund" shows "Refund recorded."; "I haven't got it yet" closes. Opening the plan from "/plans/<id>?refund=1" on a cancelled plan opens the refund step straight away.
5. "Re-open this plan" (with its optional note) on a cancelled plan still works from the page.
6. A failed cancel or refund shows its message in the sheet; layout unchanged.
