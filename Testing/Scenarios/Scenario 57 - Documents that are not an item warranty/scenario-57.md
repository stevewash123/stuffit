# Scenario 57: A return policy, a card guide and a plan certificate: what each one is

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Reader on. Clock offset 0 (2026-11-04). Test1 has the Chase Freedom Unlimited card ending 1111 and **not** a "Northshore Bank Visa Signature".
**Time:** 50 min
**Built per:** S2.4.1 (document kinds), S3.2.5 and S3.2.7 (unverified stores, nothing shared from a reading alone), S3.3.2 (card benefits), S3.4.2 (plans), S3.4.15 (cancel a plan within its window). Documents: `Testing/SampleData/warranties/retailer-return-and-store-warranty.pdf`, `edge-card-extended-warranty-benefit.pdf`, `multi-item-protection-plan.pdf`.
**Why this plan:** three documents look like warranties and none is one for the item. The app must say what each is, keep what it can, and never put a return window, a card benefit or a plan price on an item as if it were a maker warranty. T2 B11 and B12 list these as "known gap" without a run.

**Part A: a store's return policy plus a short store warranty (Westbrook Electronics)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open New Items or the Documents upload with **no item** (loose upload). Upload `retailer-return-and-store-warranty.pdf` | Recognised as a **store policy**, not a maker warranty; told so in plain words. No item is created |
| 2 | Test1 | Read what was extracted | Default return window **30 days**; **14 days** for televisions over 55 inches, computers and cameras; **final sale**: opened software, headphones, personal care items; **15% restocking fee** on opened cameras and drones; **holiday extension**: items bought November 1 to December 24 returnable until **January 31**; **store warranty 90 days** on top of the maker's |
| 3 | Test1 | Check what it offers to do | It is offered as a **private** store policy for "Westbrook Electronics" ("not in our list", not verified). Nothing is shared with anyone (S3.2.7). No claim is queued from the reading alone |
| 4 | Test1 | Accept it. Then add three items bought at Westbrook: a **65-inch TV** bought **2026-09-01**; a **camera** bought **2026-11-02**; **headphones** bought **2026-10-01** | TV: **14 days**, ended 2026-09-15. Camera: the holiday extension applies (bought November 2), return until **2027-01-31**; restocking fee 15% noted if opened. Headphones: **final sale**, shown as not returnable (no date, no reminder) |
| 5 | Test1 | Check each item for the **store warranty** | 90 days from purchase as a separate store coverage, **in addition to** the maker's: TV ends **2026-11-30**; camera ends **2027-01-31** (90 days from 2026-11-02; it happens to equal the holiday return date, so confirm the two lines are separate); headphones end **2026-12-30**. The maker's warranty is not replaced |
| 6 | Test1 | Check a TV of 55 inches exactly and one of 56 inches | "Over 55" means 56 and up. 55 inches is on the 30-day window. Record how size is read; if the app has no size field, mark Not built |
| 7 | Test1 | Check an item bought 2026-12-25 | Outside the holiday range (December 24 is the last day): the 30-day default applies |
| 8 | Test1 | Check that the policy is **not** shown as a manufacturer warranty on any item | No "warranty" coverage labelled Westbrook that is actually the return window. The return window and the 90-day store warranty are two separate lines |

**Part B: a card guide (Northshore Bank Visa Signature)**

