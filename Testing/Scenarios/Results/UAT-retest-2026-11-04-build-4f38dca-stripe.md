# UAT retest: push 14, Scenarios 58 and 59 (Stripe license and Manage membership)
Build: API 4f38dca (Staging, restarted 4:52 PM ET), UI Last-Modified 3:06 PM ET. Mode: Full-only. Tested 5:14-5:24 PM ET.
DB Stager reset Alice and Bob at ~5:15 PM ET: all testers have subscription_status 'none', no Stripe customer id, 0 stripe_events.
New accounts via normal sign-up: stevewash123.test+stripe1 (created ~5:16 PM ET) and +stripe2.

## Headline
No account ever got a license. Every account, both fresh sign-ups and Alice and Bob, shows "Your membership is being set up. This can take a few minutes after you sign up." with Manage membership disabled, still after ~15 minutes. No red message ever appeared, so this is not the "not switched on" case. The likely cause is that the sign-up never creates the Stripe customer/trial on staging (Stripe config, webhook, or price `warrantybank_free_1yr`). All Stripe-page rows are blocked.

## Scenario 58
| # | Result | Notes |
|---|---|---|
| 1 | Pass | Sign-up created and signed in (/orientation "Welcome to WarrantyCat, UAT"), not slowed by billing (form took a few seconds) |
| 2 | Pass | "Your membership is being set up..." with button off |
| 3 | **Fail** | Never became "Free 1-year license" after 2/4/6 min and again at ~15 min |
| 4 | Partial | Options right ($0 selected, Monthly/Yearly "coming soon" disabled), but no license line |
| 5 | **Fail** | Account page shows no membership status line at all |
| 6 | Partial | Same "being set up" line after sign-out/in; no date to compare |
| 7 | Not checked | Button disabled |
| 8 | **Fail** | Stripe2 also "being set up", no license (checked right after sign-up only) |
| 9 | **Fail** | Alice: "being set up", button disabled (expected license line or "not set up yet" red message). Earlier today on f2fd92a, before the reset, she showed "Free 1-year license ... runs until Nov 4, 2027" with the button on |
| 10 | Pass (isolation) / Fail (line) | Bob sees only his own page; same "being set up" line |

## Scenario 59
| # | Result | Notes |
|---|---|---|
| 1-8 | Not checked | Manage membership never enabled for Stripe1 |
| 9 | Pass | Signed out /settings/billing goes to /login?returnUrl=%2Fsettings%2Fbilling, then lands back on Plan & billing |
| 10 | Not checked | Alice's button disabled, so the "not set up yet" message can't be reached |
| 11 | Not checked | No Stripe page reached |
| 12 | Pass (isolation) | Bob never reached any Stripe page |

Earlier push-13 membership Fails: M3 (raw "One or more validation errors occurred.") can't be reproduced now because the button is disabled, so it is not confirmed fixed. M5 (new sign-up stuck "being set up") is **still failing**. M6 is still Not checked.

No raw words (trialing/none/null) and no WarrantyBank/StuffIt on any page.

**Totals (22 rows):** 4 Pass, 2 Partial, 5 Fail, 11 Not checked. Rows 58-10 and 59-12 are counted as Pass on isolation.

## Needs CC
- Find why staging sign-up doesn't create the Stripe customer or free-year trial (check Stripe__Enabled, keys, the webhook, price lookup key warrantybank_free_1yr, and that stripe_events stays at 0). DB Stager confirms 0 Stripe events for every account.
- The UI shows "being set up" indefinitely for status 'none', including DB Stager accounts. The notes expected Alice and Bob to reach the "not set up yet" message.
- The Account page has no membership status line (58-5).
- The DB Stager reset nulls the Stripe fields, so Alice and Bob can never have a Stripe customer. That is expected per the notes, but there is no way to test the portal with them.

## Not run
Scenarios 52-57 are on hold pending Steve's answers to the plan questions.
