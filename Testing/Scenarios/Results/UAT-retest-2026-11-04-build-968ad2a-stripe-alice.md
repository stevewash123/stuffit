# UAT retest: build 968ad2a, Stripe on (Scenarios 58 and 59 with Alice, push 15 export name)
Build: API 968ad2a (Staging, started 10:44 PM ET Nov 4; /api/version reports stripe enabled, secret key set, webhook secret set). UI Last-Modified 5:30 PM ET. Mode: Full-only. Tested 10:49-10:56 PM ET.
Account: Alice (stevewash123.test@gmail.com), deleted by Steve and recreated through the normal sign-up form at 10:49 PM ET, so she now plays the "Stripe1" role. Bob, Carol and Ops were not recreated yet.

## Headline
Stripe now works on staging. Alice's new sign-up got "Free 1-year license ... runs until Nov 4, 2027" straight away, and Manage membership opened the Stripe sandbox portal with the right account. Cancel and renew in Stripe both worked and the app kept the license line. The export ZIP is now named warrantycat-export-<date>.zip. One new Fail: after going to Stripe and pressing the browser Back button, Manage membership stays stuck on "Opening..." until a reload.

## Scenario 58
| # | Result | Notes |
|---|---|---|
| 1 | Pass | Sign-up, confirm email arrived 10:49 PM, link landed on /orientation "Welcome to WarrantyCat, Alice" |
| 2-3 | Pass | First look at Plan & billing already showed "Free 1-year license. Included with your account. It runs until Nov 4, 2027." (never "being set up") |
| 4 | Pass | Free for 1 year ($0); Monthly $5.99 and Yearly $59.99 "coming soon" |
| 5 | Pass | /account shows "Free 1-year license / Included with your account. It runs until Nov 4, 2027." No raw words. (Was Fail on 4f38dca.) /settings/profile has no status line, which is fine |
| 6 | Pass | Same line and date after reload and sign-out/in |
| 7 | Pass | Button read "Opening..." and the browser went to billing.stripe.com |
| 8 | Not checked | Only Alice tested tonight (no second sign-up) |
| 9 | Not checked | Needs a DB Stager account with no Stripe customer; Alice is now a Stripe account |
| 10 | Not checked | Bob not recreated yet |

## Scenario 59 (Alice as Stripe1)
| # | Result | Notes |
|---|---|---|
| 1 | Pass | "Opening..." then billing.stripe.com/p/session, "SteveWash sandbox" with Sandbox badge |
| 2 | Pass | Name Alice and her email; WarrantyCat Membership, $5.99 per month, "Free trial ends Nov 5, 2027"; no payment method; one invoice Nov 5, 2026 $0.00 Paid "Trial period for WarrantyCat Membership" |
| 3 | Pass | Return went back to /settings/billing, still signed in, line unchanged |
| 4 | **Fail** | After browser Back the button stayed "Opening..." and disabled and never cleared; a reload fixed it |
| 5 | Pass | Cancel subscription: "Cancels Nov 5, 2027 ... After your free trial ends on November 5, 2027, this service will no longer be available." |
| 6 | Pass | About 1 minute later the app still said "Free 1-year license ... runs until Nov 4, 2027", not ended |
| 7 | Pass | "Don't cancel subscription" then Renew: Stripe shows active ("Free trial ends Nov 5, 2027"); app line unchanged. Alice left active |
| 8 | Pass | Double-click gave one trip to Stripe, no second window, no error |
| 9 | Pass | Signed out /settings/billing goes to /login?returnUrl=%2Fsettings%2Fbilling, then lands on Plan & billing |
| 10 | Not checked | Needs a DB Stager account with no Stripe customer |
| 11 | Pass (record) | The old Stripe session address opened in a private window still loaded Alice's live portal page (name, email, subscription, invoice, Cancel subscription) with no sign-in, even after Alice signed out of the app. Nothing from the app was exposed. The plan allows "the same page", but note that anyone with that link can manage Alice's subscription until Stripe expires the session |
| 12 | Not checked | Bob not recreated yet |

## Push 15
| # | Result | Notes |
|---|---|---|
| 1 | Not checked | "Not set up yet" message needs an account with no Stripe customer |
| 2 | Pass | Export downloaded as warrantycat-export-2026-11-05.zip (3 KB), no HTTP 500 |

## Other findings
- Date difference: the app says the license runs until **Nov 4, 2027**; Stripe says the trial ends **Nov 5, 2027**. Probably UTC vs Eastern day boundary (sign-up was 03:49 UTC Nov 5), but worth deciding which the app should show.
- Unexpected sign-out: after Return from Stripe and the double-click test, /account showed the sign-in page although Alice hadn't signed out. Not reproduced or explained yet.
- Earlier push 13 Fail M3 (raw "One or more validation errors occurred.") still not re-checked: needs a no-Stripe account.

**Totals (24 rows):** 15 Pass, 1 Fail, 8 Not checked (rows 58-2/3 counted as one).

## Needs CC
- 59-4: Manage membership stuck on "Opening..." after browser Back (likely the page is restored from the back/forward cache with the busy state; reset it on pageshow).
- License end date one day off from Stripe's trial end (Nov 4 vs Nov 5, 2027).
- Unexplained sign-out after returning from Stripe (needs a repro).

## Not run
Rows needing Bob or a DB Stager no-Stripe account wait for the other accounts. Scenarios 52-57 are still on hold for Steve's plan answers.
