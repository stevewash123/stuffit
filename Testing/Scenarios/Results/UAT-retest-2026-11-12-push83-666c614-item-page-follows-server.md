# StuffIt QA Retest — Push 83 (`666c614`, Item Page Follows Server Decision)

- **Date:** Thursday, Nov 12, 2026, 10:53 PM ET
- **Environment:** Staging (`https://stuffit-ui.onrender.com`, `https://stuffit-api.onrender.com`)
- **API Commit:** `666c614` (started `2026-11-12T23:26:28Z` / 6:26 PM ET)
- **UI Last-Modified:** `Thu, 12 Nov 2026 23:25:11 UTC` (6:25 PM ET)
- **Source Notes:** `Testing\Scenarios\Bot Rules\CHANGES-push-83-item-page-follows-the-server.md` (S9.10.5)
- **Tester:** QA Controller (Alice, `vault_2448781_*`)

## Summary

**3 Pass, 0 Fail.** All Push 83 checks passed on the item page's suggested-coverage list (`GET /api/items/{id}/proposals`). Every suggestion entry includes `decision`, ended return windows are not ticked (`decision: "choose"` even with 0.91 confidence), and hand-ticking + `"Verify the above policies apply"` work as before.

*(Note: Because the saved test item `"P83 UAT Vizio TV"` resolved to category `TVs`, the ended Walmart electronics window had confidence 0.91 / `"Confirmed"` but was correctly held at `decision: "choose"` because it was ended; Walmart general had confidence 0.69 / `"Likely"` and `decision: "choose"`; Vizio warranty had confidence 0.05 / `"Unconfirmed"` and `decision: "choose"`. So all 3 suggestions were unticked by `decision: "choose"`.)*

## Checks

### 1. Item Page Suggested Coverage List (`Policies card > Review`)
- **Setup:** Uploaded `/workspace/uat/push78/30-thermal-walmart-vizio-tv-protection.pdf` on `/add/new` (dated `2026-08-29`), named `"P83 UAT Vizio TV"`, unticked all coverage lines, and saved. Policies card showed `"Not set up yet · 2 suggested policies to review · Review"`.
- **Result:** **PASS**
  - **Walmart ELECTRONICS return window** (`Aug 29 – Sep 28, 2026`, `"Confirmed"`): unticked (ended window not ticked).
  - **Walmart general return window** (`Aug 29 – Nov 27, 2026`, `"Likely"`): unticked.
  - **Vizio TVs manufacturer warranty** (`Aug 29, 2026 – Aug 29, 2027`, `"Unconfirmed"`): unticked.

### 2. Network Response (`GET /api/items/{id}/proposals`) `decision` Field
- **Result:** **PASS**
  - Inspected `GET /api/items/{id}/proposals` in DevTools Network (Fetch/XHR). All 3 entries carried `decision`:
    - `Walmart return policy: electronics` — `"decision": "choose"` (confidence `0.91`, trust `0.99`, applicability `0.92`, `policyCategory: "Electronics"`)
    - `Walmart return policy: general` — `"decision": "choose"` (confidence `0.69`, trust `0.99`, applicability `0.7`, `policyCategory: null`)
    - `Vizio warranty` — `"decision": "choose"` (confidence `0.05`, trust `0.05`, applicability `0.95`, `policyCategory: "TVs"`)

### 3. Hand-Ticking, `"Verify the above policies apply"`, and Added Coverage
- **Result:** **PASS**
  - `"Verify the above policies apply"` button is disabled when 0 lines are ticked, enables and updates its count when ticked (`"Verify the above 2 policies apply"`), and disables again when unticked.
  - Ticked Walmart general + Vizio warranty and clicked `"Verify the above 2 policies apply"`: `"Your coverage"` card added `Return window · Walmart` (`Aug 29 – Nov 27, 2026`, 15 days left, `"Try this first"`) and `Manufacturer warranty · Vizio TVS` (until `Aug 29, 2027`); item status became `"Expiring soon"`.
  - **Cleanup:** Deleted `"P83 UAT Vizio TV"` via Edit pencil → Delete → Delete item; reopening its URL shows `"Not found."`

## Screenshots
Saved under `/workspace/uat/push83/shots/`:
- `01-suggestions-list.png`
- `02-suggestions-json.png`, `02b-suggestions-json.png`, `02c-suggestions-json.png`
- `03a-hand-ticked.png`
- `03-added-coverage.png`
