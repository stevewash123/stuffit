# Scenario 50: One plan, five appliances, each with its own age and limit

**DEFERRED until implemented: S3.4.20 (with S3.4.7, S3.4.8, S3.4.10, S3.4.16).** Do not run before then. Steps that need a not-yet-built screen say what to look for and will fail on build 982952c.

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Test1 has items "UAT Fridge" ($1,500, 5 years ago), "UAT Washer" ($800, 3 years ago), "UAT Dryer" ($700, 3 years ago) and no plan. Test1 also has an appliance that came with the house: a range, about 15 years old, no receipt.
**Time:** 50 min
**Built per:** S3.4.20, S3.4.7, S3.4.8, S3.4.10, S3.4.16, S3.4.2 (offer a plan for a new item).
**Why this plan:** appliances are bought over many years but the plan is bought once; at a breakdown the person needs this appliance's age, limit and history.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Add a protection plan from UAT Fridge > **It covers more than this item** | Plan form with Fridge pre-ticked in Cover items |
| 2 | Test1 | Company "UAT Appliance Shield", $24.99 monthly, start today, appliance limit $1,500 each, contract states "not covered if over 12 years old" | Saved; the plan page has an Appliances section |
| 3 | Test1 | Add Washer and Dryer from the list | Each line shows the item, approximate age from its purchase date, limit, and no age flag |
| 4 | Test1 | Add the range as a line with no receipt: "about 15 years old" | A line with a name and an estimated age; flagged over the stated 12-year limit with the quote; not removed |
| 5 | Test1 | Untick a second fridge line the contract does not cover | Recorded as excluded, not forgotten |
| 6 | Test1 | Add a new item "UAT Dishwasher" ($600) | The app offers "Add to your UAT Appliance Shield plan?"; never added silently |
| 7 | Test1 | Accept the offer | A dishwasher line linked to the item; plan shows 4 appliances plus the range |
| 8 | Test1 | UAT Washer: Request service; fee $75 | Shows the fee, limit remaining for the Washer ($1,500), requests used this term, claim phone and contract number |
| 9 | Test1 | Record the request: covered, repaired, cost to company $210 | On the Washer's history and on the plan; the plan shows "$210 of $1,500 used on Washer" |
| 10 | Test1 | Record a replacement under the plan | The replacement washer inherits the line; plan records the date and, if the contract caps replacements, how many are used |
| 11 | Test1 | Read the cost view | $24.99 x 12 = $299.88 a year, one plan counted once, plus fees paid; ages beside prices; no worth-it verdict |
| 12 | Test1 | Clock to the plan's anniversary | Per-appliance usage resets; ages increase; decision panel appears (S3.4.17) |
| 13 | Test1 | Mark UAT Dryer sold | Asks about the plan for that line; the dryer leaves; other lines keep the plan |
| 14 | Test2 | Open Test1's plan or its lines | Not found; nothing visible |

Also record: any appliance shown covered that is past the contract's stated age limit without the flag, any limit used that disagrees with the arithmetic ($210 of $1,500), and any plan counted twice in the yearly total.
