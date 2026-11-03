# StuffIt UAT results: build 982952c
**Build:** commit 982952c, startedAt 2026-11-03T02:06:55Z (9:06 PM ET, Nov 2), Staging. The build watch still sees 982952c at 1:33 AM ET.
**Run:** Nov 2–3, 2026, about 9:30 PM to 1:36 AM ET. Plans are FS-22 and FS-24 to FS-42 from the merged Full Scenarios set. DB Stager reset all four accounts before the run and between every plan; the simulated clock was reset to offset 0 after each clock plan.
**Not run:**
- FS-23 and FS-18–21 are deferred until built.
- FS-22 steps 7–8 are deferred (no share checkbox).
- FS-25 steps 5, 6, 7 and 11 (they need the accounts not to exist).
- FS-27 steps 17, 18 and 20 (deleting Bob) are waiting for your OK; step 14 was not run.
- FS-28 steps 14–18 (optional API checks; there's no Ops or Bob token). Steps 1–3 were skipped because two-step was already on.
- Each plan's "not built" items, per your note.

## Storage (Cloudinary) failures — check the PDF/ZIP delivery setting
As you predicted, every download of a PDF or ZIP fails, which looks like the Cloudinary PDF/ZIP delivery setting being off:
- **FS-40 steps 7–8:** contract PDF view and download give HTTP 500.
- **FS-27 step 13 and FS-37 step 19:** "Prepare my download" shows Ready, then "That download is no longer available. Prepare a new one."
Image files (JPG/PNG) upload, view and delete fine (FS-31 step 12).

## Summary
| Plan | Area | Pass | Partial | Fail | Not run | Headline |
|---|---|---|---|---|---|---|
| FS-22 | Shared policy, private purchases | 6 | 0 | 0 | 2 (deferred) | Privacy holds. The suggestion shows no end date before saving (cosmetic). |
| FS-24 | Clock and reminders | 9 | 1 | 0 | 0 | Refund and claim are still offered after the window ends. |
| FS-25 | Account lifecycle and email | 13 | 0 | 0 | 4 | Both d1ed2c0 fails are fixed (no enumeration; the newest reset link wins). |
| FS-26 | Purchases, items and privacy | 17 | 2 | 0 | 0 | Suggest coverage works now. The doubt note is only on the add form. |
| FS-27 | Cards, notifications, export | 13 | 1 | 2 | 4 | Export fails (storage). Still no "Is yours one of these?". |
| FS-28 | Admin two-step and shared data | 10 | 1 | 0 | 8 | Bob is refused everywhere. No verified filter; "Brand (maker)s" typo. |
| FS-29 | Returns in progress | 20 | 1 | 0 | 0 | No days-left badge on return rows. |
| FS-30 | Insurance | 18 | 1 | 2 | 0 | Still no over-limit note or "not advice" line. |
| FS-31 | Extended warranty plan | 17 | 3 | 0 | 0 | The yearly total now drops an ended plan; the item still says "Ends today". |
| FS-32 | To-dos | 13 | 1 | 0 | 0 | Done and dismissed can now be found again. The reminder doesn't name the item. |
| FS-33 | What to track | 15 | 1 | 0 | 0 | Works. A $25.98 line is never demoted. |
| FS-34 | Color themes | 15 | 0 | 0 | 0 | Clean; no flash on load. |
| FS-35 | Send feedback | 17 | 0 | 0 | 0 | Clean; the limit of 5 per hour works. |
| FS-36 | Claim guidance wizard | 15 | 3 | 1 | 0 | The wizard loses its answers on reload; "window has passed" wording bug. |
| FS-37 | Money recovered | 16 | 2 | 2 | 0 | A user with only returned items sees no Recovered card; export (storage). |
| FS-38 | Admin feedback queue | 16 | 0 | 0 | 0 | Clean. |
| FS-39 | Daily digest | 16 | 0 | 0 | 0 | Works; a possible gap if the 3-day lead passes between runs. |
| FS-40 | Fix retests | 8 | 6 | 3 | 0 | Steps 7–8 are storage; no To do box (step 2). |
| FS-41 | Receipt plans, stated warranties (live reader) | 8 | 8 | 3 | 0 | Reader misses are graded Partial, with what it read quoted. |
| FS-42 | Policy note, source link, to-dos, polish | 17 | 3 | 2 | 0 | The "usual window" note shows on a Confirmed policy; a date shows in UTC. |
| **Total** | | **279** | **34** | **15** | | |

## Fixed since d1ed2c0
- FS-25-12: sign-up no longer reveals accounts. It shows a neutral "Check your email", and the inbox gets "You already have a WarrantyBank account".
- FS-25-17: only the newest reset link works; older ones are refused.
- FS-26-5: Suggest coverage now responds. The policy source link and the note now exist (FS-42), though the note isn't kept on the saved item.
- FS-31-17: the end-date box starts empty, and an ended plan is left out of the yearly total.
- FS-32: done, dismissed and not-applicable to-dos can be found under "Show done and dismissed" and undone.
- The Feedback page is built (FS-35, FS-38).

## Unchanged since d1ed2c0
- An item still treats a plan that ended today as running ("Ends today", still covered) (FS-31-18, FS-40-6).
- No over-limit note on insurance (FS-30-11/12).
- No "Is yours one of these?" card match (FS-27-4).
- No verified filter on Shared data, and the "Brand (maker)s" typo (FS-28-9).
- No days-left count on return rows (FS-29-7).
- Empty forms flag one field only, and date errors show the generic "One or more validation errors occurred." (FS-30, FS-31, FS-37).

## New issues worth a look
1. **Storage downloads** (above).
2. **FS-37-17:** Home hides the Recovered card when every item is returned, so that user never sees the money recovered.
3. **FS-36-7:** the claim wizard resets to step 1 on reload.
4. **FS-42-5/21:** the "usual window" note shows on a Confirmed policy, and a date shows in UTC.
5. **FS-32-12:** to-do reminder emails and bell entries don't name the item. The unsubscribe link carries the `purchase_needs_info` category, so it may turn off the wrong email type. The reminder went out at about 1:17 AM rather than 9:00.
6. **FS-32 oddity:** the bell's "1 to do" is the credit-card notice and never changes with the To do page. Overdue badges are grey, less prominent than the orange due-soon badge.
7. **FS-33-3:** the Work gloves line ($25.98) stays in the main list with its own "Under $50" badge.
8. **FS-31-15:** "Update from a newer document" lists every value, not just the changes.
9. **FS-36 staging side finding:** an unexpected coverage source value makes the whole items list return 500.

---
# Per-plan detail

# FS-22 — Shared policy vs private purchase — build 982952c (Staging)
Mode: Full. Accounts: Alice, Bob (reset clean at 12:03 AM ET). Steps 7–8 deferred (no share checkbox).

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | Alice (New Balance, Oct 25): "New Balance return policy", Merchant, 30 days, Unconfirmed ("We could not check this policy. Tick it only if your paperwork says so."), with the note "Usual window, can differ for your item. Check your receipt." and Source `https://www.newbalance.com/returns`. It was unticked by default. The item shows "Oct 25, 2026 to Nov 24, 2026". |
| 2 | Pass | Bob (Oct 30): identical suggestion, and the item shows "Oct 30, 2026 to Nov 29, 2026", computed from his own date. |
| 3 | Pass | Same policy text ("Online orders: 30 days from delivery… confirm it on the source page before relying on it.") and the same Source href for both. |
| 4 | Pass | Alice edited the end date to Dec 1. After reload: "Oct 25, 2026 to Dec 1, 2026 · 28 days left". |
| 5 | Pass | Bob still has "Oct 30, 2026 to Nov 29, 2026". |
| 6 | Pass | Nothing shows other users' data or counts. Stores & brands says "The ones you add are private to you". Note: /returns is labelled "First design: example data", with sample Sony, Ninja, Keurig and Bosch items (placeholder content, not Bob's). |
| 7–8 | Not run | Deferred (no share checkbox). |

**Summary:** 6/6 Pass (7–8 deferred). The suggestion doesn't show an end date before saving (cosmetic).


# FS-24 — Time travel: a return window ends and the reminder arrives — build 982952c (Staging)
Mode: Full (browser plus maintenance API plus Gmail). Account: Alice (reset clean at 12:09 AM ET; default notification prefs).

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | "UAT24 Clock Shoes", New Balance, Nov 3, 2026 (the default date; it was just past midnight ET), with the 30-day policy ticked. Shows "30 days left" and "Next to end: Return window, Dec 3, 2026 · 30 days left". |
| 2 | Pass | Return window closing and Warranty expiring both have Email and In-app on, delivered "At once". |
| 3 | Pass | GET /api/maintenance/clock returns "Offset N day(s)…" (offset 0 confirmed at reset). Note: a POST to `clock` returns 401; only GET is supported. |
| 4 | Pass (deviation) | +20 days (Nov 23, 10 days left): reminders Sent 0. The app's lead days are 7/3/1, not 10. +3 (offset 23, 00:10 ET Nov 26): Sent 0, because the 7-day lead fires at the 9:00 reminder time. +1 (offset 24): **Sent 1**. |
| 5 | Pass | The email "UAT24 Clock Shoes: return window ends in 6 days" reads "The return window on UAT24 Clock Shoes ends in 6 days, on December 3, 2026." Its "View item" link is the item's own URL, and it also has Manage and Unsubscribe links. It is labelled as a 7-day-lead reminder but says 6 days because it was sent a day late after the clock jump (correct for the send date). |
| 6 | Pass | The bell showed "1" ("Notifications, 1 unread, 1 to do"). /notifications had the reminder as Unread, stamped "Nov 27, 2026, 12:10 AM · just now". View item opened the item, and the notice is now read ("Mark unread"). Home showed "1 Return windows closing… UAT24 Clock Shoes, Return window · 6 days". |
| 7 | Pass | A second run-reminders the same day: Sent 0. |
| 8 | Pass | +7 (offset 31, Dec 4): Sent 0, Cancelled 2 (the skipped 3-day and 1-day leads). No reminder after the window ended, and no new notification. |
| 9 | Partial | Badge "Expired", "Coverage ended · 1 policy", row "Ended Dec 3, 2026"; /items "All coverage has ended"; Home cards all 0. No warranty on the item. **Still offered after the window ended:** "Start a refund or claim", "Refund", "Mark returned" (same finding as FS-40 step 1). The bell keeps "1 to do" while Home says "Nothing needs your attention right now." |
| 10 | Pass | clock/reset: "Back to real time. Offset 0 day(s)". |

No screen showed the real-world date in place of the simulated one; notification stamps followed the simulated clock.
**Summary:** 9 Pass, 1 Partial.


