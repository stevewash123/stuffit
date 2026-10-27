# Scenario 1: a Home Depot pick-up order, one Milwaukee hammer drill (happy path)

One purchase, one item, everything known to the system. An order email arrives, the receipt is uploaded, the item is added to My Items, then the manufacturer's warranty is uploaded on the item. Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty.

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | The Home Depot #2310, Testville, ME |
| Store in shared data? | Yes: **Home Depot**, a shared store (the name "The Home Depot" and the store number match it) |
| Store verified? | Yes. Return policy **90 days**, verified 2026-09-30 (source: homedepot.com/c/Return_Policy). The 2-day policy is for major appliances only and does not apply |
| Order number | H23100-41982 (on the email and printed on the receipt, which is what joins them) |
| Register transaction | 2310 0914 4471 (receipt only) |
| Purchase date | 2026-09-14 (email 08:20, picked up 11:05) |
| Item | Milwaukee M18 FUEL Hammer Drill/Driver, **tool only** (no battery) |
| Model / serial | 2904-20 / M18F26B3305172 (the serial is on the receipt and the warranty) |
| Item price / tax / total | $249.00 / $13.70 (5.5%) / **$262.70** |
| Payment | VISA ending **1111** |
| Card on the test client | **Chase Freedom Unlimited** (last four 1111, current) |
| Card benefits verified? | Yes, verified 2026-09-30. Purchase protection: 120 days, up to $500 per item. Extended warranty: adds 12 months to manufacturer warranties of 3 years or less, so it does **not** apply to this 5-year warranty |
| Brand in shared data? | Yes: **Milwaukee**, a shared brand |
| Brand verified? | Yes. Category **Power tools**: 60 months from purchase, verified 2026-09-30 (source: milwaukeetool.com/support/registration-and-warranty). The evidence is a human search, not an official-source read |
| Purchased by | Sam Sample (name on the pick-up and the warranty) |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 1 | `01-email-homedepot-order-milwaukee-hammer-drill.eml` | Order confirmation, "Pick Up In Store" | The test mailbox, then a scan |
| 2 | `02-receipt-homedepot-pickup-milwaukee-hammer-drill.pdf` or `.jpg` | Register receipt for the pick-up. The two files are the same receipt (use one) | New Items, Upload a receipt or warranty |
| 3 | `03-warranty-milwaukee-m18-hammer-drill.pdf` or `.jpg` | Milwaukee Tool limited warranty for this tool and serial. The two files are the same document (use one; the `.jpg` is a skewed phone photo) | The item's page, after it is in My Items |

### Steps and what should happen

1. **Send the email to the test mailbox.** From `C:\Projects\StuffIt\TestEmails`: `python send_scenario.py 1` (it asks for the Gmail app password). Then run Check Emails.
   - New Items gets **one** item: Milwaukee M18 FUEL hammer drill, from The Home Depot, order H23100-41982, 2026-09-14, $262.70, model 2904-20. No card yet: the email does not name one.
2. **Upload the receipt** in New Items.
   - It joins the same item through the order number (no second item). The receipt is added as a document and fills what the email lacked: the card (VISA 1111, so **Chase Freedom Unlimited**).
3. **Add the item to My Items.** The review should propose:
   - Home Depot return window: 90 days, ends **2026-12-13**.
   - Milwaukee manufacturer warranty: 60 months, ends **2031-09-14**.
   - Chase Freedom Unlimited purchase protection: 120 days, ends **2027-01-12**.
   - Chase Freedom Unlimited extended warranty: not offered (the manufacturer's warranty is longer than 3 years).
4. **Upload the warranty** from the drill's page. The panel is headed with the file name and says Warranty document.
   - Store: The Home Depot #2310 matches Home Depot. Nothing to decide.
   - Model number 2904-20 matches the item. Nothing to decide.
   - **Brand: Milwaukee vs Milwaukee Tool** shows as "Close, but not the same". Either choice is fine: Milwaukee is a shared name, so it is never renamed and the item keeps it.
   - Then it asks to add the warranty: 5 years on the tool (motor and electronics), 1 year on the chuck (ends 2027-09-14). Registration is optional within 90 days (by 2026-12-13). Add it; "Came with the product" is the right origin.

## Checked when this was made

- The email read by the plain email parser (no model): Ok, store The Home Depot, stage Confirmation, order H23100-41982, date 2026-09-14, total 262.70, 1 item.
- The receipt PDF text: store 2310, order H23100-41982, 09/14/2026, model 2904-20, SN M18F26B3305172, subtotal 249.00, tax 13.70, total 262.70, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The warranty PDF text: Milwaukee M18 FUEL Hammer Drill, model 2904-20, serial M18F26B3305172, The Home Depot #2310, 2026-09-14, tool 5 years, chuck 1 year. Its `.jpg` is a photo of the same document.
- Shared data (store, brand, policies, card, last four 1111) read from the development database on 2026-10-24.

## Known rough edges (not part of the answer key)

- The "Milwaukee Tool" prompt in step 4 is the system being careful, not an error. Adding "Milwaukee Tool" as an alias of the shared Milwaukee would remove it.
- The small print at the bottom of the warranty says its facts were copied from "receipt 41-thermal-homedepot-milwaukee-hammer-drill". That is the older register receipt in `receipts/pdf` for the same purchase (same item, serial, date and VISA 1111, but no order number). The receipt in this folder replaces it for this scenario.
- The email is the pick-up order confirmation. The plain parser reads a register e-receipt from Home Depot as Thin (no items, date or order number), so an order confirmation is the reliable email for a happy path.
