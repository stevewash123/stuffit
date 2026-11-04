# StuffIt Development Plan

Generated from the story dependencies. Milestones are ordered; every story's dependencies are in the same or an earlier milestone.

## M0 Foundation
Environments, schema and plumbing exist. Nothing user-visible yet.

- S7.6.1 Environments and deployment
- S7.5.5 Migration tooling and seed scripts (needs S7.6.1)
- S7.5.1 DDL: reference data schema (needs S7.5.5)
- S7.5.2 DDL: account, user and billing schema (needs S7.5.5)
- S7.5.3 DDL: purchases, items and coverage schema (needs S7.5.5)
- S7.5.4 DDL: curation and learning schema (needs S7.5.5)
- S7.6.3 Private file storage (needs S7.6.1)
- S7.6.2 Background job scheduler (needs S7.6.1)
- S7.6.4 Transactional and inbound email (needs S7.6.1)
- S7.5.6 DDL: notification and messaging schema (needs S7.5.5)

## M1 Accounts & app shell
A user can sign up, log in, and land in an empty, mobile-friendly app with a settings page.

- S1.1.1 Sign up and log in with email (needs S7.5.2, S7.6.1)
- S1.1.2 Reset a forgotten password (needs S1.1.1, S7.6.4)
- S9.1.1 Responsive layout for phone and desktop (needs S7.6.1)
- S9.1.3 Inline quick-add, expand for details (needs S9.1.1)
- S9.8.1 Settings page (needs S9.1.1, S1.1.1)

## M2 Reference data, parties, policies, cards
Stores, manufacturers, policies and cards can be seeded, viewed, created inline and edited.

- S3.2.1 Party and versioned policy tables (needs S7.5.1)
- S3.2.3 Seed initial reference data (needs S3.2.1, S7.5.5)
- S7.1.1 Edit reference data with versioning (needs S3.2.1, S1.1.1)
- S9.5.1 Pick a party or create one inline (needs S3.2.1, S9.1.3)
- S9.5.2 Manage my parties (needs S9.5.1)
- S9.5.3 View a global party (needs S9.5.1)
- S3.2.2 Pick a known manufacturer policy or add a new one (needs S3.2.1, S9.5.1, S9.6.1)
- S9.6.1 Add a policy for a party (needs S9.5.1, S3.2.1)
- S9.6.2 Edit or retire my policy (needs S9.6.1)
- S9.6.3 View policy history (needs S9.6.1)
- S3.3.1 Add a card (needs S7.5.3, S9.1.3)
- S3.3.2 Confirm card benefits (needs S3.3.1, S3.2.1)
- S9.7.1 List, add, edit and remove cards (needs S3.3.1, S3.3.2)

## M3 Purchases & coverage (walking skeleton)
A user can enter a purchase with items and receipt, get proposed coverages, and confirm them. Observation hooks start collecting data.

- S2.1.1 Add a purchase with one or more items (needs S7.5.3, S9.5.1)
- S2.1.2 Attach receipts, manuals, photos (needs S7.6.3, S2.1.1)
- S9.3.1 Create a purchase (needs S2.1.1, S2.1.2, S3.3.1, S9.5.1, S9.1.3)
- S9.3.2 Edit a purchase (needs S9.3.1)
- S9.3.3 Delete or archive a purchase (needs S9.3.1)
- S3.1.1 Add or edit a coverage (snapshot of terms) (needs S7.5.3, S2.1.1)
- S3.1.2 Propose coverages when a purchase is saved (needs S3.1.1, S3.2.1, S3.2.3, S3.3.2)
- S9.4.1 Add or edit a coverage (needs S3.1.1, S3.2.2)
- S9.4.2 Confirm or edit proposed coverages (needs S3.1.2, S9.4.1)
- S6.2.1 Log coverage observations (needs S3.1.1, S7.5.4)

## M4 See it & get reminded
Items list, dashboard, item detail, "something broke" view, and expiry reminders by email with the notification preference grid.

