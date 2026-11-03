# Scenario 45: A plan that renews, ends or is cancelled

**DEFERRED until implemented: S3.4.6, S3.4.14, S3.4.15, S3.4.17.** Do not run before then. Steps that need a not-yet-built screen say what to look for and will fail on build 982952c.

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Test1 has "UAT Phone" ($900) and "UAT Tablet" ($500), bought 10 days ago. Clock offset 0.
**Time:** 50 min
**Built per:** S3.4.6 (renewing until cancelled, waiting period), S3.4.14 (bought later), S3.4.15 (cancel and refund), S3.4.17 (decision panel), S2.4.13, S5.4.11. Uses the simulated clock.
**Why this plan:** a person who elected a plan wants to know when it starts, when it renews and how to stop it with money back; ending it by date says none of that.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Add a monthly plan on UAT Phone: $12.99, no end date, renews until cancelled, starts 10 days ago, 30-day waiting period | Status **Waiting** for 20 more days; "Covered from <date>"; the item says the same; next renewal date shown |
| 2 | Test1 | Open UAT Phone's Make a claim | Says coverage has not started and when it does |
| 3 | Test1 | Clock +21 days | Plan Active; item says covered |
| 4 | Test1 | Read the yearly cost on the plans list | $155.88 a year (12 x 12.99), not $12.99 |
| 5 | Test1 | Clock to 30 days before the next renewal | Reminder and notification "renews on <date> - cancel or compare", linking to a **Plan decision** panel |
| 6 | Test1 | Read the panel | Renewal date; cost so far; paid out (none); covered items with age; other layers; no word on whether to renew; actions Stop it renewing, Cancel it, I renewed it, Replace it, Remind me later, Nothing to do |
| 7 | Test1 | **Remind me later** 7 days | Snoozed; returns in 7 days and not after the end |
| 8 | Test1 | **Stop it renewing**; "I cancelled", today, by phone | Flow first shows the contract's cancellation terms (quoted), how to cancel and the contract number |
| 9 | Test1 | Look at the plan and the item | "Ends <renewal date> (will not renew)"; renewal reminder replaced; end reminder remains; item coverage ends that date |
| 10 | Test1 | Add a 2-year $79 one-payment plan on UAT Tablet bought 5 days ago with a stated 30-day full-refund window | Plan page shows "Cancel for full refund by <date> (25 days left)" quoted from the contract |
| 11 | Test1 | Cancel it now; "I got a refund": $79, today | "Cancelled <today>, refunded $79"; coverage ends today; Money recovered counts $79 as a plan refund (not a returned item); yearly cost excludes it; no refund to-do |
| 12 | Test1 | Cancel another plan and record no refund | To-do "Check that your refund arrived" due in 14 days |
| 13 | Test1 | Add a plan whose start is 30 days after the item's purchase | The start is the plan's own date; "Starts <date>" if future; no coverage counted before it; waiting counts from it |
| 14 | Test1 | Type a start 90 days after the item where the plan text says enrolment within 60 days | A neutral note quoting the plan's window; save still allowed |
| 15 | Test1 | Let a plan pass its end date with the clock, no answer | "Did this renew?" with Renewed / Ended / Cancelled; plan not left active |
| 16 | Test1 | Read all cancel wording against the plan's own text | Nothing says what the person is entitled to; every statement is quoted with its page |
| 17 | Test2 | Open any of Test1's plan addresses | Not found |

Also record: any money figure that disagrees with the arithmetic (12 x 12.99 = 155.88), any date that disagrees with the simulated today, and any cancel wording that reads as legal advice.
