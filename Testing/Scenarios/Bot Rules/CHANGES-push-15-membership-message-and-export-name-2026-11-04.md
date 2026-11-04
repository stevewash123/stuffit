# What changed in push 15: Manage membership message, export file name (2026-11-04)

For GrokBot. API and UI commits are named in the push message; check `/api/version` and record it. No migration.

## Fixed
| Was reported | Now |
|---|---|
| Manage membership, no Stripe customer or Stripe off: the red message read "One or more validation errors occurred." | The red message is the plain sentence: "Your membership is not set up yet. Please try again in a few minutes." (or "Managing your membership is not switched on yet." when Stripe is off for the site) |
| The data export ZIP was named `stuffit-export-<date>.zip` | It is named `warrantycat-export-<date>.zip` |

## Not fixed here (configuration, not code)
- **No license on any account (Scenarios 58 and 59).** Staging is not creating the free-year trial at sign-up, so Plan & billing keeps saying "Your membership is being set up". Steve is correcting the staging Stripe settings. Until that is done, grade the rows that need a license **Not checked**; do not retest 58 and 59 until a later note says Stripe is on.
- The email sender name "StuffIt" is a setting in the Render dashboard (Steve).

## Decided, do not report
- Monthly and Yearly are placeholders; no Founders option yet.
- The 20-second wait at "Signing in..." for Ops is noted; not being chased now.
