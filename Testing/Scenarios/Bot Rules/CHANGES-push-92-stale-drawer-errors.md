# Push 92: a drawer's old error goes away when you edit the form (small fix from the Push 91 report)

UI only (API unchanged at bde7439). Push 91 (the "Replaced by the plan" drawer) is now 4 Pass (the empty-Name Fail was withdrawn). Its one Low: after a failed save ("The replacement date cannot be in the future."), the red message stayed even after the date was fixed. The same held for the "Mark as returned" drawer's red message. Both drawers now report an edit, and the item page clears the message at that point. A new failed save still shows its own message.

## What to check (item page)
1. "Replaced by the plan": set Replaced on to a future date, Make the replacement: the red message appears. Change the date to today: the red message disappears. Save again: works (or shows a fresh message if something else is wrong).
2. "Mark as returned": enter a negative refund, Mark returned: the red message appears. Change the amount to a valid number: the message disappears.
3. Nothing else about either drawer changed (fields, plan questions, disabled states, saving).
Also added in this push (tests only): a spec that the replace drawer's save follows the Name field.
