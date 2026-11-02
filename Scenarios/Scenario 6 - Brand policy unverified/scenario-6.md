# Scenario 6: The brand is in the shared data, but its policy is not verified

Based on `Scenario 1` (the happy path), with one change: **Sony is a shared brand, but its 12-month audio policy is an unverified placeholder, so the manufacturer warranty from shared data is low confidence until the document confirms it.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | BEST BUY, store 0123, Testville, ME |
| Store in shared data? | Yes: **Best Buy**, a shared store |
| Store verified? | Yes. 15 days (14 days for smartphones), verified 2026-10-22 |
| Order number | BBY01-806412 |
| Purchase date | 2026-10-03 (Sat 03 Oct 2026) |
| Item | Sony WH-1000XM5 Wireless Noise Canceling Headphones, Black |
| Model / serial | WH1000XM5/B / 4829175 |
| Item price / tax / total | $399.99 / $22.00 (5.5%) / **$421.99** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **Sony**, a shared brand |
| Brand verified? | **No.** 12 months for Audio, an unverified placeholder with no source |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-best-buy-sony-wh1000xm5-b.eml` | Order confirmation (pick-up) | The test mailbox, then a scan |
| 02 | `02-receipt-best-buy-sony-wh1000xm5-b.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |
| 03 | `03-warranty-best-buy-sony-wh1000xm5-b.pdf` or `.jpg` | Manufacturer limited warranty (the two files are the same document; use one) | The item's page, after it is in My Items |

To send the email: from `C:\Projects\StuffIt\TestEmails`, `python send_scenario.py 6` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email**, then scan. New Items gets one item: Sony WH-1000XM5 Wireless Noise Canceling Headphones, Black, order BBY01-806412, 2026-10-03, $421.99.
2. **Upload the receipt.** It joins the same item and adds the card (VISA 1111 = Chase Freedom Unlimited).
3. **Add the item to My Items.** The review should show the Best Buy return window (verified), the Sony manufacturer warranty **marked as unverified**, and the card coverage.
4. **Upload the warranty** from the item's page (the panel is headed with the file name and says Warranty document).
   - Model number WH1000XM5/B matches the item. Nothing to decide.
   - The brand in the document ("Sony") is the same name as the item's brand. Nothing to decide.
   - The store in the document ("Best Buy #0123, Testville, ME") matches the purchase. Nothing to decide.
   - Then it asks to add the warranty: headphones 1 year. Add it; "Came with the product" is the right origin.
   - The document says the same as the shared (unverified) policy, so it is offered to the community to help verify it.

## Expected coverage (dates counted from the purchase date)

- Best Buy return window: 15 days, ends **2026-10-18**.
- Sony manufacturer warranty: 12 months, ends **2027-10-03** (unverified placeholder: lower confidence).
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-01-31**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 12 months, 36 or less), so coverage ends **2028-10-03**.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Best Buy, Confirmation, order BBY01-806412, date 2026-10-03, total 421.99, 1 item.
- The receipt PDF text: store 0123, order BBY01-806412, 10/03/2026, model WH1000XM5/B, SN 4829175, subtotal 399.99, tax 22.00, total 421.99, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The warranty PDF text: Sony WH-1000XM5 Wireless Noise Canceling Headphones, model WH1000XM5/B, serial 4829175, purchased from Best Buy #0123, Testville, ME, 2026-10-03, headphones 1 year. Its `.jpg` is a render of the same PDF.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
