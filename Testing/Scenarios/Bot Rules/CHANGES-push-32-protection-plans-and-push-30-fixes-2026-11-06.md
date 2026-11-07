# What changed in push 32: Protection plans front door and true state (S3.4.12 to 14), and fixes from your push 30 results (2026-11-06)

For GrokBot. API `14fa6e8` and UI `bdd617e`. Check `/api/version` (`commit` must be `14fa6e8`). Migration **`PlanOwnStart`** (seven new columns on `warranty_plans`, one on `coverages`; additive) is applied to staging before this push. Reader contract bumped to `warranty-v2` (two new fields: order date, enrolment window). Stories S3.4.12, S3.4.13, S3.4.14, S3.4.6 (minimal slice).

## New: a plan has its own start date (S3.4.14)
- Adding a plan **for an item** (item page, or the plan form opened for an item) asks **"When did the plan start?"**: *Same day as the purchase*, *On delivery*, *Another date*. Nothing is filled in until the person answers. A plan covering many items, or an existing plan, keeps the plain date field. ("On delivery" asks for the delivery day: a saved item does not keep one.)
- A plan whose start is in the **future** reads **"Not yet started"** / **"Starts <date>"**. It is listed, but not counted as coverage anywhere (item badge, "Next to end", Home, filters). An item whose only plan starts later reads **"Not covered yet"**, not "Coverage ended".
- **Waiting period** (S3.4.6 minimal: days only): counted from the plan's own start. The plan reads "Waiting period until <date>" then "Covered from <date>".
- A plan **document** dated after the purchase is read as bought later: its start is its effective date, else its order date. The reader now also reads the order date and any enrolment window.
- If the plan states an **enrolment window** ("within 60 days of purchase") and the dates are further apart, a note quotes it ("Your plan says enrolment is within 60 days; your dates are 75 days apart. Check the contract."). A note, never a block.
- The end date says **"counted from <start>"** while it still equals the start plus the term.

## New: one front door, one vocabulary (S3.4.12)
- Names used everywhere user-facing: **Protection plans** (page, menu, Home), **Add-on protection** (the section on an item), **Card extended warranty** (the free card benefit, always with "Card"). "Extended warranties" and "protection plan" are search synonyms on the plans page and in My Items; `/extended-warranties` redirects.
- The plans list shows every plan, including ones **needing details**; the empty state names the four ways to add one, each a link; a "What is the difference?" note separates a plan you bought from a card benefit.
- Home tile counts a not-yet-started plan separately. My Items filters "Has a protection plan" / "Plan ending soon" and the plan icon (already built) still work.

## New: the item page tells the truth about a plan (S3.4.13)
- Section **Add-on protection** with a plan card: company, plan, status (**Not yet started**, **Waiting period**, Active, Ending soon, **Renews**, Ended, Cancelled), dates, a one-line **what it adds** (from the plan's own covers text, else from what its kind means), service fee, claim phone and site, contract number with copy, link to the plan.
- The receipt line ("From your receipt: Paid $299.99, plan number …") with a confidence word only when the reader was under 80% sure.
- The claim wizard now breaks ties between equally fitting routes in the item page's order (maker first, card after), and no longer says "closes soonest" when the first route does not.
- No advice wording anywhere (a test checks it).
- **Already fixed earlier, now guarded by tests:** a plan ended today reads Ended on the plan, the item, "Next to end", Home and the plan list (FS-31-18, FS-40-6).

## Fixed (from your push 30 results)
| Where | What |
|---|---|
| Admin company links | Refusing a returns/support link now shows **why** ("must be on the company's own site" / "must be an https address") instead of "One or more validation errors occurred." |
| Private-sale item guidance | Reads "Ask the **seller** whether they will make a courtesy return…", never "Ask Private sale…" |
| Start-date notice (your repeated finding) | We could not reproduce it with a Sub-Zero-shaped fridge. One real gap is closed: if the to-do was already Done by another route while its notice was still pending, saving the date now settles the notice too. The server now **logs** each time it completes notices. **Please retest** (item page > To do card > save date > Notifications) and record whether the Notifications tab was **already open before** the save (that page loads once); if the "Enter the date" button is still there after a fresh load, record the notice id |

## Steps to run (Scenario 31/40 plus new)
1. Item with a protection plan bought with it (Geek Squad on a TV), end it today: Ended everywhere, "Expiring soon" gone (FS-31-18, FS-40-6).
2. Item page > Add-on protection > Add plan: the start question appears unanswered; choose **Another date** in the future: "Not yet started / Starts <date>"; item shows "Not covered yet" if it has no other coverage; Home counts it as not started.
3. A plan with a 30-day waiting period starting in the future, then today: "Waiting period until" then "Covered from".
4. Attach a plan contract dated after the purchase: the start offered is the document's effective/order date. A contract with "within 60 days of purchase" and dates 75 days apart: the quoted note.
5. Menu "Protection plans"; search "extended warranty" finds plans and items that have one; `/extended-warranties` redirects; empty state for a new account; "What is the difference?".
6. Claim wizard on an item with a maker warranty and a plan: maker first, plan "Backup"; wording says "Card extended warranty" only for the card benefit.
7. Admin > Companies > Edit pages: an http address and an address on another site each give their own message.
8. Private-sale item: no "Private sale" in the guidance text.

## Known gaps (built less than the story asked; do not report as new)
"What it adds" cannot say what the maker's warranty does not cover; the stack line cannot say how many months a card adds; the receipt line has no store SKU; the waiting period is days only (no initial-versus-renewal flag).

## Not changed, do not report as new
Items listed under pushes 26 to 31 "Not changed". Still not built: real-time toasts (S4.5.7), pending-consolidation table (S4.2.4), Error attention level (S9.2.11).
