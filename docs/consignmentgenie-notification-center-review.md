# ConsignmentGenie Notification Center: deep review vs WarrantyCat (2026-10-05)

Source: V1 (`C:\Projects\ConsignmentGenie`, API last commit 2026-03-30). V2 has no notification code. This goes below the 2026-09-30 summary in `consignmentgenie-lessons.md`; read that first for the overview. Here: what V1 actually does line by line, the defects found, and a gap check against what WarrantyCat has built (not just what its stories say).

## 1. What V1 is, in one picture

```
feature code ──> INotificationService.CreateAsync(CreateNotificationRequest)
                   1. INSERT Notification row (always)
                   2. look up prefs (JWT bit-claim -> else DB matrix)
                   3. email: pref on? -> CanSendEmail (compliance) -> build + footer + List-Unsubscribe -> Resend
                      sms:   pref on? -> stub (logs only)
                   4. set EmailSent / SmsSent flags
Hangfire: daily 3:00 / weekly 3:30 x7 weekday jobs / monthly 4:00 batches; 5-min debounce consolidation job
SignalR NotificationHub: only pushes "UnreadCountUpdated" after read/unread/read-all
UI: bell (5 latest, badge) -> /{role}/notifications (center, ?focus=id) -> preferences grid
API: one abstract NotificationsControllerBase, one subclass per role (Owner/Consignor/Admin), route /api/{role}/notifications
```

Files: `Core/Entities/Notification.cs`, `Application/Services/EnhancedNotificationService.cs` (997 lines), `NotificationPreferenceService`, `EmailComplianceService`, `NotificationBatchService` (689), `ConsolidatedNotification{Service,Job}`, `NotificationTemplateService`, `Core/Utilities/NotificationPrefsBitPacker.cs`, `API/Controllers/NotificationsControllerBase.cs`, `API/Hubs/NotificationHub.cs`; UI `shared/components/notification-{bell,center,preferences}.component.*`, `shared/services/notification.service.ts`, `services/signalr-notifications.service.ts`, `shared/config/notification.config.ts`.

## 2. Defects and traps found in V1 (new vs the 09-30 notes)

