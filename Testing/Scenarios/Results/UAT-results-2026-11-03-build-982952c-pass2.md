# StuffIt UAT results: build 982952c, pass 2
**Build:** commit 982952c, Staging (the same build as pass 1; the build watch still read 982952c at 4:22 AM ET).
**Run:** Nov 3, 2026, about 1:41 AM to 4:28 AM ET (pass 1 ran Nov 2–3, about 9:30 PM to 1:36 AM ET). Plans are FS-22 and FS-24 to FS-42 from the merged Full Scenarios set, in the same order as pass 1. DB Stager reset the accounts before each plan; the simulated clock was reset to offset 0 after every clock plan.
**Why a second pass:** requested to repeat the full suite on the same build, to check for flaky results and to confirm the earlier findings.
**Not run (same as pass 1, except FS-28):**
- FS-23 and FS-18–21 are deferred until built.
- FS-22 steps 7–8 are deferred (no share checkbox).
- FS-25 steps 5, 6, 7 and 11 (they need the accounts not to exist).
- FS-27 steps 14, 17, 18 and 20 (deleting Bob needs your explicit OK; step 14 depends on the download).
- FS-28 steps 14–18 (optional API checks; no Ops or Bob token). Steps 1–3 were **run** this time (pass 1 skipped them).
- Each plan's "not built" items, per your note.

**Grading notes applied:** FS-41 uses the live reader, so a reader miss is Partial and what it read is quoted. A plan with no printed start date that shows the purchase date, with no "receipt does not say" note, is cosmetic. FS-40 steps 7–8 fail if the Cloudinary PDF/ZIP delivery setting is off; this is called out below.

## Totals
**Pass 2: 286 Pass, 31 Partial, 13 Fail, 15 Not run (345 steps).**
**Pass 1: 278 Pass, 34 Partial, 15 Fail, 18 Not run (345 steps)**, counted from pass 1's per-step tables.
Change: Pass +8, Partial -3, Fail -2, Not run -3.
*Count note:* the pass-1 report's headline said 279 Pass, but its FS-28 row listed 10 Pass where the step table has 9 Pass (steps 4–8 and 10–13), plus 3 skipped and 5 not run. Recounted, pass 1 is 278 Pass. Pass-1 "Not run" counts skipped steps 1–3 of FS-28 as not run (18 in all).

## Storage (Cloudinary) failures — check the PDF/ZIP delivery setting
Same as pass 1: every PDF or ZIP download fails, which fits the Cloudinary "PDF and ZIP files delivery" setting being off. DB Stager has no access to that setting, so it **could not be confirmed**. These are storage settings, not app code.
- **FS-40 steps 7–8:** the export download gives HTTP 500 (`/api/exports/<id>/download`) and the PDF receipt view gives HTTP 500 (`/api/documents/<id>/content`, "Could not open that file.").
- **FS-27 step 13 and FS-37 step 19:** "Prepare my download" shows Ready, then "That download is no longer available. Prepare a new one."
- In pass 1 the export failed silently in FS-40 step 7; in pass 2 the message "That download is no longer available. Prepare a new one." is shown again.
Image files (JPG/PNG) still upload, view and delete fine (FS-31 step 12, FS-26 step 10).

## Summary by plan
Counts show pass 2, with the change from pass 1 in brackets when it differs. "Pass 1" gives Pass/Partial/Fail/Not run.

| Plan | Area | Pass | Partial | Fail | Not run | Pass 1 (P/Pa/F/NR) | Headline |
|---|---|---|---|---|---|---|---|
| FS-22 | Shared policy, private purchases | 6 | 0 | 0 | 2 | 6/0/0/2 | Privacy holds. No end date before saving (cosmetic). Same. |
| FS-24 | Clock and reminders | 9 | 1 | 0 | 0 | 9/1/0/0 | Refund, claim and Mark returned still offered after the window ends. Same. |
| FS-25 | Account lifecycle and email | 13 | 0 | 0 | 4 | 13/0/0/4 | No enumeration; only the newest reset link works. Same. |
| FS-26 | Purchases, items and privacy | 17 | 2 | 0 | 0 | 17/2/0/0 | Same two Partials. The extra "smartphones" suggestion row from pass 1 is gone. |
| FS-27 | Cards, notifications, export | 13 | 1 | 2 | 4 | 13/1/2/4 | Same totals. The card notice now shows in the bell (step 1 Partial, step 6 Pass). Export still fails (storage). |
| FS-28 | Admin two-step and shared data | 12 (+3) | 1 | 0 | 5 (-3) | 9/1/0/8 | Steps 1–3 (two-step enrolment) were run this time and passed. Pass-1 recount: 9 Pass; see the count note under Totals. |
| FS-29 | Returns in progress | 20 | 1 | 0 | 0 | 20/1/0/0 | No days-left badge on return rows. Same. |
| FS-30 | Insurance | 18 | 1 | 2 | 0 | 18/1/2/0 | Still no over-limit note or "not advice" line. Same. |
| FS-31 | Extended warranty plan | 17 | 3 | 0 | 0 | 17/3/0/0 | An item still says "Ends today" for a plan ended today. Same. |
| FS-32 | To-dos | 13 | 1 | 0 | 0 | 13/1/0/0 | Reminder does not name the item. Same. |
| FS-33 | What to track | 15 | 1 | 0 | 0 | 15/1/0/0 | A $25.98 line is never demoted. Same. |
| FS-34 | Color themes | 15 | 0 | 0 | 0 | 15/0/0/0 | Clean. Same. |
| FS-35 | Send feedback | 17 | 0 | 0 | 0 | 17/0/0/0 | Clean; limit of 5 per hour works. Same. |
| FS-36 | Claim guidance wizard | 16 (+1) | 2 (-1) | 1 | 0 | 15/3/1/0 | Step 5 Partial → Pass (colour now verified). Wizard still loses its answers on reload. |
| FS-37 | Money recovered | 16 | 2 | 2 | 0 | 16/2/2/0 | Same. A session drop was seen once in step 17 (not reproduced). |
| FS-38 | Admin feedback queue | 16 | 0 | 0 | 0 | 16/0/0/0 | Clean. Same. |
| FS-39 | Daily digest | 16 | 0 | 0 | 0 | 16/0/0/0 | Works. Possible gap if the 3-day lead passes between runs. Same. |
| FS-40 | Fix retests | 11 (+3) | 4 (-2) | 2 (-1) | 0 | 8/6/3/0 | Step 2 Fail → Pass; steps 10, 13 Partial → Pass. Steps 7–8 still storage (HTTP 500). |
| FS-41 | Receipt plans, stated warranties (live reader) | 8 | 8 | 3 | 0 | 8/8/3/0 | Identical. Reader misses are graded Partial, with what it read quoted. |
| FS-42 | Policy note, source link, to-dos, polish | 18 (+1) | 3 | 1 (-1) | 0 | 17/3/2/0 | Step 21 Fail → Pass (with a time-of-day caveat). |
| **Total** | | **286** (+8) | **31** (-3) | **13** (-2) | **15** (-3) | 278/34/15/18 | 345 steps in both passes |

## What changed since pass 1
**Improvements (8 steps moved up, 3 more steps now run):**
- **FS-40-2 Fail → Pass:** an overdue to-do now reads "Overdue since Dec 3, 2026" on the item and on /todos.
- **FS-40-10 Partial → Pass:** the nested feedback link keeps the same `from=` URL ("Page you were on: /items"); no `from=…from=…`.
- **FS-40-13 Partial → Pass:** Work gloves ($25.98) stays in the main list and now carries the "Under $50" label.
- **FS-42-21 Fail → Pass (caveat):** "Return in progress since Nov 3, 2026…" is right. The run was at about 4 AM ET, when the ET and UTC dates are the same, so pass 1's failure (the UTC date after 7 PM ET) can't be reproduced at that hour. The time-zone fix is **unconfirmed**; retest after 7 PM ET.
- **FS-36-5 Partial → Pass:** the red-on-pink "no longer own it" warning is now verified.
- **FS-28 steps 1–3 now run and Pass:** enrolling Ops in two-step works (QR, key, first code accepted, 10 recovery codes shown). Not run in pass 1.
- **Better, but the grade stays the same:** FS-40-1 now hides "Start a return" after the window ends (Refund, "Start a refund or claim" and Mark returned are still offered). FS-42-1 the store dropdown now offers the existing "New Balance". FS-26-3 and FS-29-1 no longer show the extra "smartphones 14 days Likely" / "major appliances 2 days Likely" rows.

**Regressions:** none by grade. Small differences worth knowing:
- **FS-41-4:** Save on the full Add form with nothing ticked now does nothing with no message (pass 1 said "Tick at least one policy…").
- **FS-27-1:** the bell now shows a standing "Add a credit card and confirm its benefits" notice ("1 to do"), but /notifications says "You are all caught up", so the bell and the page disagree (the step is now Partial, and step 6 is Pass; totals are unchanged).
- **FS-37-17:** after the refund was saved, one Home reload dropped Bob to the sign-in page (session lost). Not reproduced. The Fail itself is unchanged.
- **FS-36-13:** the protection plan route now reads "Applies" (pass 1 said "Might apply"). Not graded as a regression.

**New findings or notes:**
- **FS-40-12:** the upload note now says "1 more line is under Smaller things", but there are 8 lines under Smaller things, and the reason reads "much cheaper than the rest" rather than "Cheaper than the lines kept".
- **FS-40-14:** sign-up for a taken address takes about 0.96 s and for a new address about 1.43 s, a steady ~0.47 s gap (pass 1: about 0.5 s). The page is identical, but a timing leak is likely.
- **FS-39 (UI display):** Settings > Profile showed the time zone as "Not set (UTC)" until a time of day was set, and again after it was cleared, while DB Stager reports Alice's stored time zone as America/New_York. This is a UI display bug, not a stored-value problem; reminder timing behaved as New York.
- **FS-39-4:** the first reminder run gave Sent = 0 because the app time (3:28 AM ET) was before the 9:00 AM default; with Time of day set to 01:00 it sent.
- **FS-32-12:** the to-do reminder went out at real time (2:44 AM ET, "To do tomorrow"), not held to 9:00. The email and bell entry still don't name the item, and the unsubscribe category is still `purchase_needs_info`.
- **FS-41:** the generator receipt now says "Not added by a quick add:" with nothing after the colon. Reads over 20 s again: 21-bestbuy (about 23.6 s), 15-bestbuy-tv (about 24.6 s), 12-thermal (over 25 s).
- **FS-35-2:** the Send feedback page shows "App version: unknown" for a moment before "982952c" (harmless).
- **FS-34:** a single 504 Gateway Timeout on the sign-in page's first request (it loaded on retry).
- **FS-38-1:** the customer-side "What will be sent" shows the item **id** ("Item: 01a1a0b9-…"), not its name. Same in pass 1 (FS-35-3), so not new; the admin detail shows the name.
- **FS-42-17:** setting a file on an item opens a document reading, and after "Not now" the file wasn't attached until a reload and retry.

