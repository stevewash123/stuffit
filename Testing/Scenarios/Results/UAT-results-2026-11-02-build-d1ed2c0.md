# StuffIt UAT results: build d1ed2c0
**Build:** commit d1ed2c0, startedAt 2026-11-02T12:48:36Z (7:48 AM ET), Staging. Checked again at 9:02 AM ET: unchanged.
**Run:** Nov 2, 2026, 8:05–9:16 AM ET. Plans are from the merged Full Scenarios set (FS-22 to FS-32).
**Not run:**
- FS-23 and FS-18–21 are deferred until built.
- FS-22 steps 7–8 are deferred (no share checkbox).
- FS-27 steps 17–20, which delete Bob, are waiting for your OK.
- FS-28 steps 14–18, the optional API checks, need a signed-in token.

**Clock:** the simulated clock was moved 20, 23 and then 31 days ahead, then reset to 0. Confirmed at 9:06 AM ET: "Offset 0 day(s)".

## Summary
| Plan | Area | Pass | Partial | Fail | Not run | Headline |
|---|---|---|---|---|---|---|
| FS-22 | Shared policy, private purchases | 4 | 2 | 0 | 2 (deferred) | Privacy holds. No "usual window" note and no source link. |
| FS-24 | Simulated clock and reminders | 8 | 2 | 0 | 0 | Emails are right and not duplicated. The item page and to-dos ignore the simulated date. |
| FS-25 | Account lifecycle and email | 13 | 1 | 1 | 2 | The older reset link wins over the newest one. Sign-up reveals which emails are registered. |
| FS-26 | Purchases, items and privacy | 17 | 1 | 1 | 0 | No "usual window, can differ" note. Suggest coverage does nothing. |
| FS-27 | Cards, notifications, export | 12 | 2 | 1 | 5 | "Prepare my download" fails. "Is yours one of these?" is never shown. |
| FS-28 | Admin two-step and shared data | 12 | 1 | 0 | 5 (API) | Two-step works end to end and Bob is refused. There is no verified filter. |
| FS-29 | Returns in progress | 20 | 1 | 0 | 0 | No days-left wording on the returns list. |
| FS-30 | Insurance | 17 | 2 | 1 | 1 | No over-limit note ($1,800 item against a $1,500 limit). |
| FS-31 | Extended warranty plan | 14 | 6 | 0 | 0 | A plan ended today still counts as running. |
| FS-32 | To-dos | 14 | 0 | 0 | 0 | Works. Dismissed or not-applicable to-dos can't be found again. |

## Fixed since 8e7ea94
- FS-26 step 8: an approximate date now gives no return window and shows the warranty as a range.
- FS-26 step 9: Upload is disabled while the document is being read, so the upload is no longer lost.
- The simulated clock now works (it was unavailable last run), so FS-24 ran for the first time.

## Issues (most important first)
1. **FS-25-17: reset links work in the wrong order.** The older link changed the password, and the newest link then said "This link has already been used or has expired." The email itself says to use the newest one.
2. **FS-27-13: data export fails.** "Prepare my download" shows "Could not be prepared. Please try again" every time. The delete-account warning says "Download your data first", which isn't possible.
3. **FS-24-9: item page ignores the simulated date.**
   - At the simulated Dec 3, the item page shows "Expired" next to "30 days left" and "Covered 1 policy", and still offers **Start a return**.
   - /todos still says "Due in 1 day" for a to-do that is overdue.
   - Home, the items list and the emails do use the simulated date.
   - Real users will see the same mismatch at midnight boundaries if the item page computes dates in the browser.
4. **FS-30-11/12: no over-limit note.** Nothing warns about an item priced above its category limit.
5. **FS-26-5 and FS-22-1/3: policy suggestions lack their note and source.**
   - The "usual window, can differ for your item" note never appears.
   - There is no source link, though the policy text says "confirm it on the source page".
   - Suggest coverage does nothing.
6. **FS-25-12: sign-up reveals accounts.** "An account with this email already exists" tells anyone which addresses are registered.
7. **FS-31-16/17: ending a plan today.** It still shows "Ends today", isn't dimmed, and still counts in the yearly total. The end-date box also starts filled with today.
8. **FS-27-4: no match prompt.** An unlisted card is saved without ever asking "Is yours one of these?".
9. **FS-24-6: bell badge and links.**
   - The badge shows 4 when 3 notifications are listed (it appears to add to-dos to the unread count).
   - Clicking a notification's title does nothing; only "View item" works.
10. **FS-24-8 and FS-32: no overdue to-do reminder.** No reminder is sent once a to-do is overdue (Todos = 0 on every run). Done, dismissed and not-applicable to-dos can't be found again.
11. **FS-30-14: stale count.** After the Lamp is left out of the policy, its Policies card still says "Covered 1 policy".
12. **Missing wording.**
    - Returns list: there is no days-left count (FS-29-7).
    - Admin Shared data: there is no verified filter, and the filter shows the typo "Brand (maker)s" (FS-28-9).
13. **Validation.** Empty forms flag only one field, and date errors show the generic banner "One or more validation errors occurred." (FS-30, FS-31).
14. **Small things.**
    - Stray space in "since Nov 2, 2026 .".
    - Grammar: "1 item, which cost".
    - File size shows 4 KB before upload and 3 KB after.
    - "Stop covering" and file delete happen with no confirmation.
    - Two "Delete policy" buttons, which is an accessibility problem.
    - The account menu needs a second click to open.
    - Typing a store name doesn't select it; you have to click the dropdown option.
    - The /returns sample data reads "Started Oct 20. Return window closes Oct 18…: 2 days left".
    - /settings/security shows Bob "You cannot do that." instead of redirecting him.
