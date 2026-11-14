# Push 86: New Items coverage chips say which lines a quick add leaves for Add Details (S9.10.5)

UI only (API unchanged at bde7439). Fixes the gap behind the Push 85 Fail. The "Not added by a quick add" sentence under a New Item only ever appeared for plan and stated-warranty lines read from the receipt (it is that line's warning, as before Push 85); the chips for the store's return policy, the maker's warranty and the rest never said it. The Walmart/Best Buy fixtures have no doubtful stated line, so Push 85 showed nothing to flag. Now every chip whose server decision is not `auto` carries "· left to you on Add Details".

## What to check (New Items)
1. Walmart / Vizio receipt: the Vizio warranty (Unconfirmed) chip and the Walmart electronics return chip (window ended) end with "· left to you on Add Details". The Walmart general window and the Allstate plan, which quick add attaches, have no such suffix.
2. Best Buy / Geek Squad receipt: LG warranty and the Geek Squad plan (attached) have no suffix; the ended Best Buy return chip does.
3. Quick add still attaches exactly the lines without the suffix (as Push 84/85 check 3).
4. The receipt-line sentence ("Not added by a quick add: ...") is unchanged.

## Answers to the Push 85 report
- Highly Likely shown in amber on a sure line: that is the certainty word's own colour (only Confirmed is green), unchanged, left as is.
- Save needing a category while the unknown-category ticks are correct: held for a design decision (see the summary to Steve), not changed here.
