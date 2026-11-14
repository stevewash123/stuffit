# UAT retest: Push 87, no client-side thresholds (regression)

- **Build:** UI-only, redeployed 5:16 AM ET Nov 13 2026. API unchanged at `bde7439`.
- **Notes:** `Bot Rules\CHANGES-push-87-no-client-thresholds.md`. The screens dropped their own 80% fallback, so ticks now come only from the server's decision. Nothing should look different.
- **Tested:** Nov 13 2026, about 5:30 to 5:35 AM ET, as Alice (P34-Alice Repairs).
- **Fixtures** (existing; no new ones made):
  - `30-thermal-walmart-vizio-tv-protection.pdf`
  - `homedepot-receipt-01.pdf`
  - `15-thermal-bestbuy-tv-geek-squad.pdf`
  - Lowe's/DeWalt and Sam's Club were typed in by hand.
- **Out of scope:** the Add form's own estimate for a paper attached on the form (TICKED_FROM and document-fit values), left in place on purpose.
- **NEXT-REPORT-ADDITIONS.md:** not present.

## Summary: 3 Pass, 0 Fail

| # | Check | Result |
|---|---|---|
| 1 | `/add/new` ticks match Push 81/84, and "Other return windows (n)" still shows | **Pass** |
| 2 | Item page Review: ticks match Push 83, and the ended window stays unticked | **Pass** |
| 3 | New Items chips and suffix match Push 86, and quick add attaches the same lines | **Pass** |

## 1. Add purchase form: Pass

### a) Walmart PDF, category Not sure, name "Item 1"
Screenshot: `c1a-walmart-form.webp`

- Walmart general, 90 days, Confirmed: **ticked**. It shows the "could not tell what kind of item" note.
- Walmart electronics, 30 days, Likely: disabled, because the window ended 2026-09-28.
- Walmart smartphones, 14 days, Likely: disabled, because the window ended 2026-09-12.
- Vizio warranty, 1 year, Unconfirmed: unticked.

### b) Lowe's / DeWalt / Power tools / Cordless Drill / 2026-11-12
Screenshot: `c1b-lowes-dewalt.webp`

- DeWalt warranty, 3 years, Confirmed: ticked.
- Lowe's return policy, 90 days, Confirmed: ticked.
- "Checking what applies…" showed briefly and then cleared.

### c) Home Depot PDF, category Not sure
Screenshot: `c1c-homedepot.webp`

- Home Depot general, 90 days, Confirmed: ticked.
- Home Depot major appliances, 2 days, Likely: disabled, because the window ended 2026-08-17.
- Six Milwaukee lines, all Likely and unticked: general 1 year, portable generators 2 years, outdoor power equipment 3 years, hoists 1 year, digital levels 3 years, power tools 5 years.

### d) Sam's Club / 2026-11-12 / Test TV / TVs
Screenshot: `c1d-samsclub.webp`

- The form shows Sam's Club electronics, 90 days, Unconfirmed, plus the link "Other return windows (1)".
- Clicking the link shows Sam's Club general, and the link changes to "Hide other return windows".
- Clicking the label text toggles the two return windows, and only one can be ticked at a time.
- **Info:** before the category took effect, the panel briefly showed only the general line with "Other return windows (3)".

All four cases match Push 81/84.

## 2. Item page Review: Pass
Screenshot: `c2-item-review.webp`

"P87 UAT Vizio" was saved with category TVs and every line unticked. Its Suggested coverage list shows:

- Walmart electronics, Aug 29 to Sep 28 2026, ended: unticked.
- Walmart general, to Nov 27 2026, Likely: unticked.
- Vizio TVs warranty, Unconfirmed: unticked.

This matches Push 83, and the ended window stayed unticked.

**Info:** on the item page the ended window's checkbox is not disabled, so it can still be ticked by hand. That is the known earlier Low, and it is unchanged.

**Info:** uploading the PDF on the form overwrote the typed item name with "Vizio V5", so the name had to be typed again.

## 3. New Items: Pass
Screenshots: `c3-new-items-chips.webp`, `c3-walmart-item.webp`

Best Buy chips:
- `Best Buy return policy (merchant)· Confirmed· left to you on Add Details`
- `LG warranty (manufacturer)· Confirmed`
- `Includes: GEEK SQUAD PROTECTION 4YR, $299.99 (plan)· Highly Likely`

Walmart chips:
- `Walmart return policy: electronics (merchant)· Confirmed· left to you on Add Details`
- `Vizio warranty (manufacturer)· Unconfirmed· left to you on Add Details`
- `Includes: Allstate Protection 3YR, $49.00 (plan)· Highly Likely`

Quick add results:
- **Best Buy:** Covered, 2 policies (LG warranty and the Geek Squad plan), plus 1 suggested.
- **Walmart:** Covered, 1 policy (the Allstate plan), plus 2 suggested.

This is identical to Push 86.

## Cleanup
- Deleted P87 UAT Vizio, 4K TV and OLED TV, choosing "Cancel the plan too" for the plans.
- New Items Waiting shows 0 of 0. My Items has no test items left.

## Screenshots
All in `/workspace/uat/push87/shots/` on the QA box:
- `c1a-walmart-form.webp`
- `c1b-lowes-dewalt.webp`
- `c1c-homedepot.webp`
- `c1d-samsclub.webp`
- `c2-item-review.webp`
- `c3-new-items-chips.webp`
- `c3-walmart-item.webp`
