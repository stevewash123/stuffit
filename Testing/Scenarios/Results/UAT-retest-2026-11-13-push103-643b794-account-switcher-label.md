# UAT retest: Push 103, the account switcher shows the active account

- **Notes:** CHANGES-push-103-account-switcher-label.md (written 8:51:07 PM ET)
- **Build tested:**
  - API `643b794`, read from /api/version. It started at 8:51 PM ET (01:51:31 UTC, Nov 14).
  - UI Last-Modified Sat, 14 Nov 2026 01:51:45 UTC (8:51 PM ET).
- **Run:**
  - Fri Nov 13 2026, 8:53 to 8:58 PM ET.
  - Box browser, with real mouse and keyboard input.
  - A hard reload came first, and no new-version banner appeared.
- **Accounts:**
  - Alice (QA Test 1), who owns P34-Alice Repairs and has a Personal account.
  - Bob (QA Test 2), who has a Personal account and is an employee in P34-Alice Repairs.

## Summary
5 Pass, 0 Fail, 1 Not tested by QA (covered by CC's API tests), 3 Info. The Push 102 Info is fixed. In every state the run reached, the switcher showed the account that was really active, matching both the header and the Privacy page (file count and sharing card).

| # | Check | Result |
|---|-------|--------|
| 1 | Switching business to Personal and back: the switcher, header and Privacy page agree | Pass |
| 2 | A hard reload on each account keeps the switcher on that account | Pass |
| 3 | A fresh sign-in as Bob: the switcher matches the header | Pass |
| 4 | Ticking or unticking sharing doesn't change the switcher | Pass |
| 5 | "(n new)" notices, the account menu and the chooser page are unchanged | Pass |
| - | Employee gets a 403 on `PUT /api/privacy/sharing` | Not tested by QA; the notes say CC's API tests cover it |

## Details
1. **Alice, switching back and forth (shots 01, 02, 03, 07, 09)**
   - Personal showed the switcher on "Personal", no business name in the header, 0 files and the sharing card.
   - The business showed the switcher on "P34-Alice Repairs" (truncated to "P34-Alice Repa…"), the header "P34-Alice …", 7 files (15 KB) and the sharing card. She is the owner.
   - All three switches matched.
2. **Hard reloads (shots 04, 08):** after a hard reload, the switcher still showed the account Alice was in, both in Personal and in the business.
3. **Bob (shots 11 to 16)**
   - His fresh sign-in landed in Personal, with 29 files (414 KB) and the sharing card shown.
   - After switching to the business, the switcher showed "P34-Alice Repa…", with 7 files (15 KB) and no sharing card, which is right for an employee.
   - After switching back and doing a hard reload, he was in Personal and everything matched.
4. **Sharing toggle (shots 05, 06):** I did this on Alice's Personal account. Unticking showed "Sharing is off. …" and ticking showed "Sharing is on." The switcher stayed on "Personal" both times. Sharing was left ticked.
5. **Notices, account menu and chooser page (shot 10)**
   - The account options showed no "(n new)" notice in this run. The bell showed 2 for Alice's Personal and 11 for the business.
   - The account menu lists the usual items.
   - Switch account opens /choose-account ("Where to?"), which lists "P34-Alice Repairs Owner" and "Personal Your own things".

## Info
- **One of Bob's switches back to Personal didn't take (shot 14).**
  - I typed the /settings/privacy address right after picking Personal. The page went blank and then showed the business, with the switcher and header both on the business, so the label still matched the account.
  - A second pick, waiting about 5 seconds for Home to load, worked (shot 15).
  - It looks like my navigation cut the switch off before it finished. I haven't confirmed whether it's a real intermittent bug.
  - If CC wants to be sure: a switch interrupted by a navigation shouldn't leave the app half-switched.
- **The account order differs between users.** Bob's list shows Personal first, while Alice's shows the business first.
- **The business name truncates in the header.** It shows as "P34-Alice …" and overlaps the logo slightly, and the switcher truncates it to "P34-Alice Repa…". This is the same as the earlier logo overlap Info.

## Fixtures
None.

Screenshots are in /workspace/uat/push103/shots/, numbered 01 to 16.
