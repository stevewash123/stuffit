# Scenario 12: The receipt arrives as a PDF attached to the email

Based on `Scenario 1` (the happy path), with one change: **The email has no order details in its body: the receipt is a PDF attached to it, and what the item is, costs and was paid with has to come from the attachment.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | THE HOME DEPOT, store 0417, Testville, ME |
| Store in shared data? | Yes: **Home Depot**, a shared store |
| Store verified? | Yes. Return policy 90 days, verified 2026-09-30 (homedepot.com/c/Return_Policy) |
| Order number | none printed (register transaction 0417 1014 5532 only) |
| Purchase date | 2026-10-14 (Wed 14 Oct 2026) |
| Item | DEWALT 20V MAX XR Brushless Drill/Driver Kit |
| Model / serial | DCD791D2 / DW26D2209145 |
| Item price / tax / total | $179.00 / $9.85 (5.5%) / **$188.85** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **DeWalt**, a shared brand |
| Brand verified? | Yes. 36 months for Power tools, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-attached-home-depot-dewalt-dcd791d2.eml` | Receipt email with the receipt PDF attached (nothing about the order is in its body) | The test mailbox, then a scan |
| 02 | `02-receipt-home-depot-dewalt-dcd791d2.pdf` and `.jpg` | The receipt that is attached to the email (a reference copy, and its image) | Nowhere: it is already attached to the email. Do not upload it |
| 03 | `03-warranty-home-depot-dewalt-dcd791d2.pdf` or `.jpg` | Manufacturer limited warranty (the two files are the same document; use one) | The item's page, after it is in My Items |

To send the email: from `C:\Projects\StuffIt\TestEmails`, `python send_scenario.py 12` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email** (`python send_scenario.py 12`), then run Check Emails. The email body says only that the receipt is attached, so New Items gets **one** item made from the email and the attachment together: The Home Depot, 2026-10-14, DEWALT 20V MAX XR Brushless Drill/Driver Kit, model DCD791D2, price $179.00, total **$188.85**, card VISA 1111 = **Chase Freedom Unlimited**.
2. Open the item: it holds **two documents**, the email and the attached receipt PDF. Nothing is uploaded by hand.
3. **Add the item to My Items.** The review should propose the coverage listed below.
4. **Upload the warranty** from the item's page (the panel is headed with the file name and says Warranty document).
   - Model number DCD791D2 matches the item. Nothing to decide.
   - The brand in the document ("DEWALT") is the same name as the item's brand. Nothing to decide.
   - The store in the document ("The Home Depot #0417, Testville, ME") matches the purchase. Nothing to decide.
   - Then it asks to add the warranty: tool 3 years. Add it; "Came with the product" is the right origin.

## Expected coverage (dates counted from the purchase date)

- Home Depot return window: 90 days, ends **2027-01-12**.
- DeWalt manufacturer warranty: 36 months, ends **2029-10-14**.
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-02-11**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 36 months, 36 or less), so coverage ends **2030-10-14**.

## Checked when this was made

- The email read by the plain email parser (no model): Thin, as expected: store The Home Depot, stage Receipt, but no items, total, date or order number (all of those have to come from the attachment). The PDF attached to it is the receipt in this folder, 42,392 bytes.
- The receipt PDF text: store 0417, 10/14/2026, model DCD791D2, SN DW26D2209145, subtotal 179.00, tax 9.85, total 188.85, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The warranty PDF text: DEWALT 20V MAX XR Brushless Drill/Driver Kit, model DCD791D2, serial DW26D2209145, purchased from The Home Depot #0417, Testville, ME, 2026-10-14, tool 3 years. Its `.jpg` is a render of the same PDF.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
