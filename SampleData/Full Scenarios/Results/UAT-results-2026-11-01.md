# StuffIt / WarrantyBank UAT results

**Run date:** Nov 1, 2026 (EST)
**Site:** https://stuffit-ui.onrender.com
**Accounts:** Alice/Test1 = stevewash123.test@gmail.com, Bob/Test2 = stevewash123.tester2@gmail.com, Carol = stevewash123.tester3@gmail.com, Test4 = stevewash123.tester4@gmail.com (stood in for Alice in UAT-04)
**Tester:** QA Controller (browser + Gmail inboxes)

## Summary
| Plan | Status | Result |
|---|---|---|
| UAT-03 Shared policy vs private purchase | Run | 1 fail (step 7), 1 partial (step 1), rest pass |
| UAT-04 Three reports confirm | Run (partial) | 3 fail (steps 3, 5, 6), step 9 not built, steps 1, 2, 4, 10 pass, steps 7-8 skipped (admin/authenticator) |
| UAT-05 Time travel reminders | Skipped | Needs simulated clock + maintenance key |
| UAT-06 Accounts, email, reset | Run | 1 fail (step 14 password reuse allowed), rest pass |
| UAT-07 Purchases, items, privacy | Run | 2 fail (steps 1, 8), 1 partial (step 5), rest pass |
| UAT-08 Cards, notifications, export | Not started | Deletes Test2 at end |

---

## UAT-03: Shared policy data is visible to all; purchases stay private
Store used: **New Balance** (shared 30-day return policy, "Unconfirmed").

| # | Persona | Pass/Fail | What was seen (exact text) | Evidence |
|---|---|---|---|---|
| 1 | Alice | Partial | Added "UAT03 Alice Sneakers", Nov 1 2026. Form suggested "New Balance return policy [Merchant] 30 days [Unconfirmed]"; saved item showed "Nov 1, 2026 to Dec 1, 2026 · 30 days left". The expected "usual window, can differ for your item" note **never appeared**; nearest is "...confirm it on the source page before relying on it." | /items/01a19868-3738-7db5-a9a8-e5982273a070 |
| 2 | Bob | Pass | Added "UAT03 Bob Sneakers", Nov 1 2026. Same suggestion; "Nov 1, 2026 to Dec 1, 2026 · 30 days left". | /items/01a1986e-d5e9-7a1d-ba56-0b1c1b4de6c2 |
| 3 | Both | Pass (gap) | Policy text identical. Source link https://www.newbalance.com/returns loads (HTTP 200). Source link is only on the store page (Settings > Stores & brands), **not on the item page**. | /settings/stores/01a0ff7e-4cb1-7750-97d4-063ddd1f47c2 |
| 4 | Alice | Pass | Changed end date to Dec 15; item reads "Nov 1, 2026 to Dec 15, 2026 · Until Dec 15, 2026". | Alice item |
| 5 | Bob | Pass | Bob's item still "Dec 1, 2026 · 30 days left"; Alice's edit did not leak. | Bob item |
| 6 | Alice | Pass | No way to see other users' purchases or counts anywhere in nav, account, settings, store pages. | — |
| 7 | Alice | **Fail** | No "share" checkbox for submitting a policy exists. Added stores are private ("The ones you add are private to you." / "Only you can see this store until it is verified."). Shared stores have no add-policy option. Possibly an outdated plan step. | /settings/stores/01a1986a-6f17-7f52-85d4-d141dffc1c53 |
| 8 | Bob | Pass | Alice's private "UAT03 Alice Store" not visible to Bob in picker or store list. Nothing unverified shown as official. | — |
| Extra | Bob | Pass | Opening Alice's item URL as Bob: "Not found." No Alice data shown. | — |

**Other observations (UAT-03)**
- **Suggest coverage** button on the item page does nothing when clicked (clicked twice).
- Account menu overlay covers the item page Edit button until dismissed.
- Settings > Stores & brands: the Name box looks like a search box, but **pressing Enter creates a private store** with no confirmation; typing does not filter the list. (Created a stray "Alice" store under Bob; deleted it.)
- "Return or claim steps" link goes to a sample page: /items/sample/refund.
- New Balance Footwear warranty is placeholder: "A placeholder for testing: these are not the real terms."
- 1 console error on every page.

