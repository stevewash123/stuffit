# Push 76: pick between candidates, and the app learns (S9.10.6)

UI only (API unchanged at 29c6fda). This is the screen that calls `POST /api/match-feedback`, so the Push 75 steps that were blocked can now be run by clicking.

## What to check (Add a purchase, upload the Target Practice Supplies receipt on /add/new)
1. The "What we found" panel opens. The Store row shows a sentence ("Starts like Target, but may be something else.") and radio options: **Target** (selected as the main action) and "None of these: Target Practice Supplies (new)". The Store row is still unticked. No percentages anywhere.
2. Click **Target** (or leave it and tick the row), then Update: the Store field becomes Target (the known shared store), the toast/fields show no "(new)", and no private "Target Practice Supplies" is created. In Neon: one `match_feedback` row for Alice (store, key `targetpracticesupplies`, party Target, confirmed).
3. Upload the same receipt again: the store is now filled straight away as Target with no panel (match log rule `user`). Ops or another account uploading it still gets the panel.
4. Clean up/undo: DB Stager deletes Alice's `match_feedback` rows. Then repeat with **None of these** and Update: the store field becomes "Target Practice Supplies" (a new private store, as ticked on purpose) and a `match_feedback` row (store, same key, party Target, confirmed = false) is written; uploading the receipt again then offers no Target candidate for Alice.
5. Sure stores (Home Depot, Walmart, Lowe's, Sam's Club) still fill straight away with the toast.
Clean up: delete the private Target Practice Supplies party and Alice's match_feedback rows.
