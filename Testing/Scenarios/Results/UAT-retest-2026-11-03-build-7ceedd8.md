# StuffIt retest - build 7ceedd8 (Staging) - Nov 3, 2026
Commit 7ceedd8 (Staging, started 7:14 AM ET). Retest only, per Bot Rules/RETEST-NEXT-BUILD.md (updated 7:12 AM, with second push). No regression, at Steve's request.
Runs: 8:25-8:55 AM ET. Accounts were reset by DB Stager at 8:22 (all 4) and 8:42 (Alice and Bob); Ops two-step was kept.

## Totals
| Chunk | Area | Steps | Pass | Partial | Fail | Not run |
|---|---|---|---|---|---|---|
| A | Receipts/Add Details, per-item coverage, upload note, usual-window note, store field, time zone, bell, PDF View, export | 29 | 21 | 7 | 0 | 1 |
| B | To-do reminders type, soft-closed return windows, wizard courtesy link | 20 | 19 | 1 | 0 | 0 |
| C | Claim wizard reload and courtesy wording | 10 | 8 | 2 | 0 | 0 |
| D | Recovered card and recoveries.csv | 10 | 9 | 1 | 0 | 0 |
| **Total** | | **69** | **57** | **11** | **0** | **1** |
Earlier on 83fdfd8: SM-1 export download Pass, FS-28 13/13 Pass (step 9 "Brands (makers)" fixed).

