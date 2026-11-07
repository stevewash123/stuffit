# What changed in push 33: what happens to a plan when its item changes (S3.4.16), a safer plan form (S3.4.18), and fixes from your push 32 results (2026-11-06)

For GrokBot. API `bd40de6` and UI `67b9071`. Check `/api/version` (`commit` must be `bd40de6`). Migration **`ItemReplacedAndPlanAnswers`** (items.replaced_by_item_id, warranty_plans.keep_when_empty, new table item_plan_answers) is applied to staging before this push. Stories S3.4.16, S3.4.18.

## Fixed (from your push 32 results)
| Where | What |
|---|---|
| Start-date notice still showing "Enter the date" (your repeated finding, finally reproduced) | The server had completed the notice; the Notifications card still drew its stored shortcut button labelled "Enter the date". A finished (completed or cancelled) notice's shortcut now says **Open**. Retest: save the date from the item's To do card with Notifications open, then reload: the card is done and its shortcut reads Open |
| "counted from <start>" missing on a plan made from a document (S3.4.14) | The item page's Add protection plan dialog dropped the term when a document had filled in the end date, so nothing could say it was counted. The term is now kept whenever the end date equals the start plus the term (dialog and the plan page's "start from the document"). The plan page, the Add-on protection card and the edit form then say "The end date was counted from the start, <date>, plus N months." A typed end date says nothing |
| Company "Claims or support page" (plain claim field in the admin create/edit dialog) accepted http and any site | A new or changed claims page must be an **https address of a real website**, with a plain message beside the field. Any host is allowed (claims sites are often on another host). Stored values are untouched. The returns and support pages under **Edit pages** still need the company's own site; **test those under Edit pages, not in the create dialog** |

## By design (do not report as new)
An ended plan shows its end date on the plan page ("to Nov 6") and the last day covered on the item card ("Nov 5"): the same convention as ended-by-miles.

## New (S3.4.16): WarrantyCat asks what happens to the plan
**Nothing changes without an answer.** Deleting an item, marking it returned, marking it disposed, or replacing it, when a protection plan is running on it, is refused until every plan has an answer (the message names the plan).
- **Mark returned:** the return form asks **"Did you return the plan too?"**: *Yes, refunded* (cancels the plan on the return date and records the refund; amount required), *Yes, no refund* (cancels it on the return date), *No, I'm keeping it* (plan keeps running, flagged on its page and in the list as covering an item you no longer have, plus a to-do), *Not sure* (to-do, nothing else changes). "Yes, refunded" is pre-ticked only for a plan read from the item's receipt.
- **Replaced by the plan:** a button on the item page. It makes the replacement item (brand, model, serial, date editable). The plan can *carry on*, *end*, or *restart from the replacement date*. The old item is kept, marked **Replaced**, and links to the replacement.
- **Mark disposed** (sold, given away, thrown away, lost, died): asks what happened (used only to word the answers; not stored), then the plan question: cancel, leave it with the new owner (for a sale or gift; the contract decides if it can be passed on), take it off the plan, keep, not sure.
- **Delete item:** the confirmation names the plan: drop it from the plan, or cancel it too.
- **A plan covering several items** is never cancelled, ended or restarted for one item; the others keep it.
- **A plan that covers nothing** shows Add items / Cancel / Keep on its page; Keep is remembered until it covers an item again.
- **Undo:** an Undo bar stays on the item page for the session: it re-opens a cancelled plan, puts items back on it, removes the to-dos, restores plan dates and puts the item back as owned. There is no undo after a delete (the item cannot come back); a plan cancelled along with it can be re-opened from the plan page.
- Wording is free of advice.

## New (S3.4.18): the plan form
- A start in the future says **"Not started yet"** on the form. Server refusals on the plan page read in plain words (never "One or more validation errors occurred."). An error about a field the form does not show goes in the banner. The first error field scrolls into view; the form fits a 360px screen.
- Already built, now covered by specs: a message beside each required field with focus on the first; end-before-start message; the unsaved-work warning; "Update from a newer document" lists only the differences; an address without https:// is offered with it added; confirmations for End this plan, Stop covering and delete file.

## Steps to run
1. Item with a plan bought with it: **Mark returned**: choose each answer in turn on separate items (*Yes, refunded* needs an amount; check the plan status/date; *No, keeping it* shows the flag and the to-do).
2. **Delete** an item with a plan: the dialog names the plan; try *drop it from the plan* and *cancel it too*.
3. **Replaced by the plan** on an item: make the replacement; try carry on / end / restart; the old item shows Replaced and links across.
4. **Mark disposed** with a plan: the two questions in order.
5. A plan covering **two** items: delete one: the other keeps the plan.
6. Delete the only item on a plan then open the plan: **Add items / Cancel / Keep**.
7. After a cancel, press **Undo** on the item page: the plan is running again with its dates.
8. Plan form: save empty (each field has its own message, focus on the first); a future start ("Not started yet"); leave with typed work (warning).

## Known gaps (not built; do not report as new)
- No entry from a service request (S3.4.8 is not built). No sold-by / serviced-by company picker line (needs S3.4.5 plan types). Marking returned from a return receipt in New Items, and recording a store refund, do not ask: the plan stays running and is flagged. A vehicle part deleted along with its vehicle drops off its plan without a question. The on-screen phone keyboard has not been tried on a device.

## Not changed, do not report as new
Items listed under pushes 26 to 32 "Not changed".
