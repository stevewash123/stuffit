# Push 73: a store the server says to choose is never filled in silently (S9.10.5, first part)

UI only (API unchanged at 362340d). Fixes the Push 72 Medium: on the Add form, a receipt printing "Target Practice Supplies" filled that name in and created a private store.

## What to check (Add a purchase, upload a receipt on the form)
1. Upload the "Target Practice Supplies" receipt on /add/new: the "What we found in your document" panel opens (it does not fill the form and toast). The store is not filled in until you choose; no private "Target Practice Supplies" appears in your data unless you tick it in the panel and save.
2. Receipts with a sure store (Home Depot, Walmart, Lowe's, Sam's Club) still fill the form straight away with the toast, as before.
3. Unchanged otherwise. (Known and left for the next UI push: the Add form and New Items give slightly different coverage lists for the same receipt; the panel does not yet show the Target candidate as a pick.)