# FS-25 — Create two accounts, confirm by email, sign in, recover a password — build 982952c (Staging)
Mode: Full (browser + Test1 Gmail). Run 12:14–12:29 AM ET, Nov 3, 2026, after a DB Stager reset.
Precondition: both addresses already have accounts, and the 4-user limit rules out new ones. Steps 5–7 and 11 are not run; per the plan, step 14 uses Forgot password. The Test1 password changed during the run is stored in `RUN-CONFIG.env` (a pointer to a secret file), not in this report. DB Stager's next reset restores the original.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | Signed out, the site redirects to `/login?returnUrl=%2F`. Tab title "Sign in · WarrantyBank". |
| 2 | Pass | `/terms` "Terms of Service", `/privacy` "Privacy Policy", `/disclaimer` "Disclaimer" all load with no sign-in wall. Each shows "Version 2026-10-01 · last updated October 1, 2026" and "Draft for review. This text has not yet been read by a lawyer. Items in [square brackets] are filled in before launch." |
| 3 | Pass | Empty submit gives per-field messages: Email "Enter a valid email address.", Password "Use at least 10 characters.", terms "Please agree to continue." No banner, nothing created. (Name and Confirm password show no message.) |
| 4 | Pass | A short password gives "Use at least 10 characters."; the email `abc` gives "Enter a valid email address." No stack trace or JSON. |
| 5–7 | Not run | Accounts already exist (see precondition). |
| 8 | Pass | Sign out goes to `/login`; Back and reload show only the Sign in form, no account data. |
| 9 | Pass | Wrong password for an existing email and for a nonexistent email both show "Invalid email or password." |
| 10 | Pass | Lands on Home ("Home · WarrantyBank"). Nav: Home, My Items, New Items, Returns, Notifications. |
| 11 | Not run | Account already exists. |
| 12 | Pass (**fixed since d1ed2c0**) | Signing up with the existing Test1 address shows the neutral "Check your email / We sent a link to <email>. Open it to finish creating your account. It works for 24 hours. Nothing is created until you do." The inbox gets "You already have a WarrantyBank account": "Someone tried to sign up for WarrantyBank with this email address, but you already have an account. Sign in, or reset your password if you have forgotten it…". The page no longer reveals which addresses are registered. |
| 13 | Pass | "If that email is registered, we sent a link to reset your password. It may take a minute to arrive." (sent 12:16:37 AM ET) |
| 14 | Pass | The email "Reset your WarrantyBank password" from StuffIt <noreply@stuff.microsaasbuilders.com> arrived within a second, linking to `stuffit-ui.onrender.com/reset-password`. The page "Choose a new password" accepted the new password: "Your password was changed. Sign in with the new one." The new password signs in; the old one gets "Invalid email or password." |
| 15 | Pass | Reusing the link: the form still renders, but submitting gives "This link has already been used or has expired. Request a new one." (Minor: the page could say this before you type a password.) |
| 16 | Pass | `nobody.uat@example.com` gets the identical neutral message as step 13. |
| 17 | Pass (**fixed since d1ed2c0**) | Requests at 12:26:54 and 12:27:02 AM ET, more than 10 minutes after step 13. Both landed in one Gmail thread. The older message has no "Requested at" line. The newest says "Requested at 12:27 AM. If you asked more than once, use the newest email." (ET, correct). The older link was refused: "This link has already been used or has expired. Request a new one." The newest link changed the password, and sign-in landed on Home. The two requests were 8 s apart, not 20 s; within the plan's 10-minute window. |

Notes: the reset page briefly flashes the Sign in screen before the form renders. The browser tool reported "Console: 2 errors" on the sign-up/sign-in pages (not investigated).
**Summary:** 13 Pass, 0 Partial, 0 Fail, 4 Not run (5, 6, 7, 11). Both d1ed2c0 fails (12 enumeration, 17 link order) are fixed.


# FS-26 — Add purchases, check suggested coverage, browse items, prove privacy — build 982952c (Staging)
Mode: Full (browser). Run 12:30–12:37 AM ET, Nov 3, 2026, after a DB Stager reset (Alice and Bob with no purchases; reference data loaded). All pages loaded in under 3 s (slowest about 1.4 s).

