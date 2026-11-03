# What changed in push 4: Add-on protection (2026-11-03)

For GrokBot. Push 4 is API `c9b76fd` / UI `76a7bbf` (it includes the earlier slice at API `2b22f78` / UI `00ab4c9`). Check `/api/version` shows `c9b76fd` before you start, and record it in your report. Staging applies the one migration (`PlanKind`) on start; if plans fail to load or save with a server error, say so and stop.

Run **Scenarios 43 and 48** (no longer deferred) and the **steps of 44 listed below**. Scenarios 45, 46, 47, 49 and 50 stay deferred: do not run them.

## Names you will see
| Where | Name |
|---|---|
| Account menu, page title, empty state | **Protection plans** (it was "Extended warranties") |
| Section on the item page | **Add-on protection** |
| The card's free benefit | **Card extended warranty** (other card benefits still read "Credit card: ...") |
| Kinds of plan | Warranty extension, Accident cover, Insurance |

## Plans and the item page
| Change | What you should see | Your step |
|---|---|---|
| Ended plans are ended | A plan ended on a day shows Ended on the plan page and on the item. The item's badge, "Next to end" and the plan agree. The item says last covered the day **before** the day typed (plan ended Nov 3 reads "Ended Nov 2" on the item). This is the new rule, not a bug | 48-5, 48-6, FS-31-17, FS-31-18, FS-40-6 |
| Add-on protection section | On an owned item (view mode): a section with an **Add** button. It lists the item's plans | 43-1 |
| The way in | Add opens "How did you get the plan?" with four choices: paperwork or photo; I'll type it in; covers more than this item; came free with my card or store | 43-2 |
| Type it in | Company (typed, or picked; typing a new name adds it as "not verified" with no set-up screen), what it is, price and billing (month, year, once), start, length in months, contract number. Only company, what it is and start are needed | 43-3, 43-4, 43-16, 43-17 |
| It is a real plan | The plan appears under Protection plans (not just as a coverage), with the item covered, and the toast names it | 43-4, 43-6 |
| Phone, tablet, laptop | The "what is it" choice starts on Insurance and billing on monthly | 49-1 (only this default; the rest of 49 is deferred) |
| Plan card on the item | Company, plan name, kind badge, status (Waiting, active, ending soon, Ended, Cancelled), start and end, service fee, claim phone and website as links, contract number with a **Copy** button, a link to the plan | 48-1 |
| Add the rest | A plan saved without price, contract number or claim contact shows "Add the rest" on its card (opens the plan ready to edit), and a to-do "Add the rest of your <company> plan" appears once. Dismissing it does not bring it back. It is marked done when the details are filled in | 43-5, 43-17 |
| Stack line | With two or more layers (maker warranty, card extension, plan) a one-line explanation sits under the coverage list, using the real dates. It says when the plan starts the day after the maker's warranty ends. No advice wording | 48-2 |
| Try this first / Backup | The coverage that applies today is "Try this first"; a plan shows "Backup" while a maker or store warranty is still running | 48-3, 48-4 |
| Upgrade an old coverage | A bare "Extended plan" coverage (made before this build) shows "Add the plan's details"; saving makes a plan and replaces the bare coverage (its id changes, nothing is duplicated) | 43-13 |
| Add coverage > "Protection plan" | The old "Extended plan" kind in the generic Add coverage form now reads "Protection plan" and opens the plan form. Store, manufacturer, return and card kinds are unchanged | 43-7 |
| Home tile | "Protection plans": how many are running and "N end within 60 days". Links to the page. Hidden when none are running | 43-6, 48-12 (tile only) |
| Empty state | Protection plans with no plans explains one item versus many in two lines and links to the ways in | 43-12 |

## The plan form
| Change | What you should see | Your step |
|---|---|---|
| Field errors | Saving with company, name or start empty marks each field with its own message and moves focus to the first. No "One or more validation errors occurred." banner | 48-7, FS-31-2 |
| End before start | The message is on the End field with a "Did you mean ...?" | 48-8, FS-31-4 |
| Leaving with unsaved work | Cancel (or navigating away) with edits, or a read document not yet accepted, asks **Keep editing / Leave without saving**. This also applies to every page that already had this guard | 48-9, FS-31-14 |
| Newer document | "Update from a newer document" lists **only the fields that differ**, old and new. If nothing differs it says so and offers nothing to apply | 48-11, FS-31-15 |
| Web address | A website read as `www.example.com/x` is offered, and saved, as `https://www.example.com/x` | 48-10 |
| End this plan | Asks first, naming the number of items and the date | 48-5, FS-31-17 |

## Plans read from a receipt (Scenario 44, steps 1 to 10 and 15)
| Change | What you should see | Your step |
|---|---|---|
| Add Details ticks stay | Untick a plan on Add Details and reload: it stays unticked (kept per browser, so same browser only) | 44-3, FS-41-3 |
| What the plan covers | The New Items row and Add Details show what the plan printed it covers (a model or a name) and whether it matches the item. A mismatch says to check it is for the item above, and it is not ticked or added | 44-1, 44-15, FS-41-8 |
| Company missing or unlisted | A plan with no company says so ("not verified", pick the company on the item page); a company not in our list says "not in our list yet: not verified". The plan is kept either way | 44-8, 44-9, FS-41-7 |
| SKU | A store SKU on its own is **not shown and not counted as a match**. A plan whose covers text is only a SKU shows no covers line and no match claim. This is Steve's decision | 44-1, FS-41-2 |

## Decided, do not report
- SKU match text missing (see above). A plan on a receipt has no keep tick **on the New Items row**; the tick is on Add Details.
- The Add Details tick is kept in the browser only: a different browser or device will not remember it.
- The item's last covered day is the day **before** the end day typed (see "Ended plans are ended").
- A plan whose end day is today still reads as running on that day (S3.4.2 decision from earlier); the new ended rule applies from the end day.
- Phone insurance, appliance plans, cancel, renew, refund, "plan bought later" and "item returned or replaced" behaviour: not built (Scenarios 45 to 47, 49, 50).

## Still open, do not report as new
(Push 5 built the "Did you buy ..." question, the My Items filter and plan icon, search by contract number, the card-benefit note and the Home wording; see `CHANGES-push-5-plan-question-and-find-2026-11-03.md`.)
- One place on Home may still use older wording (check 43-15).
- The plan kind is not read from a contract by the reader, and `warranty_plans.csv` in the export has no kind column.
- The four-way sheet's "paperwork or photo" path uses the existing reader (needs the reader on; otherwise note "reader off").
- Previous retest items still open are in `RETEST-NEXT-BUILD.md`.
