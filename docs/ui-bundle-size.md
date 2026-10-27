# UI bundle size: long-term plan

Decided 2026-10-01 (Steve): the app will keep growing, so the first download must not grow with it.

## Where we are
- Initial download (production build): about 435 kB raw, 117 kB over the wire (415 kB before the installable-app and sign-in changes in M5; that work added about 20 kB: service worker support, banners, the re-authentication prompt, route guards). That is Angular itself (core, router, forms, http) plus the shell, sign-in screens and Home.
- Every other screen is its own on-demand chunk (`loadComponent` in `app.routes.ts`). Adding a screen adds nothing to the first download.

## The rules
1. **Every screen inside the signed-in shell is lazy.** Only the shell and Home are eager. `src/app/app.routes.spec.ts` fails the unit tests if someone adds an eager screen.
2. **Signed-out screens stay small and eager** (login, signup, reset): they are the first thing a new visitor sees.
3. **A heavy library never goes in the initial bundle.** Charts, PDF viewers, rich text, maps, date pickers, anything over about 30 kB: import it inside the one lazy screen that needs it, or with a dynamic `import()` when the user asks for it. Prefer a plain HTML/CSS solution first.
4. **Use `@defer`** for large parts of a screen that are below the fold or behind a tab.
5. **No barrel files** that pull a whole feature into a shared import. Shared code (`core/`, `shared/ui/`) stays small and free of feature code.
6. **Icons are inline SVG paths**, not an icon font or library.
7. **Fonts are the system font stack.** No web fonts.
8. When a feature grows large (billing, admin console, a future reports area), give it its own route file (`loadChildren`) so its screens, services and models load together, only when visited.

## Budgets (the build fails, not just warns)
`angular.json`, production configuration:
- **Initial bundle:** warn at 450 kB, **error at 550 kB** (raw). The current 435 kB leaves only about 15 kB of headroom before the warning, so a warning is the signal to act, not the error.
- **Component styles:** warn at 4 kB, error at 8 kB.
- When a warning appears, fix it before adding more. Raising a budget needs a written reason in the commit.

## How to see what is growing
- `npm run size` builds with stats and writes `dist/stuffit-ui/bundle-report.html`, a map of what is in each chunk.
- Check it when the initial total moves by more than about 10 kB, and before each release.
- Watch two numbers over time: initial total (raw) and the largest lazy chunk.

## What would make us act
- Initial total passes 450 kB: find out why with the report; move the cause behind a lazy route or `@defer`.
- A lazy chunk passes about 250 kB: split the screen, or defer its heavy part.
- First-load time on a mid-range phone over 4G passes about 3 seconds: audit before adding anything else.

## Later, when it matters
- Preload lazy routes the user is likely to visit next (`withPreloading`), once there are enough screens that waiting for a chunk is noticeable.
- A service worker for caching (comes with the installable-app story, S9.1.4).
- Server compression (brotli) on the host; check it when we deploy to Render.
