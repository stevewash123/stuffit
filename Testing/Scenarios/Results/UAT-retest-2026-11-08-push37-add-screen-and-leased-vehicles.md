# UAT retest — Push 37: one Add screen and leased vehicles (Nov 8, 2026)

- **Build:** API af55cd8 (started 11:25:43 AM ET), Staging. UI live Push 37 build.
- **Source:** CHANGES-push-37-one-add-screen-and-leased-vehicles-2026-11-08.md (S3.5.7, S3.5.8)
- **Scope:** Steps to try 1–4, plus four extra API checks (X1–X4). This is a targeted retest of those items only. It does not cover every bullet in the notes, and no regression testing was done.

## Results

| Result | Count |
|---|---|
| Steps to try passed | 4 of 4 |
| Extra API checks passed | 4 of 4 |
| Failed | 0 |
| Partial | 0 |
| Inconclusive | 0 |
| Low-priority observations | 2 |

## Setup

- **Seed and migrations:** DB Stager ran one supported seed (same as `--seed`), which returned 200. It verified 180 vehicle models across 17 makers, including Ford Bronco. Migrations PurchasePaidBy and VehicleLease are applied.
- **No reset:** existing accounts and memberships were kept. All test data uses new P37 records.
- **Accounts:**
  - UI tests: Bob (tester2), in his Personal account.
  - API tests: Alice, as owner of the P34-Alice Repairs business account.

## Steps to try

| # | Step | Who / how | Result | Evidence |
|---|---|---|---|---|
| 1 | Add > Retail purchase rules, then Switch to the vehicle form | Bob, UI | **Pass** | Shot 1 |
| 2 | Vehicle with Payment plan and Leased: lease line, note, lease-end to-do | Bob, UI | **Pass** | Shot 2 |
| 3 | Change to Bought: lease line and to-do go | Bob, UI | **Pass** | Shot 3 |
| 4 | Lease mileage reminder: one notice, none on rerun, email off | Alice, API with real clock moves; Bob, UI for the Settings toggle | **Pass** | run-log.jsonl, Gmail, Shot 4 |

### Step 1: Pass

- The Category list has no Vehicles.
- Brand Ford asks the part/accessory question. The tester answered Yes.
- Model Bronco is refused with the expected message, and Save is blocked.
- **Switch to the vehicle form** carried over:
  - make Ford and model Bronco
  - the nickname
  - date 11/08/2026
  - price 12,345
  - seller "P37 QA Seller" (an unverified seller)

### Step 2: Pass

- The vehicle was saved with Paid by Payment plan, Leased, lease end 11/08/2029, 12,000 a year allowed, and a 0.25 fee per mile over.
- Vehicle ID: 01a1bc0e-0e33-7c61-a9ce-e6608d862c9f.
- The vehicle page shows the lease line and the GAP note, worded exactly as in the release notes.
- The lease-end to-do is active and due 11/08/2029.

### Step 3: Pass

- After editing the vehicle to Bought, the lease line is gone.
- The lease-end to-do moved to Done, under the done reminders.

### Step 4: Pass

Tested through the API and the test-clock routes, using real clock moves.

- **4a, one notice:**
  - Vehicle L1 was leased from Nov 8, 2026 with 12,000 miles a year.
  - The clock was moved forward 182 days, to May 9, 2027, and the reminder job was run. The run summary showed `LeaseMileage = 1`.
  - In the app: "P37 Lease L1: halfway through a lease year".
  - By email (Alice's test inbox, 11:41 AM ET): "P34-Alice Repairs: P37 Lease L1: halfway through a lease year".
- **4b, same day again:** `LeaseMileage = 0`, so no duplicate.
- **4c, email turned off:**
  - The Lease mileage check email was turned off and in-app left on. A second vehicle, L2, was got on May 9, 2027, so its first halfway point had not been used.
  - The first run at +364 days was 2 days before L2's point, which was a timing mistake on our side. The clock was reset and moved forward 366 days, to Nov 9, 2027.
  - That run showed `LeaseMileage = 1`. The in-app notice for L2 appeared with email status "none", and no L2 email arrived. A rerun showed 0.
- **4c, Settings toggle in the UI (Bob, Personal account):** Lease mileage check is listed under Expiring, with Email and In-app both on at the start. Turning Email off showed Saved and stayed off after a reload, while In-app stayed on. Email was then turned back on, showed Saved, and both were on after a reload. No other settings were changed and no reminders were run.
- **Clock:** reset to 0 after each run. Final check: Offset 0 at 11:43 AM ET.
- **Setting:** restored to its value before the test (email on, in-app on) and checked at 11:43 AM ET.

## Extra API checks (not in Steps to try)

| # | Check | Result |
|---|---|---|
| X1 | A retail item with Ford model "  bRONCO " is refused on create (400, field `model`). Editing a retail item to Bronco is refused the same way. A vehicle with model Bronco saves (201). | **Pass** |
| X2 | A lease end before the date the vehicle was got is refused on create and on edit (400, `leaseEndDate`). | **Pass** |
| X3 | The lease-end to-do is due on the end date and carries the GAP note. Moving the end date to Dec 15, 2029 moves the due date. Changing to Bought finishes the to-do and clears the lease fields. | **Pass** |
| X4 | The reminder run summary includes the `LeaseMileage` count. | **Pass** |

## Low-priority observations

1. The email says "12000 miles" while the in-app notice says "12,000 miles". Both say "0.25 per mile" with no currency symbol.
2. The model refusal repeats what was typed ("bRONCO is a Ford vehicle") instead of the catalog name "Bronco".

## Test data created

- **Bob, UI:** vehicle 01a1bc0e-0e33-7c61-a9ce-e6608d862c9f (now Bought).
- **Alice, API (P34-Alice Repairs):**
  - L1, vehicle 01a1bc09-1b50-7fc7-ad5f-2b1f24d86e9b (now Bought)
  - L2, vehicle 01a1bc09-26bd-7f42-95de-a2103d18da66
  - retail item "P37 Ford floor mat", 01a1bc0a-c16b-77d0-a5c6-0f4246955fa4

## Evidence

- /workspace/uat/push37-api-findings.md
- /workspace/uat/push37-api/run-log.jsonl
- Screenshots:
  1. Step 1, model guard (Bronco refused): /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/9fc1984ebd3dfbb785c0f473c421094f98cdcebd42eaf3239de66edaf32b0fa3.png
  2. Step 2, saved lease (lease line and GAP note): /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/07be1a839fd271a0132f7377ef3264936e7ee22d313a1e1f4e460f7e8f7dc8df.png
  3. Step 3, changed to Bought: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/12dd9cfe856be002cbda877a010c344ad5685d62a7e64fef704c6beb5f491af8.png
  4. Step 4c, Settings toggle restored (both on): /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/7f7862213690b3bd5279b0a50f942befa0a0bbd0c96ed2b6e5946c39e13f8d14.png