**Unchanged since pass 1** (everything not listed above): no "Is yours one of these?" card match (FS-27-4); no over-limit note on insurance (FS-30-11/12); "Ends today" plan still treated as running (FS-31-18, FS-40-6); no verified filter and the "Brand (maker)s" typo (FS-28-9); no days-left count on return rows (FS-29-7); the wizard loses its answers on reload (FS-36-7); Home hides the Recovered card when every item is returned (FS-37-17); a full Add drops receipt plans and stated warranties (FS-41-3/4/11); the "usual window" note shows on a Confirmed policy and is missing on the saved item (FS-42-5, FS-42-3); Work gloves is never demoted (FS-33-3); "Update from a newer document" lists every value (FS-31-15).

## Open Fail list (13)
| Step | What fails | Note |
|---|---|---|
| FS-27-4 | No "Is yours one of these?" prompt for an unknown card | Same as pass 1 |
| FS-27-13 | Data export download gives "That download is no longer available" | Storage (PDF/ZIP delivery) |
| FS-30-11 | No over-limit note or "not advice" line on the policy page | Same |
| FS-30-12 | No over-limit note on the item's insurance card | Same |
| FS-36-7 | The wizard resets to step 1 on reload (the plan only says to record it) | Same |
| FS-37-17 | Home shows no Recovered card when every item is returned | Same; one session drop seen |
| FS-37-19 | Recoveries export can't be downloaded | Storage |
| FS-40-7 | Export download gives HTTP 500 | Storage |
| FS-40-8 | PDF receipt view gives HTTP 500 | Storage |
| FS-41-3 | No "Add Details" control for a receipt plan | Same |
| FS-41-4 | A full Add drops the Geek Squad plan | Same; new silent no-op on empty Save |
| FS-41-11 | An item with only a stated warranty can't be created | Same |
| FS-42-5 | "Usual window" note shows on a Confirmed policy | Same |

Pass 1 had 15 Fails: FS-40-2 and FS-42-21 are now Pass. The remaining 13 are the list above.

---
# Per-plan detail (pass 2)
Each section below is the pass-2 results file for that plan. "vs pass 1" columns appear where the plan was written with one.


# FS-22 — Shared policy vs private purchase — build 982952c (Staging), pass 2
Mode: Full. Run 1:41–1:43 AM ET, Nov 3, 2026, after the full pre-run reset. Steps 7–8 deferred (no share checkbox).

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | Alice, New Balance, Oct 30: "New Balance return policy · Merchant · 30 days · Unconfirmed", "Usual window, can differ for your item. Check your receipt.", Source link https://www.newbalance.com/returns. Unticked by default ("Not added. Tick it to add it when you save…"). Saved: "Oct 30, 2026 to Nov 29, 2026 · 26 days left". The note isn't kept on the saved item (Source is). No dates shown before saving (cosmetic, same as pass 1). |
| 2 | Pass | Bob, Nov 1: same policy and note; saved "Nov 1, 2026 to Dec 1, 2026 · 28 days left". |
| 3 | Pass | The same terms text and source on both; the link opens https://www.newbalance.com/returns/. |
| 4 | Pass | Alice's end changed to Dec 15: "Oct 30, 2026 to Dec 15, 2026 · Until Dec 15, 2026". |
| 5 | Pass | Bob's is unchanged: "Next to end: Return window, Dec 1, 2026 · 28 days left". |
| 6 | Pass | Nothing exposes other users. Searching for "UAT NB Bob" gives "No items match."; Bob's item URL gives "Not found." (Returns page = "First design: example data".) |
| 7–8 | Deferred | No share checkbox. |

**Summary:** 6/6 Pass; same as pass 1.


# FS-24 — Time travel: a return window ends and the reminder arrives — build 982952c (Staging), pass 2
Mode: Full (browser plus maintenance API plus Gmail). Run 1:45–1:47 AM ET, Nov 3, 2026. Alice reset clean with default notification preferences. Calls are in `fs24-calls.log`.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | "UAT24 Clock Shoes", New Balance, Nov 3, with the 30-day policy ticked: "Next to end: Return window, Dec 3, 2026 · 30 days left". |
| 2 | Pass | Return window closing and Warranty expiring: Email and In-app on, "At once" (defaults). |
| 3 | Pass | GET clock: "Offset 0 day(s)". |
| 4 | Pass (deviation) | +20: Sent 0 (the leads are 7/3/1, not 10). +3 (Nov 26, before 9:00): Sent 0. +1 (Nov 27): **Sent 1**. |
| 5 | Pass | Email "UAT24 Clock Shoes: return window ends in 6 days", "The return window on UAT24 Clock Shoes ends in 6 days, on December 3, 2026." View item opens the item's own URL. |
| 6 | Pass | Bell "Notifications, 1 unread, 1 to do". /notifications shows the same title and body, "Nov 27, 2026, 1:45 AM · just now", "Unread". View item opens the item; it is then read ("Mark unread"). Home: "1 Return windows closing… UAT24 Clock Shoes — Return window · 6 days". |
| 7 | Pass | Second run the same day: Sent 0. |
| 8 | Pass | +7 (Dec 4): Sent 0, Cancelled 2. No new notification. |
| 9 | Partial | "Expired", "Coverage ended · 1 policy", "Ended Dec 3, 2026"; /items "All coverage has ended"; Home all 0. **Still offered after the window ended:** "Refund", "Start a refund or claim", "Mark returned", "Mark refunded". The bell keeps "1 to do" (the credit-card notice; see FS-32). |
| 10 | Pass | clock/reset: back to offset 0. |

Every screen followed the simulated clock.
**Summary:** 9 Pass, 1 Partial; same as pass 1.


# FS-25 — Create two accounts, confirm by email, sign in, recover a password — build 982952c (Staging), pass 2
Mode: Full (browser plus Test1 Gmail). Run 1:48–2:02 AM ET, Nov 3, 2026, after a DB Stager reset (tokens cleared). Both accounts already exist, so steps 5–7 and 11 are not run. The changed Test1 password is kept in a secret file referenced from `RUN-CONFIG.env`, not in this report. DB Stager's next reset restores the original.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | `/login?returnUrl=%2F`, "Sign in · WarrantyBank". |
| 2 | Pass | /terms "Terms of Service", /privacy "Privacy Policy", /disclaimer "Disclaimer"; "Version 2026-10-01 · last updated October 1, 2026"; draft banner; no sign-in wall. |
| 3 | Pass | "Enter a valid email address.", "Use at least 10 characters.", "Please agree to continue."; nothing created (Confirm password shows no message). |
| 4 | Pass | A short password gives "Use at least 10 characters."; `abc` gives "Enter a valid email address.". |
| 5–7 | Not run | The account exists. |
| 8 | Pass | Sign out, then Back and reload show only the Sign in form. |
| 9 | Pass | "Invalid email or password." for both a real and an unknown email. |
| 10 | Pass | Home ("Welcome, QA"); nav Home, My Items, New Items, Returns, Notifications. |
| 11 | Not run | The account exists. |
| 12 | Pass | Neutral "Check your email / We sent a link to <email>… Nothing is created until you do."; the inbox gets "You already have a WarrantyBank account" (06:49:25Z). |
| 13 | Pass | "If that email is registered, we sent a link to reset your password. It may take a minute to arrive." (1:49:41 AM ET; email at the same second). |
| 14 | Pass | "Choose a new password" leads to "Your password was changed. Sign in with the new one."; the new password works and the old one gets "Invalid email or password." |
| 15 | Pass | Reuse: the form renders, then "This link has already been used or has expired. Request a new one." (Minor: no warning before typing.) |
| 16 | Pass | The unknown address gets the identical neutral message. |
| 17 | Pass | Requests at 2:00:36 and 2:01:15 AM ET (more than 10 min after step 13), both in one Gmail thread. The older one has no "Requested at"; the newest says "Requested at 2:01 AM. If you asked more than once, use the newest email." (ET). The older link is refused ("This link has already been used or has expired. Request a new one."); the newest changes the password, and sign-in lands on Home. |

**Summary:** 13 Pass, 0 Partial, 0 Fail, 4 Not run; same as pass 1.


# FS-26 (pass 2): Add purchases, check suggested coverage, browse items, prove privacy
Build 982952c (Staging). Run 2026-11-03, about 2:05-2:10 AM ET. Users: Alice (Test1) and Bob (Test2). Clean reset before the run (DB Stager).

| Step | Result | Notes |
|---|---|---|
| 1 | Partial | `/add/new`. Field order: Store, Date, "Credit card used", "Order number", then **Category**, "Brand (optional)", "Item", "Model number". The plan expects category, brand, then item name; here Category comes before Brand, and the field is labelled "Item". Price is under "More about this item: price, size, serial number, notes" (matches). Same as pass 1. |
| 2 | Pass | "Add at least one item." / "Tell us what you bought." Nothing was saved. |
| 3 | Pass | "Best Buy return policy · Merchant · 15 days · Confirmed" was pre-ticked, with "Usual window, can differ for your item. Check your receipt." and a bestbuy.com Source link. "Ninja warranty · Manufacturer · 1 year · Unconfirmed" was not ticked ("Not added. Tick it to add it when you save…"), so I ticked it. Category was filled in automatically as Small appliances. Saving opened the item. Pass 1's extra "smartphones 14 days Likely" row did not appear. |
| 4 | Pass | Read-only. "Bought Nov 3, 2026 from Best Buy", $89.99, badge "Expiring soon" at 15 days left. |
| 5 | Partial | The return window reads "Nov 3, 2026 to Nov 18, 2026 · 15 days left", which is correct. The warranty reads "Nov 3, 2026 to Nov 3, 2027 · Until Nov 3, 2027", which is correct but shows no days-left count. The usual-window note is not on the saved item, and there is no confidence score. Stale Best Buy text: "(2025 season: through January 15, 2026)". The warranty terms are a placeholder. Same as pass 1. |
| 6 | Pass | Edit changes to Done. Edit item and Edit purchase; Edit and Remove on each coverage; Add coverage and Suggest coverage; Money recovered; To do; Receipts and files; Start a return. |
| 7 | Pass | Renamed to "UAT Blender 2". The new name shows on the item and in My Items. |
| 8 | Pass | Saved as "Bought Oct 2026 (approximate) from Best Buy", Needs info. The return was blocked: "This return window ended 2026-10-30, so it cannot be added." Policies reads "Not set up yet". Oddity: pressing Enter in the Store field picked "AJ Madison". |
| 9 | Pass | While the document was read, Upload was disabled with the tooltip "Wait until the document has been read". "What we found in your document" showed a store conflict (Best Buy against UAT TEST STORE, high confidence) and Order total 89.99. "Not now" kept Best Buy. |
| 10 | Pass | "Receipt / test-receipt.jpg (4 KB)" (7 KB before upload). View opened the 600×400 image. |
| 11 | Pass | "Toaster" and "Blender" each matched one item. "zzzqqq" showed "No items match." with Clear filters. |
| 12 | Pass | The Needs info filter showed only the Toaster. Clear restored both. |
| 13 | Pass | `/items/01a1a039-a9a9-7234-8790-804ddb6aef60` |
| 14 | Pass | Bob: "Nothing here yet … Add your first purchase." |
| 15 | Pass | Bob on Alice's URL saw "Not found.", tab title "Item · WarrantyBank". Nothing of Alice's leaked. |
| 16 | Pass | Bob's UAT Kettle (Target, $19.00): "Bought Nov 3, 2026 from Target", "Try first: Return window · Target", until Feb 1, 2027 (the holiday window). |
| 17 | Pass | Alice's search for "Kettle" shows "No items match." |
| 18 | Pass | "Delete this item? UAT Toaster and its coverage and files are removed. This cannot be undone." with "Delete item". The item left the list. No Undo was offered (the plan allows this). |
| 19 | Pass | After a reload and after signing out and back in, only UAT Blender 2 is listed. |

