# Scenario 8: A store protection plan on the receipt, with its own document

Based on `Scenario 1` (the happy path), with one change: **The receipt carries a Geek Squad 4-year protection plan line, and the document uploaded is the plan, not a manufacturer warranty.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | BEST BUY, store 0123, Testville, ME |
| Store in shared data? | Yes: **Best Buy**, a shared store |
| Store verified? | Yes. 15 days (14 days for smartphones), verified 2026-10-22 |
| Order number | BBY01-806771 |
| Purchase date | 2026-10-10 (Sat 10 Oct 2026) |
| Item | LG 65-inch OLED evo C4 4K Smart TV + Geek Squad Protection, 4 years |
| Model / serial | OLED65C4PUA / 512KCZM9Y447 |
| Item price / tax / total | $1,496.99 + plan $299.99 / $82.33 (5.5%, on the TV only) / **$1,879.31** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **LG**, a shared brand |
| Brand verified? | Yes. 12 months for TVs, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-best-buy-lg-oled65c4pua.eml` | Order confirmation (pick-up) | The test mailbox, then a scan |
| 02 | `02-receipt-best-buy-lg-oled65c4pua.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |
| 03 | `03-protection-plan-best-buy-lg-oled65c4pua.pdf` or `.jpg` | Geek Squad protection plan document (the two files are the same document; use one) | The item's page, after it is in My Items |

To send the email: from `C:\Projects\StuffIt\Testing\TestEmails`, `python send_scenario.py 8` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email**, then scan. New Items gets one item: LG 65-inch OLED evo C4 4K Smart TV, order BBY01-806771, 2026-10-10. The email lists the TV and "Geek Squad Protection, 4 years (OLED65C4PUA)"; total **$1,879.31** (the plan is not taxed).
2. **Upload the receipt.** It joins the same item, adds the card (VISA 1111 = Chase Freedom Unlimited) and shows the plan line (plan # GS-91440236, $299.99), so a protection plan is proposed with the receipt's details only.
3. **Add the item to My Items.** The review should show the Best Buy return window, the LG warranty from shared data (12 months), the Geek Squad plan, and the card coverage.
4. **Upload the plan document** from the item's page (headed with the file name; it is a retailer protection plan, not a manufacturer warranty).
   - Model number OLED65C4PUA and the store match. Nothing to decide.
   - It asks to add the plan: "This looks like the protection plan for your LG ...". Add it. The plan replaces the proposal made from the receipt: 4 years, starting on the purchase date, plan number and price from the document.

## Expected coverage (dates counted from the purchase date)

- Best Buy return window: 15 days, ends **2026-10-25**.
- LG manufacturer warranty: 12 months from the shared data, ends **2027-10-10**.
- Geek Squad protection plan: 4 years, ends **2030-10-10** (from the plan document: start 2026-10-10).
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-02-07**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 12 months, 36 or less), so coverage ends **2028-10-10**.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Best Buy, Confirmation, order BBY01-806771, date 2026-10-10, total 1,879.31, 1 item.
- The receipt PDF text: store 0123, order BBY01-806771, 10/10/2026, model OLED65C4PUA, SN 512KCZM9Y447, subtotal 1,796.98, tax 82.33, total 1,879.31, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The plan PDF text: plan GS-91440236 (also on the receipt), model OLED65C4PUA, serial 512KCZM9Y447, Best Buy #0123, 2026-10-10, 4 years to 2030-10-10, $299.99. Its `.jpg` is a render of the same PDF.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
