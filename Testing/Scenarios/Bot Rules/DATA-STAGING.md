# Data staging for the browser test plans

For the bot that prepares the database before the browser bot (Grok) runs. The browser bot should spend its effort testing, not rebuilding the same four accounts and the same starting items in every plan. This file says what state to leave things in. The rules in `README.md` still apply (in particular rule 8: anything a plan is *testing* must be done through the site, never by writing rows; every fixture you write is listed in your report and removed at the end).

Targets the UAT database only (the dev database `stuffit`, shared with the deployed UAT site). Never run any of this against a database holding real users.

## Two levels of reset

**Run reset: drop and recreate (once, before a run).** Delete the four personas and everything they own, then create them again as the fixture accounts below. Use the app's own deletion (`dotnet run --project src/StuffIt.Api -- --remove-test-accounts --confirm` removes every non-administrator account and its data; it keeps the administrators and shared reference data) or delete the same rows by hand. Then recreate:

| Persona | Address | Role | State to create |
|---|---|---|---|
| Alice (Test1) | stevewash123.test@gmail.com | customer | email confirmed, terms accepted (current version), display name "QA Test 1", known password from `RUN-CONFIG.md`, quick set-up not finished, no cards, no items |
| Bob (Test2) | stevewash123.tester2@gmail.com | customer | same, display name "QA Test 2" |
| Carol | stevewash123.tester3@gmail.com | customer | same, display name "QA Test 3" |
| Ops (Test4) | stevewash123.tester4@gmail.com | administrator | Reset in place by default: keep the account and the operator flag, turn two-step OFF, clear its sessions and its data. Delete-and-recreate is allowed (Steve approved it, with the maintenance key as the safeguard): recreate the account like the others, then make it an administrator with `POST /api/maintenance/operators/grant` (header `X-Maintenance-Key`, body `{"email":"stevewash123.tester4@gmail.com"}`). Display name "QA Test 4". Scenario 28 enrols two-step itself |

`--create-user <email> <password>` creates a confirmed account (add `--operator` for Ops). Time zone: America/New_York. Do NOT run the run reset between plans: it is only for the start of a run, because the plans that test sign-up and deletion expect to create and destroy accounts themselves.

**Scenario reset: wipe the data, keep the person (before each plan).** For each persona the plan uses, delete everything the person created and put their settings back to defaults, but keep the login (user row, password hash, confirmed email, terms acceptance, account row). Delete, per account:
- purchases, items, coverages, reminders, documents/files (and the stored files), pending (New) items, to-dos, returns and recoveries (`item_returns`, `recoveries`)
- cards (payment methods and their last-4 rows), insurance policies and limits, warranty plans, private stores/brands/policies the account added
- notifications, notification settings and preferences, feedback messages, data exports (and their files), linked mailboxes
- claims the person reported (`shared_claims` accounts links), per-person tracking minimum, any theme/profile choices stored server-side (theme is per browser, not stored)
Reset the user's own settings to defaults: time zone America/New_York, reminder time default, tracking minimum unset (so the standard $50 applies), digest/email toggles at defaults. Revoke refresh tokens (so the browser bot signs in fresh). Clear the maintenance clock to offset 0 (`POST /api/maintenance/clock/reset`) unless a plan is mid-run.
Easiest correct method: delete from every table that has an `account_id` for that account (children first), except the account and membership rows. Check the schema rather than trusting this list; new tables arrive often. After the reset, verify and report counts of zero for items, purchases, pending items, cards, to-dos, feedback, exports.

**Shared data:** a reset never touches shared reference data (stores, brands, policies, card catalog, claim guides). The leftovers that plans create there (claims, shared test stores, `UAT04 Policy Store`) are cleaned by the scripts in `scripts/tools/` (`cleanup18.js`, `cleanup_shared.js`) at the end of a run, and listed in the report.

## Start state each plan expects

"Clean" = scenario reset done, nothing else. Create fixtures through the database only where the plan says so; the plan's own steps must create everything else through the site.

