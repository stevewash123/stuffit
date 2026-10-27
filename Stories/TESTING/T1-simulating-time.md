# T1 Simulating the passing of time (testing playbook)

**Type:** Testing playbook, not a product feature. Open this before testing anything that depends on the date.  
**Phase:** v2 (use whenever a date-driven behaviour needs checking)  
**Decision (2026-10-18):** there is no system-wide clock or "Time Machine". The API has about 94 direct clock reads in 39 files; converting them was judged too much churn for a nice-to-have. Time is simulated by moving the data and by running jobs "as of" a day. If a real date bug needs more, put a clock into that one code path, not everywhere.

## When to use this
Anything that depends on today's date: return windows closing, warranties ending (30 and 60 day tiles), reminders and their emails, the todo "due in 30 days" rule, an estimated delivery date arriving, trial and billing dates, the daily AI spend cap.

## The techniques, in the order to try them

### 1. Seed items that are already old (cheapest)
`--seed-demo you@example.com` creates a demo account's items relative to today: bought 12, 20, 50, 140 and 400 days ago, one with a return started, one returned, registration deadlines 18 days ahead and 50 days past. Every dashboard tile has something. Run it on a throwaway account.

### 2. Run a time-driven job as of a day
`dotnet run --project src/StuffIt.Api -- --send-reminders --as-of 2027-09-01` runs the daily reminder send as if it were that day (noon UTC). Development only; it refuses to run elsewhere. It uses the real data and **really sends** what is due (email and in-app notification), so use it on a test account.

### 3. Pass the date in, in a test
Where code takes an explicit "as of" date (for example the coverage rules take the day), a test can pass any date. Where a test needs "today", build the data relative to today (`today.AddDays(-30)`), never a fixed calendar date, so the test does not rot.

### 4. Age an existing account (not built yet)
A `--shift-dates <account> <days>` command that moves every date on an account back by N days is the next step, if 1 to 3 are not enough. It must move all of these together or the data is inconsistent: purchase date and its latest, delivery date, coverage start / end / latest end / labor end, return started / returned, reminder dates, check-on dates, todo due / remind-from / snoozed-until, plan and policy start / end. Moving only some of them is the usual way to get a confusing result.

## What time simulation does not reach (known from the code; not all hit yet)
- **Postgres `now()` defaults, Hangfire's schedule and JWT expiry use the real clock.** To trigger a job, run it from the command line, do not wait for Hangfire. Token expiry cannot be tested this way.
- **Reminders are rows made in advance.** Each reminder has its own `RemindOn` date, set when the coverage was created. Changing a purchase date later does not move them; they have to be rebuilt (`--backfill-reminders`) or shifted with the rest.
- **A reminder that has been sent is not sent again.** Re-running the same day finds nothing. To repeat a test, reset the reminder to pending or use a fresh item.
- **The send respects each person's time zone and send time.** "As of noon UTC" is not the same day everywhere; the job also looks one day ahead for people east of UTC. If a reminder does not appear, check the person's zone first.
- **The AI daily cost cap counts the real day.** A job run "as of" another day still spends against today's cap.
- **The browser has its own clock.** The UI uses `new Date()` for "today" (the date field, the todo 30-day cutoff, "days left" wording). The API can be moved to 2027 and the phone will still say 2026. Check what the UI computes itself before trusting a screen.
- **The dev database is the shared one.** The deployed app on Render reads the same data. Aged or emailed test data shows up there too, and a mailed reminder is a real email.
- **Do not change the PC or server clock.** It breaks token checks, the database's TLS and Hangfire all at once, and the symptoms point nowhere useful.

## Procedure
1. Use a throwaway account (the test account), never one with data you care about.
2. Pick the technique above that needs the least. Write down the date you are simulating and what you expect to see before you run anything.
3. Run it. Check the in-app result and the email, and the dashboard tiles.
4. Clean up: `--clear-new-items` for New Items, `--clear-items` for everything on the account, and remove any aged data you added.
5. Add anything surprising to the log below.

## Lessons learned (add to this as snags are hit)
| Date | What we did | What went wrong | Fix or workaround |
|------|-------------|-----------------|-------------------|
| | | | |

## Status
- Built 2026-10-18: `--send-reminders --as-of yyyy-MM-dd` (development only), a stopped-clock `FixedTimeProvider` used only by that command. Checked: it builds and rejects a bad date. Not yet run end to end, because it sends real mail.
- Existing: `--seed-demo`, `--seed-new-items`, `--backfill-reminders`, `--send-reminders`, `--clear-items`, `--clear-new-items`.
- Not built: `--shift-dates`; a dev-only way to tell the UI what "today" is.
