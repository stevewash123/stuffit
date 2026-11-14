# Push 69: changing one item re-checks only that item's coverage

UI only. Fixes the Push 68 Medium (row 4): a change to one item reloaded every item's lookup, so one failure blanked the other rows.

## What to check (Add a purchase with two items)
1. Item 1 shows its coverage list. Change only item 2's category: only item 2 shows "Checking what applies…"; item 1's list stays. In Network, one coverage-preview call, not two.
2. With the request blocked, only item 2 shows "We could not check…". Item 1 keeps its good list. Try again on item 2 reloads item 2 only.
3. Changing the store, date or card still re-checks every item (they apply to all).
4. Removing item 1 still leaves item 2 with its own list.
