# Push 91: the "Replaced by the plan" drawer is its own component (S9.10.10, step 4)

UI only (API unchanged at bde7439). Push 90 (the "Mark as returned" drawer) passed. Same kind of step: the "Replaced by the plan" drawer on the item page is now `ItemReplaceDrawerComponent`. Nothing should look or behave differently. The production build was checked locally before this push.

## What to check (item page, regression)
1. On an item with a protection plan, the replace flow opens the "Replaced by the plan" drawer: the sentence "This makes the replacement as a new item. <item> is marked replaced and kept here with its history and files.", Name (prefilled with the item's name), Brand picker (prefilled), Model, Serial number, Replaced on (today).
2. The plan question block appears when the item has plans; "Make the replacement" stays disabled until the plan question is answered, and while Name or the date is empty.
3. Saving creates the replacement item and marks the old one replaced (as before); a failed save shows its red message in the drawer.
4. Layout of the drawer unchanged.
