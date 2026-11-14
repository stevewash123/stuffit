# Push 71: indexed store and brand name lookup (S2.8.2)

API only (UI unchanged). Behavior should be identical to Push 70; this replaces "load every store/brand and scan" with an indexed lookup. New table `party_name_keys`, filled at start.

## What to check (a regression pass; nothing should look different)
1. Re-run the Push 70 receipts: THE HOME DEPOT #0999, WALMART SUPERCENTER, Lowe's Home Improvement, SAMS CLUB #6452 each give the same store, return policies and match-log rule as in the Push 70 report. Target Practice Supplies still leaves the store empty (rule candidate).
2. Brand reads still work: Milwaukee / DeWalt on the Home Depot receipt, "Milwaukee Tool" style alias if you have one.
3. Admin: edit a store's name or add an alias, then upload a receipt printing the new name: it matches (the index follows the edit).
4. First load after deploy: the receipt reads should not be noticeably slower or fail (the index is filled at API start; check /api/version startedAt is the new build first).
