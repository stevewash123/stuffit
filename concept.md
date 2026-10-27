# StuffIt (working name): concept notes (2026-09-30)

## Goal
Consumer SaaS (Stripe membership) to track warranties and return windows on things you buy, with expiry reminders. MVP = stand it up and see who comes; minimal marketing; keep the option to sell or drive it later. Future: business memberships.

## Differentiators (vs. crowded field, see competitor chart in chat; verify pricing on vendor sites)
- Multi-layer coverage per item: return window, manufacturer, store, extended plan, credit-card benefit
- "Something broke" view: coverages ranked, claim contacts, receipt attached
- Email-in capture (forwarded receipts, incl. Amazon confirmations); v2 after manual entry + upload
- Card-benefit surfacing: join user's card against issuer benefits

## Amazon
No consumer order-history API. Path: email-in (v1/v2), "Request My Data" export import (backfill), browser extension / inbox OAuth scan later. Never credential scraping.

## Data model
**Rule: reference data suggests, user data records.** A coverage row stores its own terms snapshot.

Reference (curated, small): party (one table, role flags: seller/manufacturer/card issuer/warranty provider), seller_policy (by category, nullable = general), manufacturer_policy, card_benefit, plan_type, category. No product catalog.
Policies are versioned: effective_from/effective_to, never edit terms in place (typo fixes are the exception), exclusion constraint (btree_gist) prevents overlaps, lookup by purchase_date. verified_at + source_url on each.

User: account (tenant; household now, business later), user, purchase, item, payment_method (issuer + product only, never card numbers), coverage, reminder, claim, document, inbound_email (review queue). Billing: subscription, stripe_event.

## Future story: crowd-learned defaults (want-to-have)
When many users enter the same value for (manufacturer, category), suggest it as a default for the next buyer. Suggestion only, labeled with source, user confirms.
- Threshold (~20+ samples, ~80% agreement); curated policy outranks crowd
- Only count user-EDITED values as votes (accepted defaults are echo, feedback loop)
- Confirmed items only; reject implausible outliers per category
- **Disagreement is a signal, two possible meanings:** (1) the curated policy is wrong/stale, or (2) the policy is consolidating things that differ and must be SPLIT (e.g. consumer vs pro line, region, model tier). Flag for review; resolution may be a new versioned row, a split by category/line, or a model-key level policy.
- Promote stable, verified crowd defaults into versioned manufacturer_policy (source "crowd, n=N")

### Basic support now (cheap, do in MVP)
- coverage.source (default | user | extracted) and coverage.user_edited boolean
- Aggregate table `coverage_observation` (manufacturer_id, category_id, coverage_kind, term_months, count_edited, count_accepted, updated_at), incremented on confirmed coverage save
- No suggestion UI yet, no review UI yet

## Open decisions
- Who seeds reference data (top ~50 sellers, ~30 manufacturers, ~15 card products): Claude drafts from official pages, Steve approves
- Pricing anchor ~$20-30/yr; free tier ~10 items
- Stack idea: Neon Postgres, Next.js, Stripe (Checkout + Portal + webhooks), R2/S3, Resend, inbound email (Postmark/Mailgun), Claude vision/LLM for extraction
- Next: verify competitor pricing, write Postgres DDL

## Core flow (agreed 2026-09-30)
1. Receipt email arrives (forward or auto-forward) -> parsed into a purchase + items, status per item: Complete or Needs info.
2. Auto-attach what's knowable: seller (from sender/receipt), payment method (match "card ending 1234" to user's payment_method last4), seller return policy (by purchase_date + category).
3. Daily digest (only if something changed): "X purchases added, Y need info". Return-window deadlines close to expiry bypass the digest.
4. In-app "Needs info" queue: e.g. Walmart purchase, store + card attached, manufacturer warranty missing. Dropdown of that manufacturer's known policies (filtered by category) or "Add new policy".
5. User-added policy: works immediately for that user (private), also lands in a candidate queue.
6. AI curation: verify candidate against the manufacturer's official page, dedupe against existing policies + coverage_observation, then promote to global versioned policy. Single-user submissions never auto-publish; promotion needs source verification or crowd threshold; human spot-check early on.

## Payment methods (agreed 2026-09-30)
User adds a card: nickname ("Chase Sapphire"), issuer + card product (picked from reference), last 4 (never full number). Card benefits are user-CONFIRMED: reference card_benefit rows are proposed, user confirms/edits per card (tier and issuer terms vary, benefits change), stored as payment_method_benefit (term, cap, claim window, confirmed_at, source). Reissued cards: keep multiple last4 values with valid ranges on one method so email matching still works. Coverage from a card snapshots the confirmed benefit at purchase time.

## Name (2026-09-30)
Working name "StuffIt". Known: Smith Micro owns the old StuffIt (compression) mark, product EOL 2019-2020; registration status unchecked. Punctuation variants (Stuff-It / Stuff It!) don't reduce risk. Decision: keep the name while this is an experiment; run USPTO search + domain check before spending on brand/logo, and before any sale. Fallback: distinctive add-on ("StuffIt Vault") or new name. "WarrantyKeeper" is an existing competitor (do not use as a name).


## AI curation add-on (v2, 2026-09-30)
Scheduled AI review detects policy changes from crowd signals (e.g. 10 distinct accounts edit a Citi card benefit the same way), verifies against the official source, and asks affected cardholders to confirm their own card's benefit. Also: stale-policy sweep, source-page monitoring, seasonal return windows, anomaly review. Stories: Stories/E6-curation-learning (F6.3, F6.4). Guardrails: distinct accounts only, echo excluded, neutral wording when unverified, changes versioned with existing coverages untouched.