**Summary:** 17 Pass, 2 Partial (1, 5), 0 Fail. Same as pass 1.


# FS-27 (pass 2): Cards, notifications and preferences, data export
Build 982952c (Staging). Mode: Full (browser plus the Test1 inbox). Run 2:11-2:16 AM ET, Nov 3, 2026, after a DB Stager reset. Alice had "UAT Blender 2" staged; Bob was brand new.
**Steps 17, 18 and 20 were not run.** They delete Bob's account, which needs Steve's explicit OK.

| # | Result | Evidence |
|---|---|---|
| 1 | Partial | **New since pass 1:** the bell now shows the standing notice "Add a credit card and confirm its benefits: Your credit card can add warranty time and purchase protection to what you buy…", with "I don't use credit cards", and the bell reads "Notifications, 1 to do". But the /notifications page still says "You are all caught up.", so the bell and the page disagree. |
| 2 | Pass | Chase Freedom Unlimited, UAT Card, 4242: "UAT Card / XXXX-XXXX-XXXX-4242 / Chase Freedom Unlimited", with both benefits. |
| 3 | Pass | Both benefits are "Confirmed Nov 3, 2026". The label is Confirmed, not verified or unverified. |
| 4 | **Fail** | "UAT Mystery Rewards Card" (Citibank, 0001) is saved as "UNVERIFIED / ⚠ No policy added". There is **no "Is yours one of these?" prompt**, during the add or on the detail page. Same as pass 1. |
| 5 | Pass | "Your card UAT Card already ends in 4242. Receipts ending in 4242 are matched to that first card, so these digits were not added." No error page. |
| 6 | Pass | Once the Chase card with confirmed benefits was added, the bell went from "1 to do" to "You are all caught up." That is consistent. (Pass 1: Partial, because the notice never appeared.) |
| 7 | Pass | Groups: Expiring, Purchases, Summaries, Account, System alerts, Product news. Each type has Email, In-app and Text ("Text messages are coming soon"). "Account and security" and "Your files and data" are Required and locked. The Expiring types have an "At once"/"In my daily digest" choice. |
| 8 | Pass | Warranty expiring Email turned off ("Saved"); Return window closing Email stayed on. Both persisted after a reload. |
| 9 | Pass | /settings/profile: "Email: [Test1 address] (confirmed)" as plain text, not editable. |
| 10 | Pass | /todos: "Nothing to do right now." /returns: "First design: example data", showing sample Sony, Ninja, Keurig and Bosch returns. |
| 11 | Pass | The pass-2 FS-24 reminder arrived at 1:45 AM ET: "UAT24 Clock Shoes: return window ends in 6 days". It names the item and the date (December 3, 2026, simulated clock) and has Manage and Unsubscribe links. |
| 12 | Pass | "Email preferences. You are getting emails about Return window closing. What would you like to stop?" It offers just this type, all Expiring, or all optional emails. After Unsubscribe: "Done. No more "Return window closing" emails. Required notices about your account, payments and security still reach you." Settings agrees that it is off. |
| 13 | **Fail** | "Prepare my download" went to "Being prepared", then "Ready until Nov 10, 2026", "Download (4 KB)". Clicking Download gives "**That download is no longer available. Prepare a new one.**" Retrying did the same. This is the same storage-delivery failure as FS-40 step 7 (Cloudinary PDF/ZIP delivery appears to be off). |
| 14 | Not run | No file (blocked by step 13). |
| 15 | Pass | The delete warning lists what is removed and ends "Download your data first if you want a copy." It requires the email and the password, and the button stays disabled until both are filled. Not submitted. |
| 16 | Pass | No Cancel button. Leaving the page deleted nothing; Bob is still signed in with both cards. |
| 17, 18, 20 | Not run | Needs Steve's OK to delete Bob. |
| 19 | Pass | Alice's UAT Blender 2 is still listed. |

**Summary:** 13 Pass, 1 Partial (1), 2 Fail (4, 13), 4 Not run (14, 17, 18, 20).
Compared with pass 1: the card notice now appears, but only in the bell (step 1 is now Partial and step 6 is now Pass). The totals are the same.


# FS-28 (pass 2): Administrator sign-in with two-step, and the shared data screens
Build 982952c (Staging). Mode: Full (browser). Run 2:19-2:24 AM ET, Nov 3, 2026, after a DB Stager reset. Ops's two-step was off, so steps 1-3 enrolled it fresh. The setup key and recovery codes are kept in the run config only, not in this report.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | Email and password only, then `/settings/security`, "Two-step sign-in": "Administrator accounts need two-step sign-in before any admin screen opens. It adds a code from your phone to your password." |
| 2 | Pass | QR alt text "QR code to add WarrantyBank to your authenticator app", "Or type this key" with the key, a "6-digit code" field and "Turn on". |
| 3 | Pass | The first code was accepted. "Two-step sign-in is on. Save these recovery codes now." showed 10 codes, "Download as a file", the tickbox and Done. Then "You have 10 recovery codes left…". Administrators: <admin address> "Two-step on", Ops (you) "Two-step on", stuffit-<admin address> "Two-step not set up". (These steps were skipped in pass 1.) |
| 4 | Pass | `/admin`: ADMIN badge; Review, Companies, Shared data, Feedback; "Customer view". |
| 5 | Pass | "Enter your authenticator code." Field "Authenticator code", hint "The 6 digits from your authenticator app, or one of your recovery codes." |
| 6 | Pass | `000000` gives "That code is not correct." |
| 7 | Pass | Lands on `/admin`, "Shared data". |
| 8 | Pass | Customer view goes to `/` ("Welcome, QA", customer navigation); Admin view returns to `/admin`. |
| 9 | Partial | "Shared stores, brands and issuers". The Show filter still has the typo **"Brand (maker)s"**. Home Depot is "Verified Store"; Milwaukee is "Not verified Brand"; the private UAT TEST STORE gives "Nothing matches." **No row count**, about 200 rows render (looks like a cap), and no verified-only filter. Same as pass 1. |
| 10 | Pass | `/admin/parties/01a0f4e4-…` Home Depot: "Everything else" 90 days and "Major appliances" 2 days, both Current and "Verified: Checked against the official source on Oct 24, 2026.", with Source links to homedepot.com/c/Return_Policy, "Correct a mistake" and "This no longer applies". |
| 11 | Pass | Companies: the type list (Credit cards and Extended warranty sellers "not built yet") with "Find return policy". Review: "Not built yet. Planned in S7.1.2…". Feedback: "0 new · 0 shown", "No messages match." |
| 12 | Pass | Bob: no Admin badge, no Admin view, no Security tab. |
| 13 | Pass | Bob's `/admin`, `/admin/companies`, `/admin/review` and `/admin/feedback` all go to `/`; `/settings/security` goes to `/settings/profile`. No admin data. |
| 14-18 | Not run | API steps (optional), as in pass 1. |

**Summary:** 12 Pass, 1 Partial (9), 0 Fail; 5 not run (14-18, optional API). Compared with pass 1, steps 1-3 were run and passed this time.


# FS-29 (pass 2): Start a return, work the returns list, mark it returned
Build 982952c (Staging). Mode: Full (browser). Run 2:23-2:28 AM ET, Nov 3, 2026, after a DB Stager reset (nothing staged).

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | Drill and Saw (Home Depot, "Merchant · 90 days · Confirmed") and Kettle (Target, the same), each with "Usual window, can differ for your item." and a Source link. Category was filled in automatically (Power tools / Small appliances). Each item shows "Until Feb 1, 2027" (Nov 3 + 90 days, correct). Pass 1's extra "major appliances 2 days Likely" row did not appear. |
| 2 | Pass | "Returns in progress" / "Nothing to return right now. Open an item and choose Start a return; it will show up here until you mark it returned." |
| 3 | Pass | "Start a return" is on all three items. |
| 4 | Pass | "Return in progress since Nov 3, 2026. It is on your returns list until you mark it returned." with Mark returned and Cancel return. Still Active, coverage unchanged, and Start a return is gone. |
| 5 | Pass | The note persists after a reload. |
| 6 | Pass | Same note on the Saw and the Kettle. |
| 7 | **Partial** | The order is Drill, Kettle, Saw (all end Feb 1, 2027). The rows read "UAT Return Drill / Until Feb 1, 2027 / Home Depot · Bought Nov 3, 2026 · $120.00 / Return window ends Feb 1, 2027". **No days-left badge.** Same as pass 1. |
| 8 | Pass | "Home Depot 2 items · $200.00" and "Target 1 item · $30.00". The store leaves the row text, and unticking restores the list. |
| 9 | Pass | The Kettle row opens the item. |
| 10 | Pass | The note goes, Start a return is back, and there is no "The return" summary. |
| 11 | Pass | Drill and Saw only. |
| 12 | Pass | "Mark as returned": Date 2026-11-03, Refund 120 ("Leave empty if the money has not come back yet."), Paid back by (Not sure / not yet, Back to the original payment, Store credit, Gift card, Exchange, Cash, Check, Other), How hard 1-5, Problems getting paid. |
| 13 | Pass | Submit is disabled with the date empty. |
| 14 | Pass | "Returned Nov 3, 2026 / Refund $100.00 · Store credit / How hard 2 of 5 · Fairly easy / Problems Restocking fee". Status Returned. Money recovered: "$100.00 · Store refund · … · credit, not cash". |
| 15 | Pass | Mark returned and Start a return are gone; "I have it again" is offered. Nothing about reminders; the coverage still shows. |
| 16 | Pass | Only the Saw. |
| 17 | Pass | "Refund $110.00 · Store credit"; Money recovered also shows $110.00. |
| 18 | Pass | Active again and not on the list. "The return" summary and the Money recovered entry are removed ("Nothing recorded yet."). |
| 19 | Pass | Bob sees "Nothing to return right now."; nothing of Alice's. |
| 20 | Pass | Bob on Alice's Saw URL: "Not found.", tab title "Item · WarrantyBank". |
| 21 | Pass | "Returned Nov 3, 2026 / Refund Not paid yet". |

/returns (from the menu) is still "First design: example data" (Sony, Ninja, Keurig, Bosch); none of Alice's items appear.
**Summary:** 20 Pass, 1 Partial (7), 0 Fail. Same as pass 1.


