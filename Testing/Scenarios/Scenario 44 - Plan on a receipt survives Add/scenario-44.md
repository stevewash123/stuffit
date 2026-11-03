# Scenario 44: The plan on the receipt is not lost when the item is added

**DEFERRED until implemented: S3.4.11 (and the Add Details half of S3.4.3).** Do not run before then. Steps that need a not-yet-built screen say what to look for and will fail on build 982952c.

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Reader on. Files from `Testing/SampleData/receipts/pdf`: Geek Squad 15, 16, 21; `30-thermal-walmart-vizio-tv-protection.pdf`; `33-a5-lowes-bosch-dishwasher-protection.pdf`.
**Time:** 45 min
**Built per:** S3.4.11, S3.4.3 (Add Details section, to-do when quick add cannot make the plan), S2.4.7. Reader on, real model: a reader miss is Partial, quote what it read.
**Why this plan:** UAT FS-41 steps 3 and 4 (build 982952c) failed: Add Details had no plan section and the full Add dropped the plan. The point of purchase is the best chance to record a plan.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Upload `21-letter-bestbuy-email-marketing-geek-squad.pdf` | One New Item (Sony headphones 349.99); plan under it: Geek Squad, 24 months, $49.99, for the headphones, matched to the item |
| 2 | Test1 | Open **Add Details** | A **Protection plan** section, ticked, with company, name, term, price, contract number and start editable |
| 3 | Test1 | Untick the plan, reload | Stays unticked. Tick again |
| 4 | Test1 | Add with the plan ticked | Item added with a coverage from a **plan record** (Extended warranties lists it); toast names both; the receipt is attached to the plan as proof of purchase |
| 5 | Test1 | Repeat the Add (second tap or retry) | No second plan |
| 6 | Test1 | Upload `15-thermal-bestbuy-tv-geek-squad.pdf`; **Quick add** | TV added with the 4-year plan, the row said the purchase date was used. If no plan could be made, a to-do "Add your Geek Squad plan" opens the form prefilled |
| 7 | Test1 | Upload `16-a5-bestbuy-dishwasher-geek-squad-install.pdf`; Add Details | Item plus 3-year plan; the install line is neither an item nor a plan; the item price is not the order total |
| 8 | Test1 | Upload `33-a5-lowes-bosch-dishwasher-protection.pdf` (plan with no company) | Plan section asks to pick the company; saving without one leaves the to-do, not a silent drop |
| 9 | Test1 | Upload the Walmart/Allstate receipt | Allstate matched or shown "not verified" |
| 10 | Test1 | In a full Add untick everything and Save | A message "Tick at least one coverage, or choose Add without coverage"; not a silent no-op |
| 11 | Test1 | Add a Best Buy TV by hand with no receipt | "Did you buy a protection plan with this?" Yes / No / Not sure |
| 12 | Test1 | Answer **Not sure** | A to-do "Check for a protection plan" due in 14 days; no plan created |
| 13 | Test1 | Add another TV by hand; answer **No** | Not asked again for that item |
| 14 | Test1 | Add a $5 item or a subscription by hand | The question is not shown |
| 15 | Test1 | Edit the name and model so the plan's covered product no longer matches | "Check this is for the item above"; plan flagged, not attached silently |
| 16 | Test2 | Look for any of Test1's plans or to-dos | None |

Also record: any plan that silently disappeared between New Items and the item page, and any step where the plan count on the list differs from what you added.
