# Deferred and not-started work: story pass (2026-11-10)

Source: the 310 story files under `Stories/`. Each story's Phase, Milestone and Status were read. Status is recorded unevenly: 200 stories have status text, 110 have none. "No status" means no record that anything happened, which is usually not started but can also be built long ago and never logged (M0/M1 foundation). Check before acting.

## 1. Launch gate: planned MVP, not started
| Work | Stories | Note |
|---|---|---|
| Stripe billing: checkout, portal, webhooks, plan page, founder pricing and trial, past-due handling, gating, payment method before trial ends | S1.2.1 to S1.2.8 | All M5, none started. A free one-year license is attached to every account instead. |
| Canceled accounts: 90 days then purge | S1.4.3 | M5, needs a decision on the retention period. |
| Fair-use storage cap | S2.6.3 | M5. |
| Native app wrapper (iPhone and Android) | S9.1.5 | M5. Also blocks the iPhone share sheet (S2.2.11) and a real-device pass. |
| Sharing privacy: personal-information scan and redaction, preview, skip, account switch, shared-items list with withdraw, terms wording | S6.1.6 (reopened), S7.2.2 | Required by the 2026-11-04 decision, nothing built. Code today writes facts-only claims on every upload with no setting. |
| Text-reminder opt-in: phone number, consent box, verification code, STOP/START/HELP | S4.4.4 | Public pages are live; the in-app part is not. Needs the SMS provider. |
| Operator Review screen (`/admin/review`) | S6.1.4 follow-up | API done; only a placeholder route exists. |
| Welcome email; invite links that skip verification | S1.1.1, S9.1.7, S1.3.4 | Not built. |
| Fill the placeholders before launch | S7.2.1 | Mailing address, minimum age, governing law, backup period, lawyer review. |

## 2. Planned MVP candidates, not started
S5.4.1 how-to per way out, S5.4.3 pre-flight checklist, S5.4.10 honest labelling of guidance, S9.2.10 archive items with no coverage left, S3.3.4 search the internet for a card's terms, S3.2.6 purchase channel (online or in store), S9.2.8 returns in progress (a first slice exists), S4.6.1 general reminder record (the table and API exist), S7.7.1 / S7.7.2 / S7.7.5 / S7.7.6 / S7.7.7 service-layer refactors (some are built; the stories carry no status).

## 3. Status text that is probably stale (says not started, but the feature exists)
Verify and update these before planning from them:
- S5.4.11 record money recovered, S9.2.5 dashboard total recovered: Scenario 37 "Money recovered" exists.
- S7.1.8 send feedback, S7.1.9 feedback queue: Scenarios 35 and 38 exist. S7.1.9's list of gaps may still be right.
- S5.4.2 claim steps as data, S5.4.3 pre-flight, S5.4.13 eligibility rules: Scenario 36 "Claim guidance wizard" and claim-guidance models exist.
- S2.4.2 one intake for every document: the intake now reads many kinds (warranty, service record).
- S7.6.4 email: says `IEmailSender` is stubbed; Resend is live.
- M0/M1 foundation (S7.5.x, S7.6.1, S7.6.2, S9.1.1, S9.1.3): built and deployed, no status recorded.

## 4. Not started, v2 and later (by cluster)
| Cluster | Stories | Size |
|---|---|---|
| Partial data: evidence behind a fact, items already owned, manual or nameplate start, serial and model decoding, installer, two sources disagree, vehicle VIN | S2.7.2 to S2.7.15 | 14, all M6 except S2.7.15 |
| Claim guidance: route choice, scripts, last real day, tracking, own steps, drafts for unknown sellers, free-text intake, AI chat | S5.4.4 to S5.4.9, S5.4.15 to S5.4.19, S5.4.21 | 14 |
| Price-drop alerts | S6.8.1 to S6.8.11 | 11, M9 and not planned |
| Extended warranty plans: add from item page, ending or renewing, phone and device plans, home appliance plans, plan types as shared data | S3.4.5, S3.4.10, S3.4.17, S3.4.19, S3.4.20 | 5 |
| Inbox connection and guided forwarding | S2.2.8, S2.2.9 | 2 |
| Settings: region and display, setup checklist, what is worth tracking | S9.8.3, S9.8.4, S9.8.5 | 3 |
| Other: gift receipts, order-total versus line price, store brands, whose items I see (parked) | S2.4.10, S2.4.15, S3.2.10, S1.3.7 | 4 |

