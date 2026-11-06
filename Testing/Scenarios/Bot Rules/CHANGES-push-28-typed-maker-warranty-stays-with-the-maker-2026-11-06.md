# What changed in push 28: a typed maker warranty stays with the maker; offers sorted by confidence; new logo; fixes from your push 26/27 results (2026-11-06)

For GrokBot. API `02cca5d` (includes `b849044`, `ae06cbd`) and UI `6d037ce` (includes `06c8417`, `aa26b64`). Check `/api/version` (`commit` must be `02cca5d`); the UI proof is the new logo (below). No migration. No reference seed change. Story S3.2.12.

## Fixed (from your push 26 and push 27 results)
| Where | What |
|---|---|
| S62.23 reader | A document that says free replacement for 36 months, then prorated to 72, should now give **two** coverages (free 36 months, then a Prorated stage). The cause was the reader's instructions (it returned 72 for the free stage); they are reworded. **Not verified against the live reader**: please retest with the same tire paper and report what you get |
| S62.17 My Items | The row shows **Prorated: you pay a share** when the item has a prorated stage, even when the row's own coverage is the free stage |
| S62.14 no install day | A part's coverage typed by hand, or taken from a shared policy, with no install day is counted from the purchase date and marked **start date to confirm** (the usual to-do and notification). Entering the install day finishes it. A start date you typed that differs from the purchase date is kept. Linking an item that already has coverage is **not** marked (left alone on purpose) |
| S62.13 | The part's coverage line reads "It ends at 88,000 miles on the odometer." and the vehicle's Parts row ends "...50,000 miles, ends at 88,000 miles on the odometer." |
| S62.11 | A part taken off a vehicle reads "Until <date>, counted by date." then "Miles no longer watched...", with no "whichever comes first" |
| P26-3B | Saving a start date from the item page's **To do** card, the **To do** page, or **Notifications** now refreshes the header badge and the item's coverage dates at once (no reload) |
| Verified beats typed | When a **verified** shared policy exists for the same maker and kind of product, it wins the maker's headline slot over your hand-typed entry. Your typed entry shows only when there is no verified one. Policies you entered by other means (receipt, document, settings) still win |

## Answers / by design (do not report as new)
- **P26-1 (the "Your own entry may be out of date" note never appeared on an appliance):** by design today. On an ordinary item a document **replaces** a typed maker warranty on that item, so a typed row and a document row never exist together there. The note applies where both exist (for example a typed row added after a document is read). The typed warranty now also stays as your own policy on the maker. Retest the note by typing the maker warranty **after** applying the document.
- **S62.16:** "Ended Nov 5" beside "ended by miles on Nov 6" is by design (the day before the reading day).
- **S62.15:** a never-linked ordinary item has no mile-limit field (by design).
- **S62.7, S62.9, S62.12:** no follower form on vehicles or parts yet; the vehicle cannot be offered as a part so the refusal message is not reachable; Bob checks need an API contract.

## New: offers are sorted by confidence (all offer lists)
In every list of offered coverages (New Items, Add a purchase, the item page), the **most trusted offer is at the top**. Equally trusted offers keep their earlier order. A hand-typed maker entry (low confidence) therefore sits below a verified shared policy.
- Check: an item whose maker has a verified shared warranty and whose card has an extended-warranty benefit: the higher-confidence offers come before the "typed in by hand" one.

## New: Rocky with the car ball on the sign-in screens
Login, sign-up, password reset, verify email, accept terms and unsubscribe show **Rocky lying with the four round icons** above the WarrantyCat wordmark (before: the head only). The header inside the app is unchanged (logo beside the wordmark). Check by eye; no data change.

## New (S3.2.12)
When you **type a maker warranty by hand** on an ordinary item (Edit > Add coverage, kind Manufacturer), WarrantyCat now keeps it as **your own policy on that maker** (for the item's category). Later items and New Items from the same maker are **offered it** in the "could apply" list, like any policy, but:
- It is **never ticked**: confidence is low ("Your own entry, typed in by hand; not checked against the maker's source.").
- It is offered only to **your account**; another account is never offered it.
- Your waiting **New Items** from that maker are re-checked and offered it.
- The item you typed it on is **not** offered its own policy.
- Typing the **same term again** makes no duplicate. A **different term** replaces the term of your entry for that maker and category. An unrelated edit (a phone number) does not change it.
- Deleting the coverage or the item keeps the policy (it is the maker's, not the item's). Retire it with the existing policy retire action.
- A term the shared list already holds for that maker and category is not copied (the shared one is offered, with higher confidence).

## Not made into a policy (expected)
A vehicle or a part of one; an item with no maker; an item with no category; a private-sale seller; a coverage whose provider is not the item's maker; lifetime, optional, component, certified, prorated, start-unknown or plan coverages; a term that cannot be worked out (months, or exact start/end dates one year-ish apart).

## Steps to run
1. Add an appliance from a maker on our list with a category (say Whirlpool dishwasher). Edit > Add coverage: maker warranty, 12 months. Save.
2. Add a **second** item from the same maker and category. In its "could apply" list, expect "Whirlpool warranty: 12 months", **unticked**, with the "typed in by hand" reason.
3. Do the same from a **New Item** (forwarded receipt or Add a purchase) that was waiting before step 1: it shows the offer after re-check.
4. Type 12 months again on a third item: still one offered policy (no duplicate). Type 24 months: the offer now says 24.
5. Test2 with the same maker: **not** offered Test1's entry.
6. Repeat on a vehicle: nothing is offered to later vehicles.
7. Check the "probably replaced" note (push 26) still behaves the same.

## Known, not a bug
A private policy beats a shared one at the same category level in the lookup, so a typed term that differs from a verified shared one is offered **ahead** of it, unticked and low confidence, with the existing "differs from the verified" note. Say if this order looks wrong.

## Not changed, do not report as new
Items listed under push 26 and 27 "Not changed".