- S9.2.1 Items list with coverage highlights (needs S3.1.1)
- S9.2.2 Dashboard highlights (needs S9.2.1)
- S9.2.3 Item detail page (needs S9.2.1, S3.1.1)
- S5.1.1 Search items (needs S9.2.1)
- S5.1.2 Ranked coverage detail (needs S9.2.3)
- S9.1.2 Empty states and first-run guidance (needs S9.2.1)
- S3.3.4 Search the internet for a card's terms; finder stubbed (needs S3.3.1, S3.3.2)
- S3.3.5 Change the number for a card (needs S3.3.1)
- S3.3.6 Find a card in the catalog, or add one we do not list (needs S3.3.1, S3.2.1)
- S3.3.7 Say what a debit or prepaid card does and does not cover (needs S3.3.1, S3.3.2; migration, so after the desktop merge)
- S4.4.1 Message type catalog (needs S7.5.2, S7.5.6)
- S4.4.3 Dispatcher: store preferences and enforce them on every send (needs S4.4.1, S7.6.4, S4.5.1)
- S4.1.1 Generate reminders from coverage dates (needs S3.1.1, S7.6.2)
- S4.1.2 Daily job sends due reminders (needs S4.1.1, S4.4.3, S7.6.4)
- S4.4.2 Notification preference grid (needs S4.4.3, S9.8.1, S4.5.3)
- S4.5.1 Notification record and API (needs S7.5.6)
- S4.5.2 Header bell and dropdown (needs S4.5.1, S4.5.6, S9.1.1)
- S4.5.3 Notification Center page (needs S4.5.1, S9.1.1)
- S4.5.6 Keep the unread count current (needs S4.5.1)
- S4.4.7 Seed default preferences at signup (needs S4.4.1, S1.1.1)
- S4.4.8 Email compliance and one-click unsubscribe (needs S4.4.3, S7.6.4)
- S4.4.9 Email templates (needs S4.4.1, S7.6.4)
- S1.3.1 Every item has an owner (needs S7.5.3, S1.1.1)
- S1.3.2 Add and remove people on an item (needs S1.3.1)
- S1.3.3 Reminders go to the people on the item (needs S1.3.2, S4.1.2, S4.4.3)
- S9.2.4 People on an item (needs S9.2.3, S1.3.2)

## QA stage
Friends set the app up on their own, use it for a few weeks, and report problems. Between the digests and the launch gate. Entry: deployed somewhere a friend can reach, the leaked credentials and database password rotated, the feedback form (S7.1.8) working. Exit: a few clean weeks, then the M5 launch gate.

- Seed data for ski equipment (brands, warranties by kind of product, retailers), because the first outside tester (Ramesh) skis and his gear is a likely source of receipts; see HANDOFF.md "Current state"
- Admin Data Review screen at /admin/review for verifying shared data (store, brand, alias, card, warranty claims; S6.1.4, S7.1.2): operator steps are API calls today
- S9.2.11 Attention levels (UI for New Items and My Items)
- S5.4.20 Offer to mark an item refunded
- S2.4.7 Read a protection plan on a receipt, and keep it out of the item
- S2.4.8 Read a warranty the receipt only states, and map it to a policy
- S5.4.11 Record money recovered
- S9.2.5 Dashboard total recovered
- S5.4.2 Claim steps as versioned data
- S5.4.13 Eligibility rules as data
- S5.4.14 The real result (replaces the mock refund wizard)
- S5.4.3 Pre-flight checklist
- S4.2.1 Digest content and frequency (needs S4.1.2, S2.2.3, S4.2.3)
- S4.2.2 Urgent deadlines bypass the digest (needs S4.2.1)
- S4.2.3 Digest batch job (needs S4.4.3, S7.6.2)
- S4.2.4 Consolidate bursts of events (needs S4.4.3, S7.6.2, S2.2.3)
- S4.5.7 Real-time updates and toasts (needs S4.5.6)
- S4.5.8 Retention and cleanup (needs S4.5.1, S7.6.2)
- S7.1.8 Send feedback or report a problem (needs S1.1.1, S7.6.4, S4.5.1)
- S7.1.9 Feedback and issues queue (needs S7.1.8, S7.1.3, S7.6.4)

## M5 Monetize & launch
Stripe membership, legal pages, marketing page. Public launch of MVP.

