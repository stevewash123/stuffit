# UAT retest — Push 37 follow-up on build 7c02bda: vehicle makers, dealers, and scenarios 63–66 (Nov 8, 2026)

- **Build:** API 7c02bda, started 12:33:14 PM ET. UI Last-Modified 12:31:56 PM ET. Staging.
- **Source:**
  - CHANGES-push-37-one-add-screen-and-leased-vehicles-2026-11-08.md, updated revision (5392 B)
  - HANDOFF-push37-7c02bda-retest.txt
  - scenario-63.md to scenario-66.md
- **Scope:**
  - Steps to try 1–4 on the new build.
  - The new Make list and Dealer list rules.
  - Scenarios 63–66.
  - Four extra API checks (X1–X4).
  - Targeted only; no regression testing.
  - Items the notes list as decided, and S65 HIN/year extraction and plate decoding (not built), are left out.
- **Run:** 1:00–1:35 PM ET.
- **Clock:** Offset 0 at the end.

## Results

| Result | Count |
|---|---|
| Pass | 10 (Steps 1–4, X1–X4, Make/Dealer rules, S66) |
| Partial | 3 (S63, S64, S65) |
| Fail | 0 |
| Inconclusive | 0 |

## Deviations and setup

- **Account for scenarios:** S63–S66 were all run in Bob's personal account (tester2). The plans name Alice's personal account for S63 and S65, but Alice has no personal account; her only membership is the P34-Alice Repairs business.
- **API account:** API checks ran as Alice in P34-Alice Repairs, which she owns.
- **S65 make:** Tracker is now a seeded vehicle maker and appears in the Make list, unlike scenario-65.md, which says to type it. Only the model "Pro Team 175 TXW" had to be typed. (DB Stager correction.)
- **No reset:** there was no database reset. Memberships and fixtures were kept, and all new data uses unique P38 names.
- **Seed:** DB Stager ran one supported seed, which returned HTTP 200. Migrations PartyVehicleMaker and PartyDealer are applied. 78 parties are flagged as vehicle makers, and there are 5 shared dealers with no owner:
  - CarMax
  - Carvana
  - AutoNation
  - Camping World
  - Private sale
- **No jobs or clock moves for S63–S66:** reminder lead times in those plans are "verify", and none were shown at clock 0.

## Per-step results

| # | Check | Who / how | Result |
|---|---|---|---|
| 1 | Add > Retail: no Vehicles category, Ford part/accessory question, Bronco refused, Switch carries over Make, Model, nickname, date, price and dealer. Tiles are real radio buttons ("What are you adding?"). Model year starts at 2026. | Bob, UI | **Pass** |
| 2 | Leased vehicle (01a1bc5b-26a9-70a4-a9e7-cb29c46310f1): lease line, GAP note, lease-end to-do due Nov 8, 2029 | Bob, UI | **Pass** |
| 3 | Change to Bought: lease line gone, to-do Done | Bob, UI | **Pass** |
| 4 | Lease mileage reminder (see details below) | Alice, API | **Pass** |
| X1 | Retail model " bronco " refused (400, `model`) on create and on edit. A vehicle with model Bronco is fine. | API | **Pass** |
| X2 | Lease end before the date the vehicle was got: 400, `leaseEndDate`, on create and on edit | API | **Pass** |
| X3 | Lease-end to-do due on the end date. Moving the end date moves it. Bought removes it and clears the lease fields. | API | **Pass** |
| X4 | Reminder run summary includes the `LeaseMileage` count | API | **Pass** |
| MD | Make and Dealer rules (see details below) | UI + API | **Pass** |
| S63 | New Bronco (01a1bc5e-9aca-7b92-bd60-53cbb3361bc4) | Bob, UI | **Partial** |
| S64 | Certified RAV4 (01a1bc63-e4fa-7fe3-ae21-0cc901b5671d) | Bob, UI | **Partial** |
| S65 | Tracker boat (01a1bc6a-f340-796a-9d55-f62a43a491a5) and Mercury part (01a1bc6d-4c90-7eb2-be98-c5e3c3843412) | Bob, UI | **Partial** (mostly matches) |
| S66 | Private-sale Softail (01a1bc6f-ddba-7d43-a13e-b7ff2fe3675e) | Bob, UI | **Pass** |

