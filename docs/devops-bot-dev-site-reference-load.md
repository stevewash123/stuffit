# Task for DevOpsBot: bring the Dev site's database (Neon `stuffit`) up to date with the reference data

The Dev site (Render static site `stuffit-ui`, whose API reports environment "Staging") reads the Neon database **`stuffit`**. It still has the old Oct 27 fake placeholder policies and does not have the ski data. Goal: remove the fakes, load the reference files, change nothing else. Accounts, purchases and everything Grok created stay.

## Rules
- Touch ONLY the Neon database `stuffit`. Not `stuffit_dev`, `stuffit_test`, `stuffit_test_ref`, and not the WarrantyCat/aDonelpha database.
- Never print, log or commit a connection string. Set it as an environment variable for these commands only.
- Do NOT run `--seed`, a reset, `--remove-test-accounts`, or drop anything. `--seed-placeholders` no longer exists.
- Stop and report if any step errors or a number below is not what is described. Do not improvise a fix.

## Before starting
1. Check `C:\Projects\StuffIt\Testing\Scenarios\Bot Rules\`: if `TESTING-IN-PROGRESS.txt` exists, wait (a QA run is using the site). Leave your own note there only if the instructions for DevOps say to.
2. Optional safety net: make a Neon branch of `stuffit` named `stuffit-before-ski-load-2026-11-14` (instant, free). Do it if you can; the steps are additive apart from deleting the fake policies.
3. Get the API code that has `--remove-placeholders --confirm` and the ski files: `C:\Projects\StuffIt\StuffIt_API` on `main`, at commit `c593687` or later (both are pushed to GitHub; `git pull` is fine, no local-only commits are needed any more). Check `reference-data/ski-round1.json` exists.
4. Count what is there now, and report it:
   - `SELECT count(*) FROM manufacturer_policies WHERE conditions ILIKE '%placeholder%';`
   - `SELECT count(*) FROM seller_policies WHERE conditions ILIKE '%placeholder%';`
   - `SELECT count(*) FROM accounts;` (expect Grok's test accounts; just report it)

## Steps (from `C:\Projects\StuffIt\StuffIt_API`, connection string for `stuffit` set as `ConnectionStrings__Default`)
1. Remove the fake policies:
   `dotnet run --project src/StuffIt.Api -- --remove-placeholders --confirm`
   It prints "Removed N placeholder policies." Report N. It deletes only the fake policies, their evidence and audit rows, and fake companies nothing uses. Run it a second time: it must say 0.
2. Load the reference files (the whole folder; idempotent; the base seed is already there):
   `dotnet run --project src/StuffIt.Api -- --import-reference reference-data`
   Report the lines for `entities-ski.json` and `ski-round1.json`.
3. Run step 2 again. Every line must say `inserted 0`. If anything is inserted the second time, stop and report.

## Checks (SQL against `stuffit`)
- Placeholders: both counts from step 4 above are now 0, and `SELECT count(*) FROM policy_evidence WHERE kind = 'Placeholder';` is 0.
- Accounts: the same number as before (nothing of Grok's was touched).
- Ski policies exist:
  - Manufacturer: Rossignol 24 months (no category); K2 Skis 24; K2 Snowboards 36; K2 "Ski boots and bindings" 12; Smith Helmets 36 months with purchased-from 2022-11-18.
  - Seller: evo 366 days; Christy Sports 367 days; Backcountry 90 days from delivery and L.L.Bean 365 days (both unconfirmed).
- Websites present on Atomic, Rossignol, K2, Smith, evo.
- The Dev API has the newest code: open `https://<the Dev API address>/api/version` and report the commits (should show API `c593687` or later and UI `0194421` or later). If the API has not redeployed yet, report it; do not redeploy.
- The new table exists (the API creates it on start): `SELECT count(*) FROM policy_source_checks;` runs without error. If the table is missing, the API has not restarted on the new code yet: report it.

## Report back
The counts before and after, N from step 1, the step 2 lines (counts only), every check result, and anything skipped or surprising. Then tell Steve and Grok that the Dev site now has no placeholder policies: Grok scenarios that relied on fake terms (the Vizio "not the real terms" lines) become Not tested, not Fail.

## Do not do
- Any change to accounts, purchases, files, or the alpha database.
- Pushing either repo.
