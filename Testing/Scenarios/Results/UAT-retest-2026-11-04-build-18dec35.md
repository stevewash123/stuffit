# UAT retest: build 18dec35 (push 9), Scenario 51 cancel a plan and record the refund
Date: Nov 4 2026, ~6:40-6:47 AM ET. API 18dec35 (Staging), UI redeployed 6:30 AM ET. Mode: Full-only (browser). Reset: DB Stager --only alice,bob, clock offset 0. Migration PlanCancellation present (DB Stager).

**Totals: 11 Pass, 6 Partial, 1 Fail**

| Step | Grade | Notes |
|---|---|---|
| 1 | Partial | Item-page "Add protection plan" drawer has no "renews automatically" or months field; used full form /plans/new?item=. Saved "Oct 25, 2026 to Oct 25, 2027 · renews automatically", $120.00 a year, Active |
| 2 | Pass | "Cancel this plan" separate from "End this plan" |
| 3 | Pass | Three choices shown |
| 4 | Pass | "No cancellation terms saved for this plan.", contract with Copy, phone, cancel-for-refund line; no entitlement wording |
| 5 | Pass | "Ends Oct 25, 2027 (will not renew)"; to-do "ends on Oct 25, 2027. Renew or replace it." |
| 6 | Pass | $79.00 one payment ($39.47 a year); no Stop it renewing |
| 7 | Partial | Undo and Record a refund shown; no "10 seconds" text; "How" is free text |
| 8 | Pass | Undo restored plan, coverage, no refund to-do |
| 9 | Pass | "Cancelled Nov 4, 2026, refund not recorded yet"; coverage Oct 30 to Nov 3, 2026; to-do "Due in 14 days" |
| 10 | Pass | 0 / empty / -5 rejected with "Enter an amount greater than zero." |
| 11 | Partial | Plan "refunded $79.00", to-do done. **Bug:** item's Money recovered says "Nothing recorded yet. Add it when the money comes back."; no "Plan refund" label or plan name anywhere. Home: "$79.00 on 0 items · $79.00 in cash" |
| 12 | Partial | Changed to $75.00. No Record a refund link once a refund exists; only ?refund=1 reopens it (pre-filled 79). One-entry check not possible (entry never shown) |
| 13 | **Fail** | Home tile "2 Protection plans · 2 running." with the tablet plan cancelled (two reloads). List total, Has a protection plan filter and plan icon correctly exclude it |
| 14 | Pass | Re-open and Delete offered; no Cancel/End/Stop covering |
| 15 | Pass | Re-open restored end date; refund, Money recovered and to-do gone |
| 16 | Pass | "It already ended..." uses End-this-plan date flow, no refund step |
| 17 | Pass | ?refund=1 opens refund step |
| 18 | Partial | Bob gets "Not found." on both plan URLs and ?refund=1; cancel/refund/reopen calls not tried (no buttons for Bob) |

## Other observations
- Home counts the refund "on 0 items" while the item page says nothing recorded; reads as a contradiction.
- Both items show "1 suggested policy to review" though created with no coverages (likely the known maker warranty/return suggestion).
- No wording read as legal advice.
