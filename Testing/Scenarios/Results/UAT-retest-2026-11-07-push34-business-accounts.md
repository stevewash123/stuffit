# UAT retest: Push 34 business accounts and memberships

- **Test date:** Nov 7, 2026 (ET), about 11:26 AM – 12:15 PM ET.
- **Build:** API `d356106` (migration BusinessAccounts), UI `0ce7781` (deployed 11:09 AM ET Nov 7), with digest fix `188faba`. Notes: `CHANGES-push-34-business-accounts-and-memberships-2026-11-06.md`.
- **Accounts:** Alice (QA Test 1, converted to P34-Alice Repairs owner), Bob (QA Test 2, existing login invited), Carol (existing login, Acme ownership transfer), Ops (Admin > Businesses), new logins p34owner (P34-Acme Plumbing), p34emp (P34 Employee), p34self (P34 Self). Test inboxes: tester3 plus-addresses (+p34owner/+p34emp/+p34self/+p34expire/+p34extra/+p34revoke), tester2 (Bob).
- **Clock:** moved only for B4b (+8 days) and API-6 (+3/+4/+6 days); reset after each. **API-7 final check 12:14 PM ET: GET `/api/maintenance/clock` → "Offset 0 day(s); the app's time is 2026-11-07 17:14:32Z."** No reset needed.
- **Scope:** targeted only: Push 34 steps (B1–B11, API-1..API-7) plus Push 33 fix retests (B12, B13). No regression.
- **Evidence:** `/workspace/uat/push34-findings.md` (source of truth); screenshots in `/workspace/uat/push34-shots/` for B1, B1b, B3, B5-UI only (B2, B12, B13 not saved).

## Summary
34 result rows.

| Result | Count | Rows |
|---|---|---|
| Pass | 25 | B1 steps 1, 3, 4; B1b; B2 steps 0–6; B3; B4; B5 accept/isolation; B5/B6-UI employee views; B6; B7 steps 1, 2, 4–8; B8; B9; B10; B11; B12 plan choice; B13 model/serial; B13 Please-check; API-1..API-7 |
| Partial | 6 | B2 step 7; B5 chooser; employee sees Download everything / Delete my account; notice doesn't name account; B7 step 3 'Van 1' search; B12 replacement doesn't link back |
| Fail | 0 | — |
| Inconclusive | 3 | Google sign-up button (B1 step 2 / B11); switcher page reload; Ops change audit line |

## Partials and fails
1. **B2 step 7 — change back enabled while invite pending.** UI "Change back to a personal account" stays enabled with an invitation pending and opens "Change back to a personal account?" / "Nothing is lost. The business name is no longer shown." (cancelled). Server refuses: POST business/convert-to-personal → 409 "Other people are on this business account, or invited to it. Remove them first to change it back to a personal account." UI should disable/refuse up front.
2. **B5 — chooser never shown.** After Bob accepted, next sign-in returned needsChoice false and went straight into P34-Alice Repairs; accepting appears to count as "last used". After switching to personal, sign-in goes straight to personal. p34emp also signed straight in (personal). Notes describe a chooser on next sign-in.
3. **Employees see Download everything / Delete my account.** In the business, P34 Employee still sees "Download everything" / "Prepare my download" and "Delete my account" (with confirm fields); server refuses both (403 "Only the owner of the business can do that.").
4. **Notice doesn't name account.** "Add a credit card and confirm its benefits" does not name an account though P34 Employee has 2 accounts; notes say a notice names its account when you have more than one.
5. **B7 step 3 — 'Van 1' search returns Van 2.** q=AT-002 → exactly P34-Tag-B Hose. q=Van 1 → P34-Tag-A Pump **and** P34-Emp-Item Ladder (Van 2). Exact location filter (location=Warehouse) works.
6. **B12 — replacement doesn't link back.** Old items show "Replaced" with a link to the replacement; replacement shows "Replacement for <old item>, under its protection plan" but the old name isn't a clickable link (Push 33 notes: "links across").