| # | Result | Evidence |
|---|---|---|
| 1 | Partial | `/add/new` (New Items, then "Add a purchase"). Field order: Store, "Date you bought it", "Credit card used", "Order number", **Category**, "Brand (optional)", "Item", "Model number". The plan expects category, brand, then item name; here Category comes before Brand, and the field is labelled "Item". Price is under "More about this item: price, size, serial number, notes" (matches). |
| 2 | Pass | "Add at least one item." and "Tell us what you bought."; nothing saved. |
| 3 | Pass | Best Buy, Ninja, "UAT Blender", 89.99, 11/03/2026. The coverage panel had "Best Buy return policy … Merchant 15 days Confirmed" pre-ticked, with "Usual window, can differ for your item. Check your receipt." and a Source link. "Ninja warranty Manufacturer 1 year Unconfirmed — Not added. Tick it to add it when you save…" was ticked; "Best Buy return policy: smartphones … 14 days Likely" was also listed. Saving opened the item. Category "Not sure" was filled in automatically as "Small appliances". |
| 4 | Pass | Read-only. "Bought Nov 3, 2026 from Best Buy", Price "$89.99", Date "Nov 3, 2026". Badge "Expiring soon" at 15 days left (a wide threshold; worth a look). |
| 5 | Partial | Return window "Nov 3, 2026 to Nov 18, 2026 · 15 days left" (3 + 15 = Nov 18, correct). Warranty "Nov 3, 2026 to Nov 3, 2027" (1 year, correct). **The doubt note "Usual window, can differ for your item" shows only on the add form, not on the saved item**, and there is no confidence score to hover. Suggest coverage (edit mode only): "Nothing new to suggest. Everything we know of is already added to this item." (it now responds, which it didn't on d1ed2c0). The return policy has a bestbuy.com Source link; the warranty has none and its terms read "[placeholder] Fake terms for testing, not from the manufacturer or the store." **Stale text:** Best Buy's policy says "Extended holiday return window for purchases October 31 to December 31 (2025 season: through January 15, 2026)", but a Nov 3, 2026 purchase gets 15 days, not the holiday window. |
| 6 | Pass | Edit mode: Done, Delete, Edit item, Edit purchase, Edit and Remove on each policy, Add coverage, Suggest coverage, a To do box, and "Add a receipt or other file / Choose files". |
| 7 | Pass | "UAT Blender 2" shows on the item and in My Items. |
| 8 | Pass | "Bought Oct 2026 (approximate)". No return window: "This return window ended 2026-10-30, so it cannot be added." Warranty "Ends between Oct 1, 2027 and Oct 31, 2027 (date estimated)". |
| 9 | Pass | During "Reading your document… This takes a few seconds. Keep this screen open." (about 7 s), Upload was disabled with the tooltip "Wait until the document has been read". Afterwards, "What we found in your document" asked questions: a store conflict (Keep yours: Best Buy, or Use the document's: UAT TEST STORE "(high confidence; new to us, added to your list)"), and "Order total 89.99", with the buttons "Keep 1 & Update 1", "Not now" and "Reject this document". Upload came back enabled after answering. |
| 10 | Pass | "Receipt / test-receipt.jpg (4 KB) / View / Read it / Delete". It went from 7 KB to 4 KB, so it was re-encoded (consistent with location data being removed). View opens it again. |
| 11 | Pass | "Toaster" and "Blender" each match only that item; no match shows "No items match." with Clear filters. |
| 12 | Pass | "Filter and sort" (Status, Sort by, Store, Brand, Category). "Expiring soon" leaves only Blender, with a badge of 1; "Clear all" restores both. |
| 13 | Pass | `/items/01a19fe4-6391-7b6c-8f6c-8c820da7fa44` |
| 14 | Pass | Bob: "Nothing here yet … Add your first purchase." |
| 15 | Pass | Bob on Alice's URL: "Not found.", tab "Item · WarrantyBank"; no title, price or store leaked. |
| 16 | Pass | Bob's UAT Kettle (Target, $19.00) saved: "Bought Nov 3, 2026 from Target", "Try first: Return window · Target". |
| 17 | Pass | Alice's search for "Kettle" shows "No items match." |
| 18 | Pass | "Delete this item? UAT Toaster and its coverage and files are removed. This cannot be undone." It leaves the list. No Undo offered (the plan allows this). |
| 19 | Pass | After a reload and signing out and back in, only UAT Blender 2 is listed; Toaster is gone. |

Other observations:
- A brand-new, empty account shows the bell "Notifications, 1 to do" with no purchases (probably the Quick set-up to-do).
- Greeting "Welcome, QA" and avatar "Q1" (app profile name; known).
- Uploading the receipt adds the receipt's store ("UAT TEST STORE") to the person's store list even when they keep their own store.

**Summary:** 17 Pass, 2 Partial (1, 5), 0 Fail. Compared with d1ed2c0, Suggest coverage now responds. The doubt note is present on the add form but not on the saved item.


# FS-27 — Cards, notifications and preferences, data export — build 982952c (Staging)
Mode: Full (browser plus the Test1 inbox). Run 12:41–12:48 AM ET, Nov 3, 2026. Before the run, DB Stager reset the accounts and staged Alice's "UAT Blender 2" (Best Buy and Ninja coverage); Bob was brand new.
**Steps 17, 18 and 20 were not run.** They delete Bob's account, which needs Steve's explicit OK.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | Bob's /notifications: "You are all caught up. New notices about returns, warranties and your account show up here." There is no standing card-benefits notice, so the empty state is allowed. On /cards the bell read "Notifications, 1 to do" for an account with nothing in it. |
| 2 | Pass | "Chase Freedom Unlimited", nickname UAT Card, ending 4242. Listed as "UAT Card · XXXX-XXXX-XXXX-4242 · Chase Freedom Unlimited" with "Extended warranty: Adds 1 year, up to 4 years total" and "Purchase protection: Covers 120 days from purchase". |
| 3 | Pass | Detail: "What you have confirmed for this credit card…"; both benefits show "Confirmed Nov 3, 2026". The label is Confirmed, not verified or unverified. |
| 4 | **Fail** | "UAT Mystery Rewards Card" (Citibank, ending 0001) saved with "UNVERIFIED", "⚠ No policy added" and "No policies on file yet. Open this credit card to search the internet for its terms." The detail page says "We do not have published benefits for this credit card." **No "Is yours one of these?" prompt** during the add or on the detail page; there is only a "Pick from our list instead" link. Unchanged from d1ed2c0. |
| 5 | Pass | "Your card UAT Card already ends in 4242. Receipts ending in 4242 are matched to that first card, so these digits were not added." No error page. |
| 6 | Partial | Notifications unchanged: the standing card notice never appears, before or after. Even an unverified card with no policy raises no notice, so the notice described in the plan doesn't seem to exist. |
| 7 | Pass | /settings/notifications: groups Expiring, Purchases, Summaries, Account, System alerts and Product news, each type with Email and In-app (Text is "coming soon"). "Account and security" and "Your files and data" are "Required" and locked: "Required: account, billing and security notices always reach you." |
| 8 | Pass | Warranty expiring Email off ("Saved", autosave) and Return window closing Email on; both persisted after a reload. |
| 9 | Pass | /settings/profile shows the Test1 email "(confirmed)", not editable. "Changing your name and password from here arrive in a later milestone." (/settings/email is the mailbox-connection page, not the sign-in email.) |
| 10 | Pass | /todos: "Nothing to do right now." /returns: "First design: example data", with sample returns (Sony, Ninja, Keurig, Bosch). |
| 11 | Pass (with caveat) | Used the real reminder "UAT24 Clock Shoes: return window ends in 6 days" from FS-24 (05:10 UTC today). It names the item and the right date (Dec 3, 2026, simulated clock) and has Unsubscribe and Manage links. The item has since been reset away. |
| 12 | Pass | The page "Email preferences": "You are getting emails about Return window closing. What would you like to stop?" offers just this type, all "Expiring", or all optional emails. Then "Done. No more “Return window closing” emails. Required notices about your account, payments and security still reach you." Settings agrees: Return window closing Email is off. |
| 13 | **Fail** | "Prepare my download" goes "Preparing your download…" then "Nov 3, 2026 · Ready until Nov 10, 2026" with "Download (4 KB)". Clicking Download gives "**That download is no longer available. Prepare a new one.**" A retry did the same. Marked ready, but the file can't be fetched. This is the same storage-delivery failure as FS-40 step 7 (Cloudinary PDF/ZIP delivery appears to be off). |
| 14 | Not run | No file (blocked by step 13). |
| 15 | Pass | /settings/privacy "Delete my account": "This permanently deletes: your purchases, items, coverage and credit cards / every receipt and file you uploaded / your notifications, settings and sign-in / stores, brands and policies you added for yourself. Shared knowledge other people rely on stays. A paid plan is cancelled first. This cannot be undone. Download your data first if you want a copy." Requires typing the email and the password; the button stays disabled until both are filled. |
| 16 | Pass | No Cancel button. Leaving the page deletes nothing; still signed in, cards intact. |
| 17, 18, 20 | Not run | Needs Steve's OK to delete Bob. |
| 19 | Pass | Alice's UAT Blender 2 is still listed. |

**Summary:** 13 Pass, 1 Partial (6), 2 Fail (4 and 13), 4 Not run (14, 17, 18, 20).
The delete warning still says "Download your data first", which isn't possible while the export fails.


# FS-28 — Administrator sign-in with two-step, and the shared data screens — build 982952c (Staging)
Mode: Full (browser). Run 12:49–12:52 AM ET, Nov 3, 2026, after a DB Stager reset (Ops two-step and operator role preserved). Pages took about 1 s or less; sign-in submit about 2.5 s.
Steps 1–3 were skipped because two-step is already set up (as the plan allows). Codes came from the setup key in `RUN-CONFIG.env`; no codes or keys are in this report.

| # | Result | Evidence |
|---|---|---|
| 1–3 | Skipped | Two-step already on. Settings > Security shows "Two-step sign-in is on." and "You have 10 recovery codes left…". The Administrators list shows admin@microsaasbuilders.com "Two-step on", Ops "(you)" "Two-step on", and stuffit-admin@microsaasbuilders.com "Two-step not set up". |
| 4 | Pass | Nav: Review, Companies, Shared data, Feedback; "ADMIN" badge; "Customer view" button. |
| 5 | Pass | "Enter your authenticator code." with field "Authenticator code", hint "The 6 digits from your authenticator app, or one of your recovery codes." |
| 6 | Pass | `000000` gives "That code is not correct." Not signed in. |
| 7 | Pass | Lands on `/admin`, headed "Shared data". |
| 8 | Pass | Customer view goes to `/` (Home, My Items, New Items, Returns, Notifications; "Welcome, QA"). "Admin view" returns to `/admin`. |
| 9 | Partial | "Shared stores, brands and issuers" / "Reference data everyone sees. Changes here are versioned and audited." Search placeholder "Best Buy, Dyson, Chase…". Show filter: Everything, Stores, **"Brand (maker)s"** (typo, still there), Credit card issuers, Warranty providers. "Home Depot" shows "Home Depot Verified Store"; "Milwaukee" shows "Milwaukee Not verified Brand"; the private "UAT TEST STORE" shows "Nothing matches. Add it above." (shared only, correct). Each store or brand shows "Verified", "Not verified" or "Needs data". Issuers and warranty providers show no status. **No row count.** 200 rows render, which looks like a cap. No verified-only filter (unchanged since d1ed2c0). |
| 10 | Pass | `/admin/parties/01a0f4e4-…`: "Home Depot · Store · Shared", website homedepot.com, policies "Everything else – 90 days" and "Major appliances – 2 days", both "Current" and "Verified: Checked against the official source on Oct 24, 2026.", each with a Source link to homedepot.com/c/Return_Policy, "Correct a mistake" and "This no longer applies". |
| 11 | Pass | Companies: type list (Retailers; Brands; Credit cards "(not built yet)"; Extended warranty sellers "(not built yet)"), with "Find return policy" on each row. Review: "Not built yet. Planned in S7.1.2 (review queues) and S7.1.3 (admin home)." Feedback: "0 new · 0 shown", Status and Type filters, "No messages match." (now built). |
| 12 | Pass | Bob: no Admin badge, no Admin view, no Security tab (Settings tabs: Profile, Stores & brands, Notifications, What to track, Email, Appearance, Credit cards, Privacy & data, Plan & billing). |
| 13 | Pass | Bob's `/admin`, `/admin/companies`, `/admin/review` and `/admin/feedback` all go silently to `/`; `/settings/security` goes to `/settings/profile`. No admin data shown. |
| 14–18 | Not run | API steps (optional). I have no API token for Ops or Bob without reading passwords into a script; left for API mode. |

Other observations: Profile reads "Changing your name and password from here arrive in a later milestone." (grammar). The time zone list is very long. The browser tool reported 1 console error on /login.
**Summary:** 10 Pass, 1 Partial (9), 0 Fail; 3 skipped (1–3), 5 not run (14–18, optional API).


# FS-29 — Start a return, work the returns list, mark it returned — build 982952c (Staging)
Mode: Full (browser). Run 12:52–12:57 AM ET, Nov 3, 2026, after a DB Stager reset (nothing staged).

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | Drill and Saw (Home Depot, "Merchant 90 days Confirmed") and Kettle (Target, "Merchant 90 days Confirmed"), all dated Nov 3, 2026. Each item shows "Return window, Feb 1, 2027 · Until Feb 1, 2027" (Nov 3 + 90 = Feb 1, correct). The Drill form also offered an unticked "Home Depot return policy: major appliances … 2 days Likely" for a power tool. Category auto-filled. |
| 2 | Pass | "Returns in progress" / "Nothing to return right now." / "Open an item and choose Start a return; it will show up here until you mark it returned." |
| 3 | Pass | "Start a return" is on all three items. |
| 4 | Pass | "Return in progress since Nov 3, 2026. It is on your returns list until you mark it returned." with Mark returned and Cancel return. Status still Active, coverage unchanged, Start a return gone. |
| 5 | Pass | The note persists after a reload. |
| 6 | Pass | Same note on the Saw and the Kettle. |
| 7 | **Partial** | Rows: Drill, Kettle, Saw (all end Feb 1, 2027). Each reads like "UAT Return Drill / Until Feb 1, 2027 / Home Depot · Bought Nov 3, 2026 · $120.00 / Return window ends Feb 1, 2027". **No days-left badge** (the badge says "Until Feb 1, 2027"). Unchanged since d1ed2c0. |
| 8 | Pass | "Home Depot 2 items · $200.00" (Drill, Saw) and "Target 1 item · $30.00"; the store leaves the row text; unticking restores the list. |
| 9 | Pass | The Kettle row opens the item. |
| 10 | Pass | Cancel return: the note goes, Start a return is back, no "The return" summary. |
| 11 | Pass | Drill and Saw only. |
| 12 | Pass | "Mark as returned": Date 2026-11-03; Refund 120 ("Leave empty if the money has not come back yet."); Paid back by: Not sure / not yet (default), Back to the original payment, Store credit, Gift card, Exchange, Cash, Check, Other; How hard 1–5 ("1 is easy, 5 is very hard."); Problems getting paid is a free-text box. |
| 13 | Pass | Submit is disabled while the date is empty. |
| 14 | Pass | "Returned Nov 3, 2026 / Refund $100.00 · Store credit / How hard 2 of 5 · Fairly easy / Problems Restocking fee". Status "Returned". Money recovered shows "$100.00 · Store refund · Nov 3, 2026 · Store credit · credit, not cash". |
| 15 | Pass | Mark returned and Start a return are gone; "I have it again" is offered. Nothing about reminders; the coverage still reads "Covered 1 policy". |
| 16 | Pass | Only the Saw remains. |
| 17 | Pass | Edit gives "Refund $110.00 · Store credit"; Money recovered updated to $110.00. |
| 18 | Pass | "I have it again": status Active, Start a return back, not on the returns list. **"The return" summary and its Money recovered entry are removed** ("Nothing recorded yet."). |
| 19 | Pass | Bob: "Nothing to return right now."; nothing of Alice's. |
| 20 | Pass | Bob on Alice's Saw URL: "Not found.", tab "Item · WarrantyBank". |
| 21 | Pass | Returned with no amount: "Returned / Nov 3, 2026 / Refund / Not paid yet". Status Returned; the in-progress list is empty. |

/returns (menu) is still "First design: example data" (Sony, Ninja, Keurig, Bosch); none of Alice's items appear.
Bob's bell says "Notifications, 1 to do" on an empty account (as in FS-26 and FS-27).
**Summary:** 20 Pass, 1 Partial (7), 0 Fail.


# FS-30 — Record a renter's policy, link items, see the notes on the item — build 982952c (Staging)
Mode: Full (browser plus the live document reader). Run 12:58–1:05 AM ET, Nov 3, 2026. Before the run, DB Stager reset the accounts and staged Alice's UAT Guitar ($1,800, Musical instruments), UAT Laptop ($1,200, Computers) and UAT Lamp ($40, Home utility). All three are hand-added Best Buy purchases with the Best Buy return window.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | "Insurance" / "No policies yet." / "Add the policy you have, even if you are not sure what it covers. You can type in the limits it lists for things like instruments or electronics." / "Add your first policy". |
| 2 | Partial | Nothing saved, but only "Choose the insurer." is flagged. Name, Policy number and Ends aren't called out (Starts is prefilled with today). |
| 3 | Pass | Inline `Add "UAT Insurer"` gives "UAT Insurer UNVERIFIED". The other fields were accepted. |
| 4 | Pass | Field error "The end date cannot be before the start." plus the generic banner "One or more validation errors occurred." Nothing saved. |
| 5–6 | Pass | Premium, deductible and property limit were accepted. The blank third limit row is **ignored** (not flagged); the two real limits are kept. |
| 7 | Pass | Saved; it opens read-only at `/insurance/01a19ffe-…`. |
| 8 | Pass | "Renter's · UAT Insurer · policy UAT-001"; badge "Until May 3, 2027"; Term "May 3, 2026 to May 3, 2027 · renews automatically"; "$240.00 a year"; Deductible $500.00; Personal property limit $20,000.00; phone `tel:800-555-0100`; "Make a claim online"; "Electronics: $2,500.00", "Musical instruments: $1,500.00". |
| 9 | Pass | "All your items except the ones left out below: 3 items, which cost $3,040.00." / "No exceptions: every item is covered." (1800 + 1200 + 40 = 3040, correct.) |
| 10 | Pass | "Covered, under Musical instruments ($1,500.00), listed at $1,800.00". |
| 11 | **Fail** | **No notes on the policy page**: no over-limit note for the $1,800 Guitar against the $1,500 limit, and no "not advice" line (even after a reload). Unchanged from d1ed2c0. |
| 12 | **Fail** (the note only) | The Guitar's card shows "UAT Renter's policy · UAT Insurer · until May 3, 2027", "Deductible $500.00. Limit for Musical instruments: $1,500.00. Listed on the policy at $1,800.00.", "Call 800-555-0100" and "Make a claim online". **No over-limit note.** |
| 13 | Pass | The Lamp's card shows the policy and "Deductible $500.00.", with no instrument limit. |
| 14 | Pass | The Lamp shows "Left out"; "2 items, which cost $3,000.00."; the Lamp's Insurance card is gone. Its "Covered 1 policy" is the Best Buy return window, which is correct (the stale-count finding from d1ed2c0 doesn't apply). |
| 15 | Pass | "Only the items you link below: 1 item, which costs $1,800.00." |
| 16 | Pass | "$240.00 a year for the policies still running." Row: "UAT Renter's policy · Until May 3, 2027 · Renter's · UAT Insurer · covers 1 item · $500.00 deductible · renews automatically". |
| 17 | Pass | Reader on. "Reading your document…" disabled for about 5 s. "What we found … Nothing is filled in until you press the button…": Insurer UAT Mutual Insurance Co., Policy number UAT-777, Type Renters, Start 2026-05-01 / End 2027-05-01 ("Check this one"), Premium 180 Annual, Deductible 250, Personal property 15000, Special limits Jewelry 1000, Claim phone 800-555-0199. Each shows a quote and page; all were correct. "The document did not say: Items listed separately, Claim website." Nothing was pre-filled. |
| 18 | Pass (oddity) | Only the ticked Policy number filled ("UAT-777"); Deductible stayed empty. Note: "Filled in from your document. Read the form over and fix anything that is wrong, then save." **Oddity:** Name also became "Renter's policy" without being accepted. Suggestions are tick boxes, all pre-ticked, rather than accept or dismiss per item. |
| 19 | Pass (gap) | Navigating with typed changes: "Leave without saving? You have changes that have not been saved. If you leave this page now they will be lost." (Stay / Leave). **Gap:** the form's own Cancel button discards changes with no warning. |
| 20 | Pass | Bob: "No policies yet."; Alice's policy URL shows "Not found." with no details. |
| 21 | Pass | "Delete this policy?" / "This removes UAT Renter's policy, its limits, its documents and its link to your items. The items themselves stay." The list is empty and the Guitar has no Insurance card. (Delete is a "Delete this policy" button, not a trash icon.) |

No wrong amounts, no wording that reads like advice to buy, and no date disagreeing with today.
**Summary:** 18 Pass, 1 Partial (2), 2 Fail (11, 12: the over-limit note is still missing).


# FS-31 — Record a third-party warranty plan and cover items with it — build 982952c (Staging)
Mode: Full (browser plus the live document reader). Run 1:08–1:13 AM ET, Nov 3, 2026. Before the run, DB Stager reset the accounts and staged Alice's UAT Fridge ($900) and UAT Washer ($600), hand-added Best Buy purchases with the Best Buy return window.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | "Extended warranties" / "No plans yet." / "…A plan bought at the store for a single item is added on that item instead." / "Add your first plan". |
| 2 | Partial | Nothing saved, but only the banner "Choose the company that sold the plan." Name and Ends are not called out. |
| 3 | Pass | Inline `Add "UAT Home Warranty Co"` creates the company (shown "UNVERIFIED"). |
| 4 | Pass | "The end date cannot be before the start." plus the generic banner "One or more validation errors occurred."; nothing saved. |
| 5–6 | Pass | Saved; opens read-only at `/plans/01a1a005-…`. |
| 7 | Pass | "Sep 3, 2026 to Sep 3, 2027"; "$30.00 a month ($360.00 a year)"; Per service call "$75.00"; `tel:800-555-0111`; "Make a claim online"; "Refrigerators, washers, dryers"; "Exclusions and limits: Cosmetic damage". |
| 8 | Pass | "UAT Fridge · $900.00", "UAT Washer · $600.00"; "No items yet." gone. |
| 9 | Pass | "UAT Home Warranty Co · 2 items · $360.00 a year"; "$360.00 a year for the plans still running, covering items that cost $1,500.00 in all." |
| 10 | Pass | Fridge: "Covered · 2 policies"; Return window first ("Try this first"), then "Extended plan · UAT Home Warranty Co, Sep 3, 2026 to Sep 3, 2027 · Until Sep 3, 2027, UAT Home protection. Refrigerators, washers, dryers, Call 800-555-0111, Make a claim online". |
| 11 | Pass | "Stop covering this item? UAT Washer will no longer show UAT Home protection as a coverage. The item itself stays." Then "1 item", "$900.00 in all". |
| 12 | Pass | "test-receipt.jpg (4 KB)" (re-encoded from 7 KB); View opens the image; "Delete this file? … This cannot be undone." leads to "No files yet." (Images work; PDF/ZIP delivery is what fails in FS-27 and FS-40.) |
| 13 | Pass | "$25.00 a month ($300.00 a year)". |
| 14 | Pass | Reader on: "Reading your document…" (disabled). Correct values: company UAT APPLIANCE SHIELD LLC, Appliance Shield Gold, 2026-06-01 ("Check this one") to 2027-06-01, 19.99 monthly, fee 60, covers, exclusions, phone 800-555-0122. The website "www.example.com/shield" is flagged "That is not a web address starting with http or https.". Nothing is filled before accepting. Cancel left with **no unsaved-changes warning** (same gap as FS-30 step 19). |
| 15 | Partial | "Update from a newer document" lists **all 8 values, not only those that differ** (an unchanged price of 25 and phone are listed too), all pre-ticked. With only the service call fee accepted, it shows "Fee per service call: $75.00 → $95.00" and saves $95.00; covers stayed unchanged. The v2 file was attached automatically ("Keep these files with the plan when I save it" is on by default). |
| 16 | Pass | "It ended on" is empty and "End this plan" is disabled. "Tell us the day it ended and every covered item stops showing it as active from then." |
| 17 | Pass (**fixed since d1ed2c0**) | The date box starts empty (it used to be prefilled with today). "Plan ended." Badge "Ended Nov 3, 2026"; term "Sep 3, 2026 to Nov 3, 2026". List row "Ended Nov 3, 2026 / … · 1 item · $300.00 a year"; the total is now "$0.00 a year for the plans still running, covering items that cost $0.00 in all." (The ended plan is excluded; this used to be a fail.) Whether the row is dimmed was not confirmed. |
| 18 | **Partial** | The Fridge still treats the plan as running today: "Sep 3, 2026 to Nov 3, 2026 · **Ends today**", "Covered 2 policies", "Next to end: Extended plan, Nov 3, 2026 · Ends today". This contradicts the plan's own "Ended" badge. Same as FS-40 step 6. |
| 19 | Pass | Bob: "No plans yet."; Alice's plan URL shows "Not found." |
| 20 | Pass | "Delete this plan? This removes UAT Home protection, its contract files and the plan coverage on 1 item. The items themselves stay." The list is empty; the Fridge shows "Covered 1 policy" (the return window). |

All money figures are consistent ($30 × 12 = $360, $25 × 12 = $300, $900 + $600 = $1,500).
**Summary:** 17 Pass, 3 Partial (2, 15, 18), 0 Fail. Fixed since d1ed2c0: the yearly total drops an ended plan, and the end-date box starts empty.


# FS-32 — General reminders on an item and on the To do page — build 982952c (Staging)
Mode: Full (browser plus email; clock for step 12). Run 1:14–1:19 AM ET, Nov 3, 2026, after a DB Stager reset. Staged: Alice's "UAT Reminder Blender" (Best Buy, today, hand-added, no open to-dos).

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | "To do" / "Nothing to do right now." / "Reminders such as registering a warranty show up here, and on the item they belong to." with a link to Your items. |
| 2 | Pass | Read-only item: no To do card. |
| 3 | Pass | Edit shows the "To do" card with "Add a reminder" (placeholder "For example: register the warranty") and "Due (optional)" (date). Add is disabled while the title is empty. |
| 4 | Pass | "Register the warranty" shows "Due in 5 days" (orange); "Keep the box" has no label. |
| 5 | Pass | "Check the cord" shows "Overdue since Nov 2, 2026". **The colour is neutral slate grey** (class `badge-expired`), so it is less urgent-looking than the orange due-soon badge. Worth a look. |
| 6 | Pass | After Done, the card stays with all three plus "Show done and dismissed (1)". |
| 7 | Pass | /todos lists the same three, each linking "UAT Reminder Blender" to the item. |
| 8 | Pass | Mark as done removes it from both pages; it shows under "Show done and dismissed" with "Reopen". |
| 9 | Pass | Dismiss for now: "Dismissed until Nov 10, 2026" (7 days) with "Undo", found under the done-and-dismissed toggle. No wording says it will come back. |
| 10 | Pass | Not applicable: leaves the list; recoverable through "Not applicable" plus "Undo". |
| 11 | Pass | After reload nothing returns; "Show done and dismissed (4)". |
| 12 | Partial | A to-do due Nov 4; clock +1 day; run-reminders reported `Todos = 1`. Email "To do today: Clock reminder test", body "Clock reminder test is due today, on November 4, 2026." plus "See your to-dos". The in-app bell entry has the same title and body. A second run sent nothing (`Todos = 0`), so it is once only. **Neither the email nor the bell entry names the item** ("UAT Reminder Blender" is absent). /todos shows "Due today" with the item link. Clock reset to offset 0 afterwards. |
| 13 | Pass | Bob: "Nothing to do right now."; no toggle; none of Alice's reminders. |
| 14 | Pass | Bob on the Blender URL: "Not found."; no to-dos. |

**Also recorded:** a double click on Add creates one reminder (good). Due-soon reads "Due in N days" / "Due today" / "Due in 1 day"; overdue reads "Overdue since <date>".
**Oddities:**
- The bell's "1 to do" is the credit-card notice ("Add a credit card and confirm its benefits"), not the to-do list. It stays at 1 whatever the To do page holds, which is confusing next to the To do page.
- A read-only item with only done or dismissed reminders still shows the To do card, holding just the toggle.
- The unsubscribe link in the to-do email carries the category `purchase_needs_info`, so unsubscribing from it may turn off the wrong email type.
- The reminder was sent at about 1:17 AM local app time (the reminder rule says 9:00 local).

**Summary:** 13 Pass, 1 Partial (12), 0 Fail.


# FS-33 — Set what is worth tracking, and New Items follows it — build 982952c (Staging)
Mode: Full (browser). Run 1:19–1:24 AM ET, Nov 3, 2026, after a DB Stager reset (New Items empty, threshold unset).
Receipt: `12-thermal-long-many-items.pdf` (Pine Street Hardware, 06/22/2026), 12 lines: Stud x24 $110.16, Deck screws x2 $65.98, Wood glue $6.99, Sandpaper x5 $12.45, Interior paint x3 $116.97, Roller cover x2 $17.98, Painters tape x4 $23.16, Tarp $18.99, LED bulbs x2 $21.98, Extension cord $24.99, Dishwasher supply line $14.99, Work gloves x2 $25.98.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | Tabs: "Profile", "Stores & brands", "Notifications", "What to track", "Email", "Appearance", "Credit cards", "Privacy & data", "Plan & billing". |
| 2 | Pass | Heading "What is worth tracking"; text "Track things worth at least this much. Smaller lines on a receipt are listed under "Smaller things" in New Items and are not ticked for you. Nothing is hidden or deleted, and one click tracks any of them."; field "Track things worth at least" = 50; note "Using the standard amount, $50.00. Zero tracks everything."; buttons "Everything", "Only larger purchases", "Use the standard amount", "Save". |
| 3 | **Partial** | The upload took ~25 s ("Uploading and reading your receipt…"). Main list (4): Interior paint, Deck screws, Stud and **Work gloves · L $25.98, which has the badge "Under $50" but is not demoted**. "Smaller things (8)" (collapsed): "Probably not worth a warranty: under your tracking minimum, or past the limit of lines shown up front from one receipt. Track any you want, or dismiss the rest together." Reasons such as "Still to check. Under your $50 minimum." / "Under $50 · used up, much cheaper than the rest", "Under $50 · cord". |
| 4 | Pass | Everything sets the field to 0. |
| 5 | Pass | "Saving…" then "Saved" ("Saved." announced). No separate toast. |
| 6 | Pass | Still 0; the note now reads "The standard amount is $50.00. Zero tracks everything." |
| 7 | Pass | Smaller things (2): Wood glue and Sandpaper, now with the reason "Cheaper than the lines kept" (relative-price rule, not the minimum). 6 lines moved to the main list (supply line, cord, bulbs, tarp, tape, roller cover). Nothing had been accepted. |
| 8 | Pass | Only larger purchases gives 250, Saved. Smaller things (11) of 12; reasons name the amount ("Under your $250 minimum.", "Under $250 · used up"). Again **Work gloves stays in the main list** with the badge "Under $250". |
| 9 | Pass | 100001: "Not saved" / "Choose an amount from 0 to 100,000."; 250 kept after reload. |
| 10 | Pass | -5: same refusal; 250 kept. |
| 11 | Pass | A blank field is treated as the standard amount: 50, "Saved", note "Using the standard amount, $50.00." No error. |
| 12 | Pass | 20: Smaller things (5) are Wood glue $6.99, Sandpaper $12.45, Supply line $14.99, Tarp $18.99, Roller cover $17.98, all under $20 ("Under your $20 minimum."). Every line of $20 or more is in the main list. |
| 13 | Pass | Use the standard amount gives 50, "Saved", note "Using the standard amount, $50.00." New Items matches step 3 exactly (8 down, the same 4 up). |
| 14 | Pass | (Alice set to 250 first.) Bob shows 50, "Using the standard amount, $50.00. Zero tracks everything." |
| 15 | Pass | Bob's New Items: "Nothing waiting. Forward a receipt or order email to your WarrantyBank address, upload a receipt, or add a purchase yourself." No Pine Street lines. |
| 16 | Pass | Alice, signed in again: 250 is kept. |

**Also recorded:** the reason text does mention the amount set ("Under your $250 minimum."). Pages load in under 3 s except the receipt read (~25 s, within "up to half a minute"). The list briefly shows "Showing 0 of 0" before it fills in.
**Bug:** a $25.98 line (Work gloves, x2 at $12.99) is never put under Smaller things at $50 or $250, though its own badge says "Under $50" / "Under $250". Possibly a "keep at least one line up front" rule; if so, it should say so. Interior paint ($116.97) is called "used up" at $250.
**Summary:** 15 Pass, 1 Partial (3, the Work gloves line; the same issue shows at 8), 0 Fail.


# FS-34 — Color theme and light or dark — build 982952c (Staging)
Mode: Full-only (browser). Run 1:27–1:32 AM ET, Nov 3, 2026. Site data was cleared first. The theme lives in localStorage `stuffit.theme` as `{theme, mode}`; nothing is in the database (DB Stager confirmed).

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | Card "Appearance"; "Color theme" offers Teal, Indigo and Berry, each with a swatch dot; "Light or dark" offers "Match my device", "Light" and "Dark". Teal and "Match my device" are selected by default, with "Using light because that is your device's setting." Note: "This choice is kept on this device. It is not yet saved to your profile, so other devices keep their own." |
| 2 | Pass | Indigo applies at once (logo, avatar, tab underline, card accents, headings, links, page tint). |
| 3 | Pass | Home, /items, New Items, the item page and Settings are all Indigo with no teal left. Fixed colours that stay put, which look like deliberate status colours: the /items card's light-blue background and blue left border; badges "Expiring soon" and "15 days left" (orange) and "Covered" (green); on Home, the "Link your email" button (blue) and "Add an item" (orange). |
| 4 | Pass | Berry and then Teal each apply at once; Teal matches the start. |
| 5 | Pass | Dark is readable on Home, the item page, New Items and Settings, with no bright patches. Checked the select, the "Alpha test." banner, the "Quick set-up is not finished" box and the badges. Text inputs in dark mode were only lightly checked. |
| 6 | Pass | Light comes back; the "Using…" line hides. |
| 7 | Pass | "Using light because that is your device's setting." With DevTools emulating a dark device, the app follows at once: "Using dark because that is your device's setting." |
| 8 | Pass | Berry plus Dark, then reload: no flash. An inline head script sets `data-theme="berry" data-mode="dark"` before first paint. |
| 9 | Pass | A new tab is still Berry and dark. |
| 10 | Pass | The sign-in page uses the saved theme (Berry, dark). |
| 11 | Pass | Bob in the same browser sees Berry and dark (the theme follows the device). |
| 12 | Pass (limited) | A private window with no earlier choice shows Teal on light (device light), with no Berry. Bob's sign-in in the private window was not completed (the test tooling can't fill the private window); the theme there doesn't depend on the account. |
| 13 | Pass | Clearing the site data brings back the default Teal light; the page works (only the expected 401 on `/api/auth/refresh` while signed out). |
| 14 | Pass | At 375 px the choices wrap without sideways scrolling. The Settings tab strip scrolls inside itself (cut off at "Wl…"). |
| 15 | Pass | /terms and /disclaimer in Berry dark are themed and readable. |

