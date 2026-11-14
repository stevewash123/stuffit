# UAT retest: Push 86, New Items chips say what quick add leaves (S9.10.5)

- **Build:** UI-only, redeployed 4:08 AM ET Nov 13 2026; API unchanged at `bde7439`
- **Notes:** `Bot Rules\CHANGES-push-86-chips-say-what-quick-add-leaves.md`
- **Tested:** Nov 13 2026, 4:34 to 4:37 AM ET, as Alice (P34-Alice Repairs). Results are from after the in-app "new version" Reload; before the reload the chips still had no suffix.
- **Fixtures** (existing; no new ones made):
  - `30-thermal-walmart-vizio-tv-protection.pdf`
  - `15-thermal-bestbuy-tv-geek-squad.pdf`
- **Out of scope** (held for design per the notes): "Highly Likely" shown in amber, and Save needing a category.
- **NEXT-REPORT-ADDITIONS.md:** not present

## Summary: 3 Pass, 0 Fail, 1 not exercisable (Info)

| # | Check | Result |
|---|---|---|
| 1 | Walmart/Vizio: the chips quick add won't attach carry the suffix; Allstate has none | **Pass** |
| 2 | Best Buy/Geek Squad: LG and Geek Squad have no suffix; the ended Best Buy return chip has it | **Pass** |
| 3 | Quick add attaches exactly the chips without the suffix | **Pass** |
| 4 | The "Not added by a quick add: ..." receipt-line sentence is unchanged | **Info:** neither fixture has a doubtful stated line, so the sentence didn't appear (expected, per the notes) |

## 1. Walmart entry: Pass
"4K TV · 50IN", Walmart · Aug 29 2026 · $397.74 (`shots/c1-walmart-entry.png`, `shots/c1-walmart-chips-zoom.png`)

Chips:
- `Walmart return policy: electronics (merchant) · Confirmed · left to you on Add Details` (the window ended)
- `Vizio warranty (manufacturer) · Unconfirmed · left to you on Add Details`
- `Includes: Allstate Protection 3YR, $49.00 (plan) · Highly Likely` (no suffix)
- There's no separate Walmart general chip, because the category was inferred as TVs.

Notes are unchanged from Push 85: the Vizio placeholder, Allstate 36 months, "Covers TV", and "Allstate is not in our list yet".

The suffix reads "· left to you on Add Details". The "A…" in the CHANGES notes was a garbled character.

## 2. Best Buy entry: Pass
"OLED TV · 65IN", Best Buy · Sep 27 2026 · $1,299.99 (`shots/c2-bestbuy-chips-zoom.png`)

Chips:
- `Best Buy return policy (merchant) · Confirmed · left to you on Add Details` (the window ended Oct 12)
- `LG warranty (manufacturer) · Confirmed` (no suffix)
- `Includes: GEEK SQUAD PROTECTION 4YR, $299.99 (plan) · Highly Likely` (no suffix)

## 3. Quick add: Pass
- **Best Buy item** (`shots/c3-bestbuy-policies-card.png`): Covered · 2 policies, plus 1 suggested.
  - LG manufacturer warranty, to Sep 27 2027.
  - Geek Squad 4YR, Sep 27 2026 to Sep 27 2030, GS-88104471.
  - The Best Buy return window was not attached.
- **Walmart item** (`shots/c3-walmart-policies-card.png`): Covered · 1 policy, plus 2 suggested.
  - Allstate 3YR, Aug 29 2026 to Aug 29 2029, AS-66120934.
  - The Vizio warranty and the Walmart electronics window were not attached.

The attached policies match the chips without the suffix exactly.

## 4. Receipt-line sentence: Info
- No "Not added by a quick add: ..." sentence appeared on either entry.
- The notes say this sentence belongs only to doubtful plan or stated-warranty lines, and neither fixture has one. This check is therefore not exercised. Nothing suggests a change.

## Other observations (outside scope, for Steve or CC)
- **Info: HDMI cable not listed.** The Best Buy upload showed no "Smaller things" section and no HDMI cable entry. In Push 85 it appeared as "Smaller things (1)". The likely cause is that QA dismissed that HDMI entry in Push 85, and a re-upload of the same receipt now skips it. This is not confirmed.
- **Low: two different prices for the Walmart item.** The Price field on the Walmart item page shows $328.00, while New Items showed $397.74, which is the receipt total. The My Items card showed $328.00. Not investigated further.

## Cleanup
- Deleted both items via Edit > Delete > "Cancel the plan too" > Delete item. "Delete item" stays disabled until a plan option is chosen.
- New Items Waiting shows "Nothing waiting." (`shots/c3-cleanup-new-items-empty.png`).

## Screenshots
All in `/workspace/uat/push86/shots/` on the QA box:
- `c1-walmart-entry.png`
- `c1-walmart-chips-zoom.png`
- `c2-bestbuy-chips-zoom.png`
- `c3-bestbuy-policies-card.png`
- `c3-walmart-policies-card.png`
- `c3-cleanup-new-items-empty.png`
