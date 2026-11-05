# UAT retest: push 17 Scenario 55 redo (correct door) + Bob/Carol recreate
Build: API still c6dc314; UI Last-Modified Thu, 05 Nov 2026 10:50:29 UTC (push 17 Opening fix). Mode: Full-only. Tested ~5:56–6:00 AM ET Nov 5.
Notes: CHANGES-push-17-back-button-and-scenario-55-door-2026-11-05.md. Alice scenario-reset by DB Stager just before the run.

## Headline
Bob and Carol are recreated and confirmed. The Scenario 55 redo **could not grade steps 2, 3, 5, 9, 13, 15, 16** because neither correct door offered a manufacturer's warranty for `standard-lifetime-limited-reel.pdf`. That matches Steve's "possible real bug" case. Add-on protection was not used.

## Bob and Carol
| Account | Result | Notes |
|---|---|---|
| Bob (tester2) | Pass | Sign-up 5:56:02 AM ET; confirm link → /orientation "Welcome to WarrantyCat, Bob" |
| Carol (tester3) | Pass | Sign-up 5:56:29 AM ET; confirm link → /orientation "Welcome to WarrantyCat, Carol" |

## Door check (required before redo)
| Door | Result | Notes |
|---|---|---|
| 1. Add a purchase + PDF | **Fail (reader)** | Attached as "Warranty or terms (PDF)". Brand auto-filled Penn. **No "Manufacturer's warranty found" box.** Catalog offered "Penn warranty, Manufacturer, 1 year, Confirmed" (ticked) plus other Unconfirmed models. After save, item shows 1-year catalog warranty to Jun 1, 2027. PDF filed under Receipts and files as "Receipt". Lifetime wording never extracted |
| 2. Item paperwork re-upload | **Fail (reader)** | "Read it" on Receipt: "Warranty document… Start a plan from it… Nothing to add: what you have already matches the document." Re-upload filed as "Terms": "Warranty document. The document does not give one clear length or end date. Add the coverage yourself." Still no maker's warranty offer |
| PDF content (pdftotext) | — | Clearly states lifetime of the product, original purchaser, not transferable, proof of purchase required |

## Scenario 55 steps (redo target)
| # | Result | Notes |
|---|---|---|
| 2 | Not checked | No lifetime suggestion to read |
| 3 | Not checked | No lifetime coverage / "Lifetime, can end" to grade |
| 5 | Not checked | No lifetime proof-asked line |
| 9 | Not checked | No lifetime coverage to End |
| 13 | Not checked | Not reached (tub path not run; blocked upstream) |
| 15 | Not checked | Would not exercise lifetime coverage |
| 16 | Not checked | Would not exercise lifetime export columns |

Item left on Alice: `/items/01a1ab5c-e0da-7ec0-9886-fa9f3145eb0b` (1-year catalog Penn + Receipt + Terms copies of the PDF). Delete before a later redo.

## Not run this pass
- Push 17 Opening… Back-button fix (Alice has billing status none after reset; Manage membership disabled).
- Scenario 55 steps outside the redo list.

## Needs CC
- Reader does not extract the lifetime term from `standard-lifetime-limited-reel.pdf` on Add a purchase or on item paperwork; classifies as warranty but says no clear length/end date and never shows "Manufacturer's warranty found."

**Totals:** Bob/Carol Pass; door 1 and 2 Fail (reader); 7 redo steps Not checked.
