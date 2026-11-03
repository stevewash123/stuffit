# Bot rules for the browser test plans

The browser test plans are Scenarios 22 to 28 in the parent folder (Scenarios). A bot (Grok) follows them as a real user: browser plus a test mailbox. Deterministic checks stay in the API/UI test suites; the plans are for what needs a browser, an inbox, or more than one person. This folder holds the rules for the bot and the report format (`_template.md`).

## Before a run
- **Reachable URL.** The bot cannot see localhost. It needs the deployed UI (Render) or a tunnel. Put the URL in `RUN-CONFIG.md` (not committed with secrets).
- **Data.** There is no production yet, so UAT runs against the dev database (`stuffit`, shared by local dev and Render). It holds test data only. Before this changes (real users), move UAT to its own Render services and Neon database.
- **Data staging.** A separate data-staging bot resets the accounts and creates starting fixtures so this bot does not rebuild them: see `DATA-STAGING.md` (run reset: drop and recreate the four personas once per run; scenario reset: wipe their data, keep the logins, before each plan; what each plan expects). When a plan's precondition says an account or item "exists", it will already be there; if it is not, stop and report it instead of building it.
- **Clean start.** `dotnet run --project src/StuffIt.Api -- --remove-test-accounts` (add `--confirm` to delete) removes every non-administrator account and its data; the two administrators and the shared reference data stay.
- **Test mailboxes.** The four Gmail accounts in the table below, created only for testing. Each persona signs up with its own address (no aliases), and the bot reads each inbox.
- **Never give the bot** personal logins or real receipts. Ops is the administrator test account and is used for admin steps.

## Personas (accounts the bot holds)
| Persona | Address | Role | Notes |
|---|---|---|---|
| Alice (Test1) | stevewash123.test@gmail.com | customer | Primary user; owns most test data |
| Bob (Test2) | stevewash123.tester2@gmail.com | customer | Second household/user; must never see Alice's data |
| Carol | stevewash123.tester3@gmail.com | customer | Third independent reporter (N=3 rules) |
| Ops (Test4) | stevewash123.tester4@gmail.com | administrator | Made operator with `--make-operator`; two-step sign-in applies |

Passwords live in `RUN-CONFIG.md` only. Use two browser contexts (or private windows) so sessions never mix.

## Rules for the bot
1. Follow steps in order; do not improvise fixes. If a step cannot be done, stop that plan and report it.
2. Quote what you actually saw (exact text, amounts, dates); do not paraphrase.
3. Screenshot or page URL for every failure.
4. Stay on the StuffIt site and the test mailbox. Do not follow links to other sites.
5. Report using the format in `_template.md`.
6. Never substitute one persona for another. If a persona cannot sign in, sign in fresh or sign up again; if that fails, stop the plan and report it.
7. **Newest email only.** Gmail groups messages with the same subject into one thread. When a step asks for a link from an email you just requested, use the newest message in the thread; an older one may no longer work.
8. **Fixtures only through the database.** A bot with database access may create starting state a plan needs (for example a store with no policy), and must list every such fixture in its report and remove it at the end. Anything a plan is testing (signup, purchases, policy reports, confirmation, deletion) must be done through the site, never by writing rows.
9. **Administrators.** The administrator test account is Ops, `stevewash123.tester4@gmail.com` (Test4). It is an administrator and has access to every feature, so it runs any admin step; it does not stand in for Alice, Bob or Carol. An administrator can be made (or unmade) over HTTP with the maintenance key: `POST /api/maintenance/operators/grant` or `/operators/revoke` with header `X-Maintenance-Key` and body `{"email":"..."}`. It only works for an existing account whose email is confirmed, never creates an account, refuses to remove the last administrator, and is written to the admin audit trail as "maintenance key". The command line (`--make-operator <email>`) still works too. The key lives in `RUN-CONFIG.md` only. Two-step sign-in is ON for administrators since build `f1c96c7`: the first admin sign-in goes to Settings, Security to enrol an authenticator, and later sign-ins ask for a 6-digit code. Grok can compute the codes; keep the setup key in `RUN-CONFIG.md`, never in a report.

