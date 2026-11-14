# UAT retest: Push 102, sharing on by default (fix for the Push 101 Medium)

- **Notes:** CHANGES-push-102-sharing-on-by-default-fix.md (written 6:58 PM ET)
- **Build tested:** API `6406362` (from /api/version, started 7:39 PM ET / 00:39:40 UTC Nov 14). UI Last-Modified Sat, 14 Nov 2026 00:38:24 UTC (7:38 PM ET).
- **Migration:** `20261113234614_AccountSharingOnByDefault` is applied (checked with read-only SQL).
- **Run:** Fri Nov 13 2026, 7:59 to 8:15 PM ET, in the box browser with real mouse and keyboard input, after a hard reload. No new-version banner appeared.
- **Accounts:** Alice (QA Test 1 and P34-Alice Repairs), Bob (QA Test 2), Ops (database check only), and a new account, P102 Tester (stevewash123.tester2+p102a@gmail.com).

## Summary
4 Pass, 0 Fail, 3 Not tested, 2 Info. The Push 101 Medium (sharing was off by default) and the Push 101 Low (the Terms link opened at the top) are both fixed.

| # | Check | Result |
|---|-------|--------|
| 1 | Existing accounts have sharing on | Pass |
| 2 | A new account has sharing on | Pass |
| 3 | Untick and retick persist across a hard reload | Pass |
| 4 | "Read exactly what is shared" opens at the right section; Terms from sign-up open at the top | Pass |
| 5a | Ops re-accept screen (left over from Push 101) | Not tested |
| 5b | Employee gets a 403 on `PUT /api/privacy/sharing` | Not tested |
| 5c | Ops > Claims ignores an opted-out account | Not tested |

## Details
1. **Existing accounts: Pass.** Without touching anything, the "Share the policy facts from what I add" box was ticked in Alice's P34-Alice Repairs account (02), in Alice's Personal account (03) and in Bob's Personal account (15).
   - Read-only SQL: the `accounts.share_with_community` column default is `true`, and all 15 rows are true with none false. That includes QA Test 1, P34-Alice Repairs, QA Test 2 and QA Test 4 (Ops).
   - No terms re-accept screen appeared for Alice or Bob, as expected.
2. **New account: Pass.**
   - The sign-up form reached "Check your email" (12).
   - The confirmation email arrived in tester2 Gmail **Spam** again, and its link points at dev.warrantycat.com. I opened the same path on stuffit-ui.onrender.com. It landed on /orientation signed in as P102 Tester.
   - On first view the box was ticked (14), and the database row is true (created 8:09:26 PM ET, email confirmed).
3. **Untick and retick: Pass.**
   - Unticking showed "Sharing is off. Nothing more of what you add will be shared, and anything we had not yet checked has been taken back." The box stayed off after a hard reload (04, 05).
   - Ticking again showed "Sharing is on." The box stayed on after a hard reload (06, 07). It was left ticked.
4. **Terms positioning: Pass.**
   - "Read exactly what is shared" opens the Terms window with "What is shared and what never is" at the top of the visible text (08).
   - The Terms opened from /signup still start at "What WarrantyCat is" (11).
5. **Push 101 leftovers: Not tested.**
   - Ops wasn't signed in this run. Push 102 has no new terms version.
   - The employee 403 needs a raw API call with Bob's session, which QA doesn't do.
   - I skipped the optional Claims effect.

## Info
- **The account switcher label lags behind the real account** (13, 09, 15). This was also seen in Push 101.
  - When Alice first switched to Personal, the switcher still showed P34-Alice Repairs. Picking Personal again fixed it. After she ticked sharing back on, the label flipped from Personal to P34-Alice Repairs.
  - For Bob, the switcher said "Personal" while the header showed "Alice ..." and the Privacy page showed the business data: 7 files, 15 KB, and no sharing card (09). That made it look as if Bob's personal account had no sharing card.
  - Only after switching to the business and back, then a hard reload, did Bob's real Personal page appear: 29 files, 414 KB, with the card ticked (15).
  - This could mislead a user about which account they are changing.
- **The sign-up confirmation email lands in Spam and links to dev.warrantycat.com**, the same as in Push 99.

## Fixtures and leftovers
- No files were created.
- The new test account P102 Tester (stevewash123.tester2+p102a@gmail.com) is empty.
- Every account has sharing on.

## For CC
- Make the account switcher's selected value follow the active account after a switch and after a settings save.
- If a check of the employee 403 is wanted, an API test would cover it better than the browser.

Screenshots are in /workspace/uat/push102/shots/: 01 to 13 as PNG, 14 and 15 as WebP.
