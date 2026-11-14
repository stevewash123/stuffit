# UAT retest: Push 93, the "Edit purchase" drawer is its own component

- **Build tested:** API `bde7439`; UI Last-Modified **Fri, 13 Nov 2026 14:41:26 UTC (9:41 AM ET)**, confirmed before and after the run. Hard reload, no new-version banner.
- **Scope:** `CHANGES-push-93-purchase-drawer-split.md` (S9.10.10 step 5, regression only). There were no new scenarios and no NEXT-REPORT-ADDITIONS.md.
- **Tester / account:** QA Controller, box browser, Alice ("P34-Alice Repairs"), 10:02–10:08 AM ET Nov 13 2026. Save's state was read from the real disabled property (Playwright `isDisabled()`).
- **Test items:** "P93 UAT Item" and "P93b UAT Item" (Walmart/Vizio fixture `push85/30-thermal-walmart-vizio-tv-protection.pdf`, Electronics). Both were deleted.
- **Test cards:** Alice has no cards, so "P93 Visa" (BofA Travel Rewards, last 4 1001), "P93 Amex" (Amex Gold, last 4 1002) and PayPal were added on /cards for check 2. All were removed afterwards, and /cards shows "No credit cards yet.". No new fixtures were made.

## Results

| # | Check | Result |
|---|---|---|
| 1 | Pencil opens Edit purchase with the hint, Store, Date (precision), Card, Total, Order, Notes | **Pass** |
| 2 | PayPal: "Which credit card is behind PayPal?" with the bank cards only, warning hint until one is chosen | **Pass** |
| 3 | Save disabled with no date; failed save shows a red message in the drawer; good save updates the purchase card and coverage | **Pass** |
| 4 | Drawer layout unchanged | **Pass** |

**4 Pass, 0 Fail, 2 Info.**

### 1. Opening the drawer
- **Hint:** "Coverage you already confirmed keeps its dates. New suggestions will use these details." (shot 01)
- **Store:** prefilled with Walmart, with a "Clear all ×" button.
- **Date bought:** 2026-08-29, with "I am not sure of the exact date". Ticking it shows "How close the date is", with three options: Only the month / Only the year / Somewhere between two dates. It also shows the help line "Pick any day in the right month. We plan on the start of it."
- **Credit card used:** Not sure / cash plus the account's cards. With test cards it listed P93 Amex, P93 Visa and PayPal.
- **Other fields:** Total paid 397.74, Order number 04417, Notes empty.

### 2. PayPal
- Picking PayPal showed "Which credit card is behind PayPal?". The options were Not sure yet, P93 Amex and P93 Visa, so PayPal itself is not in the list (shot 05).
- **Hint, verbatim:** "PayPal's own receipt doesn't say. The credit card's benefits (card extended warranty, purchase protection) are the ones that apply, so pick it."
  - With "Not sure yet" chosen, it is styled `var(--color-warn)` (orange), and it stays.
  - With P93 Visa chosen, the warning style goes and the same text shows in plain grey (shot 06).
- Switching the main card to P93 Amex removed the PayPal question (shot 07).
- Saving with PayPal backed by P93 Visa updated the purchase card to "Paid with: PayPal" and "Credit card behind PayPal: P93 Visa". It also showed the existing notice "P93 Visa's benefits are not confirmed yet, so we cannot add its warranty or protection to this purchase." with "Review credit card benefits" (shot 08).

### 3. Save and errors
- **Save `disabled`:** false at the start, true with Date bought cleared, and false again after the date was restored.
- **Failed save (Total paid -50):** the drawer stayed open with the red message "One or more validation errors occurred." The same text also showed under the item header buttons (shot 02).
- **Good save:** Total 350, Order P93-ORDER, Notes "P93 note". The drawer closed and the purchase card shows Walmart, Aug 29, 2026, $350.00, Order P93-ORDER, Notes P93 note (shot 03).
- **Coverage after the good save:** unchanged. The same 4 suggestions kept the same dates, and "Your coverage" still says "No coverage confirmed yet."

### 4. Layout
The drawer runs in the usual order: heading, Close, hint, Store, Date, Card, Total, Order, Notes, Save. There was no overlap or broken layout.

## Info (not regressions)
- **Info:** a negative Total paid gives the generic server text "One or more validation errors occurred.", not wording that names the field. This is like the raw RefundAmount message seen in Pushes 90 and 92.
- **Info:** after a backing card is chosen, the PayPal hint keeps its text and only loses the warning colour. The notes say "it goes away", which reads as the warning; please confirm that's the intended behaviour.
- **Not tested:** a future Date bought as a failed save, because the negative total already covered the error path.

## Cleanup
- Both P93 items were deleted. A plain "Delete item" confirmation appeared, with no plan prompt.
- The three test cards were removed.
- A My Items search for "P93" shows "No items match." (shots 04, 09).

Screenshots: `/workspace/uat/push93/shots/` (01–09).
