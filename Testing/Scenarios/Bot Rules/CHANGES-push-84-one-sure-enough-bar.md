# Push 84: one "sure enough" bar for ticks, quick add and the full form (S9.10.5)

API only (UI unchanged). The 0.8 "sure enough to tick or attach" rule was written in three server places (quick add, the full form's default ticks, completing a purchase). It is now read from one function, `MatchPolicy.SureEnough`, with the identical threshold. Nothing should behave differently; a new test arrives the same receipt three ways (quick add, full form with the server's own ticks, full form left untouched) and checks they attach the same coverage.

## What to check (regression pass)
1. Quick add (New Items > Add as a new item with a sure coverage) attaches only the sure coverage, as in Push 80.
2. Add Details (the full form) from a New Item, left on its default ticks, attaches the same coverage as the quick add did for the same receipt.
3. Add a purchase (/add/new): ticked lines and saved coverage as in Push 81/83.
