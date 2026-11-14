# UAT retest: push 75 (API `29c6fda`), remember a store or brand correction

- **Build:** API `29c6fda` started 11:25:54 AM ET Nov 12 2026; UI unchanged (Last-Modified Thu 12 Nov 2026 15:07:49 UTC).
- **Run:** 12:08 to 12:14 PM ET, as Alice, after a hard reload. App clock not moved (offset 0).
- **Scope:** CHANGES-push-75-match-feedback.md. NEXT-REPORT-ADDITIONS.md: none. New `POST /api/match-feedback` and per-account `match_feedback` table; no screen calls it yet.
- **How I checked:** uploads from a blank `/add/new` with the form's "Upload a receipt or warranty" button; nothing saved. Parties and `match_feedback` read read-only in Neon. The API steps were attempted from the signed-in tab's console.

## Summary: 2 Pass, 0 Fail, 1 Blocked (API steps not run)

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Regression: Home Depot, Lowe's, and Target Practice receipts | **Pass** | A THE HOME DEPOT at 12:11:08 PM: no panel; toast store Home Depot, brand Milwaukee (match log store `key` high, brand `key` high). C Lowe's Home Improvement at 12:11:34 PM: no panel; store Lowe's, brand DeWalt (store `alias` high, brand `key` high). E Target Practice Supplies at 12:11:45 PM: panel opened with Store **unticked**, "Select a store on the form before adding"; nothing applied (store `candidate` middle, brand Bushnell `key` high). Shots `p75-01-part1-A.png`, `p75-02-part1-C.png`, `p75-03-part1-E-panel.png`. |
| 2 | API match-feedback (remember, reject, clear, and error cases) | **Blocked** | Steps 2 to 4 of the notes were not run. A console `fetch` with the sign-in cookie got **401** at 12:13:12 PM ET. The API wants a bearer token, which the app keeps in memory (`localStorage` has only `stuffit.welcomeSeen`, `wb-alpha-notice-seen`, `stuffit.recovered.period`; `sessionStorage` empty), so a console call cannot reuse Alice's sign-in without pasting the token on screen, which QA will not do. Neon shows no `match_feedback` rows. Shot `p75-05-call1-401.webp`. |
| 3 | Baseline F, new "ORCHARD HDW" fixture | **Pass** | Uploaded at 12:12:06 PM, before any API call: no panel; the form filled with store "ORCHARD HDW (new, added to your local data)", brand DeWalt (match log store `none` low). A private party ORCHARD HDW was created at **12:12:21 PM ET** without saving (same auto-create behaviour as the earlier Allstate/Bushnell notes). Shot `p75-04-part2-F-baseline.png`. |

## Notes
- **Info:** the panel on receipt E had no Model row this time (push 74 showed model 202208), so the button read **"Keep 1 & Update 6"** instead of 7. Seen once; likely document reading variance.
- **Ask for CC:** a way to test `POST /api/match-feedback` without pasting a token on screen, for example a temporary small UI hook, an Ops-only test page, or the S9.10.6 picker. QA will run steps 2 to 4 then.

## Cleanup
Nothing saved. DB Stager confirmed at **12:16 PM ET** that it deleted the private party ORCHARD HDW (`01a1d0bf-01e5-78d5-969e-6d4a4a1e38c8`) and its name key. Alice has 0 `match_feedback` rows.

## Fixtures
New fixtures in `Testing\SampleData\push75-match-feedback\`: `p75-receipt-orchard-hdw.pdf` (prints "ORCHARD HDW") and `p75-receipt-lowes-plain.pdf` (prints "LOWE'S"; for the reject step, not used in this run). Also used the push 70 receipts in `Testing\SampleData\push70-store-names\` plus `homedepot-receipt-01.pdf`.
