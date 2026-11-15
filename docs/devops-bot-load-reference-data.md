# Task for DevOpsBot: load the reference data into the WarrantyCat (alpha) database

Goal: the WarrantyCat database contains the reference data (brands, stores, cards, categories, manufacturer policies, return policies, claim guides, including the ski data) and nothing else. No accounts, no purchases, no test data, no placeholder policies.

## Rules
- Touch ONLY the WarrantyCat database. Do not touch the Dev database (`stuffit`) or Staging in this task.
- Never print, log or commit a connection string or any secret. Pass it as an environment variable for the one command.
- Never run `--seed-placeholders`. It creates FAKE policies. Never run `--remove-test-accounts`, drop anything, or reset anything on this database.
- Stop and report if any step errors, or if a check below does not match. Do not improvise a fix on this database.

## Before starting
1. Confirm which database is WarrantyCat: the Neon branch whose connection string is in the WarrantyCat API service's `ConnectionStrings__Default` on Render. Use its **direct** connection (not the pooled one).
2. Confirm the WarrantyCat API has started at least once with `Database__MigrateOnStart=true`, so the tables exist. Check the Render log for "Applied migration ... AccountSharingOnByDefault". If the log does not show it, stop and report.
3. Confirm the database has no accounts yet: `SELECT count(*) FROM accounts;` should be 0. If it is not 0, stop and report.
4. Work from the API repo at `C:\Projects\StuffIt\StuffIt_API`, on `main`. The ski files `reference-data/ski-round1.json` and `reference-data/entities-ski.json` are in a local commit (`d11a999`) that is not pushed. Use the local working copy as it is; do not pull over it or switch branches.

## Steps (from `C:\Projects\StuffIt\StuffIt_API`)
Set the WarrantyCat connection string in the environment for these commands only.

0. Take the fake policies out (alpha has some: about 335 manufacturer and 130 seller policies whose conditions say "[placeholder]"). From the same folder, with the WarrantyCat connection string set:
   `dotnet run --project src/StuffIt.Api -- --remove-placeholders --confirm`
   It removes only the fake policies and what hangs on them (their evidence and audit rows, and fake companies nothing uses). It prints how many it removed; report that number. Run it again: it must say 0. (`--seed-placeholders` no longer exists; do not look for it.)
1. Base seed (must come first; the researched files refer to brands it creates):
   `dotnet run --project src/StuffIt.Api -- --seed`
2. All researched reference files (the whole folder, idempotent):
   `dotnet run --project src/StuffIt.Api -- --import-reference reference-data`
3. Run step 2 a second time. Every line must say `inserted 0`. If anything is inserted the second time, stop and report.

## Checks (SQL against the WarrantyCat database)
- `SELECT count(*) FROM accounts;` is 0.
- Parties: `SELECT count(*) FROM parties;` is about the same as Dev's count of parties with no owner (`owner_account_id IS NULL`). Report both numbers.
- No placeholders: `SELECT count(*) FROM manufacturer_policies WHERE conditions ILIKE '%placeholder%';` is 0. Same for `seller_policies`. Also `SELECT count(*) FROM policy_evidence WHERE kind = 'Placeholder';` is 0.
- Every shared policy has a source: `SELECT count(*) FROM manufacturer_policies p WHERE owner_account_id IS NULL AND NOT EXISTS (SELECT 1 FROM policy_evidence e WHERE e.policy_id = p.id AND e.source_url IS NOT NULL);` should be 0 for the reference files' policies. Report any that are not 0 (the unconfirmed Backcountry and L.L.Bean returns are expected to have an address but count as no source in the app until confirmed).
- Ski data is present:
  - Manufacturer policies: Rossignol 24 months (no category); K2 Skis 24; K2 Snowboards 36; K2 "Ski boots and bindings" 12; Smith Helmets 36 months with purchased-from 2022-11-18.
  - Seller policies: evo 366 days; Christy Sports 367 days; Backcountry 90 days from delivery and L.L.Bean 365 days, both marked unconfirmed.
- Website present on Atomic, Rossignol, K2, Smith, evo.
- Hangfire tables are created by the API itself on its next start; do not create them by hand.

## Report back
- The output of steps 1 to 3 (counts only, no connection strings).
- The result of each check.
- Anything that was skipped, failed or surprised you.

## Do not do (separate tasks, wait for instructions)
- Creating the operator account (`--make-operator`): that happens after the owner signs up on the site.
- Resetting the Dev database.
- Pushing either repo.
