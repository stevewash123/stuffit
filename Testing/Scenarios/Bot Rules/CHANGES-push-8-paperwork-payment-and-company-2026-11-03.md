# What changed in push 8: paperwork route payment and company match (2026-11-03)

For GrokBot. Push 8 is UI only: API stays `bbc006b`, UI is `22fa3af`. No migration. It answers your retest of `bbc006b`. Re-run **P-1 and P-2** with the same Geek Squad paperwork on a fresh UAT Laptop; everything else you passed stands.

| Change | What you should see | Your row |
|---|---|---|
| Payment rhythm | When the document gives a price but not how often it is paid, and the plan runs **more than a year**, "Paid" is set to **one payment** and the note says "We assumed one payment because the plan runs more than a year: check Paid". The cost line reads "$299.99 one payment". A plan of a year or less keeps the old note and the old default, and you choose | P-2 / C43-9 |
| Company with the seller in brackets | "Geek Squad (Best Buy)" is searched as **Geek Squad**; the bracketed seller is dropped. If Geek Squad is in the shared list it is selected. If not, the Company box holds "Geek Squad" (not the bracketed text) to add as new | P-1 / C43-8 |

## Decided, do not report
- The plan cost showing a derived yearly figure beside one payment ("$54.99 one payment ($27.48 a year)") is intended.
- The Tablets and Subscriptions and services categories are not added on a normal start; the seed runs only with `--seed` (the data note now says so). Tablets listed flat in the Add purchase picker is how the picker shows categories; its parent is still Electronics (the plan question shows for it).
- The "1 to do" on a fresh account right after sign-in and the second or two before the plan question appears are noted, not changed.
- Everything in the earlier push notes still holds.
