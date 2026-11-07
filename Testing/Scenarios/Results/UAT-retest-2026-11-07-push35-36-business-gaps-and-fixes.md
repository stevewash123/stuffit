# UAT retest: Push 35+36 business gaps, per-account upload queue, and Push 34 fixes

- **Test date:** Nov 7, 2026 (ET), about 5:14 PM – 5:28 PM ET.
- **Build:** API `619cfcd` (Staging, started 5:05 PM ET; push 35 alone `c103d4a`), UI `c7a7367` (Last-Modified 5:06 PM ET Nov 7; push 35 alone `8752182`). No migration. Notes: `CHANGES-push-35-business-gaps-and-per-account-upload-queue-2026-11-07.md`, `CHANGES-push-36-push-34-fixes-2026-11-07.md`.
- **Accounts:** Alice (P34-Alice Repairs owner), Bob (QA Test 2, re-invited, two accounts), Carol (personal Carol + P34-Acme Plumbing owner), p34owner (Acme employee, then removed), Ops (Admin > Businesses). Push 34 fixtures kept instead of an Alice/Bob reset.
- **Clock:** moved only for the free-year reminder (+365, +381, +388, +389 days); reset in a finally block, verified Offset 0 at 5:16:39 and 5:17:26 PM ET. **Final check: GET `/api/maintenance/clock` → "Offset 0 day(s); the app's time is 2026-11-07 22:27:45Z."** (5:27 PM ET). No reset needed.
- **Scope:** targeted only: Push 35 checks 1–4 and Push 36 fixes 5–9 (`PENDING-RETEST.push35-36-started.txt`). No regression.
- **Evidence:** `/workspace/uat/push35-36-findings.md` (source of truth); API responses in `/workspace/uat/push35-36-api/` (no tokens/passwords).

## Summary
12 result rows.

| Result | Count | Rows |
|---|---|---|
| Pass | 7 | #2 account name on notices/email (Acme, API); #3 Switch account in account menu; #5 change-back refused by API with employee present; #6 employee Privacy & data; #7 replacement link back; #8 cancel/end closes to-do; #9 Admin "1 person" |
| Partial | 2 | #4 free-year reminder sent at 30 and 7 days; #3 chooser page has no own Switch account link (note) |
| Fail | 0 | — |
| Inconclusive | 3 | #1 per-account upload queue (needs phone/app); #5 UI button state not checked on screen; Bob's pre-fix cancelled-plan to-do |

## Partials
1. **#4 — free-year reminder sent twice per business.** Notes: "gets a notice (and email) before the free year ends, once per business". Acme (freeUntil Dec 7, 2027): at +365 days (30 days before end) one notice "Your free year ends in 30 days" + email; at +381 (14 days) nothing new; at +388 (7 days) **another** notice "Your free year ends in 7 days" + email. Immediate reruns and +389 sent nothing (FreeYear=0); Acme ends with exactly two notices. Looks like one per 30-day/7-day milestone — bug or notes wording to fix.
2. **#3 — chooser page has no own "Switch account" link (note).** Notes say the link is "in the account menu and on the chooser page". Menu has it; the chooser page itself doesn't, though the chooser already is the switch page.

