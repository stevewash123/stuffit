# UAT retest: Push 32 protection plans, plus Push 30 fixes

- **Build:** API `14fa6e8`. I read `/api/version` (200) at 8:38 PM ET and it returned `14fa6e8`, started 7:42 PM ET. The notes give the UI as `bdd617e`; the UI's Last-Modified time was 7:41 PM ET.
- **Clock:** I read the clock read-only with `GET /api/maintenance/clock` for Alice's account. It returned **Offset 0** at 8:38, 8:51 and, for the final check, 9:37 PM ET. At 9:37 PM ET `/api/version` was still `14fa6e8`, started 7:42 PM ET.
- **Accounts:** Alice (Test1) for every step except step 7. Step 7 used Ops, signed in through Steve's 2FA handoff. DB Stager reset Alice at 7:59 PM ET. All fixtures are new and named `P32 …`.
- **Scope:** targeted only, not regression. This covers Push 32 steps 1–8, the Push 30 start-date notice retest, and Push 31 steps that need no clock change and send no email.
- **Nothing changed outside the tests:** no clock moves, no reminder, digest or cleanup jobs or sweeps started by hand, and no other accounts. Normal app actions can still send notification emails on their own. For example, the start-date notice shows email_status Sent. So this report does not claim that no email was sent at all.
- **Evidence:** `push32-batchAB/CD/E/F-findings.md` and `push32-batch*-screenshots/`.
- **Synthetic fixture:** `fixtures/P32-synthetic-test-contract-enrolment-60d-gap-75d.pdf` is titled "SYNTHETIC QA TEST CONTRACT — NOT A REAL POLICY". It is fictional, made by QA to test the reader, and is not a real policy.

## Summary
Ten rows: Push 32 steps 1–8, the Push 30 start-date notice, and Push 31 step 1.
- **Pass: 5.** Push 32 steps 2, 5, 6 and 8, and Push 31 step 1.
- **Partial: 3.** Step 1 (end dates one day apart), step 3 (fixed states pass; the change over time was not run), and step 4 ("counted from" missing).
- **Fail: 2.** Step 7 (link validation not enforced) and the Push 30 start-date notice.

Not part of the ten: **Push 31 steps 2–7 (six steps) are Not run.** They wait on Steve's OK for the clock and emails.

## Push 32 results

