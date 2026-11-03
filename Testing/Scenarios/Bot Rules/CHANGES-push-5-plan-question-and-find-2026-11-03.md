# What changed in push 5: the plan question, and finding plans (2026-11-03)

For GrokBot. Push 5 is API `9803509` / UI `1d9941b`. It follows push 4 (API `c9b76fd` / UI `76a7bbf`, notes in `CHANGES-push-4-add-on-protection-2026-11-03.md`; if you have not run push 4 yet, run it on this build). Check `/api/version` shows `9803509` before you start and record it. One new migration (`PlanQuestion`, adds a column to items) is applied on start; if adding or opening an item gives a server error, say so and stop.

Run **Scenario 44 steps 11 to 14** and **Scenario 48 step 12**, and recheck **43-15** (words). Scenarios 45, 46, 47, 49 and 50 stay deferred.

## The question when an item is added (Scenario 44, steps 11 to 14)
| Change | What you should see | Your step |
|---|---|---|
| The question | On the **Add purchase** form and on **Add Details** of a New Item, one line: "Did you buy additional protection, an extended warranty, insurance or something similar with this?" with **Yes / No / Not sure**. Small buttons, usable by keyboard, never blocks saving. Pressing the chosen answer again clears it | 44-11 |
| When it shows | Only for a store picked from the shared list (a store typed in by hand does not show it), an item whose category is Electronics (phones, computers, TVs, audio, cameras), Major appliances, Small appliances, Power tools or Smart home and security, with a price at or above your tracking minimum (default $50) or no price yet, and only when the receipt showed **no** plan for that item | 44-11, 44-14 |
| Not shown | A $5 item, a service or subscription, a store typed in by hand, an item in another category, an item whose receipt already shows a plan | 44-14 |
| Yes | After saving, the item opens with the "How did you get the plan?" sheet already open. Nothing is stored for Yes. Closing the sheet without adding a plan leaves nothing behind | 44-11 |
| Not sure | A to-do "Check for additional protection, extended warranty or insurance" due in 14 days (reminders from day 7), on the To do page and the item. Dismissible. One per item; a dismissed one does not come back. No plan is created | 44-12 |
| No | Remembered for that item: it is not asked again if you open Add Details for it again or edit the item. No to-do | 44-13 |
| Several items in one Add | Yes opens the sheet for the first item answered Yes only | note |

## Finding plans (Scenario 48 step 12, 43-15)
| Change | What you should see | Your step |
|---|---|---|
| My Items filters | The filter panel has a "Protection plan" group: **Has a protection plan** and **Plan ending soon** (within 60 days). They show in the address bar (`hasPlan`, `planEndingSoon`) and count on the filter button. Ended and cancelled plans do not count | 48-12 |
| Plan icon | A small shield on item rows that have a running plan. Tooltip and accessible label "Has a protection plan" | 48-12 |
| Search by contract number | The My Items search finds an item by its plan's company, plan name or **contract number**. A row found that way says "Matches plan contract GS-88104471" (or "Matches plan <name> (<company>)"). The line is not shown when the item's own words already match. Only your own account's plans are searched | 48-12 |
| Plans page search | **Protection plans** has a search box (company, name, contract number) | 48-12 |
| "What is the difference?" | On Protection plans, a collapsed note: a protection plan is bought (from the maker, a store or a third party); a card benefit comes with the card and is added automatically when the card is confirmed, and shows as "Card extended warranty". Links to Credit cards. No advice wording | 48-12 |
| Words | The Home hints for the 30-day and 60-day tiles and the Items window note now say "Warranties and protection plans". The account-menu hint says "Warranty extensions, accident cover and other plans...". The sample item says "Card extended warranty" | 43-15 |

## Decided, do not report
- The question's eligibility rule (shared store plus category plus price) is deliberate: the data has no "store sells plans" flag yet. A store or item outside the rule not showing the question is expected.
- A Yes that is closed without adding a plan is not remembered, so it will not ask again on that form.
- Card-benefit wording on the Credit cards pages ("Extended warranty" as a benefit kind), the welcome text and the PayPal hint stay as they were.
- The reminder email and the claim wizard may still use older plan wording: note it for 43-15 but it is not a failure of this push.
- Everything in "Decided, do not report" in the push 4 notes still holds.

## Still open, do not report as new
- The Home "Protection plans" tile counts "ending within 60 days" from the plan's end date; the new filter counts from the last covered day. They can differ for a plan ended on a future date, exactly at the 60-day edge.
- The "Plan ending soon" filter is not linked from the Home tile.
- The question is checked in the browser only; the server does not re-check eligibility.
- Not built (Scenarios 45 to 47, 49, 50): cancel, renew and refund of a plan, plan bought later, an item returned or replaced under a plan, phone-insurance deductibles and claim caps, appliance-plan limits, home-warranty service requests.
