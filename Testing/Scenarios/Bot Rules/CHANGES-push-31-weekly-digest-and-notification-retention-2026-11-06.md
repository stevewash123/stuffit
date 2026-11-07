# What changed in push 31: a weekly digest, and cleaning out old notifications (2026-11-06)

For GrokBot. API `529fc86` and UI `4f14856`. Check `/api/version` (`commit` must be `529fc86`); the UI proof is the **"In my weekly digest"** choice in Settings > Notifications. No migration (the settings table already had a weekly mode). No reference seed change. Stories S4.2.1, S4.2.3, S4.2.4, S4.4.2, S4.5.8.

## New: the weekly digest (S4.2.1, S4.2.3, S4.4.2)
- **Settings > Notifications:** each message type now offers **At once / In my daily digest / In my weekly digest**. Choosing weekly shows a **weekday** picker. There is **one weekday per person**: choosing a day on any weekly type sets it for all that person's weekly types (default Monday).
- **A new message type "Weekly digest"** (Summaries) with its own Email and In-app toggles, on by default, like the daily digest. Switch it off and no weekly digest is sent.
- **The job:** the same hourly digest job (`send-daily-digests`) now also sends, on the person's chosen weekday and from their own digest time (their own time zone), **one weekly email** listing everything held for weekly types. Their daily digest still goes every day for their daily types. A type is in one digest only, set by its current mode.
- **Once per week:** a second run the same local week sends nothing. A week is Monday to Sunday in the person's local calendar. If the chosen day passes with the job not running there is **no catch-up**: it waits for next week.
- **Nothing held, nothing sent.** Held notices older than 14 days are let go (not listed). More than three of one type become one line ("5 warranties are ending") as in the daily digest. **Urgent and important notices still bypass the digest** and are sent at once.
- The run summary says "(N weekly)" when weekly digests were sent.

## New: old notifications are cleaned out (S4.5.8)
The nightly retention job (`receipt-retention`, also `POST /api/maintenance/run-retention`) now also removes old notifications for everyone:
- **Read (or deleted-by-you) notifications** after **90 days** from when they were read or deleted.
- **Unread or important** ones after **365 days** from creation.
- **Never removed:** anything still waiting for your answer (Pending action); anything whose email is still **held for a digest**; a required system alert you have not deleted yourself; **digest notifications are kept at least 30 days** whatever the settings (they stop a second digest being sent for the same day or week).
- The retention run reports how many notifications were purged (`NotificationsPurged`). Settings: `Notifications:Retention:ReadDays` (90), `Notifications:Retention:KeptDays` (365).

## Steps to run
1. Test1 > Settings > Notifications: set **Warranty ending soon** (or another type) to **In my weekly digest**, pick **Friday**. Reload: the choice and the day stay. Set a second type to weekly: it shares Friday.
2. Create two or three warranty-ending notices for Test1 for the weekly type (items with warranties ending soon). Nothing is emailed at once for that type (held).
3. Set the simulated clock to the Friday after Test1's digest time. Run the digest sweep (`run-digest`): **one weekly digest** email listing the held notices; the in-app notice "Weekly digest" appears. Run it again the same week: **none**. Run on a non-Friday: none.
4. Add more than three held notices of one type: the digest shows **one consolidated line** with a link.
5. A notice of that type with 3 or fewer days left (urgent) is sent **at once**, not held.
6. Switch the **Weekly digest** type's Email off for Test1: no weekly email next Friday (the in-app notice still appears if In-app is on).
7. Retention: with an old read notification (advance the clock more than 90 days, or use an old one), `run-retention` reports `NotificationsPurged` > 0 and the old read one is gone; an unread one, a pending-action one, a held one, and a recent digest are still there. **Reset the clock to offset 0.**

## Known / not built, do not report as new
- Real-time toasts (S4.5.7) are not built; the unread count still updates by polling.
- The pending-consolidation table for bursts (S4.2.4 second part) and the Error attention level (S9.2.11) are not built.
- Items listed under pushes 26 to 30 "Not changed".