15. **Needs a real document (FS-30-18, FS-31-14/15).** The reader works, but my receipt image matched nothing. A sample policy page and a sample contract would let me test accept, dismiss and update.

## Accounts and secrets
- **Alice:** her password was reset during FS-25. The saved login matches the new password.
- **Test4 (Ops):** two-step sign-in is now on. The setup key and 10 recovery codes are stored in RUN-CONFIG on my computer, not in this report.

## Test data left behind
- **Alice:**
  - UAT Blender 2 (Nov 2)
  - UAT Return Drill (Active) and UAT Return Saw (Returned, "Not paid yet")
  - UAT Return Kettle
  - UAT Guitar, UAT Laptop, UAT Lamp
  - UAT Fridge, UAT Washer
  - UAT Reminder Blender, with the open to-do "UAT Clock todo"
  - UAT22 Alice Shoes, UAT24 Clock Shoes
  - Older items
- **Bob:**
  - UAT Kettle (Nov 2), UAT22 Bob Shoes
  - Cards UAT Card (4242) and UAT Imaginary (0001)
  - Reminder notifications created by the clock test
- **Fixture:** UAT04 Policy Store is still there. I'll delete it only with your OK.

---
# FS-22 Shared policy, private purchases — build d1ed2c0 (run 08:56–09:00 ET, Nov 2 2026). Steps 7–8 deferred.
Alice item /items/01a19c8c-d69e-7c2b-861f-0141fa053c54, Bob item /items/01a19c8d-c094-72d4-b9c6-6555387cdb00.

| # | Result | Notes (quoted) |
|---|---|---|
| 1 | Partial | Suggestion "New Balance return policy", "Merchant", "30 days" (tooltip "Ends 2026-11-27"), "Unconfirmed" ("We could not check this policy. Tick it only if your paperwork says so."); unticked by default: "Not added. Tick it to add it when you save…". **No "usual window, can differ for your item" note** (same gap as FS-26-5). Item: "Oct 28, 2026 to Nov 27, 2026 · 25 days left". |
| 2 | Pass | Bob same policy, "Ends 2026-11-29" = his Oct 30 date + 30; "Oct 30, 2026 to Nov 29, 2026 · 27 days left". |
| 3 | Partial | Policy text identical for both. **No source link** anywhere, though the text says "confirm it on the source page before relying on it." Only link "Return or claim steps" → /items/sample/refund (mock). |
| 4 | Pass | Alice edited end to Dec 15: "Oct 28, 2026 to Dec 15, 2026 · Until Dec 15, 2026". |
| 5 | Pass | Bob unchanged "Oct 30, 2026 to Nov 29, 2026 · 27 days left". |
| 6 | Pass | No cross-user data on /items, /add, /returns, /notifications, /orientation, /insurance, /cards, /settings/profile, /settings/stores ("The ones you add are private to you."). Filter counts ("New Balance 2") are Alice's own. /stores, /warranties, /policies redirect Home. |
| 7–8 | Deferred | No share checkbox yet. |

Note: days-left label changes to "Until <date>" after a manual edit (inconsistent with "25 days left" elsewhere).
Leftover: Alice UAT22 Alice Shoes, Bob UAT22 Bob Shoes.
Screenshots: step 1 cb2fe286….png, step 5 cbeadbe1….png

---
# FS-24 Simulated clock and reminders — build d1ed2c0 (run 09:00– ET, Nov 2 2026)
Persona: Alice. Item UAT24 Clock Shoes (New Balance, $60, Nov 2) /items/01a19c91-060b-7a6d-86d4-04c29e3c28dd.

| # | Result | Notes |
|---|---|---|
| 1 | Pass | "Next to end: Return window, Dec 2, 2026 · 30 days left"; badge "Expiring soon" (on a 30-day window, odd). Policy "Unconfirmed", unticked by default (ticked). |
| 2 | Pass | /settings/notifications: "Changes save as you make them." Return window closing, Warranty expiring, Extended plan expiring: Email ON, In-app ON. No separate to-do row ("Info needed" covers dated to-dos). Text messages "Coming soon". |
| 3 | Pass | "Offset 0 day(s); the app's time is 2026-11-02 14:02:44Z." |
| 4 | Pass (lead time 7 days) | advance 20 → "Offset 20 day(s); the app's time is 2026-11-22…". run-reminders: Sent 1, Cancelled 20 → Bob got "UAT22 Bob Shoes: return window ends in 7 days" (Nov 29). Alice's item (10 days left) not yet due. Advanced 3 more (offset 23, Nov 25): Sent 3, Cancelled 1. Summary lists counts only, not which reminders (plan expects run summary to list Alice's). |
| 5 | Pass | Email "UAT24 Clock Shoes: return window ends in 7 days" — "ends in 7 days, on December 2, 2026."; "View item" link = item URL; manage + unsubscribe links. |
| 7 | Pass | Re-run same simulated day: Sent 0 (both at offset 20 and 23). No duplicate email. |
| 6 | Partial | /notifications (offset 23): "UAT24 Clock Shoes: return window ends in 7 days" "Nov 25, 2026, 9:03 AM · just now", Unread; also "UAT Laptop: return window ends in 7 days" (Dec 2). Clicking the title does nothing; "View item" marks it read ("Mark unread" appears) — landing URL not captured. Badge said "4" with only 3 notifications listed (mismatch). |

