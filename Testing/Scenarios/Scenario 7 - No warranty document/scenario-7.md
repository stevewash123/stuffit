# Scenario 7: No warranty document: the manufacturer warranty comes from shared data

Based on `Scenario 1` (the happy path), with one change: **There is no warranty document. The manufacturer warranty can only come from the shared data.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | WALMART, store 5120, Testville, ME |
| Store in shared data? | Yes: **Walmart**, a shared store |
| Store verified? | Yes. 90 days (30 days electronics, 14 days smartphones), verified 2026-09-30 |
| Order number | WM-2026-77120 |
| Purchase date | 2026-10-08 (Thu 08 Oct 2026) |
| Item | BLACK+DECKER 20V MAX Cordless Hedge Trimmer |
| Model / serial | LHT2220 / BD26H5520377 |
| Item price / tax / total | $99.00 / $5.45 (5.5%) / **$104.45** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **Black+Decker**, a shared brand |
| Brand verified? | Yes. 24 months for Power tools, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-walmart-blackdecker-lht2220.eml` | Order confirmation (pick-up) | The test mailbox, then a scan |
| 02 | `02-receipt-walmart-blackdecker-lht2220.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |

To send the email: from `C:\Projects\StuffIt\Testing\TestEmails`, `python send_scenario.py 7` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email**, then scan. New Items gets one item: BLACK+DECKER 20V MAX Cordless Hedge Trimmer, order WM-2026-77120, 2026-10-08, $104.45.
2. **Upload the receipt.** It joins the same item and adds the card (VISA 1111 = Chase Freedom Unlimited).
3. **Add the item to My Items.** The review should show the Walmart return window, the Black+Decker warranty from the **shared data** (24 months, verified), and the card coverage.
4. There is no warranty document to upload. The item stays on the shared-data warranty; nothing on the item page asks about one.

## Expected coverage (dates counted from the purchase date)

- Walmart return window: 90 days, ends **2027-01-06**.
- Black+Decker manufacturer warranty: 24 months, ends **2028-10-08**.
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-02-05**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 24 months, 36 or less), so coverage ends **2029-10-08**.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Walmart, Confirmation, order WM-2026-77120, date 2026-10-08, total 104.45, 1 item.
- The receipt PDF text: store 5120, order WM-2026-77120, 10/08/2026, model LHT2220, SN BD26H5520377, subtotal 99.00, tax 5.45, total 104.45, VISA ****1111. Its `.jpg` is a render of the same PDF.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
