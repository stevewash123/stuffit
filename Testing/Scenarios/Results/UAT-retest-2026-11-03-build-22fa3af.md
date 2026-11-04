# StuffIt retest - push 8 (UI 22fa3af, API bbc006b)
Date: Tue Nov 3 2026, 9:35-9:37 PM ET. UI-only push (UI redeployed 9:29 PM ET; /api/version still bbc006b). Alice reset by DB Stager first (Geek Squad is in the shared plan-company list). Clock offset 0. Fixes only.

**Totals: 4 rows. 4 Pass, 0 Partial, 0 Fail.**

| Id | Source | Result | What we saw |
|---|---|---|---|
| S-0 | setup | Pass | UAT Laptop (Best Buy, Computers, $1,200.00) saved. |
| P-1 | C43-8 | Pass | Paperwork route `/plans/new?item=...&paperwork=1`; file read at once; Company box shows "Geek Squad" **selected** (bracketed "(Best Buy)" dropped), no "not selected yet" hint; "Covers UAT Laptop" ticked. |
| P-2 | C43-9 | Pass | Paid defaulted to **one payment**; note "...We assumed one payment because the plan runs more than a year: check "Paid" under What it costs."; plan page "Cost $299.99 one payment ($75.00 a year)", list "$299.99 one payment". |
| P-2b | control | Pass (note) | `plan-contract.png` (one-year term, Jun 1 2026 to Jun 1 2027, printed "$19.99 a month"): Paid = a month, note "Price: $19.99 a month.", no assumption text. This document states the rhythm, so it isn't a true "price without rhythm, a year or less" case. Not saved. |

Note: the plan name now reads "Geek Squad Protection Plan - 4-Year Protection Plan" (was "Geek Squad Protection Plan (4-Year Protection Plan)" on bbc006b), probably a reader wording difference.

C43-8 and C43-9 are now closed.
