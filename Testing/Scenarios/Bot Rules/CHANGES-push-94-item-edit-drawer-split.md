# Push 94: the "Edit item" drawer is its own component (S9.10.10, step 6)

UI only (API unchanged at bde7439). Push 93 (the "Edit purchase" drawer) passed. Same kind of step: the "Edit item" drawer on the item page is now `ItemEditDrawerComponent`. Nothing should look or behave differently. The production build was checked locally before this push.

## What to check (item page, Edit mode, regression)
1. Edit mode > the pencil by the item name opens "Edit item": Item (name), Brand (maker) picker prefilled, Category (Not sure plus the categories), Model, Size or variant, Serial number, Price, Status (Still have it / Returned / Gone / thrown out), Notes.
2. In a business account only: Asset tag and Location (with the saved locations offered as you type). A personal account shows neither.
3. Save is disabled when the name is empty or while saving; a failed save shows the red message in the drawer; a good save updates the item header, category and coverage as before.
4. Layout of the drawer unchanged.
