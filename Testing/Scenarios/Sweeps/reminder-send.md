# Sweep: reminders are sent once, and only for the account asked

**Needs:** the simulated clock and key. **Accounts:** Alice and Bob (both after a scenario reset). **Time:** 10 min.

## Setup
1. Read each account id from the `account_id` claim of their access token: `A` (Alice), `B` (Bob).
2. As each, add a purchase with a warranty that ends 25 days from today (the reminder goes out 7 days before the end, so the clock is advanced 18 days below) (any seeded store; set the warranty end by hand if the document has none). Email on for warranty reminders in notification preferences.
3. `GET /api/maintenance/clock` and note the offset.

## Steps
| # | Call | Expected |
|---|---|---|
| 1 | `POST /api/maintenance/clock/advance?days=18` | clock moved (the warranty now ends in 7 days; the app sends the warranty-ending reminder 7 days before the end date) |
| 2 | `POST /api/maintenance/run-reminders?accountId=A` | `Failed = 0`, and `Sent` is 1 or more |
| 3 | Alice: `GET /api/notifications` | a warranty-ending reminder for the item, unread |
| 4 | Bob: `GET /api/notifications` | **no** reminder for his item: Bob was not run |
| 5 | `POST /api/maintenance/run-reminders?accountId=A` again, same day | `Sent = 0`: a reminder already sent is not sent again |
| 6 | Alice: `GET /api/notifications` | still one reminder for the item, not two |
| 7 | `POST /api/maintenance/run-reminders?accountId=B` | `Failed = 0`, `Sent` 1 or more |
| 8 | Bob: `GET /api/notifications` | his reminder is there now |
| 9 | `POST /api/maintenance/clock/reset` | offset back to 0 |

If step 2 sends nothing, check Alice's time zone and send time in her notification preferences first: the job sends at each person's own local time and looks a day ahead for people east of UTC. That is a setup problem, not a sweep Fail, so report it as Blocked with the zone.
