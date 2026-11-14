# Scenario 74: One receipt, several items — split, cover, return one

**Accounts:** one **personal** account (P34 Self, or Alice's personal account if it exists) plus Test2 (Bob) for a privacy check. Do not run this in the shared business P34-Alice Repairs.
**Preconditions:** clock offset **0**, app date **2026-11-11** (America/New_York). **Do not move the shared clock.** The purchase date 2026-11-04 is already in the past, and the 15-day return window is still open on Nov 11 (last day Nov 19). Reader on, or record **reader off**. The store is **Best Buy**, taken from a read-only look at the development database on 2026-11-11: the shared, verified, **general** seller policy is **15 days** from receipt (`return_days = 15`, `return_from_delivery = false`, no restocking fee). There is a separate 14-day policy for Smartphones, which does not apply here. My Best Buy Plus / Total 60-day membership extensions are not used on this ticket.
**Time:** about 30 min.
**Built per:** Scenario 41 (a protection plan on a receipt becomes its own plan; a return window is not a warranty; a TV-plus-cable receipt was an incidental check); Scenario 26 (the add form says one receipt can hold several items, but 26 never splits one); push 32 / 41 notes on receipt plans. Best Buy's 15-day general policy as stored on 2026-11-11.
**Why this plan:** a basket receipt is how people usually buy. If the whole ticket becomes one item, warranties and return windows attach to the wrong thing. If returning a $25 cable also cancels the TV's four-year plan or drops the shared receipt, the person loses coverage and proof.

## The story (answer key)

| Fact | Samsung TV | Belkin HDMI cable | Geek Squad plan | Fee / tax |
|---|---|---|---|---|
| What it should become | **Item:** **UAT S74 Samsung 55" QLED TV** | **Item:** **UAT S74 Belkin HDMI 6 ft** | **A plan on the TV only**, not a third item | **Not items** |
| SKU / model / serial | 6414275 / QN55Q60D / 0UATQ60D7411004 | 6419008 / AV10176tt06 / n/a | GSP4YTV55 / 4-year plan for SKU 6414275 only | Recycling fee; ME tax |
| Price (before tax) | **$597.99** | **$24.99** | **$179.99** | Fee **$7.50**; tax **$44.16** on the $802.97 merchandise subtotal only |
| Store return | Best Buy **15 days** from 2026-11-04 → **to 2026-11-19**, still open on Nov 11 | Same 15-day window, **to 2026-11-19** | n/a (it is not an item) | n/a |
| Maker / plan term | Samsung limited, **12 months → 2027-11-04** | Belkin limited, **12 months → 2027-11-04** | **4 years from 2026-11-04 → 2030-11-04** | n/a |
| After the cable is returned | Unchanged: still owned, same warranty, **plan still on the TV**, **the receipt stays** | Marked returned / refunded | Unchanged; it does not cover the cable | n/a |

Totals on the paper (5.5% ME tax on merchandise, fee not taxed): subtotal $802.97, fee $7.50, tax $44.16, **total $854.63**. Purchase date 11/04/2026 → **2026-11-04**. Receipt **BBY-0174-26-110447**. Customer: UAT Sample Buyer, 74 Example Lane, Testville, ME 00000, (207) 555-0174. Store: Best Buy Store #0174, 174 Example Commerce Blvd, Testville, ME 00000, (207) 555-0174.

Day terms (push 26): 2026-11-04 + 15 days = **2026-11-19**. Month terms: 2026-11-04 + 12 months = 2027-11-04; + 48 months = 2030-11-04.

## Files, in the order to use them

Each file is one PDF plus a JPG of its first page with the same name.

| # | File (.pdf + .jpg) | What it is | Who uploads it, and when | Where it goes |
|---|---|---|---|---|
| 01 | `01-receipt-bestbuy-samsung-tv-hdmi-plan` | Best Buy sales receipt dated 11/04/2026: TV, HDMI cable, 4-year Geek Squad plan on the TV, recycling fee and tax | The personal-account tester, step 1, offset 0 | Add a purchase / New Items, Read it |

## Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Tester | Confirm the **personal** account and offset **0**. Add a purchase / upload to New Items: attach receipt **01**, Read it | The reader should offer **two items and one plan**, not one bundled item and not four or five lines. **Tax ($44.16) and the $7.50 recycling fee are not items.** If the split is wrong, correct it to the key, record **reader miss / Partial**, and continue (same rule as Scenarios 52 and 69) |
| 2 | Tester | Accept / add the TV as **UAT S74 Samsung 55" QLED TV** and the cable as **UAT S74 Belkin HDMI 6 ft**. Accept the Geek Squad plan onto the **TV only**. Open both items | **TV:** store Best Buy, 2026-11-04, price $597.99, model QN55Q60D, serial from the key. **Return 15 days, active, to Nov 19, 2026.** Samsung 12-month warranty **to Nov 4, 2027** (from the receipt text, a shared Samsung policy, or added by hand — record which). **Plan:** Geek Squad Protection, **4 years, $179.99, to Nov 4, 2030**, on the TV only. If the paper states no plan start, the **purchase date is used** and the row says so (Scenario 41). **Cable:** $24.99, Belkin 12-month warranty **to Nov 4, 2027**, **same 15-day return to Nov 19**, **no** Geek Squad plan |
| 3 | Tester | Open the documents on each item | **Both items can open the same receipt.** The plan is not a third item in My Items. A return window is not labelled as a maker warranty (Scenario 41) |
| 4 | Tester | On the **cable only**, Mark returned (and record a refund of $24.99, plus any tax the UI asks for). Do not return the TV | The cable is returned / refunded. **The TV, its Samsung warranty, and the 4-year plan are unchanged.** The shared receipt **remains on the TV** (and may remain on the returned cable as history — **verify**, do not fail if it is only on the TV). The plan is not cancelled and is not moved onto the cable |
| 5 | Test2 | From Bob's personal account, open My Items and paste each item address | Empty of these UAT S74 items. Not found or no access. No prices, serials or papers |

## Per-line answer key

| Line on the paper | Amount | Keep as | Coverage / plan | Leave out? |
|---|---|---|---|---|
| Samsung 55" Class QLED 4K Q60D Smart TV (SKU 6414275) | $597.99 | **Item** (the TV) | Best Buy return 15 days to 2026-11-19; Samsung 12 months to 2027-11-04; Geek Squad 4-year plan attaches here | No |
| Belkin Ultra HD High-Speed HDMI Cable, 6 ft (SKU 6419008) | $24.99 | **Item** (the cable) | Best Buy return 15 days to 2026-11-19; Belkin 12 months to 2027-11-04; **no** plan | No |
| Geek Squad Protection 4-Year Plan — Samsung 55" TV only (SKU GSP4YTV55) | $179.99 | **Plan on the TV**, not an item | 48 months, $179.99, 2026-11-04 → 2030-11-04 | Do not make a third item |
| Environmental recycling fee | $7.50 | Neither an item nor a plan | n/a | **Leave out** of the item list |
| ME sales tax 5.5% | $44.16 | Neither an item nor a plan | n/a | **Leave out** of the item list |
| Total | **$854.63** | n/a | n/a | Used only to check the arithmetic |

## What to check, in short

1. **The ticket splits:** two items + one plan on the TV, never tax or the fee as items.
2. **Coverage follows the right line:** both items get Best Buy's 15-day window; each gets its own 12-month maker warranty; the 4-year plan is on the TV only.
3. **Returning the cable** does not cancel the TV's plan or remove the shared receipt from the TV.
4. Bob never sees any of it.
5. Reader misses are **Partial**, then corrected to this key.

## Cleanup

- Delete **UAT S74 Samsung 55" QLED TV** and **UAT S74 Belkin HDMI 6 ft**, the Geek Squad plan if it remains, their documents, notices and to-dos, in the personal account only.
- No clock change was required. If someone moved it, ask QA Controller to reset it to 0.

## Checked when this was made

- Built 2026-11-11 on the box (`generate_all.py` in `/workspace/uat/scen-71-74/`). Receipt number, all three line prices, subtotal $802.97, fee $7.50, tax $44.16, total $854.63, dates, model QN55Q60D and "Geek Squad Protection" were found in the PDF text layer (`validation.json`). The JPG twin was checked by eye.
- The purchase date 2026-11-04 is in the past at step 1, and the 15-day window is still open on 2026-11-11.
- Best Buy policy facts came from a **read-only** development-database query on 2026-11-11. No database write was made.

## Known rough edges and open questions for CC (not part of the answer key)

- **Split quality.** Scenario 41 noted that "several items per receipt each with its own plan" was not built at the time, and its TV-plus-cable case was incidental. If today's reader still bundles the ticket or creates a third item for the plan or the fee, that is a **Partial** (correct to the key) and a finding for the reader, not a tester error.
- **Shared Samsung / Belkin policy vs stated-on-receipt.** The receipt only states the 12-month terms; it is not a full warranty booklet. Record whether each warranty is suggested from shared data, stated from the receipt (low confidence, Scenario 41), or typed by hand.
- **Tax on the recycling fee.** This pack does not tax the $7.50 fee. If a tester or the reader reallocates tax, the merchandise total and the two item prices should still match the key.
- **Returning one line of a multi-item purchase.** Push 33 asks what happens to a plan when *that* item is returned. It should not ask about, or cancel, a plan that is only on a sibling item. If the UI asks anyway, record the wording.
- **Where the receipt lives after one line is returned.** The TV must still be able to open it. Whether the returned cable also keeps a copy is unspecified.
