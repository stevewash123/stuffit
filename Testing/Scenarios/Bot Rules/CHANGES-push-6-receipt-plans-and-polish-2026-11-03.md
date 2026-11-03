# What changed in push 6: receipt plans become plans, and the retest fixes (2026-11-03)

For GrokBot. Push 6 is API `ba04c85` / UI `9f2c261`. It answers your retest of build `c9b76fd` (push 4) and the extra findings from push 5 (`9803509`). Check `/api/version` shows `ba04c85` before you start and record it. No migration in this push. Use Alice and Bob after a DB Stager scenario reset, because the receipt-plan rows below need fresh pending items.

Run **Scenario 44 steps 1 to 10 and 15**, then the rows named in the tables. The reader steps need the live reader; a reader miss is Partial, quote what it read.

## Receipt plans are now plans (Scenario 44)
| Change | What you should see | Your row |
|---|---|---|
| Quick add makes a plan | A plan read from a receipt (company, name, term, price, reader sure) is created as a **plan** on quick add: it appears under **Protection plans**, covers the item, has a kind (Warranty extension, Accident cover or Insurance), and has the receipt attached as its proof of purchase. The item shows the plan card, not a bare coverage | C44-4, C44-6 |
| Full Add and Add Details | Same result for the plans left ticked. An unticked plan makes nothing | C44-4 |
| Repeating the accept | A second tap or a retry makes **no second plan** | 44-5 |
| A plan that cannot be made | Missing company, term or price (for example the Lowe's plan with no company): **no bare coverage**. The item gets the to-do "Add your <company or plan name> plan: check its term" (once; dismissible). The to-do opens the item | C44-6, C44-8b |
| Add Details plan section | The plan line is editable: company, name, length, price, plan number, start. Only what you change is saved | C44-2 |
| Editing the New Item | Changing the New Item's name or model on Add Details is **kept after a reload** (it saves about half a second after you stop typing). If the plan's printed "covers" text no longer matches, the plan is unticked, held back from quick add, and says "Check this is for the item above". Naming the item back leaves the plan unticked until you tick it | C44-15 |
| Covers text | A plan that printed only "Covers SKU 6505727" shows **no covers line and no match claim**. Text like "Covers SKU 6571204 QN65Q80" shows "QN65Q80" and a match. The word "Covers" is never printed twice. The coverage terms on the item no longer show the SKU | C44-1 |

## Plan form, plan page and item card
| Change | What you should see | Your row |
|---|---|---|
| Ended label | A plan whose end day has passed reads **Ended** on the item card and the plans list. "Cancelled" no longer appears (there is no cancel state yet). After the plan has ended, "Stop covering" is not offered; Delete is | C31-9, C48-5 |
| Status word | The card status is Waiting (with the start date), Active, Ending soon or Ended. "Try this first" and "Backup" are a separate badge | C48-1 |
| Update from a newer document | Lists **only fields that really differ**, with "Saved now: ..." above the new value. Case, punctuation, commas versus semicolons, spacing, phone formatting and a trailing slash are not differences. Applying changes only the ticked fields. If nothing differs it says so | C31-6, C31-7 |
| Website | An address that already starts with http:// or https:// is not flagged and is ticked by default. A bare www.example.com/x is offered as https://www.example.com/x | C31-5 |
| Device default | The type-it-in drawer starts on **Insurance, monthly** for phones, tablets **and computers/laptops** (by category) | C43-7 |
| Paperwork route | "I have the paperwork or a photo" > Start a plan from it carries the file to the plan form and reads it at once; the plan is ticked for this item; the company is matched or its name filled in with "add as new". A price paid once reads "$299.99 one payment", never "a year" | C43-8, C43-9 |
| Type-it-in drawer | Company, what it is and start are marked required, with "Only company, what it is and start are needed." Optional service fee, claim phone and claim website sit under "More details". The covered item is a ticked, labelled checkbox row | C43-3, C43-10, C48-0 |
| Copy contract | Shows "Copied" for 2 seconds (an error message if the clipboard is blocked) | C48-1 |
| Home tile | Shows "N end within 60 days" only when N is above zero, and uses the same rule as the My Items "Plan ending soon" filter (counted from the last covered day) | C43-6 |
| Add purchase | Cancel with unsaved edits asks Keep editing / Leave without saving | C31-4 |
| Money recovered | An empty, zero or negative amount shows "Enter an amount greater than zero." and Save stays enabled; a missing date has its own message | P3-6 |
| To-do wording | New plan renewal to-dos say "From your protection plan." Old to-dos keep their old text | C43-15 |

## From your push 5 findings
| Change | What you should see |
|---|---|
| `?addPlan=1` | After you answer Yes and the item opens with "How did you get the plan?", the address no longer keeps `?addPlan=1`; reloading does not reopen the sheet |
| Account hint | Not a bug: the line "Warranty extensions, accident cover and other plans you bought on top of what an item already has." is on the **Account page** (the phone's Account tab), not in the dropdown menu, which has no hints. The push 5 notes sent you to the wrong place |

## Decided, do not report
- The Lowe's plan with no company has no "not verified" prompt on the item page itself: the to-do carries "pick the company", and Add Details lets you type the company.
- The quick-add toast does not name the plan.
- A plan on a multi-item receipt whose line cannot be matched to an item is still not attached.
- Old to-dos keep their old wording.
- A bare `www.` address still gets the server message "not a web address"; the page offers it with https:// added.
- Everything in "Decided, do not report" in the push 4 and push 5 notes still holds.

## Still open, do not report as new
- The subscription/service hide case and the "receipt already shows a plan" hide case of the plan question were not testable on push 5: retest them with fresh data.
- Cancel, renew and refund of a plan, a plan bought later, an item returned or replaced under a plan, phone-insurance deductibles and claim caps, appliance-plan limits, home-warranty service requests (Scenarios 45 to 47, 49, 50): not built.
