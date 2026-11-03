# Scenario 47: A monthly home warranty: waiting period, limits, asking for service

**DEFERRED until implemented: S3.4.4, S3.4.5, S3.4.6, S3.4.7, S3.4.8 (and S3.4.9 for the state step).** Do not run before then. Steps that need a not-yet-built screen say what to look for and will fail on build 982952c.

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Test1 has "UAT Dishwasher" ($700). 2-10 Home Buyers Warranty exists as a company with role warranty provider and plan types Systems and Pinnacle (have an operator stage them if not).
**Time:** 60 min
**Built per:** S3.4.4 (company page leads to plans), S3.4.5 (plan types), S3.4.6, S3.4.7 (covered home and lines), S3.4.8 (limits, fees, requests), S3.4.9. Reader steps need the reader on and the 2-10 sample contract (Texas) from `Testing/SampleData/warranties`.
**Why this plan:** the home-warranty owner covers things that have no receipt, pays monthly, waits 30 days, and must decide at a breakdown whether to call.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open the 2-10 company page | A **Plans** section: what a plan is in one line; Upload the contract / Type it in; plan types listed with "Use this plan" |
| 2 | Test1 | **Use this plan** for Systems | Plan form filled from the shared terms, marked as from the company's record; the user's own price, dates and contract number win |
| 3 | Test1 | Upload the 2-10 sample contract (reader on) | Company matched; $39.99 or $59.99 monthly; **30-day waiting period, initial plan**; recurring until cancelled; Texas read; bracketed alternatives such as [Monthly] [One-Time] flagged "pick one", not guessed |
| 4 | Test1 | Enter the covered home address; start 10 days ago | Status **Waiting** until day 30; "Covered from <date>" |
| 5 | Test1 | Read the covered lines | Heating, cooling, electrical, plumbing, ducts; Pinnacle adds kitchen and laundry appliances; unticking a system the contract leaves out removes the line; each line has its limit ($5,000 HVAC, $2,000 per appliance) with page and quote |
| 6 | Test1 | Match UAT Dishwasher | Offered "This plan covers it"; never attached silently; item page shows the plan with its limit and waiting state |
| 7 | Test1 | Read the yearly cost on the list | One plan, 12 payments; not once per line or per item |
| 8 | Test1 | UAT Dishwasher: Make a claim during the waiting period | Says coverage has not started and when it does |
| 9 | Test1 | Clock past day 30; Request service | Shows the phone or online link, contract number, waiting state over, the limit, the service fee as a range when it is one, exclusions |
| 10 | Test1 | Record a request: what broke, who was sent, fee $75, decision covered, what was replaced | Request on the plan and in the item's claim log marked as a plan request; the plan shows requests this year and limit remaining on that line |
| 11 | Test1 | Record a second request, denied, reason in the company's words | Reason and the contract text it points to kept; the claim wizard offered later |
| 12 | Test1 | Read the cost view | Price paid plus fees ($75) beside what it paid out; no worth-it verdict |
| 13 | Test1 | Attach photos and the company's email to a request | They attach like other documents |
| 14 | Test1 | State check: the contract says Texas | "Your contract says X; the shared record says Y" if they differ; the user's contract wins; "No version for <state> yet" for another state |
| 15 | Test2 | Add a plan at the same address | Test2 sees only their own plan, home and requests |

Also record: any limit or fee shown without a source, any guess at a bracketed contract value, and any wording that states a legal right.
