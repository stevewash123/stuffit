# UAT retest: Push 91, "Replaced by the plan" drawer is its own component

- **Build tested:** API `bde7439` (/api/version, startedAt 2026-11-13 03:58 UTC); UI Last-Modified **Fri, 13 Nov 2026 12:53:03 UTC (7:53 AM ET)**, re-checked unchanged after the run (7:59 AM ET). A "new version is ready" banner showed early in setup; Reload was clicked and all checks ran on the 12:53:03 build.
- **Scope:** `CHANGES-push-91-replace-drawer-split.md`. Regression only (nothing should look or behave differently). Push 90 passed (4 Pass, 0 Fail, 3 Info). NEXT-REPORT-ADDITIONS.md: none.
- **Tester / account:** QA Controller, box browser, Alice ("P34-Alice Repairs"), 7:55–7:59 AM ET Nov 13 2026.
- **Test items:** "P91 UAT Replace Me" (Walmart/Vizio fixture `push85/30-thermal-walmart-vizio-tv-protection.pdf`, Electronics, Vizio V505-J09, $328.00) with an Allstate Protection Plans warranty extension typed in (Aug 29 2026 – Aug 28 2028). Replacement "P91 UAT Replacement". Both deleted afterwards. No new fixtures.

## Results

| # | Check | Result |
|---|---|---|
| 1 | Drawer opens with the sentence and prefilled fields | **Pass** |
| 2 | Plan question; Make the replacement disabled until answered, and while Name or date is empty | **Fail** (empty Name does not disable it) |
| 3 | Save creates the replacement and marks the old item replaced; failed save shows red message | **Pass** (1 Low) |
| 4 | Drawer layout | **Pass** |

**3 Pass, 1 Fail, 1 Low, 1 Info.**

### 1. Drawer
"Replaced by the plan" button appears in the item header once a plan exists. Title "Replaced by the plan"; sentence "This makes the replacement as a new item. P91 UAT Replace Me is marked replaced and kept here with its history and files." Name prefilled "P91 UAT Replace Me"; Brand picker prefilled "Vizio" (with ×); Model prefilled "V505-J09"; Serial number empty (item had none); Replaced on 2026-11-13 (today). Button "Make the replacement". Shot `01-drawer-open.png`.

### 2. Plan question and disabled states
"What should Warranty extension do?" / "Allstate Protection Plans · Aug 29, 2026 to Aug 28, 2028". Options: Carry on with the replacement (shows "The plan's dates have changed" checkbox), End the plan (Ends the plan on Nov 13, 2026), Start a new term from Nov 13, 2026. Button disabled until answered, then enabled. Empty Replaced on: disabled (option texts switch to "today"). 

**Fail (Medium):** with the plan answered and **Name cleared, "Make the replacement" is NOT disabled** (it looks pale but is clickable). The note expects it disabled while Name is empty. Saving with no name was not tried. Shot `02-name-cleared.png`. Repro: item with a plan > Replaced by the plan > answer the plan question > clear Name.

### 3. Save and failed save
- Replaced on 2027-06-01 > Make the replacement: red message in the drawer "The replacement date cannot be in the future."; nothing saved, drawer stayed open. Shot `04-future-date-error.png`.
- **Low:** after fixing the date back to today, that red message stayed visible until the next successful save. Shot `05-before-real-save.png`.
- Real save (Name "P91 UAT Replacement", Model P91-M, Serial P91-S, today, "Carry on with the replacement"): new item "P91 UAT Replacement", Active, Bought Nov 13 2026, Vizio / Electronics / P91-M / 50IN / P91-S, notes "Replaced P91 UAT Replace Me on 2026-11-13." and "Replacement for P91 UAT Replace Me, under its protection plan.", Allstate plan moved to it (Aug 29 2026 – Aug 28 2028). Banner "P91 UAT Replace Me is marked replaced by P91 UAT Replacement. Warranty extension: carries on with the replacement." (Undo, Dismiss). Old item: status Replaced, "Replaced by P91 UAT Replacement. This item is kept here with its history and files.", header Edit and "I have it again", Policies "Not set up yet"; the plan's "Add the rest of your Allstate…" to-do stayed on the old item. Shots `06-new-item-after-save.png`, `07-old-item-replaced.png`.

### 4. Layout
Normal in all states: fields aligned, error box above the full-width button, no overlap.

## Info
- **Info (not this push):** in the site header the "WarrantyCat" logo overlaps the "P34-Alice…" account label in every screenshot.
- **Info:** after the plan carried on to the replacement, its "Add the rest of your Allstate Protection Plans plan" to-do stayed on the old (replaced) item.

## Cleanup
"P91 UAT Replacement" (Cancel the plan) and "P91 UAT Replace Me" deleted; My Items search "P91" shows "No items match." Shot `08-cleanup-search-P91.png`.

Screenshots: `/workspace/uat/push91/shots/`.