## 5. Built in part: the leftovers named in the stories
57 stories record what was left out. The ones that matter:
- **Vehicles:** VIN decoding, readings mined from documents, start rules (S3.5.1 to S3.5.3); a prorated stage read from a document works on the item page only (S3.5.5, S3.5.6).
- **Notifications:** one-click actions in the message (S4.5.4, S4.6.3); weekly digest mode and per-type delivery UI (S4.2.1, S4.4.2); attention levels (S9.2.11); editing an existing reminder (S4.6.2).
- **Documents and extraction:** refund emails read as mail, exchange slips (S2.4.9); reading file bytes that are not stored yet (S2.4.1, S7.6.5); splitting a document over the page limit; extraction cost cap (S2.2.6).
- **Capture:** blur and too-dark warning, crop and rotate, waiting-to-send queue, Wi-Fi-only (S2.2.11); Yahoo and Outlook mail, a Settings > Email page (S2.2.10).
- **Admin:** work-queue counts on the admin home (S7.1.3); audit-trail screen for admin security events (S7.1.5); feedback queue: closing, replies, attachments, search (S7.1.9); evidence list on the admin screen, weights as configuration (S3.2.5).
- **Plans and coverage:** reading cancellation terms from a contract (S3.4.15); the sold-by versus serviced-by picker (S3.4.18); registration rules on shared policies (S3.1.13); product tree phases 2 and 3 (S3.2.8); "not returnable" on existing items (S3.2.11).
- **Return matching:** refund receipt matching to New Items, ending a plan returned with its item, recording money recovered (S5.4.20); undo and matching on model or serial (S9.9.6); "stop suggesting this store" (S9.9.4).
- **Repair orders (this week):** the coverage picker names Powertrain and Bumper-to-bumper (built on branch `picker-labels`, not merged) and keeps the choice when a row is unticked and reticked (not built).
- **Process:** a Dismissed view with Restore (S2.2.5), recompute coverage when a date is firmed up (S3.1.6, waits on S2.7.12).

## 6. Suggested order
1. Decide and build what blocks launch: sharing privacy (S6.1.6), the text opt-in (S4.4.4), Review screen, then Stripe.
2. Fix the stale status text in section 3, so later passes are reliable.
3. Run real repair orders and mine the "added by you" rows.
4. Pick one v2 cluster from section 4 after that: the claim-guidance leftovers and S2.7 partial data are the largest.