**Step 4 details:**
- **One notice:** L1 was leased with 12,000 miles a year. The clock moved +182 days, and the run showed `LeaseMileage=1`. The in-app notice and the email were both sent; the email arrived at 1:09 PM ET.
- **Same day again:** `LeaseMileage=0`.
- **Email off:** L2 was got at its own first point. The clock moved another +184 days (366 in total), and the run showed `LeaseMileage=1`. The in-app notice appeared with email status "none", and no email arrived. A rerun gave 0.
- **Restored:** the notification setting went back to its starting value (email on, in-app on), and the clock was reset to 0.

**Make and Dealer details:**
- **Make list:** the 78 seeded makers, including Ford, Toyota, Harley-Davidson and Tracker. Ordinary brands are absent: Abu Garcia, Dyson, KitchenAid, Samsung, Target, Best Buy and Home Depot.
- **Dealer list:** exactly the 5 shared dealers. Best Buy, Home Depot and Target are absent.
- **Dealer vs store:** a dealer is also a store, and a store is not a dealer.
- **Typed entries:** a typed new make or dealer saves as the person's own entry, shown as Unverified. A typed store does not become a dealer.

**Scenario matches:**
- **S63:**
  - Bumper-to-bumper Nov 7, 2026 to Nov 7, 2029, 36,000 miles, 35,982 left.
  - Powertrain ends Nov 7, 2031.
  - Read it offered the vehicle line ($42,500) and the order total ($45,300) separately.
  - No to-do or notices.
- **S64:**
  - Hand-entered certified coverage: Comprehensive to Nov 6, 2027, starting at 28,400 miles with a 12,000-mile limit. Powertrain to Nov 6, 2028 with a 24,000-mile limit. The page labels these as certified or dealer-added, not factory.
  - Exactly one RoadGuard plan, Nov 6, 2026 to Nov 6, 2029.
  - Price kept at $26,000. No to-do, and the earliest end is Nov 6, 2027.
- **S65:**
  - Tracker hull to Nov 7, 2031 and equipment/finish to Nov 7, 2027, with no hour limit.
  - The part is linked ("Part of… installed at 0.8 hours"), with brand Mercury, the model and the serial.
  - Mercury warranty Nov 7, 2026 to Nov 7, 2029, on the part only.
  - The HIN plate photo matches by eye. No registration task.
- **S66:**
  - Private sale wording shown, with no return period.
  - Read it kept Private sale as the seller.
  - Harley-Davidson warranty Nov 7, 2025 to Nov 7, 2027, unlimited miles, transfers to the next owner, clock not restarted, active.
  - No to-do.

## Findings, ranked by severity

### Medium

1. **S63 Powertrain is missing its 60,000-mile limit.** The 2031 end date is right, but there's no mileage limit and no "59,982 left".
2. **S64 protection plan's structured fields are empty.** Company, Price and Contract are blank, and the start shows "Another date" instead of "Same day as the purchase". The provider, contract, $1,800, the $100 fee and the 64,400-mile limit appear only in the plan text.
3. **S64 CPO certificate is offered as one plan instead of two coverages.** The warranty prompt offered one plan, Nov 6, 2026 to Nov 6, 2027, rather than comprehensive and powertrain coverages. It was declined. Hand entry has no coverage-name field, and the Certified box isn't offered for the Protection plan kind. End mileages (40,400 and 52,400) aren't shown as totals.
4. **S65 Read it mis-splits the model "Pro Team 175 TXW"** into Size "175" and Model number "TXW", flagged Not sure.

### Low

5. **S65 part form has no year field** (2026 not recorded) and no "came with the boat" option.
6. **S65 hours rounding and unit:** 0.8 hours shows as "1 hours" in the summary, and the reading unit defaults to Miles for a boat.
7. **No in-service field for New on Add.** It has to be set later in Edit vehicle details (S63, S65).
8. **No odometer date field.** The reading takes the purchase date (S64).
9. **S63 Read it doesn't suggest** the model, VIN, trim, odometer, kind, or New/Bought. The plan allows VIN, year and odometer to be entered by hand; model and trim are misses.
10. **Read it is only available after saving.** The Add form only queues the file.

### Wording and display notes

11. Dealers such as CarMax appear in the retail Store list. This matches "a dealer is also a store", so it's a note only.
12. Fee per mile isn't shown on the vehicle page; it's filled in on the edit form.
13. Save looks enabled on the Bronco refusal but is refused when clicked.
14. The combobox briefly showed stale results when typing fast.
15. Carried over from af55cd8:
    - The lease email says "12000 miles" while the in-app notice says "12,000".
    - "0.25 per mile" has no currency symbol.
    - The refusal repeats the typed casing.

## Fixture issues (not app issues)

