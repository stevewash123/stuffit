# Push 83: the item page ticks its suggestions by the server's decision (S9.10.5)

API and UI together. The item page's coverage suggestions (the "N suggested policies to review" list) now come with the server's `decision` (auto / choose / ask), the same rule as the Add form (Push 80/81). The item page ticks `auto` and leaves the rest unticked; the old number rule is only a fallback.

## What to check (item page, regression: nothing should look different)
1. Item page suggestions list (Policies card, Review) for a purchase with an open return window and a warranty: the same lines ticked as before (Confirmed ones ticked, Likely ones not). An ended return window is still not ticked.
2. In the network response of the item's suggestions, each entry has `decision`.
3. Ticking by hand, "Verify the above policy applies", and the added coverage behave as before.
