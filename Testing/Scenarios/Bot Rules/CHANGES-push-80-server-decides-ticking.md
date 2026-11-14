# Push 80: the server decides which coverage is ticked (S2.8.4 / S9.10.5, API part)

API only (UI follows as Push 81). Every coverage line the API returns (coverage preview, New Items coverage) now carries `decision`: `auto` (ticked), `choose` (offered unticked), `ask` (a remote extra return window, tucked behind a link). A closed window is never `auto`. The bar is the same 0.8 as before, now set in one place. The old numbers stay.

## What to check (regression: nothing should look different yet)
1. Add a purchase with a known store/brand: the same coverage lines are ticked as in Push 78 (sure ones ticked, "Likely" ones not, an ended window not).
2. New Items: the same coverage ticked on a receipt (Home Depot / Walmart / Lowe's).
3. If you can see the network response of the coverage preview: each coverage entry has `decision`.