**Summary:** 15 Pass, 0 Partial, 0 Fail. No flash of the wrong theme; the only fixed colours are status and category badges and two Home buttons.


# FS-35 — Send feedback and see your messages — build 982952c (Staging)
Mode: Full (browser). Run 1:34–1:36 AM ET, Nov 3, 2026, after a DB Stager reset (no feedback rows for any QA persona). Alice has "UAT Feedback Blender".

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | Footer link (`/feedback?from=…`); Account menu "Quick set-up, Bring in purchases, Credit cards, Extended warranties, Insurance, Send feedback, Settings, Sign out"; the `/account` card "Send feedback – Ask a question, suggest something or report a problem." |
| 2 | Pass | "Send feedback". "What will be sent with your message": "Page you were on: /items", "App version: 982952c", "Nothing else about your items, purchases or cards is sent." No Item line. "You have not sent any messages yet." |
| 3 | Pass | "Page you were on: /items/01a1a01c-…", "Item: 01a1a01c-9074-7eea-8e46-a4b3afc78de4". |
| 4 | Pass | "Write a message first."; nothing changed. |
| 5 | Pass | "Sending…", then "Thank you. We received your message."; the form clears (counter "0 / 4,000"). |
| 6 | Pass | "Question · Nov 3, 2026 / Received / UAT question one". |
| 7 | Pass | Problem, Suggestion, Question, newest first, all "Received". |
| 8 | Pass | All three are kept after reload. |
| 9 | Pass | Typing stops at 4,000: "4,000 / 4,000 · That is the most we can take. Shorten your message to send it." No error. |
| 10 | Pass | `<b>bold</b> & "quotes"` shows literally; not rendered. |
| 11 | Pass | The 5th message ("UAT five") is accepted. |
| 12 | Pass | 6th refused: "You have sent several messages in the last hour. Please try again a little later." Nothing added; the typed text stays. (The wording says "several", not the number.) |
| 13 | Pass | Bob: "You have not sent any messages yet."; none of Alice's. |
| 14 | Pass | Bob's message is accepted and listed alone (Alice's limit doesn't apply). |
| 15 | Pass | Alice sees only her 5. |
| 16 | Pass | `?from=https://example.com/x` gives "Page you were on: none". |
| 17 | Pass | Signed out, it redirects to `/login?returnUrl=%2Ffeedback`; nothing shown. |

