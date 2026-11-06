# What changed in push 30: the company's own returns or support page; a list-note fix (2026-11-06)

For GrokBot. API `bc78d21` and UI `0bb9a5b`. Check `/api/version` (`commit` must be `bc78d21`). Migration **`PartyCompanyLinks`** (five columns on `parties`) is applied to staging before this push. No reference seed change (no links were added to the data files: nothing is invented). Story S3.2.14.

## New (S3.2.14): a link to the company's own returns or customer support page
- A shared or private **store or brand** can carry two optional https links: a **returns page** (for a maker, its warranty-claim page, stored in the existing claim address) and a **customer support page**, each with the date it was last confirmed.
- **The finders suggest them** in the same visit as the policy (return-policy and warranty research), only if the link is https, on the company's own site, and the page opens without ending up on another site. Nothing is saved by a suggestion.
- **Operator screens** (admin Stores and Brands): the saved links show with their confirmed date and the page each was read from. The operator can add, change or clear a link; saving needs the page it was read on, and writes an official-source record. A later research round never changes a saved link.
- **Data files** accept `returnsUrl`, `supportUrl`, `linksSourceUrl`, `linksReadOn` (validated; filled only where empty; importing twice changes nothing).
- **In guidance** (the claim wizard result / how-to card): a return shows "Start with <store>'s returns page" and a second link "<store>'s customer support"; a maker's warranty claim shows "<maker>'s warranty and support page"; with only a support page it says "<company>'s customer support". With neither link known the card reads as before. Links open in a new tab. A link not confirmed for 12 months (or never) still shows with **"Check that this page is still current"**.
- A **private-sale seller** gets no links; a **not-returnable** store shows support only. A person can set a returns and support page on their **own private company** in the company edit form (never shared).
- The person's data export is unchanged.

## Steps to run
1. Admin > Stores: open a store with a website. Add a returns page (https, on the store's own site) with the page you read it on and confirm: it shows with today's date. Try an https page on another site: refused. Try http: refused.
2. Add a support page the same way. Clear one: it goes.
3. As a person, open the claim wizard for an item bought from that store (return option): the card shows "Start with <store>'s returns page" and the support link, both opening in a new tab. A store with no links: the card is as before.
4. A maker (Admin > Brands) with a claim address: the warranty claim option shows "<maker>'s warranty and support page". Brand with only a support page: "customer support".
5. Advance the clock more than 12 months (then reset to offset 0): the link still shows with "Check that this page is still current".
6. A private-sale purchase: no returns link. A store marked not returnable: support only.
7. Test1 sets a returns page on a private company they added: shown in their own guidance; Test2 does not see it.

## Fixed
| Where | What |
|---|---|
| My Items card note "Your own entry may be out of date" (push 26/28) | Now appears when **any** coverage of the item is superseded by a document-read one, not only when the coverage shown on the card is. Before, a typed 12-month warranty ending the same day as the document's 1-year one hid it (the card showed the document coverage). Retest: apply the standard appliance warranty document first, then add a typed Samsung 12-month warranty: the amber badge on the item page **and** the note on the item's card in My Items. Dismiss it with the X; reload and it stays gone |
| Start date from the item page To do card (your push 28 P26-3B path A) | The server and the page already finished the notification and refreshed the badge in our tests; we could not reproduce it. **Please retest on this build**: item page > To do card > save the date: the header unread count should drop and the Notifications page should show the "Enter the date" notice as done (no buttons). If it still fails, record which build commit you were on and whether the notification was one created before the item was reset |

## Corrections to the push 28 notes (our mistake)
- **S3.2.12 retest must use a maker that has no verified shared warranty for the item's kind.** A verified shared warranty wins the maker's headline slot over your typed entry (decided in push 28), so a maker like Cove or Whirlpool that has a verified policy shows only the verified one and never your typed one. That is not a failure. To see the typed offer, use a **maker with no verified policy** (a brand with only an unconfirmed or placeholder warranty, or a brand you add yourself that is on the shared list without a warranty). Then on a second item from that maker and kind, expect your typed 12 months offered, unticked, "Your own entry, typed in by hand; not checked against the maker's source."
- Sorting by confidence can only be seen where a verified or higher-confidence offer and your typed one are both offered (for example an item with a card extended-warranty benefit plus the typed maker entry): the higher-confidence offer is on top.
- The "Known" line in the push 28 notes (typed term offered ahead of a verified one) is wrong: the verified one wins.

## Not changed, do not report as new
Items listed under pushes 26 to 29 "Not changed".
