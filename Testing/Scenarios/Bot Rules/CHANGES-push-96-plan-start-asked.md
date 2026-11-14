# Push 96: a protection plan added through "Add coverage" asks when it started (fix for the Push 95 Medium)

UI only (API unchanged at bde7439). Push 95 (the coverage drawer split) passed 5 of 6; the Medium: Edit > Add coverage > pick "Protection plan" saved the plan with no start question. It is not from the split: the same code was in the page before. "Add coverage" fills Starts with the purchase date; the other routes to a plan ("Add protection plan", "I'll type it in", Add-on protection) clear it because a plan's start is asked, never filled in with the purchase date (S3.4.14). Now choosing "Protection plan" in the kind list clears that prefilled start too, so the plan form asks "Say when the plan started." like the others. Choosing another kind afterwards puts the purchase date back.

## What to check (item page, Edit mode)
1. Add coverage > What kind of coverage: Protection plan > leave the start untouched > Save plan: the field error "Say when the plan started." appears and nothing is saved. Choose a start basis/date and save: the plan is added.
2. Same drawer, change the kind back to Store warranty (or any other kind): Starts shows the purchase date again.
3. A new store warranty / manufacturer warranty / return window / card benefit through Add coverage still defaults Starts to the purchase date and saves as before.
4. "Add protection plan" and "I'll type it in" behave as before.
