# Push 74: a store the server says to choose starts unticked (S9.10.5)

UI only (API unchanged at 362340d). Fixes the Push 73 finding: in the "What we found in your document" panel the Target Practice Supplies store row was ticked by default, so Update All filled it and created a private store.

## What to check (Add a purchase, upload the Target Practice receipt on /add/new)
1. The panel opens and the Store row is NOT ticked. Update All fills the other facts and leaves Store empty; no private "Target Practice Supplies" is created.
2. If you tick Store on purpose and click Update All, the form takes it (the panel says "New store: added to your local data" before you do). That path still creates the private store when applied; it is a deliberate tick now, not a default. Creating it only on Save is a later change (S9.10.6 candidate picks).
3. Sure stores (Home Depot, Walmart, Lowe's, Sam's Club) still fill straight away with the toast.
