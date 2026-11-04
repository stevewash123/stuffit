# WarrantyCat API conventions (confirmed 2026-09-30, implemented in M1 auth)

Drafted 2026-09-30 from a review of ConsignmentGenie_API. Status: **confirmed** and implemented in `StuffIt_API` (branch `m1-auth`). Every story follows it. Covered by tests in `AuthApiTests`.

## What ConsignmentGenie actually did (evidence)

### Claims in tokens
- Mixed claim names in one token: long .NET URIs (`ClaimTypes.NameIdentifier`, `ClaimTypes.Email`, `ClaimTypes.Role`) plus custom camelCase (`organizationId`, `consignorId`, `isApproved`, `isFounder`, `founderTier`).
- Readers disagree on the name. Most controllers read `organizationId`; `RequiresTierAttribute` reads `OrganizationId` (FindFirst is case-sensitive, so it finds nothing and returns 401); `AdminController` reads `userId`, which the token never issues.
- Role casing was ambiguous ("Owner" vs "owner", 70 `[Authorize(Roles=...)]` usages mixing both), so the token emits **both** casings of the role as a workaround.
- Every controller re-implements `GetOrganizationId()` / `GetUserId()` privately.
- State that changes (founder status, approval) is baked into a 24-hour token, so it can be stale.
- Booleans are strings (`"true"`), no refresh token, 24-hour lifetime.
- Signing key has a hardcoded fallback default in code; signed with ASCII bytes, validated with UTF-8 bytes (works only because the default is ASCII).
- Every token issue logs every claim at Information level.
- A bit-packed `notif_prefs` claim was designed (see lessons doc) but the token code never adds it.

### Response shapes
- Two styles side by side. `ApiResponse<T>` (`success`, `data`, `message`, `errors[]`) is used in about 15 controllers (374 uses: Admin, Auth, Items, ItemCategories, Consignors, Subscription, ...). The other 47 controllers return raw `Ok(dto)`, `BadRequest("text")`, `NotFound()`, anonymous objects.
- `PagedResult<T>` (`data`, `totalCount`, `totalPages`, `page`, `pageSize`, `hasNextPage`, `hasPreviousPage`) for lists.
- No global exception handler or ProblemDetails.
- JSON: camelCase properties, enums as camelCase strings (configured in Program.cs).
- Routes: `api/[controller]` mostly, some role-prefixed (`api/owner`, `api/consignor`), plural and singular mixed.

## The WarrantyCat conventions

### 1. Token claims
- Use the registered JWT names, lowercase, and turn off the default claim remapping (`MapInboundClaims = false`): `sub` (user id), `email`, `jti`, `iat`, `exp`, `iss`, `aud`.
- One custom claim: `account_id` (snake_case lowercase, like the registered names). Already what `HttpTenantProvider` reads.
- Names live in one constants class (`StuffItClaims`); nothing else types a claim name.
- **Not in the token:** role (single customer role), subscription or founder state, feature entitlements, notification preferences. Anything that can change is read server-side from cached account state, so it is never stale.
- Operator access: `is_operator` only for operator users, checked server-side against the database; not relied on from the token alone.
- Access token 15 minutes; refresh token rotated, stored hashed, in an httpOnly cookie; access token held in memory by the UI.
- One `ICurrentUser` service (UserId, AccountId) used everywhere, plus a fallback authorization policy requiring sign-in on every endpoint unless `[AllowAnonymous]`. No per-controller helpers.

### 2. Responses: do not wrap
- Success: return the resource or list directly, with the right status (200, 201 + Location, 204).
- Errors: RFC 7807 ProblemDetails (`application/problem+json`) from a global exception handler and the built-in validation behavior; validation errors as `errors: { field: [messages] }`.
- Lists that page: `{ items, page, pageSize, totalCount }`. Only paged endpoints use an envelope.
- Reason: HTTP status already says success or failure, a wrapper duplicates it and forces every client call to unwrap; ConsignmentGenie ended up with both styles.

### 3. JSON and routes
- camelCase properties; enums as camelCase strings (the database stores the enum names, the API converts); dates ISO-8601, DateOnly as `yyyy-MM-dd`, timestamps UTC.
- Routes: `api/` + plural kebab-case nouns (`api/purchases`, `api/payment-methods`), no role prefixes, no version segment until a breaking change needs one.
- `[ApiController]` on every controller; the account comes from the token, never from the URL.

### 4. Config and secrets
- JWT signing key required from configuration with no fallback (app fails fast at startup); 32+ bytes; UTF-8 consistently.
- Do not log token contents or claims.

### 5. Errors and logging
- Exceptions bubble up. `ApiExceptionHandler` logs each one once: a refusal that becomes a 4xx as a warning (no stack), anything else as an error with its stack. The framework's own line for the same exception and EF's failed-query lines are switched off in `appsettings.json`, so there is no second copy.
- A controller that catches an exception and answers with its own result (`catch { return NotFound(msg); }`) has swallowed it, so it always logs it first (`logger.LogWarning(ex, ...)`). A catch that rethrows logs nothing; the handler does. `ControllerCatchTests` fails the build if a controller catch neither logs nor rethrows.
- A service catch that does not rethrow is rare; when one exists it logs a warning and the flow continues. Background jobs have no handler above them, so a job logs its own failures.
- Every controller action logs its inputs (`InputLoggingFilter`): values in Development, only field names and ids elsewhere, secrets masked, sign-in and two-factor calls never. See `StuffIt.Core/Logging/InputRedactor.cs`.
- Every API call logs one summary line when it finishes: method, path, status, milliseconds, user, account and trace id.
