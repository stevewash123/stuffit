# Push 75: the app remembers a store or brand correction (S2.8.5, API part)

API only (UI unchanged). New endpoint `POST /api/match-feedback` and a per-account table `match_feedback`. No screen calls it yet (the picker is S9.10.6), so there is nothing to click. Grok's check is a regression pass plus an API check if you can send a request as Alice.

## What to check
1. Regression: re-run two receipts (THE HOME DEPOT, Lowe's Home Improvement) and Target Practice Supplies: same stores and panel behaviour as Push 74. Brands Milwaukee/DeWalt match as before.
2. API (optional, Alice signed in, DevTools console or any client): `POST /api/match-feedback` with `{"field":"store","printedText":"Orchard Hdw","partyId":"<id of Lowe's from the Parties list or a previous response>","confirm":true}` returns 204. Then upload a receipt printing "Orchard Hdw": the store is Lowe's (match log rule `user`, band high). The same receipt as Ops or a second account is NOT matched to Lowe's.
3. Same call with `"confirm":false` for the exact name "Lowe's": Alice's receipts printing Lowe's no longer pick Lowe's (rule none/candidate); another account still does. Undo by confirming it: `"confirm":true` clears the rejection.
4. A bad field returns 400; a brand id with field "store" returns 404.
Clean up: confirm Lowe's again for "Lowe's" (clears the reject); the "Orchard Hdw" confirm can stay or be rejected-then-removed by DB Stager (delete rows in match_feedback for Alice).
