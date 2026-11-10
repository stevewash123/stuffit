# UAT retest — Push 57: plans they sell, stores as plan sellers, and collision orders (Nov 10, 2026)

- **Build:** API bc87027, started 2:20:09 PM ET. UI redeployed ~2:18 PM ET. Staging. API and UI. **No migration.**
- **Source:** CHANGES-push-57-plans-they-sell.md (SHA256 `f7691bbb6850912678d50c0d70c834daa98f116e66ec2931df521b783b16c124`); TESTPLAN.md; p57-A-notes.md; p57-B-notes.md.
- **Accounts:** Ops (vault 2460773, TOTP) for Admin Shared data and the operator plan-type form; P34 Self personal (vault 3550464) for Stores & brands, Add a plan, and the Scenario 69 re-reads. Ops saw **"A new version of WarrantyCat is ready"** and clicked Reload; P34 Self did not see the banner. Clock Offset 0 (never moved; confirmed after the run).
- **Reuse:** UAT P54 Shared Care Co (`01a1c677-dc79-7b44-aac8-dea0722b550a`), UAT P54 Shared Claims Co (`01a1c677-f090-7374-a0f8-b01000b3dded`), the P54 Care types, and the S69 vehicles. UAT P54 Demo plan was not changed.
- **Fixtures:** none new. Tucson order 08 used **Read it in item Edit mode** on the existing file on **UAT S69 Hyundai Tucson** (https://stuffit-ui.onrender.com/items/01a1c3ac-2e79-7ccd-979d-c676a961710d). Dealer orders 03/06/07/09/12 were also re-read that way; all cards were dismissed with **Not now**.
- **Not reported:** items marked **Not built yet** (person-added types, receipt-to-type matching, seeded providers, the item quick-add type select, phone/device/home appliance plans). Push 58 notes were still a `.hold`; this run started early at Steve's request and is push 57 only.

## Results

| Result | Count |
|---|---|
| Pass | 10 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |

Plus **3 Lows** (first-load empty card / page until a hard reload; Best Buy details line starts with **"· "**; **"Add or confirm plan types"** opens `/admin/companies?type=plans` with the default Needs confirming filter and no company filter). Sub-checks not graded as rows: **"warranty-paid job on a collision order still kept"** is **Inconclusive** (no such line on order 08; no fixture); **"a single paint job on a dealer order does not turn it into a collision repair"** is **untested (Needs fixture)**.

The new-company-as-warranty-provider check is **Pass** after a read-only Neon lookup (`is_warranty_provider = true` on both new parties). The UI itself shows no role prompt or label (noted under that row).

## Per-step results

| # | Check | Result |
|---|---|---|
| 57-sell-ops | Plans they sell on Shared Care Co (Admin) | **Pass** |
| 57-sell-person | Plans they sell on Shared Care Co (Stores & brands) | **Pass** |
| 57-none-ops | Shared Claims Co, operator empty card | **Pass** |
| 57-none-person | Shared Claims Co, person sees no card | **Pass** |
| 57-bestbuy-card | Best Buy store page lists the new type | **Pass** |
| 57-picker | Sold-by / Company picker finds store, maker and warranty company | **Pass** |
| 57-newco | A brand-new company from either picker is a warranty company | **Pass** (SQL) |
| 57-storetype | Store-sold type confirmed, listed on Add a plan, saved on the plan | **Pass** |
| 57-08 | Tucson order 08 is not kept as warranty service | **Pass** |
| 57-dealer | Orders 03, 06, 07, 09, 12 unchanged vs push 56 | **Pass** |

### Plans they sell

**57-sell-ops Pass.** After a hard reload (see Low 1), Admin > Shared data > UAT P54 Shared Care Co (`/admin/parties/01a1c677-dc79-7b44-aac8-dea0722b550a`, header **"Warranty provider" / "Shared"**) shows a complete **"Plans they sell"** card (`s57-A-care-plans.png`):

> Extended warranties and protection plans this company sells, as it publishes them. Your own contract always decides what you have.
>
> - **UAT P54 Care Basic — Confirmed from the company's page**
>   $99.00 a year · claims go to UAT P54 Shared Claims Co · 30 day waiting period · service fee $0.00 to $50.00
>   UAT P54 covers mechanical breakdown of the appliance
>   Cancel within 30 days for a full refund
>   Where this was read (href https://example.com/uat-p54-care-basic)
> - **UAT P54 Care Unconfirmed — Not checked yet**
>   UAT P54 unconfirmed type for the picker
> - **UAT P54 Care Unused — Not checked yet** (no other details; exclusions are not displayed on this card)

The earlier Basic version (ended 2026-11-09) is not shown. **"Add or confirm plan types"** is present for the operator.

**57-sell-person Pass.** Settings > Stores & brands > UAT P54 Shared Care Co (`/settings/stores/01a1c677-dc79-7b44-aac8-dea0722b550a`) shows the same three types, the same confirmed wording and source link, and **no** **"Add or confirm plan types"** link (`s57-B-care-plans.png`). The earlier Basic version is not shown.

**57-none-ops Pass.** Admin > Shared data > UAT P54 Shared Claims Co (`/admin/parties/01a1c677-f090-7374-a0f8-b01000b3dded`): the card reads **"No plans recorded for this company yet."** with **"Add or confirm plan types"** (`s57-A-claims-empty.png`). The link goes to `https://stuffit-ui.onrender.com/admin/companies?type=plans`, Show = **"Needs confirming"** (the default), with no company pre-filter (Low 3). The card does not mention that this company services Care Basic's claims (note only).

**57-none-person Pass.** The person's Claims Co page is **"UAT P54 Shared Claims Co / Warranty provider / Shared data"** and nothing else — **no "Plans they sell" card** (`s57-B-claims-none.png`).

**57-bestbuy-card Pass.** Best Buy (`/settings/stores/01a0f4e4-458d-720b-88fb-277b1120c7bd`, labelled **"Best Buy / Store"**) shows **"Plans they sell"**:

> - **UAT P57 Best Buy Care — Confirmed from the company's page**
>   · claims go to UAT P54 Shared Claims Co
>   UAT P57 store plan covers mechanical breakdown
>   Where this was read

The details line starts with **"· "** because there is no price note (Low 2).

### Pickers and store-sold types

**57-picker Pass.** In the operator plan-type **"Sold by"** picker and in the person's Add a plan company picker, **Best Buy**, **Ford**, **Hyundai**, and **UAT P54 Shared Care Co** were all offered (`s57-A-picker-bestbuy.png`, `s57-B-picker-bestbuy.png`).

**57-newco Pass (SQL).** Adding **"UAT P57 New Seller Co"** from the operator picker and **"UAT P57 Person Seller Co"** from the person picker showed no role prompt or label. Both appear as **"Unverified"** with a creator-only tooltip, and the Ops company also appeared in the **"Claims serviced by"** picker. Read-only SQL on Neon (project `square-tree-53585492`, db `stuffit`):

| Name | id | `is_warranty_provider` | Other role flags | Shared (`owner_account_id` is null) |
|---|---|---|---|---|
| UAT P57 New Seller Co | `01a1c711-f134-717c-bd3e-3d526186a82a` | **true** | seller, manufacturer, dealer, vehicle maker, card issuer all false | no |
| UAT P57 Person Seller Co | `01a1c714-fb88-7ed4-ad71-3d4d19f7aefd` | **true** | same (all false) | no |

Both were created as warranty providers, which is the required behavior. The UI still does not show that role.

**57-storetype Pass.** Ops added **"UAT P57 Best Buy Care"** sold by Best Buy, serviced by UAT P54 Shared Claims Co, coverage **"UAT P57 store plan covers mechanical breakdown"**, and confirmed it with `https://example.com/uat-p57-best-buy-care`. After confirm (Show = Everything): **"UAT P57 Best Buy Care sold by Best Buy , serviced by UAT P54 Shared Claims Co / Confirmed [Change]"** (`s57-A-store-type.png`). The P54 types were not edited.

On Add a plan with Sold by Best Buy, **"What kind of plan is it?"** listed **"Not on the list, or not sure"** and **"UAT P57 Best Buy Care"** (`s57-B-store-type-select.png`). Picking it showed: **"Filled in what it covers from Best Buy's record for UAT P57 Best Buy Care, not from your contract. Check them against your contract. Claims are handled by UAT P54 Shared Claims Co."** The plan was saved as **UAT P57 Best Buy plan** (`/plans/01a1c715-5fa9-7a6a-a5b3-af8ad34033f3`) and the view shows **"Plan type: UAT P57 Best Buy Care"**. The plan form has no item link; the Kettle was attached afterwards via **Cover items** (note).

### Collision and dealer orders

**57-08 Pass.** Tucson order 08, Read it in Edit mode on the existing Precision Collision Center file. Card verbatim (`s57-B-08-card.png`):

> Service on covered parts
> Jun 3, 2026 · 14,022 miles · Precision Collision Center · order PCC-26-0412
> Nothing on this order is service on a covered part. Its odometer reading can still be kept.
> 8 other jobs were left out: not on a covered part. Tick any that should be kept.
> [ ] Front bumper cover and absorber: Replaced bumper cover and absorber with body labor · $0.00
> [ ] Front bumper cover: Refinished (3-stage) · $0.00
> [ ] A/C condenser: Replaced condenser assembly with mechanical labor · $0.00
> [ ] A/C system: Evacuate and recharge with R-1234yf refrigerant · $0.00
> [ ] Front radar: ADAS static calibration (sublet) · $0.00
> [ ] Wheels: Four wheel alignment (sublet) · $0.00
> [ ] Paint materials: Paint and materials for refinish · $0.00
> [ ] Hazardous waste: Hazardous waste removal · $0.00
> The odometer (14,022 miles) is added as a reading.

Clicked **Not now**. The **"warranty-paid job on a collision order still kept"** sub-check is **Inconclusive** (this order has no such line; no fixture). **"A single paint job on a dealer order does not turn it into a collision repair"** is **untested (Needs fixture)** — none of 03/06/07/09/12 has a single paint job.

**57-dealer Pass.** Same keeps as push 56. All **Not now**.

- **09** (`s57-B-09-card.png`): Sep 16, 2026 · 19,880 miles · Seaport Hyundai · order 5590184. Kept: coolant reservoir hose **"repaired under warranty · you paid $0.00 · Powertrain (to Apr 5, 2035)"**; liftgate lift strut LH **"repaired under warranty · you paid $0.00 · Bumper-to-bumper (to Apr 5, 2030)"**; TCM software campaign 9ZZ **"repaired under warranty · you paid $0.00 · Powertrain (to Apr 5, 2035)"**. Left out (1): multi-point inspection and wash. **"This order is already in the service history. Adding it again replaces what it gave; jobs you added by hand stay."**
- **03** (`s57-B-03-card.png`): Jan 15, 2026 · 31,207 miles · Granite Ridge Ford · order 6650291. Recall 25S99 **"repaired under warranty · you paid $0.00"** (no coverage); rear axle pinion seal **"repaired under warranty · you paid $0.00 · Powertrain (to Jun 10, 2028)"**; RH front seat cushion heater **"repaired under warranty · you paid $0.00 · Bumper-to-bumper (to Jun 10, 2026)"**. Left out (1): multi-point inspection.
- **06** (`s57-B-06-card.png`): Feb 11, 2026 · 31,890 miles · Tread Masters Tire & Auto, Store #08 · order 08-561077. Rotate & balance **"you paid $0.00 · Michelin warranty (to Jul 22, 2031)"**; flat repair RR **"repaired under warranty · you paid $0.00 · Tread Masters road hazard protection (to Jul 22, 2028)"**. Wipers **"already added by you"** with no tick box.
- **07** (`s57-B-07-card.png`): Oct 15, 2026 · 61,240 miles · Lakeside Subaru · order 77031. Goodwill CVT valve body **"repaired under warranty · you paid $352.80"** (no coverage). Left out (5): spark plugs $294.20, brake fluid $131.85, MPI & car wash $0.00, shop supplies $16.00, hazmat / disposal $4.50.
- **12** (`s57-B-12-card.png`): Apr 9, 2025 · 41,120 miles · Hillside Garage & A/C · order HG-24518. Kept: CVT fluid exchange **"you paid $282.00 · Powertrain (to Nov 20, 2026)"**; rear differential fluid **"you paid $89.50 · Powertrain (to Nov 20, 2026)"**. Left out (4): A/C $223.95, headlamp $43.99, state inspection $18.50, shop supplies $10.00.

## Lows and notes

1. **Low:** the Admin Shared Care Co **"Plans they sell"** card first showed **"No plans recorded for this company yet."** right after the banner Reload, until a hard reload. The person's Care Co store page first rendered empty (Settings tabs only) until a hard reload. This may be caching or new-bundle timing.
2. **Low:** the Best Buy card details line starts with **"· "** when there is no price note (**"· claims go to UAT P54 Shared Claims Co"**).
3. **Low:** **"Add or confirm plan types"** opens `/admin/companies?type=plans` with the default **"Needs confirming"** filter and no company filter.
4. **Note:** Claims Co's operator card does not mention that it services Care Basic's claims (only sellers' plans are shown).
5. **Note:** the plan form has no item link, so **UAT P57 Kettle** was linked via **Cover items**.

## Test data created

- UAT P57 New Seller Co (`01a1c711-f134-717c-bd3e-3d526186a82a`, Ops, unverified, `is_warranty_provider` true)
- UAT P57 Person Seller Co (`01a1c714-fb88-7ed4-ad71-3d4d19f7aefd`, P34 Self, unverified, `is_warranty_provider` true)
- Type **UAT P57 Best Buy Care** (sold by Best Buy, serviced by UAT P54 Shared Claims Co, confirmed, https://example.com/uat-p57-best-buy-care)
- Item **UAT P57 Kettle** — https://stuffit-ui.onrender.com/items/01a1c714-9517-71fc-b184-d2b0754cfde2
- Plan **UAT P57 Best Buy plan** — https://stuffit-ui.onrender.com/plans/01a1c715-5fa9-7a6a-a5b3-af8ad34033f3

No QA fixture files were made for the share.

## Evidence

- `/workspace/uat/push57/p57-A-notes.md`, `/workspace/uat/push57/p57-B-notes.md`, `/workspace/uat/push57/TESTPLAN.md`
- `/workspace/uat/push57/CHANGES-push-57-plans-they-sell.md`
- Screenshots under `/workspace/uat/push57/shots/`
- Neon read-only: `parties` flags for the two UAT P57 seller companies
