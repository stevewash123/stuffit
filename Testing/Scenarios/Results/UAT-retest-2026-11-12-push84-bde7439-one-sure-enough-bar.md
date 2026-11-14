# StuffIt QA Retest — Push 84 (`bde7439`, One `SureEnough` Bar)

- **Date:** Thursday, Nov 12, 2026, 11:41 PM ET
- **Environment:** Staging (`https://stuffit-ui.onrender.com`, `https://stuffit-api.onrender.com`)
- **API Commit:** `bde7439` (started 10:58 PM ET, per build watch)
- **UI Last-Modified:** `Thu, 12 Nov 2026 23:25:11 UTC` (6:25 PM ET, unchanged from Push 83)
- **Source Notes:** `Testing\Scenarios\Bot Rules\CHANGES-push-84-one-sure-enough-bar.md` (S9.10.5)
- **Tester:** QA Controller (Alice, `vault_2448781_*`)

## Summary

**2 Pass, 1 Partial (0 Fail).** Quick Add (`Quick add, edit later`) and Add Details (`Add as a new item` left on default ticks) from New Items both attached the exact same 2 sure policies on `homedepot-receipt-01.pdf` (Hammer Drill). On `/add/new`, the default ticks after uploading `30-thermal-walmart-vizio-tv-protection.pdf` matched Push 81/83, though the form required picking a category before saving; picking `TVs` and then switching back to `Not sure` left Walmart general unticked, so saving attached 0 policies.

## Checks

### 1. Quick Add (`New Items > Quick add, edit later`) — Hammer Drill
- **Fixture:** `/workspace/uat/push75/homedepot-receipt-01.pdf`
- **Result:** **PASS**
  - Pending card showed Home Depot return (Confirmed), Milwaukee warranty (Confirmed), and 5 Likely Milwaukee lines.
  - Saved item (`"Covered · 2 policies"`):
    - `Return window · Home Depot`, Aug 15 to Nov 13, 2026 (1 day left)
    - `Manufacturer warranty · Milwaukee, POWER TOOLS`, Aug 15, 2026 to Aug 15, 2031
  - None of the 5 Likely lines were attached.
  - Deleted afterwards; remaining pending items dismissed and deleted for good.

### 2. Add Details (`New Items > Add as a new item`, default ticks) — Hammer Drill
- **Fixture:** `/workspace/uat/push75/homedepot-receipt-01.pdf`
- **Result:** **PASS**
  - **Default ticks:** Home Depot return policy (90 days, Confirmed) and Milwaukee warranty (5 years, Confirmed) ticked; all 5 Likely Milwaukee lines (`165' Laser Detector`, `8 Gallon Dust Extractor`, `AIRSNAKE Drain Cleaning Air Gun Accessories`, `Drain Cleaning Cables`, `Job Site Radios`) unticked (`"Not added"`).
  - **Saved item:** Exact same 2 policies and dates as Check 1 Quick Add.
  - Deleted afterwards; remaining pending items dismissed and deleted for good.

### 3. Add a Purchase (`/add/new`) — Ticked Lines & Saved Coverage
- **Fixture:** `/workspace/uat/push78/30-thermal-walmart-vizio-tv-protection.pdf` (Walmart + Vizio TV, `2026-08-29`)
- **Result:** **PARTIAL**
  - **Default ticks after upload (PASS):** Walmart general (90 days, Confirmed) ticked; Walmart electronics (30 days, Likely, ended `2026-09-28`) and smartphones (14 days, Likely, ended `2026-09-12`) unticked and greyed out; Vizio warranty (1 year, Unconfirmed) unticked.
  - **Save / category selection (Low/Info):** Saving without picking a category was blocked with `"Pick a category."` (`"needed: Vizio's warranty depends on it"`). Picking `TVs` switched Walmart electronics to Confirmed (still ended, so unticked) and Walmart general to Likely (unticked). Switching back to `"Not sure"` did not re-tick Walmart general, so saving `"P84 UAT Vizio TV"` attached 0 policies (`"Not set up yet · 2 suggested policies to review"`).
  - Deleted `"P84 UAT Vizio TV"` afterwards (`"Not found."` on revisit).

## Cleanup
- All created items (both Hammer Drills and `"P84 UAT Vizio TV"`) deleted via Edit pencil → Delete → Delete item.
- All remaining pending items dismissed and deleted for good; Alice's New Items Waiting and Dismissed tabs are empty.

## Screenshots
Saved under `/workspace/uat/push84/shots/`:
- `01-quick-add-hammer-drill.png`
- `02-add-details-hammer-drill.png`
- `03-add-new-saved.png`