Nothing took over 3 s (the slowest was 2.99 s, opening feedback from the item page).
**Summary:** 17 Pass, 0 Partial, 0 Fail.


## FS-36 Claim guidance wizard (Full-only) — Alice, Bob

Staging note: DB Stager's first hand-written coverages (source 'Manual') made GET /api/items and /api/items/<id> return 500 for Alice. They were replaced: the Blender coverages were added through the UI (ticked the 2 suggestions), and the other three were copied from those with source 'Default'. This was a staging problem, not an app bug. Side finding: coverage source values outside the expected set crash the whole items list with a 500 rather than failing gracefully.

| # | Result | Actual (quoted) |
|---|---|---|
| 1 | Pass | Header "Edit / Refund / Mark returned / Mark disposed"; panel "Need to return it or make a claim?" with "Start a refund or claim" |
| 2 | Pass | "Step 1 of 3"; all 7 reasons with lines ("It works, I just do not want it.", "A defect or a failure.", "Damage you did not cause.", "Wrong item, missing parts, not as described.", "A lower price after I bought it.", "A drop, a spill, a crack.", "I no longer have it."); Next disabled until a reason is chosen |
| 3 | Pass | "Step 2 of 3", "A few quick questions", "We already know what you bought, where and when, so we only ask what changes the answer. Not sure is always fine." Questions: used as intended; can you read the serial number (shown, since no serial is saved); still have the receipt. Button "See my options" |
| 4 | Partial | Intro exactly "You said It does not work or it broke. Here is what may apply to your UAT Blender, best option first." (fix confirmed). But the result page has no "Step 3 of 3" label |
| 5 | Partial | "Return window · Best Buy / Best option / Applies", "15 days left (until Nov 17, 2026)" (no holiday window), 4 steps, have-ready "Your receipt or order confirmation: You have it", "The order number: Not on file", label as expected. Warning text: "Once the item is returned you no longer own it, so the maker's warranty and any card protection for it usually end too." (red colour not verified) |
| 6 | Pass | "Manufacturer warranty · Cuisinart / Applies", "365 days left (until Nov 2, 2027)", have-ready as expected, "General guidance for a maker's warranty claim. We have not checked Cuisinart's own page." |
| 7 | Fail* | Ticks are not kept; a reload goes back to "Step 1 of 3" with answers cleared. *The plan only says to record it. Losing the whole wizard state on reload is worth a look |
| 8 | Pass | "StuffIt shows what companies have published and general guidance. The company decides every claim and return, its terms can change, and this is not legal advice. Nothing is sent for you, and no one can promise a request will be approved." No "will be approved" |
| 9 | Pass | Intro "You said I changed my mind. ..." (capitals kept). Best Buy "Might apply", no badge: "...depends on something you were not sure about: the item is unopened, or still like new." Cuisinart "Does not apply": "The maker's warranty does not cover changing your mind." (dimming not verified) |
| 10 | Pass | Best Buy "Might apply": "The return window may not accept this without it: the item is unopened, or still like new. Check the company's own page." |
| 11 | Pass | No price-protection route. Best Buy Might apply; Cuisinart "does not cover finding it cheaper elsewhere." |
| 12 | Partial | Card Item: "Nothing we know of covers this"; "Credit card: Purchase protection · Chase / Does not apply: The card's purchase protection does not cover something that stopped working." Offered "Ask Best Buy whether it will make a courtesy return or exchange, even though the return window has passed." **Wording bug:** the item was bought Nov 2 and has no return-window coverage, yet the text says the window "has passed". No card route with days/steps, because only PurchaseProtection was staged, and the extended-warranty benefit is not a coverage here |
| 13 | Pass | "Extended plan · SquareTrade / Might apply", "1096 days left (until Nov 2, 2029)", 3 steps, "General guidance for a protection plan claim. We have not checked SquareTrade's own page." |
| 14 | Pass | Ended Item: "Nothing we know of covers this"; Cuisinart "Does not apply": "The maker's warranty ended on Sep 15, 2026." Offers goodwill and courtesy requests labelled "A request, not a right" |
| 15 | Pass | Marked returned (Nov 2, $89.99); Refund link and panel gone |
| 16 | Pass | "This item is already marked returned or gone, so there is nothing left to return or claim on." + "Back to the item" |
| 17 | Pass | As Bob: "Not found." on both /items/<id>/refund and /items/<id>; nothing of Alice's item shown |
| 18 | Pass | "Design mock with sample data. Nothing here is saved or sent." Note: the mock still lists the old 6 reasons, including "Something else" (the real wizard has 7). That's cosmetic |
| 19 | Pass | Redirect to /login?returnUrl=%2Fitems%2F...%2Frefund (the /items/sample/refund mock also requires sign-in) |