- S1.2.1 Upgrade to paid via Stripe Checkout (needs S1.1.1)
- S1.2.2 Manage billing in Stripe Customer Portal (needs S1.2.1)
- S1.2.3 Stripe webhooks keep account status in step (needs S1.2.1, S7.5.2)
- S7.2.1 Terms, privacy, disclaimer
- S1.2.4 Plan and billing page (needs S1.2.1, S1.2.2, S9.8.1)
- S1.2.5 Founder pricing and trial (needs S1.2.1, S4.4.1)
- S1.2.6 Past-due and canceled handling (needs S1.2.3, S4.4.3, S4.5.2)
- S1.2.7 Feature and limit gating (needs S1.2.3)
- S1.2.8 Add a payment method before the trial ends (needs S1.2.1, S1.2.5)
- S9.1.4 Installable on a phone (PWA) (needs S9.1.1)
- S9.1.5 Native app wrapper for iPhone and Android (needs S9.1.4, S2.2.6)
- S9.1.6 Account menu: cards, plans, insurance and settings hang off Account (needs S9.1.1)
- S2.6.1 Choose how long receipts are kept (needs S9.8.1, S7.6.2, S4.4.3)
- S2.6.2 Strip location data and shrink photos on upload (needs S2.1.2)
- S2.6.3 Fair-use storage cap (needs S1.2.7, S2.1.2)
- S1.4.1 Export everything (needs S7.5.3, S2.6.1)
- S1.4.2 Delete my account (needs S1.2.2, S2.6.1)
- S1.4.3 Canceled accounts: 90 days, then purge (needs S1.2.3, S1.2.6)
- S7.2.2 Crowd-data terms and consent at signup (needs S1.1.1, S7.2.1)
- S6.1.6 Share uploaded warranty documents safely, with redaction preview and opt-out (needs S7.2.2); reopened 2026-11-04
- S7.1.5 Protect administrator access (needs S1.1.1, S7.1.1)
- S7.1.7 Turn administrator two-step sign-in back on before deployment (needs S7.1.5, S7.6.1; release gate, do it last)
- S3.2.4 Verified policies for the most common cards (needs S3.2.3, S3.3.6)

## M6 v2a: Email-in & digest
Forward a receipt, get a draft purchase, see it in a needs-info queue; daily digest.

- S7.7.1 Split the pending-item service (no dependencies; FIRST, before more work on that class)
- S7.6.5 LLM integration and cost control (needs S7.6.1; the remaining wiring needs S7.7.1)
- S2.2.1 Unique inbound address per user (needs S7.6.4, S7.5.4)
- S2.2.2 Extract purchase details from email (needs S7.7.1, S7.6.5, S2.2.1)
- S2.4.1 Document reader: find a list of properties in a scanned document (needs S7.6.5, S2.1.2, S2.6.2)
- S2.2.3 Needs-info review queue (needs S2.2.2, S3.2.2); the screen is F9.9 below
- S2.2.4 De-duplicate forwarded receipts (needs S2.2.2)
- S2.7.1 A purchase date can be approximate (needs S2.1.1, S7.5.3)
- S2.7.2 Evidence behind a fact (needs S2.7.1, S2.1.2)
- S3.1.6 Coverage from an uncertain date (needs S2.7.1, S3.1.2)
- S3.1.7 The item page: read it, then edit it (needs S3.1.2, S3.2.5; built 2026-10-04)
- S2.7.3 Add something I already own (needs S2.7.1, S2.7.2, S1.3.1)
- S2.7.12 Firming up a fact recomputes coverage (needs S2.7.2, S3.1.6, S4.1.2)
- S2.7.14 Two sources disagree (needs S2.7.2)
- S2.7.10 Date clues from context (needs S2.7.1, S2.7.2, S2.7.3)
- S2.7.11 Ask for the one fact that helps most (needs S2.7.2, S3.1.6, S9.2.3)
- S2.7.5 Date from a serial number (needs S2.7.2, S7.5.1)
- S2.7.6 Model number fills in the rest (needs S3.2.1, S2.7.2)
- S2.7.8 The installer is part of the coverage (needs S3.1.2, S3.2.1, S9.5.1)
- S2.7.9 Next steps to recover a missing fact (needs S2.7.1, S2.7.2)
- S2.2.5 Pending items and their API (needs S7.5.3, S2.1.1)
- S3.1.5 Default coverage for a pending item (needs S3.1.2, S2.2.5)
- S2.2.6 A receipt upload becomes a pending item (needs S2.2.5, S2.1.2, S2.2.2)
- S2.2.9 Guided forwarding setup (needs S2.2.1)
- S2.2.11 Capture from the phone: camera first, and the share sheet (needs S2.2.6, S9.1.4)
- S3.4.1 Renter's or homeowner's insurance policy (needs S3.1.1, S2.1.2, S4.1.1)
- S3.4.2 Plans from third-party warranty companies (needs S3.1.1, S4.1.1, S2.1.2)
- S2.7.4 Start from a manual, nameplate photo or registration card (needs S2.7.5, S2.2.5, S2.1.2, S7.6.5)
- S2.7.7 The registration card nobody filled in (needs S2.7.4, S3.1.6, S3.2.1)
- S2.7.13 Match a partial item to the purchase that arrives later (needs S2.2.4, S2.7.3, S2.7.4)
- S9.9.1 New Items list (needs S2.2.5, S3.1.5, S9.1.1)
- S9.9.2 Add Details opens the prefilled form (needs S9.9.1, S9.3.1)
- S9.9.3 Accept into My Items (needs S9.9.1, S2.2.5, S3.1.5)
- S9.9.4 Dismiss: do not track (needs S9.9.1, S2.2.5)
- S9.9.5 Tab names and new-item count (needs S9.9.1, S2.2.5)
- S9.9.6 Each arrival: a new item, or a document for one I already have (needs S9.9.1, S2.2.5, S2.2.11)
- S3.3.3 Match receipts to cards by last 4 (needs S3.3.1, S2.2.2)
- S1.3.6 A forwarded receipt belongs to the person who sent it (needs S1.3.1, S2.2.1, S2.2.2)

