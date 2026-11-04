# Scenario 58: Free year license from sign-up

**Built per:** S1.2 (license in Stripe) and S1.2.2 (Plan & billing tab), pushes 12 and 13. The free year is a one-year Stripe trial on a price set up in the Stripe sandbox dashboard.

**Needs:** Stripe switched on for staging (`Stripe__Enabled=true`, secret key, webhook secret) and the price with lookup key `warrantybank_free_1yr` in the sandbox. If the staging site says "Managing your membership is not switched on yet." at row 7, Stripe is off: mark rows 3 to 8 **Not checked** and say so.
**Accounts:** a **new account made through the normal sign-up form** (not DB Stager), for example `stevewash123.test+stripe1@gmail.com`. Use a fresh plus-address each run. Alice and Bob from DB Stager have no Stripe customer and are used only in rows 9 and 10.
**Time:** 20 min

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | New user | Register with the sign-up form and finish any email step | Account created and signed in; sign-up is not slowed or blocked by Stripe |
| 2 | New user | Open Settings > Plan & billing straight away | Either the license line or "Your membership is being set up. This can take a few minutes after you sign up." **Manage membership** is off while it is being set up |
| 3 | New user | Wait 2 minutes, reload the page, repeat up to 3 times | The line becomes **Free 1-year license** with "Included with your account. It runs until <date>." The date is about one year after today (give the date you see) |
| 4 | New user | Read the three options | **Free for 1 year** ($0) selected; **Monthly** ($5.99 a month) and **Yearly** ($59.99 a year) greyed out, "coming soon", cannot be selected |
| 5 | New user | Open the Account page | The membership status is shown in plain words (no "none", no raw words like trialing) |
| 6 | New user | Reload, sign out, sign in again, open Plan & billing | The same license line and date; the date does not move |
| 7 | New user | Press **Manage membership** once | Only check here that the button reads "Opening..." and the browser leaves the site. The Stripe page is Scenario 59 |
| 8 | New user | Register a **second** new account the same way | Its own license and its own date; nothing from the first account is shown |
| 9 | Alice | Open Plan & billing | The line is plain words (no error text, no raw status). If **Manage membership** is on and pressed, the red message "Your membership is not set up yet. Please try again in a few minutes." is acceptable (DB Stager accounts have no Stripe customer); the button comes back |
| 10 | Bob | Open Plan & billing | Bob sees his own account's line only, never Alice's |

Also record: any raw word such as `trialing`, `none`, `null` or a status code on screen, any date that is not about a year ahead, a license line that appears and then disappears on reload, and any way sign-up was delayed or failed because of billing.

Not for Grok: the **trial ending** (needs a Stripe test clock; Steve checks it in the Stripe dashboard).