## Notifications + billing revision (2026-09-30)
Studied ConsignmentGenie_UI (C:\Projects\ConsignmentGenie\ConsignmentGenie_UI); lessons in docs/consignmentgenie-lessons.md. The in-app Notification Center (bell + full page, F4.5) is MVP and central: the dispatcher writes in-app records, most prompts land there first, actionable notifications carry the policy-change confirmation. Stripe: portal-first, price lookup keys, trial + founder pricing, past-due handling.

## API study revision (2026-09-30)
Studied ConsignmentGenie_API (notifications backend, Stripe). Lessons appended to docs/consignmentgenie-lessons.md. Single customer role in MVP (membership role column reserved; operator flag separate). New stories: default preferences at signup, email compliance/unsubscribe, email templates, digest batch job, burst consolidation, entitlement gating, payment-method setup, notification DDL. API repo CLAUDE.md contains exposed credentials: rotate them.

## Device strategy (2026-09-30, corrected)
Usage is expected to split roughly evenly between phone and desktop. Phone: capturing receipts, reminders, SMS links. Desktop: entering many purchases, reviewing and cleaning data, import. Design both properly, not a stretched phone layout and not a shrunk desktop one. Plan: keep the Angular signed-in app as one responsive app, installable as a PWA (S9.1.4); keep the API-first design so the UI stays replaceable; publish SEO and marketing pages as a separate static site; add a Capacitor native wrapper only if share-sheet intake, barcode scan or reliable push is proven to matter. Every SMS carries a link to more info (S4.4.10). Open question (low urgency now): Angular vs React for resale appeal; decide before M2 if at all.
## Hosting (decided 2026-09-30)
Localhost for development for a long time. When deploying (S7.6.1): Render. Neon stays the database. Notes for then:
- API: Render web service from a Dockerfile (Render runs .NET through Docker). Paid instance once real users exist: free instances sleep, which would stop reminder and digest jobs.
- UI: Render static site. Keep UI and API on one site so the httpOnly refresh cookie stays first-party: either a rewrite of /api to the API service, or app. and api. subdomains of one domain (CORS with credentials is already enabled).
- Jobs (S7.6.2): Render cron job or an always-on background worker; do not rely on a sleeping web service.
- Secrets: Render environment variables (ConnectionStrings__Default, Jwt__Key); never in the repo.
- Custom domain also serves the SMS short-link domain (S4.4.10).

## Sender addresses (noted 2026-10-01)
Placeholder emails are fine in development. Expected real addresses once the domain is chosen: system@stuffit.com or noreply@stuffittracker.com (domain still open; matters for S7.6.4 email, SMS short links and Render custom domains). The first operator account is whichever email the owner signs up with; any placeholder works until then.
Decision (2026-10-01): sender name and address, reply-to, app base URL and the SMS short-link domain are all configuration (Email:FromName, Email:FromAddress, Email:ReplyTo, App:BaseUrl, Sms:ShortLinkDomain), set per environment (on Render as Email__FromAddress etc.), never hardcoded. Implemented for email: EmailOptions in appsettings.json with placeholder defaults.

## Receipts, retention and contributed documents (decided 2026-10-01)
- Retention: keep files until the user deletes them (default); opt-in auto-delete one year after the last coverage ends, with 30 days notice. Strip location data and shrink photos on upload. Fair-use storage cap per plan. Canceled accounts keep data read-only for 90 days, then purge, with notices. Stories: F2.6, F1.4 (M5).
- Contributed official warranty documents (PDF or screenshot): a user's upload backs their own coverage immediately, but is never "Confirmed" on its own. Statuses: Submitted > Confirmed (checked against the official source) > Superseded, or Rejected. Version watching re-checks the source and raises change signals. Stories: F6.6 (M7).
- Contribution credits (idea): credits only for Confirmed contributions, 10 credits = a free month, bonus for the first few contributors where we have no policy. Validate before building; the main risk is gaming. Stories: F6.7 (M8).

## Crowd data licensing (decided 2026-10-01)
Signing up means contributing to shared data. Shared by default: policy facts (warranty and return terms, durations, conditions, source links) and official warranty documents, through a Share with the community checkbox that is checked by default and can be unchecked per submission (or set account-wide). Never shared and no checkbox for them: purchases, receipts, cards, account data. Terms and signup text say so in plain words, and the accepted terms version and time are stored (S7.2.2).
Trust model: a shared submission is Unverified until either (a) it is verified against the official source, or (b) N independent users (default 3, distinct accounts, accepted suggestions not counted) report the same thing, which makes it Community-reported. Labels shown to users: Verified, Reported by N users, Added by you. A single unverified submission is never shown to other users or used for suggestions. Stories: S6.1.3 to S6.1.5, S7.2.2.
Operator: stevewash123@gmail.com for now (sign up first; then run the make-operator command).

## Administrator (noted 2026-10-01)
Customers have one role. The administrator is the one exception: a flag on the user (is_operator in code, called administrator in the product), checked against the database on every admin request, never in the token. Later the administrator signs in to a different home: a work queue of things needing review (warranty submissions, candidates, change signals, flagged uploads), with a switch to the customer view. Two-step sign-in is required for administrators before launch. A limited reviewer role is possible later if review volume needs help. Stories: S7.1.3 to S7.1.6.
