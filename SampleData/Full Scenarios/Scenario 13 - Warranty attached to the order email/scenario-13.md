# Scenario 13: The warranty arrives attached to the order email

Based on `Scenario 1` (the happy path), with one change: **The order email has the manufacturer's warranty PDF attached, so the warranty has to be sorted out as a warranty, not read as a receipt.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | WALMART, store 5120, Testville, ME |
| Store in shared data? | Yes: **Walmart**, a shared store |
| Store verified? | Yes. 90 days (30 days electronics, 14 days smartphones), verified 2026-09-30 |
| Order number | WM-2026-82067 |
| Purchase date | 2026-10-15 (Thu 15 Oct 2026) |
| Item | Makita 18V LXT Brushless Cordless 1/4 in. Impact Driver (Tool Only) |
| Model / serial | XDT16Z / MK26I8830412 |
| Item price / tax / total | $149.00 / $8.20 (5.5%) / **$157.20** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **Makita**, a shared brand |
| Brand verified? | Yes. 12 months, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-walmart-makita-xdt16z.eml` | Order confirmation (pick-up) | The test mailbox, then a scan |
| 02 | `02-receipt-walmart-makita-xdt16z.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |
| 03 | `03-warranty-walmart-makita-xdt16z.pdf` and `.jpg` | The manufacturer limited warranty that is attached to the email (a reference copy, and its image) | Nowhere: it is already attached to the email. Do not upload it |

To send the email: from `C:\Projects\StuffIt\TestEmails`, `python send_scenario.py 13` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email**, then run Check Emails. New Items gets one item from the order email: Makita 18V LXT Brushless Cordless 1/4 in. Impact Driver (Tool Only), order WM-2026-82067, 2026-10-15, $157.20. The email has the Makita warranty PDF attached.
2. Open the item: it holds **two documents**, the email and the attached warranty. The warranty is **not** read as a receipt: the item is still the order, and the warranty appears as a coverage to check on the item (Makita, 1 year, "your document").
3. **Upload the receipt** in New Items. It joins the same item through the order number and adds the card (VISA 1111 = Chase Freedom Unlimited).
4. **Add the item to My Items.** The review should show the Walmart return window, the Makita manufacturer warranty (it comes from your document and agrees with the shared 12 months), and the card coverage. There is nothing to upload from the item's page.

## Expected coverage (dates counted from the purchase date)

- Walmart return window: 90 days, ends **2027-01-13**.
- Makita manufacturer warranty: 12 months, ends **2027-10-15**.
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-02-12**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 12 months, 36 or less), so coverage ends **2028-10-15**.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Walmart, Confirmation, order WM-2026-82067, date 2026-10-15, total 157.20, 1 item.
- The receipt PDF text: store 5120, order WM-2026-82067, 10/15/2026, model XDT16Z, SN MK26I8830412, subtotal 149.00, tax 8.20, total 157.20, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The warranty PDF text: Makita 18V LXT Brushless Impact Driver, model XDT16Z, serial MK26I8830412, purchased from Walmart Supercenter #5120, Testville, ME, 2026-10-15, tool 1 year. Its `.jpg` is a render of the same PDF.
- The warranty PDF attached to the email (text): Makita 18V LXT Brushless Impact Driver, model XDT16Z, serial MK26I8830412, purchased from Walmart Supercenter #5120, Testville, ME, 2026-10-15, tool 1 year. It is attached to the email as `Makita-limited-warranty.pdf`.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