Route order: Best Buy, then Cuisinart, every time. Nothing over 3 s. No legal-advice or promise wording, and no store-specific steps.


## FS-37 Money recovered (API+Full, run in Full) — Alice, Bob

| # | Result | Actual (quoted) |
|---|---|---|
| 1 | Pass | Prompt: "Nothing recorded this year. Got money back? Open the item and choose Mark refunded." No amount |
| 2 | Pass | "Mark refunded", "Add a card payout"; "Nothing recorded yet. Add it when the money comes back." |
| 3 | Pass | "$120.00 · Store refund · Nov 2, 2026 · Back to the original payment / UAT refund"; item Returned |
| 4 | Pass | "$120.00on 1 item", "$120.00 in cash". Cosmetic: there's no space between "$120.00" and "on" |
| 5 | Pass | "$180.00on 2 items", "$120.00 in cash · $60.00 in store credit and gift cards"; the row is tagged "credit, not cash" |
| 6 | Pass | "$45.00 · Card payout"; item stays "Needs info"; "$165.00 in cash · $60.00 in store credit and gift cards" |
| 7 | Pass | Two rows; "$173.99 in cash"; still Returned |
| 8 | Pass | "$174.99 in cash" |
| 9 | Pass | "Remove this?" with Keep it / Remove; "$165.00 in cash"; still Returned |
| 10 | Pass | One mirrored row, "$200.00 · Store refund"; "$365.00 in cash" (not 565) |
| 11 | Pass | The row follows the edit to $190.00; "$355.00 in cash" |
| 12 | Pass | "Remove the $190.00 you recorded? It will no longer count toward what you have recovered." then "Do you have the item again?" / "If the refund did not come through and you still have it, we can mark it as owned again and restart its reminders." with "No, leave it returned" / "Yes, I have it". Chose No: stays Returned, refund line shows "Not paid yet", Home "$165.00 in cash". Minor: the first Remove click seemed to do nothing |
| 13 | Partial | A future date is refused, nothing saved, but the message is the generic "One or more validation errors occurred." and doesn't name the field |
| 14 | Partial | Negative and empty amounts keep Save disabled (nothing saved), but no specific message is shown |
| 15 | Pass | "This year", "Last 12 months", "All time"; numbers unchanged ($225.00 on 3 items); the choice is kept after reload |
| 16 | Pass | Rec Three $45 Card payout, Rec Two $60 Store refund (credit), Rec One $120 Store refund; no Bob items |
| 17 | **Fail** | Bob's Home shows no Recovered card at all. After recording a $50.00 store refund on UAT Rec Bob (row saved, item Returned), Home still has no Recovered card after reload, and no "What needs attention" section either. Expected "Home shows 50.00 only". Nothing of Alice's leaked. Likely cause (DB Stager, based on the front-end code): Home renders the Recovered card and 'What needs attention' only when /api/items/dashboard returns itemCount > 0, and Bob's only item became Returned. So **a user whose items are all returned never sees their recovered money**. That's a product/spec gap for Steve to decide on, and the plan could give Bob a second Owned item |
| 18 | Pass | "Not found." |
| 19 | **Fail** | "Prepare my download" was ready in about 25 s ("Nov 2, 2026 · Ready until Nov 9, 2026", "Download (4 KB)"). Clicking Download gives "That download is no longer available. Prepare a new one." Same result on the second try. recoveries.csv could not be checked. Likely the same export-delivery issue as FS-40 steps 7-8 (Cloudinary PDF/ZIP delivery setting) |
| 20 | Pass | Redirect to /login?returnUrl=%2F, no amounts |

Labels: "Store refund", "Card payout (a card benefit paid you)" (picker) / "Card payout" (row), "Warranty payout".
Exchange: not offered on the recovery form (Not sure, Back to the original payment, Store credit, Gift card, Cash, Check, Other). **But the return form's "Paid back by" offers "Exchange"**, which conflicts with "it should not be" (it may be in scope only for the recovery form; for Steve to judge).
Timing: "Prepare my download" took about 3.4 s to show "Being prepared". Everything else was under 3 s.


## FS-38 Admin feedback queue (API+Full, run in Full) — Ops, Alice, Bob

Setup note: the run reset turns Ops two-step off. With it off, Ops signing in lands on /settings/security ("Administrator accounts need two-step sign-in before any admin screen opens.") and /admin/feedback bounces back there, so the gate works. Ops was re-enrolled through the UI, as in Scenario 28, and the new key and recovery codes are stored in RUN-CONFIG only.

| # | Result | Actual (quoted) |
|---|---|---|
| 1 | Pass | Three messages under "Your messages", all "Received"; the Problem was sent from the item page ("Page you were on: /items/01a19f8c-...", "Item: ..."). Confirmation "Thank you. We received your message." |
| 2 | Pass | "Problem · Nov 2, 2026 / Received / UAT admin bob problem" |
| 3 | Pass | "Feedback", "4 new · 4 shown", newest first, each with type, date/time, status, text and sender email. Not a placeholder |
| 4 | Pass | Detail: "Problem", "Nov 2, 2026, 10:57:02 PM", "UAT admin problem", From "QA Test 1 · stevewash123.test@gmail.com", Page "/items/01a19f8c-...", Item "UAT Feedback Item", App version "982952c", Status dropdown |
| 5 | Pass | Type Problem: "4 new · 2 shown" (both Problems) |
| 6 | Pass | Received filter shows 4; All restores "4 new · 4 shown" |
| 7 | Pass | Bob's Problem is set to "In progress" at once ("3 new · 4 shown"), and it's kept after reload |
| 8 | Pass | Alice's Problem is set to "Answered" ("2 new · 4 shown"), and it's kept after reload |
| 9 | Pass | Bob sees "Problem · Nov 2, 2026 / In progress / UAT admin bob problem" |
| 10 | Pass | Alice sees Problem "Answered", Suggestion and Question "Received", and only her own 3 |
| 11 | Pass | Answered filter: "2 new · 1 shown", only Alice's Problem |
| 12 | Pass | Read-only. Only Status is editable |
| 13 | Pass | Bob is redirected to Home; no Admin entry in his menu |
| 14 | Pass | Alice is redirected to Home; no Admin menu |
| 15 | Pass | Signed out, it redirects to /login?returnUrl=%2Fadmin%2Ffeedback |
| 16 | Pass | Only "Item: UAT Feedback Item"; no price, store or receipt |

Order: newest first (the story says oldest first for a work queue, so this is the expected first-build behaviour). Statuses are Received, In progress and Answered, and "new" counts Received only. Filters: Status and Type. No paging seen with 4 messages. The user-side list shows a date only, no time.


# FS-39 — Daily digest — build 982952c (Staging)

Mode: Full (browser + Gmail + maintenance clock). Accounts: Alice (Test1), Bob (Test2).

