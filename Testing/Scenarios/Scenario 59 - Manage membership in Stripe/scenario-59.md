# Scenario 59: Manage membership in Stripe

**Built per:** S1.2.2, push 13. The page after the click is **Stripe's own Customer Portal**, set up in the Stripe sandbox dashboard. Grade that it opens, shows the right account, and that Return and the webhook bring the result back. Do not grade Stripe's layout or wording.

**Needs:** the same as Scenario 58, plus a saved Customer Portal configuration in the sandbox. Use the **new normal-flow account from Scenario 58** with its license line showing (call it Stripe1). If none exists, mark everything **Not checked**.
**Time:** 20 min

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Stripe1 | Settings > Plan & billing > **Manage membership** | Button reads "Opening..." and is off; the browser goes to a `billing.stripe.com` page in test/sandbox mode |
| 2 | Stripe1 | Read the Stripe page (change nothing yet) | It shows the account's email (or name) and its subscription, the free-year membership. Say what plans, invoices and payment methods it lists, as information only |
| 3 | Stripe1 | Press Stripe's **Return** link | Back on Settings > Plan & billing, still signed in, the license line unchanged |
| 4 | Stripe1 | Press **Manage membership** again, then the browser **Back** button instead of Return | Back in the app, still signed in; the button is usable and does not stay on "Opening..." |
| 5 | Stripe1 | Open Manage membership, in Stripe choose **Cancel plan** and confirm | Stripe shows the plan as ending on the trial end date |
| 6 | Stripe1 | Return to the app, wait up to 1 minute, reload Plan & billing | The line still says **Free 1-year license** with the same end date (cancelling keeps what was already given until the end date). It must **not** say the license ended |
| 7 | Stripe1 | Open Manage membership again; if Stripe offers to keep or renew the plan, choose it | Stripe shows the plan active again; the app's license line is unchanged |
| 8 | Stripe1 | On Plan & billing double-click Manage membership quickly | One trip to Stripe only (no second window, no error) |
| 9 | Stripe1 | Sign out, open `/settings/billing` directly | Sent to sign-in; after signing in you land on Plan & billing |
| 10 | Alice | Press Manage membership (DB Stager account) | Plain red message "Your membership is not set up yet. Please try again in a few minutes." beside the button, button comes back; no Stripe page, no stack trace |
| 11 | Stripe1 | In a private window, paste the Stripe page address from row 1 | Stripe's own expired or invalid message, or the same page; nothing from the app exposed. Record which |
| 12 | Bob | Open Plan & billing, press Manage membership | Bob never reaches Stripe1's or Alice's customer; at most his own page or the "not set up yet" message |

Also record: a red message showing a raw server error or a Stripe error id, "Opening..." that never clears after coming back, the license line saying ended after row 5, and any case where one account saw another account's details on the Stripe page.

Not for Grok: the webhook status changes for **past due** and **ended** (Steve checks these with Stripe test clocks and the Stripe webhook log, `POST /api/stripe/webhook`).