## M7 v2b: Curation & change detection
User policies are verified and promoted; crowd-reported changes are detected, verified and confirmed by affected users.

- S6.1.1 Submission creates a private policy and a candidate (needs S9.6.1, S7.5.4)
- S6.1.2 AI verifies against the official source (needs S6.1.1, S7.6.5)
- S6.1.3 Card terms research agent, replaces the S3.3.4 stub (needs S3.3.4, S6.1.1, S7.6.5)
- S7.1.2 Review candidate and disagreement queues (needs S6.1.1)
- S6.3.1 Scheduled job detects crowd-reported changes (needs S6.2.1, S7.5.4)
- S6.3.2 AI checks the change against the official source (needs S6.3.1, S6.1.2)
- S6.3.3 Ask affected users to confirm their policy (needs S6.3.2, S4.4.3, S4.5.4)
- S6.3.4 Apply a confirmed change without rewriting history (needs S6.3.2, S3.2.1)
- S4.5.4 Actionable notifications (needs S4.5.3)
- S6.6.1 Upload the official warranty document (needs S2.1.2, S3.1.1)
- S6.6.2 Ask for the document when we have none (needs S6.6.1, S3.1.2)
- S6.6.3 Verify submitted documents (needs S6.6.1, S6.1.2, S7.1.2)
- S6.6.4 Watch for new versions of a warranty (needs S6.6.3, S6.3.1, S6.4.2)
- S6.1.4 Unverified until enough people agree (needs S6.1.1, S6.2.1)
- S6.1.5 Show how trustworthy shared data is (needs S6.1.4)
- S7.1.3 A different home for the administrator (needs S7.1.2, S6.1.4, S6.6.3)
- S7.1.4 Switch between admin and customer view (needs S7.1.3)

## M8 Future / unconfirmed
Channels beyond email, crowd suggestions, and unconfirmed AI sweeps. Schedule only if the product earns it.

- S2.7.15 Vehicles: VIN gives the rest (needs S2.7.2, S2.7.6, S2.7.1)
- S2.2.7 Suggest skipping receipts that do not need tracking (needs S2.2.5, S9.9.4)
- S2.2.8 Connect an inbox, read-only (needs S2.2.5, S2.2.2, S2.2.7)
- S2.2.10 Connect a mailbox with an app password, IMAP (needs S2.2.5, S2.2.2, S2.2.9); sequence vs S2.2.9 open
- S1.3.4 Invite a person to my account (needs S1.3.2, S7.6.4)
- S1.3.5 Remove a person or leave an account (needs S1.3.4)
- S4.4.4 SMS opt-in and verification (needs S4.4.3)
- S4.5.5 Star important notifications (needs S4.5.3)
- S4.4.6 Quiet hours and timezone (needs S4.4.3)
- S9.8.2 Choose a color theme (needs S9.8.1)
- S1.2.9 Paid add-ons (needs S1.2.3)
- S4.4.10 Every SMS links to more info (needs S4.4.4, S4.5.1, S4.5.3)

- S7.1.6 A limited reviewer role (needs S7.1.3)

## M9 Price-drop alerts
Same-store price-drop alerts during the return window (F6.8). Not curation; schedule after launch.

- S6.8.1 to S6.8.8 (see F6.8; S6.8.4 same store only)

## Not planned
Kept for the record, not scheduled. Validate each idea before it is built.

