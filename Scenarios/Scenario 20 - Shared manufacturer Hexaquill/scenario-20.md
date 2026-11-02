# Scenario 20: A manufacturer the shared data does not have is reported by three people and verified, with its warranty

The brand **Hexaquill** is not in the shared data (scenario 4). Three people each add it as their own brand and upload the manufacturer's warranty document, which is offered to the community by default. Once three have, an operator verifies the **brand** and then its **warranty**. Then the question is what happens to the three people's own records, and to the next person.

Uses the files of **scenario 4** (Target / Hexaquill 12V Cordless Screwdriver Set, with its warranty document). No files are copied here. Needs **three people (three accounts)** plus an **operator**, and a **fourth person** at the end. `python run_shared.py 20` plays all of them on new accounts and prints `PASS` or `FAIL` for each check below.

## The purchase and the warranty (answer key)

| Fact | Value |
|---|---|
| Store | Target (a shared store, 90-day window; unchanged by this scenario) |
| Order / date | TGT-4471903 / 2026-09-19 |
| Item | Hexaquill 12V Cordless Screwdriver Set, model HX-SD12, SN HQ26S900144 |
| Total | **$36.91** (VISA ending 1111, Chase Freedom Unlimited) |
| Brand in shared data? | **No** |
| The warranty document says | tool **2 years**, battery **1 year** (counted from purchase) |

## Files (all in `Scenario 4 - Brand not in shared data`)

| # | File | Where it goes |
|---|---|---|
| 01 | `01-email-order-target-hexaquill-hx-sd12.eml` | The person's mailbox, or upload it |
| 02 | `02-receipt-target-hexaquill-hx-sd12.pdf` or `.jpg` | New Items, `/add` |
| 03 | `03-warranty-target-hexaquill-hx-sd12.pdf` or `.jpg` | The item's page, after it is in My Items |

## Steps and what should happen (S6.1.4)

### Part 1: three people report the same new brand and warranty

1. **Person 1** brings in files 01 and 02. In New Items the brand "Hexaquill" is **not recognised**: they add **Hexaquill as a new brand on their own list**, then add the item to My Items.
2. Person 1 opens the item and **uploads the warranty** (file 03, origin "Came with the product"). It matches the model and the store. It asks to add the warranty: tool 2 years, battery 1 year. They add it. It is **shared by default** (a short note on the screen says so).
   - *Operator view:* one claim, **brand "Hexaquill", 1 account**. The warranty is also one claim of **1 account, not ready**.
3. **Persons 2 and 3** do the same, each on their own account with their own private brand "Hexaquill".
   - *Operator view:* the **brand claim reaches 3 accounts and is ready**.
   - **The warranty is still three separate claims of 1 account each.** Each is about its own person's private brand, so they cannot be counted together yet.

### Part 2: the operator verifies the brand, then the warranty

4. The operator **approves the brand** claim (`POST /api/admin/claims/approve` with the claim's `id`; `name` can correct the spelling). A new shared brand "Hexaquill" exists. All three private brands are replaced by it; every item, purchase and warranty offer that pointed at them points at it.
5. **The three warranty claims now become one claim of 3 accounts, ready.** (They were three because the brands were three; now it is one brand.)
6. The operator looks the warranty up (the maker's page says: tool 2 years) and **approves** it with the page they read: `{ "id": "<claim id>", "sourceUrl": "<the maker's warranty page>" }`. A shared Hexaquill warranty exists: **24 months**, counted from purchase, with the operator's page as official-source evidence. The three offers are marked approved.
   - A brand with no shared warranty is created fresh; a placeholder one is corrected in place; a verified one needs the date the new one took effect (`effectiveFrom`) and becomes a new version.

### Part 3: what changes for the three people, and the next one

7. Each of the three people: their item shows **Hexaquill as a shared brand**. The warranty they added from the document is unchanged (they keep their own coverage; a document they uploaded is theirs).
8. A **fourth person** brings in files 01 and 02: the brand matches **the shared Hexaquill** with no brand to add, and the **verified 24-month Hexaquill warranty is ticked and added on its own** when they add the item, ending **2028-09-19**, with no document needed.
9. If a person had **typed their own warranty** for Hexaquill (36 months, say), it stays and wins for them. Its line carries a note: *Hexaquill's verified warranty is 24 months; yours says 36 months. Check which applies to you.*

## Expected coverage for the fourth person (dates from the purchase date, 2026-09-19)

- Target return window: 90 days, ends **2026-12-18**.
- Hexaquill manufacturer warranty: **24 months, ends 2028-09-19** (from shared data now, verified).
- Chase Freedom Unlimited purchase protection: 120 days, ends **2027-01-17**; extended warranty +12 months, so coverage ends **2029-09-19**.

## Not covered here

- Parts (the 1-year battery) are not carried into the shared warranty: the operator adds parts in the console.
- A screen for the operator: the operator steps are API calls (see the README).

## Checked when this was made

- The steps and numbers follow the code and the tests (`ClaimTests`) and scenario 4's answer key. `python run_shared.py 20` was run against the development API: **8 of 8 checks passed** (see `last-run-shared.txt`). Running it found, and the code now handles, three things: the three warranty offers must be pointed at the new shared brand or they never count together; each person's item, purchase and card must be pointed at it too; and the warranty claim is made the moment the brand is verified, not before.
