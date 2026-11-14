# Push 78: a closed return window is never pre-ticked on the item page

UI only (API unchanged at 29c6fda). Fixes a Low from the Push 77 report: the item page's suggestion list showed the Walmart electronics 30-day window (ended Sep 28, 2026) already ticked, while the Add form refuses it.

## What to check
1. Item page, suggestions list (Policies card, "suggested policies to review") for a purchase whose store's return window has already ended: that return line is NOT ticked. A window still open, a manufacturer warranty and card benefits are ticked/unticked as before.
2. You can still tick it by hand if you want it (only the default changed).
Note on the count: "N suggested policies to review" does not count alternate return windows (other windows the store may have for the item), but the list shows them. That is by design; the Push 77 "2 vs 3" is this.
