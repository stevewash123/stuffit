# Scenario 3: The store is not in the shared data

Based on `Scenario 1` (the happy path), with one change: **The store, Quillfeather Mercantile, is not in the shared data at all, so the app has no return policy for it and the store has to be added to the person's own list.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | QUILLFEATHER MERCANTILE, store 07, Testville, ME |
| Store in shared data? | **No.** Not in the shared data |
| Store verified? | n/a: there is no policy for it |
| Order number | QM-260903-1187 |
| Purchase date | 2026-09-03 (Thu 03 Sep 2026) |
| Item | Makita 18V LXT Brushless 7-1/4 in. Circular Saw (Tool Only) |
| Model / serial | XSH06Z / MK26X4410218 |
| Item price / tax / total | $199.00 / $10.95 (5.5%) / **$209.95** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **Makita**, a shared brand |
| Brand verified? | Yes. 12 months, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-quillfeather-mercantile-makita-xsh06z.eml` | Order confirmation (pick-up) | The test mailbox, then a scan |
| 02 | `02-receipt-quillfeather-mercantile-makita-xsh06z.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |
| 03 | `03-warranty-quillfeather-mercantile-makita-xsh06z.pdf` or `.jpg` | Manufacturer limited warranty (the two files are the same document; use one) | The item's page, after it is in My Items |

To send the email: from `C:\Projects\StuffIt\TestEmails`, `python send_scenario.py 3` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email**, then scan. New Items gets one item: Makita 18V LXT Brushless 7-1/4 in. Circular Saw (Tool Only), order QM-260903-1187, 2026-09-03, $209.95. The store "Quillfeather Mercantile" is **not recognised**, so it shows as store text still to pick.
2. **Upload the receipt.** It joins the same item through the order number and adds the card (VISA 1111 = Chase Freedom Unlimited).
3. **Add the item to My Items.** The store has to be chosen: add "Quillfeather Mercantile" as a new store on the person's own list. The review should show **no return window** (no policy for the store); the brand and card coverage are as listed below.
4. **Upload the warranty** from the item's page (the panel is headed with the file name and says Warranty document).
   - Model number XSH06Z matches the item. Nothing to decide.
   - The brand in the document ("Makita") is the same name as the item's brand. Nothing to decide.
   - The store in the document ("Quillfeather Mercantile #07, Testville, ME") matches the purchase. Nothing to decide.
   - Then it asks to add the warranty: tool 1 year. Add it; "Came with the product" is the right origin.
   - The store is now the person's own, so the warranty's "Quillfeather Mercantile #07" matches it.

## Expected coverage (dates counted from the purchase date)

- Quillfeather Mercantile return window: **none suggested** (the store is not in the shared data, so there is no policy).
- Makita manufacturer warranty: 12 months, ends **2027-09-03**.
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-01-01**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 12 months, 36 or less), so coverage ends **2028-09-03**.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Quillfeather Mercantile, Confirmation, order QM-260903-1187, date 2026-09-03, total 209.95, 1 item.
- The receipt PDF text: store 07, order QM-260903-1187, 09/03/2026, model XSH06Z, SN MK26X4410218, subtotal 199.00, tax 10.95, total 209.95, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The warranty PDF text: Makita 18V LXT Brushless Circular Saw, model XSH06Z, serial MK26X4410218, purchased from Quillfeather Mercantile #07, Testville, ME, 2026-09-03, tool 1 year. Its `.jpg` is a render of the same PDF.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
