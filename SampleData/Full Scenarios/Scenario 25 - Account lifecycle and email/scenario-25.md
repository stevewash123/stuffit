# Scenario 25: Create two accounts, confirm by email, sign in, recover a password

**Accounts:** Test1 = stevewash123.test@gmail.com, Test2 = stevewash123.tester2@gmail.com (the bot reads both inboxes)
**Preconditions:** Neither address has a StuffIt account yet. If one does, say so, and use "forgot password" in step 14 to continue. The bot may open each Gmail inbox in its own browser context.
**Time:** 25 min
**Why this plan:** accounts, email confirmation and password reset are built and tested, and they need a real inbox, which only the bot can supply.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | (none) | Open the site's address while signed out | Redirects to the sign-in page. Note the browser tab title (app name) |
| 2 | (none) | Open `/terms`, `/privacy` and `/disclaimer` without signing in | Each loads readable legal text; no sign-in wall |
| 3 | Test1 | Go to Create account. Submit with an empty form | Clear per-field messages; nothing is created |
| 4 | Test1 | Submit with a too-short password, and separately with an invalid email like `abc` | Specific refusals, no stack traces or raw JSON shown |
| 5 | Test1 | Create the account with the Test1 address and a valid password; accept the terms/privacy consent if asked | Moves to a "check your email" or confirm-email state (or straight in, if confirmation is off). Record exactly what the screen says |
| 6 | Test1 | Open the Test1 inbox | A confirmation email arrived within a few minutes. Record sender name, subject, and whether the link points at the right site |
| 7 | Test1 | Click the confirmation link | Account confirmed; lands in the app or on sign-in with a clear message. Clicking the same link a second time gives a sensible "already used/expired" message, not an error page |
| 8 | Test1 | Sign out, then press the browser Back button | Signed-out screen. No account data is visible |
| 9 | Test1 | Sign in with the right email and a wrong password | One generic failure message that does not say whether the email exists |
| 10 | Test1 | Sign in correctly | Lands in the app. Navigation shows Home, My Items, New Items, Returns, Notifications |
| 11 | Test2 | In a second browser context, create the Test2 account the same way and confirm it by email (steps 5 to 7 for the Test2 address) | Works the same; the Test2 inbox received its own mail |
| 12 | Test2 | Try to sign up again with the Test1 address | Refused or handled without revealing more than necessary; no second account, no error page |
| 13 | Test1 | Sign out. On sign-in choose Forgot password; enter the Test1 address | A neutral message ("if an account exists, we sent an email") |
| 14 | Test1 | Open the Test1 inbox, follow the reset link **in the newest message** (Gmail groups repeats of the same subject into one thread and collapses them; expand the thread and use the last message, not an earlier one), set a new password, sign in with it | Reset email arrived; the new password works; the old one is refused |
| 15 | Test1 | Reuse the reset link a second time | Refused with a clear message |
| 16 | Test2 | Request a reset for an address with no account (`nobody.uat@example.com`) | The same neutral message as step 13; no email, no hint the account is missing |
| 17 | Test1 (Alice) | Wait at least ten minutes after the step 13 request, so the first message below is not itself a repeat. Then request a password reset for the Test1 address twice, within ten minutes (Forgot password, enter the address, send; then again). Open the Test1 inbox and look at the thread with the subject "Reset your WarrantyBank password" | Gmail groups the two messages into one thread. The first message has no "Requested at" line. The newest message says "Requested at <time>. If you asked more than once, use the newest email." (time in the person's time zone, or UTC if none is set). The link in the NEWEST message works. The link in the older message may no longer work: record what it does |

Write the new Test1 password in `RUN-CONFIG.md`, not in the report.
