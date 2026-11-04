# Security notes

No secrets in this file or anywhere under C:\Projects. See also `C:\Projects\GITHUB-SETUP.md`.

## Database (Neon, WarrantyCat)
- The connection string is stored in **dotnet user-secrets** for `StuffIt.Api` (UserSecretsId `826661e7-f2c8-407b-a300-826f73d39705`), at `%APPDATA%\Microsoft\UserSecrets\<id>\secrets.json`, outside every repo.
- Key: `ConnectionStrings:Default` (Npgsql keyword format).
- Staging/production: environment variable `ConnectionStrings__Default` on the host.
- The original password is in the Neon console (project > Connect). Rotate it there if it is ever exposed, then update user-secrets.

## Rules
- Never commit or paste credentials. `.gitignore` excludes `.env*` and `appsettings.Development.json`.
- If a secret is committed or shared, rotate it; deleting it from history is not enough.
- ConsignmentGenie_API (public) leaked a DB password and an email API key: rotate them.



TEST DATABASE CONNECTION STRING:  postgresql://neondb_owner:npg_6NgyWLz7RAkc@ep-square-smoke-b4qkzqjp-pooler.c-6.us-east-2.aws.neon.tech/stuffit_test?sslmode=require&channel_binding=require