**Real-date leaks at offset 23 (app = Nov 25):** Home is correct ("Return windows closing… 7 days"), but the item page says "30 days left" / "Dec 2, 2026 · 30 days left"; /todos shows "UAT Clock todo" (due Nov 3) as "Due in 1 day", not overdue; old notification shows "Nov 2, 2026, 9:00 AM · 4 minutes ago". The item page and to-do labels ignore the simulated clock.
| 8 | Pass | advance 8 → "Offset 31 day(s); the app's time is 2026-12-03…". run-reminders: Sent 0, Cancelled 8. No new email or notification for the ended window (the two "ends in 7 days" entries on /notifications are the Nov 25 ones from step 4, not new). Note: Todos = 0 on every run, so no overdue to-do reminder for "UAT Clock todo" (due Nov 3). |
| 9 | Partial | /items: "Expired" · "All coverage has ended" (correct), and the item is not under Expiring soon. Item page contradicts itself: badge "Expired" but chip "30 days left", "Next to end: Return window, Dec 2, 2026 · 30 days left", "Covered 1 policy", and **Start a return** still offered. Nothing says the window ended (real-date leak on the item page). |
| 10 | Pass | reset → Offset 0 day(s); the app's time is 2026-11-02 14:06:35Z. [200] |

Also: Home at Dec 3 correctly listed UAT03 Alice Sneakers and UAT22 Alice Shoes as "Return window · 12 days". The notification timestamps stay at the time the run produced them.

---
## FS-25 Account lifecycle and email (partial, in progress)
| # | Result | What I saw | Evidence |
|---|---|---|---|
| 1 | Pass | Redirected to sign-in. Tab title "Sign in · WarrantyBank", heading "Sign in". | /login?returnUrl=%2F |
| 2 | Pass | /terms "Terms of Service", /privacy "Privacy Policy", /disclaimer "Disclaimer" all load with no sign-in wall; each says "Version 2026-10-01 · last updated October 1, 2026" and "Draft for review. This text has not yet been read by a lawyer. Items in [square brackets] are filled in before launch." | /terms, /privacy, /disclaimer |
| 3 | Pass | Empty submit: "Enter a valid email address." (Email), "Use at least 10 characters." (Password), "Please agree to continue." (terms). Confirm password showed no message. Nothing created. | /signup |
| 4 | Pass | Short password: "Use at least 10 characters." Email "abc": "Enter a valid email address." No stack trace or raw JSON. | /signup |
Precondition note: Alice's account already exists. Her saved password was refused ("Invalid email or password."), so per the plan's precondition, the reset in steps 13-14 is used to continue.
Odd: banner "A new version of WarrantyBank is ready. | Reload" on /signup.
| 13 | Pass | "If that email is registered, we sent a link to reset your password. It may take a minute to arrive." Submitted 08:19:51 ET; email "Reset your WarrantyBank password" arrived 08:19:52 ET from StuffIt <noreply@stuff.microsaasbuilders.com>, link points at https://stuffit-ui.onrender.com/reset-password?email=…&token=… | /forgot-password |
| 16 | Pass | Same text word for word for nobody.uat@example.com. | /forgot-password |
| 14 | Pass (partial) | Newest reset link: "Your password was changed. Sign in with the new one." Sign-in with the new password works (lands on /). The old password could not be checked: it was not known (it was the one refused at the start). | /reset-password?… |
| 10 | Pass | Greeting "Welcome, QA"; nav "Home", "My Items", "New Items", "Returns", "Notifications"; account button "Q1", menu header "QA Test 1". | / |
| 8 | Pass | Sign out went to /login; Back showed the sign-in form (login?returnUrl=%2F); no account data visible. | /login |
| 9 | Pass | "Invalid email or password." | /login |
| 15 | Pass | Second use refused after submit: "This link has already been used or has expired. Request a new one." with "Send me a new link". The page loads clean (heading "Choose a new password", "At least 10 characters."); refusal shows only after submit. Password not changed. | /reset-password?… |
Odd: account menu "Q1" needed a second click to open; "Sign out" is plain text, not a menu item. Home showed "Quick set-up is not finished." and leftover data from earlier runs ("UAT Blender 2", return window 14 days). Console shows 1-2 errors on most pages (not inspected).
| 5 | Pass (account existed) | Sign-up with the Test1 address: "An account with this email already exists. Try signing in." (stays on /signup). Precondition not met: the account already existed, so steps 5-7 (confirmation email and link) were not repeated. | /signup |
| 11 | Pass (account existed) | Same for Test2: "An account with this email already exists. Try signing in." Bob signs in with his saved login ("Welcome, QA", menu header "QA Test 2"). | /signup, / |
| 12 | Partial | Duplicate sign-up is refused with no error page and no second account, but the message "An account with this email already exists. Try signing in." tells anyone which addresses are registered, unlike the neutral Forgot-password message. | /signup |

