# UAT retest: Push 98, a negative refund is refused in words

- **Date:** Fri Nov 13, 2026, 1:48 to 1:54 PM ET
- **Build tested:** API `bde7439` (startedAt 2026-11-13 03:58 UTC, unchanged) and UI Last-Modified Fri, 13 Nov 2026 18:38:54 UTC (1:38 PM ET)
- **Notes:** `Bot Rules\CHANGES-push-98-negative-refund-in-words.md` (1:38:19 PM ET). The UI is newer than the notes, so the build matches.
- **Account:** Alice ("P34-Alice Repairs")
- **Scope:** item page > Mark as returned only, as the notes list. No wider regression was run.

## Result: 2 Pass, 0 Fail (every sub-check passed)

| # | Check | Result |
|---|---|---|
| 1 | Refund -50 then Mark returned: the drawer shows the red message, nothing is sent, nothing is saved; changing to a valid number or empty clears it; saving works as before | **Pass** |
| 2 | Zero and empty refunds, and the rest of the drawer, behave as before | **Pass** |

### Check 1 detail
- With -50, the drawer showed exactly: "The refund can't be less than zero. Leave it empty if the money has not come back yet." (shot 03, 18:50:08 UTC)
- **Network:** the Playwright request listener (all xhr/fetch and any non-GET) saw no request on the -50 click. A valid save sends `PUT /api/items/<id>/return`. The item stayed "Needs info", not Returned.
- The Mark returned button stays enabled (disabled=false), so the check happens on click.
- Changing the amount to 100 removed the message straight away, before any click.
- Clearing the field with real keys (Ctrl+A, Backspace, then blur) removed the message; the DOM count of the error text was 0 (shot 07, 18:53:04 UTC).
  - The first pass cleared the field with Playwright `fill('')` and no blur, and the message stayed. The re-check with real keystrokes shows that was a test artifact, not an app fault.
- Saving with 100 and "Back to the original payment" sent one PUT. Card: "Returned Nov 13, 2026 — Refund $100.00 · Back to the original payment" (shot 04).

### Check 2 detail
- **Refund 0:** saved with no error. Card: "Returned Nov 13, 2026 — Refund $0.00" (shot 05).
- **Empty refund:** saved twice (Item C, and Item D after the cleared-error re-check). Card: "Refund — Not paid yet".
- **Drawer unchanged:**
  - Date returned.
  - Refund amount, with the hint "Leave empty if the money has not come back yet."
  - Paid back by: Not sure / not yet, Back to the original payment, Store credit, Gift card, Exchange, Cash, Check, Other.
  - How hard was it? 1–5 ("1 is easy, 5 is very hard.").
  - Problems getting paid.
  - Mark returned.
- Edit return reopened with the 100 refund still in place.

## Notes
- **Version banner:** at setup the "A new version of WarrantyCat is ready" banner appeared (shot 01). The next full navigation loaded the new bundle, and the banner never came back. The re-check started from a hard reload with no banner.
- **Order number:** the sample PDF's order number (04417) was refused for a second item ("You already have a purchase from this store with that order number."). This is the expected duplicate guard, so Order number was cleared for Items B through D.

## Fixtures and cleanup
- **Fixtures:** no new fixtures. Used the existing `push85/30-thermal-walmart-vizio-tv-protection.pdf`.
- **Cleanup:** P98 UAT Items A through D were deleted, and a My Items "P98" search shows "No items match." (shot 06).

Screenshots are in the box folder `/workspace/uat/push98/shots/` (01 through 07).
