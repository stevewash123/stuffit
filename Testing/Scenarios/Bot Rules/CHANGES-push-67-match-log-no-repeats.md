# Push 67: the match log counts a decision once

API only (UI unchanged). Fixes the Low from the Push 66 retest: one receipt read wrote the same store/brand decision 4 times, inflating `GET /api/admin/match-decisions/summary`.

## What to check
1. Upload `homedepot-receipt-01.pdf` again as Alice. In the Ops summary, "THE HOME DEPOT" (store / key / high) and "Milwaukee" (brand / key / high) should rise by 1 each, not 4.
2. Receipts still match the same store and brand as before.

## Answer to the Push 66 Partial (add-purchase document, QuickTop Lube)
Not a Push 66 change. The add-purchase document read does not propose a store from a service-order document today, so matching never runs for it. Logged as a follow-up; not tested this push.
