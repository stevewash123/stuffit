# What changed in push 9: cancel a plan and record the refund (2026-11-04)

For GrokBot. Push 9 is API `18dec35` / UI `90106c7`. Check `/api/version` shows `18dec35` and record it. One new migration (`PlanCancellation`: columns on plans, and recoveries can now belong to a plan) is applied on start; if plans or Money recovered fail with a server error, say so and stop.

Run **Scenario 51** (new). Scenario 45 stays deferred for the parts not built (waiting period, decision panel, plan bought later); do not run it.

## What you should see
| Change | What you should see | Your step |
|---|---|---|
| Cancel this plan | A button on the plan page, separate from **End this plan**, shown while the plan is not ended or cancelled. Opens "What do you want to do?": Stop it renewing (only when the plan auto-renews), Cancel it now, It already ended or I cancelled it | 51-2, 51-3, 51-6 |
| What we hold | Step 2 shows the plan's saved cancellation terms ("Cancelling: ..."), else the saved coverage notes, else "No cancellation terms saved for this plan."; the contract number with Copy; claim phone and website; "Check your contract for any cancel-for-refund window." It never states what the person is entitled to | 51-4 |
| Stop it renewing | "Ends <date> (will not renew)" on the plan and the item. The renewal to-do becomes the plain "ends on ... Renew or replace it". Coverage runs to the end date | 51-5 |
| Cancel it now | A date (default today, not before the plan's start) and an optional "How did you cancel?". Coverage on every covered item ends the day **before** the cancellation date (the same last-covered-day rule as ending a plan). A to-do "Check that your refund arrived" is due in 14 days, once | 51-7, 51-9 |
| Undo | Ten seconds after cancelling, **Undo** restores the plan and the items' coverage and removes the refund to-do | 51-8 |
| Record a refund | Amount (above zero), date (not before the cancellation, not in the future), optional method. "I haven't got it yet" leaves it for the to-do. One refund per plan: recording again replaces it | 51-9 to 51-12 |
| Money recovered | The refund shows as **Plan refund**, not a returned item, with the plan's name; one entry per plan. The to-do is marked done | 51-11, 51-12 |
| Cancelled status | The plan reads **Cancelled** (expired tone) with "Cancelled <date>, refunded $79.00" or "Cancelled <date>, refund not recorded yet" (with a Record a refund link) on the plan page, the list and the item card. Never Active or Ending soon | 51-9, 51-11 |
| Not counted | A cancelled plan is not running: out of the Home tile counts, the yearly cost total, the 60-day count, the My Items plan filters and the plan icon. Its own yearly cost counts only the billed months up to the cancellation | 51-13 |
| Re-open | A cancelled plan offers **Re-open this plan** (optional note) and Delete; no Cancel, End or Stop covering. Re-opening removes the refund, its Money recovered entry and the refund to-do, and restores the original end date | 51-14, 51-15 |
| Already ended | "It already ended or I cancelled it" uses the existing End-this-plan date flow: date only, no refund | 51-16 |
| `?refund=1` | On a cancelled plan the refund step opens | 51-17 |

## Decided, do not report
- Cancellation terms are shown only from what the plan already holds (read notes). The reader does not yet pull cancellation terms from a contract, so a plan made by hand shows "No cancellation terms saved".
- The item page's "Add a payout" form has no Plan refund option; plan refunds are recorded on the plan page.
- A plan refund has no item, so on Money recovered it shows the plan's name.
- Everything in "Decided, do not report" in the earlier push notes still holds.

## Still open, do not report as new
- Scenario 45's unbuilt parts: waiting period, monthly renewal decision panel ("Plan decision"), plan bought later, "Did this renew?" after the end date.
- Item returned or replaced under a plan, phone-insurance deductibles and claim caps, appliance-plan limits, home-warranty service requests (Scenarios 46, 47, 49, 50).
