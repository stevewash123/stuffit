# StuffIt QA Retest — Push 81 (UI-only, Add Form Follows Server Decision)

- **Date:** Thursday, Nov 12, 2026, 5:34 PM ET
- **Environment:** Staging (`https://stuffit-ui.onrender.com`, `https://stuffit-api.onrender.com`)
- **UI Last-Modified:** `Thu, 12 Nov 2026 22:05:09 UTC` (5:05 PM ET)
- **API Commit:** `018a5c1` (unchanged from Push 80)
- **Source Notes:** `Testing\Scenarios\Bot Rules\CHANGES-push-81-add-form-follows-the-server.md` (S9.10.5 UI part)
- **Tester:** QA Controller (Alice, `vault_2448781_*`)

## Summary

**3 Pass, 0 Fail.** All Push 81 Add Purchase checks passed. Coverage ticking on `/add/new` matches Push 80/78 across Walmart/Vizio, Lowe's/DeWalt, and Home Depot receipts, `"Other return windows (1)"` appears and expands on `Sam's Club` (with mutual exclusion between return windows), and saving a purchase attaches only the ticked coverage lines.

## Checks

### 1. Add Purchase (`/add/new`) — Ticked/Unticked Regression
- **Result:** **PASS**
  - **a) Walmart / Vizio PDF** (`/workspace/uat/push78/30-thermal-walmart-vizio-tv-protection.pdf`, filled `2026-08-29`, Vizio V5, category "Not sure"):
    - Walmart return policy: general, 90 days (Confirmed) — ticked.
    - Walmart electronics, 30 days (Likely) — greyed out and unticked ("This return window ended 2026-09-28, so it cannot be added.").
    - Walmart smartphones, 14 days (Likely) — greyed out and unticked (ended `2026-09-12`).
    - Vizio warranty, 1 year (Unconfirmed) — unticked.
    - Not saved.
  - **b) Lowe's / DeWalt / Power tools / Cordless Drill / `2026-11-12`:**
    - DeWalt warranty, 3 years (Confirmed) — ticked.
    - Lowe's return policy, 90 days (Confirmed) — ticked.
    - Not saved.
  - **c) Home Depot PDF** (`/workspace/uat/push75/homedepot-receipt-01.pdf`, filled `2026-08-15`, Milwaukee M18 FUEL, category "Not sure"):
    - Home Depot general return, 90 days (Confirmed) — ticked.
    - Home Depot major appliances, 2 days (Likely) — greyed out and unticked (ended `2026-08-17`).
    - Six Milwaukee warranty lines, all Likely and all unticked (general 1 year, portable generators 2 years, outdoor power equipment 3 years, hoists 1 year, digital levels 3 years, power tools 5 years).
    - Not saved.

### 2. `"Other return windows (n)"` Link & Mutual Exclusion
- **Result:** **PASS**
  - **Other return windows link:** Tested with Store `Sam's Club`, Purchase date `2026-11-12`, Item `Test TV`, Category `TVs`. Before expanding, the page showed `Sam's Club return policy: electronics` (90 days, Merchant, Unconfirmed, unticked) and the link **`Other return windows (1)`**. Clicking it opened `Sam's Club return policy: general` (Merchant, Unconfirmed) and changed the link to `Hide other return windows`.
  - **Mutual exclusion:** Verified on both `Sam's Club` (TVs, `2026-11-12`) and `Walmart` (Vizio TV, `2026-11-12`). Ticking one return window automatically unticks the other return window, while warranty lines remain independent.
  - **Note:** On `Sam's Club`, clicking the label/title text toggled the checkbox reliably, whereas a synthetic click directly on the `electronics` checkbox input did not toggle it.

### 3. Saving a Purchase Attaches Exactly the Ticked Lines
- **Result:** **PASS**
  - Saved `"P81 UAT Vizio TV"` (Walmart, `2026-11-12`, TVs) with **Walmart general 90 days** ticked and **Walmart electronics 30 days** + **Vizio warranty 1 year** unticked.
  - The saved item page showed `"Covered, 1 policy"`: `Return window · Walmart, Nov 12, 2026 to Feb 10, 2027` (the 90-day window). Neither unticked line was attached (`"1 suggested policy to review"` appeared only as a suggestion).
  - **Cleanup:** Deleted the test item via Edit → Delete → Delete item; reopening its URL shows `"Not found."`

## Screenshots
Saved under `/workspace/uat/push81/shots/`:
- `01-walmart-vizio.png`
- `02-lowes-dewalt.png`
- `03-homedepot.png`
- `04-other-windows-open.png`
- `05-return-window-mutual-exclusion.png`
- `06-saved-item-coverage.png`
