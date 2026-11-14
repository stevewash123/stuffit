# UAT retest: push 77 (UI-only), coverage tooltips in words, no percentages

- **Build:** UI Last-Modified Thu 12 Nov 2026 18:25:32 UTC (1:25:32 PM ET Nov 12 2026); API unchanged at `29c6fda` (started 11:25:54 AM ET).
- **Run:** 2:09 to 2:19 PM ET, as Alice, after a hard reload. App clock not moved (offset 0). Three rounds: existing items plus Add/New Items with nothing saved; then two test items saved and deleted.
- **Scope:** CHANGES-push-77-no-percentages.md (S9.10.4 part one; Bot Rules 1:24 PM ET). NEXT-REPORT-ADDITIONS.md: none.
- **How I checked:** existing item pages; uploads on a blank `/add/new` and in New Items; two test items saved from the Walmart/Vizio fixture and deleted in the app. No DB Stager cleanup.

## Summary: 2 Pass, 0 Fail

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Score-word tooltip in words, no % | **Pass** | Found on the item page's **"Suggested coverage — Tick what applies."** list (Policies card **"Not set up yet · 2 suggested policies to review"** → Review), on a test item **"P77 suggestions test TV"** saved at 2:18 PM with all coverage unticked and deleted at 2:19 PM. Tooltips: Confirmed (Walmart return policy: electronics, pre-ticked, checked Sep 29, 2026) **"Policy checked: very sure. Fit for this purchase: very sure: A store's usual window can differ for an item"** (`p77-401-suggest-confirmed.png`); Likely (Walmart return policy: general, checked Oct 28, 2026) **"Policy checked: very sure. Fit for this purchase: fairly sure: Walmart's window for general items; it applies only if your item is one"** (`p77-402-suggest-likely.png`); Unconfirmed (Vizio warranty) **"Policy checked: not sure. Fit for this purchase: very sure"** (`p77-403-suggest-unconfirmed.png`). No percentages anywhere. Nine existing Alice items, and an item saved with coverage ticked (round 2, **"P77 tooltip test TV"**, 2:16 PM, deleted 2:17 PM), showed no score words, as expected: that list is only for suggestions. Shot `p77-301-item-policies-no-score.png`. |
| 2 | Add a purchase and New Items unchanged | **Pass** | Add form upload B at 2:09 PM: toast **"Filled in from your document: store Walmart, brand Vizio, name Vizio V5, size or variant 50IN, model number V505-J09, item price 328.00, date 2026-08-29, order total 397.74, order number 04417."** Score-chip hover text unchanged: Confirmed **"The policy is checked against an official source and fits your item. It is added when you save."**; Likely **"Probably applies. Tick it to add it."**; Unconfirmed **"We could not check this policy. Tick it only if your paperwork says so."** Shots `p77-11-add-confirmed.png` to `p77-13-add-unconfirmed.png`. Left without saving. New Items upload A made 3 waiting items (Circular Saw, Hammer Drill, Prime stud). Hammer Drill review-form chips used the same sentences; list-card chips **"Checked against the official source on Oct 24, 2026."** / **"Read on the company's own website on Sep 30, 2026."** Shots `p77-21-review-confirmed.png`, `p77-22-review-likely.png`. No percentages anywhere. All three dismissed and deleted for good; Waiting and Dismissed left empty. |

## Notes
- **Low:** the Policies card said "2 suggested policies to review" but the suggestions list showed 3.
- **Low:** the Walmart electronics 30-day suggestion (window ended Sep 28, 2026) appeared already ticked in the suggestions list even though nothing was ticked on save. On the Add form the same line could not be ticked because the window had ended ("This return window ended 2026-09-28, so it cannot be added.").
- **Info:** the Unconfirmed tooltip has no reason part after "very sure".
- **Info:** the Add form and New Items chips still use the older sentences (CC said only the item page changed).
- **Info:** the Add form path showed no Allstate plan line for B (as in push 72). Picking category TVs re-scored the lines (electronics 30-day became disabled Confirmed; general 90-day became Likely).
- **Info:** the Home Depot upload now makes a third waiting item **"Prime stud"** under Smaller things.

## Cleanup
Two test items were saved and deleted in the app (Edit → Delete → "Delete item"). New Items Waiting and Dismissed were empty. No DB Stager cleanup was needed.

## Fixtures
No new fixtures this run. Used `30-thermal-walmart-vizio-tv-protection.pdf` (B) and `homedepot-receipt-01.pdf` (A).
