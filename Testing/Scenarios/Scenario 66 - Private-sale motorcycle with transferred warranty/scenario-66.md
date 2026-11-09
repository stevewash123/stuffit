# Scenario 66: Private-sale motorcycle with a photographed bill of sale and remaining factory warranty (happy path)

**Accounts:** Test2 (Bob); Test1 (Alice) only for optional isolation check.
**Preconditions:** Bob's **personal account**, clock offset **0**, app date **2026-11-08** (America/New_York). Shared maker/model **Harley-Davidson / Softail** in seed; shared seller **Private sale** available. Pushes 25, 28 and 37 vehicle/start/transfer handling. Reader on or record **reader off**. No existing data reset or emails required. These are synthetic papers, not current official Harley-Davidson terms.
**Time:** 25 min
**Built per:** Full-document Scenario 1; Scenario 61 private sale/transferable coverage; push 25 in-service start rules; push 37 single Add screen.
**Why this plan:** an ordinary private sale has a simple signed-sale form and a remaining transferable factory warranty, not a new dealer return right or a fresh warranty counted from resale.

## The purchase (answer key)

| Fact | Value |
|---|---|
| Item / kind / category | **UAT P38 S66 Private Softail** / Motorcycle / Vehicles |
| Make / seeded model / year / trim | **Harley-Davidson / Softail / 2025 / Standard**; do not make unseeded "Softail Standard" a separate model |
| Seller in app / printed seller | Shared **Private sale** / **UAT Sample Seller**, 66 Example Seller Lane, Testville, ME 00000, `seller@uat-seller.example` |
| Condition / ownership / paid by | Used / Bought / Cash or check |
| Purchase price / seller-collected tax / total | **$12,000 / $0 / $12,000**. Government title/tax later is outside this bill |
| Purchase / original first service | **2026-11-07 / 2025-11-07** |
| VIN / reading | `1UATBVB10S0000066` (synthetic) / **4,200 miles on 2026-11-07** |
| Maker / coverage origin | **Harley-Davidson / Came with the product**, transferable remaining manufacturer's warranty |
| Coverage | Whole motorcycle defects, parts/labor; **24 months from 2025-11-07 to 2027-11-07**, **unlimited miles**. About 12 months remained at resale; no restart to 2028-11-07 |
| Transfer confirmation / conditions | Transfer recorded **2026-11-07**, no fee or outstanding registration step; factory term stays active for buyer |
| Seller warranty / plans / returns | None from seller, no purchased plan, no store return period; factory coverage supplied separately |

## Files, in the order to use them

| # | File | What it is | Where it goes |
|---|---|---|---|
| 1 | `01-private-sale-motorcycle-phone.jpg` | Skewed phone-photo look of a typed private bill of sale with signature lines | Add > Vehicle / saved vehicle, primary image-reading happy path |
| 1a | `01-private-sale-motorcycle.pdf` | Same bill of sale as a clean one-page PDF; alternative, **not another transaction** | Use instead of JPG for a separate repeat/run |
| 2 | `02-transferred-motorcycle-factory-warranty.pdf` | Two-page factory warranty schedule and transfer confirmation | Saved motorcycle > Read it |

### Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test2 | Confirm personal account / clock 0. Add > Vehicle > Motorcycle. Enter identity and dates from key, Used / Bought / cash or check. Choose shared seller **Private sale**, attach file 1; save | One Softail, correct year/trim, $12,000 and 4,200 miles on 2026-11-07, original first-service date 2025-11-07. Seller is shared Private sale, not a retailer named UAT Sample Seller. VIN/year/in-service/reading manually entered |
| 2 | Test2 | Before applying a warranty, inspect item coverage | Private-sale wording says the app assumes nothing about warranty transfer. No automatic store return period, invented new maker term, missing-coverage alert from private sale or lease task |
| 3 | Test2 | Read photographed bill; review/correct suggestions | Target Harley-Davidson, Softail / Standard trim, purchase 2026-11-07, $12,000 and printed private seller. Keep **Private sale** selected in app if reader proposes individual as a store. No order number required. No duplicate transaction or vehicle from PDF alternative |
| 4 | Test2 | Upload file 2, Read it, inspect and apply maker warranty | Transferable remaining factory warranty, explicit original start **2025-11-07**, end **2027-11-07**, 24 months and **unlimited miles**; provider Harley-Davidson. Transfer 2026-11-07 does not restart clock. Scope whole motorcycle parts/labor, with quotes |
| 5 | Test2 | Reload item and details | Coverage counted/active for new owner, **not** labelled Not counted: not transferable. Unlimited means no 4,200-mile limit or false remaining-mile number. Latest reading still dated. Source links to uploaded paper; record **Extracted from receipts** if shown, not a verified shared-policy claim |
| 6 | Test2 | Inspect Home/Next to end and To do / Notifications without jobs or time travel | Dated factory end **2027-11-07** (not resale plus 24 months), no outstanding start/transfer/registration task warranted by papers, no return/lease reminder. No end-date reminder due now. Future configured reminder lead time **verify** |
| 7 | Test1 | Optional direct link from Alice's personal account | Not accessible; no shared-business isolation assertion |

## Checked when this was made

- PDF and photographed bill agree; model is seeded Softail with Standard as trim. PDF text, arithmetic and visual renders checked locally. No live app reader test, database writes, sign-ins, email or authenticator access.

## Known rough edges (not part of the answer key)

- Private-sale seller preservation after reading a named individual's bill is **verify**; correct it in the review instead of creating a retailer. No real seller contact exists; do not send/call.
- Exact transfer/source labels and extraction confidence are **verify**. A reader miss is Partial with raw suggestions, not a live Fail or invented pass. Manually entered identity fields are not claimed as OCR features.
- Photo is a synthetic recreation of a typed bill, not an actual customer's paper. Signature lines are intentionally blank to make it clear this is test evidence only.
