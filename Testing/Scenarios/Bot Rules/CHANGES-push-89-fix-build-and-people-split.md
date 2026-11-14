# Push 89: replaces Push 88 (never deployed) and splits People out of the item page (S9.10.10, steps 1 and 2)

**Replaces Push 88 (f4dc531), which never went live.** Its production build failed, so the site stayed on the Push 87 build (5:16 AM ET). Nothing from Push 88 was ever served. Push 89 (4bd2d11, live 6:57 AM ET Nov 13) is the fix plus the next step of the same change, so this one note covers both: the build that carries them is the one to test and to name in the report.

UI only (API unchanged at bde7439). Push 88 (f4dc531, "Suggested coverage is its own component") failed the production build because the page's `picks` member was `private` and a template cannot read a private member; the site stayed on the 5:16 AM ET build (Push 87). Fixed (`picks` is now `protected`) and checked with a full production build before pushing. This push also carries the next step of the same split: the People section is now `ItemPeopleComponent`. So Push 88 never reached the site; please test the item page now as the first time with both pieces.

## What to check (item page, regression: nothing should look or behave differently)
1. Edit an item that has suggestions: the "Suggested coverage. Tick what applies." list is as in Push 83/87 (ticks, certainty words and their hover text, category badge, dates, Source link, warranty parts), and its Change it / Doesn't apply / Not sure yet buttons and "Verify the above N policies apply" work.
2. A household with more than one member: the "People" card lists everyone, marks the Owner and "(you)", "Make owner" shows only to the owner, "Remove"/"Take me off" work, and "Add a person" (the picker and the Add button, disabled until someone is chosen) adds them and clears the choice.
3. Layout and spacing of both blocks unchanged.
