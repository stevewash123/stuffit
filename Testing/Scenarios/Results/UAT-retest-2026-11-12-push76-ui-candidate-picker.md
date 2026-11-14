# UAT retest: push 76 (UI-only), pick between candidates and the app learns

- **Build:** UI Last-Modified Thu 12 Nov 2026 17:37:27 UTC (12:37:27 PM ET Nov 12 2026); API unchanged at `29c6fda` (started 11:25:54 AM ET).
- **Run:** 1:05 to 1:11 PM ET, as Alice then Bob, after a hard reload. App clock not moved (offset 0).
- **Scope:** CHANGES-push-76-candidate-picker.md (S9.10.6; first screen that calls `POST /api/match-feedback`). Also covers the push 75 API steps that were blocked. NEXT-REPORT-ADDITIONS.md: none.
- **How I checked:** uploads from a blank `/add/new` with the form's "Upload a receipt or warranty" button; nothing saved. Parties and `match_feedback` read read-only in Neon.

## Summary: 5 Pass, 0 Fail (also covers the blocked push 75 match-feedback checks)

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Panel offers Target and "None of these"; Store starts unticked | **Pass** | Alice uploaded E at 1:05:26 PM: panel opened. Store row sentence **"Starts like Target, but may be something else."**, radios **Target** (selected) and **"None of these: Target Practice Supplies (new)"**, row **unticked**, no percentages. Other rows ticked: Brand Bushnell [Yours], Name Bushnell Bone Collector 600, Model 202208, Item price 149.00, Date 2026-10-04, Order total 157.20, Order number TPS-70070703. Button **"Keep 1 & Update 7"**. Store and Brand fields empty before Update. Match log store `candidate` middle. Shot `p76-01-E-panel.png`. |
| 2 | Choose Target: shared store, remembered for Alice only | **Pass** | Choosing Target auto-ticked the Store row and relabeled the button **"Update All"**. Clicked at 1:05:46 PM: Store **Target** (no "(new)"), Brand Bushnell; no private party created. Neon: one `match_feedback` row for Alice (field store, key `targetpracticesupplies`, party Target `01a0f4e4-458d-74b3-93f4-481b5cfd0157`, confirmed true, 1:05:47 PM). Shot `p76-02-E-target.png`. Re-upload E at 1:06:03 PM: no panel, Store Target filled; match log rule `user` high → Target. Shot `p76-03-E-again.png`. Bob (second account) at 1:07:49 PM still got the same picker (log `candidate` middle); Update was not clicked. Shot `p76-20-bob-E.png`. |
| 3 | "None of these" after the remembered choice was deleted | **Pass** | DB Stager deleted Alice's row (`01a1d0ef-ee4d-7b70-9f8d-cc4e822643d2`) at 1:09 PM. E at 1:10:31 PM opened the same panel as check 1. Shot `p76-301-E-panel.png`. "None of these" + Update All at 1:10:44 PM: Store **"Target Practice Supplies"**, Brand Bushnell. Private party `01a1d0f4-7576-7abe-8456-34ab4dd9156f` created at 1:10:44 PM; a `match_feedback` row was written (confirmed false, party Target). Shot `p76-302-E-none.png`. Re-upload E at 1:10:55 PM: no panel, no Target candidate; Store filled with her private store and the toast. Match log rule `exact` high → the private party. Shot `p76-303-E-again.png`. |
| 4 | Sure stores still fill straight away with the toast | **Pass** | No panel, 1:06:27 to 1:07:01 PM. A Home Depot / Milwaukee (store and brand `key`); B Walmart / Vizio (store `alias` WALMART SUPERCENTER); C Lowe's / DeWalt (store `alias`); D Sam's Club / Samsung (store and brand `key`). Each showed the "Filled in from your document: store …, brand …" toast. Shots `p76-11-A.png` to `p76-14-D.png`. |
| 5 | Push 75 match-feedback checks that were blocked | **Pass** | Confirm and reject both write correctly and change only Alice's matching: choosing Target stored confirmed=true for Alice and her next upload filled Target; Bob still got the picker. After that row was deleted, "None of these" stored confirmed=false and Alice's next upload no longer offered Target. |

## Notes
- **Info:** choosing a radio auto-ticks the Store row and relabels the button to "Update All" (fine).
- **Info:** no toast after Update from the panel, and none on the 1:06:03 PM `user`-rule re-upload. The toast is shown when the form is filled straight away by the other rules (sure stores, and the 1:10:55 PM `exact` re-upload).
- **Info:** Bob's panel showed Brand Bushnell as "New brand: added to your local data" and had no Name row (button "Keep 1 & Update 6").
- **Info:** Bob's account switcher lists "P34-Alice Repairs" as well as Personal (maybe from an earlier invite).

## Cleanup
Nothing saved. New Items Waiting and Dismissed were empty for Alice and Bob. DB Stager deleted Alice's first `match_feedback` row (`01a1d0ef-ee4d-7b70-9f8d-cc4e822643d2`) at **1:09 PM ET** so the "None of these" round could run. After the run, DB Stager confirmed at **1:12 PM ET** that it deleted Alice's later `match_feedback` row (`01a1d0f4-758c-7c6d-ac04-49741473fc1e`) and the private party Target Practice Supplies (`01a1d0f4-7576-7abe-8456-34ab4dd9156f`) with its name key. Alice has 0 `match_feedback` rows. The shared Target party is untouched.

## Fixtures
No new fixtures this run. Used the push 70 receipts in `Testing\SampleData\push70-store-names\` plus `homedepot-receipt-01.pdf` and `30-thermal-walmart-vizio-tv-protection.pdf`.
