# UAT retest: push 22 Read it optional + Missed label
Build: API `bb416b8` (started ~3:23 PM ET Nov 5, verified). UI Last-Modified ~3:22 PM ET Nov 5. Mode: Full-only. Browser run ~4:05–4:10 PM ET Nov 5.
Notes: `CHANGES-push-22-read-it-optional-and-missed-label-2026-11-05.md`. Follows Push 21 (16b Fail, 19 Partial). Alice (vault2448781 "QA Test1") reset by DB Stager at clock offset 0. "Welcome QA" greeting is normal, not a defect. Scenario 61 (vehicles) excluded — vehicles build not deployed.

## Headline
**16b Partial** — Read it now adds the optional coverage + Register to-do (fix works), but base is re-offered and the to-do appears only after reload. **19 Pass** — closed to-do labelled **Missed** with the missed sentence.

## Retest rows
| # | Result | Notes |
|---|---|---|
| 16b. Base-only add → Read it | **Partial** | Add a purchase with `edge-registration-required.pdf`, base 3 months only (optional unticked). Item [01a1ad89-9ec0-7329-a726-06e1d56df8db](https://stuffit-ui.onrender.com/items/01a1ad89-9ec0-7329-a726-06e1d56df8db), bought Nov 5. Read it: "Nothing to update" toast, then "Add this warranty?" choice. **Both base and optional re-offered, unticked** (notes expect base NOT re-offered). Ticked optional → Add: exactly two coverages — base Nov 5, 2026–Feb 5, 2027; optional 3 years "if register by Dec 5", Not counted yet. **Register to-do appeared only after reload** (not immediately). Second Read it re-offers both rows again; chose Not now → still 2 coverages, 1 to-do. *Limit:* re-adding the existing optional was **not attempted**, so no-double is verified only for reread without Add. Shots: choice `/cursor/stores/store-5417ec58-ea75-4baf-b2e2-a6e69ffc43ca/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/563ce538ac3de572e56c7c79d52ca70c92f06078db685cfe88fcd5860d954268.png`; after Add `/cursor/stores/store-5417ec58-ea75-4baf-b2e2-a6e69ffc43ca/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/e168c794c72d349909435fe0a3feafa8463a9256190224a7b11567a5f1b5115f.png`; after reread `/cursor/stores/store-5417ec58-ea75-4baf-b2e2-a6e69ffc43ca/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/aae3e3c5f5567cfa0e132a5827a6bb3d3017e7e765f4427bc60fe19e4b0bb4e4.png`. |
| 19. Past deadline, never registered | **Pass** | Requested Nov 25 (offset 20), but deadline is Dec 5 (bought today), so advanced to Dec 6 (offset 31). Item reload: "Not earned: the registration window ended Dec 5, 2026". /todos open: "Nothing to do right now". Closed "Register TB-350" labelled **Missed** (not Not applicable): "The registration window ended Dec 5, 2026, so this was closed as missed. If you did register in time, press I registered on the item to say so." Optional 15s Undo toast **Not checked** (skipped). Shots: not earned `/cursor/stores/store-5417ec58-ea75-4baf-b2e2-a6e69ffc43ca/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/407aaa87762bca946c416e10610f296d4a09ee2523861f7590bf8cd42606361f.png`; empty to-dos `/cursor/stores/store-5417ec58-ea75-4baf-b2e2-a6e69ffc43ca/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/a821c92346e0b4a10a6dbd8f3e390349a8bd0ac0d4a2d2fc7ff042928f08397f.png`; Missed `/cursor/stores/store-5417ec58-ea75-4baf-b2e2-a6e69ffc43ca/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/c73978a4f48e8380182e759514a5e88cf674889fc9b928b8d1d021a53c5bcb16.png`. |

## Open issues for dev
1. Read it on base-only item re-offers the base row (expected only optional).
2. Register to-do not shown until page reload after Read it Add.

## State left
Alice: item `01a1ad89-…` with base + optional (Not earned). Global clock **restored to offset 0**, independently GET-verified by DB Stager on bb416b8 at 4:11 PM ET; Alice untouched. Build watch paused until filing completes.

**Totals:** 19 Pass, 16b Partial.
