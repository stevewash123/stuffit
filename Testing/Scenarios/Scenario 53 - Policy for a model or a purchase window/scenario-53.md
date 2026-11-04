# Scenario 53: A policy that applies only to certain models, or to purchases in a date window

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. The reference data is loaded: `samsung.json` (general policy plus the 2-year addendum for 65 listed models bought 2022-10-01 to 2023-09-30) and `penn.json` (Battle IV and Fierce lines). The 2-year addendum is the shared policy; no document is needed in Parts A and B. Clock offset 0 (2026-11-04).
**Time:** 50 min
**Built per:** S3.2.8 phase 1 (`ProductNodeMatcher`, `ModelNumbers.Normalize`, purchase window `PurchasedFrom/To`, listed `ModelNumbers`, nearest policy wins per component). Penn tree seeded from `penn.json`.
**Why this plan:** Scenarios 15 to 17 prove the app can choose between a maker's *lines*. This proves the harder case: the same maker, the same product, a different answer because of the **exact model number** or the **purchase date**. A wrong answer here shows a person 24 months when they have 12, or the reverse.

**Answer key**

| Item | Model | Bought | Whole product | Why |
|---|---|---|---|---|
| A | RF23A967535/AA | 2023-03-15 | 24 months, ends **2025-03-15** (already ended) | Listed model, inside the window |
| B | RF23A967535/AA | 2023-10-05 | 12 months, ends **2024-10-05** | Same model, 5 days after the window closed |
| C1 | RF23A967535/AA | 2022-10-01 | 24 months, ends 2024-10-01 | First day of the window (inclusive) |
| C2 | RF23A967535/AA | 2023-09-30 | 24 months, ends 2025-09-30 | Last day of the window (inclusive) |
| C3 | RF23A967535/AA | 2022-09-30 | 12 months, ends 2023-09-30 | One day before the window |
| D | RF28T5001SR | 2023-03-15 | 12 months, ends 2024-03-15 | Not a listed model, inside the window |
| E | RF23A967535/AC | 2023-03-15 | 12 months | `/AC` is not listed for this base number (only `RF23A9675AP/AC` is) |

For A, C1 and C2 the **other terms are unchanged**: ice maker 24 months, sealed system 60, digital inverter compressor parts 120 / labor 60, counted from the purchase date.

**Part A: model and window**

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Add by hand: "UAT Bespoke A", brand Samsung, category refrigerator, model RF23A967535/AA, bought 2023-03-15, $2,400 | Maker warranty proposed: whole product **24 months** (the addendum), ice maker, sealed system and compressor lines as in the key. The source line says the addendum and its window, not just "Samsung" |
| 2 | Test1 | Read the item page | Whole product shown ended on 2025-03-15; sealed system (to 2028-03-15) and compressor (parts to 2033-03-15, labor to 2028-03-15) still active. "All other terms unchanged" is true on screen: the three component end dates match the general policy |
| 3 | Test1 | Add "UAT Bespoke B", same model, bought 2023-10-05 | Whole product **12 months**; the addendum is **not** applied and not mentioned as applying. Components as in step 1 counted from 2023-10-05 |
| 4 | Test1 | Add C1, C2, C3 (dates in the key, same model) | C1 and C2: 24 months. C3: 12 months. The window is inclusive at both ends; record any off-by-one |
| 5 | Test1 | Edit B's purchase date from 2023-10-05 to 2023-09-01 | Whole product changes to 24 months and the source line changes with it; no second coverage is left behind |
| 6 | Test1 | Edit it back to 2023-10-05 | Back to 12 months; no stale 24-month line |
| 7 | Test1 | Add D: model RF28T5001SR, bought 2023-03-15 | 12 months; the addendum is not offered. (Date in window but model not listed) |
| 8 | Test1 | Add E: model RF23A967535/AC, bought 2023-03-15 | 12 months. A regional or colour suffix that is not listed is **not** guessed to be the listed one. Record whether the app says the model was not recognised |
| 9 | Test1 | Add A again but type the model as `rf23a967535 / aa` (lower case, spaces) | Matches the same model (case and spaces are ignored): 24 months. Record the result of `RF23A967535-AA` too (dash instead of slash) |
| 10 | Test1 | Add an item with brand LG and model RF23A967535/AA | The app puts the contradiction to the person ("this model number belongs to Samsung"), and does not apply either brand's policy silently |
| 11 | Test1 | Add an item with brand Samsung and **no model** (name "Samsung French door fridge"), bought 2023-03-15 | Brand policy only (12 months). The addendum is not applied from the name alone |
| 12 | Test2 | Add model RF23A967535/AA bought 2023-03-15 | Same answer as step 1 (shared data), and nothing of Test1's items is visible |

**Part B: product tree (Penn lines and sizes)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 13 | Test1 | Add "Penn Battle IV 4000 reel", brand Penn, model BTLIV4000, bought 2026-08-01 | Matched by exact model number to the Battle IV > 4000 node. Penn's policy: 12 months from purchase, ends **2027-08-01**; source is Penn's own warranty page |
| 14 | Test1 | Add the same with model `BTLIV4000HS` | Matches the separate 4000HS node, not 4000. Same 12 months |
| 15 | Test1 | Add "Penn Fierce IV reel" with no size or model | Stops at the Fierce IV line (no sizes seeded). It is not forced to a size. Brand policy (12 months) applies. Record if it asks "which size?" |
| 16 | Test1 | Add "Penn reel 4000" with no model and no line | A size alone never picks a node. Brand policy only; the app does not guess Battle IV |
| 17 | Test1 | Add model BTLIII4000 (Battle III, the model in the lifetime sample) | Not in the tree (Battle III is not seeded). Brand policy only. Record whether it says the model is unknown. (Scenario 55 uses this item) |

**Part C: Milwaukee line ambiguity (the gap Scenarios 15 to 17 leave)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 18 | Test1 | Add "Milwaukee M12 tool", brand Milwaukee, no model, bought 2026-10-19 | The general line is proposed, with the note "Milwaukee has different warranties for: Heated gear, Digital levels, Portable generators, ...". **No line is ticked on a guess** |
| 19 | Test1 | Change the name to "Milwaukee M12 Heated TOUGHSHELL Jacket Kit", model 204B-21L | Heated gear (12 months, ends 2027-10-19) now matches and the note goes |

Also record: any date that differs from the key, any item where both 12 and 24 months show, any item showing the addendum without its model list or window as the source, and any place a model number is treated as matched when it is only similar.
