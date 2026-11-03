# Scenario 43: I have a protection plan: every way to add one

**DEFERRED until implemented: S3.4.10, S3.4.12.** Do not run before then. Steps that need a not-yet-built screen say what to look for and will fail on build 982952c.

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist and are clean. Test1 has items "UAT TV" ($800, Best Buy, 20 days ago) and "UAT Laptop" ($1,200, Best Buy, 5 days ago) and no plans.
**Time:** 40 min
**Built per:** S3.4.10 (the sheet and its four ways), S3.4.12 (words, empty state), S3.4.2 (plan form, reader). Reader steps need the reader on; otherwise note "reader off".
**Why this plan:** a person who elected a plan must find how to add it from the item, the plan page and a photo, and every way must make the same record (a plan, not a bare coverage).

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open UAT TV (view mode). Look at the coverage section | An **Add a protection plan** button beside Add coverage. Record wording and position |
| 2 | Test1 | Click it | One sheet "How did you get the plan?" with four choices: paperwork or photo; type it in; covers more than this item; came free with my card or store |
| 3 | Test1 | Choose **I'll type it in** | Plan form with the item already chosen. Required: company, name or length, start. Price, contract number, fee, claim contacts are optional |
| 4 | Test1 | Company Geek Squad (from the list), name "2-Year Protection", 24 months, start today, Save | Toast "Geek Squad plan added to your UAT TV". The item shows the plan beside the maker warranty, ending 24 months out |
| 5 | Test1 | Open the item's plan row | Opens the plan page (not a dead end) listing UAT TV. "Add the rest" offers price, contract number, fee, claim phone. A dismissible to-do "Add the rest of your Geek Squad plan" is on the To do page |
| 6 | Test1 | Open Account > Extended warranties and Home | The plan is listed (company, status, 1 item). Home shows a Protection plans tile |
| 7 | Test1 | On UAT Laptop open Add coverage and its kind list | "Extended plan" is no longer a bare coverage form (opens the same sheet, or is gone). Record which |
| 8 | Test1 | UAT Laptop > Add a protection plan > **paperwork or a photo**; upload `Scenario 8 .../03-protection-plan-*.pdf` (reader on) | "Reading your document..."; each value with quote and page; nothing saved until accepted; company matched or flagged not verified |
| 9 | Test1 | Accept and Save | Laptop shows the plan with the contract's term; the file is attached to the plan as its contract; the item's receipt is not attached to the plan |
| 10 | Test1 | From UAT TV choose **It covers more than this item** | Plan form with UAT TV pre-ticked in Cover items |
| 11 | Test1 | Choose **It came free with my card or store** | Shows the card or store coverage already proposed and how to add the card; no plan created |
| 12 | Test2 | Open Extended warranties (no plans) | Empty state explains one item versus many in two lines and links to the four ways |
| 13 | Test1 | Open a plan-less extended coverage (stage with DB Stager) | Shows "Add the plan's details"; pressing it upgrades in place without duplicating the coverage |
| 14 | Test2 | Paste the address of Test1's plan | Not found; nothing of Test1's plan shows |
| 15 | Test1 | Check the words on the item page, Extended warranties, reminder email, claim wizard | A paid plan is always "protection plan"; the card benefit is always "Card extended warranty". Record any place that still mixes them |
| 16 | Test1 | Add "UAT Phone" ($999) from a receipt that does not show insurance. On the item, open the insurance section and type a company the app has never seen ("UAT Phone Cover Co"), insurance, $14 monthly, starts today | Saved with no company set-up screen, no role and no website asked; the company shows "not verified" (typing a new company inline already works on 982952c via Add "name"; the new part is that it saves a plan with price and billing, not a bare coverage); the plan is on the phone and in Extended warranties; a later plan typed with the same name reuses the company |
| 17 | Test1 | Same, leaving everything but company and start blank | Saves; "Add the rest" and the to-do offer the missing fields |

Also record: any way of adding a plan that creates a plan-less coverage, any plan that appears twice in the list, and any wording that reads like advice to buy a plan.
