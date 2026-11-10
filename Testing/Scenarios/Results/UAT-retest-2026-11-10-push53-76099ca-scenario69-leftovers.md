# UAT retest — Push 53: Scenario 69 leftovers and push 52 Medium (Nov 10, 2026)

- **Build:** API 76099ca, started 10:27:17 AM ET. UI ~10:26 AM ET. Staging. API and UI. No migration. Reader prompt service-record-v5 (order 08 must be re-read).
- **Source:** CHANGES-push-53-scenario69-leftovers-2026-11-10.md (SHA256 `66ddb43cd4517ec69cc116a6743144ddf51f9f07b0e88b0944bf5c928afea1a6`); p53-findings.md. (CHANGES-build-cf4a117 was a prior no-behavior pin, not this build.)
- **Account:** P34 Self personal. Already signed in. No new-version banner, even after a reload (`s53-01-banner.png`). Steve's laptop went offline during the run, so browsing went over the box's network; the app was not affected.
- **Clock:** Offset 0 (never moved; confirmed after the run).
- **Fixtures:** none new. Nothing was uploaded; re-reads used **Read it** in item Edit mode on existing files.
- **Left on test data:** a hand-added wipers row on F-150 order 06, and a "Tire rotation, 7,500 mi" maintenance task on the F-150 tire part.
- **Not reported (Not done):** other Lows not listed in the notes; plan types, phone and home appliance plans.

## Results

| Result | Count |
|---|---|
| Pass | 5 |
| Partial | 1 |
| Fail | 1 |
| Inconclusive | 0 |

## Per-step results

| # | Check | Result |
|---|---|---|
| 53-merge | Order 06 re-add replaces differently worded hand-added rotation and flat-repair rows | **Pass** |
| 53-wipers | After adding wipers by hand, a re-read shows "already added by you" and stays hand-added | **Partial** (Low, Needs CC) |
| 53-twojobs | "Rotate & balance" and "Mount & balance" stay two rows | **Pass** |
| 53-maint | Tire part has a Maintenance panel; rotation 7,500 mi from order 06; toaster has no panel | **Pass** |
| 53-match | "Tire rotation" matches the rotate-and-balance job, not flat repair or wipers | **Pass** |
| 53-untick | Order 12: kept jobs have tick boxes; untick CVT, Add saves only the rest | **Pass** |
| 53-08 | Tucson body-shop order 08 lists condenser, refrigerant, labor, and sublet as jobs | **Fail** (Medium, Needs CC) |

### 53-merge — Pass

F-150 order 06 history **before** had four Feb 11 rows, with the two hand copies next to the rules' rows (`s53-06-hist-before.png`): "Rear tire: Flat repair - plug/patch ... billed to road hazard plan RH-08-552190 · added by you" and "Tires: Rotate & balance - lifetime (no charge) · added by you".

After Read it + Add, **two rows**, neither "added by you" (`s53-06-hist-after.png`):
- "Rear tire: Flat repair RR - plug/patch (nail in tread) · repaired under warranty · you paid $0.00 · Tread Masters road hazard protection (to Jul 22, 2028)"
- "Tires: Rotate & balance - lifetime · you paid $0.00 · Michelin warranty (to Jul 22, 2031)"

ODD: the reader's wording for the same jobs changed from push 52 ("Rear right tire: Flat repair plug/patch" became "Rear tire: Flat repair RR - ..."; "Rotate & balance (lifetime, original invoice 08-552190)" became "Rotate & balance - lifetime").

### 53-wipers — Partial (Low, Needs CC)

Wipers were added by hand from a re-read (tick, picker default **"No coverage (history only)"**, "Add to service history, with 1 left-out job"). History: "Wiper blades: Wiper blade 22\" all-season x2 · you paid $49.98 · added by you".

Reading 06 again, the card showed only the two kept jobs plus **"Untick a job that should not be kept."** There was **no wipers row**, **no "already added by you"**, and **no left-out line** (`s53-06-wipers-card.png`). After Add, the wipers stayed as one hand-added row (`s53-06-wipers-hist.png`) — the **"stays hand-added"** part passes; the **"shows already added by you"** part is missing. Feb 11 now has three rows.

### 53-twojobs — Pass

Order 05 "Wheels/tires: Mount & computer balance · you paid $100.00 · Michelin warranty (to Jul 22, 2031)" and the Feb 11 "Rotate & balance - lifetime" row remain **separate**.

### 53-maint / 53-match — Pass

The tire part's **Edit** mode shows a Maintenance panel: "Upkeep your warranty asks for. We work out when it is next due from your service history and remind you before it lapses." Added "Tire rotation" every 7,500 mi: **"Tire rotation · Overdue · Every 7,500 miles · Last done Feb 11, 2026 at 31,890 miles. Was due by 39,390 miles."** Overdue because the latest reading is 45,050. It counted the rotation, not the flat repair or wipers. The "Rotated tires" wording was not testable (no fixture with that text). UAT P50 Toaster A has **no** Maintenance panel in view or Edit mode. (`s53-maint-part.png`, `s53-maint-toaster.png`)

### 53-untick — Pass

Order 12: both kept jobs have tick boxes, with **"Untick a job that should not be kept."** under the list. Unticked the CVT fluid exchange ($282.00) and Add. Outback history now has the CVT valve body (Oct 15, 2026, $352.80, repaired under warranty) and Rear differential $89.50 **Powertrain (to Nov 20, 2026)** — **no CVT fluid row**. (`s53-12-card.png`, `s53-12-hist.png`)

### 53-08 — Fail (Medium, Needs CC)

Tucson file `08-invoice-body-shop-tucson-collision-ac-condenser.pdf` was already on the item; Read it was run after the deploy. Card (`s53-08-card.png`):

- "Jun 3, 2026 · 14,022 miles · Precision Collision Center · order PCC-26-0412"
- "Nothing on this order is service on a covered part. Its odometer reading can still be kept."
- "The odometer (14,022 miles) is added as a reading."

No jobs were listed (condenser, refrigerant, labor, and sublet all missing). Clicked **Not now**.

**Question for CC:** it is unclear whether Read it re-ran the v5 prompt or reused a stored read from before this build.

## Needs code / product follow-up

1. **Medium, Needs CC:** order 08 still lists no jobs after a post-deploy Read it. Confirm whether a stored read was reused; if so, a true v5 re-read (or a way to force one) still needs to be checked. If v5 did run, the body-shop lines still need to appear as kept or left-out rows with tick boxes.
2. **Low, Needs CC:** a left-out job already added by hand should show **"already added by you"** on the re-read card (and not disappear from the left-out list). Staying in history after Add already works.

## Evidence

- `/workspace/uat/push53/p53-findings.md`
- `/workspace/uat/push53/CHANGES-push-53-scenario69-leftovers-2026-11-10.md`
- Screenshots under `/workspace/uat/push53/shots/`
