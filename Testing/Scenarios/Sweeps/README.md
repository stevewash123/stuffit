# Sweeps: API-only tests of the scheduled jobs

Short scripts that need no screens: make some data, move the clock, run a sweep on demand, read the result back from the API. They check what a person cannot watch happen (a job ran once, did not repeat itself, left other accounts alone). The numbered scenarios in the folders above drive the app by hand; these do not, and they have no number.

## What you need
- The simulated clock and the maintenance key on the API service you test against: `Clock__Simulated=true` and `Maintenance__Key` (16+ characters), and `ASPNETCORE_ENVIRONMENT` not `Production`. Without them every trigger below answers 404. The key goes in header `X-Maintenance-Key`. Call them on the UI address, which forwards `/api`.
- A signed-in test account (the usual Alice or Bob after a scenario reset). Its **account id** is the `account_id` claim inside its access token; decode the token (a JWT) to read it.
- Run one script at a time. The clock is shared by everyone on that API, so another run moving it at the same time spoils both.

## The triggers
All are `POST /api/maintenance/<name>` with the key. `accountId` is optional on the first five: with it, only that account's data is touched. Always pass it. Two have no account and act on the whole database: use them only on the clone (WarrantyCat), never on a copy other people are testing.

| Trigger | Runs | `?accountId=` | Answer |
|---|---|---|---|
| `run-reminders` | due reminders become notifications and emails | yes | `ReminderSendSummary { Sent, Cancelled, Failed, Todos, CardReviews }` |
| `run-digest` | the daily digest | yes | counts: sent, failed, skipped |
| `run-retention` | receipt retention | yes | `RetentionRunSummary { NoticesSent, PurchasesCleared, FilesRemoved }` |
| `run-export-expiry` | data exports past their 7 days expire, their file is removed | yes | `Expired N export(s).` |
| `run-new-items` | works out waiting New Items | yes | `New Items processed.` |
| `run-email-retry` | retries emails that failed in the last 24 hours | **no** | `Retried N email(s).` |
| `run-signup-purge` | removes sign-ups nobody finished, past their time | **no** | `Removed N unfinished sign-up(s).` |

Clock: `GET clock`, `POST clock/advance?days=N` (forward only), `POST clock/reset`. Always reset at the end. Design and limits: `Stories/TESTING/T1-simulating-time.md`.

## Format
Each script has: **Setup** (calls that make the data), then a table of steps with the call and what it should return. A step is Pass or Fail on that answer alone. Note the clock offset you started at, and reset it at the end even if a step failed.

## Scripts and what covers each sweep
| Sweep | Where |
|---|---|
| Data export expiry | `export-expiry.md` |
| Reminder send, no repeat, one account only | `reminder-send.md` |
| Registration to-do closed as missed | Scenario 54, step 19 (opening the to-do list also closes it) |
| Daily digest | Scenario 39 |
| Return window ends, reminder arrives | Scenario 24 |
| Receipt retention, email retry, sign-up purge, New Items | not written yet |