- The S63 and S66 VINs (1UATB1BH0T0000063, 1UATBVB10S0000066) fail the VIN checksum, so the app's "does not look like a valid VIN" warning is correct. Regenerate them with a valid check digit.
- In S63, Paid by wasn't chosen before saving from Add, which was a tester gap. Edit screens have no Paid by, and showing Paid by is a decided item.

## Needs code changes

- S63/S65: Read it should keep the warranty's mileage limit (powertrain 60,000) and keep "Pro Team 175 TXW" as one model, with no Size/Model split.
- S64: an accepted protection plan from Read it should fill Company, Price, Contract and the start answer. The Certified box should be offered for plans.
- S64: a multi-term CPO certificate should become one coverage per term, or offer a coverage-name field.
- Part form: add a year field and a "came with the parent" option.
- Boat: default the reading unit to Hours and stop rounding 0.8 to "1 hours" (also fix the plural).
- Add form: an in-service date for New, an odometer reading date, and Read it before saving.
- S63: Read it should suggest the model and trim.
- Bronco refusal: disable Save, or show it as disabled, while the model is refused.
- Combobox: stale results when typing fast.
- Fee per mile on the vehicle page.

## Test data created (P38)

- **Bob (UI):**
  - Lease test vehicle 01a1bc5b-26a9-70a4-a9e7-cb29c46310f1
  - Unknown make/dealer vehicle 01a1bc5d-8785-7b3a-a1f4-b695f5fffe63
  - S63–S66 items as listed in the table above
- **Alice (API, P34-Alice Repairs):**
  - L1 vehicle 01a1bc59-7d20-77f1-bb2c-8fb8fac120d8
  - L2 vehicle 01a1bc59-85c3-76c0-a468-74038067fe5e
  - Floor mat 01a1bc59-db37-7622-b62c-49e3fbb7658c
  - Own maker 01a1bc59-e444-…
  - Own dealer 01a1bc59-e4b5-…
  - Own store 01a1bc59-e533-…

## Evidence

- /workspace/uat/push37b-findings.md
- /workspace/uat/push37b/run-log-p38.jsonl
- /workspace/uat/push37b/parties-readonly.json
- /workspace/uat/p38-ui-findings.md
- /workspace/uat/p38-checklists.md
- Screenshots:
  - **S64:**
    - Order Read it: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/05e6061e75865fc5dac68ef9ea2327ac1d84bab72efadd8fa8db8e6bf212a162.png
    - CPO prompt: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/ade0aff738304f4f0286ea0eda4ef064e933ba742606a3dd02c59ffc7ff6c1e3.png
    - Certified entry: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/426e55f66e5dca733748c131640b1ddfe4e53981c865777d9f6233d3c934a11d.png
    - Plan: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/7741b942b3f6ff53daf6b08918556f25d403352357d390cb1668495b9d47e5b9.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/394140f945b1cebae8d832975e405b515457a8319344282882df6c7c0e84772b.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/13c1be067f9b897a56072475537aa95c93227576381de8ddeeb3a46b03580fd9.png
    - To do: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/fd5feefffb2a112896d2364ea3b2559b4cd0623721f515b9ad28b87c7d1ad54a.png
  - **S65:**
    - Read it split: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/5cbb78496dd4a4121dadf5ab1dcd20982b296b2ff8eec2002e4e7b876d0a30a4.png
    - Hull: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/76989f2eff300d118060d6ab338ac14c36b397169970334a2487d822bd9ee96a.png
    - Part: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/b242a6513e0e1b378abe3398703219788318d3cdf22c6a2986bb590e4788e245.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/f5c66e8bf3cc6a92940be3f4bc53af1c2bfc706f34f9e2431c9f57f38e09fae1.png
    - To do: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/63b7ec6635d0d9cc8294a2663822eccc80afd0ec7158d60ee362b7f7e84940b7.png
  - **S66:**
    - Private sale wording: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/2403ae72f1c4022dd021ecc2a71842f6e4b591cc246f848fdc758aea81680bf7.png
    - Read it seller: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/3857d175400deeba38928b9af81314fed2f34c48c69e70684ea2e31411000bcc.png
    - Warranty: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/225257f4f06619b02274d5aba1a51094bd96da2d107b0ef4c7cce230c2c3ef0d.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/611731c07c0c26b5e0ca333b8ed4e55c59c1ce797c3264d69014ed97dae519c6.png
    - To do and notices: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/02185b1edcba91611a8dfc6bb5752d3fb744fc67cf38a44363d3e7b2dcae369b.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/9abb640bc12549fc74a1740a668a388ba1e62b838d98f4046fdd27ca69aa8976.png
