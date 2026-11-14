# Push 72: the server's decision on store and brand matches (S2.8.4, first part)

API only (UI unchanged). Additive: the document-facts response (`POST` that reads a receipt for the Add form / New Items) now carries, on the store and brand proposals, `decision` (auto / choose / ask), `confidenceBand`, `reason` and `candidates`. No screen uses them yet, so nothing should look different.

## What to check (regression pass)
1. Re-run two or three receipts from Push 70/71 (THE HOME DEPOT, WALMART SUPERCENTER, Lowe's Home Improvement, Target Practice Supplies): same store, policies and brand as before. The document-facts panel still offers the same fill/correct/ask choices.
2. If you can see the network response of the facts call: store "Home Depot" shows `decision: auto`, `confidenceBand: high`, a reason like "Matches Home Depot by name."; "Target Practice Supplies" shows no `partyId` and a `choose` or `ask` decision with Target as a candidate.
