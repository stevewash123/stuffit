# Alpha launch runbook (2026-11-13)

Goal: the first outside tester (Ramesh) signs up on a clean WarrantyCat deployment that QA never touches. Code is feature-complete for alpha; what is left is deployment, secrets, email, and testing. Tick items as they are done. "Steve" = needs your accounts or your eyes; "CC" = I can do it or check it once I have the URL.

Source for the deployment steps: `StuffIt_API/docs/render-setup.md`. Gates and decisions: `HANDOFF.md`, section "Alpha readiness".

## A. Secrets first (Steve)
- [ ] Rotate the database password that sat in `StuffIt_API/docs/security.md`; remove it from the file.
- [ ] Rotate the credentials leaked in the public ConsignmentGenie_API repo (and make the repo private or clean its history).
- [ ] New `Jwt__Key` (32+ random characters) for the alpha API. Never reuse Staging's.
- [ ] A fresh Anthropic key for the alpha API.
- [ ] Decide Cloudinary: the doc reuses the ConsignmentGenie account (folder `stuffit/`, private files). For real receipts, prefer an account of its own, or at least confirm nobody else's tooling can list that folder.

## B. The deployment (Steve for settings, CC checks)
- [ ] New Neon branch for alpha, **direct** connection string (not pooled). Not the dev data.
- [ ] API Web Service (Docker, repo `StuffIt_API`, branch `main`, health check `/health`). Use the **Starter** instance, not Free: reminders and New Items processing only run while the API is awake.
- [ ] API environment: `ConnectionStrings__Default`, `Database__MigrateOnStart=true`, `Jwt__Key`, **`App__BaseUrl` = the alpha site's real URL** (the sign-up email link is built from it: Staging's sends `dev.warrantycat.com`), `Cors__Origins__0` = same URL, `Storage__Provider=cloudinary` + Cloudinary values, `Ai__Provider=anthropic`, `Ai__AnthropicApiKey`, `Ai__DefaultModel=claude-sonnet-5-5`, `Ai__ModelByKind__receipt` and `__document` = `claude-haiku-5-5`, `Email__ResendApiKey`, `Email__FromAddress`, `Email__FromName=WarrantyCat`, `Email__ReplyTo`, `Email__MailingAddress`, optional `Google__ClientId`.
- [ ] **Do NOT set** `Maintenance__Key` or `Clock__Simulated` on this deployment (they move the app's date and can make accounts administrators).
- [ ] UI Static Site (repo `StuffIt_UI`, `npm ci && npm run build`, publish `dist/stuffit-ui/browser`), rewrites in order: `/api/*` to the alpha API, then `/*` to `/index.html`. Custom domain if wanted.
- [ ] Let the API start once so migrations run (check the log for "Applied migration ... AccountSharingOnByDefault").
- [ ] Load reference data from your PC against the alpha branch, **in this order** (the researched files refer to the brands the base seed creates, so `--seed` must come first; `render-setup.md` leaves it out): `dotnet run --project src/StuffIt.Api -- --seed`, then `dotnet run --project src/StuffIt.Api -- --import-reference reference-data` (stores, brands, cards, policies, the ski data in `entities-ski.json` and `ski-round1.json`). Never run `--seed-placeholders`: it makes FAKE policies. A test (`ReferenceImportRehearsalTests`) runs this exact sequence inside a rolled-back transaction, so a broken file is caught before you load a real database.
- [ ] Storage check: `dotnet run --project src/StuffIt.Api -- --storage-check` with the alpha Cloudinary values.
- [ ] Sign up your own account on it, then `--make-operator <your email>`; set up two-step sign-in on that account.
- [ ] CC, with the URL: `/api/version` shows the current `main` commits and environment is not Staging-by-accident; `/health` is green; UI Last-Modified matches.
- [ ] Tell Grok's tooling and the DB stager that this site and database are off limits (until the planned pre-launch smoke, section D).

## B2. Make Dev look like launch (the plan: improve the ski data, then reset Dev)
Dev (Neon database `stuffit`) is also what the Staging site and Grok's QA use. Resetting it removes every account and all test data, which is the intent. Accounts are recreated as needed.
- [ ] **Ski data reviewed.** Round 1 is in `reference-data/ski-round1.json` and `entities-ski.json`: sourced terms for Rossignol, K2 and Smith helmets, returns for evo and Christy Sports, unconfirmed Backcountry and L.L.Bean, websites for the ski entities. What was left out, and why, is in the file's `note`. Read the "unconfirmed" ones on the stores' own pages and confirm them in Admin > Companies after the load.
- [ ] **Safety net (Steve):** make a Neon branch of the current `stuffit` database (or note the restore point). Name it so it is obvious, e.g. `stuffit-before-reset-2026-11`.
- [ ] **Stop writers:** tell Grok not to start a run (leave a TESTING-IN-PROGRESS note), and expect the Staging site to error for a minute.
- [ ] **Empty the database.** Neon will not let you drop the database you are in, so empty it instead: run `DROP SCHEMA public CASCADE; CREATE SCHEMA public;` and `DROP SCHEMA IF EXISTS hangfire CASCADE;` in the Neon SQL editor against `stuffit`. (Hangfire recreates its own tables on the API's next start.)
- [ ] **Rebuild the tables:** `dotnet ef database update -p src/StuffIt.Infrastructure -s src/StuffIt.Api` with `ConnectionStrings__Default` set to the dev string. This applies every migration from the first, including AccountSharing and AccountSharingOnByDefault.
- [ ] **Load the reference data:** `--seed`, then `--import-reference reference-data` (see section B). Do not run `--seed-placeholders`.
- [ ] **Check:** sign up an account on the Staging site, `--make-operator <email>`; the new account has the sharing box ticked; `/api/version` shows the current commits; Admin > Companies shows Rossignol, K2 and Smith with their policies, evo and Christy Sports with their returns, and no policy mentioning "[placeholder]".
- [ ] Tell Grok the database is fresh: its test accounts (Alice, Bob, Ops) must be recreated, and its fixtures that depend on placeholder terms (for example the Vizio "not the real terms" lines) will no longer exist.

## C. Email that reaches people (Steve, CC verifies)
Staging's sign-up email landed in Spam and linked to the wrong host. For the tester that means he may never see it.
- [ ] Send from a domain that matches the brand and is authenticated in Resend (SPF, DKIM, and a DMARC record). The doc's sender `stuff.microsaasbuilders.com` is verified, but a `warrantycat.com` sending domain will look right to Gmail and match the Terms.
- [ ] `Email__ReplyTo` and the address in the Terms are a mailbox you read: **support@warrantycat.com**. The Terms promise "email us and we will act on it" for sharing.
- [ ] Send one of every email type to a real Gmail and a real iPhone mail account and look at where it lands and where the link goes: verify your email, welcome, password reset, reminder, invitation, data export ready, anything else the app sends.
- [ ] Set Gmail aside: ask Ramesh to check spam and mark "not spam" on the first one, until the domain has a reputation.

## D. Testing (before Ramesh)
- [ ] **Your walkthrough** of the scenarios in `Testing/Scenarios` on the alpha site with your own account, especially what only a human can check: Google sign-in on business sign-up, the account switcher, the upload queue on a real phone, the change-back button state, "Stop it renewing" on a plan that auto-renews (never exercised in QA).
- [ ] **Phones:** take photos of real receipts on an iPhone (HEIC) and an Android and upload them; install the app to the home screen on both; try the camera upload (needs HTTPS, which Render gives).
- [ ] **A ski receipt end to end** (Ramesh's likely first upload): store, brand, item, coverage shown. The ski brands are names only, so coverage will be thin; decide what he is told.
- [ ] **Fresh-account run exactly as Ramesh would do it:** sign up, read the Terms in the window, tick the box, confirm email, add a purchase from a photo, see coverage, turn sharing off and on in Settings, export, sign out and in.
- [ ] **One Grok smoke** on the alpha site with throwaway accounts only, then wipe those accounts and their files before Ramesh is invited (so QA never mixes with his data).
- [ ] Check that deleting an account really removes it and its files (the Terms say it does).

## E. Running it (Steve)
- [ ] Neon backups: confirm the retention on the alpha branch, and fill the privacy policy's "[number of] days" with the real number.
- [ ] Render failure alerts on the API and the UI; know where the logs are. A simple uptime ping on `/health`.
- [ ] A way for Ramesh to report problems (an email address or a form) and a short note of known rough edges to send with the invite.
- [ ] Tell Ramesh it is an alpha and the legal text is a draft; who to contact; that his receipts are private and what is shared (the policy facts) and how to turn it off in Settings.
- [ ] A plan for the first bad day: how to switch the site to a maintenance notice, and how to restore from a Neon backup.

## Not needed for alpha
Stripe and billing, the marketing page, the lawyer's read of the legal pages, trademark and domain checks, the storage cap, the personal-information scan and withdraw list for sharing (only policy facts are shared, never files).