## Appendix: every story with no status text (110)
- S1.2.1 Upgrade to paid via Stripe Checkout (MVP / M5)
- S1.2.2 Manage billing in Stripe Customer Portal (MVP / M5)
- S1.2.3 Stripe webhooks keep account status in step (MVP / M5)
- S1.2.4 Plan and billing page (MVP / M5)
- S1.2.5 Founder pricing and trial (MVP / M5)
- S1.2.6 Past-due and canceled handling (MVP / M5)
- S1.2.7 Feature and limit gating (MVP / M5)
- S1.2.8 Add a payment method before the trial ends (MVP / M5)
- S1.2.9 Paid add-ons (future / M8)
- S1.3.4 Invite a person to my account (v2 / M8)
- S1.3.5 Remove a person or leave an account (v2 / M8)
- S1.3.6 A forwarded receipt belongs to the person who sent it (v2 / M6)
- S1.4.3 Canceled accounts: 90 days, then purge (MVP / M5)
- S2.2.1 Unique inbound address per user (v2 / M6)
- S2.2.12 Leave out services and subscriptions, and notice the repeaters (v2 / M8 (proposed))
- S2.2.3 Needs-info review queue (v2 / M6)
- S2.2.7 Suggest skipping receipts that do not need tracking (future / M8)
- S2.4.3 Measure how well documents are read (v2 / M6 (proposed))
- S2.4.4 Check what was read against itself (v2 / M6 (proposed))
- S2.4.5 Keep what the person corrected (v2 / M7 (proposed))
- S2.4.6 Read a PDF from its text, not its page images (v2 / M7 (proposed))
- S2.4.7 Read a protection plan on a receipt, and keep it out of the item (v2 / QA)
- S2.4.8 Read a warranty the receipt only states, and map it to a policy (v2 / QA)
- S2.6.3 Fair-use storage cap (MVP / M5)
- S3.1.7 The item page: read it, then edit it (v2 / unassigned)
- S3.1.8 Lifetime warranties: whose lifetime, and can it be passed on (v2 / )
- S3.1.9 What proof of purchase a warranty asks for (v2 / )
- S3.2.6 Purchase channel: online or in store (MVP / M6 (proposed); wiz)
- S3.2.7 Stores, brands and cards a user adds show as Unverified until verified (v2 / unassigned)
- S3.3.3 Match receipts to cards by last 4 (v2 / M6)
- S3.3.4 Search the internet for a card's terms (MVP / M4)
- S3.3.7 Say what a debit or prepaid card does and does not cover (v2 / unassigned)
- S3.4.3 Add the plan that was bought with an item (v2 / M8 (proposed))
- S3.4.4 A warranty company's page leads to its plans (v2 / M8 (proposed))
- S3.4.6 Waiting period, monthly billing and open-ended renewal (v2 / M8 (proposed))
- S3.4.7 A plan that covers a home and its systems (v2 / M9 (proposed))
- S3.4.8 Plan limits, service fees and asking for service (v2 / M9 (proposed))
- S3.4.9 State-specific versions of a plan agreement (v2 / M9 (proposed))
- S3.5.7 One Add screen: retail purchase or vehicle (v2 / )
- S3.5.8 Leased vehicles (v2 / )
- S4.4.10 Every SMS links to more info (v2 / M8)
- S4.4.4 SMS opt-in and verification (v2 / M8)
- S4.4.6 Quiet hours and timezone (v2 / M8)
- S4.5.5 Star important notifications (future / M8)
- S4.5.7 Real-time updates and toasts (v2 / QA)
- S4.6.1 General reminder record and API (MVP candidate / M6 (proposed))
- S4.6.4 Reminders found by document review (v2 / unassigned)
- S5.2.2 Was my electronic copy accepted? (v3 / )
- S5.5.1 Question: what would help people with disabilities? (open question / none until answere)
- S5.5.2 Share my return story (future, tentat / M8 or later (propo)
- S5.5.3 Accessibility tags and filter on return stories (future, tentat / M8 or later (propo)
- S5.5.4 No-trip returns first (future, tentat / M8 or later (propo)
- S6.1.1 Submission creates a private policy and a candidate (v2 / M7)
- S6.1.2 AI verifies against the official source (v2 / M7)
- S6.1.3 Card terms research agent (v2 / M7)
- S6.1.4 Claims are counted; enough accounts sends one to an operator (v2 / M7)
- S6.1.5 Show how trustworthy shared data is (v2 / M7)
- S6.2.2 Suggest crowd defaults (future / Not planned)
- S6.2.3 Flag disagreement or needed policy splits (future / Not planned)
- S6.2.4 Grow the product catalog from what people buy (future / Not planned)
- S6.3.1 Scheduled job detects crowd-reported changes (v2 / M7)
- S6.3.2 AI checks the change against the official source (v2 / M7)
- S6.3.3 Ask affected users to confirm their policy (v2 / M7)
- S6.3.4 Apply a confirmed change without rewriting history (v2 / M7)
- S6.4.1 Re-verify stale policies (future / Not planned)
- S6.4.2 Monitor official pages for changes (future / Not planned)
- S6.4.3 Seasonal and temporary return windows (future / Not planned)
- S6.4.4 Review implausible or conflicting entries (future / Not planned)
- S6.4.5 Warranty registration deadline nudges (future / Not planned)
- S6.4.6 Price-protection window alerts (future / Not planned)
- S6.4.7 Coverage gap and overlap review (future / Not planned)
- S6.6.1 Upload the official warranty document (v2 / M7)
- S6.6.2 Ask for the document when we have none (v2 / M7)
- S6.6.3 Verify submitted documents (v2 / M7)
- S6.6.4 Watch for new versions of a warranty (v2 / M7)
- S6.7.1 Credit ledger (future / Not planned)
- S6.7.2 Earning rules (future / Not planned)
- S6.7.3 Redeem credits for free months (future / Not planned)
- S6.7.4 Credits page (future / Not planned)
- S6.7.5 Fraud controls (future / Not planned)
- S6.9.1 Read the model and term from an uploaded warranty document (future / M8)
- S6.9.2 Log a document observation (future / M8)
- S6.9.3 Group observations by model line (future / M8)
- S6.9.4 Operator view of the groups (future / M8)
- S6.9.5 Promote a group to a model-level policy (future / M8)
- S6.9.6 Mark a company's terms as depending on a model or a lookup (future / M8)
- S6.9.7 Propose the model-level term for an owner's item (future / M8)
- S6.9.8 Conflicting terms open a review (future / M8)
- S7.1.10 See how the app is being used (v2 / M8 (proposed))
- S7.1.2 Review candidate and disagreement queues (v2 / M7)
- S7.1.6 A limited reviewer role (future / M8)
- S7.5.1 DDL: reference data schema (MVP / M0)
- S7.5.2 DDL: account, user and billing schema (MVP / M0)
- S7.5.3 DDL: purchases, items and coverage schema (MVP / M0)
- S7.5.4 DDL: curation and learning schema (MVP / M0)
- S7.5.5 Migration tooling and seed scripts (MVP / M0)
- S7.5.6 DDL: notification and messaging schema (MVP / M0)
- S7.6.1 Environments and deployment (MVP / M0)
- S7.6.2 Background job scheduler (MVP / M0)
- S7.7.1 Split the pending-item service (MVP / M6 (first thing, b)
- S7.7.2 Program.cs: tasks and registrations out (MVP / M6)
- S7.7.5 Reference and admin controllers use services (MVP / M5)
- S7.7.6 The remaining controllers use services (MVP / M5)
- S7.7.7 A test keeps controllers off the database (MVP / M5)
- S9.1.1 Responsive layout for phone and desktop (MVP / M1)
- S9.1.3 Inline quick-add, expand for details (MVP / M1)
- S9.1.5 Native app wrapper for iPhone and Android (MVP / M5)
- S9.2.10 Archive items with no coverage left (MVP candidate / unassigned)
- S9.2.8 Returns in progress (MVP candidate / M5/M6)
- S9.2.9 Group, filter and search on every list (deferred / unassigned)
