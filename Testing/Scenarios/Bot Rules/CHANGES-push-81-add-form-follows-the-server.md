# Push 81: the Add form ticks by the server's decision (S9.10.5, UI part)

UI only (API unchanged at 018a5c1, Push 80). The Add form no longer applies its own 80% rule: a coverage line is ticked when the API says `decision: auto`, offered unticked for `choose`, and tucked behind "Other return windows (n)" for `ask`. The old numbers are only a fallback for a response without a decision.

## What to check (Add a purchase, regression: nothing should look different)
1. Same ticked/unticked coverage as Push 80/78 for the Walmart/Vizio, Lowe's/DeWalt and Home Depot receipts: Confirmed lines ticked, Likely lines not, an ended window greyed and unticked.
2. The "Other return windows (n)" link still appears for a store with extra windows and opens them. Ticking one return window still unticks the others.
3. Saving a purchase attaches exactly the ticked lines (as before).