| Plan | Personas | Start state |
|---|---|---|
| 22 Shared policy, private purchases | Alice, Bob | clean. Seeded reference data present (`--seed`; New Balance and a store with a known window) |
| 23 Three reports confirm | Alice, Bob, Carol, Ops | DEFERRED. When built: clean; Ops with two-step already enrolled; a fixture store/brand with no policy (listed, removed after) |
| 24 Time travel and reminders | Alice | clean; `Clock:Simulated=true` and `Maintenance:Key` set on the deployed API; clock offset 0 |
| 25 Account lifecycle and email | (none) | **No reset to existing accounts: the addresses must have NO account** (drop them first). The bot signs them up itself. Use a different address for the sign-up probe |
| 26 Purchases, items, privacy | Alice, Bob | clean. Both accounts exist and are signed up (create them as in the run reset: the sign-up path is Plan 25's job) |
| 27 Cards, notifications, export | Alice, Bob | clean, plus Alice has at least one purchase (Plan 26 leaves one; if not, create one item "UAT Seed Item" by hand). **Bob is deleted at the end of the plan**: recreate Bob afterwards |
| 28 Administrator two-step, shared data | Ops, Bob | Ops operator with two-step OFF (the plan enrols it; store the key in `RUN-CONFIG.md` only). Bob clean. Between runs, turn Ops's two-step back OFF |
| 29 Returns in progress | Alice, Bob | clean (no item named "UAT Return ...") |
| 30 Insurance | Alice, Bob | clean, plus Alice has 3 items added by hand, today's date, any store: "UAT Guitar" 1800.00, "UAT Laptop" 1200.00, "UAT Lamp" 40.00. No insurance policies |
| 31 Extended warranty plan | Alice, Bob | clean, plus Alice has 2 items: "UAT Fridge" 900.00, "UAT Washer" 600.00, today's date, any store. No plans |
| 32 To-dos | Alice, Bob | clean, plus Alice has 1 item "UAT Reminder Blender", today's date, any store. No open to-dos |
| 33 What is worth tracking | Alice, Bob | clean (empty New Items); tracking minimum unset. The receipt to upload is in the plan (record file and its lines first) |
| 34 Color theme | Alice, Bob | clean. The bot must use a browser profile with no earlier choice |
| 35 Send feedback | Alice, Bob | clean (no feedback rows: the 5-per-hour limit counts rows from the last hour, so the reset also resets the limit), plus Alice has at least one item |
| 36 Claim guidance wizard | Alice, Bob | clean, plus Alice has: item "UAT Blender" (Best Buy, Cuisinart, Small appliances, 89.99, today, return window and maker warranty ticked), a card "UAT Card" (Chase Sapphire Preferred, benefits confirmed) with item "UAT Card Item" paid by it, and item "UAT Plan Item" covered by an extended plan. The 8 general claim guides loaded |
| 37 Money recovered | Alice, Bob | clean (no recoveries), plus Alice has items "UAT Rec One" 120.00, "UAT Rec Two" 60.00, "UAT Rec Three" 45.00, "UAT Rec Four" 200.00 and Bob has "UAT Rec Bob" 50.00 (any store, today) |
| 38 Admin feedback queue | Ops, Alice, Bob | Ops operator with two-step enrolled (store the key in `RUN-CONFIG.md`); Alice and Bob clean with NO feedback this hour; Alice has one item |
| 39 Daily digest | Alice, Bob | clean; simulated clock on with the maintenance key; clock offset 0; Alice time zone America/New_York, reminder time 9:00; digest choices at default |
| 40 Retest of the UAT fixes | Alice, Bob | clean; simulated clock on, offset 0; Cloudinary with PDF and ZIP delivery enabled; the 12-line Pine Street receipt available |

Plans 1 to 21 are not browser plans (answer keys, runners, email senders); they have their own cleanup scripts and are not covered here.

## At the end of a plan and of a run
- Report every fixture you created and every row you wrote, in the same report format, so the browser bot's report and yours reconcile.
- After a plan that created shared data (claims, shared entries, `UAT04 Policy Store`), run the matching cleanup script and say so.
- At the end of a run, leave Ops's two-step OFF, the clock at offset 0, and no persona with leftover data except what the next run's reset will remove.
- If something cannot be reset cleanly (a table you did not recognise, a stored file you could not delete), stop and report it. Do not guess: a half-reset account makes the next plan's results meaningless.

## Clarifications from the first dry run (2026-11-02)
Answers to the staging bot's gaps. Anything marked **Steve** needs a person's decision or a secret, not a guess.

- **Ops rebuild: decided.** Steve approved delete-and-recreate of Ops with the maintenance key as the safeguard (the web endpoint above). The `--ops-rebuild` flag may be used.
- **Plan 25 needs Alice and Bob absent.** Add a drop-only mode: delete the persona and its data and create nothing. Plan 25 then signs them up through the site. After Plan 25, run the normal run-reset recreate for Alice and Bob before Plans 26 onward.
- **Terms version.** Recreated accounts must carry the app's *current* terms version, not an old one, or the browser bot is stopped by an accept-terms screen. Read it from the app (`LegalVersions.Current` in `StuffIt.Core/Legal`; today `2026-10-01`) and stamp `terms_accepted_at` now.
- **Clock offset is not in the database.** Reset it with `POST /api/maintenance/clock/reset` (needs the maintenance key and the API URL) or an API restart, never SQL. Timestamps already written under a shifted clock go away with the data reset, so a non-zero offset only matters for rows you create next: reset the clock first, then stage fixtures. **Steve** supplies the maintenance key and the UI/API URLs as environment values (never in chat or a committed file).
- **Fixture items: create them as the person, through the app's API, not by SQL.** Sign in as the persona with the known password, add the item the way the UI does (`POST /api/purchases` with the store, date and item), so the app derives its own coverage from the policies. Plans 30, 31 and 32 assume the items carry a return window ("Return window · Target"), so items inserted by SQL with no coverage would change what those plans see. Insert by SQL only when the API route is not available to the staging bot, and say so in the report so the browser bot's findings can be read in that light.
- **Fixture dates.** "Today" is today in Alice's time zone (America/New_York), the same convention the UI uses for the date field. Not the UTC date.
- **Orphaned files.** SQL does not remove stored files (`documents.file_key`, `data_exports` zips). For UAT that is acceptable. Before a real run, list the keys in the report so they can be purged from storage later (the Cloudinary `stuffit/` folder). **Steve** decides whether to purge them.
- **Attribution left in place.** `reference_audits.user_id` and `policy_evidence.entered_by_user_id` rows on shared data stay as they are: they are the audit trail and shared data is out of scope for a reset.
- **Operator tokens.** Do not read, change or delete `operator_tokens` rows. They are credentials. **Steve** should check the admin accounts' tokens and revoke any that are not in use, since some labels look like token fragments.