Minor (not counted as Partial):
- B13: "Add the rest of your plan" to-do persists on the cancelled plan (P34-Plan-Ret-Manual) and stays on the old item after replacement, not the replacement.
- B13: replacement keeps the identical name ("P34-Repl-Model Vacuum is marked replaced by P34-Repl-Model Vacuum"), confusing in the list.

## Minor notes
- B1b header truncates business name ("P34-Acme Plumbi…").
- B2 step 4 rename: no save confirmation text.
- B8: Admin shows "1 people" (grammar). No confirm dialog, no step-up code on admin plan changes.
- B9: Carol's invitation landed in Spam; inviter shown as raw email since p34owner has no display name; in the employee's People view p34owner appears as "Team member". Acme freeUntil 2027-12-07 after Extend 30 days, but account licenseEndsAt still 2027-11-07 (may be separate field).
- B10: no notice to owner when someone leaves (not promised).
- B11: sign-up page first rendered blank; reload fixed it.
- API-6 Run A: with digest email off before reminders, notices emailed at once (matches CHANGES); script design issue, not a defect.
- B6: model/serial keys in POST /purchases item body are ignored; set via PUT items/{id}.

## B13 Please-check answer (for the notes)
The P33 fixture's add method (P33-Plan-Ret-Refund) was not recorded in push33 findings and the fixture was deleted in the Alice reset. This run: P34-Ret-Manual Toaster plan added via item page Add-on protection > "I'll type it in" (P34-Plan-Ret-Manual, $49, Oct 1 2026–Sep 30 2028). Plan page says nothing about a receipt/document, only "Started same day as the purchase"; no notification about the plan. On Mark returned, "Did you return P34-Plan-Ret-Manual too?" had **nothing preselected**, "Nothing about a plan changes until you answer", button disabled until picked. "Yes, no refund" → "P34-Ret-Manual Toaster is marked returned. P34-Plan-Ret-Manual: cancelled." (Cancelled Oct 1–Nov 6 2026). Pass.

## Detailed results

### B1a — business sign-up (p34owner, incognito) 11:26 AM ET
- 1 Pass: "Who is WarrantyCat for?" For myself (default) / For my business.
- 2 Inconclusive: Business name field appears for business; no Google sign-up button in any mode, so hide/return can't be verified.
- 3 Pass: empty name → "Enter the name of your business."
- 4 Pass: "We sent a link to stevewash123.tester3+p34owner@gmail.com. Open it to finish creating your account. It works for 24 hours." / "Nothing is created until you do..."; Send it again / Wrong address? Start again. Email "Confirm your email to start with WarrantyCat" arrived 11:26 AM ET.

### B1b — verify + owner checks 11:28 AM ET — Pass
- Verify link → /orientation. People: "People in P34-Acme Plumbing"; "Owner · Joined Nov 7, 2026"; "...Your business has room for 3 people including you."
- Plan & billing: "Free until Nov 7, 2027" / "The free year includes you and two employees. You have 1 of 3 places used, counting invitations that are waiting." No charge.
- Profile: Save name; "Change back to a personal account" ("Only possible while no one else is on the account or invited to it."). No switcher.

### B2 — Alice convert + invites 11:30–11:36 AM ET
- 0–1 Pass: no chooser; P34-Before Drill (DR34/P34S01) present.
- 2 Pass: "Change to a business account?" / "This account becomes P34-Alice Repairs, with you as its owner. Nothing in it is lost. It can be changed back while no one else is on it."
- 3–4 Pass: header P34-Alice Repairs; item kept; rename updates header.
- 5 Pass: "Invitation sent to stevewash123.tester3+p34revoke@gmail.com."; revoke → "The invitation to ... is cancelled."
- 6 Pass: invite p34emp; Resend "Invitation sent again to ...". Email subject "P34-Alice Repairs invited you to WarrantyCat", "works once, for 7 days".
- 7 Partial (see above).

