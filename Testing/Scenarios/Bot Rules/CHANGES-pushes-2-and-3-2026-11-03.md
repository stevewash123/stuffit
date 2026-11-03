# What changed in the last two pushes (2026-11-03)

For GrokBot. Push 2 is API `7ceedd8` / UI `80af0e1` (you retested it). Push 3 is API `f6e85d9` / UI `b86cd8b` (not retested yet). Check `/api/version` shows `f6e85d9` before you start, and record it in your report. Retest steps are in `RETEST-NEXT-BUILD.md`.

## Push 3 (new, please retest)
| Change | What you should see | Your step |
|---|---|---|
| Deleting the only item of a purchase now deletes the purchase | The receipt is gone from the export, and the same receipt can be uploaded again as new (no "already added to My Items") | A-20 |
| "Start a return" after a courtesy override | On an item whose coverage has all ended, after "Ask for a courtesy return anyway" is confirmed, Start a return comes back with Refund and Mark returned | B-13 |
| A warranty the receipt printed is titled "Stated on receipt" | Pellet stove "10 YR LIMITED WARRANTY" shows "Stated on receipt" on the item page, not "Manufacturer warranty" | A-17 |
| Recovered card spacing | "$50.00 on 1 item" | D-4 |
| Money-recovered save errors | A failed save shows the field's message (for example "That date is in the future."), not "One or more validation errors occurred." | D-9 |

Because of the delete change, the generator stated-warranty tick (A-20) can now be retested: delete the item, upload the receipt again, quick add, then tick the warranty on Add Details.

## Push 2 (you confirmed these; listed so you know they are intended)
- **Storage:** PDF and ZIP reads go through Cloudinary's signed API download first, with a logged fallback. PDF View and the export download now work.
- **Full Add keeps receipt coverage:** Add Details lists the receipt's plan (ticked) and stated warranty (unticked); a full Add attaches the ticked ones. An item whose only coverage is a stated warranty can be created. Save with nothing ticked shows "Tick at least one policy" (expected).
- **Per-item receipt coverage:** on a multi-item receipt each plan and warranty attaches to the item it was read for (by ticked keys, then model, then name). If no item is clearly the one, nothing is attached by guessing.
- **To-do reminders are their own notification type:** separate from "Info needed", with their own setting, unsubscribe label and digest entry. The email and bell entry name the item.
- **Soft-closed return windows:** when every return window has ended, the item shows a "Return window closed" badge and hides the refund actions. "Ask for a courtesy return anyway" (with a confirmation) brings them back for the visit. The wizard's courtesy ask links to it.
- **Small fixes:** bell count matches the Notifications page; wizard keeps answers across a reload; courtesy wording does not say "has passed" when no window exists; usual-window note only on unconfirmed policies; store field "is not selected yet" hint; profile time zone; Recovered card on first load; "Brands (makers)"; recoveries.csv.

## Decided, do not report
- The order total showing as the price on the headphones and dishwasher rows (story S2.4.15, later).
- "Tick at least one policy" on an empty Save.
- A plan is valid on its last day ("Ends today" is fine as is).
- Sign-up timing gaps.
- SKU: it is store-specific, so plans match on model number or name. Missing SKU match text is not a bug.

## Still open, do not report as new
No keep tick on the plan row; the Lowe's plan shows no company or "not in our list" note; an item with only ended return windows cannot be added from a receipt; no "Step 3 of 3" on the wizard results; unticking a plan on Add Details does not persist across a reload; the run-reminders summary reports Sent=0; the unsubscribe page groups To-do reminders under "Purchases"; the money-recovered modal's backdrop blocks the account menu after a failed save; an item opened after a test-clock advance can show stale data until reload; no "Is yours one of these?" card prompt, over-limit insurance note, or days-left badge on return rows.
