# Push 60: more of the extended warranties (2026-11-10)

API and UI. Migrations `PlanOfferDismissals` (new table) and `PlanTypeLines` (plan_types.lines_json). Stories S3.4.5, S3.4.7, S3.4.8, S3.4.17, S3.4.19, S3.4.20.

## 0. Push 59 findings (the Medium and the Lows)
| Change | What to check |
|---|---|
| **Medium:** the fee and payout figures on "Asking for service" are this plan year's | A plan with a Covered request this year ($180) and an older year's request: the summary reads "... fees you paid $X this plan year, the company paid $180.00 this plan year" and, when the other years add more, "all years together: fees $X, the company paid $Y". The old year's payout no longer inflates this year's figure. The plan decision panel's "Service requests" line stays all-time on purpose |
| A request dated before the plan started is refused | "That is before the plan started." (this is how an earlier-year request got in) |
| A request shows the line and the item behind it | A request tied to the Dishwasher line and the item: "Dishwasher · UAT P58 Dishwasher" |
| No stray space before a comma | "Pat Lee, 555-010-5902" and "limit $5,000.00, $50.00 of it used this plan year" |
| Export: `plan_service_requests.csv` has a **past the claim cap** column (yes/no) and is ordered by plan, then date | With a cap of 2 and three requests, the third reads yes |

## 1. Add this to your plan? (S3.4.20)
| Change | What to check |
|---|---|
| A new item that looks like a line on one of your running plans is offered the plan | You have a plan with a line named "Refrigerator" (no item on it yet). Add a new item "Samsung refrigerator". Its page shows a card **Add this to your plan?**: "Your plan <name> lists a Refrigerator. Is this the one? Your contract still decides whether it is covered." |
| Only a yes attaches it | **Yes, add it to the plan**: the item joins the plan and the line is tied to it (the line then shows the item's age from its purchase date). The card goes away |
| A no is remembered | **No thanks**: the card goes away and does not come back for this item and plan, even after a reload |
| What is never offered | A line your contract leaves out ("My contract does not cover this one"); a line that already has an item; a plan that has ended or been cancelled; an item already on the plan; another account's plans |

## 2. The line follows a replacement (S3.4.20, S3.4.16)
| Change | What to check |
|---|---|
| Replacing an appliance under the plan carries its line to the replacement | A plan with a line tied to the old TV. Replace the TV and answer Carry on: the line now shows the replacement (age from today). Undo the replacement: the line goes back to the old TV |
| A phone plan names the new phone | A device-insurance plan with an IMEI. Replace the phone under the plan with a serial for the new one: the plan's IMEI/serial becomes the new phone's (or empty if it has none). Everything else (cap, deductibles) stays. Undo restores the old IMEI. A plan that covers other items too is not changed this way |

## 3. Plan types list their lines; fill a plan's lines in one step (S3.4.5, S3.4.7)
| Change | What to check |
|---|---|
| Operator: a "What this plan covers, line by line" editor on the plan type form | Admin > Companies > plan types > Add or Change: add rows (kind, name, limit $, the limit in their words, age limit). A repeated name or an unknown kind is refused. Blank rows are dropped |
| Person: **Fill in the lines from <plan type>** | A plan picked from a type that lists lines shows the button in the "What it covers, line by line" card while the plan has fewer lines than the type. It adds every line the plan lacks (matched by name, ignoring case); lines the person already has are untouched. Tick "My contract does not cover this one" on any that do not apply |
| Messages | A plan with no plan type, or whose type lists no lines, shows the message instead of filling |

## 4. Fees and payouts on the plan decision (S3.4.17, S3.4.8)
| Change | What to check |
|---|---|
| The plan decision panel shows the service requests | On a plan inside its decision window that has requests: "Service requests: 2 requests, fees you paid $150.00, the company paid $420.00". No line when there are no requests |

## 5. Claim help by kind of loss on a phone plan (S3.4.19)
| Change | What to check |
|---|---|
| Record a request on a phone plan with deductibles: "Kind of loss" | Pick Cracked screen: "The plan lists $29.00 for this. What you were charged is what counts: enter it below." and the fee box fills with 29 unless you typed one. Pick one listed as a range: the range shows. Plans with no deductibles have no such choice |

## Not built yet (do not report)
- Request attachments (photos, the company's email), joining requests to a general claim log or Money recovered, the claim wizard offer on a denial, the cost view for phone insurance, the three-layer explanation on the item page, the plan reader filling limits from an agreement, a seeded provider list, receipt-to-plan-type matching, a person adding their own plan type from the app.
