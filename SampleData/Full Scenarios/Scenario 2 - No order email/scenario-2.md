# Scenario 2: No order confirmation email: the receipt is the first thing in

Based on `Scenario 1` (the happy path), with one change: **There is no order confirmation email. The register receipt, uploaded in New Items, is what creates the item.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | LOWE'S, store 1832, Testville, ME |
| Store in shared data? | Yes: **Lowe's**, a shared store |
| Store verified? | Yes. Return policy 90 days, verified 2026-09-30 (lowes.com/l/help/returns-policy). The 2-day policy is for major appliances only |
| Order number | none printed (register transaction 1832 0822 5510 only) |
| Purchase date | 2026-08-22 (Sat 22 Aug 2026) |
| Item | DEWALT 20V MAX Brushless 6-1/2 in. Circular Saw (Tool Only) |
| Model / serial | DCS565B / DW26B1177403 |
| Item price / tax / total | $149.00 / $8.20 (5.5%) / **$157.20** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **DeWalt**, a shared brand |
| Brand verified? | Yes. 36 months for Power tools, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-receipt-lowes-dewalt-dcs565b.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |
| 02 | `02-warranty-lowes-dewalt-dcs565b.pdf` or `.jpg` | Manufacturer limited warranty (the two files are the same document; use one) | The item's page, after it is in My Items |

## Steps and what should happen

1. **Upload the receipt** in New Items. There is no email, so the receipt makes the item by itself: DEWALT 20V MAX Brushless 6-1/2 in. Circular Saw (Tool Only), from Lowe's, 2026-08-22, $149.00 (total **$157.20**), model DCS565B, card VISA 1111 = **Chase Freedom Unlimited**. The receipt has no order number (it was a walk-in sale), so nothing is joined to it.
2. Check New Items has **one** item and it already has the card and the store (no store to pick).
3. **Add the item to My Items.** The review should propose the coverage listed below.
4. **Upload the warranty** from the item's page (the panel is headed with the file name and says Warranty document).
   - Model number DCS565B matches the item. Nothing to decide.
   - The brand in the document ("DEWALT") is the same name as the item's brand. Nothing to decide.
   - The store in the document ("Lowe's Home Centers #1832, Testville, ME") matches the purchase. Nothing to decide.
   - Then it asks to add the warranty: tool 3 years. Add it; "Came with the product" is the right origin.

## Expected coverage (dates counted from the purchase date)

- Lowe's return window: 90 days, ends **2026-11-20**.
- DeWalt manufacturer warranty: 36 months, ends **2029-08-22**.
- Chase Freedom Unlimited purchase protection: 120 days, ends **2026-12-20**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 36 months, 36 or less), so coverage ends **2030-08-22**.

## Checked when this was made

- The receipt PDF text: store 1832, 08/22/2026, model DCS565B, SN DW26B1177403, subtotal 149.00, tax 8.20, total 157.20, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The warranty PDF text: DEWALT 20V MAX Brushless Circular Saw, model DCS565B, serial DW26B1177403, purchased from Lowe's Home Centers #1832, Testville, ME, 2026-08-22, tool 3 years. Its `.jpg` is a render of the same PDF.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