## Plans
The test plans are Scenarios 22 to 42 in the parent folder (Scenarios); each is a `scenario-N.md` in its own folder:
- Scenario 22 - Shared policy vs private purchase (**DRAFT**): shared policy visible to all, purchases private (Alice, Bob).
- Scenario 23 - Three reports confirm (**DEFERRED**, see S6.1.4): three matching reports do not confirm on their own; an administrator approves (Alice, Bob, Carol, Ops).
- Scenario 24 - Time travel and reminders (**DRAFT**): clock jump, reminder send, window ends; needs the simulated clock (Alice).
- Scenario 25 - Account lifecycle and email: two real accounts, signup, email confirmation, sign-in, password reset including a repeated request (Test1, Test2).
- Scenario 26 - Purchases, items and privacy: add purchases, suggested coverage, receipt upload, search and filter, privacy between accounts (Test1, Test2).
- Scenario 27 - Cards, notifications and export: cards, notification settings, data export, account deletion (Test1, Test2).
- Scenario 28 - Administrator sign-in and shared data: two-step sign-in for an administrator, the shared data screens, a customer refused, claims by API (Ops, Bob).
- Scenario 29 - Returns in progress: start and cancel a return, the working list, group by store, mark returned (Test1, Test2).
- Scenario 30 - Insurance policy and items: policy form, limits, items linked or left out, notes on the item (Test1, Test2).
- Scenario 31 - Extended warranty plan: plan covering several items, cost arithmetic, ending the plan (Test1, Test2).
- Scenario 32 - Reminders and to-dos: item To do card and the To do page (Test1, Test2).
- Scenario 33 - What is worth tracking: the Settings control and New Items following it (Test1, Test2).
- Scenario 34 - Color theme: themes, light and dark, kept per device (Test1, Test2).
- Scenario 35 - Send feedback: the form, your messages, the hourly limit (Test1, Test2).
- Scenario 36 - Claim guidance wizard: the Refund wizard, ranked routes, general-guidance labels, no promise of approval (Test1, Test2).
- Scenario 37 - Money recovered: refunds and card payouts, the Home total, no double count, export (Test1, Test2).
- Scenario 38 - Admin feedback queue: the administrator reads and sets the status of every account's feedback (Ops, Test1, Test2).
- Scenario 39 - Daily digest: choose the digest, one email a day, urgent bypass, bursts; needs the simulated clock and the maintenance key (Test1, Test2).
- Scenario 40 - Retest of the UAT fixes: the fixes from the 2026-11-02 rounds (Test1, Test2).
- Scenario 41 - Receipt plans and stated warranties (**DRAFT**): protection plans and printed warranties read from receipts and attached to the item; uses the real reader, so a miss is Partial (Test1, Test2).
- Scenario 42 - Policy source, recoverable to-dos and polish: the unconfirmed-policy note and Source link, Suggest coverage, Done and dismissed to-dos with Undo, and small interaction fixes (Test1, Test2, Ops).

Scenarios 25 to 27 and 29 to 35 use Test1 (Alice) and Test2 (Bob) from the persona table. They cover only parts that are built and were checked end to end, so a failure is a real finding. Run them in order: Scenario 25 creates the accounts that 26 and 27 use.

## Which build is running
`GET https://<ui-site>/api/version` (no sign-in) returns `{"commit":"abc1234","startedAt":"...","environment":"..."}`. `commit` is the short git hash Render deployed; `startedAt` is when that API process started (real time). Record both at the start of every run and in the report. After a push, poll it about once a minute starting five minutes later: a changed `commit` (or a new `startedAt`) means the deploy is live. The UI is a separate Render site, so this shows the API build only.

## Simulated clock
On the Render API service set `Clock__Simulated=true` and `Maintenance__Key` (16+ characters); `ASPNETCORE_ENVIRONMENT` must not be `Production` (the API refuses to start the clock there). Without them these endpoints return 404. Call them on the UI address, which forwards `/api` to the API (`https://<ui-site>/api/maintenance/clock`), with header `X-Maintenance-Key`:
- `GET /api/maintenance/clock` shows the offset and the app's date
- `POST /api/maintenance/clock/advance?days=N` moves forward (forward only)
- `POST /api/maintenance/clock/reset` returns to real time
- `POST /api/maintenance/run-reminders` and `/run-retention` run those jobs as of the app's date
Design and limits: `Stories/TESTING/T1-simulating-time.md`.
