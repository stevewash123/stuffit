# Push 85: New Items follows the server's decision (S9.10.5)

UI only (API unchanged at bde7439). On New Items, the receipt-coverage warning ("Not added by a quick add: ...", in warning colour) now follows the server's `decision` (auto = a quick add attaches it) instead of a local 80% number.

## What to check (New Items, regression: nothing should look different)
1. A sure receipt line (e.g. the Geek Squad plan on the Walmart/Best Buy receipts that show one) has no "Not added by a quick add" text and is in the muted colour.
2. A doubtful line (e.g. a stated warranty with an unconfirmed provider) shows "Not added by a quick add ..." in the warning colour, as in Push 84.
3. Quick add still attaches only the sure coverage (as Push 84 check 1).

## Note on the Push 84 Partial
Picking category TVs then "Not sure" left Walmart general unticked. That follows the item name: "P84 UAT Vizio TV" contains "TV", so the server infers the category TVs even when the category box says "Not sure", and Walmart's general window is then Likely (choose), not auto. Not a regression from Push 80-84 (the ticks only change when someone toggles a line). To re-test the "unknown category" case, keep the item name free of a product word (e.g. "Item 1" or leave the document's own name).