| Step | Result | Notes |
|---|---|---|
| 1–3 | Pass | Digest row has Email and In-app checkboxes rather than a single switch. Note text: "One email a day, at your reminder time (set in your profile)... A return window or warranty ending within 3 days is always emailed at once." Changes autosave. |
| 4 | Pass | UAT Digest One (window to Nov 17). Clock +8 days; run-reminders Sent 1; no separate email; in-app notice "UAT Digest One: return window ends in 7 days". |
| 5 | Pass | Digest run: sent 1, skipped 0, failed 0. Email "1 thing needs your attention" lists the item with its link plus Manage and Unsubscribe links. From noreply@stuff.microsaasbuilders.com, reply-to stuffit-admin@. Arrived as soon as the digest ran (forced run at 11 PM ET, not at the 9:00 reminder time). Landed in Gmail Promotions. A second in-app summary "1 thing needs your attention" also appeared. |
| 6 | Pass | Covered by step 5 contents. |
| 7–8 | Pass | Re-run: digest sent 0; reminders Sent 0 (no duplicates). |
| 9 | Pass | Five burst items (window to Nov 25). Clock +8 (offset 16): reminders Sent 5, Cancelled 2; digest sent 1. Subject "5 things need your attention", line "5 return windows are closing". |
| 10 | Pass (deviation) | UAT Urgent (window to Dec 3). Jumping to "2 days left" (offset 29): Sent 0, Cancelled 12, so no email. The 3-day lead was already past and got cancelled. One more day (offset 30, 1-day lead): Sent 1, and "UAT Urgent: return window ends tomorrow" arrived at once, separate from the digest. Digest afterwards sent 0. **Possible gap:** an item that crosses the 3-day threshold between reminder runs gets no urgent email until the next lead day. |
| 11 | Pass | Digest Email and In-app unticked; the type choice stays "In my daily digest" after reload. |
| 12 | Pass | UAT Instant (window to Dec 17). Clock +8 (offset 38): Sent 1; separate email "UAT Instant: return window ends in 7 days" arrived. Digest sent 0. |
| 13 | Pass | Digest Email and In-app re-ticked; Return window closing set back to "At once". After reload all four types read "At once" and both digest boxes are ticked. |
| 14 | Pass | Bob's Gmail: newest StuffIt mail predates this run, and none of Alice's digests or reminders reached him. Bob's settings: all four "At once", digest Email and In-app ticked. My Items: "Nothing here yet", with no UAT Digest/Burst/Urgent/Instant items. Notifications: "You are all caught up." |
| 15 | Pass | Unsubscribe link opens a confirm page, not an instant unsubscribe: "Email preferences — You are getting emails about Daily digest. What would you like to stop?" Options: only "Daily digest", all "Summaries", or all optional emails, plus the note "You will still see these in the app. Only email stops." No account, email address or other data is shown. "Unsubscribe" was not pressed. The Manage link opened Alice's /settings/notifications with her own email shown. |
| 16 | Pass | clock/reset: "Back to real time. Offset 0 day(s); the app's time is 2026-11-03 04:11:42Z." |

**Summary:** 16/16 Pass. One deviation and possible gap at step 10 (urgent email is skipped if the 3-day lead passes between runs). Cosmetic: the digest went to Gmail Promotions.


# FS-40 — Retest the 2026-11-02 fixes — build 982952c (Staging)

Mode: Full. Accounts: Test1 (Alice), Test2 (Bob, as outsider target). Clock offset 0 → +31 (app "today" Dec 3, 2026 NY) → reset.
Cloudinary "PDF and ZIP files delivery": **could not be confirmed** by DB Stager (no access to storage config). Steps 7–8 fail with HTTP 500 from the API, consistent with that setting being off. **These are storage settings, not app code.**

| # | Finding | Result | Evidence |
|---|---|---|---|
| 1 | FS-24-9 item dates | **Partial** | At offset 0: "30 days left", "Covered 1 policy", "Next to end: Return window, Dec 2, 2026". After +31: item badge "Expired", "Coverage ended · 1 policy", row "Ended Dec 2, 2026", no days-left and no Next-to-end; /items "Expired", "All coverage has ended", so the two pages agree. **Still offered:** "Need to return it or make a claim?" with a "Start a refund or claim" link (/refund), plus "Refund" and "Mark returned". There is no button literally labelled "Start a return" ("Start a return" is a heading). |
| 2 | To-do overdue | **Fail (blocked)** | The item page has no To do box, so "UAT overdue" could not be added. /todos: "Nothing to do right now." Dates are mixed: the new-plan form defaulted to the simulated date (2026-12-03), but one notification was stamped with the real time ("Nov 2, 2026, 11:15 PM") and the export says "kept until November 10, 2026" (real clock). A later notification read "Dec 3, 2026, 11:24 PM", so the stamps are inconsistent. |
| 3 | FS-24-6 bell badge | **Pass** | Badge "1" (aria "Notifications, 1 unread, 1 to do") with 1 unread listed ("Your data export is ready"). After it was read: "1 to do" with no number. |
| 4 | FS-24-6 notification title | **Pass** | Clicking the title "Your data export is ready" opened /settings/privacy (its target) and marked it read. This notice has no "View item" link to compare. |
| 5 | FS-31-16/17/18 end plan | **Pass** | The item page has no add-plan control, so the plan was added via /plans > Add a plan > Cover items ("UAT Clock Plan", UAT Provider, $5.00 a month, from Nov 2). "It ended on" was empty, and "End this plan" stayed disabled until a date was entered. |
| 6 | End plan today | **Partial** | The plan shows "Ended Dec 3, 2026". Totals went from "$60.00 a year … covering items that cost $90.00" to "$0.00 … $0.00", so the plan is excluded. The row still shows "$60.00 a year" (dimming not checked). **Item page still treats the plan as running:** the badge flipped from "Expired" to "Expiring soon", with "Covered · 2 policies", "Next to end: Extended plan, Dec 3, 2026 · Ends today", and the plan marked "Try this first". |
| 7 | FS-27-13/14 export | **Fail (storage)** | "Prepare my download", then "Ready until Nov 9, 2026" and "Download (4 KB)". Clicking Download did nothing on screen, and no zip arrived. `GET /api/exports/<id>/download` returned **HTTP 500**. This differs from the earlier report: the old "That download is no longer available" message is gone, and the failure is now silent. |
| 8 | PDF receipt | **Fail (storage)** | The upload succeeded (201), listed as "Receipt · small-receipt.pdf (45 KB)". View showed "**Could not open that file.**", and `GET /api/documents/<id>/content` returned **HTTP 500**. Side note: the store typed on the add form ("Quillfeather Mercantile") didn't save ("Bought from —"). |
| 9 | FS-35-9 feedback overflow | **Pass** | Counter "4,000 / 4,000 · That is the most we can take. Shorten your message to send it." (red, alert). No sideways scroll, and input is capped at 4,000. The words version sent ("Thank you. We received your message."), and "Your messages" wraps the text. |
| 10 | Nested link | **Partial** | The URL never nests (links from /feedback go to plain /feedback, and from /items to `/feedback?from=%2Fitems`, "Page you were on: /items"). Clicking from /feedback itself gives "Page you were on: none" instead of the page before the form. |
| 11 | FS-33 tracking note | **Pass** | With 250 typed and after "Everything": "The standard amount is $50.00. Zero tracks everything.", shown under the field. Same after saving at 0 and reloading. (Initial load at the saved 50 reads "Using the standard amount, $50.00. Zero tracks everything.") |
| 12 | FS-33-3 lines past cap | **Partial** | All 12 lines are accounted for ("Showing 12 of 12"): 10 in the main list and "Smaller things (2)", with Wood glue 16OZ $6.99 and Sandpaper 80G $12.45, both "Cheaper than the lines kept". The upload note "Added 1 receipt with 12 items. Open each to check it." doesn't say how many lines are under Smaller things. |
| 13 | Work gloves | **Partial (note)** | Work gloves L, $25.98, stays in the main list (expected). It has no "Under $50" label, only "Just added". |
| 14 | FS-25-12 sign-up leak | **Pass (timing note)** | Same page for taken and new addresses ("Check your email / We sent a link to <addr>… Nothing is created until you do…"). Times in seconds: taken 1.320 / 0.804 / 0.834; new 1.355 / 1.309 / 1.319. After warm-up, taken addresses are about 0.5 s faster, a **possible timing leak**. Test2 got "You already have a WarrantyBank account" ×3, and each of +fs40a/b/c got "Confirm your email to start with WarrantyBank". |
| 15 | FS-25-17 reset links | **Pass** | Requests at 11:27:34 and 11:28:45 PM ET, both "If that email is registered, we sent a link…". The older link was refused: "This link has already been used or has expired. Request a new one." The newer link gave "Your password was changed. Sign in with the new one." (set to the same password). The older email lacks the "Requested at" line; the newer has "Requested at 11:28 PM. If you asked more than once, use the newest email." |
| 16 | Console | **Partial** | /login (signed out) and a Home reload both log `401` on `/api/auth/refresh`. The item page, /notifications and /feedback had 0 errors. Earlier in the session there were the 500s from steps 7–8. |
| 17 | Clock reset | **Pass** | "Offset 0 day(s)". |

**Summary:** Pass 8 (3, 4, 5, 9, 11, 14 with a timing note, 15, 17). Partial 6 (1, 6, 10, 12, 13, 16). Fail 3 (2 blocked: no To do box; 7 and 8 storage, HTTP 500).
Compared with the earlier report: row 7 now fails silently with a 500 instead of the old message. Row 1 hides the days-left but still offers refund/claim.
Left behind: Alice has 12 pending Pine Street lines, the tracking minimum saved at 0 (standard), and a feedback message.


# FS-41 — Receipt protection plans and stated warranties — build 982952c (Staging)

Mode: Full. Accounts: Test1 (Alice), Test2 (Bob). Live reader (anthropic); per Steve, reader misses are Partial with the reading quoted. Accounts reset clean at 11:34 PM ET. Receipts are from SampleData/receipts/pdf.

## Part A: protection plans

