# Push 50: Plan decision for ending or renewing protection plans (2026-11-10)

Story S3.4.17. API and UI. Migration `PlanDecision` (warranty_plans: renewal_price, decision_snoozed_until, decision_dismissed_for). Needs a plan with an end date within 30 days, or one that ended recently: use the test clock (forward only) or create a plan that ends in 10 days.

## What to check
| Change | What to check |
|---|---|
| Plan decision panel at the top of the plan page | A plan whose term ends within 30 days shows "This plan renews in N days" (auto-renewing) or "This plan ends in N days". Facts: Renews on / Ends on, Renewal price ("Not known: ask the company" until entered), Cost so far ("About $X (worked out from the price and how it is billed)"), and a list of the covered items with price, bought date, age, "the maker's warranty has ended" and "N other coverages still running" |
| No verdict | The wording never says whether to renew; no red/green on value |
| Enter or change the renewal price | Enter it, Save: the panel shows it |
| Stop it renewing | Only on an auto-renewing plan. After it, the panel goes away and the plan shows it will not renew |
| I renewed it | Opens a form with the end date a year on and an optional new price. Save: the plan's end date moves, the item coverages follow, the panel goes away until the next term |
| Cancel it | Asks first; coverage ends today |
| Replace it with another | Opens the add-plan form with the item ticked when the plan covers one item |
| Remind me later: 7 or 14 days | Panel goes away; it never snoozes past the end date. Reappears when the snooze ends |
| Nothing to do | Panel goes away for this term; a renewal (new end date) asks again later |
| After the date: "Did this renew?" | A plan whose end date passed with no answer shows the panel with Renewed / Ended or cancelled / Not sure yet. Ended or cancelled records the end the day after its last day |
| Home tile | The Protection plans tile lists each plan to decide on ("Care plan: ends in 9 days", "did it renew?"), soonest first, linking to the plan |

## Not built (do not report)
- Money paid out or replaced and service fees in the cost (waits on service requests, S3.4.8).
- A separate "Cancelled" answer after the date (cancelling a plan that already lapsed is refused; "Ended or cancelled" covers it).
- The renewal reminder email still links to the plan page; it does not name the panel.
- Plan types as shared data, phone/device insurance and home appliance plans: later pushes.

Repair-order card (from push 49) is unchanged by this push.
