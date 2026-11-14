# UAT retest: push 71 (API 4a1d3ac), indexed store and brand name lookup

- **Build:** API `4a1d3ac`, started 7:18 AM ET Nov 12 2026 (`/api/version` startedAt 12:18:37 UTC). UI unchanged since 11:00 PM ET Nov 11.
- **Run:** 7:37 to 7:50 AM ET, as Alice and Ops. App clock not moved (offset 0).
- **Scope:** CHANGES-push-71-name-index.md, rows 1 to 4. NEXT-REPORT-ADDITIONS.md: none.
- **How I checked:** uploaded each receipt with "Upload a receipt or warranty", opened the review form, recorded it and cancelled. Match log and `party_name_keys` read read-only in Neon.

## Summary: 4 Pass, 0 Fail

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Push 70 receipts give the same store, policies and log rule | **Pass** | **A** "THE HOME DEPOT" became "Home Depot" (key, high, 1.0), Home Depot return 90d Confirmed. **B** "WALMART SUPERCENTER" became "Walmart" (alias, high, 0.95), Walmart electronics 30d Confirmed (window ended), general 90d Likely, Vizio 1y Unconfirmed, Allstate 3YR plan line. **C** "Lowe's Home Improvement" became "Lowe's" (alias, 0.95), Lowe's return 90d Confirmed. **D** "SAMS CLUB #6452" became "Sam's Club" (key, 1.0), Sam's Club electronics 90d. **E** "Target Practice Supplies" left the store empty (candidate, middle, 0.6). All identical to push 70. Shots `p71-201-A.png` to `p71-205-E.png`. |
| 2 | Brand reads still work | **Pass** | Milwaukee (FUEL Hammer Drill, Milwaukee 5y Confirmed) and DeWalt (Circular Saw) on A, Vizio, DeWalt, Samsung and Bushnell all matched on key, high, 1.0. "Prime stud" logged none/low as before. No "Milwaukee Tool" style alias receipt was available. |
| 3 | Admin edit, then a receipt with the new name matches | **Pass** (by rename) | There is no alias editor in the admin pages ("Edit details" has Name, Website, Claims page, phone and type boxes only), so I used a rename. Before: new receipt **F** "ORCHARD SUPPLY HARDWARE" left the store empty (none, low) at 7:39 AM. Ops renamed Lowe's to "Orchard Supply Hardware" at 7:48:04 AM. F uploaded at 7:48:36 AM matched it (logged **exact**, high, 1.0) with the store's 90-day return policy, Confirmed. Renamed back to `Lowe's` at 7:49:53 AM; `party_name_keys` was rebuilt at 7:49:52 with `lowes` and `loweshomeimprovement` only, no Orchard key left. Shots `p71-210-renamed.png`, `p71-211-F-renamed.png`, `p71-212-renamed-back.png`. |
| 4 | First loads after deploy not slow or failing | **Pass** | First upload on the new build (A, 7:37 AM) took about 3 seconds. Later reads took 2 to 18 seconds; one (B, second round) took over 25 seconds, without an error. No failures. |

## Notes
- **Low:** the match through the renamed name is logged as rule `exact`, while every other name match logs `key` (push 66 also showed `key`). Same result, different label.
- **Low (admin):** there is no way in the admin UI to add or remove a store alias. The notes' "add an alias" path can't be checked without one.
- **Info:** re-uploading a file whose suggestions were dismissed doesn't read it again ("you set this aside earlier. See Dismissed."), but it still writes match-log rows (7:37 to 7:39 AM). I used "Delete for good" on the dismissed items to get fresh reads.
- **Info:** the review form's Price is the pre-tax line price (B 328, C 99, D 379, E 149, F 89) while the suggestion card shows the receipt total. Probably by design; flagging in case.
- Still open from push 70: the private Allstate and Bushnell parties in Alice's account.

## Cleanup
Nothing saved. All suggestions dismissed and then deleted for good; New Items and Dismissed are empty. Lowe's name is back to `Lowe's`, alias "Lowe's Home Improvement" unchanged. Both accounts signed out.

## Fixtures
- **New:** `Testing\SampleData\push71-name-index\p71-receipt-orchard-supply-hardware.pdf` (prints "ORCHARD SUPPLY HARDWARE", DeWalt compact drill), for the rename/alias case.
- Reused: the five receipts from push 70 (`Testing\SampleData\push70-store-names\` plus `homedepot-receipt-01.pdf` and `30-thermal-walmart-vizio-tv-protection.pdf`).
