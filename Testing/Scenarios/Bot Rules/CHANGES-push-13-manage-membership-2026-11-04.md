# What changed in push 13: Plan and billing, Manage membership (2026-11-04)

For GrokBot. API and UI commits are named in the push message; check `/api/version` and record it. No migration. This is story S1.2.2.

Settings has a **Plan & billing** tab (it was a placeholder). Where you can go depends on the account:

| Account | What you should see |
|---|---|
| Any signed-in account | Settings > Plan & billing: the license line ("Free 1-year license", "Included with your account. It runs until ..."), then three options: **Free for 1 year** ($0, selected), **Monthly** ($5.99 a month) and **Yearly** ($59.99 a year). Monthly and yearly are greyed out and say "coming soon"; you cannot select them |
| A brand-new account with no license yet | "Your membership is being set up. This can take a few minutes after you sign up." The **Manage membership** button is off |
| An account with a Stripe license | **Manage membership** is on. Click it: it reads "Opening...", then the browser goes to a Stripe page. Stripe's **Return** link comes back to Settings > Plan & billing |
| An account with a license, when the server refuses (Stripe off, or no customer yet) | A red message beside the button ("Managing your membership is not switched on yet." or "Your membership is not set up yet. Please try again in a few minutes."); the button comes back so you can try again |

## What you can and cannot check
- Accounts made by DB Stager (Alice, Bob) have **no Stripe customer**, so Manage membership gives the "not set up yet" message for them. That is expected, not a bug.
- The Stripe page itself (plans shown, cancelling, invoices) is Stripe's, set in the sandbox dashboard. Check only that it opens and that Return comes back; do not grade its content.
- To reach the Stripe page, use an account registered through the normal sign-up flow while Stripe is on for staging. If no such account exists, grade the portal rows Not checked.

## Decided, do not report
- The monthly and yearly options are placeholders and cannot be chosen; buying is not built (S1.2.1).
- No Founders option yet; it will be a database flag later.
- Behind the scenes (not for grading): a new account's free year is now a one-year Stripe **trial** on the sandbox price, so its status reads trialing and the license line still says "Free 1-year license". Nothing on screen changes.
