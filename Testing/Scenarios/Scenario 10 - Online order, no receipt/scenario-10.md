# Scenario 10: An online order with no receipt: three emails and the warranty

Based on `Scenario 1` (the happy path), with one change: **There is no receipt. It was bought online and shipped, so the purchase is built from the order, shipping and delivery emails alone.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | Amazon.com (online) |
| Store in shared data? | Yes: **Amazon**, a shared store |
| Store verified? | Yes. 30 days, verified 2026-09-30 |
| Order number | 113-4471209-3380912 |
| Purchase date | 2026-10-05 (Mon 05 Oct 2026); delivered 2026-10-09 |
| Item | Dyson V15 Detect Cordless Vacuum |
| Model / serial | SV47 / DY26V1520094 |
| Item price / tax / total | $649.99 / $35.75 (5.5%) / **$685.74** |
| Payment | No payment on the emails (an online order shows only the total). |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **Dyson**, a shared brand |
| Brand verified? | Yes. 24 months for Vacuums, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-amazon-dyson-sv47.eml` | Order confirmation (online order) | The test mailbox, then a scan |
| 02 | `02-email-shipped-amazon-dyson-sv47.eml` | Shipping email | The test mailbox, then a scan |
| 03 | `03-email-delivered-amazon-dyson-sv47.eml` | Delivery email | The test mailbox, then a scan |
| 04 | `04-warranty-amazon-dyson-sv47.pdf` or `.jpg` | Manufacturer limited warranty (the two files are the same document; use one) | The item's page, after it is in My Items |

To send the emails: from `C:\Projects\StuffIt\Testing\TestEmails`, `python send_scenario.py 10` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the three emails** in order (order, shipped, delivered), then scan. New Items gets **one** item, not three: Dyson V15 Detect Cordless Vacuum, from Amazon, order 113-4471209-3380912, ordered 2026-10-05, $685.74; the shipping and delivery emails update it (delivered 2026-10-09).
2. There is **no receipt** to upload. The emails give no card, serial or payment details; the person adds the card (Chase Freedom Unlimited) on the review.
3. **Add the item to My Items.** The review should show the Amazon return window (30 days, from the purchase date), the Dyson warranty from shared data (24 months), and, once the card is chosen, the card coverage.
4. **Upload the warranty** from the item's page (the panel is headed with the file name and says Warranty document).
   - Model number SV47 matches the item. Nothing to decide.
   - The brand in the document ("Dyson") is the same name as the item's brand. Nothing to decide.
   - The store in the document ("Amazon.com, order 113-4471209-3380912") matches the purchase. Nothing to decide.
   - Then it asks to add the warranty: machine 2 years. Add it; "Came with the product" is the right origin.
   - The document says it was bought from Amazon.com, order 113-4471209-3380912.

## Expected coverage (dates counted from the purchase date)

- Amazon return window: 30 days, ends **2026-11-04**.
- Dyson manufacturer warranty: 24 months, ends **2028-10-05**.
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-02-02**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 24 months, 36 or less), so coverage ends **2029-10-05**.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Amazon.com, Confirmation, order 113-4471209-3380912, date 2026-10-05, total 685.74, 1 item.
- The shipped email read by the plain parser: stage Shipped, order 113-4471209-3380912 (like every follow-up email it has no items or total, so it only updates the order).
- The delivered email read by the plain parser: stage Delivered, order 113-4471209-3380912 (like every follow-up email it has no items or total, so it only updates the order).
- The warranty PDF text: Dyson V15 Detect Cordless Vacuum, model SV47, serial DY26V1520094, purchased from Amazon.com, order 113-4471209-3380912, 2026-10-05, machine 2 years. Its `.jpg` is a render of the same PDF.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
