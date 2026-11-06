# UAT retest: push 21 missed registration to-do / late banner / Undo
Build: API `1617db9` (started 2026-11-05T19:29:31Z / ~2:29 PM ET Staging). UI Last-Modified Thu, 05 Nov 2026 19:28:57 UTC (~2:28 PM ET). Mode: Full-only. Tested ~2:32–2:39 PM ET Nov 5.
Notes: `CHANGES-push-21-missed-registration-todo-2026-11-05.md`. Follows Push 20 S54 Part B Partials (to-do stayed Overdue; late refuse generic validation; 16b Not checked). Alice scenario-reset by DB Stager; clock offset 0 then +20 days for 19/19b then restored.

## Headline
**Mixed.** Plain late-date banner **Pass**. Coverage Undo after I registered **Pass** (toast Undo not caught). Missed to-do **Partial** — drops out of open list but closed label is **Not applicable**, not the missed text. Step **16b Fail** — Read it says nothing to add.

## Retest rows
| # | Result | Notes |
|---|---|---|
| 16b. Unticked optional → Read it | **Fail** | Saved base-only item `01a1ad34-112c-7cab-8c5f-16d7b7a13953`. Read it is under Edit → Receipts and files. After Read it: "This looks like a warranty or protection plan. Start a plan from it… **Nothing to add: what you have already matches the document.**" Optional coverage and Register to-do did **not** appear. Shots: choice `…/983521e0…54c6.png`; after Read it `…/4ffa0446…8710.png`. |
| 19. Clock → 2026-11-25, never registered | **Partial** | Item used: `01a1ad35-49b2-7b83-a781-d7453df73124` (optional ticked at add — fallback after 16b Fail). Coverage **Pass**: "Not earned: the registration window ended Nov 19, 2026"; 90 days still Until Jan 20, 2027. Open to-dos: "Nothing to do right now" **Pass** (not Overdue). Closed entry labeled **"Not applicable"**, not "The registration window ended … closed as missed…" — **Fail as written**. Shots: coverage/final `…/7086effe…e851.png`; to-dos `…/c955a8b3…4676.png`. |
| 19b. Late then early I registered | **Pass** | Late 2026-11-22: plain banner **"That day is after the deadline (Nov 19, 2026). Give the day you registered, or leave this coverage as not earned."** Coverage stayed Not earned. Early 2026-11-10 + confirm: "3 years, active: you registered on Nov 10, 2026. You confirmed it was in time." Shot: late banner `…/9a7a082a…4335.png`. |
| 18. Undo after I registered | **Pass** (coverage Undo) | Toast: "Counted. The longer coverage now replaces the shorter one." Toast Undo was already gone when clicked (could not confirm 15s stay). Coverage's own Undo restored prior Not earned + Jan 20, 2027. Shot: toast `…/a4e23cfd…2a33.png`. |

## Not changed / do not report as new
- Reopening a done registration to-do does not undo I registered — left as designed.
- Shared policies with registration rule; add optional by hand; yearly check-in / etc. — not built.

## State left
Alice: base-only leftover `01a1ad34-…` + optional item `01a1ad35-…` (post-Undo Not earned). Clock restored to offset 0 after the run. Build watch resumed.

**Totals:** 19b Pass, 18 Pass (coverage Undo), 19 Partial, 16b Fail.