| # | Persona | Action | Expected |
|---|---|---|---|
| 9 | Test1 | Upload `edge-card-extended-warranty-benefit.pdf` loose | Recognised as a **card benefit**, not an item warranty. The page says what it is and that it depends on which card paid |
| 10 | Test1 | Read what was extracted | Adds up to **one extra year** ("doubles the original warranty, up to one year"); only for original warranties of **3 years or less**; up to the purchase price, maximum **$10,000 per item**; **$50,000 per account per year**; **not eligible**: motor vehicles, real estate and fixtures, used or pre-owned, medical equipment, items bought for resale; file a claim within **60 days of the failure**; keep receipt, card statement and the original maker warranty |
| 11 | Test1 | Check what it offers | Offered to **add the card** (Northshore Bank Visa Signature) with these as its benefits, as an unverified private card. Not attached to any item |
| 12 | Test1 | Accept. Add a TV (Samsung, 12-month maker warranty) paid with that card | Card extension ends **12 months after the maker warranty ends**, cap $10,000. Another item with a **5-year** maker warranty: not eligible, with the reason. A used item: not eligible |
| 13 | Test1 | Pay a $12,000 item with the card | The cap ($10,000) is shown as a limit on the extension. The app does not say the whole $12,000 is covered |
| 14 | Test1 | Check the claim flow on a card-extended item | The 60-day-from-failure rule is shown, with the list of what to keep |
| 15 | Test2 | Open Test1's card or policy by address | Not found |

**Part C: a plan certificate that covers three products (SafeHaven, plan SH-2026-0091744)**

Sold by Westbrook Electronics on **2026-05-14**. Plan holder Sam Sample. Plan price **$289.99** total ($3.99 monthly option).

| # | Item | Model / serial | Item price | Term | Deductible |
|---|---|---|---|---|---|
| 1 | 65-inch OLED television | VX65-OL / 7710442 | $1,499.99 | 4 years | $0 |
| 2 | Soundbar with wireless subwoofer | SB900 / 55102 | $449.00 | 3 years | $25 |
| 3 | Streaming media player | SP-4K / 88213 | $79.99 | 2 years | $25 |

| # | Persona | Action | Expected |
|---|---|---|---|
| 16 | Test1 | Add the three items by hand (bought 2026-05-14, Westbrook, with the prices above) | Three items |
| 17 | Test1 | Upload `multi-item-protection-plan.pdf` loose, then to the TV | **Known gap (T2 B12):** may read as one plan. Expected: **one plan** with **three covered items**, each with its own term and deductible (4 / 3 / 2 years; $0 / $25 / $25). Plan holder Sam Sample |
| 18 | Test1 | Check the price | The plan price **$289.99 is the plan's cost**, not an item price. No item has its price changed to 289.99. The monthly option ($3.99) is a note, not the user's billing unless chosen |
| 19 | Test1 | Check the start date | **Conflict flagged, not guessed:** the terms say "from May 14, 2026", but coverage begins when each maker's warranty ends. The app shows both readings, asks, and does not pick one. Candidate end dates if counted from May 14: TV **2030-05-14**, soundbar **2029-05-14**, player **2028-05-14** |
| 20 | Test1 | Check what else was read | **Power surge covered from day one.** Claims are **limited to the purchase price of the item** (a limit per item, shown beside each item price). **After three paid claims on one item the plan is fulfilled and ends for that item.** **Transferable once** to a new owner for a **$20 fee.** **Cancel within 30 days for a full refund** (until **2026-06-13**) |
| 21 | Test1 | Record three paid claims on the soundbar (via the claim log) | The plan shows "3 of 3 paid claims used" for the soundbar and ends for that item only; the TV and the player stay covered. If the app has no claim counter, mark Not built |
| 22 | Test1 | Mark the player given away | Asks the plan question: this plan is transferable **once for $20**; the app says so and does not just keep or drop the plan. Other items keep it |
| 23 | Test1 | Try cancelling on a clock date of 2026-06-10, then of 2026-06-20 | Within the window (June 10): offered a full refund path (S3.4.15). After June 13: the full-refund wording is not offered |
| 24 | Test1 | Open the extended warranties list | The plan appears **once** (not once per item) and the yearly figure counts it once |
| 25 | Test2 | Open Test1's plan by address | Not found |

Also record: any return window, card benefit or plan price shown as a maker warranty on an item, any plan counted more than once, and any date that disagrees with the key.
