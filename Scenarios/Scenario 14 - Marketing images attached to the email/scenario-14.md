# Scenario 14: Marketing and branding images come with the order email

Based on `Scenario 1` (the happy path), with one change: **The order email carries a logo (embedded), a promotional banner and an app-store badge. None of them is a document, so none should be read or kept.**

Use the **test client** (`stevewash123.test@gmail.com`) with My Items and New Items empty. Everything else follows the happy path: the card is the test client's Chase Freedom Unlimited (ending 1111).

## The purchase (answer key)

| Fact | Value |
|---|---|
| Store (as printed) | WALMART, store 5120, Testville, ME |
| Store in shared data? | Yes: **Walmart**, a shared store |
| Store verified? | Yes. 90 days (30 days electronics, 14 days smartphones), verified 2026-09-30 |
| Order number | WM-2026-82351 |
| Purchase date | 2026-10-16 (Fri 16 Oct 2026) |
| Item | DEWALT 20V MAX Cordless Drill and Impact Driver Combo Kit |
| Model / serial | DCK240C2 / DW26K5550183 |
| Item price / tax / total | $199.00 / $10.95 (5.5%) / **$209.95** |
| Payment | VISA ending **1111** |
| Card | VISA ending **1111** = **Chase Freedom Unlimited** (current). Benefits verified 2026-09-30: purchase protection 120 days up to $500 per item; extended warranty +12 months on manufacturer warranties of 3 years or less |
| Brand in shared data? | Yes: **DeWalt**, a shared brand |
| Brand verified? | Yes. 36 months for Power tools, verified 2026-09-30 (human-searched source) |
| Purchased by | Sam Sample |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 01 | `01-email-order-walmart-dewalt-dck240c2.eml` | Order confirmation (pick-up) | The test mailbox, then a scan |
| 02 | `02-receipt-walmart-dewalt-dck240c2.pdf` or `.jpg` | Register receipt (the two files are the same receipt; use one) | New Items, Upload a receipt or warranty |
|  | `04-marketing-logo-embedded.png` | The store logo, embedded in the email body (a reference copy) | Nowhere: it is part of the email. Do not upload it |
|  | `05-marketing-spring-sale-banner.jpg` | A promotional banner, attached to the email (a reference copy) | Nowhere: it is part of the email. Do not upload it |
|  | `06-marketing-app-store-badge.png` | An app-store badge, attached to the email (a reference copy) | Nowhere: it is part of the email. Do not upload it |

To send the email: from `C:\Projects\StuffIt\TestEmails`, `python send_scenario.py 14` (it asks for the Gmail app password), then run Check Emails.

## Steps and what should happen

1. **Send the email**, then run Check Emails. New Items gets one item from the order email: DEWALT 20V MAX Cordless Drill and Impact Driver Combo Kit, order WM-2026-82351, 2026-10-16, $209.95.
2. Open the item: its documents are **only the email**. The embedded logo is not looked at; the banner and the app-store badge are written out, sorted as "other" (not a document), and not kept.
3. **Upload the receipt** in New Items. It joins the same item through the order number and adds the card (VISA 1111 = Chase Freedom Unlimited).
4. **Add the item to My Items.** The review should show the Walmart return window, the DeWalt warranty from shared data (36 months, verified), and the card coverage. No warranty document in this scenario.

## Expected coverage (dates counted from the purchase date)

- Walmart return window: 90 days, ends **2027-01-14**.
- DeWalt manufacturer warranty: 36 months, ends **2029-10-16**.
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-02-13**.
- Chase Freedom Unlimited extended warranty: adds 12 months to the manufacturer warranty (it is 36 months, 36 or less), so coverage ends **2030-10-16**.

## Checked when this was made

- The order email read by the plain email parser (no model): Ok, store Walmart, Confirmation, order WM-2026-82351, date 2026-10-16, total 209.95, 1 item.
- The receipt PDF text: store 5120, order WM-2026-82351, 10/16/2026, model DCK240C2, SN DW26K5550183, subtotal 199.00, tax 10.95, total 209.95, VISA ****1111. Its `.jpg` is a render of the same PDF.
- The three images were made for this scenario: a logo (embedded in the body with a Content-ID), a promotional banner and an app-store badge, each larger than the 4 KB the app looks at. The text on them is only branding and a sale slogan.
- Shared data (store, brand, policies, card, last four) read from the development database on 2026-10-24.
- The steps and the coverage are what the shared data and the documents say should happen. They have not been run through the app yet.
