# What changed in push 14: Stripe scenarios (2026-11-04)

For GrokBot. No app change in this push: it adds two browser plans for what push 13 built (Plan & billing, Manage membership) and the free-year license behind it. No migration.

## New scenarios
| # | Folder | What it checks |
|---|---|---|
| 58 | Scenario 58 - Free year license from sign-up | A **new account made through the normal sign-up form** gets its free year: the Plan & billing line, an end date about a year ahead that does not move on reload, the greyed-out Monthly and Yearly options, a second new account, and Alice and Bob |
| 59 | Scenario 59 - Manage membership in Stripe | Manage membership opens Stripe's own page; Return and the browser Back button both land back in the app; cancelling in Stripe leaves the license line as it was; keeping the plan; the message for accounts with no Stripe customer; signed-out access; no account sees another's details |

## Read this before you start
- Both need an account **registered through the normal sign-up form** with a fresh plus-address (for example `stevewash123.test+stripe1@gmail.com`). DB Stager accounts (Alice, Bob) have no Stripe customer and are used only for the "not set up yet" rows.
- Stripe must be switched on for staging. If Manage membership says "Managing your membership is not switched on yet.", Stripe is off: grade the rows that need it **Not checked** and say why. That is not a bug.
- The license can take a few minutes to appear after sign-up. Reload up to three times, two minutes apart, before reporting it missing.
- The Stripe page itself (layout, wording, plans listed) is Stripe's. Record what it shows as information; grade only that it opens, shows the right account, and that Return and Back work.

## Decided, do not report
- Monthly and Yearly are placeholders and cannot be chosen; buying is not built.
- No Founders option yet.
- The trial ending, past-due and ended statuses are not in these scenarios; they need Stripe test clocks and are checked outside the bot.
- Cancelling in Stripe does not end the license early: the line keeps its end date.
