# StuffIt / WarrantyBank UAT regression: build 8e7ea94

**Build:** commit `8e7ea94`, environment Production, started 5:15 PM EST Nov 1, 2026 (from GET /api/version)
**Run:** Nov 1, 2026, 6:40 to 6:58 PM EST, in the browser as real users
**Accounts:** Bob = stevewash123.tester2@gmail.com, Carol = stevewash123.tester3@gmail.com, Test4 = stevewash123.tester4@gmail.com (now the admin/operator account). Alice's own login (Test1) still isn't usable by the browser, so Test4 stood in for Alice in UAT-03, and Carol played Test1 in UAT-07.

## Summary

| Plan | Result | Change since last build |
|---|---|---|
| UAT-03 | 5 pass, 1 partial (step 1); step 7 deferred, so step 8 not tested | Same as before |
| UAT-04 | Deferred (waiting on ping/auto-approve) | n/a |
| UAT-05 | On hold (simulated clock) | n/a |
| UAT-06 | 10 pass, 2 fail (steps 14, 15); step 5 skipped; 6, 7, 11 not rerun (accounts exist) | Same; no 429 rate-limit hit this run |
| UAT-07 | 13 pass, 4 partial (1, 5, 9 notes, 11), 1 fail (8) | Same; new: "May be covered" filter doesn't narrow; upload race |
| UAT-08 | On hold (deletes Bob; needs your OK) | n/a |

## Still failing (carried over)
1. No "usual window, can differ for your item" note on suggested coverage (UAT-03 step 1, UAT-07 step 5).
2. Approximate purchase dates still produce exact-day coverage and "Expiring soon" (UAT-07 step 8).
3. Password reset accepts the current password as the new one (UAT-06 step 14).
4. A used reset link still shows the form; "Invalid token." only appears after submit (UAT-06 step 15).
5. The Add purchase field order is store first, while the plan expects brand first (UAT-07 step 1). This may be a plan issue rather than a bug.
6. The item page has no policy source link; it's only on the store's settings page (UAT-03 step 3).

## New this run
- The "May be covered" filter doesn't narrow the items list (UAT-07 step 11).
- Receipt upload: clicking Upload while "Reading your document…" is still showing silently drops the file. Reading takes ~12 s and upload ~10 s.
- Test4 signed in with email and password only and went straight to /admin, with no two-step prompt (6:50 PM EST). **Not a bug:** Steve confirmed two-step is deferred by a deployment setting.
- The store dropdown on Add purchase lags behind typing.
- "Suggest coverage" on the item page gave no visible response.

---

## UAT-03 (build 8e7ea94): 5 pass, 1 partial, step 7 blocked, step 8 not tested
Alice = Test4 ("QA Test 4"), Bob = tester2.

