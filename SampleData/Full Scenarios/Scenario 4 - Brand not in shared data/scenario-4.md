# Scenario 4: The brand is not in the shared data

Based on `Scenario 1` (the happy path), with one change: **The brand, Hexaquill, is not in the shared data, so there is no manufacturer policy to suggest; the only source for its warranty is the warranty document.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | TARGET, store 2284, Testville, ME |
| Store in shared data? | Yes: **Target**, a shared store |
| Store verified? | Yes. 90 days (30 days for electronics), verified 2026-10-22 |
| Order number | TGT-4471903 |
| Purchase date | 2026-09-19 (Sat 19 Sep 2026) |
| Item | Hexaquill 12V Cordless Screwdriver Set |
| Model / serial | HX-SD12 / HQ26S900144 |
| Item price / tax / total | $34.99 / $1.92 (5.5%) / **$36.91** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | **No.** Not in the shared data |
| Brand verified? | n/a: there is no policy for it |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-target-hexaquill-hx-sd12.eml` | Order confirmation (pick-up) | The test mailbox, then a scan |
| 02 | `02-receipt-target-hexaquill-hx-sd12.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |
| 03 | `03-warranty-target-hexaquill-hx-sd12.pdf` or `.jpg` | Manufacturer limited warranty (the two files are the same document; use one) | The item's page, after it is in My Items |

To send the email: from `C:\Projects\StuffIt\TestEmails`, `python send_scenario.py 4` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email**, then scan. New Items gets one item: Hexaquill 12V Cordless Screwdriver Set, order TGT-4471903, 2026-09-19, $36.91. The brand "Hexaquill" is **not recognised**.
2. **Upload the receipt.** It joins the same item and adds the card (VISA 1111 = Chase Freedom Unlimited).
3. **Add the item to My Items.** The brand has to be chosen: add "Hexaquill" as a new brand on the person's own list. The review should show the Target return window and the card coverage, but **no manufacturer warranty** (nothing to suggest from).
4. **Upload the warranty** from the item's page.
   - Model number HX-SD12 and the store match. The brand matches the brand just added. Nothing to decide.
   - It asks to add the warranty: tool 2 years, battery 1 year. Add it. It is kept on the item only: the brand is not in the shared data, so there is nothing to offer to the community.

## Expected coverage (dates counted from the purchase date)

- Target return window: 90 days, ends **2026-12-18**.
- Hexaquill manufacturer warranty: **only from the document**: 24 months, ends **2028-09-19** (nothing in shared data to suggest it).
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-01-17**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 24 months, 36 or less), so coverage ends **2029-09-19**.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Target, Confirmation, order TGT-4471903, date 2026-09-19, total 36.91, 1 item.
- The receipt PDF text: store 2284, order TGT-4471903, 09/19/2026, model HX-SD12, SN HQ26S900144, subtotal 34.99, tax 1.92, total 36.91, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The warranty PDF text: Hexaquill 12V Cordless Screwdriver Set, model HX-SD12, serial HQ26S900144, purchased from Target #2284, Testville, ME, 2026-09-19, tool 2 years. Its `.jpg` is a render of the same PDF.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
