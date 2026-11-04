# UAT retest: push 13 follow-up, Manage membership (S1.2.2)
Build: API f2fd92a (Staging), UI redeployed 2026-11-04 3:06 PM ET. Mode: Full-only (browser). Tested 3:22-3:29 PM ET.
Notes: CHANGES-push-13-manage-membership-2026-11-04.md, rename notes v2. No DB Stager reset this pass (Alice only had an export since the 2:36 PM reset).

| # | Check | Account | Result | What we saw |
|---|---|---|---|---|
| M1 | License line and options | Alice | Pass | "Free 1-year license", "Included with your account. It runs until Nov 4, 2027." Free for 1 year $0 selected; Monthly $5.99 and Yearly $59.99 "coming soon", disabled |
| M2 | Manage membership on for licensed account | Alice | Pass | Enabled, "Opens Stripe, where you can change your plan, update your payment method, see invoices or cancel." |
| M3 | Server refuses (no Stripe customer): red message | Alice | **Fail** | Shown: "One or more validation errors occurred." Expected: "Your membership is not set up yet. Please try again in a few minutes." Looks like a raw server validation error |
| M4 | Button comes back after refusal | Alice | Pass | Button returned, still enabled, stayed on /settings/billing |
| M5 | New sign-up account gets license | tester2+p13su1 (normal sign-up, created ~3:23 PM ET) | **Fail** | Still "Your membership is being set up. This can take a few minutes after you sign up." with Manage membership disabled after ~6 min of reloads (last 3:29 PM ET) |
| M6 | Opening... then Stripe page, Return back | tester2+p13su1 | Not checked | Blocked by M5 |
| R1 | Rename on visited pages | both | Pass | No visible WarrantyBank/StuffIt on /settings/billing, /orientation ("Welcome to WarrantyCat, UAT"), titles "· WarrantyCat" |

Re-grade of earlier row 2 (Manage membership disabled for Alice): superseded. Alice now has a license and an enabled button (M1/M2); the remaining issue is M3.

**Totals:** 4 Pass, 0 Partial, 2 Fail, 1 Not checked.

## Needs CC
- M3: map the portal refusal for accounts without a Stripe customer to the friendly "not set up yet" message instead of the raw validation error.
- M5: license / Stripe customer not created (or very slow) for an account made through normal sign-up on staging. Check whether Stripe is on for staging and whether the sign-up hook runs.

## Not run
Scenarios 52-57 on hold pending Steve's answers to the plan questions.
