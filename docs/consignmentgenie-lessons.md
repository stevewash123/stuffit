# Lessons from ConsignmentGenie UI

Source: `C:\Projects\ConsignmentGenie\ConsignmentGenie_UI` (Angular, UI repo only; no backend). Read 2026-09-30. Used as a reference for notifications and Stripe billing. Not copied code; patterns only.

## Notifications: what exists there

**Preference matrix** (`owner/settings/notifications/notifications.component.*`, `models/notification-matrix.models.ts`)
- Shape: categories > events, each event has email / sms / system booleans. Plus contact info (email, phone) and numeric thresholds.
- Served by the API (`GET/PUT /api/owner/settings/notifications`), so categories and events are not hardcoded in the UI.
- Auto-saves on every toggle (partial PUT of only what changed) with a status line: Saving... / Saved automatically.
- SMS checkbox disabled until a phone number exists. The System Alerts category is locked for the system channel.
- Each checkbox has a screen-reader-only label.

**Notification Center** (`shared/components/notification-center.component.*`)
- Full page: filter bar (type, search, from/to date, unread only), card list, pagination (20/page), empty states.
- Card: date and time header, type icon, title, message, metadata chips, unread indicator.
- Card actions: toggle read/unread, primary action button (from `actionUrl` with optional `metadata.actionButtonText`), delete.
- `?focus=<id>` query parameter scrolls to a notification and highlights it for 2 seconds.
- Link to the preferences screen.

**Bell** (`shared/components/notification-bell.component.ts`)
- Unread badge, dropdown of the 5 most recent, click-outside closes, mark read, mark all read, click opens the center focused on that item.

**Service and model** (`shared/services/notification.service.ts`, `shared/models/notification.models.ts`)
- Endpoints: list (paged), unread-count, read, unread, read-all, important (POST/DELETE), delete, preferences.
- DTO: type, title, message, isRead, isImportant, createdAt, readAt, reference ids, actionUrl, metadata, timeAgo.
- Unread count is a BehaviorSubject shared by the bell and the center.

**Real-time** (`services/signalr-notifications.service.ts`): SignalR hub events UnreadCountUpdated, ToastNotification, InfoMessage, JobProgressUpdate; toasts with durations, errors persistent.

## Notifications: what we adopt

- Category > event x channel grid, API-served catalog, auto-save per toggle, locked System Alerts, SMS gated on phone, accessible labels (F4.4).
- Bell + Notification Center + `?focus=` + action button with deep link (F4.5).
- Unread count as one shared source (S4.5.6).
- Real-time push and toasts as v2 (S4.5.7), polling first.

## Notifications: what we fix or avoid

- **Search and date filters in the center UI are never sent to the API** (only type and unreadOnly are). We define all filters in the API first (S4.5.1).
- **Two overlapping preference models**: the matrix plus a separate per-type email-flag DTO with digest mode. We keep one model and store digest mode beside it (S4.4.3).
- **Hardcoded lists**: type filter options and an event-name display-name map live in the UI. Ours come from the catalog (S4.4.1).
- **Browser `confirm()`** for delete, contradicting their own UI guideline. We use the shared modal (S4.5.3).
- **Emoji icons** for types. We use a real icon set.
- **Mark-as-unread** is wired in the service but the component only does an optimistic local update. Ours calls the API (S4.5.1, S4.5.3).
- **Role-specific duplicates** (admin, owner, consignor preference screens and role-prefixed API paths). We have one screen and one scoped API.
- **SignalR reconnect** schedules a new connection both in the start-failure path and in onclose, so connections can stack. Guard against it (S4.5.7).
- **Hardcoded threshold defaults** inside the template (500, 10). Defaults belong in the catalog.
- SignalR is .NET-specific. Our stack needs SSE or WebSockets, with polling as the fallback.

## Stripe and billing: what exists there

- `owner/settings/account/license.component.*`: loads `SubscriptionInfo` (plan, status active | cancelled | past_due | trialing, currentPeriodEnd, nextBillingDate, amount in cents, features[]), shows plan/status/next billing/amount, a Manage Subscription button, and a list of what the portal can do.
- `openBillingPortal()` returns `{ url }` from the backend and the client redirects (`window.location.href`).
- `owner.service.ts` and `shared/services/integration-pricing.service.ts`: per-product pricing by `lookupKey` and `priceId`, `isFounderPricing`, a pricing-impact model (current total, change, new total, billed-now amount of $0 during a trial) shown before enabling or disabling a paid add-on.
- Checkout session creation is not in the UI repo (backend).

## Stripe: what we adopt

- Portal-first, no custom billing UI (S1.2.2, S1.2.4).
- Status set including trialing; plan page with status badge and features list (S1.2.3, S1.2.4).
- Price lookup keys instead of hardcoded price IDs (S1.2.1).
- Founder pricing and trial as configuration (S1.2.5).
- Past-due handling as banner plus mandatory notification (S1.2.6).
- Pricing-impact confirmation is only needed if we ever sell add-ons (business tier, extra storage); parked.

## Open questions

- The ConsignmentGenie backend (API repo) would show how the dispatcher, digest and Stripe webhooks were built. Not available here; look in the repo or server when it's back.
- Their `docs` folder and UI_PATTERNS.md (modal vs page rules) referenced in CLAUDE.md were not in the zip.

---

# Lessons from ConsignmentGenie API (.NET)

Source: `C:\Projects\ConsignmentGenie\ConsignmentGenie_API`. Read 2026-09-30. Reference only.

