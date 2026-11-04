# ConsignmentGenie owner settings: review for WarrantyCat (2026-10-05)

## Which copy is latest

**V1 (`C:\Projects\ConsignmentGenie`), not V2.** V2 (`ConsignmentGenie_V2`) is a skeleton from 2026-05-23/24: `Organization` has only `Name`, entities are `Organization`, `User`, `UserRoleAssignment`; two migrations (InitialIdentity, B002_OrganizationsAndRoles); briefs B002 and B006 completed; B003 OwnerLogin, B004 OwnerRegistration backlog. It has **no owner settings at all**. Everything below is from V1 (last API commit 2026-03-30), which has the full settings system. V1 is the one to mine.

V1 paths (API = `ConsignmentGenie\ConsignmentGenie_API`):
- `ConsignmentGenie.Core\Entities\Organization.cs` (the settings "god entity")
- `ConsignmentGenie.Core\Enums\SettingsPage.cs`, `Attributes\SyncToColumnAttribute.cs`
- `ConsignmentGenie.Application\Services\OrganizationSettingsManager.cs`, `DefaultSettingsService.cs`
- `ConsignmentGenie.Core\DTOs\Settings\*` (20 DTO files)
- `ConsignmentGenie.API\Controllers\Settings\*` (8 controllers, route `api/owner/settings/<area>`, `[Authorize(Roles="Owner")]`)
- UI: `ConsignmentGenie_UI\src\app\owner\settings\` (settings-layout with a menu tree, one folder per area)

## How settings are tracked in V1

Three layers, which grew organically and overlap:

1. **Flat columns on `Organization`**: shop profile (`ShopName`, address, phone, `ShopTimezone`, `Currency`), `TaxRate`, `DefaultSplitPercentage`, storefront toggles, PIN rules, integration connection flags and tokens, setup progress. Typed, queryable, used by business logic.
2. **JSON text columns on `Organization`, one per settings page**: `Settings`, `BusinessSettings`, `StorefrontSettings`, `SalesSettings`, `ConsignorSettings`, `NotificationSettings`, `ReceiptSettings`, `BrandingSettings`. `SettingsPage` is a smart enum mapping page name to column name (Organization, Business, Consignor, Storefront, Notifications, Receipts).
3. **Separate settings tables**, 1:1 with the org: `PayoutSettings` (typed columns + `ExtendedSettings` jsonb with Get/SetExtendedSetting helpers), `BookkeepingSettings` (typed + `AccountMappings` jsonb), `ClerkPermissions`, `StoreConfiguration`. Per-user: `NotificationPreferences` (per user and role, `TypePreferences` jsonb).

**`OrganizationSettingsManager`** is the access layer for layer 2: get/set one key or a whole page, 30-minute `IMemoryCache` per org+page, camelCase JSON, invalidate on write. `SetSettingAsync` also **syncs a few keys into real columns** (`approvalMode`, `agreementMethod`, `agreementTemplateId`) via a hard-coded `GetColumnMapping` switch; a `[SyncToColumn]` attribute exists for the same purpose but the switch is what runs.

**Defaults**: `DefaultSettingsService.CreateOwnerDefaultsAsync` runs at owner creation and writes notification preferences plus org defaults in one place ("ensures consistency across all user types").

**API shape**: one controller per area, DTO pair per area (`XDto` read, `UpdateXRequest` with all-nullable fields for PATCH-style partial update). Controllers read/write `Organization` directly through `IUnitOfWork`; logging with `[PROFILE]`-style tags.

**UI**: settings layout with a collapsible menu (Profile > Basic info/Branding; Business > Tax/Policies/Receipts; Consignors, Payouts, Notifications, Integrations, Staff, Storefront, Accounting, Account). Items can be disabled with a reason (e.g. Storefront hidden if Square Online is chosen).

**Audit**: `AuditLog` entity exists (Action, EntityType, EntityId, OldValues/NewValues JSON, IP, UserAgent, CorrelationId, RiskLevel) but the settings controllers do not appear to write to it; no per-setting history.

### V1 weaknesses (do not copy)
- Same value lives in multiple places (e.g. `TaxRate` column, `TaxDto.SalesTaxRate` in BusinessSettings JSON, `OrganizationBusinessSettingsDto.TaxRate`; three overlapping "business" DTOs; `AutoApproveConsignors` vs `ApprovalMode`; `ConsignorPermissions` vs `ConsignorSettings`). Source of truth is unclear; hence the sync hack.
- JSON as untyped text with a string-keyed `Dictionary<string, object?>`: no schema, no versioning, no migration of old shapes.
- Integration tokens as plain columns on `Organization` with "TODO: encrypt".
- Legacy `[Obsolete]` columns left in `NotificationPreferences`; `PayoutSettings.old` file in the tree.
- Settings write path bypasses audit.
- Owner PIN hash and security flags on the same row as shop profile.

## Properties that might be useful for WarrantyCat

WarrantyCat is a single-role consumer app, so "organization" maps to the **account** (and some to the **user**). Mapping below; "have" = WarrantyCat already covers it (see `NotificationEntities.cs`, account/auth code).

| V1 property | WarrantyCat use | Note |
|---|---|---|
| `ShopTimezone` ("America/New_York") | **Account timezone**: due-date reminders, "return window ends today", digest send time | High value; reminders are date-sensitive. Check if WarrantyCat stores one. |
| `Currency` (3-char, "USD") | Account currency for purchase prices, return refunds | Needed if non-US users ever. |
| `ShopCountry` | Country drives return-law defaults, card-benefit catalog, retention rules | Reference data suggests; user data records. |
| `DateFormat` / `TimeFormat` (ReceiptHeaderDto) | Display preferences (MM/dd vs dd/MM, 12h/24h) | Cheap, noticed immediately by users. |
| `SetupStep`, `SetupCompletedAt`, `OnboardingDismissed`, `WelcomeGuideCompleted`, `SetupChecklistDismissed` | Onboarding checklist state (add a card, first purchase, forward email, enable reminders) | WarrantyCat already has a "standing notice" in the bell; these give it persistent dismissal flags. |
| `NotificationPreferences.SmsOptedIn`, `SmsPhoneNumber`, `SmsPhoneVerified`, `SmsPhoneVerifiedAt` | SMS reminders opt-in with verification timestamp (consent evidence) | Matters if S4.6.3 adds SMS. |
| `TypePreferences` jsonb `{type:{email:bool,sms:bool}}` | WarrantyCat's normalized `NotificationPreference` (per type+channel) and `NotificationTypeSetting` (`DeliveryMode`, `WeeklyDay`, `LeadDays`) is already **better** | Keep yours. |
| Digest: `DigestMode` (off/daily/weekly), `DigestTime` ("09:00"), `DigestDay` | Matches `DeliveryMode` + `WeeklyDay`; add **send time of day** if missing | Check whether reminder job honors a preferred hour. |
| `Thresholds` (`low_inventory_alert`, `high_value_sale`) | Per-type thresholds for WarrantyCat: "remind me N days before window ends" (`LeadDays` covers), "only items over $X" | A min-price filter on reminders is a likely ask. |
| "System notifications always on and locked in UI" (`password_reset`, `account_activated`...) | Mark security/legal/billing notification types non-disableable in the catalog | Cheap rule; confirm `NotificationCatalog` flags it. |
| `PayoutSettings.ExtendedSettings` jsonb + typed Get/Set helper | Pattern for the **account-level "escape hatch" bag** for new prefs before they earn a column | Use with a typed options class, not a string-key dictionary. |
| Security: `OwnerPin` (hashed), `RequirePinFor*` | **Re-auth gate for destructive actions**: delete account, export data, delete receipts | WarrantyCat has admin two-step; consider a password-recheck (V1 `SetPinRequest` requires `CurrentPassword`). |
| `ConsignmentPeriodDays`, `HoldPeriodDays`, `DefaultConsignmentPeriodDays` (30-365) | Analog: **default reminder lead time** and default "return window if unknown" per category | Account-level defaults that seed new items; item stores its own snapshot (matches your "reference suggests, user data records" rule). |
| `EnableAutoMarkdowns` + `MarkdownSchedule` | Not applicable | |
| `IntegrationMode`, `ActiveIntegrations`, `*Connected` flags, `*ConnectedAt`, `LastSync*`, `LastSyncError` | For **email access (S2.2.8 OAuth / S2.2.10 IMAP)**: `Connected`, `ConnectedAt`, `LastSyncAt`, `LastSyncError`, `ContinueOnSyncErrors` | Put on a separate `email_connection` table with encrypted tokens, not the account row. |
| `QBSyncLog`, `SquareSyncLog`, `ShopifySyncLog` | Same shape for email-import runs: per-run log row for debugging/"why was nothing imported" | |
| `PendingImportItem` / `PendingSquareTransaction` | Already mirrored by WarrantyCat New Items (pending_items) | Nothing new. |
| `ExportFilePrefix`, `EnableCsvExport`, `EnableExcelExport` | Export format choice (CSV/JSON/PDF) for S2.6 export; filename prefix | Minor. |
| `StoreCode` / `StoreCodeEnabled` / `RegistrationUrl` | **Household invite code** if sharing is built (F1.3 invites) | Invites + expiry were V1's `OwnerInvitation`, `ClerkInvitation`, `ConsignorInvitation` entities: reuse the shape. |
| `ClerkPermissions` (what a role can see/do) | **Household member permissions** if followers get limited rights (view only vs edit) | Ties to your "items belong to people (owner + followers)" design. |
| `ReceiptSettings` (auto-email, email format html/pdf, subject template with `[Store Name]` token, promo content) | Template tokens for reminder email subject (`[Item Name]`); html vs plain-text preference | |
| `BrandingSettings` (logo, colors, typography) | Not applicable (no tenant branding); maybe theme/dark mode pref | |
| `StripeCustomerId`, `StripeSubscriptionId`, `CachedSubscriptionStatus`, `CachedPeriodEnd`, `IsFounderPricing`, `FounderTier` | **Billing columns for M5 Stripe**: "Stripe is source of truth; cache status + period end via webhooks"; founder flag set once at first subscription | Good pattern to copy exactly; avoid V1's mixing of Connect tokens and subscription on the same row (WarrantyCat needs only subscription side). |
| `AuditLog` shape (OldValues/NewValues JSON, CorrelationId, RiskLevel) | WarrantyCat already audits admin changes; add **user-side preference/security changes** (email change, 2FA, consent) with the same shape | Terms acceptance already in M5. |
| `AgreementMethod` none/acknowledge/upload + `AcknowledgeTermsText` | Terms/consent flow: WarrantyCat has TermsAcceptance; version the text hash you accepted | |
| `SettingsPage` smart enum (name -> storage) | If you do page-grouped settings, a registry like this keeps controller/UI/storage names aligned | |
| UI menu-tree with `disabled` + `disabledReason` | Account page tabs: show unavailable options with a reason (e.g. "SMS needs a verified phone") | Good UX, small code. |

## Recommendations for WarrantyCat

1. **Don't import V1's three-layer model.** WarrantyCat's normalized per-user notification tables are already cleaner. For account-level prefs use **one typed table** (`account_settings`: timezone, country, currency, date/time format, digest hour, default lead days, onboarding flags) plus **one typed jsonb options class** for later additions. One source of truth per value.
2. **Adopt from V1**: central defaults-on-signup service (`CreateDefaults...`), cached settings reader with invalidate-on-write, locked system notification types, partial-update (all-nullable) request DTOs, SMS consent + verified-at fields, sync-log rows per import run, re-auth for destructive actions, Stripe cache-columns pattern.
3. **Add audit on settings writes from day one** (V1 had the entity but skipped it).
4. **Encrypt integration tokens from the start** (V1 left TODOs).
5. Verify the account timezone and digest hour exist in WarrantyCat before building more reminder features; they are the V1 properties most likely to be missing.

## Update 2026-10-05 (after checking WarrantyCat and talking it through)

- **JSON settings in V1 were a stopgap** while the settings list was still being decided, per the owner; read the "JSON as untyped text" weakness above as "unfinished", not a design choice. The advice stands for WarrantyCat: decide the settings, then use typed columns.
- **Timezone and digest hour are on the user, not the account** (`ApplicationUser.Timezone`, `DigestTime`), and the reminder job honors both. Settings are per person, which fits since reminders go to people. Account holds billing, features and receipt retention only.
- **Confirmed missing in WarrantyCat**: country, currency, date and time format, setup/onboarding flags, SMS phone and consent fields (S4.4.4 specifies them, not built), audit of user-side setting changes. Added S9.8.3 and S9.8.4; SMS is already S4.4.4; re-auth for destructive actions is already in S1.4.2.
- **Already covered, nothing to add**: quiet hours (S4.4.6), Stripe cache columns (already on `Account`), billing/plan page, theme (S9.8.2), terms acceptance (`TermsVersion`, `TermsAcceptedAt`), export (S1.4.1).
- **Not added, your call**: a min-price filter on reminders ("only items over $X"), household invite code and member permissions (F1.3 owns these, V1's invitation entities are a shape reference), export file prefix and format choice.

## Caveats
- I read entities, managers, DTOs and two controllers fully; the other settings controllers (Payout, Bookkeeping, Consignor, Sales, Account) and the UI components were skimmed by listing and DTO shape, not line by line.
- The WarrantyCat mapping above was checked only against `NotificationEntities.cs` and HANDOFF.md, not a full audit of the WarrantyCat schema; "check if WarrantyCat has X" items need a grep of `StuffIt.Core\Entities`.
- HANDOFF.md says the desktop has "the better examples of how the owner likes settings" (this is that copy, presumably); the laptop's Account menu/Settings additions still need comparing before the merge.
