# UAT retest: Push 101, sharing switch and terms version 2026-11-13.2

- **Date:** Fri Nov 13, 2026, 6:35 to 6:39 PM ET
- **Build tested:** API `bcbf622` and UI Last-Modified Fri, 13 Nov 2026 23:17:06 UTC (6:17 PM ET)
- **Notes:** `Bot Rules\CHANGES-push-101-sharing-switch.md` (6:05 PM ET). The UI is newer than the notes, so the build matches.
- **Accounts:** Alice (P34-Alice Repairs, then Settings), Bob (personal, then P34-Alice Repairs as employee), signed out (/signup). Ops was not used.
- **Network:** run on the box's own network (Steve's laptop was offline).

## Result: 4 Pass, 2 Fail (1 Medium, 1 Low), 2 Not tested, 4 Info

| # | Check | Result |
|---|---|---|
| 1 | Existing accounts see the terms-updated screen for version 2026-11-13.2; I agree returns to Home | **Pass** (Alice and Bob). Ops was not checked (**Not tested**) |
| 2 | Settings sharing switch: on by default; untick and retick messages; persists across a hard reload | **Fail (Medium)**: existing accounts are off, and the column default is false. Messages and persistence passed |
| 3 | "Read exactly what is shared" opens the Terms window at "What is shared and what never is" | **Fail (Low)**: the window opens at the top ("What WarrantyCat is") |
| 4 | Business owner sees and can use the card; a business employee does not see it | **Pass**. The server 403 for an employee was not probed (**Not tested**) |
| 5 | Optional Ops > Claims effect | **Not tested** |
| 6 | Sign-up sharing-box wording | **Pass**. New-account default was not tested by sign-up; the Postgres column default is false |

## Check 1 detail (re-accept, terms 2026-11-13.2)
- Alice landed on the terms-updated screen. "What changed": "What changed: the Terms say plainly that sharing is on by default and exactly what is and is not shared, and that you can turn sharing off at any time in Settings."
- Terms window header: Version 2026-11-13.2.
- Your choice paragraph: "Your choice. You can turn sharing off at any time in Settings, under Privacy and data. It applies from then on: nothing more you add is shared, and anything we had not yet checked is taken back. Facts we have already checked and added to the shared data stay there, and do not say who added them. To ask us to stop using something that has already been shared, email support@warrantycat.com and we will act on it. [Lawyer to confirm this wording.]"
- "I agree" went to Home in P34-Alice Repairs. Shots 01, 02, 03.
- Bob got the same updated screen again (shot 11) and accepted. Ops was not signed in.
- Read-only SQL afterwards: Alice (QA Test 1) and Bob (QA Test 2) have `terms_version` `2026-11-13.2` (accepted 6:36:54 PM ET and 6:38:08 PM ET). Ops (QA Test 4) is still on `2026-10-01`.

## Fail (Medium): sharing is not on by default for existing accounts
The first view of the Settings card was **unticked** for Alice in P34-Alice Repairs (shot 04) and for Bob's personal account (shot 12). The notes and the terms say sharing is on by default.

Read-only SQL on Neon StuffIt (project `square-tree-53585492`, db `stuffit`), after the browser run:

- Migration `20261113212616_AccountSharing` is applied (product_version 9.0.22).
- Column `accounts.share_with_community`: boolean, `NOT NULL`, `column_default` **false** (`information_schema` and `pg_attrdef`).
- Counts across all 14 accounts: **true 1, false 13, null 0**.
- Alice's personal account ("QA Test 1"), which was not flipped in this run: **false**.
- Alice's business account ("P34-Alice Repairs"): **true**. This is the only true row. It was unticked on first view; she left it ticked after the persistence check below.
- Bob's personal account ("QA Test 2"), left unticked: **false**.
- Ops's personal account ("QA Test 4"): **false**.

This is not a UI misread. Existing rows were not defaulted on, and the column default itself is false, so a new account would also start off unless the app sets the flag on insert (not tested by sign-up). That silently opts users out and contradicts "on by default."

**Messages and persistence (passed), on Alice in P34-Alice Repairs:**
- The card is first on the Privacy and data page. Label: "Share the policy facts from what I add".
- Untick message matches the expected text (shot 06). It stayed unticked after a hard reload (shot 07).
- Retick message: "Sharing is on." She left it ticked (shots 05, 08, 10).

## Fail (Low): "Read exactly what is shared" does not open at that section
Clicking the link opens the Terms window at the top ("What WarrantyCat is"), not at "What is shared and what never is" (shot 09).

## Check 4 detail (owner vs employee)
- Alice, as owner of P34-Alice Repairs, sees the card and can use it (shot 10).
- Bob switched into P34-Alice Repairs: the card is absent; only "How long we keep your files" is shown (shot 13).
- The employee 403 from the server was not probed directly.

## Check 6 detail (sign-up wording)
Signed-out /signup box text (shot 14):

- "WarrantyCat runs on shared knowledge, and sharing is on by default"
- "Shared: the policy facts in what you add: store and brand names, return windows, warranty terms and conditions. Other people see them only after we have checked them, and never see who added them."
- "Never shared: your receipts, photos and documents themselves, what you bought and paid, your credit cards, and your account details. The Terms list exactly what is and is not shared, and you can turn sharing off at any time in Settings."

The new-account default tick was not tested by creating an account. See the column default in the Medium fail above.

## Info
1. Shortly after Alice agreed, opening the account menu sent her to /orientation ("Welcome to WarrantyCat, QA").
2. After Bob switched into P34-Alice Repairs, the switcher dropdown kept showing "Personal" even though the header and data were the business.
3. The first hard reload showed an older terms screen with the previous "what changed" text (a stale tab from the old build). An old tab showed the "new version" banner.
4. Minor: Bob's first vault fill didn't take ("Enter a valid email address."); it worked the second time. The first Sign out click did nothing.

## For CC
- **Default is off, not on (Medium):** `accounts.share_with_community` was added with default `false`, and existing rows are false (13 of 14; the one true is the business account Alice turned on in this run). Backfill existing rows to true, and change the column/app default to true, so it matches the terms and the Settings/sign-up wording.
- **"Read exactly what is shared" (Low):** open or scroll the Terms window to "What is shared and what never is", not the top of the document.
- After agreeing to the new terms, Alice's account menu went to /orientation.
- The account switcher can keep showing "Personal" after a switch into a business (seen before).

## Fixtures and cleanup
None. No accounts or items were created. Alice left sharing ticked on P34-Alice Repairs. Bob's personal account is still off. Ops has not accepted terms 2026-11-13.2.

## Screenshots
In box `/workspace/uat/push101/shots/` (01 to 14):
- 01 alice-terms-updated
- 02 alice-terms-your-choice
- 03 alice-after-agree-home
- 04 alice-privacy-initial-unticked
- 05 alice-ticked-sharing-on
- 06 alice-unticked-sharing-off
- 07 alice-after-hard-reload-unticked
- 08 alice-reticked-sharing-on
- 09 read-what-is-shared-terms-window
- 10 alice-business-owner-card-ticked
- 11 bob-terms-updated
- 12 bob-personal-card-present
- 13 bob-in-alice-business-card-absent
- 14 signup-sharing-box
