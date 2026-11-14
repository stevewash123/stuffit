# StuffIt QA Retest — Push 80 (`018a5c1`, Server Decides Ticking)

- **Date:** Thursday, Nov 12, 2026, 4:57 PM ET
- **Environment:** Staging (`https://stuffit-ui.onrender.com`, `https://stuffit-api.onrender.com`)
- **API Commit:** `018a5c1` (started `2026-11-12T21:40:00Z` / 4:40 PM ET)
- **UI Last-Modified:** `Thu, 12 Nov 2026 20:44:38 UTC` (3:44 PM ET, unchanged from Push 79)
- **Source Notes:** `Testing\Scenarios\Bot Rules\CHANGES-push-80-server-decides-ticking.md` (S2.8.4 / S9.10.5, API part)
- **Tester:** QA Controller (Alice, `vault_2448781_*`)

## Summary

**3 Pass, 0 Fail.** All Push 80 API-only regression checks passed. Every coverage line returned by the coverage preview and New Items endpoints includes a `decision` field (`auto` or `choose`), ticked/unticked states on `/add/new` match Push 78, and ended return windows return `decision: "choose"` with `ended: true` (never `auto`).

No `ask` decision appeared in these fixtures (UI support for `ask` follows in Push 81).

## Checks

### 1. Add Purchase (`/add/new`) — Regression & Ended Window
- **Fixture:** `/workspace/uat/push78/30-thermal-walmart-vizio-tv-protection.pdf` (existing fixture from Push 77/78; Walmart + Vizio TV, older purchase date).
- **Result:** **PASS**
  - **Walmart return policy: general (90 days)** — Badge: Confirmed. Ticked on screen with category warning; `decision: "auto"`.
  - **Walmart return policy: electronics (30 days)** — Badge: Likely. Unticked and greyed out ("This return window ended 2026-09-28, so it cannot be added."); `decision: "choose"`, `ended: true`.
  - **Walmart return policy: smartphones (14 days)** — Badge: Likely. Unticked and greyed out (ended 2026-09-12); `decision: "choose"`, `ended: true`.
  - **Vizio warranty (1 year)** — Badge: Unconfirmed (placeholder). Unticked ("Not added. Tick it to add it…"); `decision: "choose"`.
- **Additional current-date check (Lowe's / DeWalt / Power tools / Cordless Drill, dated `2026-11-12`):**
  - **DeWalt warranty (3 years, Confirmed):** Ticked; `decision: "auto"`.
  - **Lowe's return policy (90 days, Confirmed):** Ticked; `decision: "auto"`.
  - **Info:** The preview response returned `dateAssumed: true` and the page displayed "Counted from today until you give the date" even though the date input was pre-filled with `2026-11-12` (pre-filled default date is not treated as an explicitly entered date).
- Nothing was saved.

### 2. New Items — Coverage `decision` & Ticking
- **Fixture:** `/workspace/uat/push75/homedepot-receipt-01.pdf` (existing fixture from Push 75).
- **Result:** **PASS**
  - Created three pending items (New Items cards render coverage badges rather than checkboxes):
    - **Circular Saw:** Home Depot return policy (Confirmed) `decision: "auto"`; DeWalt warranty (Confirmed) `decision: "auto"`.
    - **Hammer Drill:** Milwaukee warranty, 5 years (Confirmed) `decision: "auto"`; five Likely Milwaukee product-line warranties (Job Site Radios, Drain Cleaning Cables, AIRSNAKE Drain Cleaning Air Gun Accessories, 8 Gallon Dust Extractor, 165' Laser Detector) all `decision: "choose"` with "Not ticked: we could not tell if this is …".
    - **Prime stud** (under "Smaller things", below $50 minimum): Home Depot return policy: general `decision: "auto"`; Home Depot return policy: major appliances `decision: "choose"` (`ended: true`, not shown in UI).
- **Cleanup:** All three pending items were dismissed and deleted for good. Alice's New Items Waiting and Dismissed queues are empty.

### 3. Network Response `decision` Field
- **Result:** **PASS**
  - Verified via DevTools Network (Fetch/XHR) on both the `/add/new` coverage preview responses and the New Items upload response: every coverage entry carries `decision` (`"auto"` or `"choose"`), and ended return windows are `"choose"`, never `"auto"`.

## Open Items / Notes for CC
- **Info:** On `/add/new`, a pre-filled today date (`2026-11-12`) still triggers `dateAssumed: true` ("Counted from today until you give the date") unless the date is explicitly changed/entered.
- **Note:** `Prime stud` continues to appear as a third pending item under "Smaller things" on `homedepot-receipt-01.pdf` (previously noted).

## Screenshots
Saved under `/workspace/uat/push80/shots/`:
- `00-walmart-vizio-coverage-ui.png`
- `01-walmart-preview-json-general-auto.webp`
- `02-walmart-preview-json-electronics-choose.webp`
- `03-walmart-preview-json-smartphones-vizio.webp`
- `04-lowes-dewalt-ui.png`
- `05-lowes-dewalt-json-dewalt-auto.webp`
- `06-lowes-dewalt-json-lowes-auto.webp`
- `07-newitems-homedepot-ui.png`
- `08-newitems-json-primestud.webp`
- `09-newitems-json-circularsaw.webp`
- `10-newitems-json-hammerdrill-likely-choose.webp`
- `11-newitems-json-milwaukee-auto.webp`
