# Scenarios run against the API, 2026-10-25

Script: `Testing/Scenarios/scripts/run_scenarios.py` (raw output: `last-run-2026-10-25.txt`). Local API on the dev database, throwaway account with the Chase Freedom Unlimited card (1111). For each scenario it uploads the emails then the receipt (warranty documents not uploaded), reads New Items, marks what the page ticks (overall confidence >= 0.8, the UI's rule), then Accepts the item and reads what My Items actually received. Today is 2026-10-25.

Not covered (needs the UI or the mailbox): Check Emails, the item-page warranty upload and its panel, the New Items chips, the badges/expander look, Save in the browser. The UI tick rule is mirrored, not run.

## What should happen (the purpose of each scenario)

| # | Purpose | Should happen | Result |
|---|---|---|---|
| 1 | Happy path: everything known and verified | One item, card filled from receipt, 90-day Home Depot window, Milwaukee 60 mo, card protection 120 d, no extended warranty (maker > 3 yr). Return window ticked | Lines and dates all right. **Only the return window was ticked/added.** Milwaukee and Chase are "likely" 0.75 |
| 2 | No order email | One item from the receipt, card and store filled | Right. Lowe's window 0.73 "likely": not ticked, **item added with nothing** |
| 3 | Store not in shared data | Store not recognised; **no return window** | Right (none offered). Added with nothing ticked |
| 4 | Brand not in shared data | Brand not recognised; **no manufacturer warranty**; Target window offered | Right on the brand. **Target 90 d window is 0.77, not ticked** (screwdriver set: category unknown). Added with nothing. Card extended warranty shown with **no length or end date** (0.45) |
| 5 | Store policy unverified | Kohl's window shown, marked unverified, low confidence | Right (0.05 "unconfirmed", placeholder). Not ticked, which is right for a placeholder |
| 6 | Brand policy unverified | Best Buy window ticked; Sony warranty marked unverified | Right (the Best Buy fix works). Sony 0.05 unconfirmed |
| 7 | No warranty document | Walmart window; Black+Decker 24 mo from shared data, **verified** | Window ticked and right. **Black+Decker came back 0.45 "likely", not verified** |
| 8 | Store protection plan | Best Buy window, LG 12 mo, Geek Squad 4 yr ending 2030-10-10, card lines | All lines and dates right. The window ends today, 10-25. Plan 0.75 not ticked |
| 9 | Card not on account | No card, no card coverage; Walmart window + Garmin | Right on card. **Walmart window 0.77, not ticked** (smartwatch: category unknown). Added with nothing |
| 10 | Online order, no receipt | One item from 3 emails, delivered; Amazon 30 d, Dyson 24 mo; no card lines (no card) | Right. Amazon 0.73 "likely": not ticked. Added with nothing |
| 11 | Warranty for another model | Lowe's window, B+D 24 mo, card lines; the reject step is UI only | Lines and dates right. Added with nothing |
| 12 | Receipt PDF attached to email | **One** item, email + receipt as 2 documents | The .eml alone makes one item with 2 documents. My script also uploaded the PDF by hand (the scenario says not to), which made a second item; Accept of that one was refused (409 same store and order number), which is correct |
| 13 | Warranty attached to order email | Attached warranty kept as terms, not read as a receipt; Makita 12 mo "your document" | Right: terms document, ticked at 1.0, added with the Walmart window |
| 14 | Marketing images in the email | Only the email (then the receipt) kept; logo, banner and badge not kept | **`app-store-badge.jpg` is kept as a document, typed receipt** |

## Didn't do what it should

1. **Accept can add an item with no coverage.** Scenarios 2, 3, 4, 5, 9, 10, 11 were added to My Items with nothing attached, because nothing reached 0.8. A tracked item with no policies is the case the "at least 1 policy" rule was meant to prevent. I have not run the browser's Save, so I don't know if its readiness check stops this; the API doesn't.
2. **0.75 "likely" never ticks.** Every manufacturer warranty and card benefit from shared data is "Read from the web" (0.75), and Lowe's and Amazon returns are 0.73. So even the happy path (1) adds only the return window; you tick the warranty and the card by hand. Only a warranty document (1.0) ticks a maker line. Decision needed: should evidence read from the web tick, or only official-source evidence?
3. **Store window 0.77 when the category is unknown (4, 9).** Target (verified) and Walmart (verified) drop below the bar because "screwdriver set" and "smartwatch" aren't in the category words. Against "store return policies should be almost automatic": a verified store's general window should tick, or the words need adding (screwdriver, smartwatch/watch).
4. **Black+Decker 24 mo is 0.45, not verified (7, 11 shows 0.75).** The same maker is 0.45 for the hedge trimmer and 0.75 for the drill. Probably the category (hedge trimmer vs the policy's category) costing an applicability factor. Needs a look.
5. **Card extended warranty with no end date (4).** With no maker warranty to extend, it is listed with no length at 0.45. The scenario says it should only come from the document.
6. **Marketing badge kept as a document (14).**
7. **Expired windows are still ticked and attached (6, ended 10-18; 8 ends today).** Unanswered earlier question: should an already-ended window be unticked?

## Smaller

- Scenario 2 item name is "Circular Saw" (the receipt's wording), not the answer key's full name; the receipt's register number is stored as the order ref although the key says no order number.
- Scenario 5 shows 0.05 for an unverified placeholder; fine for "low", but it reads as "nothing" next to 0.38 for tucked windows.
- Both "alternate" return windows (major appliances 2 d, electronics 30 d, smartphones 14 d) are correctly tucked at 0.3-0.38 in every scenario.

## Left behind

Three throwaway accounts (`scenarios+<time>@example.test`) in the dev database; local API stopped.