- S6.2.2 Suggest crowd defaults (needs S6.2.1)
- S6.2.3 Flag disagreement or needed policy splits (needs S6.2.1, S6.1.2)
- S6.4.1 Re-verify stale policies (needs S6.1.2)
- S6.4.2 Monitor official pages for changes (needs S6.3.2)
- S6.4.3 Seasonal and temporary return windows (needs S3.2.1)
- S6.4.4 Review implausible or conflicting entries (needs S6.1.2)
- S6.4.5 Warranty registration deadline nudges (needs S3.2.1)
- S6.4.6 Price-protection window alerts (needs S3.3.2)
- S6.4.7 Coverage gap and overlap review (needs S3.1.1)
- S6.7.1 Credit ledger (needs S6.6.3)
- S6.7.2 Earning rules (needs S6.7.1)
- S6.7.3 Redeem credits for free months (needs S6.7.1, S1.2.3)
- S6.7.4 Credits page (needs S6.7.1)
- S6.7.5 Fraud controls (needs S6.7.2)

## Short-term order (reassessed 2026-10-20)

The milestones above say what depends on what. This is the order to build in now, while image intake is still being tested and polished. Capture is mostly built (upload, camera, multi-page scan, email parsing, IMAP mailbox, the reader, returns and refunds). Reminders exist. What is missing is the payoff (what to do when something breaks), digests, and the launch gate.

1. Finish what is half-built (a few days)
   - S9.2.11 Attention levels: the API side exists; build the New Items and My Items UI.
   - S5.4.20 Offer to mark an item refunded: the rest (match a refund email to an item, show the item as returned).
   - S2.4.7 Protection plan on a receipt, and S2.4.8 a warranty the receipt only states: the two intake gaps that most affect coverage accuracy.
2. Money recovered: S5.4.11 Record money recovered, S9.2.5 Dashboard total recovered. Small now that Returned is a real status.
3. Claim guidance, core slice (the main build): S5.4.2 claim steps as versioned data, S5.4.13 eligibility rules as data, S5.4.14 the real result, S5.4.3 pre-flight checklist. Replaces the mock refund wizard. Leave S5.4.17 to S5.4.19 (question bank, free-text intake, AI chat) for later.
4. Digests: S4.2.1 to S4.2.4, then S4.5.7 and S4.5.8. Do this before anyone outside the household uses the app; step 3 moves ahead of it only if no one else is about to use it.
5. Launch gate (when going public; needs decisions on pricing and the sender domain): Stripe S1.2.1 to S1.2.8, S1.4.3, S2.6.3, S9.1.5 native wrapper, S7.1.7 administrator two-step sign-in. Also: rotate the leaked credentials and the database password, and check how deployment (S7.6.1) really stands.

QA stage comes after step 4 and before step 5.

Not now: F2.7 partial data (S2.7.3 with S2.7.2 is the one slice to take if wanted), E6 crowd data, E8 business accounts, SMS and push, F5.5 accessibility returns.

## Notes

**Critical path to MVP:** S7.6.1 > S7.5.5 > S7.5.1-3 > S1.1.1 > S9.5.1 > S2.1.1 > S3.1.1 > S3.1.2 > S9.2.1 > S4.1.1 > S4.1.2. Everything else hangs off that spine and can run in parallel.

**Not in any milestone (features with no detail stories yet):** F1.4 data export/deletion, F2.3 Amazon import, F2.4 photo OCR, F2.5 inbox connect, F4.3 push, F5.2 claim log, F5.3 export/report, F6.5 recalls, F7.3 operations, F7.4 marketing site, E8 business membership. F7.3 and F7.4 need stories before M5.

**Cut-line options for a thinner MVP (decide later):**
- Launch free-only after M4 and add Stripe (M5) once people show up. Reminders are the hook; billing can follow.
- In M4, ship the dispatcher (S4.4.1, S4.4.3) with fixed email defaults and defer the grid UI (S4.4.2) one step.
- S9.6.x policy editing and S9.5.2 party management could trail M3 if seeded reference data is good enough.

**Soft dependencies (not enforced above):**
- S3.2.2 and S9.5.1 say user-created items enter the candidate queue. In MVP they are private only; the queue (S6.1.1) arrives in M7, so keep the candidate flag in the schema (S7.5.4).
- S6.2.1 observation logging is in M3 so data accrues from the first confirmed coverage.
- S7.1.1 needs an admin role from S1.1.1.

**Source of truth:** story files now carry Milestone and Depends on. PLAN.md was generated from them; if you change a dependency, update both.