## Fixes confirmed
- PDF View opens (200 application/pdf), and the export ZIP downloads (200) with 14 data files plus receipts. recoveries.csv is correct.
- The profile time zone shows America/New_York and keeps it when Time of day changes.
- To-do reminders are their own notification type. The email and bell entry name the item, the email arrives on the due date, the unsubscribe page says "To-do reminders", and turning them off stops them.
- The bell count matches the Notifications page for both Alice and Bob.
- Add Details keeps receipt plans (ticked) and stated warranties (unticked), and a full Add attaches only the ticked ones. The empty-Save message shows. The quick-add note sentence is complete. A stated-only receipt quick-adds with no error.
- The usual-window note shows on Unconfirmed policies and on the saved item, but not on Confirmed policies. The store field shows the '"X" is not selected yet' hint.
- Soft-closed return windows: badge, wording, hidden actions, the confirmation with Cancel, and items that shouldn't change are unchanged. The wizard's courtesy ask links to it.
- The wizard keeps its answers and ticks across a reload. The courtesy ask no longer says the window "has passed" on an item with no window.
- The Home Recovered card shows on the first load, with no session drop.
- Receipt plans attach to the item they were read for (Geek Squad, Allstate, Lowe's), never the first item by default.

## Still failing or partial (needs dev attention)
1. **B-13:** after a courtesy-return override, Refund and Mark returned come back but "Start a return" does not.
2. **A-17:** a stated receipt warranty (pellet stove, "10 YR LIMITED WARRANTY") is saved labelled "Manufacturer warranty", not "Stated on receipt".
3. **A-20 / new:** deleting an item leaves its receipt document behind. A re-upload is refused as "already added to My Items", and the export still includes the file. Because of this, the stated-warranty tick on the generator couldn't be retested.
4. **A-8:** plan rows don't show SKU match text or a keep tick on the New Items row (same as pass 2).
5. **A-14:** the Lowe's plan shows no company, and there is no "not in our list" note (same).
6. **A-12:** the HDMI cable can't be added when its only return windows have ended (nothing to tick) (same).
7. **A-5:** "N lines past the limit" note not captured, so the FS-40-12 count match is unverified. 12-line upload >30 s.
8. **A-15 Not run:** no receipt produced an unmatched plan, so "check this is for the item above" is untested.
9. **C-3:** no "Step 3 of 3" label on the results. **C-7:** card purchase protection doesn't apply to "stopped working", so there's no card route (likely correct; wording fixed).
10. **D-9:** money-recovered validation uses the generic "One or more validation errors occurred."

## New minor findings
- Unticking a plan on Add Details doesn't persist after a reload (it comes back ticked).
- An item page opened from the list after a test-clock advance shows stale data until a full reload.
- The money-recovered modal stays open after a failed save, and its backdrop blocks the account menu until a reload.
- The Recovered card reads "$50.00on 1 item" (missing space). The Rec One refund note isn't shown on the item page.
- The run-reminders summary always reports Sent=0, even when an email went out.
- The unsubscribe page lists the To-do reminders group as "Purchases".
- The reader briefly showed "Store unknown ... Missing: item, store, date, total" on back-to-back uploads before resolving. Reads take 16-21 s.

## Not reported (known or decided by Steve)
Order total shown as the price on headphones and dishwasher; "Tick at least one policy" on empty Save; plan valid on its last day; sign-up timing.

---
# Chunk A - build 7ceedd8 (Staging) - Nov 3 2026, 8:25-8:41 AM ET
Commit: 7ceedd8 (startedAt 12:14Z). 29 steps: 21 Pass, 7 Partial, 0 Fail, 1 Not run.

| Step | Result | Evidence | vs previous |
|---|---|---|---|
| A-1 | Pass | Profile time zone shows America/New_York | Fixed (was "Not set (UTC)") |
| A-2 | Pass | Settings > Notifications lists "To-do reminders" separate from "Info needed", Email/In-app, At once / daily digest | Fixed |
| A-3 | Pass | Alice bell "Notifications, 1 to do" matches /notifications card notice | Fixed |
| A-4 | Pass | Bob bell "1 to do" matches /notifications | Fixed |
| A-5 | Partial | Pine Street 12 lines: 4 main + "Smaller things (8)"; the "N lines past the limit" note was not captured, so FS-40-12 count match unverified; upload >30 s | Same / unverified |
| A-6 | Pass | All rows dismissed, "Nothing waiting." | n/a |
| A-7 | Partial | Headphones row "Includes: Geek Squad Protection - 2-Year Plan, $49.99 · 24 months" on that item, not a second item; $421.98 order total (known) | Same |
| A-8 | Partial | Row shows plan name/company/price/term but no SKU 6505727 match text and no keep tick on the row | Same |
| A-9 | Pass | Add Details: plan ticked, Sony stated warranty unticked "Not added. Tick it to add it"; ended return window disabled with reason | Fixed |
| A-10 | Pass | Empty Save: "Tick at least one policy to add it" banner (decided/expected) | Fixed |
| A-11 | Pass | Full Add attaches Geek Squad plan Oct 6 2026-Oct 6 2028 "Covers SKU 6505727"; Sony warranty not attached | Fixed |
| A-12 | Partial | TV row has Geek Squad 4YR $299.99 on the TV only; cable has no plan but could not be added (only ended return windows, nothing tickable) | Same |
| A-13 | Pass | Target kettle/coffee maker: no plan or stated warranty invented | Same |
| A-14 | Partial | Allstate on Walmart TV, Lowe's plan on dishwasher, each on its own item; Lowe's plan shows no company; no "not in our list" note | Same |
| A-15 | Not run | No unmatched plan produced "check this is for the item above" | Same |
| A-16 | Pass | Mini-Split multiple terms: "none is set. See the text and add the ones that apply." only on that item | Same |
| A-17 | Partial | Pellet stove 10-yr warranty attached via full Add but labelled "Manufacturer warranty" with "Receipt says: 10 YR LIMITED WARRANTY", not "Stated on receipt"; brand box blank in form though Emberly saved | Changed |
| A-18 | Pass | Quick-add note complete: "Not added by a quick add: we are not sure enough it applies. Tick it on Add Details to keep it." | Fixed |
| A-19 | Pass | Generator quick add creates item without warranty, no validation error ("Needs info") | Fixed |
| A-20 | Partial | Could not retest ticking the stated warranty: re-upload refused "already added to My Items" even after deleting the item (receipt file remains, still in export); Add a purchase upload offered no stated warranty | Changed (blocked) |
| A-21 | Pass | Tire road-hazard stated warranty has its own unticked checkbox and is not attached unless ticked | Fixed |
| A-22 | Pass | New Balance Unconfirmed policy shows "Usual window, can differ for your item. Check your receipt." + Source link (new tab, noopener) | Same |
| A-23 | Pass | Saved item shows the note and Source link | Fixed |
| A-24 | Pass | Best Buy Confirmed general 15 days: no Usual-window note | Fixed |
| A-25 | Pass | '"New Bal" is not selected yet. Pick a name from the list, or add "New Bal" as new.' with add button | Fixed |
| A-26 | Pass | PDF View: 200 application/pdf, opens | Fixed (was HTTP 500) |
| A-27 | Pass | Export: Download (67 KB), 200 zip, 14 data files + 7 receipts | Fixed |
| A-28 | Pass | Saving Time of day keeps America/New_York | Fixed |
| A-29 | Pass | Signed out | n/a |

## New findings / odd items
1. Deleting an item leaves its receipt document behind: re-upload says "already added to My Items" and the export still includes the file (A-20).
2. Unticking the plan on Add Details does not persist across a reload (it comes back ticked).
3. Pellet stove stated warranty labelled "Manufacturer warranty" rather than "Stated on receipt" (A-17).
4. Dishwasher receipt briefly showed "Store unknown ... Missing: item, store, date, total" during back-to-back uploads, then resolved.
5. Receipt reads 16-21 s; 12-line receipt over 30 s.
Tester note: A-17 "not sure of exact date" ticked by mistake (item shows Oct 2026 approximate); not a finding.

---
# Chunk B - build 7ceedd8 (Staging) - Nov 3 2026, ~8:43-9:00 AM ET
Commit: 7ceedd8 (startedAt 12:14Z). 20 steps: 19 Pass, 1 Partial, 0 Fail, 0 Not run.
Clock reset to offset 0 at end (B-19). Info needed delivery itself not run (no trigger staged); only its setting checked.

| Step | Result | Evidence | vs previous |
|---|---|---|---|
| B-1 | Pass | 3 items; Clock Shoes "Next to end: Return window, Dec 3, 2026 · 30 days left"; Reminder Blender 15 days left; No Window Item "Needs info" | Same |
| B-2 | Pass | To-do "UAT todo remind" Due in 1 day; Info needed Email/In-app off, To-do reminders on, persisted after reload | Fixed (own type) |
| B-3 | Pass | +1 day; run-reminders Todos=1; second run Todos=0 (once only) | Fixed |
| B-4 | Pass | Email: subject "To do today: UAT todo remind (UAT Reminder Blender)", from StuffIt <noreply@stuff.microsaasbuilders.com>, 8:45 AM ET, Updates tab; body "UAT todo remind is due today, on November 4, 2026. It is about UAT Reminder Blender." Exactly one. Bell: "To do today: UAT todo remind (UAT Reminder Blender) ..." stamped Nov 4 8:45 AM | Fixed (email and bell name the item; "today" on the due date, not a day ahead) |
| B-5 | Pass | Unsubscribe page is client-rendered; its API (GET /api/unsubscribe/{token}, 200) returns messageType todo_reminder, messageLabel "To-do reminders", category "Purchases", emailOn true. No POST made | Fixed (was "Info needed") |
| B-6 | Pass | Info needed on, To-do reminders Email/In-app off, persisted; "UAT todo two" due Nov 6 added | New |
| B-7 | Pass | +1 day, run-reminders Todos=1; no email mentioning "UAT todo two" (inbox, spam, trash searched); no bell entry | New |
| B-8 | Pass | All four toggles back on | n/a |
| B-9 | Pass | "Return in progress since Nov 5, 2026. It is on your returns list until you mark it returned." (simulated date) | Fixed (spacing) |
| B-10 | Pass | +29 days, offset 31; Clock Shoes and Blender "Expired / All coverage has ended" | Same |
| B-11 | Pass | "Return window closed" badge; "The return window ended on Dec 3, 2026. A store may still accept a courtesy return, but it is a request, not a right."; Edit, Mark disposed, Start a refund or claim, Ask for a courtesy return anyway; Refund/Mark returned/Start a return hidden | Fixed |
| B-12 | Pass | Dialog "Ask for a courtesy return? ... nothing is sent to the store."; Cancel keeps actions hidden | Fixed |
| B-13 | Partial | After confirm: "Courtesy return - The return window has closed. Returning this depends on the store agreeing." Refund and Mark returned back, but **Start a return did not reappear** | Changed |
| B-14 | Pass | Reload keeps override; new tab resets (lasts the visit, as decided) | n/a |
| B-15 | Pass | No Window Item unchanged: Refund, Mark returned, Mark disposed, no badge | New |
| B-16 | Pass | Open-window item normal, Start a return present, no badge | New |
| B-17 | Pass | Return-in-progress item keeps Mark returned / Cancel return, no badge | New |
| B-18 | Pass | Wizard: "Ask New Balance whether it will make a courtesy return ... A request, not a right" with "Ask for a courtesy return anyway" link to item ?courtesy=1, same dialog | Fixed |
| B-19 | Pass | Clock reset, offset 0; Alice Time of day cleared | Same |
| B-20 | Pass | At offset 0 Clock Shoes back to 30 days left, no closed badge | n/a |

## New findings / odd items
1. "Start a return" does not come back after the courtesy-return override (B-13); Refund and Mark returned do.
2. Item page opened from the list after a clock advance showed stale data (28 days left, return actions) until a full reload.
3. run-reminders summary shows Sent=0 even when Todos=1, so it cannot show which emails went out (B-3, B-7).
4. Tester set Alice's Time of day to 01:00 so reminders would fire before 9:00 real time; cleared at the end.
5. Unsubscribe info also reports category "Purchases" for To-do reminders (label is correct); FYI only.

---
# Chunks C and D - build 7ceedd8 (Staging) - Nov 3 2026, 8:51-8:55 AM ET
Chunk C: 10 steps, 8 Pass, 2 Partial. Chunk D: 10 steps, 9 Pass, 1 Partial.

## Chunk C - claim wizard (Alice)
| Step | Result | Evidence | vs previous |
|---|---|---|---|
| C-1 | Pass | "Step 1 of 3", 7 reasons, Next disabled until chosen | Same |
| C-2 | Pass | "Step 2 of 3", use / serial number / receipt questions | Same |
| C-3 | Partial | Results page has no "Step 3 of 3" label | Same |
| C-4 | Pass | Best Buy return 15 days left (Nov 18) best option; Cuisinart warranty 365 days left; general guidance routes | Same |
| C-5 | Pass | Reload on results keeps reason, answers and both ticked steps | Fixed |
| C-6 | Pass | Change my answers -> Step 2; changed answer survives reload | Fixed |
| C-7 | Partial | Card item: courtesy ask now says "even though no return window is on file for it" (no "has passed"); card purchase protection "Does not apply" for stopped working, so no applicable card route | Changed (wording fixed) |
| C-8 | Pass | Ended item: warranty "ended on Sep 15, 2026"; goodwill and courtesy asks, neither says the window "has passed" | Fixed |
| C-9 | Pass | Blender keeps Refund and Start a refund or claim | n/a |
| C-10 | Pass | Data left in place | n/a |

## Chunk D - recovered money (Bob, Alice)
| Step | Result | Evidence | vs previous |
|---|---|---|---|
| D-1 | Pass | Bob Home prompt "Got money back on something?..." no Alice data | Same |
| D-2 | Pass | Mark refunded $50 -> Returned; Home Recovered card on first load; no session drop | Fixed |
| D-3 | Pass | "$50.00 on 1 item / $50.00 in cash" | n/a |
| D-4 | Pass | Rec One Returned, Refund $120.00 | Same |
| D-5 | Pass | Rec Three $45 card payout, stays Needs info | Same |
| D-6 | Pass | Alice Home "$165.00 on 2 items" | Same |
| D-7 | Pass | Export 202 then download 200 zip, 14 data files | Fixed |
| D-8 | Pass | recoveries.csv 2 rows (StoreRefund 120.00, CardReimbursement 45.00), no Bob row | Fixed |
| D-9 | Partial | Future date refused with generic "One or more validation errors occurred."; negative/empty amount disables Save with the same generic text | Same |
| D-10 | Pass | Signed out | n/a |

## Odd items
1. Results label missing "Step 3 of 3" (C-3, unchanged).
2. Money-recovered modal stays open after a failed save, and its backdrop blocks the account menu until reload.
3. Rec One refund note "UAT refund" not shown on the item page (it is in the export).
4. Missing spacing "$50.00on 1 item" on the Recovered card.
5. Staged item ids from DB Stager returned "Not found" via direct URL (opened from the list instead) - staging note, not an app finding.