## Inconclusives
1. **#1 Upload queue.** Desktop upload ("Upload a receipt or warranty") is a single-file chooser that sends at once; no queue/pending list. Profile: Wi-Fi-only sending "is not available in this browser… It will work in the WarrantyCat app." Needs phone/app.
2. **#5 UI.** API refusal passes, but the "Change back to a personal account" button state was not checked on screen (owner logins Alice/Carol are env-only, not vault).
3. **Bob's old to-do.** Bob's pre-fix cancelled-plan "Add the rest of your plan" to-do not rechecked (Bob API token expired; no password retry). Fix verified on new Carol fixtures (#8).

## Detailed results

### Push 35
- **#1 Upload queue per account — Inconclusive.** See above.
- **#2 Account name on notices — Pass (API, reminder path).** Acme notification body: "P34-Acme Plumbing: Your free year ends on Dec 7, 2027. WarrantyCat will tell you about plans before anything is charged." Title "Your free year ends in 30 days" (account in body, not title). Email subject "P34-Acme Plumbing: Your free year ends in 30 days"; body starts "StuffIt" / "For P34-Acme Plumbing" (Gmail `1a1b815c56000569`, 5:16:36 PM ET). 7-day email also names the account (`1a1b815cb6e0915a`). Weekly digest line not exercised. On screen (Bob): no business notices yet; personal Held Toaster notices (created while Bob had one account) have no prefix — not a fail.
- **#3 Switch account — Pass (menu) / Partial note (chooser).** Account menu "Switch account" → chooser lists "Personal — Your own things" / "P34-Alice Repairs — Employee". With one account (before re-invite) no link, as expected.
- **#4 Free-year reminder — Partial.** API plan Acme: `personLimit:3`, `peopleCount:2`, `freeYearEnded:false`, includes "The free year includes you and two employees." Plan page template (source inspection, not on screen): "Your free year ends on <date>. WarrantyCat will tell you about plans before anything is charged." Reminders: see Partial 1. First global run also sent Alice "P34-Alice Repairs: Your free year ends today" (`1a1b815c707fada1`). Runs: FreeYear=2, then 1; Failed=0 throughout.

### Push 36
- **#5 Change back disabled — Pass (API) / UI Inconclusive.** No canChangeBack flag; shipped UI reads `business/people`, `alone = people.length <= 1`, disabled when `busy || !alone`. Acme (Carol + p34owner) convert-to-personal → 409 "Other people are on this business account, or invited to it. Remove them first to change it back to a personal account."
- **#6 Employee Privacy & data — Pass.** In P34-Alice Repairs as employee: Download everything and Delete my account absent; shows file-retention choices, "You have 0 files." Personal account still shows both.
- **#7 Replacement link back — Pass.** "Replacement for P34-Repl-Model Vacuum, under its protection plan" — name links to /items/01a1b6f3-7f81-79f4-9656-2d7a7b50e5bf (old, Replaced, VC9/P34S06). P34-Repl-Carry New links to P34-Repl-Carry Vacuum. API: new Carol replacement has `replaces: {itemId:"01a1b814-ecab-72db-ad19-1192c8794548", name:"P36 Link Old Test"}`.
- **#8 Cancel/end closes to-do — Pass.** To-do "Add the rest of your P35 Test Plan Co plan" / "Still missing: contract number, claim contact. Having them at hand makes a claim quicker." Cancel (`cancelNow`) → 200; to-do closed, status done (separate "Check that your refund arrived" created). End → 200; open list empty, to-do done. Return-plan-answer path not separately exercised.
- **#9 Admin Businesses — Pass.** "P34-Alice Repairs — 2 people, up to 3"; "P34-Acme Plumbing — 1 person, up to 3". Row buttons Extend 30 days / Extend a year / Allow 4 people.

## Skipped by design (not reported as fails)
- 'Van 1' search returns Van 2 (by design; use Location filter).
- B5 chooser not shown after accepting invite (by design S8.1.6).
- B13 identical replacement name (typed name).
- Push 34 Inconclusives (Google button, switcher reload, admin audit) — human look, not this run.
- Push 34 Known gaps / deferred.

## Data staged
- Alice invited Bob to P34-Alice Repairs (201, 5:19 PM ET); Bob accepted on screen ("This address already has a WarrantyCat login. Sign in with it to accept. Your own things stay as they are, and you can switch between the two.") → two accounts.
- Carol removed p34owner from Acme (204) to get a one-person business for #9.
- Carol personal fixtures: P36 Link Old Test → P36 Link New Test (replacement, continue); two items with P35 Test Plan Co plans (one cancelled, one ended).
- **Side effect:** Alice was alone in P34-Alice Repairs, so the #5 change-back call returned 204; converted straight back (204). Plan reinitialized: personLimit 4 → 3, freeUntil Nov 7, 2027 11:34:45 AM ET → 5:17:26 PM ET. Name/kind restored; no invitations, memberships or items deleted.
- Carol's last-used account is now personal.

## Needs CC / human
1. Decide #4: one reminder per business, or one per 30/7-day milestone (fix code or notes).
2. #3: should the chooser page carry its own "Switch account" link?
3. #1 upload queue: test on a phone/app (queue in business, switch to personal, switch back).
4. #5: check the change-back button state on screen with an employee present.
5. Push 34 Inconclusives (Google button, switcher reload, admin audit) still need a human look.

## Test emails sent (test inboxes only, automated)
- Carol (tester3): two Acme free-year reminders (30 days, 7 days).
- Alice: one "P34-Alice Repairs: Your free year ends today".
- Bob (tester2): P34-Alice Repairs re-invite.
- No manual Gmail sends.

## Cleanup state
- Clock **Offset 0** (verified 5:27 PM ET).
- Fixtures left: P34-Alice Repairs (Alice owner, Bob employee, limit 3, free until Nov 7, 2027); P34-Acme Plumbing (Carol owner alone, free until Dec 7, 2027); p34owner has no membership; Carol personal P35/P36 fixtures; Bob's Push 34 fixtures.
- Bob signed in on screen; Bob API token expired.
