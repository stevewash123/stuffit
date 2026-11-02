# Build plan: claim guidance, first real slice (2026-11-02)

Replaces the mock refund wizard (`/items/sample/refund`, rules hard-coded in `refund-wizard.page.ts`) with guidance computed on the server from data. Covers S5.4.2, S5.4.13, S5.4.14, S5.4.3 (minimal), S5.4.10 (labelling), S5.4.12 and S9.2.6 for real items, plus S5.4.11 and S9.2.5 (recoveries). Two parallel slices, A and B.

## Principles for this slice
- **Unknown stays unknown.** Where we have no store- or maker-specific guidance, show the *general* guidance for that kind of coverage and say so ("General guidance for a store return. We have not checked this store's own page."). Never invent a store's steps.
- **The server decides, the browser shows.** Rules live in data and run in the API; the UI carries none.
- **Help, never speak for the user.** Nothing is sent to anyone. The page says the company decides and never says a claim will be approved (S5.4.10).
- **Data, not code.** Guidance rows are versioned reference data like policies; the first rows are seeded from a data file, and operators get an editor later (not in this slice).

## Slice A: guidance engine and wizard (API then UI)

### Data (one migration, `ClaimGuidance`)
Table `claim_guide` (reference data, global; versioned like policies):
- `id`, `coverage_kind` (Return | Manufacturer | Store | ExtendedPlan | Card), `benefit_kind` (nullable; for Card), `party_id` (nullable: null = the general guide for this kind; set = this store/maker/issuer's own), `effective_from`, `effective_to`, `source_url`, `verified_at`
- `reasons` jsonb: list of reason keys this route covers: `changed_mind`, `defect`, `damaged_in_transit`, `not_as_described`, `cheaper_elsewhere`, `accidental_damage`, `theft_loss`
- `conditions` jsonb: list of `{ key, text }` conditions on the item (`unopened`, `original_packaging`, `accessories_complete`, `not_misused`, `serial_readable`)
- `proof` jsonb: list of `{ key, text }` things to have ready (`receipt`, `order_number`, `serial_number`, `photos`, `card_statement`, `maker_denial`, `repair_estimate`)
- `steps` jsonb: ordered list of `{ text, url? , phone? }`
- `depends_on` text (nullable, plain words: "needs the maker's warranty tried first"), `closes` text (nullable: "returning the item ends the maker warranty")
- `fees` text (nullable), `notes` text (nullable)
Lookup for a coverage: the party-specific guide effective on the purchase date, else the general guide for the kind (and benefit kind). Seed the general guides for every kind and the card benefit kinds (purchase protection, extended warranty, return protection) from `StuffIt_API/reference-data/claim-guides.json`, importable with the existing `--import-reference` command (follow how brands are loaded). Store-specific rows are NOT seeded in this slice (they need sourced, human-checked terms).

### API
`POST /api/items/{id}/claim-guidance` body `{ reason, answers: { unopened?, originalPackaging?, accessories?, notMisused?, hasReceipt?, ... each true|false|"unsure" } }` returns:
```
{ itemId, reason, generatedFor: date,
  options: [ { coverageId, kind, provider, startDate, endDate, daysLeft (earliest end if approximate), verdict: "applies"|"maybe"|"does_not_apply",
               why: "one plain sentence", best: bool, closes?: text, dependsOn?: text, fees?: text,
               steps: [ { text, url?, phone? } ], bringWithYou: [ { key, text, have: "yes"|"no"|"unknown" } ],
               guidance: { general: bool, sourceUrl?, verifiedAt?, label: text } } ],
  nothingApplies: bool, nearest: [ { text, label: "A request, not a right" } ],
  standingNote: text }
```
Evaluation (server): for each of the item's coverages (not ended unless approximate), pick the guide; `verdict` = does_not_apply if the reason is not in `reasons` or a condition answered "false" fails it or the coverage has ended; `maybe` if any needed answer is "unsure"/missing or the guide is general and the reason is only partly covered; else `applies`. Rank: applies before maybe before does_not_apply; within, soonest closing first; the top applies option gets `best` with the reason. `have` for proof comes from what we already know (receipt attached, serial saved, order number saved). Item must belong to the caller's account (tenant filter); a returned/disposed item gets a 400 with a plain message. Unit tests for the evaluator (each reason, the unknown case, the approximate-date case, ended coverage); integration tests for the endpoint including cross-account isolation.

### UI
- Real wizard at `/items/:id/refund` (keep `/items/sample/refund` as-is): Step 1 reason, Step 2 only the questions that matter for that reason (one per screen on a phone, "Not sure" always available, Back keeps answers), Step 3 the result from the API with numbered tick-off steps, a "bring with you" checklist showing what we already have, "Does not apply" routes visible with the reason, closes/depends-on warnings, and the standing wording plus guidance label (general vs the company's own, source and date when present).
- The item page (S9.2.6): a primary Refund button in the header, hidden for Returned/Disposed items; a panel "Need to return it or make a claim?" Keep changes to `item-detail.page.ts` small and local (another branch edits date logic in the same file).
- Specs for the wizard flow and the result rendering.

## Slice B: money recovered (S5.4.11, S9.2.5)
- Table `recovery` (item_id, account_id, kind: StoreRefund | CardReimbursement | WarrantyPayout, amount, received_on, method (existing `RefundMethod` + card/warranty), note, created_by, created_at), tenant-filtered; migration `Recoveries`.
- API: add, edit, delete a recovery on an item; only a StoreRefund moves the item to Returned (existing `ItemReturn` flow stays as is; reconcile with it: a recorded return with a refund amount already exists, so reuse that data rather than duplicating: decide and document how a StoreRefund recovery relates to `item_return`); card payout and warranty payout leave status alone; undo allowed and audited.
- Dashboard: total recovered (cash separate from store credit and gift cards) on the home page (S9.2.5). Data export gets a `recoveries.csv`.
- UI: "Mark refunded" / "Add a card payout" on the item page, the recovery list on the item, the total on home.

## Not in this slice
Store-specific guides and the operator editor for them; the prepared message (S5.4.4); route comparison across refund vs repair beyond the `closes` warnings (S5.4.5); transit-aware deadlines (S5.4.6); tracking (S5.4.7 beyond what exists); saving attempts (S5.4.15); question bank (S5.4.17); free-text intake and chat.

## Order and merging
Both slices add a migration. Merge Slice B (smaller) first; then regenerate Slice A's migration on top of it so the model snapshot stays linear. Run full suites only after both are merged, one at a time (shared dev/test database).
