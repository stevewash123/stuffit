# SampleData - receipt and order-email fixtures

Test inputs for the warranty tracker's receipt/email parser. See `index.csv` (one row per file: path, retailer, kind, channel_hint, source_url, license_notes, parser_notes).

See `INVENTORY.md` for which files belong together (same item, maker, store, returns). It is generated: `node _tools/make-inventory.js`.

## Layout
- `emails/order-confirmation`, `emails/shipping`, `emails/delivery` - retailer order lifecycle emails (.eml, multipart text+html).
- `emails/e-receipt` - emailed copies of in-store register receipts (store #, register, trans, card last 4), plus return/exchange receipts and two real MIT-licensed SaaS receipt templates (.html).
- `receipts/paper-photo` - photos/scans of paper receipts (.jpg).
- `receipts/pdf` - PDF invoices/receipts.
- `warranties` - warranty documents: standard manufacturer warranties, repetitive same-template ones, multi-item plans, retailer policies, a card benefit, and edge cases. Described file by file in `warranties/README.md`, with expected readings in `warranties/index.csv`.

## Provenance (61 files)
- **Synthetic (49):** all retailer emails and PDFs. Fictitious names ("Sam Sample"), addresses (Testville, ME), order/tracking numbers, card last-4s. Layout, field order, order-number formats, and wording are modeled on each retailer's public email style, but they are NOT copies of real messages. Every .eml carries an `X-Synthetic-Sample` header and an HTML comment; PDFs carry an HTML comment in the source. Real retailer templates are copyrighted, so exact wording/branding assets are deliberately not reproduced. Verify any format assumption against a real email before relying on it.
- **Real, openly licensed (12):**
  - 2 Postmark transactional receipt templates (MIT, (c) 2015 Wildbit) with placeholders filled with fictitious data - https://github.com/ActiveCampaign/postmark-templates
  - 6 paper receipt photos from Wikimedia Commons (Target 2018, Walmart x3, Uniqlo Taiwan, Fanzz 2002): CC BY-SA 4.0 or public domain; attribution links in `index.csv`. CC BY-SA requires attribution and share-alike if redistributed.
  - 4 receipt photos from CORD v2 (NAVER Clova), CC BY 4.0, https://huggingface.co/datasets/naver-clova-ix/cord-v2 (already blurred by the dataset authors; Indonesian receipts).
- No real person's receipt or email is included. No scrubbed public posts were used (none could be fetched without login/blocking).

## Notes
- Images are downsized copies of the originals (max 2000-2400 px). Some photos are deliberately left rotated/crumpled as OCR stress tests.
- Some synthetic dates fall in late 2026 (after the folder was built); treat dates as arbitrary.
- Tracking numbers and order numbers are fake and use real-looking formats only.

## Layout
- `emails/`, `receipts/`, `warranties/`, `warranties-from-receipts/` and the `*-photo` twins: the sample documents themselves. Pure data; the API seeder (`--seed-demo`, `--seed-new-items`) and the reader harness read this layout, so do not rename.
- `index.csv`, `INVENTORY.md`: the key and the generated inventory.
- `_tools/`: scripts that generate files here (`make-inventory.js`, `make-order-pair-receipts.py`, `make-photo-twins.py`, `make-test-matrix.js`).
- Scenario walkthroughs, runners and results live in `../Scenarios/` (both under `Testing/`), not here.
