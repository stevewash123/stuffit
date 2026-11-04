# Scenario 54: A warranty whose start is not the purchase date

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Test1 has the Chase Freedom Unlimited card ending 1111. Clock offset 0 (app date **2026-11-04**). Reader on for Parts B to D; otherwise note "reader off".
**Time:** 55 min
**Built per:** S3.1.11 (start rule `installation` / `registration`, pending start, to-do and notification, built 2026-10-18), S3.1.12 (dates follow the app's clock), S3.2.8 (serial decoding is **not built**), S2.4.1. Sub-Zero, Wolf and Cove use the installation rule (`manufacturers-appliances-round1.json`). Documents: `Testing/SampleData/warranties/edge-{registration-required,starts-at-manufacture-date,delivery-date-and-ddmmyyyy}.pdf`.
**Why this plan:** the date the clock starts decides every end date and every reminder. A start the app guesses is worse than a start it asks for. Only the receipt's purchase date is tested elsewhere.

**Part A: installation start (built)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Add by hand: "UAT Sub-Zero Fridge", brand Sub-Zero, bought 2026-09-20, $8,500, card 1111. Look at the suggested maker warranty | Proposed with a note that it starts at **installation**; counted from the purchase date for now and flagged **start pending**. Whole product 24 months; sealed system parts 144 months / labor 60 |
| 2 | Test1 | Add it (Add Details or accept the suggestion) | One to-do: "Enter the start date of your Sub-Zero warranty on UAT Sub-Zero Fridge", due **2026-11-18** (14 days). A `warranty_start_needed` notification arrives at once in the app **and** by email to everyone on the item |
| 3 | Test1 | Try to mark the to-do Done without a date | Refused; **Dismiss** and **Not applicable** still work (test them on a second Wolf item in step 9, not here) |
| 4 | Test1 | Enter the installation date **2026-10-15** from the notification action (`enter-date`) | Whole product ends **2028-10-15**; sealed system parts **2038-10-15**, labor **2031-10-15**; the Chase extension (if shown) moves with it; the to-do is finished; the notification is cleared |
| 5 | Test1 | Check the item page | The "pending" flag is gone; the line says the start came from the date the person entered, not the receipt |
| 6 | Test1 | Add "UAT Wolf Range", brand Wolf, bought 2026-09-25. Add it. Enter the date from the **to-do** this time (2026-10-01) | Same behaviour. Burners / heating elements / hood motors / control boards / magnetrons line (parts 60, labor 24): parts **2031-10-01**, labor **2028-10-01**; whole product **2028-10-01** |
| 7 | Test1 | Add "UAT Cove Dishwasher", brand Cove. Add it and enter the date from the **item page** (`/coverages/{id}/start` equivalent) | Same behaviour; the to-do finishes |
| 8 | Test1 | Add a second Sub-Zero item and, instead of the to-do, edit the start date in the coverage editor | Counts as entering it: the to-do finishes and the flag clears |
| 9 | Test1 | Add a Wolf item. On its to-do press **Dismiss**, then repeat on another with **Not applicable** | Both work. Record what the coverage then shows (still pending, or dated from purchase) and whether the person is told |
| 10 | Test1 | Add a Cove item then delete the coverage | The to-do goes with it; no notification stays |
| 11 | Test1 | Quick add a Sub-Zero item | The to-do and notification are still created (the rule is the same for every add path) |
| 12 | Test1 | Move the clock to 2026-11-17 (the quick-added Sub-Zero item from step 11 is still undated; its to-do is due 2026-11-18) | One nudge the day before the due date. Not before. Not twice. Items already dated, dismissed or deleted get none |
| 13 | Test2 | Open Test1's notification or item addresses | Not found |

**Part B: a term that depends on registering (known gap)**

Item: Trailblaze TB-350 portable power station, bought **2026-10-20** (the 30-day registration deadline is **2026-11-19**, still open). Document: `edge-registration-required.pdf`.

| # | Persona | Action | Expected |
|---|---|---|---|
| 14 | Test1 | Add the item by hand, upload the document to it | Two possible terms are read: **90 days** unregistered (ends **2027-01-18**), or **3 years** if registered within 30 days of purchase (ends **2029-10-20**) |
| 15 | Test1 | Look at what is proposed | The app **asks** "Did you register it?" and does not assume the 3 years. Until answered, only the 90-day term counts as covered. Record the wording |
| 16 | Test1 | Answer **No** | 90 days, ends 2027-01-18; the 3-year term is not shown as active |
| 17 | Test1 | Change the answer to **Yes** and give a registration date 2026-11-01 | 3 years, ends 2029-10-20 |
| 18 | Test1 | Change the answer to **Not sure** | Neither term asserted; a to-do or reminder to check before **2026-11-19**. Record whether the deadline is mentioned. (If not built, mark Not built; it is the reminder that makes the question useful) |
| 19 | Test1 | Repeat with a purchase date of 2026-09-01 (deadline 2026-10-01, already past) | The app does not offer to register; says the registration window has passed. Record what it offers |

**Part C: a start derived from the serial number (not built; tests the safe failure)**

Item: Aeroflow AF-D50 dehumidifier, serial **AF 2512 00417** (built December 2025), sold **2026-10-01**. Document: `edge-starts-at-manufacture-date.pdf`.

| # | Persona | Action | Expected |
|---|---|---|---|
| 20 | Test1 | Add the item with the serial, upload the document | The rule is read: 24 months from manufacture, not less than 6 months from sale |
| 21 | Test1 | Look at the dates | **If serial decoding is built:** ends December 2027 (the later of 24 months from December 2025 and 6 months from sale = 2027-04-01). **If not built (expected today):** the app does **not** use the sale date as the start silently; it says the start depends on the serial and asks. A 24-month end date of 2028-10-01 with no warning is a **Fail** |
| 22 | Test1 | Add a second unit with serial AF 2412 00102 (December 2024), sold 2026-10-01 | If decoding is built: unit sold 22 months after manufacture, balance only, but not less than 6 months from sale (**2027-04-01**). If not built: same safe failure as step 21 |
| 23 | Test1 | Add a unit with no serial | The app asks for the serial; no end date is invented |

**Part D: delivery date and day/month/year (reader)**

Item: Nordhaus ES-200 espresso machine, ordered 03/04/2026, delivered 11/04/2026. Document: `edge-delivery-date-and-ddmmyyyy.pdf`.

| # | Persona | Action | Expected |
|---|---|---|---|
| 24 | Test1 | Add the item by hand (purchase date 2026-04-03) and upload the document | Order **3 April 2026**, delivery **11 April 2026** (day/month/year). Term 24 months **from delivery**: starts **2026-04-11**, ends **2028-04-11** |
| 25 | Test1 | Check for the two classic mistakes | Start is **not** 2026-04-03 (the order) and **not** 2026-11-04 (11/04 read as month/day, which is **today** in this run, so a misread looks plausible). Start is not 2026-03-04 either |
| 26 | Test1 | Read what else was extracted | The German line and the statutory-rights sentence are **not** turned into a term. Valid in the EU and UK is kept as a condition or note, not an error |
| 27 | Test1 | Change the app's date format or locale if one exists (Settings) | Dates on the item follow the setting; the stored start does not change |

Also record: any end date the app showed before it had the date it needed, any case where the pending flag stayed after a date was entered, and any date that disagrees with the key by a day.