| Step | Result | What we saw | Limits of the check |
|---|---|---|---|
| 1 Plan ended today | **Partial** | **First fixture:** `P32 Ended TV` (`01a1b393-…81f2`) has a Geek Squad plan (`01a1b395-…403d`). After **End this plan** with Nov 6, it read **Ended Nov 6, 2026** on the plan page, the item card and the plans list. Home's 30- and 60-day counts and "Next to end" left it out. The item header said "Expiring soon" because an automatic Best Buy return window was still open. **Clean recheck:** `P32 Ended Clean` (`01a1b3ad-9526-7455-b862-8a596b3ac11b`) has no maker warranty and no return window. Its one Allstate plan (`01a1b3ae-ec33-7a8c-9cb0-cc5e30e11342`) runs Nov 6, 2025 to an explicit end of Nov 6, 2026 and was ended with the Nov 6 action. The item badge then showed **Expired**, not Expiring soon; Policies showed "Coverage ended"; the plan card showed Ended. The header question is settled. | **The dates still don't match on both fixtures.** The plan page shows "… to Nov 6, 2026", but the item card shows "… to Nov 5, 2026". Also, a 12-month term entered from Nov 6, 2025 first worked out its end as Nov 5, 2026. |
| 2 Start question and Not yet started | **Pass** | On `P32 TV Future` the start question appeared with nothing selected. With Another date set to Dec 1, 2026 and 12 months, it showed "Not yet started", "Starts Dec 1, 2026 to Nov 30, 2027". The item read "Not covered yet". Home showed "0 running, 1 not yet started". | The check that a multi-item plan keeps the plain date field was not run. |
| 3 Waiting period | **Partial** (fixed states Pass) | **Washer:** start Dec 1 with a 30-day wait reads "Not yet started · covered from Dec 31, 2026". **Dryer** (historical fixture): start Oct 6 with a 30-day wait reads "Covered from Nov 5, 2026", item Active. | The "Waiting period until" state was not seen on a started plan. The change over time from waiting to covered was **not run** because it needs a clock move. The Dryer is a historical fixture and doesn't prove that change. |
| 4 Plan bought after the purchase, with an enrolment window | **Partial** | Used the **synthetic** contract on an item bought Aug 1, 2026. The reader picked up the effective date, order date and enrolment clause. The page said "dated after the purchase … starts Oct 15, 2026". The form start was Oct 15, not Aug 1, and Ends was Oct 15, 2027. The window note did not block saving and read: "Your plan says "within 60 days of purchase of the covered item"; your dates are 75 days apart. Check the contract." | **"counted from" is missing** on the saved plan, the item and the edit form. The only "Counted from" text is the waiting-period hint. The note quotes the contract clause rather than the paraphrase in the change notes. The reader didn't pick up Company, so `P32 Test Protection` was added and shows as UNVERIFIED. This is reader behaviour on a fictional file only. |
| 5 Front door and wording | **Pass** | The menu says "Protection plans". The empty state showed four link routes (`/add`, `/items`, `/plans/new`, `/cards`). "What is the difference?" separates a bought plan from a "Card extended warranty". `/extended-warranties` goes to `/plans`. Searching "extended warranty" works on both the plans page and My Items. | The "Plan ending soon" and "Has a protection plan" filters were not run. Plans with "needing details" were not checked specifically. |
| 6 Claim wizard order and Card wording | **Pass** | On `P32 Routes`, where the maker warranty and the plan have equal dates, the wizard listed the Samsung maker warranty first and the Allstate plan second. The plan card shows "Backup". There was no "closes soonest" wording. A **synthetic** Card extended warranty benefit was then added for Nov 6, 2026 to Nov 6, 2027, with no card or account data entered. The item names it "Card extended warranty". The bought plan stays "Protection plan · Allstate…" with "Warranty extension". The wizard showed maker, plan and card as three separate routes. | The card benefit is QA-only, not a real card benefit. No claim was submitted. |
| 7 Admin company links | **Fail** | Signed in as Ops. On Best Buy (shared company, `01a0f4e4-458d-720b-88fb-277b1120c7bd`), the "Claims or support page" field accepted `http://www.bestbuy.com/returns` and then, separately, the off-site `https://www.example.com/returns`. Neither showed a validation message. Each was set back to the original blank. After a reload, the name, website, phone and roles all match the original. | The dialog has no separate Returns URL field. There is no screenshot of the second accepted value; it was seen in the page's accessibility snapshot. Screenshots show the original and restored states. |
| 8 Private-sale wording | **Pass** | `P32 Private Sale TV`: "Ask the seller whether they will make a courtesy return…". It does not say "Ask Private sale". | — |
| Add-on protection card | **Pass** (fields) | The card shows company, plan, status, dates, what it adds, fee, phone, site, contract number with Copy ("Contract number copied"), and the plan link. | Claim phone numbers and sites are synthetic and were not followed. There was no receipt-line or confidence test. |

