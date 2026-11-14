# UAT retest: push 69 (UI-only), changing one item re-checks only that item

- **Build:** the UI was redeployed at 11:00 PM ET Nov 11 2026. The API is unchanged at `7051bb3`.
- **Run:** 11:31 to 11:35 PM ET, as Alice. The app clock was not moved and is at offset 0.
- **Scope:** CHANGES-push-69-one-items-lookup-only.md, which fixes the push 68 Medium.
- **Counting calls:** I counted `POST /api/pending-items/coverage-preview` calls in Chrome DevTools Network. Each call shows twice, as the page's request and a service-worker copy, so each pair counts as one call.

## Summary: 4 Pass, 0 Fail. The push 68 Medium is fixed.

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Changing item 2 re-checks only item 2 | **Pass** | Store Best Buy; item 1 "P69 DeWalt drill" (Power tools, DeWalt); item 2 "P69 Samsung fridge" (Major appliances, Samsung). With 3G throttling on, I changed only item 2's category to Refrigerators. Network showed **1** call (200, about 2.0 s), where push 68 made 2. Item 1's list didn't change, and item 2 reloaded with Samsung warranty 1 year and Best Buy return policy 15 days. I didn't see "Checking what applies…" on item 2 here; it was probably too brief to catch. It did show on Try again in check 2. Shot `p69-01-one-call.png`. |
| 2 | A failed lookup affects only that item | **Pass** | With the request blocked, I changed item 2's category again. Network showed 1 blocked call. Only item 2 showed "We could not check the coverage just now. Try again", and item 1 kept its list. After I unblocked, Try again on item 2 showed "Checking what applies…" on item 2 only and reloaded its list with 1 call (200). Shots `p69-02-one-failed.png` and `p69-02b-retry.png`. |
| 3 | Store and date changes re-check every item | **Pass** | **Store:** changing it to Home Depot made 2 calls. Item 1 showed "Home Depot return policy · 90 days · Confirmed" and DeWalt warranty 3 years. Item 2 showed "Home Depot return policy: major appliances · 2 days · Confirmed", Samsung warranty 1 year, and "Home Depot return policy: general · 90 days · Likely" (unticked). **Date:** changing it to 2026-11-01 made 2 calls. Item 2 added "This return window ended 2026-11-03, so it cannot be added.", and "Counted from today until you give the date." went away. **Card:** not checked, because Alice has no cards and the only option is "Not sure / cash". Shots `p69-03-store-change.png` and `p69-03b-date-change.png`. |
| 4 | Removing item 1 leaves item 2's own list | **Pass** | Item 2 kept its Samsung and Home Depot list, with no new calls. Shot `p69-04-after-remove.png`. |

## Notes
- Typing "Home Depot" in the store field offered `Add "Home Depot"`, not the known shared store. The coverage lines then still named the Home Depot policies. This was not in scope, but CC may want to check how the store picker matches names.
- The app showed a "new version is ready" banner on the add page, and the run didn't click Reload. The behavior seen is the push 69 behavior (one call per item change, where push 68 made two), so the new UI code was running.
- The only console entry was DevTools' own warning about the request I blocked. There were no app errors.

## Cleanup
Nothing was saved. I left with Cancel and then "Leave without saving", and signed out. Throttling and request blocking are off again.

## Fixtures
None.