**Test data left:** Alice: item "UAT03 Alice Sneakers", private store "UAT03 Alice Store". Bob: item "UAT03 Bob Sneakers".

---

## UAT-04: Three independent matching reports confirm a policy
Store used: **UAT04 Policy Store** (shared store with no policy, created on the dev DB by DB Stager; owner_account_id NULL). URL: /settings/stores/01a198aa-3514-7532-b32d-331e15c2b59d. Page shows the "Shared data" badge and "No return policy yet."
Accounts: Alice = **Test4** (stevewash123.tester4@gmail.com, standard account) because my browser could not use the saved Test1 login; Bob = Test2; Carol = tester3. Steps 7-8 (Ops review queue) skipped per Steve: they need an authenticator and aren't critical yet.

| # | Persona | Result | What happened | Evidence |
|---|---|---|---|---|
| 1 | Alice | Pass | Added Everything else / 30 days, conditions "Items may be returned within 30 days of purchase with receipt.", source https://example.com/uat04-returns. Shows "30 days / Current / Added by you · Source / **Unconfirmed: entered by 1 person.**" No share checkbox exists (same as UAT-03 step 7); no success message. | store page |
| 2 | Alice | Pass | Identical policy again: red banner "A policy already exists for this store or brand and category. Enter the date the change took effect to add a new version." Nothing added; still "entered by 1 person." | store page |
| 3 | Bob | **Fail** | Bob saw "No return policy yet." (Alice's entry not visible). After adding 30 days his own entry reads "Unconfirmed: entered by **1** person." Expected 2 independent reports. | store page |
| 4 | Carol | Pass (as far as testable) | Carol also saw "No return policy yet." Added 45 days: "Unconfirmed: entered by 1 person." Stays unverified as expected, but because nothing is shared, not because of the mismatch. | store page |
| 5 | Carol | **Fail** | Options on her entry: "Correct a mistake" and "This no longer applies" ("Edit details" exists in page markup but isn't visible). Corrected to 30 days: still "Unconfirmed: entered by 1 person." Not confirmed or queued. Conditions text stayed "You have 45 days to return items." (correction doesn't prompt to update it). | store page |
| 6 | Alice | **Fail** | Alice sees only her own entry: 30 days, Unconfirmed, entered by 1 person, her source link. No confirmed value. | store page |
| 7 | Ops | Skipped | Admin review queue needs authenticator sign-in. | - |
| 8 | Ops | Skipped | As above. | - |
| 9 | Alice | Not built | No credits / contributions / points tally in account menu or Settings (Profile, Stores & brands, Notifications, Email, Credit cards, Privacy & data, Plan & billing). Plan & billing says "Arrives in milestone M5." | - |
| 10 | Bob | Pass | /admin, /admin/review, /admin/policies, /review-queue all silently redirect to Home with no admin content. https://stuffit-api.onrender.com/api/admin/policies returned **401 Unauthorized** (opened in the browser, likely without a bearer token, so it doesn't show 403 handling for a signed-in non-admin). | - |

**Other observations (UAT-04)**
- **Core finding:** on a store labelled "Shared data", each user's policy entry is private to them. Others still see "No return policy yet.", and counts never go above "entered by 1 person". Cross-user confirmation seems missing or not wired up.
- Shared stores that already have a policy (e.g. Aaron's) show an Add form to every user, so any user appears able to add policy versions to shared data. Effect on other users not tested.
- Admin URLs redirect to Home with no "not allowed" message (fine for security, but no feedback).
- The settings store list shows only the first 100 stores alphabetically (ends at "Capital One"); the rest are reachable only via Search.
- Carol's session dropped back to /login several times during an earlier run.
- Account menu sometimes needs a second click before "Sign out" appears.

## UAT-05: Skipped
Needs the app running with `Clock:Simulated=true` and the `Maintenance:Key` for the maintenance API.

---

## UAT-06: Create accounts, confirm by email, sign in, recover a password
Precondition note: both accounts already existed and were confirmed before the run (created earlier the same day), so steps 5, 6 and 11 are from that earlier sign-up.

| # | Persona | Pass/Fail | What was seen (exact text) | Evidence |
|---|---|---|---|---|
| 1 | none | Pass | Redirect to /login?returnUrl=%2F. Tab title "Sign in · WarrantyBank". | — |
| 2 | none | Pass | /terms, /privacy, /disclaimer load with no sign-in wall (~0.6s each). Each says "Draft for review. This text has not yet been read by a lawyer. Items in [square brackets] are filled in before launch." | — |
| 3 | Test1 | Pass | Empty submit: "Enter a valid email address.", "Use at least 10 characters.", "Please agree to continue." Confirm password has no message. | — |
| 4 | Test1 | Pass | Short password: "Use at least 10 characters." Email "abc": "Enter a valid email address." No stack trace/JSON. | — |
| 5 | Test1 | Pass | "Check your email" — "We sent a link to [email]. Open it to finish creating your account. It works for 24 hours. Nothing is created until you do." | — |
| 6 | Test1 | Pass | Email arrived within ~1 min. From "StuffIt <noreply@stuff.microsaasbuilders.com>", subject "Confirm your email to start with WarrantyBank", link https://stuffit-ui.onrender.com/verify-signup?token=… (correct site). Reply-To stuffit-admin@microsaasbuilders.com. | Gmail |
| 7 | Test1 | Pass | Reusing the confirm link: "This link has expired or was already used. Sign up again, or sign in if you already confirmed." | — |
| 8 | Test1 | Pass | After sign out + Back: /login, no account data. | — |
| 9 | Test1 | Pass | Wrong password for real and non-existent email both: "Invalid email or password." (401). | — |
| 10 | Test1 | Pass (issue) | Lands on Home; nav Home, My Items, New Items, Returns, Notifications. First two attempts got 429 with "Something went wrong. Please try again." | — |
| 11 | Test2 | Pass | Test2 created and confirmed via its own inbox. | — |
| 12 | Test2 | Pass | Sign-up with Test1 address: "An account with this email already exists. Try signing in." (409). No error page. | — |
| 13 | Test1 | Pass | Forgot password: "If that email is registered, we sent a link to reset your password. It may take a minute to arrive." | — |
| 14 | Test1 | **Fail** | Reset email arrived in ~1s: "Reset your WarrantyBank password". Reset page "Choose a new password" accepted **the current password** as the new one: "Your password was changed. Sign in with the new one." Sign-in afterwards works. (Old-password-refused check not possible since password unchanged.) | screenshot on tester box |
| 15 | Test1 | Pass (wording) | Reused reset link: form loads normally; on submit shows "Invalid token." | — |
| 16 | Test2 | Pass | Reset for nobody.uat@example.com shows the same neutral message as step 13. | — |

**Other observations (UAT-06)**
- **Rate limit UX:** login returns 429 after ~3 attempts in a few minutes; UI shows only generic "Something went wrong. Please try again." Suggest a "too many attempts, wait" message.
- **Account enumeration inconsistency:** sign-in and forgot-password hide whether an email exists; sign-up reveals it ("An account with this email already exists.").
- **Reset link reuse:** used link still renders the form; error only after submit, and "Invalid token." doesn't say used/expired.
- Reset success shows a "Sign in" button but doesn't redirect.
- Empty email says "Enter a valid email address." rather than "required".
- Console: 401s on /api/auth/refresh when signed out (expected); 1–3 other console errors after sign-in, not inspected.
- No page slower than 3s.
- **Sign-up 'Wrong address? Start again':** returns to the form with the old email, both passwords and the checkbox still filled in.

---

## UAT-07: Add purchases, check suggested coverage, browse items, prove privacy
Precondition note: each account already had one UAT-03 item (left alone). Store used: **Best Buy** (15-day return). Brand: **Cuisinart** (1-year warranty). Category: Small appliances.

| # | Persona | Pass/Fail | What was seen (exact text) | Evidence |
|---|---|---|---|---|
| 1 | Test1 | **Fail** | "Add a purchase" opens (/add/new), but field order is Store, Date, Credit card, Order number, Category, Brand (optional), Item, Model number: brand comes **after** store. Price is hidden under "More about this item: price, size, serial number, notes". | /add/new |
| 2 | Test1 | Pass | "Add at least one item." and "Tell us what you bought." Nothing saved. Store/date not called out. | /add/new |
| 3 | Test1 | Pass | Saved "UAT Blender", "Bought Nov 1, 2026 from Best Buy", "$89.99". | /items/01a19878-cdaf-7d02-b0c0-e88cf2cee40f |
| 4 | Test1 | Pass | Read-only item: Brand Cuisinart, $89.99, Best Buy, Nov 1, 2026. | same |
| 5 | Test1 | Partial | "Return window · Best Buy: Nov 1, 2026 to Nov 16, 2026 · 15 days left"; "Manufacturer warranty · Cuisinart: Nov 1, 2026 to Nov 1, 2027". Arithmetic correct. **No "usual window, can differ" note.** Warranty text is "[placeholder] Fake terms for testing". | same |
| 6 | Test1 | Pass | "Edit" button; edit mode shows Done, Mark returned, Mark disposed, Delete, Edit item, Edit purchase, per-coverage Edit/Remove, Add coverage, Suggest coverage, Receipts and files. | same |
| 7 | Test1 | Pass | Renamed to "UAT Blender 2"; shows on item and in My Items. | same |
| 8 | Test1 | **Fail** | "I am not sure of the exact date" > Only the month. Item shows "Bought Nov 2026 (approximate)", $25.00, but coverage shows **exact days** ("Nov 1, 2026 to Nov 16, 2026 · 15 days left", "Until Nov 1, 2027") and badge "Expiring soon", not a range / "may be covered". Helper: "Pick any day in the right month. We plan on the start of it." | /items/01a19879-bfae-79e4-9e72-b581989b434f |
| 9 | Test1 | Pass (issue) | Uploading a 64x64 PNG: "Reading your document…" (~5s) then "One or more validation errors occurred. You can fill it in yourself. It is not attached yet: press Upload to attach it anyway." After Upload: "Receipt receipt.png (100 B)" with View / Read it / Delete; View opens it; persists after re-login. File size changed 178 B to 100 B. API: 400 on /api/intake. | Blender 2 item |
| 10 | Test1 | Pass | "Toaster" and "Blender" match correctly; "zzqqnomatch" shows "No items match." with "Clear filters". | /items |
| 11 | Test1 | Pass | Filter and sort dialog (Status, Sort, Store, Brand, Category). Active filter narrowed; "Clear all" restored. | /items |
| 12 | Test1 | Pass | URL noted; signed out. | — |
| 13 | Test2 | Pass | Only "UAT03 Bob Sneakers". | /items |
| 14 | Test2 | Pass | Test1 item URL: "Not found." No Test1 data. (API 404) | — |
| 15 | Test2 | Pass | "UAT Kettle", Best Buy, $19.00 saved; category auto-filled Small appliances. | /items/01a1987b-f11a-796b-99ba-12d11e3b1c87 |
| 16 | Test1 | Pass | "Kettle": "No items match." | /items |
| 17 | Test1 | Pass | "Delete this item? UAT Toaster and its coverage and files are removed. This cannot be undone." Deleted; no Undo offered. | /items |
| 18 | Test1 | Pass | After reload and re-login: UAT Blender 2 (receipt still attached) and UAT03 Alice Sneakers; Toaster gone. | /items |

**Other observations (UAT-07)**
- Best Buy policy text mentions an extended holiday return window, but the app used a flat 15 days for a Nov 1 purchase.
- Cuisinart warranty is "Unconfirmed" and **not ticked by default**; a user who doesn't tick it gets no manufacturer warranty.
- Receipt-reading error message is raw ("One or more validation errors occurred.").
- My Items briefly shows a partial list right after reload, then fills in.
- Account menu button toggles; easy to close it by accident when reaching for Sign out.
- API noise: 404 on /api/items/new when opening /add/new; 409 on /api/parties.

**Test data left:** Test1: UAT Blender 2 (with receipt). Test2: UAT Kettle.