| # | Result | Evidence |
|---|---|---|
| 1 | **Partial** | One row, so the plan is not a second item and not in the name. The row reads "Wireless Noise Cancelling Headphones · Black", "Best Buy · Oct 2, 2026 · **$421.98**" (expected 349.99). The Add form and item page have Price $349.99 and Total $421.98, so the row shows the order total. "Includes: Geek Squad Protection - 2-Year Plan, $49.99 · Geek Squad · 24 months" (Highly Likely). Read in about 12–30 s. |
| 2 | **Partial** | The row shows the name, Geek Squad, $49.99 and 24 months. **It has no "covers SKU 6505727"/match text and no plan number.** There is no per-field editor (as planned), but also **no keep/untick tick**. |
| 3 | **Fail** | There is no "Add Details" control. Row actions are "Add as a new item", "Link this to an existing item", "Quick add, edit later" and "Dismiss". The full Add form doesn't list the plan, so it can't be unticked or reloaded. |
| 4 | **Fail** | The full Add needs a ticked policy. It first said "Saved in New Items. Tick at least one policy to add it to your items." because the return window had ended and Sony was unticked. With Sony ticked the item saved, but coverage is only "Manufacturer warranty · Sony, Oct 2, 2026 to Oct 2, 2027". **The Geek Squad plan is dropped by a full Add.** It is not on /plans either ("No plans yet."), which is correct. |
| 5 | **Partial** | TV row "OLED TV · 65IN … $1,299.99" with "Includes: Geek Squad Protection 4YR, $299.99 · Geek Squad · 48 months". The cable ($39.99) is under Smaller things. **No row note says the purchase date is used.** A quick add attached the plan: "Extended plan · Geek Squad, Sep 27, 2026 to Sep 27, 2030 … From your receipt: GEEK SQUAD PROTECTION 4YR. Paid 299.99. Plan number GS-88104471. Covers: COVERS SKU 6571204. Upload the plan document to add its terms." The start is the purchase date, but it isn't labelled as such and no confidence is shown. Read in about 22–25 s (**over 20 s**). |
| 6 | **Partial** | Row "800 Series Dishwasher … **$1,539.22**" (expected $1,099.00; looks like the order total). Plan "Geek Squad Protection 3-Year, $229.99 · 36 months". The install line is neither an item nor a plan (Pass). No totals warning. 16 s. |
| 7 | **Partial** | Plans were found at both stores. Walmart: "Allstate Protection 3YR, $49.00 · Allstate · 36 months" (row "4K TV · 50IN … $397.74"). Lowe's: "Lowe's Protection Plan 3-Year, $99.00 · 36 months" with no company shown (row "Dishwasher … $1,072.94"). **No "not in our list" or "not verified" note** for Allstate. 17 s / 14 s. |
| 8 | **Partial** | The TV's Geek Squad coverage shows no claim contact and no company-record wording. That fits an unlisted company, but no listed company was available to compare. The text "check this is for the item above" never appeared, so that half was **Not run** (closest: the HDMI row's "Looks like a document for OLED TV. Same order number (0412-0007-33518). Attach it there"). |
| 9 | **Pass** | Pine Street receipt: no "Includes:" line and no plan invented ("No warranty found yet. Add details to help us find one."). About 30 s (**over 20 s**). |

## Part B: stated warranties

| # | Result | Evidence |
|---|---|---|
| 10 | **Pass (note)** | "Inverter Generator", "KESTREL MARINE & POWER · Jul 19, 2026 · $790.20". "Receipt says: 2 YR MFR WARRANTY (manufacturer)· Likely … · 24 months . Not added by a quick add". Labelled "Likely" with no "may apply" or percentage. 16.5 s. |
| 11 | **Fail** | Quick add gave "**One or more validation errors occurred.**" and created no item. The full Add form had no store, brand or category prefilled and no stated-warranty option. After filling them by hand it showed "Nothing found yet…" and "…not in our shared list yet…", then on save "Saved in New Items. Tick at least one policy to add it to your items." So **an item from an unknown store or maker with only a stated warranty cannot be added**, and no "Stated on receipt" coverage can be created. |
| 12 | **Pass** | "Stated on receipt, provider unconfirmed: Road hazard warranty 50,000 mi" plus "…Stated as 50,000 miles; a mileage has no end date, so none is set from it." Reader oddity: the row name is "Tire · 225/65R17, Road, hazard, warranty". 18.5 s. |
| 13 | **Pass** | Only "Mini-Split · 12K BTU" gets "5 YR COMPRESSOR / 1 YR PARTS" with "The receipt gives more than one term; none is set." "Line Set Kit" shows none. 18 s. |
| 14 | **Partial** | "Repair warranty: 90 days parts and labor." with 3 months, but the provider is labelled **(manufacturer)**, not the seller (it is "provider unconfirmed"). The row is "Compressor Start Relay · fridge … $222.00" (whole invoice). 16.5 s. |
| 15 | **Pass** | "Pellet Stove · 40K" ($2,299.00): "10 YR LIMITED WARRANTY … · 120 months". The Stove Pipe Kit shows none. 17.5 s. |
| 16 | **Pass** | Sears Outlet: no stated warranty from the open-box sentence. It instead read a plan, "Sears Protection Agreement 2-Year, $99.99". Target (19-a5, return window only): none. |
| 17 | **Partial** | The Add form never offers the stated warranty, so there was nothing to remove. Adding the tires with Michelin ticked gave an item with only "Manufacturer warranty · Michelin" and no stated coverage, as expected, though only because a full Add never carries it. |
| 18 | **Pass** | Repair row: "The receipt says 3 months (Repair warranty: 90 days parts and labor.); the maker's policy says 1 year. Check which applies." The Whirlpool warranty is listed separately. Tires showed Michelin and the stated text with no comparison note. |
| 19 | **Pass** | Test2: New Items "Nothing waiting.", My Items "Nothing here yet". |

**Summary:** Pass 8 (9, 10, 12, 13, 15, 16, 18, 19). Partial 8 (1, 2, 5, 6, 7, 8, 14, 17). Fail 3 (3, 4, 11).
**Main findings:**
1. A full "Add as a new item" drops receipt plans and stated warranties. Only a quick add keeps a plan.
2. There is no Add Details plan tick.
3. Rows for the headphones and dishwasher show the order total, not the line price.
4. The generator from an unknown store can't be added: quick add gives a validation error, and a full Add requires a policy.
5. No "purchase date used" note or confidence label on the plan.
6. No "not in our list / not verified" note for Allstate.

Reads over 20 s: 15-bestbuy-tv (about 22–25 s), 12-thermal (about 30 s), and possibly 21-bestbuy (12–30 s).
Left: Alice has items Headphones, OLED TV and Tire; the other rows are pending.


# FS-42 — Policy note, source link, to-dos you can get back, polish — build 982952c (Staging)

Mode: Full. Accounts: Test1 (Alice), Test2 (Bob), Ops (step 20). Staged: Alice's "UAT Todo Item" (Best Buy, Nov 2). The New Balance return policy has source https://www.newbalance.com/returns (verified_at empty). Best Buy's policies have verified_at set.

| # | Result | Evidence |
|---|---|---|
| 1 | **Pass** | "New Balance return policy, Merchant, 30 days, Unconfirmed", "**Usual window, can differ for your item. Check your receipt.**", and a "Source" link ("Source for New Balance return policy (opens in a new tab)"). Note: the store dropdown offered only `Add "New Balance"` / `Add "Best Buy"`, with no existing list entry, though the shared policy was still found. |
| 2 | **Pass** | href `https://www.newbalance.com/returns`, target=_blank, rel="noopener noreferrer". |
| 3 | **Partial** | The saved item's "Return window · New Balance" has a Source link (same href, new tab). The "Usual window, can differ…" note is **not** shown on the saved item for the Unconfirmed policy. Instead it shows the policy text ending "…The 30 days is not stated in the order email, so confirm it on the source page before relying on it." Policies sit behind "Show policies". |
| 4 | **Pass** | The hand-added "Store warranty" ("UAT own warranty") has no Source link and no note. Side bug: with Length 12 months entered, it shows "**No fixed end date**". |
| 5 | **Fail** | "Best Buy return policy: general", Merchant, 15 days, **Confirmed**, yet the "Usual window, can differ for your item. Check your receipt." note **is shown**. The Source link is present (bestbuy.com return-exchange-policy page). Also offered: "Best Buy return policy: smartphones", 14 days, "Likely". |
| 6 | **Pass** | Bob sees the same note and Source href and none of Alice's stores, items, plans or insurance. |
| 7 | **Pass** | "Looking…" for about 1.5 s, then "Nothing new to suggest. Everything we know of is already added to this item." |
| 8 | **Pass (note)** | The To do card shows only in edit mode ("Add a reminder", "Due (optional)", "Add"). Three open to-dos were added. |
| 9 | **Pass** | All three left the open list. |
| 10 | **Pass** | A collapsed toggle "Show done and dismissed (3)" (open: "Hide done and dismissed (3)"). Rows: UAT n/a "Not applicable" with Undo; UAT dismiss "Dismissed until Nov 9, 2026" with Undo; UAT done "Done" with Reopen. |
| 11 | **Pass** | Undo returns "UAT dismiss" to the open list, and the section drops to (2). |
| 12 | **Pass** | /todos has a "Done and dismissed" region, collapsed ("Show done and dismissed (2)"). Reopen on "UAT done" from /todos worked. "UAT n/a" has Undo, not Reopen. |
| 13 | **Pass** | Bob's /todos: "Nothing to do right now." Alice's item URL shows "Not found." |
| 14 | **Pass** | One real click on "Q1" opens the account menu, and it stays open. |
| 15 | **Partial** | With "New Bal" typed and the field left, the field is **cleared** to its placeholder, with no `"New Bal" is not selected yet` message and no "add as new" button. The text isn't silently kept, but it vanishes without explanation. The full "New Balance" auto-selects. |
| 16 | **Partial** | The item page has no "Stop covering" (coverages have Edit/Remove). Remove asks "Remove this coverage?"; Cancel keeps it and confirming removes it. Plan "Stop covering this item?" ("…The item itself stays.") asks first and Cancel keeps it (confirm not tried). Insurance "Unlink this item?" asks first and Cancel keeps it. |
| 17 | **Pass** | "Delete this file?" ("small-receipt.pdf is removed. This cannot be undone.", Cancel / "Delete file"). Cancel keeps the file on the item, plan and insurance policy. Side: plan and insurance uploads appear only after a reload. |
| 18 | **Pass** | The page says "Delete this policy" and the dialog "Yes, delete the policy", so the labels differ. |
| 19 | **Pass** | Bob's /settings/security goes to /settings/profile, with no "You cannot do that." |
| 20 | **Pass** | Ops /settings/security opens: "Two-step sign-in", "Administrators", "Extension keys"; "Two-step sign-in is on." |
| 21 | **Fail** | "Return in progress since **Nov 3**, 2026. It is on your returns list until you mark it returned." This was started at about 11:55 PM ET on Nov 2, so the date is UTC, not the user's time zone. There is no space before the full stop (fixed). |
| 22 | **Pass** | "Only the items you link below: 1 item, which costs $90.00." |

**Summary:** Pass 17 (1, 2, 4, 6–14, 17–20, 22). Partial 3 (3, 15, 16). Fail 2 (5, 21).
Nothing took over 3 s, apart from the document read and upload refresh.
Wording that sounds certain for an unconfirmed policy: none seen. The opposite issue: the "Usual window" caution shows on a Confirmed policy (step 5) and is missing on the saved item (step 3).

