# UAT retest: push 74 (UI-only), a store the server says to choose starts unticked

- **Build:** UI redeployed 10:07 AM ET Nov 12 2026; API unchanged at `362340d`.
- **Run:** 10:20 to 10:23 AM ET, as Alice, after a hard reload. App clock not moved (offset 0).
- **Scope:** CHANGES-push-74-choose-not-pre-ticked.md, rows 1 to 3. NEXT-REPORT-ADDITIONS.md: none.
- **How I checked:** uploads from a blank `/add/new` with the form's "Upload a receipt or warranty" button; nothing saved. Parties read read-only in Neon.

## Summary: 3 Pass, 0 Fail (fixes the push 73 Medium)

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Store row starts unticked; the update leaves Store empty and creates nothing | **Pass** | The panel opened with Store **unticked**: "Store Target Practice Supplies. Read from the document. Select a store on the form before adding." Brand Bushnell, name, model 202208, price 149.00, date 2026-10-04, order total 157.20 and order number TPS-70070703 were ticked. The main button read **"Keep 1 & Update 7"** (not "Update All" while a row is unticked). Clicked at 10:21:01 AM: Store field empty, the other facts filled, receipt attached, no toast. No party was created at that time. Shots `p74-01-E-panel.png`, `p74-02-E-updated.png`. |
| 2 | Ticking Store on purpose fills it | **Pass** | Ticking Store showed "New store: added to your local data." and the button changed to "Update All". Clicked at 10:21:38 AM: Store field "Target Practice Supplies". Neon shows the private party created at **10:21:38 AM ET**, as the notes describe (created when applied, not on Save; on Save is a later change). Shots `p74-03a-E-ticked-panel.png`, `p74-03-E-ticked.png`. |
| 3 | Sure stores still fill straight away with the toast | **Pass** | No panel. A "Filled in from your document: store Home Depot, brand Milwaukee, …"; B "… store Walmart, brand Vizio, …"; C "… store Lowe's, brand DeWalt, …"; D "… store Sam's Club, brand Samsung, …". Shots `p74-11-A.png` to `p74-14-D.png`. |

## Notes
- **Info:** the button label is "Keep 1 & Update 7" when Store is unticked, so "Update All" in the notes applies only when everything is ticked.
- **Info:** on the Add form, receipts C and D fill no item name, so the Item field stays blank.

## Cleanup
Nothing saved. New Items Waiting and Dismissed empty. The private "Target Practice Supplies" party from step 2 was sent to DB Stager for deletion. Alice signed out.

## Fixtures
No new fixtures. Used the push 70 receipts in `Testing\SampleData\push70-store-names\` plus `homedepot-receipt-01.pdf` and `30-thermal-walmart-vizio-tv-protection.pdf`.
