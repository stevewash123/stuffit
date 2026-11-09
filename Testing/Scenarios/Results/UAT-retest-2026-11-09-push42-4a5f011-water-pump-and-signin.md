# UAT retest — Push 42: water-pump service order + sign-in refresh (Nov 9, 2026)

- **Build:** API 4a5f011, started 10:32:43 AM ET. UI Last-Modified ~10:31 AM ET. Staging.
- **Source:** CHANGES-push-42-report-41-fixes-2026-11-09.md (2398 B, read from Bot Rules share); HANDOFF-push42-4a5f011-retest.txt.
- **Scope:** (1) live reader — S68 water-pump repair order kept as paper (no purchase facts / plan / claim; powertrain untouched; emailed one kept with item); (2) sign-in redirect / token-refresh (light check). Targeted only.
- **Not changed (do not report as fails):** powertrain narrative (notes: cannot reproduce from API data — need exact screen); data-protection keys (next push with migration); CPO popup wording; absolute end-mile totals.
- **Run:** Bob Personal (vault 2453777). Clock Offset 0 (no moves).

## Results

| Result | Count |
|---|---|
| Pass | 3 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 1 |

## Per-step results

| # | Check | Who / how | Result |
|---|---|---|---|
| 1 | Re-read existing water-pump RO on S68 CR-V — kept as paper; no plan/claim; powertrain unchanged | Bob, UI | **Pass** |
| 2 | First upload of water-pump RO on a fresh P42 CR-V — kept as paper; no plan/claim/coverage | Bob, UI | **Pass** |
| 3 | Emailed service order kept with the item (not a new item) | — | **Inconclusive** |
| 4 | Sign-in token refresh — direct URL / F5 / idle F5 without /login redirect | Bob, UI | **Pass** |

### 1 — Existing S68 water-pump RO: Pass

- Item: https://stuffit-ui.onrender.com/items/01a1c0cc-0b72-7fdc-a4ac-286de680981a (already had the document).
- Reader: **"Nothing to update: what you have already matches the document. Your document is attached to this item."**
- No purchase-fact changes: price \$36,500.00, total \$38,950.00, Nov 8 2024, UAT Riverbend Honda.
- No plan offer, no claim.
- Powertrain unchanged: until Nov 8 2029 or 60,000 miles, 38,000 left at a 22,000 reading.
- **Low:** re-uploading created a second identical Receipt entry (no duplicate check).

### 2 — Fresh item first upload: Pass

- Item: https://stuffit-ui.onrender.com/items/01a1c119-00bd-7cac-9ae6-6eaf6dd3d1fe (UAT P42 S68 Honda CR-V).
- Reader auto-ran. Toast: **"Nothing to update: what you have already matches the document. Press Upload to attach it to this item."**
- No offers. File attached as Receipt. No purchase facts, plan, claim, or coverage term created.
- **Low:** on an empty item, "already matches the document" is misleading; prefer wording like "kept as a document".
- **Low (out of scope):** fresh vehicle showed suggested "Manufacturer warranty · Honda" tagged LAWN AND GARDEN with a different-category warning.

### 3 — Emailed doc path: Inconclusive

- Notes say an emailed service order is kept with the item instead of becoming a new item.
- Item page has no item email address and no received-by-email marker. Settings > Email has a general mailbox connection, not exercised.
- **Not testable** from the UI without connecting a mailbox. Listed under Needs CC because the CHANGES notes describe this path.

### 4 — Sign-in token refresh (light): Pass

- Signed in 16:02:16Z. Direct URL opens 16:02:39 and 16:08:13. F5 at 16:05:35, 16:06:52, 16:07:59. After ~5 min idle, F5 at 16:14:19. No redirects to /login.
- Second session ~11:16–11:20 ET: also none.

## Needs code changes

1. **Emailed service-order path** — notes describe keeping an emailed RO with the item; no item-level email address / received-by-email marker found in UI to exercise it (Inconclusive until a mailbox path is available or documented).
2. **Low:** duplicate Receipt on re-upload of the same water-pump RO.
3. **Low:** empty-item toast wording ("already matches the document" → e.g. "kept as a document").

## Test data

- Existing S68: 01a1c0cc-0b72-7fdc-a4ac-286de680981a
- Fresh P42: 01a1c119-00bd-7cac-9ae6-6eaf6dd3d1fe

## Evidence

- Browser run as Bob Personal (vault 2453777), ~11:02–11:20 AM ET Nov 9.
- Notes: /workspace/uat/CHANGES-push-42-report-41-fixes-2026-11-09.md