| # | Finding | Evidence | Lesson for WarrantyCat |
|---|---|---|---|
| 1 | **The "ultra-fast" JWT-claims preference path can never work for the common case.** `GetPackedPreferencesFromClaims` reads the claim off the *current HTTP request's* user and then rejects it unless it equals `ToUserId`. Notifications are mostly sent to someone else (owner action notifies a consignor; job has no HTTP context), so it always falls through to the DB path. When sender = recipient the claim is stale until re-login (their own TODO). | `EnhancedNotificationService.cs:949-990` | Already avoided (DB + 60 s cache). Keep it that way. |
| 2 | **The list endpoint drops most of the record.** `GetNotificationsAsync` selects 11 columns and maps to the DTO without `IsImportant`, `ActionStatus`, acknowledgment, from/to, or `Metadata`; `Metadata` is deserialized from `Payload`, not the `Metadata` column. The important flag and action status are written but never come back. | `:489-575` | Test the DTO round trip (write field -> list -> field present). WarrantyCat `ToDto()` includes them; add a contract test. |
| 3 | **Two JSON columns with unclear roles** (`Payload` and `Metadata`) plus **five typed FK columns** (`ItemId`, `TransactionId`, `PayoutId`, `StatementId`, `ItemRequestId`) plus generic `ReferenceType/ReferenceId`. Three ways to say "what is this about". | `Notification.cs` | WarrantyCat uses generic reference + one `Payload`. Good. Don't add typed FKs. |
| 4 | **Four separate lists of notification types** that must agree: `NotificationTypes` constants, `NotificationType` enum, bit-packer index table (16 entries, comment says 18), and `notification.config.ts` (+ filter options hardcoded in the center HTML, and the center's filter values `manifest/payout/sale` do not match the API's type strings `item_sold/payout_processed`, so the Type filter silently returns nothing for most). | `Constants/NotificationTypes.cs`, `Enums/NotificationType.cs`, `NotificationPrefsBitPacker.cs`, center html | WarrantyCat has one `NotificationCatalog`. Keep; add a test that every key in the UI's icon/label maps exists in `GET /api/notification-types`. |
| 5 | **Unknown type = enabled** (bit-packer and DB path both return true), so any new type spams everyone until they notice. Unsubscribe-all also clears mandatory types. | `IsEnabled`, `ProcessUnsubscribeAsync` | Already fixed in WarrantyCat (catalog default; mandatory exempt). |
| 6 | **Inbox is scoped by (user, role)** (`ToUserId == userId && ToType == role`). One person with two roles has two disjoint inboxes and two unread counts. The bell needs `role` as an input and hits `/api/{role}/...`. | `GetNotificationsAsync`, `GetUnreadCountAsync` | N/A: WarrantyCat is single role. If a household/business role arrives, scope by account + user, not a role string in the route. |
| 7 | **Email sent inline in `CreateAsync`, exceptions swallowed**, only a boolean `EmailSent` (no failed state, no error, no retry). A mail outage silently loses email forever while the row says nothing. | `SendEmailNotificationAsync` catch block logs only | WarrantyCat has `DeliveryStatus` + `RetryFailedEmailsAsync`. Verified: scheduled hourly in `Jobs.cs`. |
| 8 | **Compliance footer and unsubscribe link added to every email** including password-reset-style system mail; token is reversible encryption of JSON, 90-day expiry, one-click POST header present. Audit table exists (`RecordEmailSentAsync`) but the audit is a log line. | `EmailComplianceService.cs` | WarrantyCat: signed HMAC token, no link on mandatory types, `EmailUnsubscribeEvent` persisted. Ahead. |
| 9 | **Template merge is raw string replace** (`{Key}` -> value) into HTML with no encoding. A consignor name or item title containing markup lands in the owner's email as HTML. | `NotificationTemplateService.RenderString` | Check `NotificationEmailBuilder`/`EmailTemplates` HTML-encode every substituted value (the unsubscribe footer uses `enc(...)`; verify the body vars too). |
| 10 | **SignalR hub joins groups (`User_{id}`, `Role_{role}`) that nothing sends to**; the controller broadcasts with `Clients.User(userId)`, which relies on the default user-id provider. The hub carries only the unread count; new notifications do not push, so the bell only changes after a read action or reload. The client reconnect logic schedules a new connection in both the failure path and `onclose` (stacking). | `NotificationHub.cs`, `signalr-notifications.service.ts` | When doing S4.5.7: push the notification itself (not just a count) over SSE/WebSocket, one reconnect owner. Polling (60 s) is a fine v1. |
| 11 | **Batch jobs**: weekly = seven recurring jobs (one per weekday); all fixed UTC times; ordered by staggering cron times (2:00/2:30/3:00); `CanProcessBatch` idempotency table is good. Daily "payout ready" and sales summary batches build per-user reports in memory. | `NotificationBatchService.cs`, Hangfire registration | WarrantyCat `BatchRun` copies the good part; the hourly per-user-timezone job is the right replacement for fixed UTC. |
| 12 | **Consolidation job**: debounce 5 min, atomic claim via `ProcessingStartedAt`, then `Task.Delay(GRACE_PERIOD_SECONDS)` *inside* the job (holds a worker), no max-wait so a steady trickle postpones forever, failed rows never retried, cleaned after 7 days. | `ConsolidatedNotificationJob.cs` | WarrantyCat has `PendingConsolidation` with `FirstEventAt`: use it to cap the wait (send at min(last+5 min, first+30 min)). |
| 13 | **Center UI**: Search, From and To fields exist but are never sent to the API; Type filter values mismatched (see 4); "mark unread" is local-only in the center though the API endpoint exists; delete uses the confirm service; pagination `unreadCount` is computed from the current page only (so "Mark all read" button disabled-state is wrong on later pages); `?focus` highlight works but only if the item is on page 1. | `notification-center.component.*` | WarrantyCat API already supports q/from/to/important/actionStatus; check the Angular page sends them and that `?focus=` loads the right page (see section 4). |
| 14 | **Third preference model**: `UserNotificationPreference` (per type: Email/Sms/Slack/Push enabled, `QuietHoursStart/End`, `InstantDelivery`) sits unused beside `NotificationPreferences` (matrix JSON) and the obsolete column set. Quiet hours were designed but never enforced. | `Entities/UserNotificationPreference.cs` | Good shape for S4.4.6 (quiet hours), but store as user-level columns, not per type. |
| 15 | **Actionable notifications are done right in V1**: `CompleteNotificationActionAsync(referenceId, referenceType, completedBy)` flips every `pending` notification pointing at that thing to `completed` with who/when. Callers call it when the owner approves/imports. `AcknowledgeNotificationAsync` also marks read. | `:838-925` | **WarrantyCat has the column, DTO and filter but nothing writes it** (section 4). This is the main thing to copy. |