**Security note.** The API repo `CLAUDE.md` contains live credentials (an email-provider API key and database host, user and password) in plain text, and the file itself says secrets have been committed twice. Treat them as exposed: rotate them, and keep secrets in environment configuration. Values are deliberately not copied anywhere in StuffIt.

## Single role simplifies everything

ConsignmentGenie has owner, consignor, admin and customer roles, and role shows up in preference keys (user, role), API paths (/api/owner/notifications), duplicate screens, and the notification entity (ToType). StuffIt MVP has one customer role, so none of that exists. A membership role column (default member) is reserved for family and business features; operators use a separate flag (S7.5.2).

## Notifications backend: what exists

- **Store first, then fan out** (`EnhancedNotificationService`): every notification is saved, then email and SMS go out per the user preferences. SMS is a stub that only logs.
- **Notification entity**: from/to, ActionStatus (pending, completed, failed, cancelled) with completed at/by, Payload and Metadata JSON, ActionUrl, reference type/id, IsRead/ReadAt, IsImportant, IsAcknowledged (explicit receipt), EmailSent/SmsSent with timestamps, soft delete.
- **Preferences**: JSON matrix per (user, role) of type > email/sms/system, plus BatchPreferences (type > daily or weekly day) and Thresholds (type > number), SMS phone and verified flag. Defaults are created at registration (`DefaultSettingsService`).
- **Bit-packed preferences** (`NotificationPrefsBitPacker`): 18 types x 3 channels in one 64-bit value carried in the login token for fast checks, with database fallback. Clever, but it goes stale until the token refreshes (their own TODO), caps the type count, depends on a fixed index table, and treats unknown types as enabled.
- **Email compliance** (`EmailComplianceService`): encrypted unsubscribe token (90 days), scopes (this type, category, all email), List-Unsubscribe and one-click headers, footer, audit of unsubscribe events.
- **Batches** (`NotificationBatchService` via Hangfire): daily 3:00, weekly 3:30 (seven recurring jobs, one per weekday), monthly 4:00; `CanProcessBatch` and `RecordBatchProcessing` make runs idempotent.
- **Burst consolidation** (`ConsolidatedNotificationService` and `ConsolidatedNotificationJob`): pending row per user and type with item ids, 5-minute debounce that reschedules and appends, atomic claim via ProcessingStartedAt, 5-second grace delay, cleanup after 7 days.
- **Templates**: per-type HTML built from inline strings (`NotificationTemplateService`).
- **Real-time**: SignalR `NotificationHub`.

## Notifications backend: adopt / avoid

Adopt: store-first dispatcher, action status and acknowledgment, per-channel delivery tracking, soft delete, per-type delivery mode and thresholds, defaults at signup, one-click unsubscribe with scopes and audit, batch idempotency records, debounce consolidation with an atomic claim, cleanup of old rows.

Avoid or fix:
- Bit-packing preferences into login tokens (stale, capped, fragile).
- Unknown type defaults to enabled; we default from the catalog.
- Unsubscribe-all also switches off mandatory types; we exempt them.
- Reversible encrypted unsubscribe token; we sign instead.
- Hardcoded sender address and base URL.
- Email audit that only logs.
- Type list duplicated in four places.
- Fixed UTC batch times with no per-user time of day; seven weekday cron jobs instead of one filtered job.
- Debounce without a maximum wait; `Task.Delay` sleeping inside a job; failed consolidation rows never retried.
- Jobs ordered by staggered cron times (2:00, 2:30, 3:00).
- Two overlapping preference entities, one with obsolete columns kept for compatibility.

## Stripe backend: what exists

- **Trial without a card** (`SubscriptionService.CreateTrialSubscription`): Stripe customer plus subscription with a 30-day trial, default payment method saved on subscription, `MissingPaymentMethod = cancel`. Price by lookup key (`base_founder1`, `base_founder2`, `base_regular`). Account id, founder flag and tier in metadata.
- **Founder eligibility** by counting founder accounts (first 10, next 20).
- **Add-ons** as subscription line items by lookup key (`<feature>_founder` or `_regular`); add prorates and charges now, remove applies at period end.
- **Setup-mode Checkout** to collect a card; portal session with return URL.
- **Webhook** (`POST subscription/webhook`): signature verified (`EventUtility.ConstructEvent`), event logged (`SubscriptionEvent`: Stripe event id, raw JSON, processed, error), handles subscription created/updated/deleted and invoice payment succeeded/failed; caches status, period end and active integrations on the organization.
- **Feature gating** (`FeatureGatingService`): base features always for active subscribers, trial gets everything, add-ons by line items, per-feature upgrade prompt.

## Stripe backend: adopt / avoid

Adopt: lookup keys, card-less trial with cancel-on-missing-card, setup-mode card collection, webhook signature check and raw event log, cached status on the account, feature gating from cached state, portal with return URL.

Avoid or fix:
- Two subscription services that disagree (a Basic/Pro/Enterprise tier service with hardcoded fallback price ids and a 14-day trial, and a lookup-key service with a 30-day trial); founder schemes differ ($39/59/79 over 50 slots vs first 10 and next 20). One service, one scheme in configuration.
- Webhook events are only logged when they carry subscription metadata, so invoice events are dropped from the log; no uniqueness on the Stripe event id, so redelivery can double-process; trial_will_end is not handled.
- Founder counting by query is racy under concurrent signups; take the slot in a transaction.
