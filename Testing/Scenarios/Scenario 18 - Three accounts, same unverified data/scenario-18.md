# Scenario 18: Three accounts report the same unverified data; an operator verifies it

Uses the files of scenarios **3** (store not in shared data: Quillfeather Mercantile), **4** (brand not in shared data: Hexaquill) and **6** (Sony warranty, no verified policy). No files are copied here. `python run_scenarios.py 18` runs it on **four new accounts** plus an operator account (set up with two-step sign-in through the API).

## Steps and what should happen (S6.1.4)

1. Account 1 brings in scenarios 3, 4 and 6, accepts them, and uploads the Sony warranty document to the Sony item (shared by default). The claim list for the operator shows three claims, each with **1** account, none ready: store "Quillfeather Mercantile", brand "Hexaquill", and a Sony warranty.
2. Account 2 does the same: each claim shows **2**. Account 3: each shows **3** and is **ready**.
3. Nothing is visible to other users in the meantime, and no confidence has changed (counting is not evidence).
4. The operator runs **evaluate** (`POST /api/admin/claims/evaluate`): the three ready claims come back.
5. The operator **approves** each (`POST /api/admin/claims/approve`; the Sony policy with a sony.com source). The store and brand become shared; the Sony warranty becomes a shared policy with the operator's evidence.
6. A **fourth account** brings in the same files: the Quillfeather purchase now matches the shared store, and the Sony warranty is suggested from shared data.

The runner prints `PASS` or `FAIL` for each of these.
