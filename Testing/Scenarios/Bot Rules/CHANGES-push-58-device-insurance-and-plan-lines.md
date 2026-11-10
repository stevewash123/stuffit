# Push 58: phone and device insurance, and what a plan covers line by line (2026-11-10)

Stories S3.4.19 and S3.4.20 (with the lines of S3.4.7). API and UI. Migrations `DeviceInsurance` (warranty_plans: device_identifier, deductibles_json, claim_cap, replacement_kind, replacement_time) and `PlanLines` (new table plan_lines).

## Part 1: phone and device insurance

| Change | What to check |
|---|---|
| **Phone or device insurance** as a way in, on a phone | Open an item named like a phone, tablet, watch or laptop (for example "iPhone 16"). Add (Add-on protection) shows a fifth choice **Phone or device insurance**. It opens the plan form with the item ticked, insurance as the kind, monthly billing, auto-renew on, and the device section open. Other items (a dishwasher) do not show this choice |
| The device section on the plan form | Tick "This protects a phone or other device" (it is on the form for any plan). Fields: IMEI or serial (optional), a row for each kind of loss (Cracked screen, Other damage, Lost, Stolen, Anything else) with an amount or a range in words ("$29-$199"), claims allowed in 12 months, what a replacement is (new, refurbished, same model or equivalent), and how fast in the plan's words |
| Saving keeps it | Save; open the plan: a **Phone or device insurance** card shows the IMEI or serial, "Up to N in 12 months", the replacement kind and time, and "What a claim costs you" by kind of loss. Edit the plan: the section is open with the values |
| Only filled rows are kept | Leave some deductible rows empty: only the filled ones show. Untick the section and save: the device details are cleared |
| Bad input is refused | Two rows for the same kind of loss cannot be sent; a negative amount is refused (the form's inputs stop it, the API checks too) |

## Part 2: what a plan covers, line by line
| Change | What to check |
|---|---|
| A **"What it covers, line by line"** card on every plan page | Open a plan: below the plan decision (when shown) there is a card with an **Add a line** button and "Nothing listed yet" |
| Add an appliance, a system or an add-on | Add a line: kind (An appliance / A system of the home / An add-on), name (suggestions like Refrigerator, Heating system), brand, model, about how old in years, an item you own (one of the items the plan covers, or "None: it has no receipt"), limit in dollars, the limit in the contract's words, the contract's age limit in years, exclusions, and "My contract does not cover this one" |
| A system with no receipt | Add "Heating system", kind system, limit $5,000, age about 8. It shows "about 8 years old (your estimate)" and "limit $5,000.00" with no item |
| A linked item gives the age | Add a Dishwasher line linked to a dishwasher item you own that was bought years ago. It shows "about N years old (from your purchase date)"; the estimate you typed is ignored |
| The contract's age limit is flagged, not removed | Give that line an age limit lower than its age: "This is older than the contract's age limit of N years, so the contract may not cover it. Check the contract's words." The line stays |
| A line the contract leaves out | Tick "My contract does not cover this one": the line shows struck through with "Left out of your contract" and stays |
| Change and Remove | Change opens the line (an item-linked line shows no estimate); Remove asks first |
| Bad input | Saving with no name shows the message "Say what it is, for example Refrigerator or Heating system." |
| The export | Settings > export: `plan_lines.csv` is in the zip and listed in README.txt |

## Push 57 Lows
| Change | What to check |
|---|---|
| The plan summary line on a company's page has no stray "· " | A plan type with no price note (Best Buy's): the line reads "claims go to ..." with no leading dot. A plan type with nothing to say shows no line |
| "Add or confirm plan types" opens on that company | From Admin > Shared data > a company: the plan types page opens showing only that company's plan types, confirmed or not, with "Showing the plan types of one company. Show every company" |

## Not built yet (do not report)
- Part 2: offering "Add to your plan?" when a new item matches a line, claim counting and caps with reset, service requests (S3.4.8), a plan type filling the lines in one step, replacing an appliance under the plan, and the cost view.
- Counting claims against the cap ("1 of 2 used; resets ..."), service requests (S3.4.8), the upgrade flow when a new phone replaces the old one, claim help showing the deductible for the chosen loss, the cost view, and the three-layer explanation on the item page. Home appliance plans (S3.4.20) are next.
