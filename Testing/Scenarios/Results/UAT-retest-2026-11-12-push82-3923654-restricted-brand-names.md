# StuffIt QA Retest — Push 82 (`3923654`, Restricted Brand Names)

- **Date:** Thursday, Nov 12, 2026, 6:11 PM ET
- **Environment:** Staging (`https://stuffit-ui.onrender.com`, `https://stuffit-api.onrender.com`)
- **API Commit:** `3923654` (started `2026-11-12T22:49:03Z` / 5:49 PM ET)
- **UI Last-Modified:** `Thu, 12 Nov 2026 22:05:09 UTC` (5:05 PM ET, unchanged from Push 81)
- **Source Notes:** `Testing\Scenarios\Bot Rules\CHANGES-push-82-restricted-brand-names.md` (S2.8.3, brand half)
- **Tester:** QA Controller (Alice, `vault_2448781_*`)

## Summary

**3 Pass, 0 Fail.** All Push 82 restricted-brand-name checks passed on `/add/new`. Ordinary-word brand names (`Echo`, `Target`) are no longer extracted from product lines or shop names, while `Milwaukee`, `Vizio`, and `Bushnell` continue to bind as before.

## Checks

### 1. Regression — Home Depot & Walmart/Vizio Receipts
- **Result:** **PASS**
  - **a) Home Depot receipt** (`/workspace/uat/push75/homedepot-receipt-01.pdf`): Store `Home Depot`, Brand `Milwaukee`, Item `Milwaukee M18 FUEL`, Category `Not sure` (warranty prompt shown). No picker.
  - **b) Walmart thermal receipt** (`/workspace/uat/push78/30-thermal-walmart-vizio-tv-protection.pdf`): Store `Walmart`, Brand `Vizio`, Item `Vizio V5` (`V505-J09`), Category `Not sure` (warranty prompt shown). No picker.

### 2. Target Practice Supplies Receipt — `Bushnell` Binds, No `Target` Brand
- **Result:** **PASS**
  - **Fixture:** `/workspace/uat/push75/p70-receipt-target-practice-supplies.pdf`
  - **Store:** Candidate picker appeared (`"Store Target Practice Supplies — Starts like Target, but may be something else."` with `Target` selected and `None of these: Target Practice Supplies (new)`), Store checkbox unticked (`"Select a store on the form before adding"`).
  - **Brand:** `Bushnell` bound from `"Bushnell ..."` line; **no `Target` brand** bound from the shop name.
  - Panel was not applied and nothing was saved, so no private party was created.

### 3. Restricted Brand Name in Product Line — `Echo Dot`
- **Result:** **PASS**
  - **New Fixture:** `Testing\SampleData\push82-restricted-brands\p82-receipt-echo-dot.pdf` (box path `/workspace/uat/push82/p82-receipt-echo-dot.pdf`) — Best Buy receipt with `"1x Echo Dot (4th Gen) Smart speaker"` ($59.99, dated `2026-11-12`).
  - **Store:** `Best Buy`
  - **Brand:** Empty (placeholder only; `Echo` is NOT bound from `"Echo Dot (4th Gen) Smart speaker"`).
  - **Category:** `Not sure` (none of `Echo`'s categories auto-filled).
  - Only Best Buy general (15 days) return policy applied. Nothing saved.

## New Fixtures Added to Share
- `\\DESKTOP-TD3DQ64\Stuffit\Testing\SampleData\push82-restricted-brands\p82-receipt-echo-dot.pdf`

## Screenshots
Saved under `/workspace/uat/push82/shots/`:
- `01-homedepot-brand.png`
- `02-walmart-vizio-brand.png`
- `03-target-practice-bushnell.png`
- `04-echo-dot-no-brand.png`
