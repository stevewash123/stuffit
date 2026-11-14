# UAT retest: push 78 (UI-only), ended return window not pre-ticked

- **Build:** UI Last-Modified Thu 12 Nov 2026 19:42:33 UTC (2:42:33 PM ET Nov 12 2026); API unchanged at `29c6fda` (started 11:25:54 AM ET).
- **Run:** 3:00 to 3:02 PM ET, as Alice, after a hard reload (no "new version" banner). App clock not moved (offset 0). One test item saved and deleted.
- **Scope:** CHANGES-push-78-ended-window-not-ticked.md (Bot Rules; fix for the push 77 Low: ended window pre-ticked). NEXT-REPORT-ADDITIONS.md: none.
- **How I checked:** one test item saved from the Walmart/Vizio fixture on `/add/new` with all coverage unticked, then the item page suggestions list and a hand-tick of the ended window. Deleted in the app. No DB Stager cleanup.

## Summary: 2 Pass, 0 Fail; push 77 Low fixed

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Ended electronics window is not pre-ticked on the item page | **Pass** | Alice saved **"P78 ended window test TV"** at 3:00 PM from the Walmart/Vizio fixture (category TVs, all coverage unticked). On the Add form the electronics line was greyed: **"This return window ended 2026-09-28, so it cannot be added."** Item page Policies card **"Not set up yet · 2 suggested policies to review"** → Review, list of 3, all unticked: Return window · Walmart [ELECTRONICS] Aug 29–Sep 28, 2026 (Confirmed) **not ticked**; Return window · Walmart general Aug 29–Nov 27, 2026 (Likely) unticked; Manufacturer warranty · Vizio [TVS] Aug 29, 2026–Aug 29, 2027 (Unconfirmed) unticked. The open window and the warranty are the same as in push 77, apart from the fix (in push 77 they were also unticked; only the ended one was ticked). No card benefit lines (Alice has no card). **"Verify the above policies apply"** stayed disabled while nothing was ticked. Shot `p78-01-suggestions.png`. The card count of 2 vs a list of 3 is by design per the notes (alternate return windows are not counted). |
| 2 | Ended window can still be ticked by hand and added | **Pass** | Hand-ticking the ended electronics line at 3:01 PM worked with no warning or message; the button became **"Verify the above policy applies"**. Shot `p78-02-hand-ticked.png`. Verify added **"Return window · Walmart ELECTRONICS, Ended Sep 28, 2026"** to Your coverage. The item status became **Expired**, with a **"Return window closed"** banner ("The return window ended on Sep 28, 2026. A store may still accept a courtesy return, but it is a request, not a right."). The Policies card then read **"Coverage ended · 1 policy / 1 suggested policy to review"**. Shot `p78-03-after-save.png`. |

## Notes
- **Low:** after the ended electronics window was added by hand, the still-open Walmart general 90-day alternate window disappeared from the suggestions (only the Vizio warranty was left), so the user cannot then pick the open window; and the item became Expired.
- **Info:** the item page lets you add an ended window with no warning, while the Add form refuses it. That is allowed by design per the notes ("you can still tick it by hand").

## Cleanup
The test item was deleted in the app at 3:02 PM (Edit → Delete → "Delete item") and was gone from My Items. New Items Waiting and Dismissed were empty. No DB Stager cleanup was needed.

## Fixtures
No new fixtures this run. Used `30-thermal-walmart-vizio-tv-protection.pdf` (B).