# FS-30 (pass 2): Record a renter's policy, link items, see the notes on the item
Build 982952c (Staging). Mode: Full (browser plus the live document reader). Run 2:27-2:33 AM ET, Nov 3, 2026, after a DB Stager reset that staged Alice's UAT Guitar ($1,800), UAT Laptop ($1,200) and UAT Lamp ($40) as Best Buy purchases. Steps 4 and 20 were re-tested with a second policy, because step 20 first ran after the delete.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | "Insurance" / "No policies yet." / "Add your first policy". |
| 2 | Partial | Nothing was saved, but only "Choose the insurer." is flagged. Same as pass 1. |
| 3 | Pass | Inline `Add "UAT Insurer"` gives the insurer "UNVERIFIED" ("Only you can see this insurer until it is verified."). |
| 4 | Pass | The field error "The end date cannot be before the start." appears under Ends, plus the banner "One or more validation errors occurred." Nothing saved. (Accessibility note: the input has no aria-invalid or aria-describedby tying it to the error.) |
| 5-6 | Pass | Amounts accepted. The blank third limit row is ignored silently; the two real limits are kept. |
| 7 | Pass | Saved; it opens read-only at `/insurance/01a1a04e-…`. |
| 8 | Pass | "Renter's · UAT Insurer · policy UAT-001", "Until May 3, 2027", Term "May 3, 2026 to May 3, 2027 · renews automatically", "$240.00 a year", $500.00, $20,000.00, `tel:800-555-0100`, "Make a claim online", "Electronics: $2,500.00", "Musical instruments: $1,500.00". |
| 9 | Pass | "3 items, which cost $3,040.00." (correct) / "No exceptions: every item is covered." |
| 10 | Pass | "UAT Guitar — Covered, under Musical instruments ($1,500.00), listed at $1,800.00". |
| 11 | **Fail** | **No notes on the policy page**: no over-limit note for the $1,800 Guitar against the $1,500 limit, and no "not advice" line, even after a reload. Same as pass 1. |
| 12 | **Fail** (the note only) | The card shows "Deductible $500.00. Limit for Musical instruments: $1,500.00. Listed on the policy at $1,800.00.", Call 800-555-0100 and "Make a claim online", but **no over-limit note**. |
| 13 | Pass | The Lamp's card shows the policy and "Deductible $500.00.", with no instrument limit. (It doesn't mention that the $40 lamp is below the deductible.) |
| 14 | Pass | "2 items, which cost $3,000.00."; the Lamp shows "Left out" and its Insurance card is gone. |
| 15 | Pass | "Only the items you link below: 1 item, which costs $1,800.00." |
| 16 | Pass | "$240.00 a year for the policies still running." / "UAT Renter's policy — Until May 3, 2027 — Renter's · UAT Insurer · covers 1 item · $500.00 deductible · renews automatically". |
| 17 | Pass | Reader on. "Reading your document…" with the button disabled. All 11 values were correct, with quotes and page numbers (UAT Mutual Insurance Co., UAT-777, Renters, 2026-05-01 to 2027-05-01 marked "Check this one", $180 a year, $250, $15,000, Jewelry $1,000, 800-555-0199). "The document did not say: Items listed separately, Claim website." Nothing was filled in beforehand. |
| 18 | Pass (oddity) | Only Policy number filled ("UAT-777"), with the note "Filled in from your document…". Oddity: Name became "Renter's policy" without being accepted, and all suggestions are pre-ticked tick boxes. Same as pass 1. |
| 19 | Pass (gap) | Navigating away shows "Leave without saving? … they will be lost." (Stay / Leave). Gap: the form's own Cancel discards typed changes with no warning. Same as pass 1. |
| 20 | Pass | Bob's /insurance is empty. On Alice's live policy URL (retest, policy still present) he sees "← Insurance / Not found.", tab title "Policy · WarrantyBank", and nothing of Alice's. |
| 21 | Pass | "Delete this policy? This removes UAT Renter's policy, its limits, its documents and its link to your items. The items themselves stay." The list is empty and the Guitar has no Insurance card. |

No wrong amounts, no wording that reads like advice to buy, and no date that disagrees with today.
**Summary:** 18 Pass, 1 Partial (2), 2 Fail (11, 12). Same as pass 1.


# FS-31 (pass 2): Record a third-party warranty plan and cover items with it
Build 982952c (Staging). Mode: Full (browser plus the live document reader). Run 2:36-2:40 AM ET, Nov 3, 2026, after a DB Stager reset that staged Alice's UAT Fridge ($900) and UAT Washer ($600) as Best Buy purchases.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | "Extended warranties" / "No plans yet." / "…A plan bought at the store for a single item is added on that item instead." / "Add your first plan". |
| 2 | Partial | Nothing was saved, but only the banner "Choose the company that sold the plan." appears; Name and Ends are not called out. Same as pass 1. |
| 3 | Pass | Inline `Add "UAT Home Warranty Co"` gives the company "UNVERIFIED". |
| 4 | Pass | "The end date cannot be before the start." under Ends, plus the banner "One or more validation errors occurred." Nothing saved. |
| 5-6 | Pass | Saved; it opens read-only at `/plans/01a1a056-…`. |
| 7 | Pass | "Sep 3, 2026 to Sep 3, 2027"; "$30.00 a month ($360.00 a year)"; Per service call "$75.00"; `tel:800-555-0111`; "Make a claim online"; covers and "Cosmetic damage". |
| 8 | Pass | "UAT Fridge · $900.00", "UAT Washer · $600.00". |
| 9 | Pass | "$360.00 a year for the plans still running, covering items that cost $1,500.00 in all." Row: "UAT Home Warranty Co · 2 items · $360.00 a year". |
| 10 | Pass | Fridge: "Covered, 2 policies". The return window comes first ("Try this first"), then "Extended plan · UAT Home Warranty Co, Sep 3, 2026 to Sep 3, 2027 · Until Sep 3, 2027" with the claim details. |
| 11 | Pass | "Stop covering this item? UAT Washer will no longer show UAT Home protection as a coverage. The item itself stays." Then "1 item", "$900.00 in all". |
| 12 | Pass | "test-receipt.jpg (4 KB)" (7 KB before upload). View opens it. "Delete this file? test-receipt.jpg is removed. This cannot be undone." leads to "No files yet." |
| 13 | Pass | "$25.00 a month ($300.00 a year)". |
| 14 | Pass (gap) | Reader on. All values were correct (UAT Appliance Shield LLC, Appliance Shield Gold, 2026-06-01 to 2027-06-01 marked "Check this one", 19.99 monthly, fee 60, covers, exclusions, 800-555-0122). The website "www.example.com/shield" is flagged "That is not a web address starting with http or https." Nothing was filled before accepting. Gap: Cancel leaves with no unsaved-changes warning. |
| 15 | Partial | "Update from a newer document" lists **all values, not only those that differ** (the unchanged price of 25 is listed too), all pre-ticked. With only the fee accepted, it went from $75.00 to $95.00 ("Plan saved. Every item it covers is updated."); covers unchanged. v2 was attached automatically. Same as pass 1. |
| 16 | Pass | "End this plan" is disabled with the date empty. "Tell us the day it ended and every covered item stops showing it as active from then." |
| 17 | Pass | No confirmation. "Ended Nov 3, 2026"; term "Sep 3, 2026 to Nov 3, 2026". The row is dimmed (opacity 0.7), and the total is "$0.00 a year for the plans still running, covering items that cost $0.00 in all." |
| 18 | **Partial** | The Fridge still shows "Sep 3, 2026 to Nov 3, 2026 · **Ends today**", "Covered 2 policies", "Next to end: Extended plan, Nov 3, 2026 · Ends today". This contradicts the plan's "Ended" badge. Same as pass 1. |
| 19 | Pass | Bob: "No plans yet."; Alice's live plan URL shows "← Extended warranties / Not found." |
| 20 | Pass | "Delete this plan? This removes UAT Home protection, its contract files and the plan coverage on 1 item. The items themselves stay." The list is empty; the Fridge shows "Covered, 1 policy". |

All money figures are consistent ($30 × 12 = $360, $25 × 12 = $300, $900 + $600 = $1,500, fee $75 → $95).
**Summary:** 17 Pass, 3 Partial (2, 15, 18), 0 Fail. Same as pass 1 (the dimmed row is now confirmed).


# FS-32 (pass 2): General reminders on an item and on the To do page
Build 982952c (Staging). Mode: Full (browser plus email; reminder job for step 12). Run 2:43-2:47 AM ET, Nov 3, 2026, after a DB Stager reset that staged Alice's "UAT Reminder Blender" (Best Buy, today, no to-dos).

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | "To do" / "Nothing to do right now." / "Reminders such as registering a warranty show up here, and on the item they belong to." with a link to Your items. |
| 2 | Pass | Read-only item: no To do card. |
| 3 | Pass | Edit shows the To do card: placeholder "For example: register the warranty", "Due (optional)". Add is disabled while the title is empty. |
| 4 | Pass | "Register the warranty" shows "Due in 5 days" (orange, `badge-soon`); "Keep the box" has no label. A double click on Add created one reminder. |
| 5 | Pass | "Overdue since Nov 2, 2026". **The colour is neutral slate grey** (`badge-expired`), less urgent-looking than the orange due-soon badge. Same as pass 1. |
| 6 | Pass | After Done, the card stays with all three. |
| 7 | Pass | /todos lists the same three, each with a "UAT Reminder Blender" link. |
| 8 | Pass | Mark as done removes it from both pages; it shows under "Show done and dismissed (1)" with Reopen. |
| 9 | Pass | "Dismissed until Nov 10, 2026" with Undo, under the toggle. No wording says it will come back. |
| 10 | Pass | "Not applicable" with Undo (recoverable). |
| 11 | Pass | After a reload nothing returns; "Show done and dismissed (3)". The read-only item shows a To do card holding only the toggle. |
| 12 | Partial | A to-do due Nov 4. The reminder job ran at 2:44 AM ET at real time (the clock was not advanced) and sent `Todos = 1`: the email "To do tomorrow: Clock reminder test" / "Clock reminder test is due tomorrow, on November 4, 2026." / "See your to-dos". The bell entry and /notifications have the same title and body ("Needs action"). A second run sent nothing (`Todos = 0`), so it is once only. **Neither the email nor the bell entry names the item.** The unsubscribe link's category is still `purchase_needs_info`. It went out one day ahead, at 2:44 AM rather than 9:00. |
| 13 | Pass | Bob: "Nothing to do right now."; no toggle; none of Alice's reminders. |
| 14 | Pass | Bob on the Blender URL: "Not found.", tab title "Item · WarrantyBank". |

**Oddities:** the bell said "1 to do" the whole run. That count is the credit-card notice, not the to-do list, so it doesn't follow the To do page. Reminder timing: pass 1 got "To do today" after a +1 day clock jump; pass 2 got "To do tomorrow" at real time. Either way it is not held to 9:00.
**Summary:** 13 Pass, 1 Partial (12), 0 Fail. Same as pass 1.


# FS-33 — Set what is worth tracking, and New Items follows it — build 982952c (Staging), pass 2
Mode: Full (browser). Run ~2:49–2:51 AM ET, Nov 3, 2026, after a DB Stager reset (New Items empty, threshold unset).
Receipt: `12-thermal-long-many-items.pdf` (Pine Street Hardware, 12 lines).