## 3. Pieces of V1 worth lifting (concretely)

1. **Complete-by-reference** (`CompleteNotificationActionAsync`). Signature `(referenceType, referenceId)`; pending -> completed, set `ActionCompletedAt`, mark read. Call it from the handlers that resolve the underlying thing: item returned/marked, coverage confirmed, card benefits confirmed, to-do done/dismissed, receipt entered, extended plan added. Cancel (`Cancelled`) when the thing is deleted or the window passes.
2. **Acknowledge also marks read** (WarrantyCat does this? `Acknowledge` sets acknowledged only, not read; add it).
3. **Notification `Payload` carrying display metadata** with a small typed shape (`ActionButtonText`, item title, amounts) used by both email and card chips. WarrantyCat `Payload` is a string map used for URL templating and the action label comes from the catalog; if a type ever needs a per-instance label, allow `Payload["actionLabel"]` to override.
4. **`?focus=<id>` deep link from the bell**: keep, but have the API return the page containing it (or a `GET /api/notifications/{id}`) instead of hoping it is on page 1.
5. **Batch idempotency (`CanProcessBatch`/`RecordBatchProcessing`)**: already mirrored as `BatchRun` (unique BatchType + RunKey).
6. **Preference defaults at signup in one place (`DefaultSettingsService`)**: mirrored by S4.4.7; verify new catalog types added later get defaults for existing users (catalog default fallback covers it).

## 4. WarrantyCat gap check (what is actually built)

Read: `NotificationCatalog.cs`, `NotificationService.cs`, `NotificationControllers.cs`, `NotificationEntities.cs`, `UserClock.cs`, `ReminderSendJob.cs`, UI `core/notifications.*`, story files under `Stories/E4-reminders`.

**Ahead of V1 (keep as is):** single catalog with categories and mandatory/locked types; store-first dispatcher with per-channel `Suppressed` reasons; hidden-row when in-app is off; bulk `NotifyManyAsync` with one pref query; 60 s pref cache + `InvalidatePreferences`; email `DeliveryStatus` with `RetryFailedEmailsAsync`; signed one-click unsubscribe with persisted event and scope; mandatory types undeletable until acknowledged; all list filters server-side incl. `q` (escaped ILIKE), important, actionStatus, dates; catalog-driven action URL templates that yield no link rather than a broken one; per-user timezone + send time (`UserClock`, hourly job); "exactly once" via reminder id; retry attributes on the job; `PendingConsolidation` and `BatchRun` tables.

**Correction to my 2026-10-05 settings review:** it said to check whether WarrantyCat stores an account timezone and a preferred send hour. It does: `Timezone` on the profile (`AccountEntities.cs:29`), IANA zones via `UserClock`, default send time 9:00, and the reminder job honors both. Only the *digest hour as a separate setting* and quiet hours remain open.

**Gaps (ordered by value):**

