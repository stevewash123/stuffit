# Scenario 9: Paid with a card that is not on the account

Based on `Scenario 1` (the happy path), with one change: **The receipt shows VISA ending 7777, which is not one of the test client's cards, so no card can be matched and no card benefits apply. (This is the one scenario that does not use the card ending 1111.)**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111) except where noted.

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | WALMART, store 5120, Testville, ME |
| Store in shared data? | Yes: **Walmart**, a shared store |
| Store verified? | Yes. 90 days (30 days electronics, 14 days smartphones), verified 2026-09-30 |
| Order number | WM-2026-81234 |
| Purchase date | 2026-10-12 (Mon 12 Oct 2026) |
| Item | Garmin Forerunner 265 GPS Running Smartwatch |
| Model / serial | 010-02810-00 / 3F7M01428 |
| Item price / tax / total | $449.99 / $24.75 (5.5%) / **$474.74** |
| Payment | VISA ending **7777** |
| Card | VISA ending **7777**: **not on the account** |
| Brand in shared data? | Yes: **Garmin**, a shared brand |
| Brand verified? | Yes. 12 months, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-walmart-garmin-010-02810-00.eml` | Order confirmation (pick-up) | The test mailbox, then a scan |
| 02 | `02-receipt-walmart-garmin-010-02810-00.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |
| 03 | `03-warranty-walmart-garmin-010-02810-00.pdf` or `.jpg` | Manufacturer limited warranty (the two files are the same document; use one) | The item's page, after it is in My Items |

To send the email: from `C:\Projects\StuffIt\Testing\TestEmails`, `python send_scenario.py 9` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email**, then scan. New Items gets one item: Garmin Forerunner 265 GPS Running Smartwatch, order WM-2026-81234, 2026-10-12, $474.74.
2. **Upload the receipt.** It joins the same item. The card on the receipt is VISA ending **7777**: it matches none of the test client's cards (1111, 1212 and 4242 are), so **no card is filled in**.
3. **Add the item to My Items.** The review should show the Walmart return window and the Garmin warranty (12 months, verified) only. No card coverage, because there is no card. The person can pick a card by hand or add 7777 to one.
4. **Upload the warranty** from the item's page (the panel is headed with the file name and says Warranty document).
   - Model number 010-02810-00 matches the item. Nothing to decide.
   - The brand in the document ("Garmin") is the same name as the item's brand. Nothing to decide.
   - The store in the document ("Walmart Supercenter #5120, Testville, ME") matches the purchase. Nothing to decide.
   - Then it asks to add the warranty: watch 1 year. Add it; "Came with the product" is the right origin.

## Expected coverage (dates counted from the purchase date)

- Walmart return window: 90 days, ends **2027-01-10**.
- Garmin manufacturer warranty: 12 months, ends **2027-10-12**.
- No card benefits: the card on the receipt is not on the account.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Walmart, Confirmation, order WM-2026-81234, date 2026-10-12, total 474.74, 1 item.
- The receipt PDF text: store 5120, order WM-2026-81234, 10/12/2026, model 010-02810-00, SN 3F7M01428, subtotal 449.99, tax 24.75, total 474.74, VISA ****7777. Its `.jpg` is a render of the same PDF.
- The warranty PDF text: Garmin Forerunner 265 GPS Running Smartwatch, model 010-02810-00, serial 3F7M01428, purchased from Walmart Supercenter #5120, Testville, ME, 2026-10-12, watch 1 year. Its `.jpg` is a render of the same PDF.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