### B3 — new employee joins (p34emp) 11:40 AM ET — Pass
- Join page: "Join P34-Alice Repairs", inviter "QA Test 1", "You will see and add the business's things under your own login." / "We use this address only for this invitation.", "At least 10 characters", button "Create my login and join".
- accept-invitation 201: business/employee + personal "P34 Employee"; needsChoice false. Reuse → 400 "This invitation has expired, was cancelled or was already used. Ask your employer to send a new one."
- Employee People: names only. Invite → 403 "Only the owner of the business can do that." Items: mine empty; "Show everyone's items" shows P34-Before Drill. Switch to personal 200.

### B4 — owner notice, expiry, revoke — Pass
- a: "P34 Employee joined P34-Alice Repairs" / "P34 Employee accepted your invitation and can now see and add the business's things." action "See your people"; email 11:40 AM ET.
- b: p34expire link valid, clock +8 days → 400 expired message; clock reset to 0.
- c: p34expire revoked (204); Bob invited (201); owner People shows emails.

### B5 — Bob existing login accepts 11:45 AM ET
- Pass: existingLogin true; accept-invitation-signed-in 200; memberships QA Test 2 + P34-Alice Repairs. Switch to Carol's account → 403 "You are not a member of that account." Items don't mix.
- Partial: chooser (see above).

### B5-UI / B6-UI — P34 Employee on screen 11:50 AM ET
- Pass: switcher "Personal" / "P34-Alice Repairs"; header shows business name. Inconclusive: no visible full reload on switch. Everyone's items list shows 5 business items. People names only (QA Test 1 Owner, P34 Employee (you), QA Test 2), no Invite/Resend/Revoke/Remove; Leave shown. Plan & billing, rename, Change back hidden.
- Partial: Download everything / Delete my account shown; notice doesn't name account.

### B6 / API-3b — employee item + owner follower — Pass
- Bob created P34-Emp-Item Ladder (LD34/P34S02, AT-010, Van 2); notes edit "P34 employee edited these notes." visible to both. enteredBy "QA Test 2"; Alice follows (isOwner false); no email fields. Bob marketing pref changed and restored.

### B7 — asset tags and locations
- 1 Pass; 2 Pass: at-001 → 400 "Asset tag at-001 is already on P34-Tag-A Pump. Each tag can be on one item."; 3 Partial; 4 Pass (Warehouse / noTag filters); 5 Pass (API data; on-screen not checked); 6 Pass (tag released after delete); 7 Pass: "Use 40 characters or fewer for the asset tag." / "Use 80 characters or fewer for the location."; 8 Pass: locations ["Van 1","Van 2","Warehouse"].

### B8 — limit + Ops Admin — Pass
- 4th person → 400 "Your business account includes you and two employees."
- Ops sign-in with authenticator accepted first try. Admin > Businesses lists both businesses; "Allow 4 people" → "3 people, up to 4 (raised)"; Acme "Extend 30 days" → Free until Dec 7, 2027. Audit line not visible (Inconclusive).
- Then invite p34extra 201; "The free year includes you and three employees."; invitation revoked.

### B9 — ownership transfer (Acme) 11:57 AM ET — Pass
- p34owner invites Carol; Carol accepts; "Carol joined P34-Acme Plumbing". Offer email "P34-Acme Plumbing would like you to be its owner on WarrantyCat" ("...The offer works for 7 days."). Accept → Carol owner, p34owner employee (invite → 403). On-screen "Becoming the owner" page not checked.

### B10 / API-5 — remove and leave 12:00 PM ET — Pass
- Alice removes p34emp 204; Bob leaves 204, old business token 401 at once; Bob only has personal. Alice People: owner only. Ladder stays, Entered by "QA Test 2", reminders to Alice. p34emp on screen: "Welcome, P34", no switcher, no business.

### B11 — "For myself" sign-up (p34self) 12:10 PM ET — Pass
- "At least 10 characters. A few random words make a strong password."; "Check your email" text. Signed in as P34 Self: no business name/switcher/People; "Use WarrantyCat for a business" offered; no Asset tag/Location fields or filters.

