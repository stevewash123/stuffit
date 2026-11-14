# UAT retest: Push 94, the "Edit item" drawer is its own component

- **Build tested:** API `bde7439`; UI Last-Modified **Fri, 13 Nov 2026 15:38:26 UTC (10:38 AM ET)**, confirmed before and after the run.
  - A "new version" banner was showing on the already-open tab. The page was reloaded and the drawer reopened before testing. The banner did not come back.
- **Scope:** `CHANGES-push-94-item-edit-drawer-split.md` (S9.10.10 step 6, regression only). No new scenarios and no NEXT-REPORT-ADDITIONS.md.
- **Tester / accounts:** QA Controller, box browser, 11:08–11:13 AM ET, Nov 13 2026.
  - Alice ("P34-Alice Repairs", business) and Bob ("QA Test 2 / Personal").
  - Save state was read from the real disabled property.
- **Test items:** "P94 UAT Item" (Alice) and "P94 Bob Item" (Bob), both made from the Walmart/Vizio fixture `push85/30-thermal-walmart-vizio-tv-protection.pdf`, Electronics. Both were deleted. No new fixtures.

## Results

| # | Check | Result |
|---|---|---|
| 1 | Pencil by the name opens Edit item with all fields | **Pass** |
| 2 | Business shows Asset tag and Location (with saved locations); personal shows neither | **Pass** |
| 3 | Save disabled with empty name; failed save shows red message; good save updates header, category, coverage | **Pass** |
| 4 | Drawer layout unchanged | **Pass** |

**4 Pass, 0 Fail, 3 Info.**

### 1. Fields (Alice)
The fields run in this order (shot 01):
- Item.
- Brand (maker): a picker prefilled "Vizio", with a clear ×.
- Category: Electronics is selected; the options start "Not sure, Accessories, Air conditioning and heat pumps, Apparel, Audio…" and end "…Windows and doors, Winter sports".
- Model V505-J09.
- Size or variant 50IN.
- Serial number (empty).
- Asset tag.
- Location.
- Price 328.
- Status: Still have it / Returned / Gone / thrown out.
- Notes.
- Save.

### 2. Business vs personal
- **Alice:** has both Asset tag and Location. The Location field offers the saved locations Van 1, Van 2 and Warehouse; this was confirmed from the field's suggestion list in the page structure, not from a dropdown seen on screen.
- **Bob:** his drawer shows Item, Brand (maker), Category, Model, Size or variant, Serial number, Price, Status and Notes, with no Asset tag or Location (shot 04).

### 3. Save and errors
- **Save `disabled`:** true with Item cleared, and false after the name was typed back.
- **Failed save (Price -50):** the red message "One or more validation errors occurred." appeared in the drawer, and the same text appeared in a red box at the top of the item page (shot 02).
- **Good save:** the item was renamed "P94 UAT Item Edited", with Model P94-M, Serial P94SN1, Price 350, Notes "P94 note", Asset tag P94-TAG-1, Location "P94 Shelf A", and the category changed. Afterwards (shot 03):
  - The header shows the new name and the category shows "Major appliances".
  - All the details are shown.
  - Coverage was recalculated for the new category: the Walmart Electronics and Smartphones windows (Aug 29–Sep 28) were replaced by the Walmart general window (Aug 29–Nov 27, "General policy; none for this category.").
  - The Vizio warranty now shows the warning "Different category: this is Vizio's policy for tvs; this item is major appliances."

### 4. Layout
The order is as listed above, nothing overlaps, and the styling is normal.

## Info (not regressions)
- **Info:** a negative Price gives the generic text "One or more validation errors occurred." This is the same as the Push 93 total and the Push 90/92 RefundAmount message.
- **Info:** the drawer's Category list includes "Vehicles", but the /add/new list doesn't. This is probably deliberate, but worth a look.
- **Info (as Push 91):** the header's WarrantyCat logo runs slightly into the account label.

## Cleanup
- Both items were deleted. A plain "Delete this item?" appeared, with no plan prompt.
- A My Items search for "P94" shows "No items match." for both Alice and Bob (shot 05).
- The run finished signed in as Alice.

Screenshots: `/workspace/uat/push94/shots/` (01–05).
