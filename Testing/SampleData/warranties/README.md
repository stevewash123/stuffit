# warranties - warranty document fixtures

Test inputs for reading warranty documents (manufacturer warranties, protection plans, retailer policies, card benefits). `index.csv` has one row per file with what a correct reading should find (`expected`) and what is tricky about it (`parser_notes`).

All 17 files are **synthetic**: fictitious products, names (Sam Sample), model and serial numbers, phone numbers and dates. Three use real brand names (Samsung, Milwaukee, Penn) so brand matching against the reference data can be tested; their wording is invented and is not a copy of any real warranty. Every file says it is a sample. PDFs are rendered from HTML with headless Chrome; the one image is a rotated, slightly blurred render.

Dates are arbitrary; some fall after the folder was built.

## Standard format (baseline: one clear answer each)

| File | What it is | Expected reading |
|---|---|---|
| `standard-appliance-limited-warranty.pdf` | Samsung refrigerator, tiered table | 1y parts and labor, 5y sealed system parts, 10y compressor; starts at purchase |
| `standard-power-tool-5yr.pdf` | Milwaukee hammer drill | 5y tool, 3y battery and charger; registration optional |
| `standard-lifetime-limited-reel.pdf` | Penn fishing reel | Lifetime of the product (no end date); original purchaser only |
| `standard-headphones-limited-warranty.pdf`<br>`standard-router-limited-warranty.pdf`<br>`standard-vacuum-limited-warranty.pdf`<br>`standard-blender-limited-warranty.pdf` | Same template four times (Brightwave, Northlink, Cleanstream, Kitchenpro) | Only brand, model, term (12 or 24 months) and purchase date change. For bulk correctness checks and for confirming the reader does not depend on one layout |

## Multi-item (one document, several products)

| File | Expected reading |
|---|---|
| `multi-item-protection-plan.pdf` | Third-party plan covering a TV, soundbar and streaming player: terms 4y / 3y / 2y, deductibles $0 / $25 / $25. The plan price ($289.99) is not an item price. Terms say "from May 14, 2026" but coverage begins when each manufacturer warranty ends: a conflict to flag, not guess |
| `multi-item-kitchen-suite-warranty.pdf` | Four appliances, each with a full term and a longer limited term (range, dishwasher, microwave, refrigerator). Start is the installation date, or purchase plus 6 months if installation is not documented, whichever is first |

## Edge cases

| File | What makes it hard |
|---|---|
| `edge-registration-required.pdf` | 90 days, or 3 years only if registered within 30 days of purchase. The right answer depends on something the person may not have done: ask, do not assume 3 years |
| `edge-starts-at-manufacture-date.pdf` | Term is 24 months from the date of manufacture, which is encoded in the serial number (AF 2512 = December 2025), with a minimum of 6 months from sale. Needs the serial to compute an end date |
| `edge-delivery-date-and-ddmmyyyy.pdf` | Day/month/year dates (03/04/2026 is April 3), start is delivery not order, some German text, and a statutory-rights sentence that is not a term |
| `edge-used-item-30-day-dealer.pdf` | 30-day dealer warranty, then AS IS (no warranty). Manufacturer warranty not transferred. Battery excluded. Capital letters |
| `edge-card-extended-warranty-benefit.pdf` | Not a product warranty but a card benefit that adds up to one year to other warranties of 3 years or less. Caps and exclusions. Depends on which card paid, which matters for the funding-card and PayPal cases |
| `edge-exclusions-and-voiding-conditions.pdf` | 2y residential or 90 days commercial, wear items 30 days, voided by missing oil-change records or high-ethanol fuel, original purchaser only. Must be summarized, not reduced to "2 years" |
| `retailer-return-and-store-warranty.pdf` | A return policy, which is not a warranty: 30 days by default, 14 days for big TVs, computers and cameras, final sale categories, a holiday extension to January 31, a 15% restocking fee, and a separate 90-day store warranty |
| `edge-photo-of-warranty-card.png` | An image, not a PDF: rotated and slightly blurred card (Peakline circular saw, serial 0048821, 2 years, bought 07/19/2026). The dealer stamp repeats the date and is not the manufacturer |

## Not yet covered (ideas for later)
Scanned multi-page PDF with a signature page, a warranty in a non-English language only, a recall notice, a lease or subscription with a service guarantee, and a warranty document that is a web page or email rather than a file.