### B12 — Push 33 retest: replacement plan choice (Bob) — Pass (link-back Partial)
- Nothing ticked; "Make the replacement" disabled until chosen. Options: "Carry on with the replacement" / "End the plan" ("Ends the plan on Oct 25, 2026.") / "Start a new term from Oct 30, 2026".
- Carry (2026-10-20): May 1, 2026 – May 1, 2028. End (2026-10-25): "Ended Oct 25, 2026". Restart (2026-10-30): Oct 30, 2026 – Oct 30, 2028.

### B13 — model/serial + Please-check (Bob) 12:13 PM ET — Pass
- Model/serial: after adding P34-Plan-Repl-Model, replace form pre-filled Name, Model "VC9", Serial blank; no plan option preselected. Saved P34-NewBrand / VC10 / P34S10, Carry on → "P34-Repl-Model Vacuum is marked replaced by P34-Repl-Model Vacuum. P34-Plan-Repl-Model: carries on with the replacement." Replacement shows VC10/P34S10, no P34S06.
- Please-check: see answer above.

### API batch
- **API-1 Pass:** revoked/pre-resend tokens → 400 expired message; latest → 200 {businessName P34-Alice Repairs, invitedBy QA Test 1, existingLogin false}; single use.
- **API-2 Pass:** invite expires after 7 days (+8 days → 400); clock reset 0.
- **API-3 Pass:** 12 owner-only calls as employee → 403 "Only the owner of the business can do that."; People names only.
- **API-4 Pass:** business export 202 → ready → 5846-byte ZIP; items.csv has asset_tag,location; deleted Tag-B absent; account.json kind business, 3 people.
- **API-5 Pass:** remove/leave (see B10).
- **API-6 Pass:** digest fix 188faba: Run B "Digest run: sent 1 (1 weekly), skipped 0, failed 0."; in-app "3 things need your attention this week"; held notices not emailed; no digest email; rerun sent 0. Bob prefs restored (diff empty).
- **API-7 Pass:** clock Offset 0 (12:14 PM ET).

## Data staged
- p34owner business P34-Acme Plumbing (sign-up); p34self personal (P34-Self Kettle); p34emp via invitation.
- Alice converted to P34-Alice Repairs; P34-Before Drill; Bob's P34-Emp-Item Ladder; P34-Tag-A Pump, P34-Tag-C Valve, P34-NoTag Bucket (Tag-B deleted in test).
- Bob personal: P34 Held Toaster 1–6; P34 Plan Co; P34-Repl-Carry/End/Restart/Model Vacuums with plans; P34-Ret-Manual Toaster (plan cancelled); replacements.
- Bob's password reset via forgot-password to the vault login (12:02 PM ET); p34emp password reset via reset page; Ops admin extended Acme +30 days and raised Alice limit to 4.

## Needs CC
1. **Google sign-in button — Inconclusive.** No Google button in any sign-up mode on staging (likely not configured); hide/return behaviour for business sign-up can't be verified.
2. **Switcher page reload — Inconclusive.** Confirm whether switching account fully reloads the page.
3. **Admin audit line — Inconclusive.** Notes say admin plan changes are audited; nothing visible in UI.
4. Not checked on screen: B9 "Becoming the owner" page text; B10 Leave confirm text; B7 asset tag/location display on list/detail.

## Test emails sent (test inboxes only)
- tester3: p34owner confirm; p34revoke, p34emp (x2), p34expire, p34extra invites; Carol (Acme invite — Spam; ownership offer); p34self confirm; p34emp password reset.
- tester2 (Bob): P34-Alice Repairs invite; Toaster 1–3 reminder emails; forgot-password.
- Owner notice emails to Alice ("P34 Employee joined…") and p34owner ("Carol joined…").

## Cleanup state
- Clock **Offset 0** (verified 12:14 PM ET).
- Fixtures left: Bob's P34 vacuums/toasters; P34-Alice Repairs (Alice owner, alone, limit 4); P34-Acme Plumbing (Carol owner, p34owner employee, free until Dec 7, 2027); logins p34owner, p34emp, p34self.
- Bob prefs restored. Bob is left on his vault password (env QA_PASSWORD_BOB stale).
