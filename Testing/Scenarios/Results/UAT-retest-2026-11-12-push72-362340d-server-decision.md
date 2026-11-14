# UAT retest: push 72 (API 362340d), the server's decision on store and brand matches

- **Build:** API `362340d`, started 8:29 AM ET Nov 12 2026. UI unchanged since 11:00 PM ET Nov 11.
- **Run:** 8:49 to 8:59 AM ET, as Alice. App clock not moved (offset 0).
- **Scope:** CHANGES-push-72-server-decision-document-facts.md, rows 1 and 2. NEXT-REPORT-ADDITIONS.md: none.
- **How I checked:** receipts uploaded two ways: from New Items (`POST /api/pending-items/upload`, the path used in pushes 70 and 71) and from the Add form's own upload on `/add/new` (`POST /api/intake`, the call that carries the new fields). Response read in Chrome DevTools Network. Match log and parties read read-only in Neon.

## Summary: 2 Pass, 0 Fail, 1 finding (Medium)

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Push 70/71 receipts give the same store, policies and brand | **Pass** | New Items path, same as the push 71 report: **A** Home Depot / Milwaukee, Home Depot return 90d Confirmed, Milwaukee 5y Confirmed. **B** Walmart / Vizio, electronics 30d Confirmed (window ended), general 90d Likely, Vizio 1y Unconfirmed, Allstate 3YR $49 plan Highly Likely ticked. **C** Lowe's / DeWalt, Lowe's 90d Confirmed, DeWalt 3y Confirmed. **E** store empty, Bushnell, "Nothing found yet", no store added. Match-log rules unchanged (key / alias 0.95 / candidate middle 0.6). Fill/correct/ask choices look the same. Shots `p72-01-A.png`, `p72-102-B.png`, `p72-103-C.png`, `p72-105-E.png`. |
| 2 | The facts response carries decision, band, reason, candidates | **Pass** | Seen on `POST /api/intake` (there is no call named "document-facts"; the New Items upload response has no store/brand proposals). **A** store Home Depot: partyId set, `auto`, `high`, "Matches Home Depot by name.", candidates []; brand Milwaukee: `auto`, `high`, "Matches Milwaukee by name.". **B** Walmart: `auto`, `high`, "Matches a name Walmart is also printed as."; Vizio `auto`/`high`. **C** Lowe's: `auto`, `high`, "Matches a name Lowe's is also printed as."; DeWalt `auto`/`high`. **E** store "Target Practice Supplies": **no partyId**, `choose`, `middle`, "Starts like Target, but may be something else.", candidates [Target (middle)]; Bushnell `auto`/`high`. Shots `p72-01-A-net.png` to `p72-04-E-net.png`. |

## Finding (Medium, may predate push 72)
- **Add form fills and creates "Target Practice Supplies".** On `/add/new`, uploading receipt E fills the store field with "Target Practice Supplies" and shows "(new, added to your local data)". A private party "Target Practice Supplies" was created in Alice's account at 8:54:15 AM ET, though the server's decision was `choose` with Target as a candidate. The proposal's outcome is still "fill". The New Items path leaves the store empty as push 70 intended. Expected on both paths: store left empty (or the person asked), no store created by itself. DB Stager removed the stray party afterwards.

## Notes
- **Info:** on the Add form path, coverage differs from the New Items path for the same receipt: B shows Walmart electronics 30d as Likely (New Items: Confirmed), general 90d Confirmed (New Items: Likely), an extra smartphones 14d line, and no Allstate plan; C shows DeWalt 3y as Likely (New Items: Confirmed) and an extra Lowe's major appliances 2d line.
- **Info:** a store row "Home Depot / exact" was logged at 8:50:46 alongside "THE HOME DEPOT / key" for one Add form upload (the re-check after filling the field). As in push 71, the label `exact` appears beside `key`.
- **Info:** one 504 Gateway Timeout in the console loading `/add` at the start; a reload worked.

## Cleanup
Nothing saved. All suggestions cancelled, dismissed and deleted for good; Dismissed is empty. The private "Target Practice Supplies" party and its name key were deleted by DB Stager (shared Target untouched). Alice signed out.

## Fixtures
No new fixtures. Used the push 70 receipts in `Testing\SampleData\push70-store-names\` plus `homedepot-receipt-01.pdf` and `30-thermal-walmart-vizio-tv-protection.pdf`.
