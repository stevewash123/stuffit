# Push 70: a partial store name stops binding on its own (S2.8.3, store half)

API only (UI unchanged).

## What changed
A one-word known store ("Target", "Smith") that only starts a longer printed name is no longer taken as that store, unless the rest is store wording (Supercenter, Home Improvement, Pharmacy, Club, Pro Desk, a store number). Multi-word names ("Home Depot Pro Desk", "Best Buy Mobile") and exact/alias matches work as before.

## What to check
1. A receipt printing "Lowe's Home Improvement", "Walmart Supercenter", "SAMS CLUB #6452", "THE HOME DEPOT": same store as before.
2. A receipt whose store reads like "Target Practice Supplies" (or any one-word known store followed by an unrelated word): store is NOT filled in with the known one, and no new private store appears by itself. (If you cannot make such a receipt, skip: covered by unit tests.)
3. Ops summary (`/api/admin/match-decisions/summary`) may now show a rule `candidate` for such names.
Note: no question is asked of the person yet for a candidate (that is S2.8.4); the store field is simply left for them to pick.