| # | Result | Evidence | vs pass 1 |
|---|---|---|---|
| 1 | Pass | Tabs: Profile, Stores & brands, Notifications, What to track, Email, Appearance, Credit cards, Privacy & data, Plan & billing. | Same |
| 2 | Pass | "What is worth tracking"; field "Track things worth at least" = 50; note "Using the standard amount, $50.00. Zero tracks everything."; buttons Everything / Only larger purchases / Use the standard amount / Save. | Same |
| 3 | **Partial** | The upload took ~29 s (pass 1: ~25 s), within "It can take up to half a minute". "Showing 10 of 12". Main list: Work gloves · L $25.98 **with the badge "Under $50" but not demoted**, Interior paint, Deck screws, Stud. Smaller things (8), each "Under $50 · …" (used up / cord / bulb / supply line / much cheaper than the rest). | Same bug |
| 4 | Pass | Everything sets the field to 0. | Same |
| 5 | Pass | "Saving…" was shown; the final "Saved" wasn't caught here, but the reload in step 6 kept 0 and other saves showed "Saved". | Same |
| 6 | Pass | 0 is kept; the note reads "The standard amount is $50.00. Zero tracks everything." | Same |
| 7 | Pass | Smaller things (2): Wood glue and Sandpaper, "Cheaper than the lines kept". The other 10 are in the main list. | Same |
| 8 | Pass | 250; Smaller things (11) of 12; reasons "Under your $250 minimum." Work gloves again stays in the main list with the badge "Under $250". | Same |
| 9 | Pass | 100001: "Not saved" / "Choose an amount from 0 to 100,000."; 250 after reload. | Same |
| 10 | Pass | -5: the same refusal. | Same |
| 11 | Pass | A blank field is treated as the standard amount: 50, "Saved", "Using the standard amount, $50.00." | Same |
| 12 | Pass | 20: Smaller things (5) Wood glue, Sandpaper, Supply line, Tarp, Roller cover, all under $20; the 7 lines of $20 or more are in the main list. (Cosmetic: the note says "The standard amount is $50.00…" next to a custom 20.) | Same |
| 13 | Pass | Use the standard amount saves straight away (no Save click): 50, "Using the standard amount, $50.00."; Smaller things (8), "Showing 10 of 12", matching step 3. | Same |
| 14 | Pass | Alice is at 250; Bob shows 50, "Using the standard amount, $50.00." | Same |
| 15 | Pass | Bob: "Nothing waiting…", no Pine Street lines. | Same |
| 16 | Pass | Alice, signed in again: 250. | Same |

**Bug (still there):** Work gloves ($25.98) is never put under Smaller things at $50 or $250, though its badge says "Under $50" / "Under $250".
**Summary:** 15 Pass, 1 Partial (3), 0 Fail. Identical to pass 1.


# FS-34 — Color theme and light or dark — build 982952c (Staging), pass 2
Mode: Full-only (browser). Run ~2:55–3:00 AM ET, Nov 3, 2026, after a DB Stager between-scenario reset (Alice has one item, "UAT Cordless Drill"). Site data cleared first (localStorage `[]`).

| # | Result | Evidence | vs pass 1 |
|---|---|---|---|
| 1 | Pass | "Appearance"; "Color theme" Teal (selected), Indigo, Berry, each with a swatch dot; "Light or dark" "Match my device" (selected), "Light", "Dark"; "Using light because that is your device's setting."; "This choice is kept on this device. It is not yet saved to your profile, so other devices keep their own." | Same |
| 2 | Pass | Indigo applies at once with no reload (background, headings, avatar, selected option, footer brand). | Same |
| 3 | Pass | Home (redirects to /orientation, "Welcome to WarrantyBank, QA"), My Items, New Items (/add), the item page and Settings are all Indigo. Fixed colours: green "Active" / "Covered" / "Until Feb 1, 2027" badges, blue "Link your email", amber "Add an item". These look deliberate. | Same |
| 4 | Pass | Berry, then Teal, each apply instantly; Teal matches the start. | Same |
| 5 | Pass | Dark is readable everywhere checked (body, form fields, badges, notice and warning boxes); no bright patches. | Same |
| 6 | Pass | Light comes back, the same as the start. | Same |
| 7 | Pass | "Using light because that is your device's setting."; with a dark device emulated in DevTools it follows live: "Using dark because that is your device's setting." | Same |
| 8 | Pass | Berry + Dark, then reload: dark Berry from the first paint, no flash. | Same |
| 9 | Pass | A new tab is still Berry/dark. | Same |
| 10 | Pass | The sign-in page uses the saved theme (pink "Sign in", dark background). | Same |
| 11 | Pass | Bob in the same browser sees Berry/dark. | Same |
| 12 | Pass (limited) | The private window's sign-in page is the default Teal/light, with no Berry. Bob's sign-in there wasn't completed (the test tooling can't fill the private window). | Same |
| 13 | Pass | Clearing site data brings back default Teal/light; the page works. Side effect: Home goes back to the orientation page (onboarding state is local). | Same |
| 14 | Pass | At 390 px the choices wrap with no sideways scroll; the Settings tab strip scrolls inside itself ("What…"). | Same |
| 15 | Pass | /terms and /disclaimer are themed (Berry dark) and readable, including the green "Draft for review" box. | Same |

**Also seen:** a single 504 Gateway Timeout on the sign-in page's document request (it loaded on retry); a 401 on `/api/auth/refresh` while signed out (expected). The slowest step was ~3.5 s (opening a fresh tab and then New Items).
**Summary:** 15 Pass (12 limited), 0 Partial, 0 Fail. Identical to pass 1.


# FS-35 — Send feedback and see your messages — build 982952c (Staging), pass 2
Mode: Full (browser). Run ~3:03–3:05 AM ET, Nov 3, 2026, after a DB Stager reset (no feedback rows for any QA persona). Alice has "UAT Cordless Drill".

| # | Result | Evidence | vs pass 1 |
|---|---|---|---|
| 1 | Pass | Footer link (`/feedback?from=%2Forientation`); Account menu "Quick set-up, Bring in purchases, Credit cards, Extended warranties, Insurance, Send feedback, Settings, Sign out"; `/account` "Send feedback – Ask a question, suggest something or report a problem." | Same |
| 2 | Pass | "Send feedback"; "Page you were on: /items", "App version: unknown" at first, then "982952c" once loaded; "Nothing else about your items, purchases or cards is sent."; no Item line. | Same (the "unknown" moment is new but harmless) |
| 3 | Pass | "Page you were on: /items/01a1a06e-…", "Item: 01a1a06e-09b9-7ae3-9ff3-a7cf58069210", matching the URL. | Same |
| 4 | Pass | "Write a message first."; nothing changed. | Same |
| 5 | Pass | "Sending…", then "Thank you. We received your message."; the form clears ("0 / 4,000"). | Same |
| 6 | Pass | "Question · Nov 3, 2026 / Received / UAT question one". | Same |
| 7 | Pass | Problem, Suggestion, Question, newest first, all "Received". | Same |
| 8 | Pass | All three are kept after reload. | Same |
| 9 | Pass | Capped at 4,000 (maxlength): "4,000 / 4,000 · That is the most we can take. Shorten your message to send it." | Same |
| 10 | Pass | `<b>bold</b> & "quotes"` shows literally. | Same |
| 11 | Pass | The 5th ("UAT five") is accepted. | Same |
| 12 | Pass | 6th refused: "You have sent several messages in the last hour. Please try again a little later."; nothing added; the text stays in the box. | Same |
| 13 | Pass | Bob: "You have not sent any messages yet."; none of Alice's. | Same |
| 14 | Pass | Bob's "UAT question from Test2" is accepted and listed alone. | Same |
| 15 | Pass | Alice sees only her 5. | Same |
| 16 | Pass | `?from=https://example.com/x` gives "Page you were on: none". | Same |
| 17 | Pass | Signed out, it redirects to `/login?returnUrl=%2Ffeedback`. | Same |

Nothing clearly over 3 s (sign-in ~2.1 s, feedback page ~2.1 s, sends 0.9–1.6 s). The radio type doesn't stay selected after a send (a minor note, not a fail).
**Summary:** 17 Pass, 0 Partial, 0 Fail. Identical to pass 1. FS-38 must wait until after ~4:05 AM ET.


