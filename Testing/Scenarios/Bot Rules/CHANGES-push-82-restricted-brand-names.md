# Push 82: some brand names are not taken from inside a product line (S2.8.3, brand half)

API only (UI unchanged). A brand that is also an ordinary word or name (Echo, Smith, K2, Target) is no longer picked out of a product line, because seeing the word in a line proves nothing. It still binds when the whole printed brand is exactly that name. Other brands (Samsung, LG, Milwaukee, DeWalt, Vizio, Bushnell...) are found in a line as before.

## What to check
1. Regression: re-upload two receipts (THE HOME DEPOT with Milwaukee/DeWalt lines; Walmart with Vizio): same brands bound as in Push 81.
2. The Target Practice Supplies receipt: the item line "Bushnell ..." still binds Bushnell; the store still goes to the picker as in Push 76. No "Target" brand is bound from the shop name.
3. If you have or can make a receipt line such as "Echo Dot (4th Gen) Smart speaker" or "Smith & Wesson M&P Shield" or "K2 ski bindings": the item shows no Echo/Smith/K2 brand (and none of that brand's category) until the brand is typed or picked.
Apple is deliberately NOT restricted for now (it would add questions on every Apple receipt).
