# StuffIt retest - build bbc006b (push 7: paperwork route and retest fixes)
Date: Tue Nov 3 2026, 8:52-9:00 PM ET. API commit bbc006b (Staging, started 8:44 PM ET), UI 5245689, no migration. Alice and Bob reset by DB Stager first. Clock offset 0. Fixes only, no regression.

**Totals: 12 rows (incl. setup). 9 Pass, 2 Partial, 1 Fail.** No server errors.

**Data note:** Tablets and Subscriptions and services were **not** added by the seed on restart. DB Stager inserted both with the SQL from the DATA file (Tablets under Electronics; categories 52 to 54). The Add purchase list shows Tablets as a flat entry, not nested under Electronics.

| Id | Source | Result | What we saw |
|---|---|---|---|
| S-0 | setup | Pass | UAT Laptop and UAT Washer saved (question answered No). |
| P-1 | C43-8 | Partial | Opens `/plans/new?item=...&itemName=UAT%20Laptop&paperwork=1` with the file picker; read in ~9 s; "Covers UAT Laptop" ticked; file kept as proof; **a real plan is made** (listed under Protection plans, contract GS-91440236). But the company box was empty after "Fill the form": reader gave "Geek Squad (Best Buy)", shown as '"Geek Squad (Best Buy)" is not selected yet. Pick a name from the list, or add ... as new.' Matched neither Geek Squad nor was filled in. |
| P-2 | C43-9 | **Fail** | Form note: "The document gives a price but does not say how often it is paid. Check "Paid" under What it costs." and **Paid defaulted to "a year"**. Only after setting "one payment" by hand: "$299.99 one payment ($75.00 a year)". Notes say "a year" does not appear on this route. |
| P-3 | A-5 | Pass | Price 54.99 kept after untick, reload, tick; plan saved at "$54.99 one payment". |
| P-4 | finding 5 | Pass | The 2 suggestions were the Best Buy return window and the Sony warranty; "Doesn't apply" on both took the count to 0, still 0 after reload. |
| P-5 | B-1 | Partial | Not testable this time: the live reader found "Lowe's" as the company, so the no-company hint didn't show. Row: "Includes: Lowe's Protection Plan 3-Year, $99.00 · Lowe's · 36 months". |
| P-6 | B-7 note | Pass | Allstate shows "UNVERIFIED" on the plan list and plan page; Geek Squad shows none. |
| P-7 | D-3 | Pass | "Saved now: $75.00 New: $95.00". Typed company "UAT Home Warranty Co" shows UNVERIFIED. (Also listed Exclusions "nothing saved / Cosmetic damage", a real difference.) |
| P-8 | Other finding 1 | Pass | No renewal to-do for UAT Old Ended Plan (Ended Jan 1, 2025); the Sep 3, 2027 plan still gets "Renew or replace it." |
| P-9 | C-0 / C43-7 | Pass | Tablets exists; plan question shows for a $400 Best Buy tablet; type-it-in starts on Insurance, a month. |
| P-10 | B-8 | Pass | Subscriptions and services at $400: question not shown. |
| P-11 | B-8b | Pass | Smartphones at $5: not shown. |

## Findings for Steve
1. **P-2 (Fail):** on the paperwork route, Paid defaults to "a year" when the reader can't tell how often it's paid, so a one-off $299.99 plan shows as yearly unless the user fixes it.
2. **P-1:** the reader's company "Geek Squad (Best Buy)" isn't matched to Geek Squad, and the box is left empty instead of filled with "add as new".
3. The seed didn't add the two new categories on restart (inserted by SQL instead).
4. Minor: plan cost shows a derived yearly figure next to one payment, e.g. "$54.99 one payment ($27.48 a year)"; confirm that's intended.
5. Minor: the notification bell showed "1 to do" right after sign-in on a freshly reset account.
6. Minor: the plan question can take a second or two to appear after the price is typed.
