# warranties-from-receipts

20 synthetic warranty / protection-plan documents, each built from a receipt in `../receipts/pdf` (named in `index.csv` column `source_receipt`). Purchase facts (store, date, model, serial, plan #, price, term) match the receipt; coverage details, exclusions, fees and claim steps are invented additions. `index.csv` gives the expected reading and a `confidence` for how fully the receipt pins it down.

| Group | Files | Receipt says |
|---|---|---|
| Retailer plan named on receipt | 01-10 | plan name, term, usually plan # and serial (05, 06, 09, 10 lack a plan #; 09 also lacks serial and start date) |
| Manufacturer warranty on receipt | 11-17 | one line such as "2 YR MFR WARRANTY", "7 YR COMPRESSOR / 5 YR PARTS" |
| No warranty on receipt | 18-20 | nothing; item is likely to carry a standard manufacturer warranty |

Separate from `../warranties` (generic fixtures with no receipt tie).