| Gap | State | Recommendation |
|---|---|---|
| `ActionStatus` never set | Column, enum, DTO, filter, UI badge exist; **no code assigns Pending/Completed**; nothing completes on resolve | Add `NotificationRequest.Actionable` (sets `Pending`) for types that ask something of the user (`things_to_do`, `card_benefits_to_confirm`, `purchase_needs_info`, `receipt_unreadable`, `coverage_check_later`, policy-change types). Add `INotificationService.CompleteByReferenceAsync(refType, refId, status)` and call it from the resolving handlers. Cheap and makes the center a real to-do inbox. |
| Failed-email retry wiring | Verified: `Jobs.cs:14` runs `RetryFailedEmailsAsync(24 h)` hourly | None. |
| `Acknowledge` does not mark read | V1 does | One line. |
| `?focus=` on page 2+ | Unverified in WarrantyCat UI | Add `GET /api/notifications/{id}` or compute page for id. |
| Template encoding | Footer encodes; body vars not verified | Test: a purchase named `<b>x</b>` renders escaped in email. |
| Burst cap | `PendingConsolidation` has `FirstEventAt` but no max-wait policy documented | Max wait cap (S4.2.4). |
| Digest, urgent bypass | Stories S4.2.2/S4.2.3 deferred to M6 | Not built; mandatory types and `LeadDays` close to the date should bypass (S4.2.2). |
| Quiet hours | S4.4.6 not built | Needed only if SMS/push arrive; email reminders already land at user's local 9:00. Use V1's start/end pair as user-level columns. |
| SMS | Dispatcher suppresses with "SMS is not available yet" (cleaner than V1's stub) | Leave until S4.4.4. |
| Real-time | S4.5.7 not built; unread count polls every 60 s and on focus | Fine for MVP. Do not copy V1's count-only SignalR. |
| Retention of notifications | S4.5.8 not built | Purge read, non-important, non-pending rows after N days; keep mandatory/acknowledged longer. Config values. |
| Notification-center retention vs retention of receipts | Separate concerns | None. |

## 5. UI observations (V1 center/bell worth knowing)

- Bell: 5 latest + badge + "View All"; click marks read then routes to center with `?focus`. Two unread-count sources (SignalR subject and service subject) both write the same field; last writer wins (race on first load). WarrantyCat `UnreadService` is a single source. Good.
- Center cards: date/time header, icon by type, title, message, metadata chips (itemCount, totalValue, consignorName: shop-specific), per-card read toggle / primary action / delete, unread dot, `focused` highlight for 2 s, empty state differs for filtered vs none.
- Action button logic: icon-only buttons, tooltip from `metadata.actionButtonText` or per-type default; button hidden for welcome-style system messages by sniffing the title/message for "welcome" (brittle: use a catalog flag, which WarrantyCat's `ActionUrlTemplate == null` already gives).
- Preferences grid auto-saves per toggle (WarrantyCat matches, S4.4.2).

## 6. Suggested next steps (smallest first)

1. `Acknowledge` also marks read (one line + test).
2. Actionable notifications: `Actionable` flag on request, `CompleteByReferenceAsync`, wire three resolvers first (to-do done, card benefits confirmed, coverage check-later reopened), test each.
3. `GET /api/notifications/{id}` (or page-for-id) so `?focus` works on any page.
4. HTML-encode test for email body variables.
5. Later: S4.2.2/S4.2.3 digest with urgent bypass; S4.5.8 retention; S4.5.7 push.

## 7. Caveats

- Read in full: V1 `Notification`, `EnhancedNotificationService` (send, list, mark, action, ack), `NotificationsControllerBase`, `NotificationHub`, `NotificationPrefsBitPacker`, `EmailComplianceService` (first 200 lines), `ConsolidatedNotification{Service,Job}`; WarrantyCat `NotificationCatalog`, `NotificationService`, `NotificationControllers`, entities, `UserClock`. Skimmed: `NotificationBatchService`, `NotificationTemplateService` (first 60 lines), V1 preference UI, V1 `notification.config.ts`.
- Items marked "unverified" or "verify" (`?focus` paging, body-variable encoding) were not tested; I read code, did not run it.
- WarrantyCat story statuses were inferred from `Status` sections where present (S4.5.6 says Done) and from code presence; most E4 stories have no Status text, so "not built" for S4.2.x, S4.4.4/4.4.6, S4.5.4/7/8 is based on the absence of code, not on a written status.