## Step 17 — double reset after 08:30 (run 08:31–08:33 ET)
- Two resets requested 08:31:06 and 08:31:39 ET; Gmail threaded both with the 08:19 email.
- Newest email (13:31:40Z) contains "Requested at 8:31 AM. If you asked more than once, use the newest email." Older email (13:31:07Z) has no "Requested at" line. **Text: Pass.**
- OLDER link: form loaded normally (no expiry notice); submitting showed "Your password was changed. Sign in with the new one." → older link still works. **Fail**: not superseded by the newer request.
- NEWEST link: form loaded normally; submitting showed "This link has already been used or has expired. Request a new one." → using the older link invalidated the newest one (reverse of the email's advice). **Fail.**
- Neither link said the new password was the same as the old one (same value reused).
- Sign-in with the new password works; Home shows "Welcome, QA", menu "QA Test 1", "1 Return windows closing: UAT Blender 2". Signed out.
- **Step 17 result: Fail** (link order). Console: 1 error (not inspected).

---
## FS-26 Purchases, items and privacy
Precondition not met: Alice already had "UAT Blender 2" (Best Buy, Nov 1) and "UAT03 Alice Sneakers" from earlier runs; nothing deleted. The new blender was renamed "UAT Blender 2 (Nov 2)" to tell them apart.
| # | Result | What I saw | Evidence |
|---|---|---|---|
| 1 | Pass | Blank form at /add/new. Order: Store, "Date you bought it" (+ "I am not sure of the exact date"), "Credit card used", "Order number", "More details: total paid, notes", Category, "Brand (optional)", "Item", "Model number", "More about this item: price, size, serial number, notes" (Price first inside), "What it would be covered by". | /add/new |
| 2 | Pass | "Add at least one item." and under Item "Tell us what you bought." Store not flagged; nothing saved. | /add/new, screenshot |
| 3 | Pass | Best Buy + Cuisinart, Category "Small appliances" required ("Category (needed: Cuisinart's warranty depends on it)"), 89.99, 2026-11-02. "Best Buy return policy: general, Merchant 15 days, Confirmed" ticked by default; "Cuisinart warranty, Manufacturer 1 year, Unconfirmed" NOT ticked by default (ticked by hand). Saved to item page. | /items/01a19c6f-80f1-71f0-ba6c-9f4156774dad |
| 4 | Pass | Read-only: "Bought Nov 2, 2026 from Best Buy", Cuisinart, Small appliances, $89.99. | same |
| 5 | Fail | Return window "Nov 2, 2026 to Nov 17, 2026 · 15 days left" (15 days from Nov 2: correct). Warranty "Nov 2, 2026 to Nov 2, 2027" (1 year: correct), note "[placeholder] Fake terms for testing…". The doubt "usual window, can differ for your item" appears nowhere: no confidence score to hover, Suggest coverage (edit mode) changed nothing then greyed out, phrase not in the page source. | same |
| 6 | Pass | Edit mode: Done, Mark returned, Mark disposed, Delete; "Edit item"/"Edit purchase"; Edit/Remove per policy; Add coverage; Suggest coverage; To do box; "Receipts and files" with "Add a receipt or other file". | same |
| 7 | Pass | Renamed "UAT Blender 2 (Nov 2)"; shows on item and in My Items. | /items |
| 8 | Pass | Only the month, Sep 2026: form says "Best Buy return policy … This return window ended 2026-09-30, so it cannot be added." Item: "Bought Sep 2026 (approximate) from Best Buy", $25.00, no return window, warranty "Ends between Sep 1, 2027 and Sep 30, 2027 (date estimated)". **Fixed since 8e7ea94.** | /items/01a19c70-7ecc-7e09-9213-d9b895c2b133 |
| 9 | Pass | "Reading your document…" ("This takes a few seconds. Keep this screen open.") 12-20 s; Upload disabled with title "Wait until the document has been read". After reading, Upload hid and "What we found in your document" appeared (Store conflict Best Buy vs "Test", Order total 89.99, "Keep 1 & Update 1"/"Not now"/"Reject this document"). **Fixed since 8e7ea94 (upload no longer lost).** Tooltip is a native title attribute. | same |
| 10 | Pass | After Keep, Upload enabled; "Receipt / uat-receipt.jpg (3 KB)" with View, "Read it", Delete; View opens it. Total changed "—" to "$89.99". | same |
| 11 | Pass | "Toaster": UAT Toaster only. "Blender": UAT Blender 2 and UAT Blender 2 (Nov 2). "zzqqxx": "No items match." + "Clear filters". | /items?q=… |
| 12 | Partial | "Expiring soon" narrows to the two blenders; clearing restores all four. "May be covered" shows "No items match." (empty), still can't confirm it is right. | /items?status=mayBeCovered |
| 13 | Pass | https://stuffit-ui.onrender.com/items/01a19c6f-80f1-71f0-ba6c-9f4156774dad | |
Odd: saves and upload take several seconds. Best Buy's text mentions a holiday window (Oct 31 to Dec 31) but the item shows 15 days. Add form also lists "Best Buy smartphones" return policy (14 days, "Likely").
| 14 | Pass | Bob's My Items: "UAT Kettle", "R7 Kettle", "REG-8e7ea94 Bob shoes", "UAT03 Bob Sneakers". No Alice items. | /items |
| 15 | Pass | Bob on Alice's item address: "Not found." only. | /items/01a19c6f-… |
| 16 | Pass | Bob added "UAT Kettle (Nov 2)", Best Buy, $19.00, Nov 2. | /items/01a19c73-638d-7b73-ba19-88df465529e5 |
| 17 | Pass | Alice searches "Kettle": "No items match." | /items?q=Kettle |
| 18 | Pass (no undo) | "Delete this item?" / "UAT Toaster and its coverage and files are removed. This cannot be undone." Cancel / "Delete item". Leaves My Items; no Undo or restore offered (the plan allows "if offered"). | /items |
| 19 | Pass | After reload and sign-out/in: UAT Blender 2 (Nov 2) present; UAT Toaster gone ("Not found." at its address). | /items |

---
# FS-27 Cards, notifications, export — build d1ed2c0 (run 09:10–09:16 ET, Nov 2 2026). Steps 17–20 (delete Bob) not run; they wait for Steve's OK.
Personas: Test2/Bob, Test1/Alice. Cards: UAT Card /cards/01a19c9a-dd28-7c9e-bc85-47fe90876111, UAT Imaginary /cards/01a19c9b-6695-7105-88f9-c8275ce10ab6.

| # | Result | Notes (quoted) |
|---|---|---|
| 1 | Pass (odd) | Bob is not a new account. /notifications lists return reminders created by the clock test ("UAT03 Bob Sneakers: return window ends in 6 days", "UAT22 Bob Shoes…7 days"). The card notice "Add a credit card and confirm its benefits – Your credit card can add warranty time and purchase protection…" with "I don't use credit cards" appears only in the bell dropdown, not on /notifications. |
| 2 | Pass | "No credit cards yet. Add the one you use most below." Chase Sapphire Preferred, "UAT Card XXXX-XXXX-XXXX-4242", "Extended warranty: Adds 1 year, up to 4 years total", "Purchase protection: Covers 120 days from purchase". |
| 3 | Pass | Both benefits "Confirmed Nov 2, 2026"; nothing marked unverified. |
| 4 | Partial | Only offers 'Add "UAT Imaginary Rewards" as a new credit card'; requires Bank / Issuer ("Choose the bank that issued this credit card."). Saved as "UAT Imaginary [UNVERIFIED] [⚠ No policy added]"; detail page: "We do not have published benefits for this credit card." with "Search the internet for this credit card's terms" / "Add benefits by hand". **"Is yours one of these?" never shown.** |
| 5 | Pass | "Your card UAT Card already ends in 4242. Receipts ending in 4242 are matched to that first card, so these digits were not added." Odd: the Credit Card Name field went blank after picking the product. |
| 6 | Pass | The card notice cleared after the first card was added; badge went from 3 to 2. |
| 7 | Pass | Groups Expiring, Purchases, Summaries, Account, System alerts (Required, locked), Product news (off). Text column "coming soon". |
| 8 | Pass | Daily digest email off persisted after reload; Return window closing stayed on. Restored afterwards. |
| 9 | Partial | /settings/email is an "Email connection" page (Gmail or iCloud, app password), not the account address. The account address shows only under "Where we reach you" on Notifications. No way to clear it was found. |
| 10 | Pass (note) | /todos shows the leftover "UAT Clock todo" (expected from FS-32). /returns is labelled "First design: example data". Sample bug: "Started Oct 20. Return window closes Oct 18, 2026: 2 days left." (internally inconsistent). |
| 11 | Pass | Reminder "UAT24 Clock Shoes: return window ends in 7 days", "on December 2, 2026", item link correct, unsubscribe link present (from FS-24). |
| 12 | Pass | "You are getting emails about Return window closing. What would you like to stop?" (Only this type / All "Expiring" / All optional). After Unsubscribe: "Done. No more "Return window closing" emails. Required notices…still reach you." "You will still see these in the app. Only email stops." Settings agreed. Re-enabled afterwards. |
| 13 | **Fail** | Privacy & data "Download everything" ("One zip with your purchases, items, coverage, cards (last 4 digits only), settings, and all your files…"). "Prepare my download" twice → "Nov 2, 2026 · Could not be prepared. Please try again". No file. |
| 14 | Not tested | No export. |
| 15 | Pass | "This permanently deletes: your purchases, items, coverage and credit cards / every receipt and file you uploaded / your notifications, settings and sign-in / stores, brands and policies you added for yourself. Shared knowledge other people rely on stays. A paid plan is cancelled first. This cannot be undone. Download your data first if you want a copy." Requires typing the email and the password; button disabled until both are filled. |
| 16 | Pass | Left without submitting; still signed in; cards intact. |
| 17–20 | Waiting | Deleting Bob's account needs Steve's OK. Note: with export broken, "Download your data first" isn't possible. |

Odd: bell badge "3" vs label "2 unread, 1 to do" (the badge adds to-dos; possibly intended). Account menu needs a second click.
Leftover: Bob cards UAT Card (4242) and UAT Imaginary (0001).
Screenshots: 3 7e1ee545….png, 4 8b59d2b6….png & d86ca3e5….png, 13 03fb1478….png, 15 5b9ab2d4….png

---
# FS-28 Admin two-step and shared data — build d1ed2c0 (run 09:06–09:10 ET, Nov 2 2026)
Personas: Ops/Test4 (admin), Bob/Test2. The setup key and recovery codes are stored in RUN-CONFIG only, not here.

| # | Result | Notes (quoted) |
|---|---|---|
| 1 | Pass | Landed on /settings/security: "Two-step sign-in", "Administrator accounts need two-step sign-in before any admin screen opens. It adds a code from your phone to your password." Tip about using a separate admin email. |
| 2 | Pass | QR code alt "QR code to add WarrantyBank to your authenticator app"; "Or type this key"; "6-digit code"; "Turn on" is disabled while the field is empty. |
| 3 | Pass | First code accepted. "Two-step sign-in is on. Save these recovery codes now." "Each works once…They will not be shown again." Then "You have 10 recovery codes left…". Administrators list: admin@microsaasbuilders.com "Two-step on"; Ops (you) "Two-step on"; stuffit-admin@microsaasbuilders.com "Two-step not set up". |
| 4 | Pass | Nav shows an "ADMIN" badge, Review, Companies, Shared data, Feedback, and "Customer view". |
| 5 | Pass | "Enter your authenticator code."; "Authenticator code"; "The 6 digits from your authenticator app, or one of your recovery codes." |
| 6 | Pass | 000000 → "That code is not correct."; not signed in. |
| 7 | Pass | Lands on /admin, "Shared data". |
| 8 | Pass | Customer view leads to customer Home ("Welcome, QA", all tiles 0); "Admin view" returns to /admin. |
| 9 | Partial | "Shared stores, brands and issuers", "Reference data everyone sees. Changes here are versioned and audited." The Show filter has Everything, Stores, "Brand (maker)s" (typo), Credit card issuers and Warranty providers, but no verified/unverified option. About 290 rows. "Home Depot — Verified — Store" (1 row); "Milwaukee — Not verified — Brand" (1). The customer-created "UAT Insurer" and "UAT Home Warranty Co" do not appear (correct). The test fixture "UAT04 Policy Store — Needs data — Store" is listed. |
| 10 | Pass | /admin/parties/01a0f4e4-458d-7b8b-8d23-274f89859c14: "Everything else — 90 days — Current. Checked Sep 29, 2026 · Source", "Verified: Checked against the official source on Oct 24, 2026."; "Major appliances — 2 days". No private data. |
| 11 | Pass | Companies works (Retailers, Brands, Credit cards and Extended warranty sellers marked "not built yet"; the Find return policy flow is present). Review: "Not built yet. Planned in S7.1.2…". Feedback and issues: "Not built yet. Planned in S7.1.9…". |
| 12 | Pass | Bob sees no Admin badge, no Admin view and no Security tab. |
| 13 | Pass | /admin, /admin/companies, /admin/review and /admin/feedback each redirect to /. /settings/security shows "You cannot do that." with the heading "Two-step sign-in" (no QR) instead of redirecting. |
| 14–18 | Not run | API steps (optional) need a signed-in bearer token; the run has no sanctioned way to get one without handling the password. |

Odd: the account menu needs a second click. Companies row labels include "Made-up placeholder".
Screenshots: step 4 3fee3b3d….png, step 7 ffc9e3ac….png

---
# FS-29 Returns in progress — build d1ed2c0 (run 08:34–08:38 ET, Nov 2 2026)
Personas: Test1/Alice, Test2/Bob. Console: no errors at end (earlier pages unchecked).

| # | Result | Notes (quoted) |
|---|---|---|
| 1 | Pass | Each add form: "Home Depot return policy", "Merchant", "90 days", "Confirmed" (Target for Kettle); "Counted from today until you give the date." Item page: "Next to end: Return window, Jan 31, 2027". Drill /items/01a19c79-3b0d-7deb-92fd-a27cdb9ccec5, Saw /items/01a19c79-745b-78e7-8b82-90bd77fb38e5, Kettle /items/01a19c79-9770-746e-b1ea-aad66baf574b. Odd: Category auto-filled (Power tools / Small appliances); store field needs a dropdown click, typing alone doesn't select. |
| 2 | Pass | "Returns in progress"; "Nothing to return right now." "Open an item and choose Start a return; it will show up here until you mark it returned." |
| 3 | Pass | Start a return on all three (with Edit, Mark returned, Mark disposed). |
| 4 | Pass (cosmetic) | "Return in progress since Nov 2, 2026 . It is on your returns list…" — stray space before period. Status "Active", coverages unchanged. |
| 5 | Pass | Persists after reload. |
| 6 | Pass | Same note on Saw and Kettle. |
| 7 | Partial | Order Drill, Kettle, Saw (all end Jan 31, 2027, so ordering untestable). Row: "Home Depot · Bought Nov 2, 2026 · $120.00", "Return window ends Jan 31, 2027". Badge says "Until Jan 31, 2027" — **no days-left wording**. |
| 8 | Pass | "Home Depot" "2 items · $200.00"; "Target" "1 item · $30.00"; store leaves row text; untick restores. |
| 9 | Pass | Row opens item. |
| 10 | Pass | Note gone, Start a return back, no "The return" card. |
| 11 | Pass | Drill, Saw. |
| 12 | Pass | "Mark as returned"; date 2026-11-02; refund 120; hint "Leave empty if the money has not come back yet."; Paid back by: Not sure / not yet, Back to the original payment, Store credit, Gift card, Exchange, Cash, Check, Other; "1 is easy, 5 is very hard." |
| 13 | Pass | Submit disabled with empty date. |
| 14 | Pass | "Returned" "Nov 2, 2026"; "Refund" "$100.00 · Store credit"; "How hard" "2 of 5 · Fairly easy"; "Problems" "Restocking fee"; badge "Returned". |
| 15 | Pass | Buttons: Edit, I have it again, Edit return. No reminder/coverage wording; Policies card still "Covered", "1 policy" (worth a look). |
| 16 | Pass | Only Saw. |
| 17 | Pass | Edit drawer reuses title "Mark as returned"; summary "$110.00 · Store credit". |
| 18 | Pass | Status "Active"; "The return" summary removed entirely; not on list. |
| 19 | Pass | Test2 empty state. |
| 20 | Pass | "Not found." |
| 21 | Pass | "Refund" "Not paid yet"; no How hard/Problems rows. |
| /returns | Pass | "First design: example data"; Sony, Ninja (In progress, greyed buttons), Keurig, Bosch (Completed); no real items; link "Open the working list". |

Leftover data: Alice — UAT Return Drill (Active), Saw (Returned, Not paid yet), Kettle (Active).
Screenshots: step 7 assets/698ec443….png, step 8 assets/2e0c2fab….png, step 14 assets/5256f1c8….png

---
# FS-30 Insurance — build d1ed2c0 (run 08:39–08:44 ET, Nov 2 2026)
Personas: Test1/Alice, Test2/Bob. Items added (Target, Nov 2): Guitar $1,800 /items/01a19c7d-500e-7707-b2df-2f98abafe24d (category auto-set Musical instruments), Laptop $1,200 /items/01a19c7d-8300-74db-840f-dfb6bc678e73, Lamp $40 /items/01a19c7d-a256-7a3b-a793-31c2606dd924. Policy (deleted at end) /insurance/01a19c7e-9723-797d-a80e-641560a6646f.

| # | Result | Notes (quoted) |
|---|---|---|
| 1 | Pass | "Insurance", "No policies yet.", "Add your first policy" |
| 2 | Partial | Only "Choose the insurer." flagged; no other required fields called out. Nothing saved. |
| 3 | Pass | Insurer created inline: `Add "UAT Insurer"` → "UAT Insurer UNVERIFIED" |
| 4 | Pass | Field: "The end date cannot be before the start." Top alert is generic: "One or more validation errors occurred." |
| 5 | Pass | |
| 6 | Pass | Blank limit row silently ignored. |
| 7 | Pass | Saved, read-only page. |
| 8 | Pass | "Renter's · UAT Insurer · policy UAT-001"; badge "Until May 2, 2027"; "May 2, 2026 to May 2, 2027 · renews automatically"; "$240.00 a year", "$500.00", "$20,000.00"; tel:800-555-0100; "Make a claim online"; "Electronics: $2,500.00", "Musical instruments: $1,500.00" |
| 9 | Pass | "8 items, which cost $3,369.98." (verified: 89.99+89.99+1200+120+30+1800+40; returned Saw excluded, Sneakers unpriced) "No exceptions: every item is covered." |
| 10 | Pass | "Covered, under Musical instruments ($1,500.00), listed at $1,800.00" |
| 11 | **Fail** | No notes at top of policy page (also after reload): no over-limit comparison, no not-advice line. |
| 12 | Partial | Card: "UAT Renter's policy · UAT Insurer · until May 2, 2027"; "Deductible $500.00. Limit for Musical instruments: $1,500.00. Listed on the policy at $1,800.00."; "Call 800-555-0100"; "Make a claim online". **Missing over-limit note.** |
| 13 | Pass | Lamp card shows policy, deductible, no instrument limit. |
| 14 | Pass | "7 items, which cost $3,329.98." Lamp "Left out"; no Insurance card. Odd: Lamp's Policies card still "Covered 1 policy". |
| 15 | Pass | "Only the items you link below: 1 item, which cost $1,800.00." (grammar: "1 item, which cost") |
| 16 | Pass | "$240.00 a year for the policies still running."; row "Renter's · UAT Insurer · covers 1 item · $500.00 deductible · renews automatically" (extra "renews automatically") |
| 17 | Pass | Reader on. "Reading your document…" disabled; "you can keep filling in the form while you wait."; "Nothing is filled in until you press the button, and nothing is saved until you save."; "Nothing in this document matched what we look for." (receipt image used) |
| 18 | Not tested | Nothing found to accept/dismiss (needs a real policy page image). |
| 19 | Pass | "Leave without saving? You have changes that have not been saved. If you leave this page now they will be lost." Stay / Leave |
| 20 | Pass | Test2: "No policies yet."; Test1 URL "Not found." |
| 21 | Pass | "Delete this policy? This removes UAT Renter's policy, its limits, its documents and its link to your items. The items themselves stay." Guitar loses Insurance card. |

Other: no wrong amounts, no advice-like text, dates consistent. Delete dialog has two "Delete policy" buttons (dialog button not exposed via dialog role — accessibility). Console: 1 error on Test2 Not found page (not read).
Leftover: Alice UAT Guitar, Laptop, Lamp.
Screenshots: step 8 fc302606….png, 10 631df4fb….png, 11 144df223….png, 12 53a3b907….png

---
# FS-31 Extended warranty plan — build d1ed2c0 (run 08:45–08:51 ET, Nov 2 2026)
Personas: Test1/Alice, Test2/Bob. Items: UAT Fridge $900 /items/01a19c82-f67a-7b6f-b1fe-bc985c4f7028, UAT Washer $600 /items/01a19c83-3d7a-72ff-a629-218c2660e63c. Plan (deleted) /plans/01a19c84-22ee-7fae-aa9a-3528d362e378.

| # | Result | Notes (quoted) |
|---|---|---|
| 1 | Pass | "Extended warranties", "No plans yet.", "Add your first plan", "A plan bought at the store for a single item is added on that item instead." |
| 2 | Pass (note) | Only "Choose the company that sold the plan." flagged; Starts prefilled today. |
| 3 | Pass | Inline add → "UNVERIFIED" tag. |
| 4 | Partial | Field "The end date cannot be before the start." but top banner generic "One or more validation errors occurred." |
| 5 | Pass | |
| 6 | Pass | Read-only page, header "Until Sep 2, 2027". |
| 7 | Pass | "Sep 2, 2026 to Sep 2, 2027"; "$30.00 a month ($360.00 a year)"; "Per service call $75.00"; tel link; "Make a claim online"; covers/exclusions shown. |
| 8 | Pass | "Cover 2 items"; "UAT Fridge · $900.00", "UAT Washer · $600.00". |
| 9 | Pass | "UAT Home Warranty Co · 2 items · $360.00 a year"; "$360.00 a year for the plans still running, covering items that cost $1,500.00 in all." |
| 10 | Pass | Fridge: "Extended plan · UAT Home Warranty Co", "Sep 2, 2026 to Sep 2, 2027 · Until Sep 2, 2027", "Call 800-555-0111", "Make a claim online"; 2nd after "Return window · Target". |
| 11 | Pass | "Stop covering" immediate (no confirm); "1 item", "$900.00 in all." |
| 12 | Pass (note) | "uat-receipt.jpg (4 KB)" before upload vs "(3 KB)" after (rounding inconsistency); View opens blob tab; Delete has no confirm → "File deleted." |
| 13 | Pass | "$25.00 a month ($300.00 a year)". |
| 14 | Partial | Reader on; "Reading your document…"; "Nothing in this document matched what we look for." (receipt image, not a contract). |
| 15 | Partial | "Update from a newer document" exists; same no-match result; diff/accept untestable without real contract. |
| 16 | Partial | "It ended on" prefilled with today, so End this plan enabled by default; disabled once cleared. |
| 17 | Partial | "Plan ended." toast; term "Sep 2, 2026 to Nov 2, 2026", badge "Ends today" (not "ended"); row not dimmed; total still "$300.00 a year…$900.00" — plan counted as running on its end date. Plan expects exclusion. |
| 18 | Partial | Fridge still shows plan "Ends today"; "Next to end: Extended plan, Nov 2, 2026 · Ends today". |
| 19 | Pass | Test2 "No plans yet."; Test1 URL "Not found." |
| 20 | Pass | "Delete this plan? This removes UAT Home protection, its contract files and the plan coverage on 1 item. The items themselves stay." Fridge loses plan. |

Money: all figures match arithmetic. Leftover: Alice UAT Fridge, UAT Washer.
Screenshots: 7 556b8562….png, 9 b8b3d4fd….png, 17 e6e801c6….png & 10b2aaad….png

---
# FS-32 To-dos — build d1ed2c0 (run 08:52–08:55 ET, Nov 2 2026)
Personas: Test1/Alice, Test2/Bob. Item: UAT Reminder Blender /items/01a19c89-0c4f-789a-a205-5f9a3b7840d6. Console: none seen (passive only).

| # | Result | Notes (quoted) |
|---|---|---|
| 1 | Pass | "To do", "Nothing to do right now.", "Reminders such as registering a warranty show up here, and on the item they belong to. Your items" (link /items) |
| 2 | Pass | No To do card read-only. |
| 3 | Pass | "Add a reminder", placeholder "For example: register the warranty", "Due (optional)", Add disabled when empty. |
| 4 | Pass | "Due in 5 days" (orange outlined pill); no label on undated. Double-click Add created only one. |
| 5 | Pass (design note) | "Overdue since Nov 1, 2026" — neutral grey pill, not red/urgent; less prominent than due-soon orange. |
| 6 | Pass | Card stays after Done; order Check the cord, Register the warranty, Keep the box. |
| 7 | Pass | Same three on /todos, each linking "UAT Reminder Blender". |
| 8 | Pass | Mark as done removes from both pages. |
| 9 | Pass (gap) | Dismiss for now removes it; no dismissed/done section anywhere (/todos, item, /notifications "You are all caught up.") — dismissed to-do can't be found or brought back. |
| 10 | Pass (gap) | Not applicable removes it; no way to recover. |
| 11 | Pass | Nothing returned after reload. |
| 12 | Pass | Real-clock hourly job at 9:00 AM ET sent email "To do tomorrow: UAT Clock todo" ("UAT Clock todo is due tomorrow, on November 3, 2026.") and in-app notification "Needs action" with Done, Remind me later, Dismiss. Once only. Note: no overdue to-do reminder after the clock moved past Nov 3 (Todos = 0 on every run). |
| 13 | Pass | Test2 "Nothing to do right now." |
| 14 | Pass | Test2 "Not found." |

Odd: header bell briefly showed "Notifications, 1 to do" on /add/new before any to-do existed.
Screenshots: step 5 53d40fd8….png, step 7 e5e4df25….png

---