# FS-36 — Claim guidance wizard — build 982952c (Staging), pass 2
Mode: Full-only (browser). Run ~3:09–3:13 AM ET, Nov 3, 2026. Staged by DB Stager with coverage source 'Default' (pass 1's 'Manual' rows had crashed /api/items); /items loaded all 4 items with no error. claim_guides = 8. The Blender was bought Nov 3 (pass 1: Nov 2), so its window ends Nov 18.

| # | Result | Evidence | vs pass 1 |
|---|---|---|---|
| 1 | Pass | Header "Edit / Refund / Mark returned / Mark disposed"; panel "Need to return it or make a claim?" with "Start a refund or claim". | Same |
| 2 | Pass | "Step 1 of 3"; 7 reasons with sub-lines; Next disabled until one is chosen. | Same |
| 3 | Pass | "Step 2 of 3", "A few quick questions", intro "We already know what you bought, where and when…"; questions: used as intended, can you read the serial number, still have the receipt; "See my options". | Same |
| 4 | **Partial** | Intro exactly "You said It does not work or it broke. Here is what may apply to your UAT Blender, best option first." No "Step 3 of 3" label (no step label at all). | Same |
| 5 | Pass | "Return window · Best Buy / Best option / Applies", "15 days left (until Nov 18, 2026)", 4 steps, have-ready "You have it" / "Not on file"; warning "Once the item is returned you no longer own it, so the maker's warranty and any card protection for it usually end too." is **red text on a pink box (now verified)**; "General guidance for a store return. We have not checked Best Buy's own page." | **Better**: Partial → Pass (the colour was unverified in pass 1) |
| 6 | Pass | "Manufacturer warranty · Cuisinart / Applies", "365 days left (until Nov 3, 2027)", have-ready serial "Not on file", photos "Check you have it", "General guidance for a maker's warranty claim…". | Same |
| 7 | Fail* | Ticks aren't kept; a reload goes back to "Step 1 of 3" with nothing selected. *The plan only says to record it, but losing the whole wizard on reload is worth a look. | Same |
| 8 | Pass | "StuffIt shows what companies have published and general guidance. The company decides every claim and return, its terms can change, and this is not legal advice. Nothing is sent for you, and no one can promise a request will be approved." | Same |
| 9 | Pass | Best Buy "Might apply", no badge ("…depends on something you were not sure about: the item is unopened, or still like new."); Cuisinart "Does not apply": "The maker's warranty does not cover changing your mind.", **dimmed (opacity 0.8), now verified**. | Same |
| 10 | Pass | "The return window may not accept this without it: the item is unopened, or still like new. Check the company's own page." | Same |
| 11 | Pass | No price-protection route; Best Buy Might apply; Cuisinart "does not cover finding it cheaper elsewhere." | Same |
| 12 | **Partial** | "Nothing we know of covers this"; "Ask Best Buy whether it will make a courtesy return or exchange, even though the return window has passed. A request, not a right"; "Credit card: Purchase protection · Chase / Does not apply: The card's purchase protection does not cover something that stopped working." **Wording bug again:** the item was bought today and has no return window, yet the text says the window "has passed". No card route with days/steps (only purchase protection is staged as a coverage). | Same |
| 13 | Pass | "Extended plan · SquareTrade / Best option / Applies", "1095 days left (until Nov 2, 2029)", 3 steps, "General guidance for a protection plan claim. We have not checked SquareTrade's own page." | **Changed**: pass 1 said "Might apply"; now "Applies" with Yes answers |
| 14 | Pass | Ended Item: "Nothing we know of covers this"; Cuisinart "Does not apply: The maker's warranty ended on Sep 15, 2026."; goodwill and courtesy asks, each "A request, not a right". | Same (the courtesy ask again says "the return window has passed" with no window on file) |
| 15 | Pass | Marked returned (Nov 3, $89.99, "Store refund" under Money recovered); the Refund link and panel are gone. | Same |
| 16 | Pass | "This item is already marked returned or gone, so there is nothing left to return or claim on." + "Back to the item". | Same |
| 17 | Pass | Bob: "Not found." on /refund and on the item page. | Same |
| 18 | Pass | "Design mock with sample data. Nothing here is saved or sent." (Cosmetic: the mock still lists 6 reasons with "Something else".) | Same |
| 19 | Pass | Redirects to /login?returnUrl=%2Fitems%2F…%2Frefund. | Same |

Route order: Blender store then warranty every time; nothing-applies block and requests first for Card Item and Ended Item. No page over 3 s (slowest ~2.2 s). No promise or legal-advice wording; all steps are general.
**Summary:** 16 Pass, 2 Partial (4, 12), 1 Fail* (7). Pass 1: 15 Pass, 3 Partial, 1 Fail*. The only change is step 5 now verified.


# FS-37 — Money recovered — build 982952c (Staging), pass 2
Mode: API+Full, run in Full. Run ~3:15–3:23 AM ET, Nov 3, 2026, after a DB Stager reset. Purchases were source Manual dated Nov 3 (pass 1: source Email, Nov 2).

| # | Result | Evidence | vs pass 1 |
|---|---|---|---|
| 1 | Pass | "Nothing recorded this year. Got money back? Open the item and choose Mark refunded." No amount. | Same |
| 2 | Pass | "Mark refunded", "Add a card payout"; "Nothing recorded yet. Add it when the money comes back." | Same |
| 3 | Pass | "$120.00 · Store refund · Nov 3, 2026 · Back to the original payment" / "UAT refund"; Returned. | Same |
| 4 | Pass | "$120.00on 1 item", "$120.00 in cash" (cosmetic: no space before "on"). | Same |
| 5 | Pass | "…Store credit · credit, not cash"; "$180.00on 2 items", "$120.00 in cash · $60.00 in store credit and gift cards". | Same |
| 6 | Pass | "$45.00 · Card payout"; stays "Needs info"; "$165.00 in cash · $60.00 in store credit and gift cards". | Same |
| 7 | Pass | Two rows; cash 173.99; still Returned. | Same |
| 8 | Pass | Cash 174.99. | Same |
| 9 | Pass | "Remove this?" / "Remove the $9.99 you recorded? It will no longer count toward what you have recovered." (Keep it / Remove); cash 165.00; still Returned. | Same |
| 10 | Pass | One mirrored row "$200.00 · Store refund"; cash 365.00, not 565. | Same |
| 11 | Pass | The row follows to $190.00; cash 355.00. | Same |
| 12 | Pass | "Remove the $190.00…" then "Do you have the item again?" ("No, leave it returned" / "Yes, I have it"); left Returned, "Refund Not paid yet"; Home back to $165.00 cash. | Same |
| 13 | **Partial** | A future date is refused and nothing saved, but the message is the generic "One or more validation errors occurred." | Same |
| 14 | **Partial** | Negative and empty amounts disable Save (nothing saved), with no specific message. | Same |
| 15 | Pass | "This year", "Last 12 months", "All time"; $225.00 on 3 items in all; the choice is kept after reload. | Same |
| 16 | Pass | Rec Three $45 Card payout, Rec Two $60 Store refund (credit), Rec One $120; no Bob items. | Same |
| 17 | **Fail** | Before the refund Bob's Home showed a Recovered prompt ("Got money back on something? Open the item and choose Mark refunded."). After recording $50.00 (saved, item Returned), Home showed only the welcome and set-up block, with no Recovered card, after three reloads and waits of 20–25 s. Same gap as pass 1: a user whose items are all returned doesn't see their recovered money. **New:** the first Home reload after the refund dropped Bob to the sign-in page (session lost); not reproduced. Nothing of Alice's leaked. | Same (plus a session drop) |
| 18 | Pass | "Not found." | Same |
| 19 | **Fail** | "Prepare my download" was ready in ~6 s ("Ready until Nov 10, 2026", "Download (4 KB)"), but clicking Download gives "That download is no longer available. Prepare a new one." (twice). recoveries.csv can't be checked. Likely the Cloudinary ZIP delivery setting (see FS-40 7–8). | Same |
| 20 | Pass | Redirects to /login?returnUrl=%2F; no amounts. | Same |

Labels: "Store refund", "Card payout (a card benefit paid you)", "Warranty payout". The recovery form offers no Exchange (Not sure, Back to the original payment, Store credit, Gift card, Cash, Check, Other); **the return form's "Paid back by" still offers "Exchange"**.
**Summary:** 16 Pass, 2 Partial (13, 14), 2 Fail (17, 19). Identical to pass 1.


# FS-38 — Admin feedback queue (API+Full, run in Full) — build 982952c (Staging), pass 2
Mode: Full (browser). Accounts: Ops, Alice (Test1), Bob (Test2). Run 4:25–4:28 AM ET, Nov 3, 2026, after a DB Stager reset (feedback table empty; Alice's "UAT Feedback Item", Best Buy, $49.99, staged). Exactly 4 feedback messages were sent. Ops signed in with two-step (the code was taken from the authenticator helper; no codes or keys are recorded here).

| # | Result | Evidence | vs pass 1 |
|---|---|---|---|
| 1 | Pass | Alice sent a Question ("UAT admin question") and a Suggestion ("UAT admin suggestion"); each showed "Thank you. We received your message.", with "Page you were on: none" and "App version: 982952c". The Problem was sent from the UAT Feedback Item page: footer "Send feedback" goes to `/feedback?from=%2Fitems%2F…`, and "What will be sent" lists the Page, "Item: 01a1a0b9-…" (the item id, not the name), "App version 982952c" and "Nothing else about your items, purchases or cards is sent." "Your messages" shows Problem, Suggestion, Question (newest first), all "Received", Nov 3, 2026. | Same |
| 2 | Pass | Bob: before sending, "You have not sent any messages yet."; "UAT admin bob problem" (Problem) is then listed as "Received". | Same |
| 3 | Pass | Ops (two-step) lands on `/admin/feedback`: "Feedback", "4 new · 4 shown". Status filter (All / Received / In progress / Answered) and Type filter (All / Question / Suggestion / Problem). Four rows, newest first (4:26:47, 4:26:11, 4:25:57, 4:25:51 AM), each with type, timestamp, "Received", the text and the sender's email. Not a placeholder. | Same |
| 4 | Pass | Alice's Problem detail: heading "Problem", timestamp, text, From "QA Test 1 · <email>", the Page path, Item "UAT Feedback Item" (name only), App version "982952c", and the Status dropdown. | Same |
| 5 | Pass | Type = Problem: "4 new · 2 shown" (both Problems). | Same |
| 6 | Pass | Status = Received shows 4; back to All shows "4 new · 4 shown". | Same |
| 7 | Pass | Bob's Problem set to "In progress" at once ("3 new · 4 shown"); kept after reload. | Same |
| 8 | Pass | Alice's Problem set to "Answered" ("2 new · 4 shown"); kept after reload. | Same |
| 9 | Pass | Bob sees his message as "In progress". | Same |
| 10 | Pass | Alice sees only her own 3: Problem "Answered", Suggestion and Question "Received"; none of Bob's. | Same |
| 11 | Pass | Status = Answered: "2 new · 1 shown", only Alice's Problem. | Same |
| 12 | Pass | Detail is read-only apart from the Status dropdown (no text inputs or buttons). No paging or "load more" with 4 messages. "new" counts Received only. The Ops menu has "Customer view". | Same |
| 13 | Pass | Bob at `/admin/feedback` lands on Home (`/`): no queue, no Admin entry in his menu. | Same |
| 14 | Pass | Alice at `/admin/feedback` lands on Home (`/`): no queue, no Admin menu. | Same |
| 15 | Pass | Signed out, it redirects to `/login?returnUrl=%2Fadmin%2Ffeedback`. | Same |
| 16 | Pass | Item detail shows the name only ("UAT Feedback Item"); no price, store or receipt. | Same |

**Observations:**
- Order is newest first (the story says oldest first for a work queue; unchanged from pass 1, accepted as first-build behaviour). Statuses are Received, In progress and Answered; "new" counts Received only. The list shows the full timestamp to the second; the customer list shows the date only.
- Customer side shows the item **id** ("Item: 01a1a0b9-…") in "What will be sent", not the name. **Same as pass 1** (FS-35 step 3 in pass 1 shows the same id on the customer side). Admin detail shows the name.
- In this pass Ops's two-step was already on, so no re-enrolment was needed (pass 1 had to re-enrol first).

**Summary:** 16/16 Pass, 0 Partial, 0 Fail. Identical to pass 1.


# FS-39 — Daily digest — build 982952c (Staging), pass 2
Mode: Full (browser + Gmail + maintenance clock). Run ~3:26–3:37 AM ET, Nov 3, 2026, after a DB Stager reset (no items or reminders, all types At once, clock offset 0). Accounts: Alice (Test1), Bob (Test2).

| Step | Result | Notes | vs pass 1 |
|---|---|---|---|
| 1 | Pass | The Daily digest row has Email and In-app checkboxes (Text "coming soon") rather than one switch. Note: "One email a day, at your reminder time (set in your profile). It lists the messages below that you chose to get in the daily digest, and is not sent on a day with nothing to list. A return window or warranty ending within 3 days is always emailed at once." Each of the four types has "<type>: how email arrives" with "At once" / "In my daily digest", all At once. "Changes save as you make them." | Same |
| 2 | Pass | UAT Digest One, Best Buy, Nov 3, $99, with the suggested "Best Buy return policy: general" (15 days) coverage; window ends Nov 18, 2026. | Same (15-day policy) |
| 3 | Pass | Return window closing set to "In my daily digest"; autosaved ("Saved"); kept after reload. | Same |
| 4 | Pass | Clock +8 (Nov 11). The first run-reminders gave `Sent = 0` because the app time (3:28 AM New York) was before the default 9:00 AM reminder time; with Alice's Time of day set to 01:00 it gave `Sent = 1`. No separate email; in-app "UAT Digest One: return window ends in 7 days" / "The return window on UAT Digest One ends in 7 days, on November 18, 2026." | Same (pass 1 ran after 9:00) |
| 5–6 | Pass | "Digest run: sent 1, skipped 0, failed 0." Email "1 thing needs your attention", body "- UAT Digest One: return window ends in 7 days", with links to Returns, Open WarrantyBank, Manage settings and unsubscribe. From StuffIt <<noreply sender>>, reply-to stuffit-<admin address>. Arrived as soon as run (not held to the reminder time once due). Landed in Gmail Promotions. A matching in-app summary also appeared. | Same |
| 7–8 | Pass | Rerun: "Digest run: sent 0…"; reminders `Sent = 0`. No duplicates. | Same |
| 9 | Pass | Five burst items on Nov 11 (window Nov 26). Clock +8 (Nov 19): reminders `Sent = 5, Cancelled = 2`; digest sent 1. Email "5 things need your attention" with the single line "5 return windows are closing". In-app: the summary plus five item notices. | Same |
| 10 | Pass (deviation) | UAT Urgent on Nov 19 (window Dec 4). +13 (Dec 2, 2 days left): `Sent = 0, Cancelled = 12`, digest sent 0, so no urgent email. +1 (Dec 3): `Sent = 1`, email "UAT Urgent: return window ends tomorrow" arrived at once (Updates); digest sent 0. **Possible gap (unchanged):** an item that crosses the 3-day mark between reminder runs gets no urgent email until the next lead day. | Same |
| 11 | Pass | Digest Email and In-app unticked ("Saving…", "Saved"); "Return window closing" still "In my daily digest" after reload. | Same |
| 12 | Pass | UAT Instant on Dec 3 (window Dec 18). +8 (Dec 11): `Sent = 1`; separate email "UAT Instant: return window ends in 7 days" arrived at once; digest sent 0. | Same |
| 13 | Pass | Digest boxes re-ticked; Return window closing back to "At once"; after reload all four "At once" and both boxes ticked. | Same |
| 14 | Pass | Bob's inbox had no StuffIt mail in the hour. His settings: all four "At once", both digest boxes ticked. My Items "Nothing here yet"; /notifications "You are all caught up." | Same |
| 15 | Pass | Unsubscribe opens a confirm page: "Email preferences / You are getting emails about Daily digest. What would you like to stop?" with "Only "Daily digest" emails", "All "Summaries" emails", "All optional emails from WarrantyBank", and "You will still see these in the app. Only email stops." No address or other account data. Not pressed. Manage opens Alice's own /settings/notifications. | Same |
| 16 | Pass | clock/reset: "Back to real time. Offset 0 day(s); the app's time is 2026-11-03 08:36:02Z." Alice's Time of day cleared back to empty (9:00 default). | Same |

**Observation (new, minor):** Settings > Profile showed Time zone "Not set (UTC)" before the first save and again after Time of day was cleared, but "America/New_York" while a time was set; DB Stager reports Alice's stored time zone as America/New_York. The time zone display may be tied to whether a time of day is set. Worth a look; the reminder timing behaved as New York.
**Summary:** 16/16 Pass (step 10 with the same deviation). Identical to pass 1. Cosmetic: digests land in Gmail Promotions.


# FS-40: Retest the 2026-11-02 fixes (build 982952c, Staging, pass 2)

Mode: Full. Accounts: Test1 (Alice), plus Test2 (Bob) as the outsider target. DB Stager reset both clean at 4:03 AM ET; nothing pre-staged (same as pass 1). Clock offset 0, then +31 at 4:07 AM (app "today" Dec 4, 2026 NY), then reset at 4:20 AM. Run 4:04–4:23 AM ET.
Cloudinary "PDF and ZIP files delivery": **could not be confirmed**; DB Stager has no access to the storage setting. Steps 7–8 fail with HTTP 500 from the API, which fits that setting being off. **These are storage settings, not app code.**

| # | Finding | Result | vs pass 1 | Evidence |
|---|---|---|---|---|
| 1 | FS-24-9 item dates | **Partial** | Better | At offset 0: "Expiring soon", "30 days left", "Covered 1 policy", "Next to end: Return window, Dec 3, 2026 · 30 days left", and a **Start a return** button. After +31: badge "Expired", "Coverage ended / 1 policy", row "Ended Dec 3, 2026", no days-left and no Next-to-end; /items "Expired", "All coverage has ended", so the two pages agree. **"Start a return" is now gone.** Still offered: "Refund", "Start a refund or claim" (/refund) and "Mark returned". |
| 2 | To-do overdue | **Pass** | Fail → Pass | The To do card is in edit mode. "UAT overdue" due Dec 3 reads "**Overdue since Dec 3, 2026**" on the item and on /todos. The one notification is stamped "Nov 3, 2026, 4:05 AM": it was created before the clock advance, so the real time is correct. |
| 3 | FS-24-6 bell badge | **Pass** | Same | Badge "1" (aria "Notifications, 1 unread, 1 to do") with 1 unread listed. After reading it: "Notifications, 1 to do" with a dot, not a number. |
| 4 | FS-24-6 notification title | **Pass** | Same | Clicking the title "Your data export is ready" opened /settings/privacy and marked it read. This notice has no "View item" link to compare. |
| 5 | FS-31-16/17/18 end plan | **Pass** | Same | Plan added via /plans ("UAT Clock Plan", UAT Provider, $5.00 a month, from Nov 3) and covering the shoes. "It ended on" was empty, and "End this plan" stayed disabled until a date was chosen. |
| 6 | End plan today | **Partial** | Same | Plan "Ended Dec 4, 2026" and dimmed (opacity 0.7). The /plans total went to "$0.00 a year…", so it's excluded, but the row still shows "$60.00 a year". **The item page still treats the plan as running:** the badge flipped from "Expired" to "Expiring soon", with "Covered / 2 policies", "Next to end: Extended plan, Dec 4, 2026 · Ends today", and the plan marked "Try this first". |
| 7 | FS-27-13/14 export | **Fail (storage)** | Message is back | "Prepare my download" (POST 202), ready in about 6 s: "Ready until Nov 10, 2026", "Download (4 KB)". Download: `GET /api/exports/<id>/download` gives **HTTP 500** and the alert "That download is no longer available. Prepare a new one." No zip. Pass 1 failed silently; now the old message shows again. |
| 8 | PDF receipt | **Fail (storage)** | Same | small-receipt.pdf uploaded and listed (45 KB). View: `GET /api/documents/<id>/content` gives **HTTP 500**, "Could not open that file." (The store typed on the add form stuck this time.) |
| 9 | FS-35-9 feedback overflow | **Pass** | Same | No sideways scroll; the 4,000-character no-space text wraps. Counter "4,000 / 4,000 · That is the most we can take. Shorten your message to send it." (bold red); more input is blocked. The words version sent ("Thank you. We received your message."), and "Your messages" wraps it. |
| 10 | Nested link | **Pass** | Partial → Pass | From /items: `/feedback?from=%2Fitems`, "Page you were on: /items". Footer link ×2 and Account menu ×2 from the form kept the same URL and "/items"; no `from=…from=…`. |
| 11 | FS-33 tracking note | **Pass** | Same | After typing 250 and clicking "Everything": "The standard amount is $50.00. Zero tracks everything.", under the field. Same after saving at 0 and reloading. Restored to the standard ("Using the standard amount, $50.00…"). |
| 12 | FS-33-3 lines past cap | **Partial** | Changed | All 12 lines accounted for ("Showing 12 of 12" after Show more): 4 in the main list (Work gloves, Interior paint, Deck screws, Stud) and "Smaller things (8)", including Wood glue 16OZ $6.99 and Sandpaper 80G $12.45. The reason reads "Under $50 · … much cheaper than the rest", **not "Cheaper than the lines kept"**. New upload note: "12-thermal-long-many-items.pdf: 1 more line is under Smaller things (this receipt has more than we show up front)." It now gives a count, but **"1 more line" doesn't match Smaller things (8)**. Read about 32 s. |
| 13 | Work gloves | **Pass** | Partial → Pass | Work gloves L, $25.98, stays in the main list and now has the **"Under $50"** label. |
| 14 | FS-25-12 sign-up leak | **Pass (timing note)** | Same | The page is identical for taken and new addresses ("Check your email / We sent a link to [address]… Nothing is created until you do…"). Times (s): taken 0.964 / 0.960 / 0.956; new 1.441 / 1.436 / 1.428. **A consistent ~0.47 s gap, so a timing leak is likely** (pass 1 had about 0.5 s). Test2 got "You already have a WarrantyBank account"; +fs40p2a/b/c got "Confirm your email…". Same signed-out browser, not a cookie-free one. Some extra sign-ups came from timed-out batch runs. |
| 15 | FS-25-17 reset links | **Pass** | Same | Requests at 4:20:28 and 4:21:38 AM ET ("If that email is registered, we sent a link…"). Older link submitted first: "**This link has already been used or has expired. Request a new one.**" Newer link: "Your password was changed. Sign in with the new one." (set to the same password, and Bob signs in). Note: both links open the form, and the older one is refused only on submit. Both emails now carry "Requested at… If you asked more than once, use the newest email." (an earlier pair at 4:16/4:18 had the line only on the second email). |
| 16 | Console | **Partial** | Same | Signed-out /login logs `401` on `/api/auth/refresh` ("Failed to load resource…"). Signed in, Home, an item page, /notifications and /feedback had 0 errors on load and reload. |
| 17 | Clock reset | **Pass** | Same | "Back to real time. Offset 0 day(s)." |

**Summary:** Pass 11 (2, 3, 4, 5, 9, 10, 11, 13, 14 with a timing note, 15, 17). Partial 4 (1, 6, 12, 16). Fail 2 (7 and 8, storage, HTTP 500).
**vs pass 1 (8 Pass / 6 Partial / 3 Fail):** step 2 Fail → Pass (overdue to-do works); steps 10 and 13 Partial → Pass. Step 1 is better ("Start a return" hidden after the window ends) but still offers refund/claim. Step 7 shows its message again. Step 12 now has an upload count, but it's wrong.
Left behind: Alice has UAT Clock Shoes (with the ended UAT Clock Plan and an overdue to-do), UAT PDF Item, 12 pending Pine Street lines, the standard tracking minimum, and **one feedback message (about 4:10 AM ET)**. Bob's password is unchanged. Sign-up attempts for +fs40p2a/b/c were not confirmed, so no accounts were created.


# FS-41: Receipt protection plans and stated warranties (build 982952c, Staging, pass 2)

Mode: Full. Accounts: Test1 (Alice) and Test2 (Bob). Live reader (anthropic); per Steve, a reader miss is Partial and the reading is quoted. DB Stager reset both accounts clean at 3:38 AM ET. Run 3:40–3:49 AM ET.

## Part A: protection plans

| # | Result | vs pass 1 | Evidence |
|---|---|---|---|
| 1 | **Partial** | Same | One row, so the plan is not a second item and not in the name. Row "Wireless Noise Cancelling Headphones · Black", "Best Buy · Oct 2, 2026 · **$421.98**" (expected 349.99; item Price is $349.99, Total $421.98). "Includes: Geek Squad Protection - 2-Year Plan, $49.99 · Geek Squad · 24 months" (Highly Likely). No plan number, no SKU. About 23.6 s (**over 20 s**). |
| 2 | **Partial** | Same | Name, company, price and 24 months shown. **No "covers SKU 6505727" or match text, and no keep/untick tick.** |
| 3 | **Fail** | Same | No "Add Details" control. The row actions are only Add as a new item / Link this to an existing item / Quick add, edit later / Dismiss. |
| 4 | **Fail** | Same (one new detail) | The full Add offers only "Best Buy return policy… 15 days" (disabled: window ended 2026-10-17) and "Sony warranty… 1 year"; **the Geek Squad plan is not offered and is dropped**. New: Save with nothing ticked now silently does nothing, with no message (pass 1 showed "Tick at least one policy…"). With Sony ticked, the item has only "Manufacturer warranty · Sony, Oct 2, 2026 to Oct 2, 2027". `/plans` shows "No plans yet." (correct). |
| 5 | **Partial** | Same | TV row "OLED TV · 65IN… $1,299.99" with "Includes: Geek Squad Protection 4YR, $299.99 · Geek Squad · 48 months"; the cable ($39.99) is under Smaller things. **No "purchase date used" note.** Quick add attached "Extended plan · Geek Squad, Sep 27, 2026 to Sep 27, 2030… From your receipt: GEEK SQUAD PROTECTION 4YR. Paid 299.99. Plan number GS-88104471. Covers: SKU 6571204." No start-date or confidence label. Cosmetic per Steve's grading note, kept Partial for consistency with pass 1. About 24.6 s (**over 20 s**). |
| 6 | **Partial** | Same | Row "800 Series Dishwasher… **$1,539.22**" (expected $1,099.00; more than item + plan + install = $1,459.98, so likely the order total with tax). Plan "Geek Squad Protection 3-Year, $229.99 · 36 months". The install line is neither an item nor a plan (Pass). No totals warning. 18.4 s. |
| 7 | **Partial** | Same | Walmart: "Allstate Protection 3YR, $49.00 · Allstate · 36 months" (row "4K TV · 50IN… $397.74"). Lowe's: "Lowe's Protection Plan 3-Year, $99.00 · 36 months" with **no company** (row "500 Series Dishwasher… $1,072.94"). **No "not in our list" or "not verified" note.** 17.9 s / 15.9 s. |
| 8 | **Partial** | Same | The Geek Squad coverage has no claim contact and no "from the company's record" wording, only "From your receipt". "Check this is for the item above" never appeared (that half Not run); the closest is the cable's "Looks like a document for OLED TV. Same order number (0412-0007-33518). Attach it there". |
| 9 | **Pass** | Same | Pine Street (12-thermal): 16 rows, "No warranty found yet…", and none of the "Includes:" lines on the page come from this receipt. Read time not captured (over the 25 s check, so likely **over 20 s**, as in pass 1). |

## Part B: stated warranties

| # | Result | vs pass 1 | Evidence |
|---|---|---|---|
| 10 | **Pass (note)** | Same | "Inverter Generator", "Kestrel Marine & Power · Jul 19, 2026 · $790.20". "Receipt says: 2 YR MFR WARRANTY (manufacturer)· Likely… · 24 months. Not added by a quick add:" (nothing follows the colon). No "may apply" or percentage. 17.5 s. |
| 11 | **Fail** | Same | Quick add: "**One or more validation errors occurred.**" and no item. The full Add has Store, Brand and Category blank and no stated-warranty option. After filling them (Kestrel shown UNVERIFIED, "not in our shared list yet"), it reads "Nothing found yet…" and Save gives "Saved in New Items. Tick at least one policy to add it to your items." **No item and no "Stated on receipt" coverage can be created.** |
| 12 | **Pass** | Same | "Stated on receipt, provider unconfirmed: Road hazard warranty 50,000 mi… The receipt does not say who stands behind this warranty… Stated as 50,000 miles; a mileage has no end date, so none is set from it." Row "Tire · 225/65R17", "Lakeside Tire & Auto… $734.28 (x4, $149.00 each)". The odd pass-1 row name is gone. |
| 13 | **Pass** | Same | Only "Mini-Split Heat Pump · 12K BTU" has "5 YR COMPRESSOR / 1 YR PARTS" with "The receipt gives more than one term; none is set. See the text and add the ones that apply." "Line Set Kit · 25FT" has none. 18.5 s. |
| 14 | **Partial** | Same | "Stated on receipt, provider unconfirmed: Repair warranty: 90 days parts and labor. (manufacturer)… · 3 months". 3 months is correct, but the tag says **(manufacturer)**, not the seller. Row "Compressor Start Relay · fridge, Jim's Appliance Repair… $222.00" (the whole invoice), tagged "Under $50". |
| 15 | **Pass** | Same | "Pellet Stove · 40K" ($2,299.00): "Stated on receipt, provider unconfirmed: 10 YR LIMITED WARRANTY… · 120 months". "Stove Pipe Kit · 4IN" has none. |
| 16 | **Pass** | Same | Sears Outlet: no stated warranty from the open-box sentence. It read a plan instead, "Includes: Sears Protection Agreement 2-Year, $99.99 · 24 months". Target (19-a5, return window only): Kettle and Coffee Maker have none. 17.5 s / 17.0 s. |
| 17 | **Partial** | Same | No way to remove a stated warranty on the row (no untick, X or menu). Full Add of the tires (Michelin ticked) gives an item with only "Manufacturer warranty · Michelin, May 30, 2026 to May 30, 2027" and no stated coverage. That's the expected end state, but only because a full Add never carries it. The item price is $596.00 (4 × $149) where the row showed $734.28. |
| 18 | **Pass** | Same | Repair row: "The receipt says 3 months (Repair warranty: 90 days parts and labor.); the maker's policy says 1 year. Check which applies." The Whirlpool warranty is listed separately. No other comparison notes. |
| 19 | **Pass** | Same | Bob: New Items "Nothing waiting…", My Items "Nothing here yet…". |

**Summary:** Pass 8 (9, 10, 12, 13, 15, 16, 18, 19). Partial 8 (1, 2, 5, 6, 7, 8, 14, 17). Fail 3 (3, 4, 11). **Identical to pass 1.**

**Main findings (unchanged):**
1. A full "Add as a new item" drops receipt plans and stated warranties. Only a quick add keeps a plan.
2. There is no Add Details plan tick.
3. The headphones and dishwasher rows show the order total, not the line price.
4. An item from an unknown store or maker with only a stated warranty can't be added: quick add gives a validation error, and the full Add needs a policy.
5. Plans have no purchase-date-used or confidence label.
6. Allstate has no "not in our list / not verified" note, and the Lowe's plan has no company.

New this pass: Save on the full Add form with nothing ticked gives no message. "Not added by a quick add:" on the generator has nothing after the colon.
Reads over 20 s: 21-bestbuy (about 23.6 s), 15-bestbuy-tv (about 24.6 s), 12-thermal (over 25 s).
Data left: Alice has headphones, OLED TV and Tire; the other rows are still in New Items.


# FS-42: Policy note, source link, to-dos you can get back, polish (build 982952c, Staging, pass 2)

Mode: Full. Accounts: Test1 (Alice), Test2 (Bob), Ops (step 20). DB Stager reset and staged at 3:50 AM ET: Alice's "UAT Todo Item" (Best Buy, Nov 3). The New Balance return policy has source https://www.newbalance.com/returns (verified_at empty); Best Buy's policies have verified_at set (both unchanged since pass 1). Run 3:51–4:03 AM ET.

| # | Result | vs pass 1 | Evidence |
|---|---|---|---|
| 1 | **Pass** | Better | "New Balance return policy", Merchant, 30 days, Unconfirmed, with "**Usual window, can differ for your item. Check your receipt.**" and a Source link. **The store dropdown now offers the existing "New Balance"** (pass 1 offered only `Add "New Balance"`). |
| 2 | **Pass** | Same | href `https://www.newbalance.com/returns`, target `_blank`, rel `noopener noreferrer`. |
| 3 | **Partial** | Same | The saved item's "Return window · New Balance" has the Source link (same href). The "Usual window…" note is **not** on the saved item for the Unconfirmed policy; the policy text instead ends "…The 30 days is not stated in the order email, so confirm it on the source page before relying on it." |
| 4 | **Pass** | Same side bug | The hand-added "Store warranty · UAT own warranty" has no Source link and no note. Side bug still there: Length 12 saved, yet "Nov 3, 2026 · **No fixed end date**" (Ends blank). |
| 5 | **Fail** | Same | "Best Buy return policy: general", Merchant, 15 days, **Confirmed**, pre-ticked, still shows the "Usual window, can differ…" note. Source is the bestbuy.com return-exchange-policy page. "Smartphones", 14 days, Likely is also offered. |
| 6 | **Pass** | Same | Bob sees the same suggestion, note and Source href, and none of Alice's data (store list, /todos, her item URL). |
| 7 | **Pass** | Same | "Looking…" (about 0.3 s), then "Nothing new to suggest. Everything we know of is already added to this item." |
| 8 | **Pass (note)** | Same | The To do card is only in edit mode. Three open to-dos were added. |
| 9 | **Pass** | Same | All three left the open list. |
| 10 | **Pass** | Same | Collapsed "Show done and dismissed (3)" / "Hide…". UAT n/a "Not applicable" with Undo; UAT dismiss "Dismissed until Nov 10, 2026" with Undo; UAT done "Done" with Reopen. |
| 11 | **Pass** | Same | Undo returns "UAT dismiss" to the open list; the section becomes (2). |
| 12 | **Pass** | Same | /todos is collapsed, "Show done and dismissed (2)". Reopen on "UAT done" from /todos worked; (1) left. |
| 13 | **Pass** | Same | Bob's /todos: "Nothing to do right now." Alice's item URL: "Not found." |
| 14 | **Pass** | Same | One real click opens the account menu, and it stays open. |
| 15 | **Partial** | Same | With "New Bal" typed and the field left, the field is **cleared silently** to its placeholder: no `"New Bal" is not selected yet` and no add-as-new button. The full "New Balance" auto-selects. |
| 16 | **Partial** | Same | The item page has no "Stop covering" (coverages show Edit/Remove; the plan row too). Remove asks "Remove this coverage?"; Cancel keeps it and confirming removes it. The plan page's "Stop covering this item?" ("…The item itself stays.") asks first, and Cancel keeps it. Insurance "Unlink this item?" asks first, and Cancel keeps it; the unlink exists only on the policy page, not the item. |
| 17 | **Pass** | Same | "Delete this file?" ("small-receipt.pdf is removed. This cannot be undone.", Cancel / "Delete file"). Cancel keeps the file on the item, plan and insurance policy. Side: on the item, setting the file opens a document reading ("What we found in your document": a different store, brand, price and date read from the PDF), and after "Not now" the file wasn't attached until a reload and retry. |
| 18 | **Pass** | Same | Page button "Delete this policy" (icon), dialog "Yes, delete the policy": different labels. |
| 19 | **Pass** | Same | Bob's /settings/security goes to /settings/profile with no "You cannot do that." (no Security tab). |
| 20 | **Pass** | Same | Ops signed in with two-step (first code accepted) and landed on /admin. /settings/security shows "Two-step sign-in is on.", "You have 10 recovery codes left…", Administrators and Extension keys. |
| 21 | **Pass (caveat)** | Fail → Pass | "Return in progress since Nov 3, 2026. It is on your returns list until you mark it returned." No space before the full stop. **Caveat:** run at about 4 AM ET, when the ET and UTC dates are the same. Pass 1's fail (UTC date after 7 PM ET) can't be reproduced at this hour, so the time-zone fix is unconfirmed. |
| 22 | **Pass** | Same | "Only the items you link below: 1 item, which costs $0.00." ($0.00 because UAT NB Shoe has no price; it read "0 items, which cost $0.00" before linking.) |

**Summary:** Pass 18 (1, 2, 4, 6–14, 17–22). Partial 3 (3, 15, 16). Fail 1 (5).
**vs pass 1:** step 21 Fail → Pass (with the time-zone caveat), and the New Balance store now resolves to the existing entry. Everything else is the same.
Nothing took over 3 s apart from the document read (about 3 s or more). Console showed "1 errors" on page load (not opened).
Also seen: the insurance "End this policy" button is enabled right after saving because "It ended on" is prefilled with today (2026-11-03).
Wording that sounds certain for an unconfirmed policy: none. The opposite issue remains: the caution shows on a Confirmed policy (step 5) and is missing on the saved item (step 3).
Left: Alice has UAT NB Shoe (with UAT Polish Plan, UAT Polish Insurance and small-receipt.pdf), UAT BB Thing (return in progress) and UAT Todo Item with to-dos.

