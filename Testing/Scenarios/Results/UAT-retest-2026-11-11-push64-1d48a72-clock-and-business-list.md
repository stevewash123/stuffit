# UAT retest: Push 64, the app clock everywhere and a business's whole list (Nov 11, 2026)

- **Build:** API `1d48a72`, started 2:08 PM ET (19:08:23 UTC). UI redeployed 2:07 PM ET. Staging. API and UI, no migration (per the notes).
- **Source:** `CHANGES-push-64-clock-and-business-list.md` (Bot Rules, written 2:06 PM ET). Notes: `/workspace/uat/push64/p64-notes.md`. Screenshots: `p64-01` to `p64-11` in `/workspace/uat/push64/shots/`.
- **Accounts:** Alice personal (QA Test 1), Bob personal, S71 owner (`+s71owner`, UAT S71 Pine Rivet Repairs) and S71 employee (`+s71emp`). New-version banner was taken and the page reloaded before testing.
- **Clock:** started at Offset 0, moved +8, +1, +111 (Offset 120), then reset. **Final Offset 0** (confirmed 3:00 PM ET).
- **Fixtures:** QA made no new fixtures.
- **Not reported:** the notes' "Not built yet" list (Money recovered joins, claim wizard on denial, phone-insurance cost view, three-layer explanation, own plan type, receipt-to-plan-type matching, seeded provider list).

## Results

| Result | Count |
|---|---|
| Pass | 3 |
| Partial | 0 |
| Fail | 0 |

Plus one correction to the Scenarios 70–74 report (S73 halfway lease email), below.

| # | Check | Result |
|---|---|---|
| S72-9 | After a clock move, an open page counts from the new day without a reload; day after the last day says the window ended, hides return actions, offers a courtesy return | **Pass** |
| S70-7 | At +120 days, a purchase dated before the app date is accepted; a later date is refused | **Pass** |
| S71-5b | A business employee sees all the shop's items by default; unticking shows only their own; personal accounts unchanged | **Pass** |

## S72-9: the page follows the app clock. Pass

The Scenario 72 Instant Pot was gone (deleted in 72 cleanup), so Alice added **UAT P64 Return Test** (Amazon, Oct 20, 2026, $89.99, Small appliances). The Amazon 30-day return policy came in from the confirmed shared policy, ticked by default.

- **Offset 0:** "Next to end: Return window, Nov 19, 2026 · 8 days left", Start a return shown.
- **Offset 8** (app 2026-11-19), no reload, navigated My Items then the item: badge "Ends today", "Next to end: Return window, Nov 19, 2026 · Ends today"; Refund, Mark returned and Start a return shown. Correct for the last day.
- **Offset 9** (app 2026-11-20), no reload, navigated the same way: badge **Expired**, and

  > Return window closed
  > The return window ended on Nov 19, 2026. A store may still accept a courtesy return, but it is a request, not a right.
  > [Ask for a courtesy return anyway]

  Header actions are only Edit and Mark disposed (Refund, Mark returned, Start a return are gone). Policies: "Coverage ended 1 policy". No "Ends today" anywhere.
- **Courtesy dialog:** "Ask for a courtesy return? The return window has ended. A store does not have to take it back, and it may say no. This only shows the return actions again; nothing is sent to the store. [Cancel] [Show the return actions]". QA pressed Cancel.
- A hard reload afterwards showed the same page.

**Low (question for CC):** a "Start a refund or claim" link is still at the bottom of the closed-window item. That may be intended for warranty claims; noting it in case it should be hidden with the return path.

## S70-7: add-purchase date uses the app date. Pass

At Offset 120 (app 2027-03-11), no reload, New Items then Add a purchase. The date field defaulted to **2027-03-11** (the app date). **UAT P64 Date Test**, store UAT Harborline Electronics (existing), date **2027-03-06**, $10.00, saved with no error. The item shows "Bought Mar 6, 2027 from UAT Harborline Electronics".

Negative control: **2027-03-20** (after the app date) was refused with "Enter the date you bought it (not in the future)." under the date field. Nothing saved.

**Low:** the refusal also shows the generic page banner "One or more validation errors occurred." above the field message. It's the same generic text as the duplicate-tag refusal in Scenario 71.

## S71-5b: a business's My Items shows everyone's items. Pass

- The owner added **UAT P64 Owner Drill**, and the employee (in the business) added **UAT P64 Employee Ladder** and did not follow the drill.
- **Employee My Items:** both items listed. "Show everyone's items" is ticked by default. It sits inside the **Filter and sort** panel, not on the page itself.
- **Unticked:** URL `/items?mine=true`, only the Ladder, filter badge 1. Re-ticked shows both again.
- **Employee Personal:** "Nothing here yet", no Filter button, so no box.
- **Bob Personal:** his usual items; Filter and sort has no "Show everyone's items".
- Cleanup: both items deleted; the business list is empty again.

**Lows (seen again, already reported):** the owner's own item still says "Entered by: Team member"; after switching, the account select still reads "Personal" while the business is active.

## Correction to Scenarios 70–74: S73 halfway lease email did arrive

The 70–74 report said the halfway lease mileage notice was in-app only. That was a QA miss. Read-only Neon check: the `notifications` row "UAT S73 Honda CR-V lease: halfway through a lease year" (type `lease_mileage_check`) has `email_status` **Sent**. Alice's Gmail has it, received 11:22 AM ET Nov 11, subject "QA Test 1: UAT S73 Honda CR-V lease: halfway through a lease year". Gmail filed it under the **Promotions** tab, which is why QA missed it. The three-months-left email landed in Updates.

Please treat S73 "halfway notice not emailed" as **Pass**. **Low observation:** Gmail sorts the halfway mail into Promotions.

## Data left behind

None from this retest; all four P64 items were deleted. Throwaway logins `+s71owner` and `+s71emp` remain.
