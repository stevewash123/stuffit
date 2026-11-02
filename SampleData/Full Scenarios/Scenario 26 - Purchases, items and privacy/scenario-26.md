# Scenario 26: Add purchases, check suggested coverage, browse items, prove privacy

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com), both signed up (Scenario 25)
**Preconditions:** The reference data is loaded (stores, brands, return and warranty policies). Neither account has any purchases.
**Time:** 35 min
**Why this plan:** purchases, items, suggested coverage and the items list are built and were checked end to end. It also checks that one person's data never shows for another.

Use real names from the dropdowns. If a store or brand you want isn't offered, pick another and note which.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open **New Items**, then choose the option to add a purchase by hand (blank form) | The Add purchase form opens. Store comes first (one receipt can hold several items), then date, card, order number; category, brand and item name follow. Price is under "More about this item" |
| 2 | Test1 | Save with nothing filled in | Required fields are called out; nothing saved |
| 3 | Test1 | Add a purchase: pick a store from the list that has a known return policy, pick a brand that has a known warranty, item name "UAT Blender", price 89.99, purchase date = today | Saves; goes to the item or items list |
| 4 | Test1 | Open **My Items**, open the new item | Item opens read-only. Shows the purchase, the store, price and date |
| 5 | Test1 | Look at the coverage shown on the item | A suggested return window and a manufacturer warranty from the shared data, each with an end date computed from today. The "usual window, can differ for your item" doubt appears among the reasons (hover the confidence score on a suggestion, or in Suggest coverage); record where, if anywhere, it shows. Record each end date and verify the arithmetic from today |
| 6 | Test1 | Click the pencil (edit) | Edit mode: icons for edit and delete, Add coverage, receipt upload |
| 7 | Test1 | Change the item name to "UAT Blender 2", save, return to read-only | The new name shows on the item and in My Items |
| 8 | Test1 | Add a second purchase with "I am not sure of the exact date" > Only the month, choosing an EARLIER month than the current one (the app clamps a month to today, so the current month on the 1st collapses to one day), name "UAT Toaster", price 25.00 | Saved as "Bought <month> (approximate)"; NO store return window is suggested or shown (return windows are not tracked from an approximate date); the manufacturer warranty, if any, shows as a range ("Ends between X and Y (date estimated)") |
| 9 | Test1 | On UAT Blender 2 in edit mode, choose a small test image under "Add a receipt or other file". While "Reading your document…" is showing, look at the Upload button and hover over it. If the reading is too quick to see, record that | While "Reading your document…" is showing, the Upload button is disabled and its tooltip reads "Wait until the document has been read". After the reading finishes the person can proceed (the Upload button turns on, or the document's questions appear; record which) |
| 10 | Test1 | Upload a small test image as a receipt on UAT Blender 2 | The file attaches and can be viewed again; the photo is shown without location data (note: just confirm it opens) |
| 11 | Test1 | In My Items, search "Toaster", then "Blender", then a word that matches nothing | Matching items only each time; a friendly empty state for no match |
| 12 | Test1 | Use the filter button on the items page | Filters narrow the list; clearing restores it |
| 13 | Test1 | Copy the full address of the UAT Blender 2 item page | Address noted |
| 14 | Test2 | Open My Items | Empty state: no UAT items |
| 15 | Test2 | Paste the Test1 item address in the browser | Not found or no access; no title, price or store from Test1 appears anywhere |
| 16 | Test2 | Add a purchase "UAT Kettle", price 19.00 from any store | Saved |
| 17 | Test1 | Search My Items for "Kettle" | Nothing. Test1 never sees Test2's items |
| 18 | Test1 | Delete UAT Toaster from edit mode, confirm | It leaves the list; Undo or "restore" works if offered |
| 19 | Test1 | Reload the page and sign out and back in | Everything still there as expected (Blender 2 present, Toaster gone or restorable) |

Also record: any date, amount or label that looks wrong, and any page that was slow to load (more than 3 seconds).
