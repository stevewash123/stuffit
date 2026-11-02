# Scenario 5: The store is in the shared data, but its policy is not verified

Based on `Scenario 1` (the happy path), with one change: **Kohl's is a shared store, but its 30-day return window is an unverified placeholder, so the return window should be suggested with lower confidence.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | KOHL'S, store 0614, Testville, ME |
| Store in shared data? | Yes: **Kohl's**, a shared store |
| Store verified? | **No.** 30 days, an unverified placeholder with no source |
| Order number | KH-26-88413 |
| Purchase date | 2026-09-26 (Sat 26 Sep 2026) |
| Item | KitchenAid Artisan 5-Qt Tilt-Head Stand Mixer |
| Model / serial | KSM150PSER / KA26M2203911 |
| Item price / tax / total | $329.99 / $18.15 (5.5%) / **$348.14** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **KitchenAid**, a shared brand |
| Brand verified? | Yes. 12 months for Small appliances, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-kohls-kitchenaid-ksm150pser.eml` | Order confirmation (pick-up) | The test mailbox, then a scan |
| 02 | `02-receipt-kohls-kitchenaid-ksm150pser.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |
| 03 | `03-warranty-kohls-kitchenaid-ksm150pser.pdf` or `.jpg` | Manufacturer limited warranty (the two files are the same document; use one) | The item's page, after it is in My Items |

To send the email: from `C:\Projects\StuffIt\Testing\TestEmails`, `python send_scenario.py 5` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email**, then scan. New Items gets one item: KitchenAid Artisan 5-Qt Tilt-Head Stand Mixer, order KH-26-88413, 2026-09-26, $348.14.
2. **Upload the receipt.** It joins the same item and adds the card (VISA 1111 = Chase Freedom Unlimited).
3. **Add the item to My Items.** The review should show the Kohl's return window **marked as unverified** (lower confidence than a verified one), plus the verified KitchenAid warranty and the card coverage.
4. **Upload the warranty** from the item's page (the panel is headed with the file name and says Warranty document).
   - Model number KSM150PSER matches the item. Nothing to decide.
   - The brand in the document ("KitchenAid") is the same name as the item's brand. Nothing to decide.
   - The store in the document ("Kohl's #0614, Testville, ME") matches the purchase. Nothing to decide.
   - Then it asks to add the warranty: mixer 1 year. Add it; "Came with the product" is the right origin.

## Expected coverage (dates counted from the purchase date)

- Kohl's return window: 30 days, ends **2026-10-26** (unverified placeholder: lower confidence).
- KitchenAid manufacturer warranty: 12 months, ends **2027-09-26**.
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-01-24**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 12 months, 36 or less), so coverage ends **2028-09-26**.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Kohl's, Confirmation, order KH-26-88413, date 2026-09-26, total 348.14, 1 item.
- The receipt PDF text: store 0614, order KH-26-88413, 09/26/2026, model KSM150PSER, SN KA26M2203911, subtotal 329.99, tax 18.15, total 348.14, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The warranty PDF text: KitchenAid Artisan 5-Qt Tilt-Head Stand Mixer, model KSM150PSER, serial KA26M2203911, purchased from Kohl's #0614, Testville, ME, 2026-09-26, mixer 1 year. Its `.jpg` is a render of the same PDF.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
