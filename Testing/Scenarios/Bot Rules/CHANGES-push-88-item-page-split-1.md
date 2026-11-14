> NEVER DEPLOYED: Push 88's production build failed on Render. It was replaced by Push 89 (4bd2d11), which carries this change plus the People split. See CHANGES-push-89-fix-build-and-people-split.md.

# Push 88: the item page's "Suggested coverage" is its own component (S9.10.10, step 1)

UI only (API unchanged at bde7439). A pure refactor: the "Suggested coverage. Tick what applies." block moved out of the 2,125-line item page into `CoverageSuggestionsComponent`. Nothing should look or behave differently; a visible difference is a bug. The item-page specs passed unchanged.

## What to check (item page, regression)
1. Edit an item that has suggestions (Policies card > Review): the "Suggested coverage" list looks the same as in Push 83/87 (heading, "Tick what applies.", each suggestion with its checkbox, kind, provider, category badge, dates, source line, certainty word with its hover text in words, parts of a warranty, notes, Source link).
2. The three buttons on each suggestion: Change it (opens the edit drawer with the suggestion's values), Doesn't apply, Not sure yet (the suggestion leaves the list).
3. Ticks: the sure lines start ticked, others unticked; an ended window unticked; "Verify the above N policies apply" shows the right count, is disabled with none ticked, and adds exactly the ticked coverage.
4. Layout: the block spans the page width and has the same spacing as before.
