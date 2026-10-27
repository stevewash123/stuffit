# Plan: the "worth tracking" rule in the New Items decision process

Story: `Stories/E9-web-ui/F9.8-settings-ui/S9.8.5-choose-whats-worth-tracking.md`. This plan covers the part we can build now: the rule, with the amount as one global setting (default $50), plus bulk removal on New Items. The per-person setting and the learning prompt stay in the story for later.

Revised 2026-10-19 after review: keep more lines and lower their confidence instead of dropping them; no special "main item"; plans pair with the line printed just before them; add multi-select removal.

## What the app does today (checked 2026-10-19)
1. The reader labels each receipt line `product`, `repair`, `consumable`, `service` or `fee` (`document-kinds.json`, field `products`).
2. `ReceiptProducts.Parse` **keeps only `product` and `repair`**; everything else is dropped, and at most 12 lines are kept.
3. `PendingItemService.Reading.cs` makes **one pending item per product** (`AddOtherProductsAsync`).
4. Every field has a confidence. Values under the check line are listed in `check`, and quick add waits for them. There is already one soft choice: a repair line gets `kind = 0.4`.
5. New Items (`new-items.page.ts`) is a list with a quick-add button per row. **Removal is Dismiss only**: one row at a time, reversible (Undo, a Dismissed tab with Restore). There is no hard delete and no multi-select.

