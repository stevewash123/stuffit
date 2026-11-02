# Scenario 11: The warranty document is for a different model

Based on `Scenario 1` (the happy path), with one change: **The warranty document uploaded belongs to a different model (LDX120C) than the item bought (LD120VA), so the app should flag it and the person should reject it.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | LOWE'S, store 1832, Testville, ME |
| Store in shared data? | Yes: **Lowe's**, a shared store |
| Store verified? | Yes. Return policy 90 days, verified 2026-09-30 (lowes.com/l/help/returns-policy). The 2-day policy is for major appliances only |
| Order number | LW-48213 |
| Purchase date | 2026-09-28 (Mon 28 Sep 2026) |
| Item | BLACK+DECKER 20V MAX Cordless Drill/Driver |
| Model / serial | LD120VA / BD26D4410552 |
| Item price / tax / total | $49.99 / $2.75 (5.5%) / **$52.74** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **Black+Decker**, a shared brand |
| Brand verified? | Yes. 24 months for Power tools, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-lowes-blackdecker-ld120va.eml` | Order confirmation (pick-up) | The test mailbox, then a scan |
| 02 | `02-receipt-lowes-blackdecker-ld120va.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |
| 03 | `03-warranty-lowes-blackdecker-ld120va.pdf` or `.jpg` | Manufacturer limited warranty (the two files are the same document; use one) | The item's page, after it is in My Items |

To send the email: from `C:\Projects\StuffIt\Testing\TestEmails`, `python send_scenario.py 11` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email**, then scan. New Items gets one item: BLACK+DECKER 20V MAX Cordless Drill/Driver, order LW-48213, 2026-09-28, $52.74.
2. **Upload the receipt.** It joins the same item and adds the card (VISA 1111 = Chase Freedom Unlimited).
3. **Add the item to My Items.** The review should show the Lowe's return window, the Black+Decker warranty from shared data (24 months), and the card coverage.
4. **Upload the warranty** from the item's page. It is for model **LDX120C** (a drill with two batteries, serial BD26D7790318), not **LD120VA** (serial BD26D4410552).
   - The panel shows the model number as a **conflict** (red card): keep yours (LD120VA) or use the document's (LDX120C).
   - It then asks "This document looks like it is for a different item ... Add it anyway?". The right answer is **Not now**, or **Reject this document** on the panel: nothing from it is used or kept, and the item keeps the shared-data warranty.

## Expected coverage (dates counted from the purchase date)

- Lowe's return window: 90 days, ends **2026-12-27**.
- Black+Decker manufacturer warranty: 24 months, ends **2028-09-28**.
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-01-26**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 24 months, 36 or less), so coverage ends **2029-09-28**.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Lowe's, Confirmation, order LW-48213, date 2026-09-28, total 52.74, 1 item.
- The receipt PDF text: store 1832, order LW-48213, 09/28/2026, model LD120VA, SN BD26D4410552, subtotal 49.99, tax 2.75, total 52.74, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The warranty PDF text: BLACK+DECKER 20V MAX Cordless Drill/Driver with 2 batteries, model LDX120C, serial BD26D7790318, purchased from Lowe's Home Improvement #1832, Testville, ME, 2026-09-28, tool 2 years. Its `.jpg` is a render of the same PDF.
- The warranty is deliberately for another model: LDX120C, serial BD26D7790318 (the item is LD120VA, serial BD26D4410552).
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
