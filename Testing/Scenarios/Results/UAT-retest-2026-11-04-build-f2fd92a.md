# UAT retest: push 13 (WarrantyCat rename + Plan and billing), 2026-11-04

- **Build:** API `f2fd92a` (/api/version), UI `52098e3`, redeployed Nov 4 at 2:22 PM ET
- **Notes:** `CHANGES-push-13-warrantycat-rename-and-plan-billing-2026-11-04.md`
- **Mode:** no regression. Only the push 13 changes were tested.
- **Data:** DB Stager reset Alice and Bob only (23 rows deleted, 54 categories, clock offset 0). Nothing was staged.
- **Users:** Alice, Ops, and the new sign-up tester2+p13su1 (3 users)

## Summary
Pass 3 · Partial 2 · Fail 0 · Not checked 1 (the authenticator issuer)

| # | Check | Tag | Result | Evidence |
|---|---|---|---|---|
| 1 | Rename: no WarrantyBank or StuffIt on the pages | Full-only | **Pass** | Every tab title, signed in and signed out, ends '· WarrantyCat'. The footer reads '© 2026 WarrantyCat. Keep the paperwork, keep the protection.' The Share page and the Google/Apple app-password steps say WarrantyCat. The only exception is the admin account email stuffit-admin@microsaasbuilders.com on the Ops Security page, which is account data under the sender domain the notes mark as decided. Note: the first load served the old cached UI, and a hard reload fixed it. |
| 2 | Plan and billing tab | Full-only | **Partial** | /settings/billing reads 'Your membership is being set up. This can take a few minutes after you sign up.' The plans are Free for 1 year $0, Monthly $5.99 coming soon and Yearly $59.99 coming soon, with the radios disabled (as expected). **Manage membership** is present but stays disabled, even after a reload and a wait, so the Stripe portal was not reached. After the reset, Alice may have no billing record (see Needs CC). |
| 3 | Export README | Full-only | **Pass** | The README begins 'WarrantyCat data export, made 2026-11-04 19:39 UTC'. |
| 4a | Authenticator: an existing code still works | Full-only | **Pass** | Ops signed in with a code from the existing authenticator. Observation: the sign-in hung at 'Signing in…' for about 20 s before it completed. |
| 4b | Authenticator issuer reads WarrantyCat | Full-only | **Not checked** | Seeing the issuer needs re-enrolment, which would make the stored key stale. |
| 5 | Sign-up and reset emails | API+Full | **Partial** | Sign-up (tester2+p13su1, received 2:38 PM ET): sender name **"StuffIt"**, address `noreply@stuff.microsaasbuilders.com`, subject **"Confirm your email to start with WarrantyCat"**. Reset (Alice, received 2:38 PM ET): sender name **"StuffIt"**, address `noreply@stuff.microsaasbuilders.com`, subject **"Reset your WarrantyCat password"**. Both subjects are correct, and neither visible body has any WarrantyBank or StuffIt text (the bodies say "Welcome to WarrantyCat…" and "Use this link to choose a new password…"). Partial because the sender display name is still "StuffIt", not WarrantyBank as the notes expected; it needs editing in the Render dashboard. Reply-To is stuffit-admin@microsaasbuilders.com (sender domain decided). Links and tokens are not recorded. |

## Observations for Steve to decide
- The export ZIP filename is still `stuffit-export-2026-11-04.zip`. It is user-visible, but the notes don't list it, so it is reported as an observation, not a Fail.
- The email sender display name is "StuffIt" (row 5).
- The Ops sign-in took about 20 s at 'Signing in…' (row 4a).

## Needs CC
- Plan and billing: Manage membership stays disabled with 'Your membership is being set up' for Alice after the reset. CC or DB Stager should check whether a billing or Stripe customer record exists for Alice, or whether the reset removed it and nothing re-creates it. DB Stager did not stage this on this pass.

## Not run
- Scenarios 52-57 (warranty shapes) are on hold until Steve answers the plan questions.
- No regression was run, per the standing mode.
