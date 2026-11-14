# UAT retest: Push 97, the "Cancel this plan" sheet is its own component

- **Build tested:** API `bde7439`; UI Last-Modified **Fri, 13 Nov 2026 17:44:43 UTC (12:44 PM ET)**, confirmed before and after the run. A hard reload was done first, and no new-version banner appeared.
- **Scope:** `CHANGES-push-97-plan-cancel-sheet-split.md` (S9.10.12 step 1, regression only). There were no new scenarios and no NEXT-REPORT-ADDITIONS.md.
- **Tester / account:** QA Controller, box browser, Alice ("P34-Alice Repairs"), 1:06–1:10 PM ET on Nov 13 2026. Button states were read from the real disabled property.
- **Test data:** item "P97 UAT Item" (Walmart/Vizio fixture `push85/30-thermal-walmart-vizio-tv-protection.pdf`, Electronics), with an Allstate warranty extension typed in. That plan was `01a1d618-5467-74cc-afc7-82f921e26cb4`: paid "a year", Aug 29, 2026 to Aug 28, 2028, contract P97-CONTRACT, phone 800-555-0197, and the Allstate website. Everything was deleted afterwards, and no new fixtures were made.

## Results

| # | Check | Result |
|---|---|---|
| 1 | Sheet choices; "It already ended or I cancelled it" focuses "It ended on" | **Pass** |
| 2 | Terms step: what we hold, Copy, links, Cancelled on with before-start error, how cancelled, Back | **Pass** |
| 3 | Confirm shows "Cancelled <date>." with Undo; Undo gives "Cancellation undone." | **Pass** (cancel part) |
| 3b | Stop it renewing: "Done. It ends <date> and will not renew." | **Not tested** (see below) |
| 4 | Record a refund; "Refund recorded."; "I haven't got it yet"; `?refund=1` | **Pass** |
| 5 | Re-open this plan with optional note | **Pass** |
| 6 | Failed cancel/refund messages in the sheet; layout | **Pass** |

**5 Pass, 0 Fail, 1 Not tested, 2 Info.**

### 1. Choices
The sheet is titled "Cancel this plan", with "What do you want to do?" and two options: "Cancel it now" and "It already ended or I cancelled it". There is no "Stop it renewing", which is correct because the plan doesn't auto-renew (shot 02). Picking "It already ended…" closed the sheet and put the cursor in "It ended on"; "End this plan" had `disabled` true (03).

### 2. Terms step
- **What we hold:** "No cancellation terms saved for this plan."
- **Contract:** "Contract P97-CONTRACT". Copy changed to "Copied" and showed the toast "Contract number copied" (05).
- **Links:** "Call 800-555-0197" goes to `tel:800-555-0197`, and "Visit the website" goes to the Allstate site. They're followed by "Check your contract for any cancel-for-refund window."
- **Cancelled on:** defaults to 2026-11-13. With 01/01/2026, submitting showed "The date is before the plan starts. It must be on or after Aug 29, 2026." under the date (06, 07).
- **How did you cancel? (optional):** free text, with the placeholder "Phone call, online, letter…". The buttons are "Cancel it now" and "Back", and Back returned to the choices.

### 3. Confirm and Undo
- The confirmation sheet "Plan updated" showed "Cancelled Nov 13, 2026." with Undo, "Record a refund" and Done (10).
- Undo gave the toast "Cancellation undone.", and the plan was back to "Until Aug 28, 2028" with "Cancel this plan" (09).
- The plan was then cancelled again and left cancelled.

### 3b. Stop it renewing: not tested
The typed-in plan form has no auto-renew option, so a QA-made plan can't offer "Stop it renewing". Every other plan in Alice's /plans was already cancelled. To test this, QA needs a plan set to auto-renew, either staged in the database or created through a route that sets renewal.

### 4. Refund
- **Fields:** Amount, "Date you got it" (defaults to today), and "How it came back (optional)" with the placeholder "Card, cheque…".
- **Amount 0 or -5:** "Save refund" stays enabled, and clicking it shows "Enter an amount greater than zero." in the sheet (11).
- **Valid refund (25, today, Card):** the toast "Refund recorded." appeared, and the header changed to "Cancelled Nov 13, 2026, refunded $25.00 · Change the refund" (14).
- **`/plans/<id>?refund=1`:** opens the refund step straight away (15). "I haven't got it yet" closes it.

### 5. Re-open
The "Changed your mind?" block says "Re-opening puts the plan back as it was.", with "Note (optional)". Entering the note "P97 reopen" and clicking "Re-open this plan" gave the toast "Plan re-opened.", and the plan was back to "Until Aug 28, 2028" (16).

### 6. Errors in the sheet
All of these showed in red inside the sheet:
- Cancel before the start: "The date is before the plan starts. It must be on or after Aug 29, 2026."
- Refund dated 01/01/2026: "The refund cannot be before the cancellation." (12)
- Refund dated 12/31/2026: "That date is in the future." (13)

## Info
- **Info:** opening `?refund=1` on a plan that already has a $25 refund shows a blank Amount, not the saved amount. The header calls this "Change the refund", so prefilling may be expected. Also, after "I haven't got it yet", the URL keeps `?refund=1`.
- **Info:** the top-right toast covers the sheet's header and title while it shows (05).
- Not counted: Alice's /plans holds about 14 cancelled Allstate and Geek Squad plans from earlier QA runs today. They're harmless, but clutter.

## Cleanup
"P97 UAT Item" was deleted with "Cancel the plan too". My Items "P97" shows "No items match." (17).

Screenshots: `/workspace/uat/push97/shots/` (01–17).