| # | Result | Observed |
|---|---|---|
| 1 | Partial pass | Added "REG-8e7ea94 Alice shoes" (New Balance, Nov 1, 2026, Footwear). The add form suggested "New Balance return policy · Merchant · 30 days · Unconfirmed" and "New Balance warranty · Manufacturer · 6 months · Unconfirmed" with "Counted from today until you give the date." Once ticked and saved, the item showed "Return window, Nov 1 to Dec 1, 2026 · 30 days left". The suggestion is not pre-applied; you have to tick it. No "usual window, can differ for your item" note; the closest is the policy text "The 30 days is not stated in the order email, so confirm it on the source page before relying on it." |
| 2 | Pass | Bob's "REG-8e7ea94 Bob shoes" (New Balance, Oct 25, 2026) got the same suggestions and the window "Oct 25 to Nov 24, 2026", counted from his own date. |
| 3 | Pass with caveat | The policy text is identical for both users. The item page has no source link; it only appears under Settings › Stores & brands › New Balance ("Shared · Source" goes to https://www.newbalance.com/returns). That page rendered blank in the test browser (possibly a bot block; not confirmed). The policy is labelled "Unconfirmed: Not yet confirmed against the store's page." |
| 4 | Pass | Changed Alice's end date from Dec 1 to Dec 15, 2026; it showed "Nov 1 to Dec 15, 2026". |
| 5 | Pass | Bob's item was still Nov 24, 2026 with 23 days left. |
| 6 | Pass | Account, Settings (Profile, Stores & brands, Privacy & data) and the store page show no other users' purchases or counts, and nothing identifies Bob. Notifications and Returns were not checked. |
| 7 | Blocked | There is no "share" box. Stores & brands says "The ones you add are private to you." Neither the add-store form nor the policy drawers have a share option. "Suggest coverage" on the item page did nothing visible. |
| 8 | Not tested | Nothing was submitted in step 7. The seeded shared policies show as "Unconfirmed"/"Shared" and never as official. |

**Other observations (UAT-03)**
- The store dropdown results lag behind what you type; you have to type the full name and wait.
- The browser console shows 1 error on every page (not investigated).
- "Suggest coverage" button on the item page gave no visible response.
- Steps 7-8 may be out of date for the current design (user-added stores are private).
- Test data left: "REG-8e7ea94 Alice shoes" (Test4) and "REG-8e7ea94 Bob shoes" (Bob).

---

## UAT-06 (build 8e7ea94)
"Test1" role = Test4 (stevewash123.tester4@gmail.com); accounts already existed, so steps 6, 7 and 11 (new sign-up and confirm) were not rerun.

| # | Result | Observed |
|---|---|---|
| 1 | Pass | Redirect to /login?returnUrl=%2F; tab "Sign in · WarrantyBank". |
| 2 | Pass | /terms, /privacy, /disclaimer load signed out; "Version 2026-10-01"; banner "Draft for review. This text has not yet been read by a lawyer." |
| 3 | Pass | Empty submit: "Enter a valid email address.", "Use at least 10 characters.", "Please agree to continue." No message on Confirm password. |
| 4 | Pass | `short1`: "Use at least 10 characters."; `abc`: "Enter a valid email address." No stack traces/JSON. |
| 5 | Skipped | "Wrong address? Start again" only appears after a real sign-up; no new account was created. |
| 8 | Pass | Sign out + Back: blank sign-in form, no account data. |
| 9 | Pass | Wrong password and unknown email both: "Invalid email or password." |
| 10 | Pass | Sign-in ~2 s; nav Home, My Items, New Items, Returns, Notifications. No 429 this run. |
| 12 | Pass | Duplicate sign-up: "An account with this email already exists. Try signing in." |
| 13 | Pass | "If that email is registered, we sent a link to reset your password. It may take a minute to arrive." |
| 16 | Pass | Same neutral message for nobody.uat@example.com. |
| 14 | **Fail** | Reset email arrived in ~1 s ("Reset your WarrantyBank password"). The reset form accepted the **current password** as the new one: "Your password was changed. Sign in with the new one." Sign-in afterwards works. Same as the previous build. |
| 15 | Fail (wording) | The used link still loads the form; only on submit does it show "Invalid token." The token is single-use, but the message doesn't say the link was used or has expired. |

**Other observations (UAT-06)**
- **Test4 is now an administrator:** after sign-in it lands on /admin (Admin "Shared data" page). Earlier today it landed on Home. Because of this, Test4 shouldn't stand in for a normal user in privacy tests.
- Sign-up still reveals that an email is registered ("An account with this email already exists."), while sign-in and forgot-password don't.
- No message on Confirm password for an empty form.
- The account menu still sometimes needs a second click before "Sign out" appears.
- Signed out, the console shows only 401 errors from the session check; no page took 3 s or more.

---

## UAT-07 (build 8e7ea94): 13 pass, 4 partial, 1 fail
"Test1" role = Carol (tester3, started with no items), "Test2" role = Bob. Store Best Buy (15-day return), brand Cuisinart (1-year warranty), Small appliances.

| # | Result | Observed |
|---|---|---|
| 1 | Partial | /add/new field order: Store, Date you bought it, Credit card used, Order number, Category, Brand (optional), Item, Model number, then "More about this item" (Price, Size, Serial, Notes). The plan expects brand, then name, then store. Unchanged from the last build. |
| 2 | Pass | Empty save: "Add at least one item." and "Tell us what you bought." Nothing saved. |
| 3 | Pass | "R7 Blender" $89.99, Nov 1, 2026 saved and went straight to the item page (~2.1 s). The Best Buy window was "Confirmed" and ticked; the Cuisinart warranty was "Unconfirmed" and **unticked by default**. |
| 4 | Pass | Read-only: "Bought Nov 1, 2026 from Best Buy", $89.99. |
| 5 | Partial | Return Nov 1 to Nov 16, 2026 (15 days, correct); warranty Nov 1, 2026 to Nov 1, 2027 (correct). **No "usual window, can differ" note.** Warranty text is still "[placeholder] Fake terms for testing". The Best Buy holiday extension in the policy text (2025 season) wasn't applied, as you'd expect for 2026. |
| 6 | Pass | Edit mode: Done, Mark returned, Mark disposed, Delete; edit/delete icons on each coverage; Add coverage, Suggest coverage, "Add a receipt or other file". |
| 7 | Pass | Renamed to "R7 Blender 2"; shows on the item and in My Items. |
| 8 | **Fail** | With "Only the month" chosen, the item shows "Bought Nov 2026 (approximate)", but coverage still shows exact days ("Nov 1 to Nov 16, 2026 · 15 days left", "Until Nov 1, 2027") and the badge is "Expiring soon". No range or "may be covered". Unchanged from the last build. |
| 9 | Pass (notes) | Uploaded the FS-01 Home Depot receipt JPG. "Reading your document…" took ~12 s, then "What we found in your document" listed conflicts (Home Depot, Milwaukee, 249.00, 2026-09-14); "Not now" kept the item unchanged. Upload took ~10 s more; it then shows "Receipt receipt.jpg (53 KB)" with View / Read it / Delete. View opens the image. The first attempt was lost when Upload was clicked before reading finished ("No receipt attached"). |
| 10 | Pass | Search works; no match shows "No items match." with "Clear filters". |
| 11 | Partial | The "Expired" filter narrows correctly and "Clear all" restores. **The "May be covered" filter didn't narrow** (both "Expiring soon" items stayed). |
| 12 | Pass | /items/01a19987-a8e5-7d54-943b-9dba2943cfda |
| 13 | Pass | Bob sees only his own 3 items. |
| 14 | Pass | Carol's item URL as Bob: "Not found." No data leaked. |
| 15 | Pass | "R7 Kettle" $19.00, Best Buy, no brand; category auto-set to Small appliances; "15 days left". |
| 16 | Pass | Carol searching "Kettle": "No items match." |
| 17 | Pass | "Delete this item? R7 Toaster and its coverage and files are removed. This cannot be undone." Deleted; no undo (as the dialog says). |
| 18 | Pass | After reload and re-sign-in: R7 Blender 2 with its receipt is still there; Toaster gone. |

**Other observations (UAT-07)**
- Upload: the Upload button can be clicked while the document is still being read, and the file is then silently dropped. Reading plus upload takes about 22 s with no progress indicator on Upload.
- The manufacturer warranty suggestion is unticked by default when "Unconfirmed", so users can easily save without it.
- No other page took more than 3 s; sign-in ~2 s; New Items ~2.8 s.
- Test data left: Carol has "R7 Blender 2" (with receipt); Bob has "R7 Kettle".
