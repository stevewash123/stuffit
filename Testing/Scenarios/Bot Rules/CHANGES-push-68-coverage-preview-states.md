# Push 68: coverage preview states (S9.10.8) and shared intake helpers (S9.10.7)

UI only (API unchanged).

## What to check (Add a purchase)
1. Pick a store or brand: under "What it would be covered by" a short "Checking what applies…" shows while the lookup runs, then the list.
2. Change the category/brand quickly several times: the list always matches the last thing chosen, never an older answer.
3. If the lookup fails (e.g. Render asleep), the row says "We could not check the coverage just now" with a Try again button, not "Nothing found yet". Try again reloads it.
4. With two items on the form, each row has its own state; removing one does not mix them up.
5. Attaching a receipt, and PayPal "Which credit card is behind PayPal?" on add purchase and on the item page, behave as before.