## Design
**Keep more, say less sure.** A line the reader calls a consumable can still carry a warranty (an expensive bulb, a filter, a belt). So `Parse` stops dropping them. They become pending items whose `kind` confidence is low (consumable 0.3, below repair's 0.4), so they land in the existing `check` list and sort last. The one exception stays: a receipt with **no** product or repair line at all (a grocery run) still makes nothing, as today. Services, fees, discounts and tax lines are still not items.

**Keep the signals, compute the verdict at list time.** Store what is needed to judge a line; work out the verdict from those and the current amount when the list is built. Changing the amount later (the user setting) then needs no rewrite of stored data.

- **Signals on the pending item** (new nullable columns, written when the item is made):
  - `LinePrice` (reuse `ItemPrice` if it already holds this line's price);
  - `LargestLine` (the receipt's largest line price, for "much smaller than the rest");
  - `LineKind` (product, repair or consumable, as the reader labelled it);
  - `SmallPartWords` (which accessory or used-up words matched, for the reason text).
- **No "main item".** The rule never needs to know which line is the main one.
- **Verdict** (`TrackingHint.Judge`, a pure static function, no I/O, no model):
  - `Unlikely` = under the amount **and** at least one other signal (an accessory or wear word, a used-up part, a consumable label, or under a fifth of the receipt's largest line);
  - `Unsure` = under the amount with no other signal (a cheap but ordinary product, such as a $30 kettle);
  - `Likely` = everything else, including every line at or over the amount.
  Price alone never demotes. A lone cheap product stays `Unsure` at worst.
- **The words are data, not code**, like `category-keywords.json`: `Purchases/tracking-signals.json` holds the word lists and the "much smaller" ratio. The answer-key generator reads the same file.
- **The amount** is `TrackingOptions.SmallItemThreshold` (decimal, default 50), bound from the `Tracking` config section through `IOptions`. Zero means "track everything". Later the user's profile value overrides it; the rule already takes the amount as an argument.

**Plans pair with the line just before them.** Extended warranties are usually printed right after what they cover (the user's estimate is 85% or more). When a plan is read (S2.4.7), the default link is the **nearest preceding product line**; a plan's own text (a SKU, model, product word) overrides that when it names something else; a plan whose text points two ways, or that has no earlier product, is linked with low confidence and goes to the check list. Two consequences:
- Sorting a small item into "Smaller things" must never separate a plan from its item: a plan's item is never `Unlikely` on price alone, and the pairing is made before any sort.
- The answer key's `covers_line_no` is the same rule, so it can be used to measure how often "the line before" is right on the sample receipts (it is by construction there; a real-receipt check comes from the labelled set, S2.4.3).

**Removal gets three upgrades** (the Dismissed tab stays, as the user wants):
- **Multi-select Dismiss** on the Waiting list: a checkbox per row, "Select all" for the visible rows, and a bar with "Dismiss N". One request, one Undo for the whole batch. Reversible, the same as today's single dismiss.
- **Permanent delete on the Dismissed tab**: a checkbox per row, "Select all", and "Delete N permanently", plus a single-row delete. A confirm names the count and says it cannot be undone.
- **Empty dismissed**: one button on the Dismissed tab that permanently deletes *every* dismissed item, not only the page shown. The confirm shows the total count; the call runs server side so a long list is not a long loop in the browser.
- Deleting removes the pending item and its stored email or file copy (and the receipt pages copied for it), and keeps nothing that would stop the same receipt being scanned again. It is audited like other deletions and follows account deletion and retention (S1.4.2, S2.6.1); retention can still clear dismissed items on its own schedule.

## Rescanning after a delete (decided 2026-10-19)
A permanently deleted receipt or line leaves **no trace**: no tombstone, no kept key. Scanning or forwarding the same receipt again is the way back, and it must not duplicate what the person kept.

- **Today's rule is too blunt for this.** The first item's key is the receipt (seller plus order number, else a content hash) and later lines are keyed `{receipt}#N` by position. "Same receipt again adds nothing" (`Duplicate`) is decided for the whole receipt, and a position key breaks as soon as a line is missing or the lines come out in a different order.
- **New rule: decide per line.** Each pending item stores a receipt key and a **line key** (normalised model number, else normalised name, with the line price). On a repeat scan every line the reader finds is matched against the items that already exist for that receipt:
  - exists in **Waiting** (New Items) → skip;
  - exists in **My Items** (an accepted item whose target purchase or item still exists; a missing target means it was deleted from My Items, so the line counts as new) → skip;
  - exists in **Dismissed** → skip, and say so in the scan result with a pointer to the Dismissed tab (decided);
  - matches nothing → make a new pending item, exactly as a first scan would.
- **Example (yours):** TV kept in My Items, HDMI cable permanently deleted. Rescan: the TV matches and is skipped; the cable matches nothing and comes back to New Items. If the TV was deleted too, both come back. If nothing was deleted, nothing is added, as today.
- **After the scan the person is told what happened:** "Added 1 new item. 2 were already tracked." A scan that adds nothing says "Everything on this receipt is already tracked", not an error.
- **Matching tolerance.** A model reads the same page slightly differently on a second pass, so a match is the same receipt key and the same price with the same model number or a close name (the existing brand and name tidying is reused). Two identical lines on one receipt are counted, not collapsed: a line matches at most one existing item. The tolerance is tuned on the sample receipts (read twice).
- **Existing rows** get a line key by migration from what they already store (model number, name, price). A row too thin to match is left alone; the worst case is one duplicate a person can delete.
- **The email path** (`PendingItemService.Email.cs`, which has its own item loop) and the order-key join in `FillAndSaveAsync` use the same per-line matching, so a forwarded copy of a deleted line also comes back.

## Steps
1. **The rule and its words (no behavior change).** `TrackingHint`, `tracking-signals.json`, `TrackingOptions`; table-driven unit tests from the `judgment` and `sure` lines of the sample answer key.
2. **Let more lines through.** `ReceiptProducts.Parse` keeps `consumable` lines when the receipt has at least one product or repair line; they carry their kind and get `kind` confidence 0.3. The 12-line cap stays; a receipt over it keeps the highest-priced lines first and says how many were left out. Update the tests that assume consumables are dropped.
3. **Record the signals.** Columns, an EF migration, filled in `ApplyReadingAsync` / `AddOtherProductsAsync`, and in the email path (`PendingItemService.Email.cs`).
3b. **Per-line identity and partial rescan.** Add `ReceiptKey` and `LineKey` to the pending item, replace the `#N` position keys, and change the duplicate decision from the whole receipt to each line (see "Rescanning after a delete"). The upload and forward responses report how many lines were added and how many were already tracked. Tests: delete the cable and rescan adds only the cable; a kept TV in My Items, in Waiting, and in Dismissed is never duplicated; delete both and both return; a TV deleted from My Items after being accepted counts as new; rescanning an untouched receipt adds nothing; two identical lines; lines in a different order; a missing line; a different account's copy is never matched.
4. **Expose the verdict.** `TrackHint` and `TrackReason` on the pending item contract; computed in the list endpoint from the stored signals and the current option. Nothing is hidden server side.
5. **Show it.** `new-items.page.ts` sorts `Unlikely` rows into a collapsed "Smaller things (N)" group, each with its reason and a "Track this" button (the normal add). `Unsure` rows stay in place with the reason. Quick add keeps its own gate (a name, no values under the check line), so a low-confidence consumable asks for a look first.
6. **Bulk removal.** `POST /api/pending-items/dismiss` (a list of ids, one undo token); `DELETE /api/pending-items` with a list of ids, only for items already dismissed (anything else is refused); `DELETE /api/pending-items/dismissed` to empty them all. UI: checkboxes and a selection bar on both tabs, a batch Undo toast for Dismiss, confirm dialogs for permanent delete and Empty dismissed. Tests: a delete refuses a waiting item, delete and empty are scoped to the caller's account, and one account cannot delete another's.
7. **Plans.** When S2.4.7 lands, the "line just before" pairing above; until then the rule takes a `covered` flag that is always false.
8. **One definition with the labelled set.** Point the answer-key generator at `tracking-signals.json` and the same verdict rule (no first-product exemption); have the read eval (S2.4.3) report `judgment` lines separately from `sure` lines.
9. **Tidy up** (house rule): keep the table-driven unit tests and the bulk-dismiss tests; drop any one-off agreement check against the whole CSV or make it opt-in. Say in the summary what was added to prove it and what was removed.

Later, in S9.8.5 itself: the settings control and its audit entry, the "lower the amount?" prompt, per-person storage.

## Decisions still open
1. **Settled:** a permanently deleted receipt or line can come back by rescanning (no kept key); lines still in New Items or My Items are not duplicated.
1b. **Settled:** a line that is in Dismissed when the receipt is rescanned stays there, and the scan result says so ("1 line is dismissed; restore it from the Dismissed tab"). This keeps S9.9.4's rule that a dismissed receipt does not come back by itself.
2. **How many low-confidence extras per receipt.** With consumables let through, a long hardware receipt (the 12-line sample) would make up to 12 pending items, each with its own copy of the receipt pages and its own processing. Suggested cap: 6 extras beyond the receipt's products, highest price first, with a note on the rest. Say if you want a different number.
3. **Quantity and currency** are as before: the rule uses the line price, and the amount is dollars until S9.8.3.

## Risks and how they are contained
- **A good item gets demoted.** It stays in New Items, one click from added, with its reason shown. Zero turns the rule off.
- **Clutter from the extra lines.** They sort last, collapsed, and multi-select Dismiss clears a batch in one action.
- **A plan separated from its item.** Pairing is made before sorting, and the item a plan covers is not demoted on price.
- **Config drift between the app and the labelled set.** Both read `tracking-signals.json`.

- **A rescan reads differently and duplicates a kept item.** Matching uses price plus model or a close name, and is tuned on the sample receipts read twice; a duplicate is one delete away.
- **A rescan misses the line the person wanted back.** Only if it matches a kept item of the same price and similar name, which is the case the rule is for.

## Not changed
The reader prompt, store, brand and policy matching, dismissal retention rules, and grocery-only receipts (still make nothing).

## Story text to amend when this is built
- S9.8.5 says "pre-ticked on a quick add". The app has no pre-tick; reword to "sorted below the rest and marked, with quick add unchanged".
- S9.8.5 names "the main item on a receipt" as always tracked. Drop it; the verdict above does not need it.
- S2.2.4 (de-duplicate forwarded receipts) and S9.9.4 change from "the same receipt does not come back" to per-line matching, with the rescan rules above.
- S9.9.4 and S9.9.1 gain multi-select Dismiss, multi-select permanent delete on the Dismissed tab, and Empty dismissed.

## Built 2026-10-19: steps 2, 3 and 3b (API and UI; not committed)
- **Step 2.** `ReceiptProducts.Read` keeps consumable lines when the receipt has at least one product or repair (a receipt of only consumables still makes nothing). Cap: 12 lines, products and repairs first, then at most 6 consumables, dearest first; the rest are counted (`leftOut`). A consumable gets `kind` confidence 0.3 (repair 0.4), so Quick Add waits and naming the item clears it. The reader prompt is now `document-v10`: a consumable also gives its name and price (the rule needs a price to judge). The first-product scalars are not applied to a consumable that is printed first.
- **Step 3.** `PendingItem` gains `LineKind`, `LargestLine` and `SmallPartWords` (filled by `ApplyReadingAsync`; the line price is `ItemPrice`). Migration `ReceiptLineIdentity`, applied to the dev and test databases.
- **Step 3b.** `ReceiptKey` (the order key, else the file or email key) and `LineKey` (model number, else name, with the price in cents; a second identical line gets `:2`). The `#n` position keys are gone: a second line's `DedupeKey` is the receipt key plus a hash of its line key. A receipt of several lines is decided line by line (`PendingItemService.Lines.cs`): a line already waiting, in My Items (while its purchase still has an item), or in Dismissed is not made again; a deleted one comes back. Matching is by line key, else by model number, else by the words of the name (`ReceiptLineIdentity.Same`), with a price on both sides agreeing to the cent. A waiting line met again on a receipt it does not hold gets the receipt's pages and fills what it lacked. The first line still to be made takes the upload's own item. Upload and forward responses carry `alreadyTracked`, `dismissed` and `leftOut`; New Items says so ("3 lines were already tracked", "everything on this receipt is already tracked"). The migration writes keys for existing rows (a `LineKey` only for receipts that made several items). Single-line receipts keep the whole-receipt rule (same file again = duplicate).
- **Not done yet:** steps 4 to 9 (verdict on the list, "Smaller things", bulk Dismiss and permanent delete, plans). A line deleted from the database by hand is the only way to test the "comes back" case until step 6 exists. An email's lines carry no price, so an email line and a receipt line of the same order meet only when the names share at least two words.

## Added 2026-10-19: groups by coverage, and a unit-price check
- See S9.2.10 "The groups": Covered, Return window only, Coverage ended, Needs you, Smaller things. Needs you shows in New Items and in My Items (Quick Added but unfinished), highlighted with the return window's closing date.
- New plan step (before step 4): confirm the reader gives the unit price, not the extended line total, for lines like "2X4X8 STUD x24 110.16". The small-item threshold must test the unit price. Sample 12 (Pine Street Hardware) is the check.
- Step 5 (the list) shows the Needs-you highlight; steps 6 and S9.2.10 share the multi-select and bulk endpoint shape.

## Two values on a line: warranty value and return value (added 2026-10-19; replaces the unit-price note above for the threshold)
A line has two reasons to be tracked, and they use different numbers.
- **Warranty value** uses the unit price, because warranties are per unit. It decides whether a warranty is plausible and so whether to ask the person about one. Wooden studs have none, so they are never asked.
- **Return value** uses the whole line total, because a return takes back the whole line. 24 studs at 110.16 is worth recovering if a project is cancelled, even though no warranty applies.
- The minimum is tested against the line total for severity (what is at stake), and against the unit price only for "is a warranty plausible".
- A consumable at or over the minimum is a return-only item: it carries only the store's return window, shows in the main list as "Return window only" until the window closes, and its highlight reads "return window closes in N days, 110.16 to recover" instead of "warranty unconfirmed". It is not blocked in Quick Add for a missing warranty; the person only confirms the name.
- A consumable under the minimum goes to Smaller things as before.
- When the return window closes, the return value is gone. A return-only item then has no coverage left and is archivable (S9.2.10).

Update 2026-10-19: the rules this plan relies on now live in S9.2.11 (per-person minimum, line total versus unit price, return-only items, colours, Dismiss confirmation). Where this plan says one threshold for the account or unit price for the test, S9.2.11 and S9.8.5 take precedence.

## Built 2026-10-19: steps 3.5, 4 and 5 (New Items part; not committed)
- **Step 3.5, quantity.** The reader prompt is `document-v11`: each line also gives `quantity` (a whole number, 1 when none). `ReceiptProduct.Quantity` and `PendingItem.LineQuantity` keep it. The line price stays the whole line; the unit price is price over quantity. Not yet exercised against the live model, so whether it reads "x24" correctly on sample 12 is still to be seen.
- **Step 4, the verdict.** `ApplicationUser.TrackingMinimum` (null = the app default, 50; 0 = track everything) with `GET/PUT /api/me/tracking`. `AttentionRules.Judge` (pure) gives each waiting item a level (error, warning or none), return-only, unit price, and the `TrackingHint` likelihood and reason, from the person's minimum against the whole line. `PendingItemDto` carries `attention`, `returnOnly`, `quantity`, `unitPrice`, `trackHint`, `trackReason`, `trackingMinimum`; `GET /count` also returns `needsAttention`. Migration `TrackingMinimumAndQuantity`, applied to the dev and test databases. A new household member does not yet copy the owner's value (invites, S1.3.4, are not built).
- **Step 5, New Items.** Rows are tinted by level with an icon and words; lines the rule calls unlikely sit in a collapsed "Smaller things (N)" with their reason and a Track this button; the nav badge counts error-level items only. My Items rows tint warning for needs-info and may-be-covered, and soft blue for expiring soon.
- **Not done:** the My Items error escalation (needs the return window's closing date and the minimum on the item rows); the "closes in N days" wording and the urgent last week (New Items has no return-window date yet); the Dismiss confirmation and "Select all" skipping high-value items (step 6, with multi-select); the settings control for the minimum (S9.8.5 UI); the digest line (S4.2.1); the archive view (S9.2.10).
