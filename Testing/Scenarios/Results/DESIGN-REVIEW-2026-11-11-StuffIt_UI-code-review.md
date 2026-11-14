<cursor_untrusted_data_1337 source="CallDynamicTool">

# Code review: StuffIt UI (WarrantyCat)

Review of the Angular front end for StuffIt / WarrantyBank. The API lives in [StuffIt_API](https://github.com/stevewash123/StuffIt_API). This is a review only: no application code was changed.

Counts below are lines in `src/**/*.{ts,css,html}` as of commit `c542847` on `main`. Component templates are inline in the `.ts` files, so a “page” line count includes its template.

## Executive summary

The app is a well-structured Angular 20 standalone client: feature folders, lazy routes, signals, thin `HttpClient` services, and a session model that keeps the access token in memory and the refresh token in an httpOnly cookie. The product language around coverage trust (Attached, Confirmed, Highly Likely, Likely, Unconfirmed) is deliberate and tested. The hot paths — item detail, add purchase, plans, new items — have large Jasmine specs.

The structural problem is that the largest screens own too many jobs, and several matching rules that the API also owns are reimplemented in the UI. `ItemDetailPageComponent` is 2,118 lines with 49 `.subscribe()` calls and no teardown. `PlanPageComponent` is 1,256 lines. `AddPurchasePageComponent` is 1,075 lines and decides, locally, which warranties are pre-ticked, how sure an attached paper is (0.95 or 0.99), whether a model list fits, and whether a document’s facts can be applied without showing the review panel.

Users can correct a wrong store, brand, or coverage, but the correction does not teach the matcher. There is no candidate list for store or brand (brand match is a single silent bind), no alias or exclusion API on the client, and dismissals are per proposal key (`notApplicable` or `unknown`). Quick add posts an empty body and lets the server attach whatever it considers ≥ 80%. The full add form sends the keys the UI ticked using its own copy of that 80% bar. Those two paths can diverge.

Two shipped screens are not the product they appear to be. Primary nav **Returns** (`/returns`) is a static mock with invented purchases and disabled buttons. Operator nav **Review** (`/admin/review`) renders “Not built yet.” The working returns list is a different route.

## Repository map

| Area | Path | Files | Lines | Specs | Production lines | What it is |
| --- | --- | --- | --- | --- | --- | --- |
| Items, claims, returns UI | `src/app/features/items` | 42 | 10,070 | 23 | 4,910 | Item list and the item hub, claim wizard, panels |
| Core | `src/app/core` | 107 | 8,460 | 32 | 6,401 | Auth, HTTP, 25 API clients, models, formatters |
| Plans | `src/app/features/plans` | 21 | 5,091 | 12 | 2,476 | Protection-plan list and editor |
| Purchases / inbox | `src/app/features/purchases` | 10 | 4,313 | 6 | 1,854 | Add purchase, New Items, receipt scan |
| Shared UI | `src/app/shared/ui` | 51 | 4,226 | 16 | 2,591 | Pickers, review panels, confirm, toasts |
| Settings | `src/app/features/settings` | 19 | 3,225 | 7 | 1,556 | Profile through billing |
| Admin | `src/app/features/admin` | 16 | 2,374 | 6 | 1,578 | Operator companies, feedback, businesses |
| Cards | `src/app/features/cards` | 4 | 2,304 | 2 | 1,204 | Card list and benefit confirmation |
| Auth screens | `src/app/features/auth` | 19 | 1,793 | 6 | 1,029 | Login, signup, Google, join, consent |
| Insurance | `src/app/features/insurance` | 6 | 1,570 | 3 | 954 | Policy list and editor |
| Layout | `src/app/layout` | 13 | 1,359 | 6 | 639 | Shell, bell, reauth, account |
| Home | `src/app/features/home` | 10 | 1,299 | 5 | 687 | Dashboard, orientation, quick photo |
| Parties | `src/app/features/parties` | 5 | 1,157 | 2 | 968 | Store/brand list and detail |
| Other features | notifications, vehicles, legal, share, feedback, todos, returns, install | 16 | 2,586 | — | — | Smaller screens, including two placeholders |
| Global styles | `src/styles.css` | 1 | 430 | — | 430 | Tailwind v4 and design tokens |
| **Total under `src`** | | **348** | **50,525** | **135** | **~28,900** | About 43% of the lines are specs |

Stack (`package.json`, `angular.json`, `README.md`): Angular 20.2 standalone components, signals, RxJS 7, Tailwind CSS 4, `ngx-sonner` toasts, `@ng-select/ng-select`, Karma + Jasmine. No NgRx, no `BehaviorSubject`, no `$localize` / ngx-translate, no e2e project. Production budgets: 600 kB warning / 650 kB error on the initial bundle (`angular.json`). Dev server proxies `/api` (`proxy.conf.json`) so the refresh cookie stays first-party. `scripts/set-env.mjs` injects public legal strings at build time.

### Largest files

| Lines | File |
| ---: | --- |
| 2,118 | `src/app/features/items/item-detail.page.ts` |
| 1,256 | `src/app/features/plans/plan.page.ts` |
| 1,171 | `src/app/features/items/item-detail.page.spec.ts` |
| 1,124 | `src/app/features/purchases/add-purchase.page.spec.ts` |
| 1,075 | `src/app/features/purchases/add-purchase.page.ts` |
| 1,017 | `src/app/features/items/item-edit.spec.ts` |
| 822 | `src/app/features/purchases/new-items.page.spec.ts` |
| 816 | `src/app/features/plans/plan.page.spec.ts` |
| 778 | `src/app/features/insurance/policy.page.ts` |
| 691 | `src/app/features/cards/cards.page.spec.ts` |
| 665 | `src/app/features/parties/party-detail.page.ts` |
| 655 | `src/app/core/purchase.models.ts` |
| 625 | `src/app/features/cards/cards.page.ts` |
| 579 | `src/app/features/cards/card-detail.page.ts` |
| 564 | `src/app/features/purchases/new-items.page.ts` |

### Routing

`src/app/app.routes.ts` (120 lines). Signed-out routes are eager (login, signup, password reset). Legal, settings children, and almost every signed-in feature are `loadComponent`. The shell (`ShellComponent`) wraps the signed-in tree behind `authGuard`, `termsGuard`, and `accountChoiceGuard`. Operator routes add `operatorGuard`. Unknown paths redirect to home (`path: '**'`), not a 404.

### Review areas

The tree is one app with a shared core, so the split follows feature modules plus the two cross-cutting layers that every screen uses.

| # | Area | Doc |
| --- | --- | --- |
| 1 | Platform, session, shell | [areas/01-platform-and-session.md](areas/01-platform-and-session.md) |
| 2 | API clients and domain models | [areas/02-data-layer.md](areas/02-data-layer.md) |
| 3 | Items, coverage editing, claims | [areas/03-items-and-claims.md](areas/03-items-and-claims.md) |
| 4 | Purchases, inbox, document intake | [areas/04-purchases-and-intake.md](areas/04-purchases-and-intake.md) |
| 5 | Plans and match / confidence UI | [areas/05-plans-and-matching.md](areas/05-plans-and-matching.md) |
| 6 | Insurance, cards, parties, admin | [areas/06-insurance-cards-parties-admin.md](areas/06-insurance-cards-parties-admin.md) |
| 7 | Settings, shared UI, styling, tests | [areas/07-settings-shared-ui-quality.md](areas/07-settings-shared-ui-quality.md) |

## Architecture assessment

### What is in good shape

- **Layering of HTTP.** Each backend area is a small `@Injectable` that returns `Observable<T>` (`src/app/core/*.api.ts`, 25 clients). Components call `toProblem()` (`src/app/core/problem.ts`) in the error callback. The interceptor (`api.interceptor.ts`) owns bearer attachment, cookie credentials, 401 refresh-and-retry, and operator reauth on 403. That split is consistent.
- **Session.** `AuthService` holds the access token in a signal. `provideAppInitializer` restores it with a silent refresh before the first navigation. Refresh is single-flight. The interceptor retries when another call already rotated the token (`api.interceptor.ts` lines 41–43). Specs cover that race.
- **State.** There is no global store. Screen state is signals on the component; account, theme, unread count, upload queue, and setup notices are root services. That fits this app. The pain is component size, not a missing store.
- **Routing and code splitting.** Feature pages are lazy. `app.routes.spec.ts` locks the lazy-load policy.
- **Some extractions already happened.** Plan document parsing is pure (`plan-reading.ts`, `plan-update.ts`, `plan-start.ts`). Policy parsing is pure (`policy-reading.ts`). The claim wizard states that the rules live on the server and the page only asks questions. `DocumentFactsReviewComponent` does not mutate the form; the owner applies the ticked proposals.
- **Design system.** `src/styles.css` defines theme tokens. `theme-contrast.spec.ts` checks WCAG 4.5:1. Components use utility classes (`.btn`, `.card`, `.input`) and `var(--color-*)` rather than raw hex.

### Where layering breaks down

Presentation, workflow, and matching policy share the same class on the three biggest pages.

| Page | Lines | Also owns |
| --- | --- | --- |
| `ItemDetailPageComponent` | 2,118 | Read view, four edit drawers, coverage CRUD, suggestion ticking, document read/apply, returns, people, files, plan undo |
| `PlanPageComponent` | 1,256 | Edit and read views, document read, cancel / stop-renew / refund drawer, plan-type fill, item linking |
| `AddPurchasePageComponent` | 1,075 | Purchase form, coverage preview rules, document facts, pending-item completion, upload-after-save |

Child components exist (vehicle panel, parts, maintenance, plan lines, reading review) and are the right direction. They sit beside a parent that still contains the risky workflow.

Business rules that belong next to the matcher, and that the comments already describe as copies of server constants:

| Rule | Where the UI hard-codes it |
| --- | --- |
| Pre-tick at 80% (`ApplicabilityFactors.TickedFrom`) | `TICKED_FROM` in `add-purchase.page.ts` line 68; `PickedFrom` in `item-detail.page.ts` line 1793; inline `>= 0.8` in `isChecked` (line 491) and New Items receipt copy (line 190) |
| Attached warranty trust = 1, fit = 0.95, corroborated fit = 0.99 above 0.60 | `add-purchase.page.ts` lines 69–74, 534–536 |
| Return windows are mutually exclusive | `toggleCoverage` lines 499–500 |
| Return alternatives under 50% are hidden | `tucked` lines 565–567 |
| Model-list substring fit decides whether the paper applies | `modelFit` lines 550–557 |
| Document facts with no `ask` and no `flag` skip the review panel | `fillsWithoutAsking` lines 661–663 |
| Word bands from numeric confidence | `certaintyWord` in `certainty.ts` lines 5–10 |

`certainty.ts` is the right kind of module (one function, a spec). The thresholds inside it are the problem: the API already sends `confidence`, `confidenceBand`, and `confidenceReason`, then the client re-derives a word and a default tick from the number.

### Cross-cutting concerns

| Concern | Assessment |
| --- | --- |
| Auth / session | Strong. Memory token, cookie refresh, guards for auth, terms, account choice, operator + 2FA, owner, business. `safeReturnUrl` only rejects non-relative and `//` URLs (`guards.ts` lines 20–21). The bearer-exclusion regex omits Google, verify-signup, and account switch (`api.interceptor.ts` line 16). |
| Errors | `toProblem` is the shared shape. Many mutations surface `problem()`. Load failures are uneven: the notification bell clears `loading` and then shows “You are all caught up.” (`notification-bell.component.ts` lines 113–118 and 55–56). Setup-notice refresh errors are swallowed. |
| Loading | Signals (`loading`, `saving`, `busy`, `reading`) are the usual pattern. Document read has an overlay. Coverage preview has no per-row pending state, and in-flight previews are not cancelled (`loadPreviews`, `add-purchase.page.ts` lines 473–480). |
| Forms / validation | Mixed. Auth uses reactive forms. Most product forms use `ngModel` and hand-rolled checks (`validDate`, maxlength). Unsaved-changes is a real guard (`unsaved-changes.ts`) on item, plan, policy, and add-purchase routes. |
| i18n | None. `lang="en"`, hardcoded copy, an unused `extract-i18n` architect target. |
| Accessibility | Better than typical: labels, `sr-only` icon names, `role="alert"`, contrast tests, 44px targets called out in the shell. Gaps: account menu is hover-opened without a roving tabindex; the bell panel is not a focus trap; item-detail uses `role="alertdialog"` on inline asks without `aria-modal`. |
| Performance | Lazy routes and a service worker that does not cache `/api/**` (`ngsw-config.json`). Shell starts four pollers (unread, new-items count, setup notices, upload sync) at 60s. `ngDoCheck` on add-purchase debounces preview reloads (lines 438–444); it is guarded by a key, so it does not refetch every cycle, but it is a change-detection hook doing form watching. Initial budget is 650 kB; `npm run size` exists and no stats file is checked in. |
| Tests | 135 specs, ~21,600 lines. Dense around item detail, add purchase, plans, cards, auth interceptor. No coverage thresholds in `angular.json`. No e2e. `party-detail.page.ts` (665 lines) has no spec. Most `*.api.ts` files have no HTTP-contract spec (`inbox.api.spec.ts` is the exception). |
| Consistency | Signals + `inject()` + inline templates are uniform. Error and loading signals are named differently per page (`error` vs `problem` vs `returnError`). Three document pipelines coexist: document facts, document reading (plans and insurance), and inbox coverage preview. |

## Findings

Severity is about user impact and the chance of a wrong coverage or a wrong match sticking. Effort is S (one or two files, no new contract), M (one extracted component or one new response field wired through one flow), L (a contract change plus every screen that ticks or displays a match).

| ID | Sev. | Finding | Location | Recommendation | Effort |
| --- | --- | --- | --- | --- | --- |
| F1 | High | Coverage tick policy is reimplemented in the client and can diverge from the API. Quick add sends `{}` and the server attaches ≥ 80%. The add form and item page pre-tick with their own `0.8`, and the add form also recomputes document confidence (0.95 / 0.99) and model fit. | `add-purchase.page.ts` 67–74, 487–567; `item-detail.page.ts` 1793, 1845–1846; `new-items.page.ts` 190, 486–494; `inbox.api.ts` `accept` 234–236; `certainty.ts` 5–10 | Have the preview and proposal payloads include `decision: 'auto' \| 'choose' \| 'ask'` (or `defaultSelected` plus a band). UI renders that and posts the user’s deltas. Delete `TICKED_FROM`, `PickedFrom`, `DOCUMENT_FITS*`, and the numeric branches in `certaintyWord`. | L |
| F2 | High | Wrong matches are not learned. Brand match is one silent result. Store/brand conflicts are keep-vs-document, then a private party is created or renamed. Dismissals store a proposal key and `notApplicable` \| `unknown`, not “this printed name is party P” or “never match this”. | `reference.api.ts` `matchBrand` 58–60; `document-facts.parties.ts` 24–37; `purchase.api.ts` `dismiss` 114–116; `party-picker.component.ts` | Add a candidate picker (top 2–3 with the certainty word and reason). On confirm or reject, post an alias or an exclusion (printed text, field, chosen party id or “none”). Keep per-item dismissals for “not this item”. | L |
| F3 | High | `ItemDetailPageComponent` is a god component: ~90 methods, 49 subscriptions, no `DestroyRef` or `ngOnDestroy`. A route change can complete `load` out of order. | `item-detail.page.ts` (2,118 lines); `load` around 1311–1328 | Extract coverage drawer, policies section, purchase/item edit drawers, and a document-intake helper. Cancel in-flight loads with `switchMap` + `takeUntilDestroyed`. | L |
| F4 | High | Document facts can skip the review panel whenever every proposal is `useDocument` and none is `ask` or `flag`. A toast is the only notice. New stores/brands are created inside `applyFacts` → `FactParties.resolve`. | `add-purchase.page.ts` `fillsWithoutAsking` / `fillForm` 653–669; same idea on the item page’s read path | Auto-apply only when the API marks the batch `decision: 'auto'` and every party id is already known. Otherwise show `DocumentFactsReviewComponent`. | M |
| F5 | High | **Returns** in the primary nav is a static mock (fake Sony headphones, disabled buttons). The real list is `/returns/in-progress`. | `returns.page.ts` lines 4–14; `shell.component.ts` line 232; route `app.routes.ts` line 66 | Point the nav at `/returns/in-progress`, or replace the mock before it stays linked as “Returns”. | S |
| F6 | Medium | Confidence UI does not match the stated rule “never as a percentage”, and the three match surfaces do not share a band. Add-purchase uses word badges. New Items uses words plus a warning color when the band is not `verified`. Item detail puts percents in the tooltip (`Policy verified 96%`). Reading review uses high/medium/low. | `certainty.ts` 1–10; `item-detail.page.ts` `confidenceTip` 1832–1842; `new-items.page.ts` 174–194; `reading-review.component.ts` | One presenter fed by API `decision` + `confidenceBand` + `confidenceReason`. Keep percents out of the default UI. Map reading-review’s high/medium/low only if that pipeline stays separate. | M |
| F7 | Medium | `PlanPageComponent` (1,256) and `PolicyPageComponent` (778) repeat document-read → tick → fill, with a second pipeline (`DocumentReadingApi`) beside document facts. Cancel/refund UI still lives in the plan page template. | `plan.page.ts`; `policy.page.ts`; `plan-reading.ts`; `policy-reading.ts` | Extract the plan cancel sheet and a shared “read, review, fill” host. Leave parsing in the pure modules that already exist. | L |
| F8 | Medium | Operator **Review** is a placeholder, and the companies filter has a disabled “Credit cards (not built yet)” option. Both are reachable from the admin shell. | `app.routes.ts` 76–77; `admin-placeholder.page.ts`; `companies.page.ts` lines 12–25; `shell.component.ts` line 210 | Remove Review from nav until the queue exists. Leave the disabled issuer option only if the copy stays honest (it does). | S |
| F9 | Medium | Coverage-preview requests are not cancelled. `ngDoCheck` debounces by 400 ms, then `loadPreviews` subscribes per item with `catchError` to `null`. A slow response can overwrite a newer one. Failures look like “no coverage”. | `add-purchase.page.ts` 438–480 | Replace `ngDoCheck` with an explicit form stream and `switchMap` per row. Surface a preview error separately from an empty list. | M |
| F10 | Medium | Notification bell treats a failed `list()` as an empty inbox. | `notification-bell.component.ts` 55–56 and 110–118 | Set an error signal and a retry control. Add a spec for the failure path. | S |
| F11 | Medium | Item detail and add purchase duplicate PayPal helpers, `fileKey`, and the facts → party → field pipeline. Only add-purchase has the document-confidence math, so the two screens can show different certainty for the same paper. | `item-detail.page.ts`; `add-purchase.page.ts` 75–81 and 747–772 | One `DocumentIntake` helper used by both pages, with one spec for proposal → party → field. | M |
| F12 | Medium | `party-detail.page.ts` (665 lines, policy correction via `correctSeller` and siblings) has no spec. `add-vehicle.page.ts` has none. API clients other than inbox are untested at the HTTP boundary. No coverage gate, no e2e. | `features/parties/party-detail.page.ts`; `angular.json` test target | Spec party-detail’s correction payload and the duplicate-name path in `ReferenceApi`. Add a statement threshold only after those exist, so the gate measures the gap instead of the already-tested pages. | M |
| F13 | Medium | Subscriptions on the item page (and most feature pages) are not tied to destroy. Cards and party-picker do use `takeUntilDestroyed`; the largest page does not. | `item-detail.page.ts` (49 `.subscribe(`, no `ngOnDestroy`) | `takeUntilDestroyed` on the long-lived loads first (`load`, proposals, document read). | M |
| F14 | Low | `safeReturnUrl` is a prefix check. `authEndpoint` is a regex that does not list every anonymous auth call, so a leftover bearer can be sent to `/api/auth/google` and similar. | `guards.ts` 19–22; `api.interceptor.ts` 16 | Parse with the router and require an internal URL. Replace the regex with an explicit set shared with the interceptor spec. | S |
| F15 | Low | No i18n. Account menu is mouse-hover. Share target service worker writes every shared file into the Cache API with no size cap. Refund sample wizard is a real route (`/items/sample/refund`) that saves nothing. | `styles.css` / templates; `shell.component.ts`; `public/share-sw.js`; `refund-wizard.page.ts`; `app.routes.ts` line 51 | Leave i18n until a second language is in scope. Cap share uploads. Unlink the sample wizard from any user-facing path, or mark the route dev-only. | S |

### Matching, against the API recommendation

The API review’s bands were: **auto-bind**, **show the top 2–3**, **ask**. User picks should be stored as aliases or exclusions. What the UI does today, and what it would need:

| Band | What the UI does now | What it needs |
| --- | --- | --- |
| Auto-bind | Anything ≥ 0.8 is pre-ticked (`isChecked`, `isPicked`). Quick add (`InboxApi.accept`) sends no selection; the server applies its own cut. `fillsWithoutAsking` writes store/brand/name onto the form with a toast. `matchBrand` writes a maker when the typed name is at least 3 characters and the field is empty (`add-purchase.page.ts` 869–875). | A server `decision: 'auto'` (and a party id already resolved). The client shows the bound value with the certainty word and an “Change” action. It does not recompute 0.8. |
| Show top 2–3 | Coverage preview lists every returned row. Weak return windows (`return:*` under 0.5) hide behind “other return windows”. Return matching lists every `ReturnCandidate` with its own button (`new-items.page.ts` 124–136), which is the closest thing to a candidate picker. Party picker is a search box, not a ranked shortlist. Brand match returns a single `Party \| null`. | When the API sends `candidates[]` (store, brand, policy), render a shortlist component: certainty word, reason, primary action on the top candidate, secondary actions on the next two. Post the chosen id. |
| Ask | Document-fact `outcome === 'ask'` is a real radio choice (`document-facts-review.component.ts` 36–52). Unticked rows under 80% wait for a tick. `check[]` blocks quick add (`canQuickAdd`). Flags disable a proposed store/brand the client does not know. | One visual treatment driven by `decision: 'ask'`, not four different mechanisms (fact outcome, `check`, confidence number, `flag`). |
| Alias / exclusion | Not implemented. Comments in `document-facts.models.ts` mention aliases as something the API already resolved. `FactParties` creates or renames a party. `PurchaseApi.dismiss` records a per-item proposal key. Operator `correctSeller` / `correctManufacturer` / `correctCardBenefit` (`reference.api.ts`) correct a policy text with a required note; that is an operator content fix, not an end-user alias. | New client method, for example `POST /api/match-feedback` with `{ field, printed, partyId \| null, action: 'alias' \| 'exclude' }`, called from the candidate picker and from “this is the wrong store/brand”. Do not infer an alias from a dismissal. |

Detail, screen by screen, is in [areas/05-plans-and-matching.md](areas/05-plans-and-matching.md).

## Refactoring roadmap

### Quick wins

These do not need an API change.

1. **F5.** Retarget Returns in `shell.component.ts` to `/returns/in-progress`, or stop linking the mock.
2. **F8.** Drop Review from the operator nav until the queue exists.
3. **F10.** Bell error state and a spec.
4. **F14.** Tighten `safeReturnUrl` and the auth-endpoint set. Specs already exist beside both.
5. **F6, partial.** Stop putting percents in `confidenceTip`, or move them behind an explicit “Why this score?” that the certainty module’s header no longer forbids. One-line product decision.
6. **Share worker.** Refuse oversized share-target payloads in `public/share-sw.js`.

### Next, still mostly UI

7. **F9.** Preview reload via `switchMap`, with an error state that is not “no policies”.
8. **F13.** `takeUntilDestroyed` on item-detail loads.
9. **F11.** Extract the duplicated facts pipeline so item detail and add purchase cannot drift. This is the seam F4 and F1 will later plug a server decision into.
10. **F12.** Spec `party-detail` corrections and `ReferenceApi` create-with-similar-name. Those are the current “user fixed the match” writes.

### Larger changes

11. **F1 + F2 together.** They are one contract: the matcher returns a decision and candidates; the client posts a selection or a rejection; the server stores an alias or an exclusion. Doing the picker UI before the contract just invents a third copy of the 80% rule.
12. **F3.** Split item detail after the intake helper exists, so the move is mechanical. Order inside the file: coverage drawer (template roughly lines 601–726), then the policies block (352–494), then the edit drawers (729–827).
13. **F7.** Same treatment for plan and policy pages: cancel sheet out, document host shared, page class left as load/save/router.
14. **F4.** Switch auto-apply over to the server decision flag once F1’s payload exists. Until then, require the review panel whenever a proposal has no `partyId`.

### What not to do first

- Introducing NgRx. Cross-route state is already in a handful of services, and the bugs are inside page classes.
- A blanket i18n pass (F15) before the copy stops moving.
- Splitting `purchase.models.ts` (655 lines) for its own sake. It is a type module. Split it when the coverage types move with the extracted drawer.

## How this review was done

Read-only pass over routing, core services, the largest pages, the match/confidence call sites, admin and settings, and the spec layout. Line counts were taken from the tree. Claims in the area files cite the file and the line range that was read. No application code was modified.


</cursor_untrusted_data_1337>

---

<cursor_untrusted_data_1337 source="CallDynamicTool">

# Area 1 — Platform, session, and shell

[Back to the overview](../CODE_REVIEW.md)

## What this area is

Bootstrap, routing, the signed-in shell, and the services every feature uses for session, HTTP, theme, offline, and uploads.

| Piece | File | Lines (approx.) | Role |
| --- | --- | --- | --- |
| Root | `src/app/app.ts` | 10 | Banners + `router-outlet` |
| Config | `src/app/app.config.ts` | 31 | Router, HTTP interceptor, service worker, auth and theme initializers |
| Routes | `src/app/app.routes.ts` | 120 | Public auth, legal, shell children |
| Session | `src/app/core/auth.service.ts` | 212 | Token signal, refresh, profile, terms, Google, invitations |
| HTTP | `src/app/core/api.interceptor.ts` | ~65 | Cookies, bearer, 401, 403 reauth |
| Guards | `src/app/core/guards.ts` | ~70 | Auth, guest, terms, account choice, operator, owner, business |
| Problems | `src/app/core/problem.ts` | — | ProblemDetails → `Problem` |
| Reauth | `src/app/core/reauth.service.ts` + `layout/reauth-modal.component.ts` | — | Operator step-up |
| Unsaved | `src/app/core/unsaved-changes.ts` | — | `canDeactivate` + confirm modal |
| Theme | `src/app/core/theme.service.ts` | 88 | `data-theme` / `data-mode`, `localStorage` key `stuffit.theme` |
| Uploads | `upload-queue.service.ts`, `upload-sync.service.ts` | 116 / 121 | IndexedDB queue, Wi-Fi flush |
| Shell | `src/app/layout/shell.component.ts` | 284 | Header, nav, account switch, bell host, four background services |
| PWA | `public/share-sw.js`, `ngsw-config.json`, `core/pwa.service.ts` | — | App shell plus Web Share Target |

`src/main.ts` calls `reloadWhenRestoredFromCache` so a page restored from the back-forward cache cannot show a stale signed-out shell.

## Session and HTTP

`AuthService` documents the model in its file header: access token in a signal only, refresh via httpOnly cookie, `initialize()` awaited from `provideAppInitializer` before routing. `refreshInFlight` is shared so two 401s do not rotate the cookie twice. The interceptor (`api.interceptor.ts`):

- Limits itself to `environment.apiBaseUrl + '/api/'`.
- Sets `withCredentials: true`.
- Adds `Authorization` unless `authEndpoint` matches.
- On 401, if the in-memory token already changed, retries once with the new token (lines 41–43). Otherwise refreshes, retries, or `expireSession()`.
- On 403 with `reauth_required` or `two_factor_required`, opens `ReauthService` and retries. `two_factor_setup_required` navigates to `/settings/security`.

This is the strongest part of the client. Specs: `auth.service.spec.ts`, `api.interceptor.spec.ts`, `reauth.spec.ts`, `back-forward-cache.spec.ts`.

### Gaps

**Anonymous auth URLs are a regex, not a list** (`api.interceptor.ts` line 16):

```ts
const authEndpoint = /\/api\/auth\/(login|signup|refresh|logout|forgot-password|reset-password|verify-email)$/;
```

`/api/auth/google`, verify-signup, and account switch are not in it. A signed-in tab that hits those URLs still attaches the bearer. Low impact (the server should ignore it), but the comment above the regex says those calls never carry a bearer.

**`safeReturnUrl`** (`guards.ts` lines 19–22) accepts any string that starts with `/` and not `//`. `authGuard` puts the raw `state.url` into `returnUrl`; login reads it back through `safeReturnUrl`. Backslash and encoded-slash tricks are not rejected. Worth a router parse rather than a prefix check (finding F14).

**`expireSession`** navigates to login with the current URL. Login sanitizes on read, so this is safe only as long as every consumer keeps using `safeReturnUrl`.

No access token was found in `localStorage`. Keys that do persist are theme, view mode, PWA hints, upload preferences, and coverage-tick memory (`wb.coverage-choice.*` on the add-purchase page). The last one is a product choice stored only in that browser (see area 4).

## Guards and routes

| Guard | Used on | Check |
| --- | --- | --- |
| `authGuard` | Shell, choose-account, accept-terms | `isAuthenticated()`, else `/login?returnUrl=` |
| `guestGuard` | Login, signup | Signed-in users go home |
| `termsGuard` | Shell | `termsAcceptanceRequired` → `/accept-terms` |
| `accountChoiceGuard` | Shell | Multiple accounts and no choice yet |
| `operatorGuard` | `/admin/**` | Operator, and 2FA set up |
| `operatorHomeGuard` | Home | Operator not in customer view → `/admin` |
| `administratorSettingsGuard` | Settings → security | Operator |
| `ownerGuard` | Settings → billing | Owner |
| `businessGuard` | Settings → people | Business account |
| `unsavedChangesGuard` | Item, plan, policy, add purchase | `HasUnsavedChanges` + confirm modal |

`forgot-password` and `reset-password` are not behind `guestGuard` (`app.routes.ts` lines 17–18). A signed-in user can open them. Minor.

`path: '**'` redirects to `''` (line 119). A bad deep link looks like Home.

`app.routes.spec.ts` checks lazy loading and route order. `guards.spec.ts` covers `safeReturnUrl` only. `guards.consent.spec.ts` and `account-membership.spec.ts` cover terms, operator, owner, and business. `authGuard` and `guestGuard` have no direct spec.

## Shell

`ShellComponent` (284 lines) is the composition root for the signed-in app:

- Starts and stops `UnreadService`, `NewItemsCountService`, `SetupNoticesService`, and `UploadSyncService` for the lifetime of the shell.
- Renders desktop nav and a phone tab bar. Customer labels are Home, My Items, New Items, Returns, Notifications (`shell.component.ts` around line 232). Operator mode adds Review, Companies, Feedback, Businesses (Review at line 210).
- Account `<select>` calls a full reload via `RedirectService` on switch, which is appropriate for swapping the refresh cookie.
- Hosts the reauth modal, the legacy-uploads prompt, and the confirm modal.
- Alpha-test banner with a local dismissal.

Nav entries are inline arrays. `account-links.ts` (22 lines) is the pattern to copy: a const the shell and the account page both use. Customer vs admin nav should be the same kind of const so a route rename cannot leave the tab bar wrong. That matters because Returns and Review are the two links that currently point at placeholders (findings F5, F8; details in areas 3 and 6).

Account menu uses `role="menu"` and opens on hover as well as click. There is no roving tabindex. The bell dropdown is a `region`, closes on Escape, and does not trap focus. Reauth is a proper `role="dialog"` with `aria-modal`.

### Bell load failure

`load` (lines 110–118) sets `loading` and, on error, only clears it. The success path is the only one that writes `items`. The template (lines 53–56) treats “not loading, no items, no standing notices” as “You are all caught up.” A failed `list()` and an empty inbox look the same (finding F10). `notification-bell.spec.ts` does not cover the error callback.

`SetupNoticesService` and the upload sync each poll about once a minute while the shell is mounted, and also refresh on focus. That is reasonable for an inbox app; it should stay behind the shell so signed-out screens do not poll. They already do.

## Uploads, PWA, theme

`UploadQueueService` stores receipt batches in IndexedDB, scoped by account, with a legacy-batch path for files captured before an account id existed. `UploadSyncService` flushes on an interval, on `online`, and on focus, and refuses cellular when the user asked for Wi-Fi only (`connection.ts` reads the Network Information API). `upload-sync.service.spec.ts` is one of the better specs in the repo (account isolation, offline, legacy batches).

`refresh()` on the queue reads the whole store more than once (mine vs legacy). One `getAll()` and an in-memory split would do.

`public/share-sw.js` handles `POST /share-target`: it clears the `stuffit-share` cache and `cache.put`s every file, then redirects to `/share`. There is no count or byte cap. A huge share can fill the origin’s cache. The Angular worker (`ngsw-config.json`) does not cache `/api/**`, which is correct for private data. Production registration is `share-sw.js`, which then `importScripts('ngsw-worker.js')` (`app.config.ts` lines 24–25).

Theme tokens live in `src/styles.css`. `index.html` has an inline script that sets `data-theme` before first paint, duplicating `THEME_STORAGE_KEY` and the preset ids from `ThemeService`. The comment in `styles.css` (lines 7–9) says to update both. A build-time shared list would remove that trap. `theme.service.spec.ts` and `theme-contrast.spec.ts` cover persistence and contrast.

`scripts/set-env.mjs` runs as `prebuild` and injects public contact/legal strings. `legal.ts` still contains bracket placeholders for values that have not been set. That is a launch checklist item, not a structural defect.

## Recommendations

1. Replace `authEndpoint` with a `Set` of path suffixes, and extend `api.interceptor.spec.ts` (it already asserts the current exclusions).
2. Implement `safeReturnUrl` as “parses as an in-app `UrlTree`”.
3. Move shell nav arrays next to `account-links.ts`. Do the Returns and Review target fixes in the same edit (F5, F8).
4. Bell: `error` signal, copy that is not “caught up”, retry button, one spec.
5. Optional: a tiny lifecycle helper so the shell’s `ngOnDestroy` is not the only place that stops the four pollers. Not urgent; the shell is 284 lines, not 2,000.
6. Cap share-target file size and count in `share-sw.js`.

Leave `AuthService` as the session facade unless profile/terms methods start growing. Splitting “profile” out is tidy and not load-bearing.


</cursor_untrusted_data_1337>

---

<cursor_untrusted_data_1337 source="CallDynamicTool">

# Area 2 — API clients and domain models

[Back to the overview](../CODE_REVIEW.md)

## What this area is

`src/app/core` is 107 files, about 6,400 production lines and 2,100 spec lines. Roughly half of the production lines are typed models and small pure functions (`format.ts`, `certainty.ts`, `coverage-length.ts`, `plan-question.ts`, `document-facts.parties.ts`). The other half is HTTP.

There is no repository/mapper layer beyond a few `pipe(map(...))` calls. Components subscribe. That is a consistent choice, and it is why matching policy leaked upward: the client types include scores, and the pages decide what the scores mean.

## API clients

Every `*.api.ts` follows the same shape: `inject(HttpClient)`, `base = environment.apiBaseUrl + '/api/...'`, methods return `Observable<T>`, errors are not caught in the service.

| File | Calls |
| --- | --- |
| `account.api.ts` | Profile, privacy export/delete, 2FA |
| `admin-brands.api.ts` | Operator brand list, warranty suggest/confirm, saved documents |
| `admin-feedback.api.ts` | Operator feedback queue |
| `admin-stores.api.ts` | Operator store list, return-policy suggest/confirm, saved documents |
| `business.api.ts` | Members, ownership transfer, operator business admin |
| `claim-guidance.api.ts` | Claim-wizard questions and guidance |
| `document-facts.api.ts` | Intake read, stored read, apply warranty, keep-for-store |
| `document-reading.api.ts` | Structured read for plan and insurance documents |
| `feedback.api.ts` | User feedback |
| `inbox.api.ts` | Pending items, coverage preview, upload, accept, return matches |
| `insurance.api.ts` | Policies, links, documents |
| `items.api.ts` | List, detail, dashboard, returns in progress, people |
| `mailbox.api.ts` | Link, scan, unlink |
| `maintenance.api.ts` | Maintenance lines |
| `notifications.api.ts` | List, preferences, unread |
| `parts.api.ts` | Parts on a vehicle item |
| `party-notes.api.ts` | Operator notes |
| `plan-types.api.ts` | Plan-type catalog, including `/api/admin/plan-types` |
| `plans.api.ts` | Protection plans |
| `purchase.api.ts` | Purchases, items, coverages, proposals, dismissals, documents |
| `recoveries.api.ts` | Money recovered |
| `reference.api.ts` | Parties, policies, categories, models, cards, benefits |
| `service-history.api.ts` | Repair orders |
| `todos.api.ts` | Todos |
| `vehicles.api.ts` | Vehicle record and odometer |

`ReferenceApi.scope(admin)` (lines 38–40) prefixes `/api/admin` for operator writes. The same screen component is reused for “my stores” and “shared data” by passing `admin`. That is easy to misuse and is currently spelled out in the class comment. A new endpoint should follow it or the operator will silently write into the personal namespace.

`inbox.api.spec.ts` is the only dedicated HTTP spec among these clients. Interceptor behavior is tested separately. Purchase and reference, the two clients with the most call sites, have no contract tests of their own; page specs mock them with spies or `HttpTestingController` locally, so a path typo in the service can still slip if a page spec stubs the method.

### The one mapper

`PurchaseApi.proposals` flattens a nested trust object because “the screens read it flat” (`purchase.api.ts` lines 102–107):

```ts
map((list) => list.map((p) => (p.trust
  ? { ...p, confidence: p.confidence ?? p.trust.value, confidenceBand: p.trust.band, confidenceReason: p.trust.reason }
  : p)))
```

`ProposedCoverage` still carries both shapes (`purchase.models.ts` lines 472–485): flat `confidence` / `confidenceBand` / `confidenceReason`, plus `trust` and `applicability`. Inbox pending coverage uses the flat fields directly (`inbox.api.ts` around lines 41–43). Two payloads, one word function. Any new band field has to be added in both models and in this mapper or item detail will not see it.

## Models that are doing too much work as documentation

`purchase.models.ts` is 655 lines of interfaces: purchases, items, coverage, proposals, vehicle and part inputs, plan inputs. `plans.models.ts` is 380. `reference.models.ts` is 281. They are not god classes; they are the contract. The risk is that product rules hide in comments on the fields (`usualWindow`, `categoryDoubt`, `trust.value`) and the pages re-encode those comments as `if` statements. When the API review changes a band, these comments and `certainty.ts` both need an edit, and nothing fails to compile if one of them is missed.

`ProposedCoverage.applicability` is `{ value: number; reasons: string[] }`. `confidenceTip` on the item page turns `value` into a percent. That is presentation of a score the certainty module’s own header says not to show as a percentage (area 5).

## Pure functions that are actually domain rules

These are the right shape (pure, tested) and the wrong owner (the client):

### `certaintyWord` (`certainty.ts`, 11 lines)

```5:10:src/app/core/certainty.ts
export function certaintyWord(opts: { confidence?: number | null; band?: string | null; attached?: boolean }): string {
  if (opts.attached) return 'Attached';
  if (opts.band === 'verified' && (opts.confidence ?? 1) >= 0.8) return 'Confirmed';
  if ((opts.confidence ?? 0) >= 0.8) return 'Highly Likely';
  if (opts.band === 'likely' || (opts.confidence ?? 0) >= 0.5) return 'Likely';
  return 'Unconfirmed';
}
```

`certainty.spec.ts` locks the edges, including “verified band at 0.7 is Likely, never Confirmed”. Callers still pass the raw number. A missing `confidence` with `band: 'verified'` is treated as Confirmed because of `?? 1` (line 7). That default is generous.

`CERTAINTY_TIP` in `coverage-length.ts` (lines 25–31) is the badge tooltip and is written to match those words. `FROM_BADGE` (lines 16–21) labels merchant, manufacturer, card, plan, store. `BAND_LABEL` in `format.ts` is a separate map used on party policy history, not on the purchase flow. Three vocabularies: certainty words, high/medium/low on document reading, and band labels on operator policy rows.

### `FactParties` (`document-facts.parties.ts`, 39 lines)

When a ticked store or brand proposal has no `partyId`:

- Close match against the user’s own party: `updateParty` renames it (`Milwaukee` → `Milwaukee Tool`), with `confirmDuplicate: true` (lines 27–34).
- Close match against a shared party: do not rename; the item keeps the shared party (line 28).
- Otherwise `createParty` into the user’s list (lines 36–37).
- Store names are cut at the first `#` or comma (`storeName`, lines 19–22), so `The Home Depot #2310, Testville, ME` becomes `The Home Depot`.

This is matching policy. It runs in the browser, it writes parties as a side effect of “apply the document”, and it does not record that the printed string is an alias of the party it just bound. The next document with the same odd spelling goes through the same guess. See finding F2.

### Other pure modules worth keeping

`format.ts` (220 lines, several specs) is display formatting and belongs here. `plan-question.ts`, `coverage-length.ts`, `free-year.ts`, `photo-quality.ts`, `image-shrink.ts`, `document-class.ts` are the same kind of thing: UI or file helpers with a single job. `plan-reading.ts` and `policy-reading.ts` live next to their features rather than in `core`; that is fine because they are feature parsing, and they have specs.

## Error and loading conventions the data layer forces on screens

Services return cold observables. Every screen repeats:

```ts
this.saving.set(true);
this.api.save(body).subscribe({
  next: () => { this.saving.set(false); /* refresh */ },
  error: (e) => { this.saving.set(false); this.problem.set(toProblem(e)); }
});
```

A shared `watch(statusSignal)` operator would remove boilerplate and would not change architecture. It would not fix the real gap: some errors are dropped (`catchError(() => of(null))` on brand match and coverage preview), and the UI cannot tell “the server said there is no match” from “the request failed”. Those `of(null)` calls are in the pages, not the services, but the services give the pages no typed error channel other than the HTTP error.

## Recommendations

1. Extend `ProposedCoverage` and `PendingCoverage` with the decision and candidates the matcher already computed. Do the flattening in `PurchaseApi.proposals` so item detail cannot forget a new field. Inbox coverage should use the same type or a documented shared `CoverageSuggestion` interface; today the two interfaces overlap field-by-field.
2. Move `certaintyWord` to a pure display of `band` plus `attached`. If the API cannot send the word, have it send the band the UI should print (`confirmed` | `highlyLikely` | `likely` | `unconfirmed`) so 0.8 and 0.5 exist in one place.
3. Stop creating parties inside `FactParties` as an implied alias. `createParty` / `updateParty` can stay for an explicit “Add this store”, which `PartyPickerComponent` already does with a similar-name confirmation. Auto-rename on a close string match should be a server decision the user sees in the review panel (`outcome: 'correct'` already exists for spelling).
4. Add `HttpTestingController` specs for `ReferenceApi` (create, similar-name 409, `matchBrand`, `correctSeller`) and `PurchaseApi.proposals` / `dismiss`. Those are the match write-paths.
5. Do not introduce a generic repository base class. The current clients are readable. The missing piece is the contract fields, not another abstraction.


</cursor_untrusted_data_1337>

---

<cursor_untrusted_data_1337 source="CallDynamicTool">

# Area 3 — Items, coverage editing, and claims

[Back to the overview](../CODE_REVIEW.md)

## What this area is

`src/app/features/items` is the largest feature: 42 files, 10,070 lines, 4,910 of them production, 23 specs. It is the screen people live on after intake.

| Piece | Lines | Job |
| --- | --- | --- |
| `item-detail.page.ts` | 2,118 | The item hub |
| `item-detail.page.spec.ts` | 1,171 | Read-only layout, returns, people, navigation (~55 tests) |
| `item-edit.spec.ts` | 1,017 | Edit mode, suggestions, coverage, documents (~57 tests) |
| `items.page.ts` | 380 | Search, facet filters, empty state |
| `claim-wizard.page.ts` | 357 | Live refund/claim questions |
| `refund-wizard.page.ts` | ~220 | Sample-data design, saves nothing |
| `vehicle-panel.component.ts` | 283 | VIN, lease, odometer |
| `parts-panel.component.ts` | 268 | Parts on a vehicle |
| `returns-in-progress.page.ts` | — | Real returns list |
| Plus | — | Maintenance, service history, plan offers, insurance, recoveries, todos, condition, miles |

Related clients: `items.api.ts`, `purchase.api.ts`, `claim-guidance.api.ts`, `recoveries.api.ts`, `maintenance.api.ts`, `parts.api.ts`, `service-history.api.ts`, `vehicles.api.ts`, `todos.api.ts`.

## `ItemDetailPageComponent`

The file header (around lines 108–114) describes one item: what it is, where it came from, and everything that covers it. The class does all of that plus the editing workflows.

**Template, by block** (inline, so line numbers move if the template changes; they matched this tree):

| Lines | Block |
| --- | --- |
| 119–155 | Header actions: edit, dispose, refund, replace, delete |
| 157–213 | Plan undo, replacement links, courtesy return, return banners |
| 215–258 | Item and purchase facts |
| 264–316 | Suggested coverage, edit mode |
| 318–350 | Parts ask, plan ask, vehicle / service / maintenance / parts panels |
| 352–494 | Policies list |
| 496–504 | Plan offers, add-on protection, insurance, recoveries, todos |
| 506–591 | Files, document read, warranty choice, facts review |
| 593–598 | Start return, claim panel |
| 601–726 | Coverage drawer (new plan, lifetime, miles, certified, prorated) |
| 729–827 | Purchase edit, item edit, return, replace drawers |
| 830–860 | People on a shared account |

**Injected services** (around 869–947): `ItemsApi`, `PurchaseApi`, `AuthService`, `Router`, `ConfirmService`, `ToastService`, `UnreadService`, `ReferenceApi`, `AccountApi`, `DocumentFactsApi`, `PlansApi`, `PlanHandoffService`, `PlanUndoService`, `FactParties`, plus route flags.

**Method groups** on the class (about line 864 to the end):

- Load and refresh: `load` (about 1311–1328), route `effect`.
- Document intake: `readDocuments`, `showFacts`, `applyFacts`, `putFacts` (about 1271–1302), `decideWarranty`.
- Suggestions: `accept`, `isPicked`, `pick`, `suggestAgain`, `confidenceTip` (1783–1876).
- Coverage drawer: `open` / `openProposalEdit` / `openNewCoverage` / `openNewPlan`, `saveCoverage`, `savePlan` (1877–2017).
- Purchase and item drawers: `savePurchase`, `saveItem` (2032–2087).
- Returns and status: `saveReturn`, `changeStatus`, `remove` (1597–1724).
- People and files.

`putFacts` on this page **writes immediately** (`purchases.update` and `updateItem` via `forkJoin`). The add-purchase page’s `putFacts` only patches the form. Same review component, different commit semantics. A user who learns “Apply does not save until I press Save” on add-purchase will be wrong on the item page.

### Subscriptions

A search for `.subscribe(` in this file finds **49** calls. There is no `ngOnDestroy`, no `DestroyRef`, and no `takeUntilDestroyed`. The constructor subscribes to `api.members()` for the life of the component. `load(id)` does not cancel the previous request, so a fast id change can apply the first response after the second (finding F13). Cards (`card-detail.page.ts`) and `PartyPickerComponent` already use `takeUntilDestroyed`; this page is the one that most needs it.

### Suggestion ticking

```1793:1846:src/app/features/items/item-detail.page.ts
  private static readonly PickedFrom = 0.8;   // keep in step with ApplicabilityFactors.TickedFrom on the server
  // ...
  protected isPicked(item: Item, p: ProposedCoverage): boolean {
    return this.picks()[`${item.id}:${p.key}`] ?? (p.confidence ?? 1) >= ItemDetailPageComponent.PickedFrom;
  }
```

`confidence ?? 1` means a proposal with no score is pre-ticked. Accept posts `proposalKey` through `PurchaseApi.addCoverage` (lines 1783–1790). Dismiss posts `{ proposalKey, reason }` with reason `notApplicable` or `unknown` (`purchase.api.ts` lines 114–116; asserted in `item-edit.spec.ts` around the dismiss tests). That is a per-item “don’t suggest this key again”, not a statement about the store or the brand. “Suggest again” reloads with `includeSetAside: true` (line 1799).

`confidenceTip` (lines 1836–1842) builds `Policy verified ${percent}%` and `Fit for this purchase ${percent}%`. `percent` is `Math.round(v * 100)` (line 1832). The tooltip is the only place item detail shows a number. `certainty()` on the same class uses `certaintyWord`, and passes `attached: p.key?.startsWith('doc:')`. The add-purchase page does not use the `doc:` prefix; it uses `fromDocument`. Two attachment tests.

`label()` (around 1397–1401) rewrites source text such as “Stated on receipt” for certified and prorated coverage. `status()` (around 1404–1417) is a branchy display rule. The claim wizard’s comment says this kind of rule lives on the server. The item page still owns it.

### Courtesy returns

A courtesy return is stored in `sessionStorage` under `stuffit.courtesy.${id}` (around 1051–1064). It does not survive a second device, and it is not an API object. Fine for a session hint; risky if support staff expect it to be real state.

## The panels that already have a single job

These are the pattern the page should keep following. Each is a component with a small spec:

- `claim-panel.component.ts` — link to `/items/:id/refund`.
- `vehicle-panel`, `parts-panel`, `maintenance-panel`, `service-history.component.ts` — vehicle subsections, each with its own API.
- `plan-offers.component.ts`, `addon-protection.component.ts` — plan upsell; the parent still performs the navigation.
- `item-insurance.component.ts`, `item-recoveries.component.ts`, `todo-card.component.ts`, `condition-block.component.ts`, `miles-line.component.ts`.
- `protection-stack.ts` — pure helpers (`planState`, `stackNote`). Good. Keep rules of this shape out of the page.

`items.page.ts` (380 lines) is a list: URL-driven search, `FacetFilterComponent`, upload entry via `ItemsHeaderComponent`. It is a reasonable size. It does not need to be part of the split.

## Claims

`claim-wizard.page.ts` (~357 lines) loads questions from `ClaimGuidanceApi` and displays guidance. The page does not encode eligibility. `claim-wizard.page.spec.ts` (~279 lines) covers the lifetime term, exclusions, and proof copy. This is the model the coverage page should move toward: the server decides, the client asks and confirms.

`refund-wizard.page.ts` is a different thing. The header in the file and the route comment (`app.routes.ts` line 51, `items/sample/refund`) describe a design on `sample-item` data. Nothing is saved. It is linked as a route in the same app as the live wizard. If nothing in the shell navigates there, it is still a public route inside the auth shell. Unlink it or guard it (finding F15).

## Returns

Two routes:

- `/returns` → `ReturnsPageComponent`. The file header says “a first design, as plain HTML with made-up examples and no data behind it.” The template badges itself `First design: example data` (`data-testid="placeholder"`) and shows a Sony WH-1000XM5 at Best Buy with disabled buttons (`returns.page.ts` lines 4–35).
- `/returns/in-progress` → `ReturnsInProgressPageComponent`, which calls `ItemsApi.returnsInProgress()`.

`shell.component.ts` line 232 puts **Returns** on `/returns`. `shell.component.spec.ts` asserts that label list, so the mock is an intentional nav target, not a leftover file. It will read as a bug: the dates in the mock can even be inconsistent with “days left” (the sample copy says the window closes on a date and also that the return was started after that). Finding F5. The fix is a one-line path change plus the shell spec, or replacing the mock. Do not leave both and hope people follow “Open the working list”.

## Tests

The split between `item-detail.page.spec.ts` (read mode) and `item-edit.spec.ts` (edit, suggestions, documents, coverage) is deliberate and is why both files are over 1,000 lines. They lock behavior that a refactor must not break: 80% pre-tick, dismiss reasons, PayPal funding warnings, warranty-from-document, file retention. They are also why the page has not been split: every extraction has to drag a huge TestBed with it.

That is an argument for extracting a pure helper and a dumb drawer first, with new small specs, and leaving the page specs as integration smoke. Growing `item-edit.spec.ts` further to cover the next matching change will make the split harder.

Gaps relative to the production file:

- No test that `load` ignores a stale response.
- Document intake on the item is covered in `item-edit.spec.ts`, and the same pipeline on add-purchase has its own spec, but nothing asserts they map a proposal the same way.
- Coverage drawer validation is only reached through the page spec.

## Recommendations

1. **Coverage drawer component.** Move the template block around lines 601–726 and `saveCoverage` / `savePlan` / the draft type. Inputs: item id, purchase date, whether miles and plans are allowed. The page spec’s coverage cases move with it.
2. **Policies section.** Template around 352–494 plus `status`, `label`, and the suggestion checkbox list. This is where F1 and F6 land later; isolating it means the decision-field change does not edit a 2,000-line file.
3. **Edit drawers.** Purchase, item, return, replace (around 729–827) are each a form with a save method.
4. **`DocumentIntake` helper** shared with add-purchase (finding F11, area 4). Item detail’s `putFacts` should take an explicit `commit: 'now' | 'form'` so the save timing is obvious.
5. **`load` and document read** use `switchMap` and `takeUntilDestroyed` before any of the extractions. That is the race that can show the wrong item’s coverage.
6. **Returns nav** (F5) is independent of the split and should happen first.
7. Do not fold the vehicle/parts/maintenance panels back into the page. They are the evidence the split works.


</cursor_untrusted_data_1337>

---

<cursor_untrusted_data_1337 source="CallDynamicTool">

# Area 4 — Purchases, inbox, and document intake

[Back to the overview](../CODE_REVIEW.md)

## What this area is

How a purchase enters the app: email and receipt inbox, the full add form, and the document-facts review that also runs on the item page.

| Piece | Lines | Job |
| --- | --- | --- |
| `add-purchase.page.ts` | 1,075 | Full form, coverage preview, document intake, save |
| `add-purchase.page.spec.ts` | 1,124 | Documents, warranty offer, save, pending fill |
| `new-items.page.ts` | 564 | Inbox: quick add, dismiss, returns, paging |
| `new-items.page.spec.ts` | 822 | Quick add, returns, trust copy |
| `receipt-scan.component.ts` | — | Multi-page capture, shrink, queue |
| `purchase-redirect.ts` | — | `/purchases/:id` → first item |
| `document-facts-review.component.ts` | 162 | “What we found in your document” |
| `inbox.api.ts` | 289 | Pending items and coverage preview |
| `document-facts.api.ts` + models + `document-facts.parties.ts` | — | Read and apply |
| `upload-queue` / `upload-sync` / `image-shrink` / `photo-quality` | — | Offline receipts |

Routes (`app.routes.ts`): `/add` is New Items, `/add/new` is the form (unsaved-changes guard), `/purchases` redirects to `/items`, `/purchases/:id` is the legacy redirect.

## Add purchase

`AddPurchasePageComponent` is the second god page. Injected: `PurchaseApi`, `ReferenceApi`, `Router`, `ActivatedRoute`, `InboxApi`, `ItemsApi`, `AuthService`, `NewItemsCountService`, `DocumentFactsApi`, `ToastService`, a tracking API, `FactParties`, `AddCarryService`.

Template blocks:

| Lines | Block |
| --- | --- |
| 92–124 | Add-type tiles, upload, facts overlay, warranty offer |
| 126–188 | Store, date, card, PayPal, order number |
| 190–297 | Per item: category, brand, name, model, coverage checkboxes, plan question |
| 299–307 | Save, add another, cancel |

The class also tracks unsaved changes (`ChangeTracker`), debounces coverage preview, remembers ticks in `localStorage`, completes a pending inbox item on save, and uploads files after the purchase exists (`save` around 963–1026, then `uploadThenOpen`).

### Preview reload

```438:444:src/app/features/purchases/add-purchase.page.ts
  ngDoCheck(): void {
    const key = [this.seller?.id, this.date, this.cardId, ...this.items().map((i) => [i.maker?.id, i.categoryId, i.model, i.name].join('/'))].join('|');
    if (key === this.previewKey) return;
    this.previewKey = key;
    clearTimeout(this.previewTimer);
    this.previewTimer = setTimeout(() => { this.loadPreviews(); this.keepNameAndModel(); }, 400);
  }
```

The key means change detection does not refetch every cycle. `ngOnDestroy` clears the timer. What it does not do is cancel the HTTP call. `loadPreviews` (lines 473–480) subscribes per item and maps errors to `null`. A late response for the previous store can replace the new store’s preview, and a failure looks like an empty suggestion list (finding F9). An effect or `valueChanges` + `switchMap` is the usual Angular 20 shape; `ngDoCheck` is here because seller and items are plain fields, not signals.

### Tick, tuck, and document confidence

Constants at lines 67–74:

```ts
const TICKED_FROM = 0.8;
const DOCUMENT_TRUST = 1;
const DOCUMENT_FITS = 0.95;
const DOCUMENT_FITS_CORROBORATED = 0.99;
const CORROBORATED_FROM = 0.6;
```

The comment says `TICKED_FROM` must stay aligned with `ApplicabilityFactors.TickedFrom` on the server. Nothing in the client enforces that except a comment and the specs that assume 0.8.

`isChecked` (lines 488–491):

- Ended windows are never ticked.
- A row “from the document” is ticked only if the warranty offer is on and `documentConfidence(c) >= 0.8`.
- Otherwise the user’s `coverageChoice`, or `(overallConfidence ?? 1) >= 0.8`.

`documentConfidence` multiplies trust 1 by 0.99 when the existing score is already ≥ 0.60, else by 0.95 (lines 534–536). The server’s score is replaced for display and for the tick. `certainty()` then runs `certaintyWord` on the **original** `overallConfidence` (line 574), while the checkbox uses the recomputed number. The badge and the checkbox can disagree.

`modelFit` (lines 550–557) does a normalized substring compare of the item model against `warrantyOffer.preview.models`. Empty model list means the paper fits. A model shorter than 3 normalized characters is `unknown` and blocks the document row via `fromDocument` (line 543). This is applicability logic.

`toggleCoverage` (lines 494–500) unticks every other `kind === 'return'` when one return is ticked. If the API sends two returns that can both apply (a holiday window and a manufacturer’s satisfaction guarantee that is also tagged `return`), the UI will not allow both.

`tucked` (lines 565–567) hides `return:*` keys under 0.5 until the user opens “other return windows” or ticks one. That is a hand-rolled “show fewer options” band. It is the closest the UI gets to “top 2–3”, and it is only for return keys, and the cut is 0.5 rather than a server rank.

Choices for a pending item are stored at `wb.coverage-choice.${id}` and plan edits at `wb.plan-edits.${id}` (lines 505–531). A second browser, or quick add on the phone, never sees those ticks. Quick add does not read them either.

### Brand match

```869:875:src/app/features/purchases/add-purchase.page.ts
  protected matchBrand(item: ItemDraft): void {
    const name = item.name.trim();
    if (item.maker || name.length < 3) return;
    this.reference.matchBrand(name).pipe(catchError(() => of(null))).subscribe((brand) => {
      if (brand && !item.maker && item.name.trim() === name) this.setMaker(item, brand);
    });
  }
```

`GET /api/parties/match-brand?text=`. One party or null. No confidence, no alternatives, errors become “no brand”. There is no `match-store` client method. The store is whatever `PartyPickerComponent` search returns, or whatever document facts propose. A wrong silent brand sticks until the user notices the maker field.

### Document facts

`readDocuments` (lines 640–657) calls `DocumentFactsApi.read` with the current form as context.

- Zero proposals: a toast, no panel (line 652).
- `fillsWithoutAsking`: every proposal is `useDocument`, none is `outcome === 'ask'`, none is `flag` (lines 661–663). `fillForm` calls `applyFacts` and toasts “Filled in from your document” (lines 666–669).
- Otherwise the review panel is shown.

`applyFacts` (comment at line 747: “Nothing is saved: the person still reads the form and saves it”) runs `FactParties.resolve` first. Resolve **does** write: it `createParty` or `updateParty`s before the purchase exists (area 2). The purchase form is local; the party book is not. A user who then hits Cancel can leave a renamed or newly created party behind.

`DocumentFactsReviewComponent` itself is well bounded. Header comment: the owner applies ticks; this component changes nothing. Conflicts (`outcome === 'ask'`) are radios, “Keep yours” vs “Use the document’s”, with a “Close, but not the same” vs “Conflict: choose one” badge (lines 36–52). Fills and spelling corrections are checkboxes. Unknown parties tell the user to pick on the form. That is a real ask-the-user UI. It is binary (current vs proposed), not a ranked list of known stores, and it never posts “remember this spelling”.

The same component is embedded on item detail, with a different `putFacts` (area 3). `fileKey` is duplicated (add-purchase line 81). PayPal helpers `isPayPal` / `bankCards` exist on both pages.

## New Items inbox

`new-items.page.ts` is a better size (564) and uses `DestroyRef` to stop timers (line 278).

What the row shows:

- Store text or seller name, date, money, missing fields, `check` (“Not sure of: …”).
- Coverage chips with `certainty(c)` and a warning color when `confidenceBand !== 'verified'` (lines 174–176, 193–194).
- A `trust-note` with `confidenceReason` when the band is not verified.
- Receipt coverage under 80% is called out: “Not added by a quick add” (line 190). The 0.8 is local again.
- `likelyItem` offers “Attach it there” (lines 197–199). One candidate, plus a search via the attach control.

`canQuickAdd` (lines 487–488) requires a name and an empty `check` array. `quickAdd` calls `inbox.accept(id)`, which posts `{}` (`inbox.api.ts` lines 234–236). The comment on the method says the server attaches the coverage it is 80% sure of and refuses with 409 when there is none. The UI cannot send “tick this one, not that one” on this path. The user who unticked a window on the full form and then quick-adds from another device gets the server’s default.

Return rows are the best candidate UI in the app (`new-items.page.ts` lines 124–136): every `ReturnCandidate` shows strength (`order` | `item` | `weak`), a reason, and its own button (`Mark it returned` or `Cancel the plan`). Nothing is changed until the click. Weak matches are included, not capped at three, but the user does pick. `returnMatches` is a preview; confirm sends the chosen `itemId`. That interaction is what store, brand, and policy match should look like.

## Receipt scan and the upload queue

`receipt-scan.component.ts` shrinks images, checks quality, and either uploads through `InboxApi` or enqueues via `UploadQueueService` when the sync service says to wait (offline or cellular). Specs exist (`receipt-scan.spec.ts`, `upload-sync.service.spec.ts`, `image-shrink.spec.ts`, `photo-quality.spec.ts`). This path is in better shape than the form: the queue has an account id, and the page does not reimplement matching.

`purchase-redirect.ts` loads a purchase and navigates to its first item. It subscribes once per id. Small, fine.

## Tests

`add-purchase.page.spec.ts` (1,124 lines) and `new-items.page.spec.ts` (822) lock the current thresholds: verified vs likely bands, tucked return windows, quick-add refusal when `check` is set, document auto-fill toasts. They will fight a move to server-driven decisions unless the fixtures gain a `decision` field and the assertions move off `0.8`.

`document-facts-review.spec.ts` covers the panel in isolation. There is no shared spec that runs one `FactProposal[]` through both pages’ `putFacts`.

## Recommendations

1. **F9 first**, inside this page only: replace `ngDoCheck` with a stream that `switchMap`s the preview and records `error` separately from `coverage: []`.
2. **Extract `PurchaseCoveragePreviewComponent`.** Inputs: the preview list and a `choices` model. Move `isChecked`, `toggleCoverage`, `tucked`, `certainty`, and the constants with it. The page keeps save and routing. When F1 arrives, this component is the only one that learns `decision`.
3. **Stop skipping the review panel when a store or brand proposal has no `partyId`** (a narrow version of F4 that does not need a new API). Auto-apply of name, date, and total can stay; creating a party should stay behind the panel.
4. **Do not add a client `matchStore` that mirrors `matchBrand`.** One silent bind is already one too many. Wait for candidates (area 5) and use the return-candidate row as the layout.
5. **Share the PayPal snippet and `fileKey`.** Trivial, and it removes a false “shared helper” that is copy-paste.
6. Quick add should keep posting “accept the server default” only if the row’s chips all say the server will auto-bind. If any chip is below the ask band, the button should open `/add/new?pending=` instead of `accept`. Today that distinction is `check.length` plus a local 0.8 on receipt lines, which misses a low-confidence coverage that has no `check` flag.


</cursor_untrusted_data_1337>

---

<cursor_untrusted_data_1337 source="CallDynamicTool">

# Area 5 — Plans, and the match / confidence UI

[Back to the overview](../CODE_REVIEW.md)

This file covers the plans feature and the cross-screen question the review was asked to answer: how store, brand, warranty, and policy matches are shown, whether the user can pick or correct them, and whether a correction teaches the API.

Matching is not a module. It is behavior spread across add purchase (area 4), item detail (area 3), this plans feature, parties and admin (area 6), and cards and insurance.

## Plans feature

| File | Lines | Role |
| --- | --- | --- |
| `plan.page.ts` | 1,256 | Add/edit/view one plan. Inline template is roughly the first 480 lines |
| `plan.page.spec.ts` | 816 | Page integration |
| `plans.page.ts` | — | List |
| `plan-lines.component.ts` | — | Covered appliances and systems |
| `plan-requests.component.ts` | 288 | Service requests on a plan |
| `plan-decision.component.ts` | — | Keep / claim / cancel prompt |
| `plan-start.component.ts` | — | Start-date help |
| `plan-reading.ts`, `plan-update.ts`, `plan-start.ts` | — | Pure: document properties → form fields |
| `plan-type` picker specs | — | Filling blank fields from a catalog type |

`PlanPageComponent` already delegates lines, requests, and the decision prompt. What remains in the page:

- Edit vs read mode and the whole form (`ngModel`, around the coverage notes and exclusions textareas near lines 210 and 299).
- File attach and `DocumentReadingApi` → `ReadingReviewComponent` → `planFill` / `applyToPlan`.
- Company match from the document: `suggestedCompany` when the read name is not a known party (the picker can be pre-filled; the user still searches or adds).
- `pickType` copies catalog `coverageNotes`, `exclusions`, and waiting period into blank fields (around line 658).
- Cancel, stop renewing, and refund as a multi-step drawer in the same template (around lines 404–478 and step signal near 567–585), even though `PlanDecisionComponent` exists for a different prompt.
- Item multiselect and device-insurance defaults.

`plan-reading.ts` is the right split. `NOTE_PARTS` maps read keys onto `coverageNotes` or `exclusions` paragraphs (`plan-reading.ts` around lines 102–160). Specs (`plan-reading.spec.ts`, `plan-update.spec.ts`) lock paragraph merging so a new exclusion does not wipe a limits paragraph. Keep that code pure. Do not move it back into the page.

The page is still a god component (finding F7): too many signals (`detail`, `editing`, `form`, `step`, document result, plan types, cancel fields) for one class. Extract the cancel/refund drawer first; it has the least to do with matching. Then extract the document block so it can share a host with `policy.page.ts`, which runs the same read → review → fill sequence on `DocumentReadingApi` with `policyFill` instead of `planFill`.

There is a third pipeline, document facts, used for receipts and warranty papers (area 4). Plans and policies do not go through `DocumentFactsReviewComponent`. A warranty PDF opened from a plan and the same PDF opened from an item can take different review UIs. Unifying the parsers is not required; unifying the “here is what we read, tick what to keep” interaction is.

Dead code: no `TODO`/`FIXME` cluster and no unused plan component turned up. The size is live behavior, not leftovers.

## How confidence is shown

The product rule in `certainty.ts` lines 1–3: words, never a percentage. Five words: **Attached**, **Confirmed**, **Highly Likely**, **Likely**, **Unconfirmed**.

| Surface | What the user sees | Number visible? |
| --- | --- | --- |
| Add purchase coverage rows | Badge from `certaintyWord`, tint class, tooltip from `CERTAINTY_TIP` | No. Tick uses a separate recomputed score (area 4) |
| New Items chips | `· Highly Likely` etc. Muted if `confidenceBand === 'verified'`, warning color otherwise. Reason in `trust-note` when not verified | The 80% phrase appears in copy for receipt lines under 0.8 (`new-items.page.ts` line 190) |
| Item detail suggestions | Word via `certainty()`. Tooltip from `confidenceTip`: “Policy verified 96%. Fit for this purchase 80%…” | Yes, tooltip only (`item-detail.page.ts` 1832–1842) |
| Document facts review | Shared / Verified / Yours badges, “Not sure: check it”, conflict radios | No score. `source()` can mention high/medium/low |
| Plan and policy reading review | high / medium / low on each extracted field | No `certaintyWord` |
| Party policy history | `BAND_LABEL` in `format.ts` | Operator-facing |
| Return candidates | `strength` order / item / weak, plus `reason` | No percent |

So the user can see a word, a color, a reason string, or a percent, depending on the screen. There is no single “we will add this unless you stop us” vs “pick one” vs “we need you to choose” control. Those behaviors exist, but they are inferred:

| Intended band | Current mechanism |
| --- | --- |
| Auto-bind | Pre-tick at ≥ 0.8. Quick add posts `{}`. `fillsWithoutAsking` writes the form. `matchBrand` sets the maker with no toast. |
| Show a few options | Full checkbox list of every coverage row. Return keys under 0.5 tucked. Return **item** candidates listed in full, each with a button. |
| Ask | Fact `outcome === 'ask'`. `PendingItem.check` blocks quick add. `flag` disables the proposed party. Unticked rows sit there until Save. |

`certaintyWord` also disagrees with a strict reading of the band enum. A `verified` band under 0.8 becomes Likely (tested). A missing confidence on a verified band becomes Confirmed (`?? 1`). Highly Likely is “confidence ≥ 0.8” even when the band is `unconfirmed`. The band is not the source of truth; the number is, with the band as a modifier.

## Can the user pick or correct a match?

Yes, in several local ways. No, not as a matcher feedback loop.

### Store and brand

- **Party picker** (`party-picker.component.ts`, 222 lines). Server search `parties({ q, role, limit: 8, categoryId })`. One selection. “Add …” creates a party. HTTP 409 with `similar[]` offers those names plus “Add anyway”. That is a duplicate guard, not a match shortlist: it only appears when create collides.
- **Typed item name → brand.** `matchBrand` fills an empty maker (area 4). The user can clear it and pick another. The rejected brand is not sent anywhere.
- **Document proposal with a `partyId`.** The API already resolved an alias (the model comment in `document-facts.models.ts` says so). The UI shows the resolved name. On conflict, the user picks current vs proposed. Applying a proposal with no `partyId` creates or renames via `FactParties` (area 2).
- **Item and purchase edit drawers.** Store and brand are editable and saved with the purchase/item. Changing “Best Buy” to “Target” updates that purchase. It does not record that the receipt’s printed string was wrong, so the next receipt with the same print can match the same way.
- **Unverified badge.** User-created parties show as unverified (`unverified-badge.component.ts`). Item detail can name them (“Corner Shop (store) and Odd Brand (brand) are …”, `unverifiedNames` around line 1822). That tells the user the party is private; it does not offer a “this is actually X” control.

### Warranty and return policy

- **Before save,** the add form lists preview rows as checkboxes. The user can untick. Save sends the ticked keys (the page comment around lines 423–426). Mutual exclusion is forced for `kind === 'return'`.
- **After save,** item detail loads `GET /api/items/{id}/proposals`. The user ticks, accepts (`POST .../coverages` with `proposalKey`), dismisses (`POST .../dismissals`), or edits the row then accepts. Dismiss reasons are `notApplicable` and `unknown` (`item-edit.spec.ts` expects those bodies).
- **Quick add** does not let the user pick rows. It explains, in small type, which receipt lines will be left off because they are under 80%.
- **Plan on a receipt.** `plan-receipt-facts.component.ts` shows qualitative checks (`coversMatch`, company check), not certainty words. A SKU mismatch can auto-untick on the add form (`keepNameAndModel` is called from the preview timer). The user can tick it back.

### Policy documents (plans and insurance)

- Reading review requires an explicit tick before fill. Good.
- Insurer on a policy: the page searches parties by exact-ish name (`policy.page.ts` around 485–488) and, on an existing policy, does not swap the insurer if the document disagrees (around 475–477). The user can still change the picker. No alias write.
- Scheduled items on a policy use `ItemPickerComponent`: one `likelyItem` plus search. Same “one suggestion, then search” pattern as New Items.

### Operator corrections

These are real writes, and they are the wrong actor for end-user aliases:

- `ReferenceApi.correctSeller`, `correctManufacturer`, `correctCardBenefit` require a note (`party-detail.page.ts` around line 595 for the seller call). They amend the shared or personal policy text.
- Admin brands/stores: suggest-from-web, then an operator confirms with a `sourceUrl` (`admin-brands.api.ts`, `admin-stores.api.ts`). Human confirmation of official policy copy, not “this receipt name means that store”.
- Card benefits: the cardholder confirms a proposed set via `confirmBenefits` (area 6). That is “these benefits apply to my card”, which is closer to a user confirmation than a string alias.

## What the UI would need for the API’s bands

Assume the matcher response grows a decision and, when it is not auto, a short candidate list. The UI work, in order:

1. **Types.** Add `decision: 'auto' | 'choose' | 'ask'` and `candidates?: { partyId or policyKey, label, band, reason }[]` to `PendingCoverage`, `ProposedCoverage`, and the fact proposal for store/brand. Flatten them in `PurchaseApi.proposals` next to the existing `trust` copy. Share one interface so inbox and item detail cannot drift.

2. **One presenter.** A `MatchChoiceComponent` used by coverage preview, item suggestions, and document-fact party fields:
   - `auto`: show the bound label, the certainty word, and Change.
   - `choose`: radio or buttons for at most three candidates, top one pre-selected, reason under each. Same layout as the return-candidate rows in `new-items.page.ts` lines 124–136.
   - `ask`: no pre-selection. Block quick add. This replaces the local `check` / `flag` / `< 0.8` combination once those flags are derived server-side. Until then, treat any of them as `ask`.

3. **Stop computing scores.** Delete `TICKED_FROM`, `PickedFrom`, `DOCUMENT_FITS`, `DOCUMENT_FITS_CORROBORATED`, `modelFit`’s effect on ticking, and the numeric comparisons in `certaintyWord`. If model-list fit stays a feature, the preview payload should already have `decision: 'ask'` and a reason (“model not in the list”). The substring compare in the client (`add-purchase.page.ts` 550–557) will not match the server’s normalizer forever.

4. **Post the pick.**
   - Coverage: keep `POST /coverages` with `proposalKey` for the chosen row, and send the keys the user turned off so the server does not also apply its auto set. Quick add should either stay “accept server autos only” or accept a body of keys. An empty body plus a client that showed different ticks is finding F1.
   - Store/brand: `POST` an alias `{ field: 'store' | 'brand', printed, partyId }` when the user picks a candidate or changes the picker away from the suggestion. `POST` an exclusion `{ printed, partyId: null }` when they choose “none of these” or clear a silent `matchBrand`. Do not treat `dismissals` as that write. A dismissal means “not this item”.
   - `FactParties.resolve` should not `createParty` for an auto path. “Add as my store” stays an explicit picker action, which already confirms similar names.

5. **Copy.** Use `certaintyWord` only as a label for the band the API sent. Remove percents from `confidenceTip`, or gate them behind a control whose accessible name is “Score details” so the default UI matches the module comment. Show `confidenceReason` whenever the decision is `choose` or `ask`, which New Items already does for non-verified bands.

6. **Specs to rewrite, not extend blindly.** `certainty.spec.ts`, the 80% cases in `item-edit.spec.ts`, and the band fixtures in `add-purchase.page.spec.ts` and `new-items.page.spec.ts` encode today’s thresholds. Change the fixtures to `decision` and assert the control (pre-selected vs must-pick) rather than the number.

### What not to build in the client

- A local alias table in `localStorage`. Coverage ticks are already stored there per pending id (`wb.coverage-choice`), and they do not affect quick add or other devices.
- Fuzzy matching in `PartyPickerComponent` beyond the server’s `q` search. The picker is a search box; ranking belongs in the matcher.
- Auto-rename of a shared party. `FactParties` already refuses that (line 28). Keep the refusal even after aliases exist: an alias points at the shared party, it does not change the shared name.

## Recommendations specific to plans

1. Extract the cancel / stop-renew / refund drawer from `plan.page.ts` (template around 404–478) into something like `PlanCancelSheetComponent`. `plan-cancel.spec.ts` already describes the API behavior the sheet must keep.
2. Extract the attach / read / review / fill block, parameterized by document kind (`warranty plan` vs `insurance_policy`) and by the pure fill function. `policy.page.ts` (778 lines) is the second caller.
3. Leave `plan-lines`, `plan-requests`, `plan-decision`, and the pure reading modules where they are.
4. When a plan document names a company the picker does not know, show `decision: 'ask'` with candidates instead of only stuffing the unknown string into `suggestedCompany`. That field is the plan-page version of “we did not match”.


</cursor_untrusted_data_1337>

---

<cursor_untrusted_data_1337 source="CallDynamicTool">

# Area 6 — Insurance, cards, parties, and admin

[Back to the overview](../CODE_REVIEW.md)

These screens are the other side of matching: policies and card benefits the user confirms, the party book those matches point at, and the operator tools that publish shared store and brand data.

## Insurance

| File | Lines | Role |
| --- | --- | --- |
| `policy.page.ts` | 778 | Add/edit one policy |
| `policy.page.spec.ts` | 489 | Document fill, links, scheduled items |
| `insurance.page.ts` | — | List |
| `policy-reading.ts` | — | Pure parse (`policyFill`, `splitLimit`, `kindFromText`) |
| `insurance.api.ts` | ~58 | CRUD, item links, documents. No `catchError` in the service |

`PolicyPageComponent` is the same shape as the plan page, one step smaller: inline template, document read, form, limits editor, item links, scheduled-item matching, file upload, end/delete, `ChangeTracker`. `readDocument` uses `DocumentReadingApi.readFiles('insurance_policy', ...)`. `ReadingReviewComponent` makes the user tick fields before `policyFill` merges them. Parsing stays in `policy-reading.ts` and has a spec. That part is healthy.

Insurer matching (`policy.page.ts` 482–497):

- New policy: `parties({ q: name, role: 'warrantyProvider', limit: 5 })`, then an exact case-insensitive name hit. No hit → a note telling the user to pick or add. Errors take the same note.
- Existing policy: if the document’s insurer name differs, the form is not changed. The note says the insurer was left alone (lines 469–477).

That is safer than `matchBrand`, because it requires an exact name and it will not swap an insurer on an update. It is still not a candidate list: five search hits are fetched and only the exact one is used. “State Farm” vs “State Farm Fire and Casualty” falls through to “pick it yourself” with no suggestion of the near party. Alias storage would turn that near miss into a candidate instead of a dead end (area 5).

Scheduled items: `scheduledPending` plus `ItemPickerComponent` (`data-testid="match-{i}"`), then `InsuranceApi.setItem`. The user does pick the item. Clearing a link goes through `ConfirmService` (around 690–707). This is a good small version of “here is what the document named, you bind it”.

Recommendation: after the plan document host exists (area 5), use it here. Do not add a second insurer-fuzzy in the page. Exact match can remain the auto path; anything else should be `decision: 'ask'` with the search results as candidates, not discarded.

## Cards

| File | Lines | Role |
| --- | --- | --- |
| `cards.page.ts` | 625 | List, catalog combobox, issuer picker |
| `cards.page.spec.ts` | 691 | Larger than the page |
| `card-detail.page.ts` | 579 | Identity, benefits review, term search |
| `card-detail.page.spec.ts` | 409 | Confirm, edit, search states |

There is no `cards.api.ts`. Card catalog and benefits live on `ReferenceApi` (`reference.api.ts` from about line 148).

Benefit confirmation is the most complete “user corrects a suggestion” flow in the app:

- Detail loads `proposedBenefits`, then falls back to the catalog.
- `startEditing` (around 487–510) merges proposed rows with what the user already confirmed: per-kind include, editable months and conditions, manual rows for kinds the catalog lacks.
- Save calls `confirmBenefits(id, items)` (`card-detail.page.ts` around 519–538, and on create from `cards.page.ts` around 608).
- A card whose benefits are not confirmed is called out on the list (`cards.page.ts` around 38–50) and on the item (`card-benefits-notice` in shared UI).
- Both card pages use `takeUntilDestroyed`. They are ahead of item detail on lifecycle.

`startSearch` / `reviewFound` let the user pull terms and confirm before save. That is ask-then-commit, which is what warranty auto-apply is not.

Gaps: the catalog combobox is implemented on both the list and the detail page. A shared card-product picker would remove that. Benefit confirmation stores “this card has this benefit”, not “the printed product name is an alias of catalog product P”. If the matcher confuses two Chase products, confirming benefits on the wrong card does not fix the next import. The alias write from area 5 should accept `field: 'cardProduct'` as well as store and brand.

The issuer half of admin is not built (`companies.page.ts` line 25, option disabled: “Credit cards (not built yet)”). Cardholders can confirm benefits; operators cannot yet publish issuer terms through the companies screen. The comment at lines 12–13 says issuers join the filter when their page exists. The disabled option is honest. Finding F8 is about the Review link, which is not disabled and not honest.

## Parties

| File | Lines | Spec? |
| --- | --- | --- |
| `parties.page.ts` | — | `parties.page.spec.ts` |
| `party-detail.page.ts` | 665 | **None** |
| `plans-they-sell.component.ts` | — | `plans-they-sell.spec.ts` |
| `party-picker.component.ts` | 222 | `party-picker.spec.ts` (331 lines) |

`PartiesPageComponent` is mounted twice:

- Settings → stores (`app.routes.ts` line 106), `admin: false`.
- `/admin` (`app.routes.ts` line 75), `data: { admin: true }`.

Create goes through `createParty`, and a 409 with `similar` is handled on the page (the picker does the same). That is the duplicate-name correction users have today.

`PartyDetailPageComponent` (665 lines) is an untested god-ish form: seller return policy, manufacturer warranty, card-benefit corrections, audit, saved info and notes when `admin()` is true. `correctSeller` (around line 595) sends days, restocking fee, conditions, `sourceUrl`, and a required note. The same shape exists for manufacturer and card corrections on `ReferenceApi`. This is how a wrong shared policy gets fixed, by an operator or by the owner of a personal party, and the API stores the note. It is not how a bad match gets an alias.

No spec for this page is the largest test hole outside the god pages that are already covered (finding F12). A first spec should post a seller correction and assert the note is required, and should assert `admin: true` hits `/api/admin/...` via `ReferenceApi.scope`. A wrong `admin` flag writes into the personal namespace silently.

`plans-they-sell.component.ts` lists plan types for a company (`PlanTypesApi`). It is a focused child with a spec. Party detail should grow more children like that (return form, warranty form) rather than more fields.

`PartyPickerComponent` is the shared control (policy, plan, cards, add purchase, item detail). Search is `toObservable` + `takeUntilDestroyed`. Minimum characters and `categoryId` are documented on the class; the spec is long enough that those edges are likely covered, and it is still the control a future candidate shortlist should not reinvent. Candidates are a different UI (a few buttons with reasons). Search remains for “none of these”.

## Admin

| Route | Component | State |
| --- | --- | --- |
| `/admin` | `PartiesPageComponent` with `admin: true` | Shared party list |
| `/admin/review` | `AdminPlaceholderPageComponent` | “Not built yet.” Story ids in route data (`app.routes.ts` 76–77) |
| `/admin/companies` | `AdminCompaniesPageComponent` | Stores, brands, plan types |
| `/admin/stores` | Redirect to companies | Old path kept |
| `/admin/feedback` | `AdminFeedbackPageComponent` | Queue. File comment: reply and attachments are not built |
| `/admin/parties/:id` | `PartyDetailPageComponent` | Operator edit |
| `/admin/businesses` | `AdminBusinessesPageComponent` | Free year, person limit |

`shell.component.ts` line 210 links **Review** to `/admin/review`. The placeholder (`admin-placeholder.page.ts` lines 10–12) renders the title from route data and the sentence “Not built yet.” Operators see a nav item that opens a stub. Same class of bug as Returns, smaller audience (finding F8). Remove the nav item until the queue exists. Leaving the route is fine so the story URL does not 404 into Home (`**` redirects to Home).

`AdminCompaniesPageComponent` switches on a query param among `AdminStoresPageComponent`, `AdminBrandsPageComponent`, and `AdminPlanTypesPageComponent` (332 lines in `plan-types.page.ts`,  `saved-info.component.ts` is also 332). Stores and brands: search, status `placeholder` | `confirmed`, suggest-from-web, confirm with `sourceUrl`. That workflow is “read the company’s page, check the sentence, confirm”. It is the operator path that makes `confidenceBand: 'verified'` possible. It does not collect end-user aliases. If aliases ship, operators will need a queue of them; that queue is closer to the unbuilt Review screen than to the companies confirm form. Do not bury alias approval inside brand confirm or the two jobs will tangle.

`saved-info.component.ts` shows stored HTML for a company and can suggest a warranty or return policy from it. It has a spec. The component is large because the suggest/confirm steps are inline; it is still one job.

`feedback-queue.page.ts` can filter and change status. Replies are explicitly not built. `businesses.page.ts` can extend a free year and raise a person cap; coverage is indirect through `business-account.spec.ts`, not a page spec.

`AdminPlaceholderPageComponent` is generic. Only Review uses it. If Review is unlinked, check for other `data: { title, summary, story }` routes before deleting the component. A search of `app.routes.ts` shows Review as the only `admin-placeholder` load.

## Recommendations

1. Unlink Review (F8). Keep the route.
2. Spec `party-detail` corrections and the `admin` prefix before changing party forms.
3. When the match contract grows candidates, feed insurer search misses and card-product misses into `MatchChoiceComponent` (area 5). Keep `confirmBenefits` as the “these terms are on my card” write; it is a different fact from “this statement name means this product”.
4. Split party detail’s seller and manufacturer forms into children modeled on `plans-they-sell`, so the missing spec has a small target.
5. Do not build card-issuer admin as a copy of `brands.page.ts` until the alias/exclusion API is settled. Otherwise issuer confirm and card-product alias will be two UIs for one matcher decision.


</cursor_untrusted_data_1337>

---

<cursor_untrusted_data_1337 source="CallDynamicTool">

# Area 7 — Settings, shared UI, styling, and tests

[Back to the overview](../CODE_REVIEW.md)

## Settings and account

`settings.components.ts` is the tab shell. Visible tabs depend on `AuthService` (`isOperator`, `isBusiness`, `isOwner`). Children (`app.routes.ts` 85–114):

| Path | Component | Spec |
| --- | --- | --- |
| `profile` | `SettingsProfileComponent` in `settings.components.ts` | `settings.spec.ts` |
| `notifications` | `notification-settings.component.ts` | via settings specs |
| `people` | `people-settings.component.ts` | `business-account.spec.ts` (`businessGuard`) |
| `tracking` | `tracking-settings.component.ts` | `tracking-settings.spec.ts` |
| `email` | `email-settings.component.ts` | thin |
| `appearance` | `theme-settings.component.ts` | `theme-settings.spec.ts` |
| `privacy` | `privacy-settings.component.ts` | `privacy-security.spec.ts` |
| `security` | `security-settings.component.ts` | `privacy-security.spec.ts`, operator guard |
| `stores`, `stores/:id` | parties pages reused | parties specs, not the settings mount |
| `billing` | `billing-settings.component.ts` | `billing-settings.spec.ts`, `ownerGuard` |
| `cards` | redirect to `/cards` | — |

Profile uses `ngModel`. Login and signup use `ReactiveFormsModule` and `Validators`. Notification settings save per toggle (`notification-settings.component.ts` around 67–79). The error display (`toProblem`, a `problem()` signal, `role="alert"`) is the consistent part. The form library is not. New settings work should use reactive forms or signals, but a wholesale rewrite of profile is not worth it (the overview says not to start here).

Billing (`billing-settings.component.ts` lines 74–78) shows Free, Monthly at `$5.99`, and Yearly at `$59.99`. The paid radios are disabled and the template appends “coming soon” (line 45). The comment says the prices are placeholders until Stripe prices replace them. Manage membership opens the Stripe portal through `RedirectService` only when a license exists. The disabled rows are labeled, so this is not the Returns problem, but the dollar amounts will be quoted by users. Prefer “Paid plans are not available yet” without a price until Stripe is the source.

`layout/account.page.ts` (62 lines) is a short account menu, specced. It is not the settings hub.

People, invitations, and ownership transfer are covered from `business-account.spec.ts` rather than a small spec per component. That file is 469 lines and also reaches into admin businesses. It works; it will be brittle if people-settings is split.

## Auth screens

`src/app/features/auth` is 19 files, about 1,029 production lines, 6 specs. The security-sensitive behavior lives in `AuthService` and the interceptor (area 1), not in the templates.

What the screens do well:

- Login has a 2FA step (`login.component.ts`).
- Signup does not create a usable session until the email link (`signup.component.ts` header).
- Google waits for a terms checkbox before using the credential (`google-button.component.ts`).
- `safeReturnUrl` is applied on the way back in.
- Mailbox linking tells the user to use an app password (`mailbox-link.component.ts`).

Specs exist for login, password reset, Google button, unsubscribe, and consent. There is no focused spec for `signup.component.ts`, `join.component.ts`, `choose-account.component.ts`, `verify-email.component.ts`, or `accept-ownership.component.ts`. Join and choose-account are the multi-account paths `accountChoiceGuard` depends on. A failure there dumps the user into the wrong account; they deserve a spec more than another theme test.

`google-button` hides itself if the provider script fails (`google-button.component.ts` around line 60). The user sees a normal login with no explanation. A one-line “Google sign-in did not load” is enough.

Signup’s terms links open in a new tab. `rel="noopener"` on `target="_blank"` is the usual hardening; the router links here are in-app legal pages, so the risk is low.

## The rest of the feature folders

| Folder | Production size | Note |
| --- | --- | --- |
| `home` | ~687 | Dashboard, orientation, welcome, quick photo, recovered total. Specs on the main pieces. Uses `SetupStateService` |
| `notifications` | 444 in the page | Full page list. Spec is 465 lines |
| `feedback` | ~149 | Reactive form. Spec exists. Admin reply is a different page and is unfinished |
| `legal` | ~206 | Lazy public pages. Spec exists. Copy still depends on `set-env.mjs` / `legal.ts` placeholders |
| `share` | ~150 | Landing for the share target. Spec exists |
| `todos` | 62 | Wrapper around `TodoListComponent`, which has a spec. The page does not |
| `vehicles` | 253 in `add-vehicle.page.ts` | **No spec** |
| `install` | ~52 | `beforeinstallprompt`. Spec exists |
| `returns` | 81 | Mock. See area 3 |

Home is a composition of small components (`quick-photo`, `recovered-total`, `orientation`). That is the size the item and plan pages should have been. Nothing structural to change except keeping setup CTAs in agreement with `SetupNoticesService` (the bell’s standing notices). Both read the same service, which is correct.

## Shared UI

`src/app/shared/ui` is 51 files, about 2,591 production lines, 16 specs. Templates are inline. Almost nothing uses a `styles:` array (`home.component.ts` is one of a handful).

| Component | Lines | Used widely? | Spec |
| --- | --- | --- | --- |
| `party-picker` | 222 | Yes | Yes |
| `mailbox-link` | 225 | Orientation, email settings | Yes |
| `document-facts-review` | 162 | Add purchase, item detail | Yes |
| `reading-review` | ~108 | Plan, policy | Yes |
| `plan-ask` | 175 | Items, plans | Yes |
| `todo-list` | 114 | Todos, items | Yes |
| `item-picker` | 120 | Policy, new items | No |
| `item-multiselect` | 106 | Plans | No |
| `file-attach` | 101 | Plan, policy, items | Light (`file-attach.spec.ts`, 72 lines) |
| `confirm.service` + modal hosted by the shell | — | Deletes and guards | Yes |
| `toast.service` | — | Widespread, ngx-sonner | No |
| `facet-filter`, `items-header`, date fields, badges | small | Lists and forms | Several specs |

`company-page`, `plan-receipt-edit`, `plan-receipt-facts`, and `card-benefits-notice` live in `shared/ui` but have one feature each. That is acceptable. Moving them next to the feature would only matter if shared becomes a junk drawer; it is not there yet.

The two review components (`document-facts-review`, `reading-review`) should stay separate until a match decision type exists. They answer different questions (field conflicts vs extracted clauses). A third component, for ranked candidates, should be added beside them rather than overloading either (area 5).

`inline-add.component.ts` plus `quick-add.spec.ts` is the parties create row. `confirm.service.ts` is the replacement for `window.confirm`, and the README forbids browser dialogs. Grep-level use is consistent; do not add `alert` or `confirm` in new work.

Duplication to actually remove:

- PayPal funding helpers on item detail and add purchase (area 4).
- Return-policy editors on party detail and admin stores, if those forms are still line-for-line. They should become one child before either grows an alias queue.
- Card catalog combobox on the two card pages (area 6).

## Styling and accessibility

`src/styles.css` is 430 lines. Tailwind v4 is imported on line 1, then ng-select’s default theme, then design tokens for teal, indigo, and berry in light and dark. The header comment (lines 4–10) says components must not use raw colors. Practice matches that: muted text is `style="color: var(--color-muted)"` or a utility, not a hex. The inline style is noisy. A `.text-muted` utility (if not already in the Tailwind theme) would shrink templates without a visual change. Not a defect.

`theme-contrast.spec.ts` checks 4.5:1 for text on surface and on brand, for every theme and mode. That is unusual and worth keeping. Any new token pair should be added there.

Accessibility that is in good shape: form labels on auth, `sr-only` names on icon buttons, `role="alert"` / `role="status"`, combobox `aria-expanded` on cards, dialog semantics on reauth and confirm, 44px targets in the shell comments.

Gaps, all low severity next to the matching issues:

- Shell account menu opens on hover and does not implement a menu keyboard pattern (area 1).
- Notification panel has no focus trap.
- Item detail marks the parts/plan asks as `role="alertdialog"` without `aria-modal` or a focus move (area 3).
- No i18n. A search for `$localize` and ngx-translate finds nothing. `angular.json` still has an `extract-i18n` target. All copy is English, including the certainty words. A second language is a content project, not a refactor; do it after F1 stops changing those strings.

Production bundle budgets are 600 kB warning and 650 kB error (`angular.json`). `npm run size` builds stats and an esbuild visualizer report. No checked-in stats file, so this review did not measure the current bundle. Lazy routes are the mitigation. The initial bundle still includes the shell, auth, and the shared style/theme stack. If the budget starts failing, party-picker’s ng-select is the first dependency to check, not the feature pages (they are lazy).

## Tests

| | Count |
| --- | --- |
| Spec files under `src` | 135 |
| Spec lines | ~21,600 |
| Production lines under `src` | ~28,900 |
| E2E project | none |
| Coverage thresholds in `angular.json` | none |
| Runner | Karma, ChromeHeadless, Jasmine (`package.json` script `test`) |

The suite is a unit-and-component suite, and it is serious about the risky pages: item detail split across two 1,000-line specs, add purchase, new items, plan page, cards, interceptor, upload sync, theme contrast. That is why the matching thresholds are safe to change only with the fixtures.

Shape problems:

- **Page-sized specs mirror page-sized components.** Extracting a drawer without a new small spec just moves 200 lines of TestBed. The overview’s roadmap extracts helpers first so the new spec is a function test (`certainty.spec.ts` is the model, 11 lines of production).
- **Untested production:** `party-detail.page.ts` (665), `add-vehicle.page.ts` (253), most `*.api.ts` except inbox, `toast.service.ts`, `SetupStateService` except through home specs.
- **Well tested platform:** auth refresh, interceptor 401 races, reauth, guards that are not `authGuard`/`guestGuard`, upload account isolation.
- **No end-to-end check** that quick add and the full form attach the same coverage keys for one pending item. That is the F1 bug, and no unit spec can see it while each page has its own fixture.

A coverage threshold today would pass on the files that are already tested and would not force `party-detail` to be tested if the gate is global and the big specs dominate the percentage. Add HTTP specs for `ReferenceApi` and `PurchaseApi.dismiss` / `proposals` first, then a threshold on `src/app/core` only.

`src/app/core/testing.ts` (102 lines) is the shared TestBed helper. New specs should use it rather than copying provider lists. Several settings specs still build their own `provideHttpClient()` stacks; that is fine and slightly noisy.

## Recommendations

1. Do not start a settings rewrite. Fix billing copy if the placeholder prices are visible in a build testers use.
2. Add specs for join, choose-account, and verify-email before changing `accountChoiceGuard`.
3. Add the candidate component under `shared/ui` when the API sends candidates. Do not fold it into `reading-review`.
4. Spec `party-detail` and `add-vehicle` before their next feature change. Vehicle add is on the primary add flow (`/add/vehicle`).
5. Leave i18n, ng-select, and a global coverage gate until F1–F5 are done. Contrast tests and the token file should stay as they are.
6. Toast service: one spec that the service calls the sonner API is optional. Failures there are obvious in the UI.


</cursor_untrusted_data_1337>

---

