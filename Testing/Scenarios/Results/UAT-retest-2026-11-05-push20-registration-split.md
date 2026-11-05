# UAT retest: push 20 registration split (Scenario 54 Part B)
Build: API `1a76827` (process restarted ~1:29 PM ET after Anthropic key reconfigure; earlier startedAt 9:43 AM ET same commit). UI Last-Modified Thu, 05 Nov 2026 14:42:32 UTC. Mode: Full-only. Retest ~1:35–1:54 PM ET Nov 5 after Anthropic env fix.
Notes: `CHANGES-push-20-registration-split-2026-11-05.md` (S3.1.13 / ConditionalCoverage). Alice scenario-reset by DB Stager before the successful run (0 items; clock offset 0). Signed in as Q1 / Welcome QA via vault_2448781.

## Headline
**Mostly Pass.** Registration split UI works after the Anthropic key fix. Unticked optional coverage is not created (matches plan skip-to-16b). Missed-deadline coverage wording Pass; to-do stayed Overdue instead of closed as missed. Late register refuse works but uses a generic validation banner. Plain lifetime PDF: one coverage, no split (19c Pass).

## Earlier blocker (resolved)
First attempts today failed with reader "could not be read just now" — root cause was Anthropic **invalid x-api-key** on StuffIt_API. Steve reconfigured Anthropic; fresh upload then succeeded. Do not treat the leftover Add-form card from before the fix as a new Fail.

## Retest rows
| # | Result | Notes |
|---|---|---|
| 14. Add + `edge-registration-required.pdf` | **Pass** | Fresh `/add/new`. Item UAT Trailblaze TB-350, bought 2026-10-20, Outdoor gear, brand Trailblaze (added as new; kept document brand TRAILBLAZE Outdoor Gear). Panel "Manufacturer's warranty found": base "TRAILBLAZE Outdoor Gear: 3 months, counted from the purchase date" ticked ("Add this warranty…"); optional "Optional: 3 years if you register within 30 days of purchase" unticked; quote “Register your product within 30 days of purchase”; note "Not counted until you tell us… Not added unless you tick it…". End date on item: Jan 20, 2027. Shot: `…/ee37644a09544f7c3dc46cc9c95ffed15efb77886daee638414d87d2bb573856.png`. |
| 15. Accept base only | **Pass (unticked path)** | Only 90 days created ("Covered 1 policy", Oct 20, 2026–Jan 20, 2027). No 3-year "Not counted yet" row, no Register to-do — matches panel "Not added unless you tick it" and plan "skip to 16b". **16b Not checked** this run (Add coverage / Read it path exists). Shot: `…/b45817789e5d018b8e0e9ac788a96f8730625235998eafbcaa6eee54b00e5c5d.png`. |
| 16. Retick optional | **Pass** | Deleted + re-added with 3-year ticked. "2 policies"; 90 days to Jan 20, 2027; other "3 years if you register by Nov 19, 2026. Not counted yet." (Oct 20, 2026–Oct 20, 2029). One to-do: "Register UAT Trailblaze TB-350 by Nov 19, 2026 to extend the warranty to 3 years" (Due in 11 days). Header Until Jan 20, 2027. Shot: `…/2515d5cd7d692d6d871e8369f25b6b38c744c3c9f30fd4c6d85dc0bdeb590569.png`. |
| 17. I registered 2026-11-01 | **Pass** | Toast "Counted. The longer coverage now replaces the shorter one." + Undo. After reload: "3 years, active: you registered on Nov 1, 2026."; header Until Oct 20, 2029; 90-day "Replaced by the 3 years registered coverage since Nov 1, 2026…"; to-do Done. UI note: list still showed old "Not counted yet" until reload. Shot: `…/009ae720ebe81911dda4ade9faf2437ef9d4eb0d50ea86801ec5b2f54fa16bb3.png`. |
| 18. Undo | **Pass** (needed recreate) | Undo toast disappears in a few seconds — first attempt missed it; Reopen on Done to-do left coverage still registered ("You have already said you did this."). Recreated item, registered, Undo within toast window → 90 days active again; 3-year Not counted yet; Register to-do back. Final item left: https://stuffit-ui.onrender.com/items/01a1ad06-7bd5-78da-ae08-b0e18e4c1fef. Undo toast shot: `…/fd6d00709a51b85e451ca8019820bf380ea439f87f0050e8a85bee8d120cd763.png`. |
| 19. Clock → 2026-11-25 (never registered) | **Partial** | DB Stager option A: global offset +20 days. Coverage: "Not earned: the registration window ended Nov 19, 2026." **Pass**. 90 days still counting (Until Jan 20, 2027) **Pass**. To-do **Fail as written**: stayed open with "Overdue since Nov 16, 2026" (I registered / Dismiss / Not applicable); not closed as missed. Shots: coverage `…/e29f1959…a5ac.png`; to-do `…/8d9566ef…405f.png`. |
| 19b. Late then early register | **Partial** | Late **2026-11-22**: coverage form shows helper + "I registered in time" checkbox; refused with banner "One or more validation errors occurred." (not a plain "after the deadline" message); coverage stayed Not earned. To-do I registered path: same generic banner for both 11/22 and 11/10, did not activate. Early **2026-11-10** from coverage: confirm checkbox + activate **Pass** — "3 years, active: you registered on Nov 10, 2026. You confirmed it was in time."; Until Oct 20, 2029; Undo briefly; to-do Done (not missed). Shots: form `…/d8f5de81…ee02.png`; late refuse `…/fe28a9e1…22c3.png`; activated `…/a9952038…c139.png`. |
| 19c. Plain longer term, no condition | **Pass** | `standard-lifetime-limited-reel.pdf` on Add: "Manufacturer's warranty found" — "PENN Fishing Tackle: Lifetime, with no end date, counted from the purchase date." Saved one policy only; no optional/registration line; no Register to-do. Item https://stuffit-ui.onrender.com/items/01a1ad0f-8bc9-7015-a89a-74d74002db0e (Fishing reels, Penn / BTLIII4000, bought 2026-10-01). Reader prompt v5: lifetime offer wording matches Push 19 success. Shots: `…/b816f41d…bbdd.png`, `…/badf3c1b…9ea2.png`, `…/db2a4968…45dd6.png`. |

## Notes / polish
- Unticked optional: not created (by design per panel + CHANGES "No to-do for an unticked optional coverage").
- Undo must be caught while toast is visible; Reopen on Done to-do does not undo registration.
- After "I registered", coverage list may need reload to drop "Not counted yet".
- Missed deadline: coverage "Not earned" OK; to-do should close as missed (kept) — still Overdue.
- Late date refuse: works, but message should be plain (not generic validation).

## Do not report as new (per notes)
- Shared (community) policies with a registration rule — not built.
- Adding optional coverage by hand — not built (Read it only); 16b not run.
- Old "Not sure" — removed by design.
- Lifetime Active / yearly check-in / etc. — decided, do not report.

## State left
Alice: Trailblaze item `01a1ad06-…` (registered Nov 10 / 3-year active after 19b) + Penn lifetime item `01a1ad0f-…`. Clock restored to offset 0. Build watch resumed.

**Totals:** 14 Pass, 15 Pass (unticked path), 16 Pass, 17 Pass, 18 Pass, 19 Partial, 19b Partial, 19c Pass. 16b Not checked.