## Push 30 start-date notice retest — **Fail (reproduced)**
- Fixture: `P32 Sub-Zero Start Date Fridge` (`01a1b3a2-af3d-705c-87f9-c3565f9750d4`).
- **Notifications was already open before the save.** It showed "Enter the start date of your Sub-Zero warranty" with Needs action, Unread and **Enter the date**.
- I saved Nov 6, 2026 from the item's To do card. The To do changed to Done, and the header changed from "1 unread, 1 to do" to "1 to do".
- **After a fresh reload, the notice and its "Enter the date" button were still there.** The chips had cleared. Clicking the button opened the item with the To do already Done.
- **The notice id is not shown anywhere in the app.**
- **Database evidence (DB Stager, read-only; see `push32-notice-db-evidence.md`):**
  - Notice `01a1b3a2-afc0-7feb-9f34-71205fa04b4f`, type `purchase_needs_info`, reference `todo-start`:
    - action_status **Completed** at 8:33:20.418 PM ET
    - read at the same time
    - acknowledged false, hidden false, not deleted
    - stored action_label "Enter the date"
    - email_status Sent, already set before the inspection
  - To-do `01a1b3a2-af78-7273-a2b9-b91569f7f722` (SetWarrantyStart): **Done** at 8:33:20.405 PM ET.
  - Coverage `01a1b3a2-af6b-…7857` (24 months) and `01a1b3a2-b0e5-…3c99` (144 months) both have start_on 2026-11-06 and start_unknown false.
  - **The server saved the completion, but after a fresh reload the page still shows the button.** The cause is not confirmed. A likely place to look is the page drawing the stored action label without checking action_status.
- The notice was left as it is for follow-up.

## Push 31
| Step | Result | Reason |
|---|---|---|
| 1 Weekly digest setting | **Pass** | In Settings, "Warranty expiring" (the app's label for "Warranty ending soon") was set to In my weekly digest, Friday. "To-do reminders" was also set to weekly and shared Friday. Both stayed after a reload. **Restored and checked:** all five types are back to At once, the weekday is back to Monday, and the setting stayed after a reload. **Build:** tested on the current Push 32 API `14fa6e8`, not Push 31's `529fc86`. A newer build containing the feature is valid; it just means this isn't proof against the exact Push 31 commit. |
| 2–7 | **Not run** | Steps 3, 6 and 7 need Steve's OK for the clock and emails, which hasn't come. Step 5 (urgent notices skip the digest) would send an email at once. Step 4 can only be seen in the digest email. Step 2 depends on the step 1 setting and risks sending email. **Steps 4 and 5 are not passed.** That makes six steps Not run, counted separately from the ten rows. |

## Needs CC
1. **Company link validation is not enforced.** The admin "Claims or support page" field accepts an `http` address and an address on another site, and shows no message (step 7).
2. **The start-date notice button stays after the notice is done.** After a fresh reload, Notifications still shows "Enter the date". In the database, notice `01a1b3a2-afc0-7feb-9f34-71205fa04b4f` is action_status Completed. The cause is not confirmed.
3. **An ended plan's end date is one day off.** The plan page ends Nov 6, but the item card ends Nov 5. A 12-month term from Nov 6, 2025 also works out its end as Nov 5, 2026.
4. **"counted from <start>" is missing** on the saved plan and the item view (step 4). Minor: the enrolment note quotes the contract clause rather than the documented paraphrase.

## Fixtures left in place
- **New P32 items on Alice, with their plans:** P32 TV Future, Washer, Dryer, Test Television (synthetic contract), Ended TV, Ended Clean, Routes, Private Sale TV, and Sub-Zero Start Date Fridge. The Sub-Zero notice was left as it is for follow-up.
- **The synthetic Card extended warranty benefit** on P32 Routes.
- **The automatic "Add the rest" to-dos,** left untouched.
- **Alice's notification settings** are back to the original: all At once, weekday Monday.
- **Best Buy** is back to its original values.

## Not reported (known or not built)
- Known gaps in the Push 32 notes: "what it adds" can't list maker exclusions, the stack line can't give card months, there's no store SKU on the receipt line, and the waiting period is days only.
- Not built: real-time toasts S4.5.7, the pending-consolidation table S4.2.4, and the Error attention level S9.2.11.

Evidence: `push32-batch*-findings.md`, `push32-final-alice-findings.md`, `push32-admin-findings.md`, `push32-notice-db-evidence.md`, and the screenshot folders in /workspace/uat. No Canvas was used.
