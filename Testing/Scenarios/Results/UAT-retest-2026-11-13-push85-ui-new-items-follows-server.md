# UAT retest: Push 85, New Items follows the server's decision (S9.10.5)

- **Build:** UI-only, redeployed 2:35 AM ET Nov 13 2026; API unchanged at `bde7439`
- **Notes:** `Bot Rules\CHANGES-push-85-new-items-follows-the-server.md`
- **Tested:** Nov 13 2026, about 3:30 AM ET, as Alice (P34-Alice Repairs), after the in-app "new version ready" Reload
- **Fixtures** (existing; no new fixtures made):
  - `15-thermal-bestbuy-tv-geek-squad.pdf`: Best Buy LG OLED TV plus Geek Squad 4-year plan plus HDMI cable, Sep 27 2026, 15-day return
  - `30-thermal-walmart-vizio-tv-protection.pdf`: Walmart Vizio TV plus Allstate 3-year plan, Aug 29 2026
- **NEXT-REPORT-ADDITIONS.md:** not present

## Summary: 2 Pass, 1 Fail, plus 1 Info recheck

| # | Check | Result |
|---|---|---|
| 1 | A sure line (Geek Squad) has no "Not added by a quick add" text and is muted | **Pass** (Low note) |
| 2 | A doubtful line shows "Not added by a quick add ..." in the warning colour | **Fail** |
| 3 | Quick add attaches only the sure coverage | **Pass** |
| 4 | Push 84 Partial recheck: unknown category with a name that has no product word | **Info** (ticks behave; Save still needs a category) |

## 1. Sure line: Pass (Low note)

Best Buy entry "OLED TV · 65IN" (`shots/c1-bestbuy-new-items.png`, `shots/c2-walmart-new-items.png`) shows these lines:
- `Best Buy return policy (merchant) · Confirmed`, grey
- `LG warranty (manufacturer) · Confirmed`, grey
- `Includes: GEEK SQUAD PROTECTION 4YR, $299.99 (plan) · Highly Likely`, with a grey note under it: "Includes: GEEK SQUAD PROTECTION 4YR, $299.99 · Geek Squad · 48 months."

No line shows "Not added by a quick add" text.

**Low:** on the Geek Squad chip, the word "Highly Likely" is amber (`--color-warn`) even though quick add attaches this plan. The chip text itself is normal. Steve should decide whether a sure line's confidence word should be muted too.

## 2. Doubtful line warning: Fail

The "Not added by a quick add ..." text did **not appear anywhere** on New Items, on either entry.

- **Walmart entry "4K TV · 50IN"** (`shots/c2-walmart-new-items.png`):
  - `Vizio warranty (manufacturer) · Unconfirmed`: only "Unconfirmed" is amber. It has no "Not added by a quick add" text, and quick add did not attach it (check 3).
  - `Walmart return policy: electronics (merchant) · Confirmed`: grey with no warning. Quick add did not attach it, because the window had already ended (Aug 29 + 30 days).
  - `Includes: Allstate Protection 3YR, $49.00 (plan) · Highly Likely`: "Highly Likely" is amber. This plan *was* attached.
  - Notes under the lines:
    - Amber: "Vizio warranty: A placeholder for testing: these are not the real terms."
    - Amber: "Allstate is not in our list yet: not verified. It stays on your account until we check it."
- **Best Buy entry:** the `Best Buy return policy · Confirmed` line is grey with no warning, yet quick add did not attach it, because the window had already ended on Oct 12.

So three lines that quick add leaves out (an unconfirmed manufacturer warranty and two ended return windows) give no "Not added by a quick add" warning. Meanwhile the amber colour lands on attached lines ("Highly Likely", and the Allstate note). The push 85 change was supposed to drive this warning from the server's `decision`, but in this build no line shows it.

## 3. Quick add attaches only sure coverage: Pass

"Quick add, edit later" showed the toast "OLED TV added to My Items." with no errors.

- **Best Buy item** (`shots/c3-bestbuy-item-page.png`): Covered · 2 policies.
  - Manufacturer warranty · LG, Sep 27 2026 to Sep 27 2027.
  - Protection plan · Geek Squad, Sep 27 2026 to Sep 27 2030, GS-88104471.
  - The ended Best Buy return window (Sep 27 to Oct 12) was **not** attached. The item shows "1 suggested policy to review".
- **Walmart item** (`shots/c3-walmart-item-page.png`, category TVs): Covered · 1 policy.
  - Protection plan · Allstate, Aug 29 2026 to Aug 29 2029, AS-66120934.
  - The Vizio warranty (Unconfirmed) and the ended Walmart electronics window were **not** attached. The item shows "2 suggested policies to review".

Both items match Push 84's behaviour: only the auto lines are attached. The Allstate plan was attached even though its company is "not verified" (amber note), which is consistent with the server's decision being auto for a stated plan on the receipt.

## 4. Push 84 Partial recheck (unknown category, name without a product word): Info

Steps on `/add/new` with the Walmart Vizio PDF. The name auto-filled as "Vizio V5" and was changed to **"Item 1"**.

- **Initial state, Category "Not sure"** (`shots/c4-addnew-notsure-initial.png`):
  - The category label reads "Category (needed: Vizio's warranty depends on it)".
  - `Walmart return policy: general · 90 days · Confirmed` is **ticked**, with the note "We could not tell what kind of item this is, so this is Walmart's general window…"
  - The electronics (30 days) and smartphones (14 days) windows are disabled, because each has ended.
  - `Vizio warranty · Unconfirmed` is unticked and reads "Not added…".
  - The Allstate plan is not listed on this form. This matches earlier pushes.
- **Save with "Not sure"** is blocked with **"Pick a category."**
- **Category TVs** (`shots/c4-addnew-tvs.png`): nothing is ticked. General is now Likely and unticked, and a protection question appears.
- **Back to "Not sure"** (`shots/c4-addnew-back-to-notsure.png`): general is **ticked again**. Unlike Push 84, where the name contained "TV", the ticks follow the category box, which confirms the notes' explanation.
- **Saved with TVs:**
  - Save first hit "You already have a purchase from this store with that order number." (`shots/c4-duplicate-order-error.png`), because the quick-add Walmart item was still there. Clearing the order number let it save.
  - The Item 1 page (`shots/c4-item1-page.png`) shows Needs info, TVs, **no policies attached**, and "2 suggested policies to review".

**Open question for Steve:** the "unknown category" ticks are now correct, but they can't be saved, because Save requires a category and picking one changes the ticks. This is the same blocker as the Push 84 Partial. It needs a design call: either allow "Not sure" on save, or accept that the general window only applies once a category is chosen.

## Other observations
- **Low (visual):** in full-page screenshots of `/add/new`, the top navigation bar is drawn partway down the page.
- **Info:** the duplicate-order guard works, and its message is clear.

## Cleanup
- Deleted OLED TV (Geek Squad plan: chose "Cancel the plan too"), 4K TV, and Item 1. Each URL now shows "Not found."
- The leftover HDMI cable pending entry was dismissed, because New Items has no delete option. The Waiting tab shows "Nothing waiting."

## Screenshots
All in `/workspace/uat/push85/shots/` on the QA box:
- `c1-bestbuy-new-items.png`
- `c2-walmart-new-items.png`
- `c3-bestbuy-item-page.png`
- `c3-walmart-item-page.png`
- `c4-addnew-notsure-initial.png`
- `c4-addnew-tvs.png`
- `c4-addnew-back-to-notsure.png`
- `c4-duplicate-order-error.png`
- `c4-item1-page.png`
