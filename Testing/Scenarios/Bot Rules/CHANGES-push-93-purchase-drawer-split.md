# Push 93: the "Edit purchase" drawer is its own component (S9.10.10, step 5)

UI only (API unchanged at bde7439). Push 92 (stale drawer errors) passed. Same kind of step as Pushes 90 and 91: the "Edit purchase" drawer on the item page is now `ItemPurchaseDrawerComponent`. Nothing should look or behave differently. The production build was checked locally before this push.

## What to check (item page, Edit mode, regression)
1. Edit mode > the pencil by the purchase opens "Edit purchase": the hint "Coverage you already confirmed keeps its dates. New suggestions will use these details.", Store picker (prefilled), Date bought (with precision/approximate options), Credit card used (Not sure / cash plus the cards), Total paid, Order number, Notes.
2. Pick PayPal as the card: "Which credit card is behind PayPal?" appears with the bank cards (not PayPal itself) and its warning-coloured hint until one is chosen; pick another card and it goes away.
3. Save is disabled with no date or while saving; a failed save shows the red message in the drawer; a good save updates the purchase card and the coverage as before.
4. Layout of the drawer unchanged.
