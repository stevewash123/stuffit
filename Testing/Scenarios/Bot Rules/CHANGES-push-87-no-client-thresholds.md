# Push 87: the screens keep no 80% rule of their own (S9.10.4 part two)

UI only (API unchanged at bde7439). The Add form, the item page and New Items used to fall back to their own "80% sure" arithmetic when a coverage line had no server decision. Every coverage response now carries one (Pushes 80 and 83), so the fallbacks are gone: a line is ticked, tucked or flagged only by the server's `decision`. Nothing should look different.

## What to check (regression: the same ticks as Push 86)
1. Add a purchase (/add/new): Walmart/Vizio, Lowe's/DeWalt, Home Depot receipts: the same lines ticked and unticked as in Push 81/84. The "Other return windows (n)" link still appears for a store with extra windows.
2. Item page suggestions (Policies card > Review): the same ticks as Push 83; an ended window still unticked.
3. New Items: chips and the "left to you on Add Details" suffix as in Push 86; quick add attaches the same lines.
Left in place on purpose: the Add form's own estimate for coverage from a paper attached on the form (TICKED_FROM and the document-fit values). The server has not seen that paper until Save, so that number is not a duplicate of the server's rule.
