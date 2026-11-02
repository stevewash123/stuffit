# Scenario 24: Time travel: a return window ends and the reminder arrives

**Status:** DRAFT. Needs the simulated clock; untested live.

**Accounts:** Alice
**Preconditions:** The app runs with `Clock:Simulated=true` and a `Maintenance:Key`, on a UAT database. Alice exists. Reminder emails go to the test mailbox. The bot has the maintenance key from `RUN-CONFIG.md` and can send HTTP requests (or a human does the clock steps).
**Time:** 20 min

Clock steps call the maintenance API with header `X-Maintenance-Key`. See `Stories/TESTING/T1-simulating-time.md`.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Alice | Add a purchase from a seeded store with a 30-day return window, dated today | Return window shows an end date 30 days out |
| 2 | Alice | Notification preferences: email on for return and warranty reminders | Saved |
| 3 | (clock) | `GET /api/maintenance/clock` | Offset 0 days |
| 4 | (clock) | `POST /api/maintenance/clock/advance?days=20` then `POST /api/maintenance/run-reminders` | Run summary lists a reminder for Alice's return window (about 10 days left, or the lead time the app uses) |
| 5 | Alice | Check the mailbox | Reminder email arrived; names the item and the correct end date; links open the item |
| 6 | Alice | Open the bell/notification center | Same reminder is there, unread; open it, then it is marked read |
| 7 | (clock) | `POST /api/maintenance/run-reminders` again (same simulated day) | No duplicate reminder |
| 8 | (clock) | `POST /api/maintenance/clock/advance?days=11` (31 days after purchase), run reminders | The window is shown as ended; no "act now" reminder is sent for a window that has ended |
| 9 | Alice | Open the item | Return coverage shows as ended/expired; warranty (if any) still active |
| 10 | (clock) | `POST /api/maintenance/clock/reset` | Offset back to 0 |

Also note anything that still shows real-world dates after a clock jump (a screen that ignored the simulated date). Browser-side dates, sign-in sessions and the refresh cookie use the real clock by design.
