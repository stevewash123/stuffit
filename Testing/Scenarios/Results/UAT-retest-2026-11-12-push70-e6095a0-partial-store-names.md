# UAT retest: push 70 (API e6095a0), a partial store name no longer matches on its own

- **Build:** API `e6095a0`, started 6:10 AM ET Nov 12 2026. The UI is unchanged since 11:00 PM ET Nov 11.
- **Run:** 6:31 to 6:36 AM ET, as Alice. The app clock was not moved and is at offset 0.
- **Scope:** CHANGES-push-70-partial-store-names.md, rows 1 to 3.
- **How I checked:** I uploaded each receipt with "Upload a receipt or warranty", opened "Add as a new item", recorded the form and cancelled. I read the match log read-only in Neon (`match_decisions`, `parties`) instead of calling the Ops summary, since the summary reads the same rows.

## Summary: 3 Pass, 0 Fail

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Longer printed names still match the same store | **Pass** | **A** "THE HOME DEPOT #0999" became store "Home Depot" (log: key, high, 1.0), with the same Milwaukee lines as pushes 66 and 67. **B** "WALMART SUPERCENTER" became "Walmart" (alias, high, 0.95), with the Walmart electronics and general return policies. **C** "Lowe's Home Improvement" became "Lowe's" (alias, high, 0.95), with the Lowe's return policy at 90 days, Confirmed. **D** "SAMS CLUB #6452" became "Sam's Club" (logged input "Sams Club"; key, high, 1.0), with the Sam's Club electronics return policy. Shots `p70-01-A.png` to `p70-04-D.png`. |
| 2 | "Target Practice Supplies" is not taken as Target | **Pass** | **E** (an archery shop receipt) left the store field empty, showing the placeholder "Best Buy, Amazon…". Coverage read "Nothing found yet. Pick the store, brand, category and card to see what applies." No store named Target Practice Supplies was created; the only Target in `parties` is the shared one from Oct 1. In the store picker, typing "Target" offers the existing Target, and typing "Target Practice" offers `Add "Target Practice"`. Shots `p70-05-E.png` and `p70-06-E-picker.png`. |
| 3 | The match log shows a `candidate` rule for such names | **Pass** | The log row for "Target Practice Supplies" is store / **candidate** / middle, score 0.6, with no final choice. As the notes say, no question is asked of the person yet (that's S2.8.4). |

## Notes (outside this push)
- **Low:** for receipt E the log also has a *store* row with input "Bushnell" (none, low). The brand name seems to be tried as a store too.
- **Info:** uploads B and E each created a private party in Alice's account by themselves: "Allstate" as a warranty provider at 6:32 AM ET and "Bushnell" as a manufacturer at 6:34 AM ET. These are brand and plan-provider parties, not stores, so they don't break row 2. The brand "Bushnell" was logged twice, first as none/low and then as key/high once it existed.
- **Info:** cancelling the "Add as a new item" form leaves the suggestion in the New Items inbox. All 7 suggestions were dismissed by hand and are now under Dismissed.
- None of the store fields showed a Shared or Verified badge on this form.

## Cleanup
Nothing was saved, and My Items is empty. The suggestions are dismissed. The private Allstate and Bushnell parties are still in Alice's account. Alice is signed out.

## Fixtures (new, on the share in `Testing\SampleData\push70-store-names\`)
- `p70-receipt-lowes-home-improvement.pdf` (prints "Lowe's Home Improvement", DeWalt drill)
- `p70-receipt-sams-club-6452.pdf` (prints "SAMS CLUB #6452", Samsung TV)
- `p70-receipt-target-practice-supplies.pdf` (prints "Target Practice Supplies", a Bushnell rangefinder, for the partial-name case)

I also used the existing `homedepot-receipt-01.pdf` and `30-thermal-walmart-vizio-tv-protection.pdf`.
