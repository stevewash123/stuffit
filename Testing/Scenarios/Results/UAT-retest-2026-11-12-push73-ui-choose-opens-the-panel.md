# UAT retest: push 73 (UI-only), a store the server says to choose is never filled in silently

- **Build:** UI redeployed 9:09 AM ET Nov 12 2026; API unchanged at `362340d` (started 8:29 AM ET).
- **Run:** 9:33 to 9:36 AM ET, as Alice, after a hard reload. App clock not moved (offset 0).
- **Scope:** CHANGES-push-73-choose-opens-the-panel.md, rows 1 to 3. NEXT-REPORT-ADDITIONS.md: none. Known items in the notes (coverage lists differ between Add form and New Items; Target not offered as a pick) not tested.
- **How I checked:** uploads from a blank `/add/new` with the form's "Upload a receipt or warranty" button; nothing saved. Parties read read-only in Neon.

## Summary: 3 Pass, 1 Fail

| # | Check | Result | Detail |
|---|---|---|---|
| 1a | Target Practice receipt opens the panel instead of filling the form | **Pass** | 9:33 AM: "What we found in your document" opened; no toast; after "Not now" with Store unticked the Store field was empty. Shot `p73-01-E-panel.png`. |
| 1b | No private "Target Practice Supplies" unless ticked in the panel **and saved** | **Fail (Medium)** | The Store row is **ticked by default**: "Use the document for Store … Target Practice Supplies. Read from the document. **New store: added to your local data.**" So "Update All" fills it with no separate choice. At 9:34 AM I clicked Update All and then left **without saving**; Neon shows a private party "Target Practice Supplies" in Alice's account created at **9:34:11 AM ET**. The store is created when the panel is applied, not on save. The 9:33 run with Store unticked created nothing. Shot `p73-02-E-ticked.png`. Expected: Store row unticked for a `choose` decision, and the store created only when the item is saved. |
| 2 | Sure stores still fill straight away with the toast | **Pass** | No panel for any. A Home Depot / Milwaukee: "Filled in from your document: store Home Depot, brand Milwaukee, name Milwaukee M18 FUEL, item price 199.00, date 2026-08-15, order total 417.53, order number 3456." B Walmart / Vizio, C Lowe's / DeWalt, D Sam's Club / Samsung, each with the same "Filled in from your document: store …" toast. Shots `p73-11-A.png` to `p73-14-D.png`. |
| 3 | Nothing else changed | **Pass** | Coverage previews load as before; New Items Waiting and Dismissed empty; no errors. |

## Notes
- **Info:** receipt C (Lowe's) fills no item name on the Add form, so the Item field stays empty.
- **Info:** in the panel, Brand Bushnell shows "Yours" (the private Bushnell party from push 70 is still in Alice's account).

## Cleanup
Nothing saved. New Items empty. The private "Target Practice Supplies" party created at 9:34:11 AM ET was sent to DB Stager for deletion. Alice signed out.

## Fixtures
No new fixtures. Used the push 70 receipts in `Testing\SampleData\push70-store-names\` plus `homedepot-receipt-01.pdf` and `30-thermal-walmart-vizio-tv-protection.pdf`.
