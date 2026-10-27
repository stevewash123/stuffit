# Card policy worklist (written 2026-10-01)

Seed rows live in `StuffIt_API/src/StuffIt.Infrastructure/Seed/reference-data.json` (`cardBenefits`). Re-run `--seed` after adding rows; it only inserts.

## Seeded, with an issuer source URL (12 cards)
| Card | Benefits seeded | Check before launch |
|---|---|---|
| Chase Sapphire Preferred, Freedom Unlimited | EW, PP (earlier seed) | |
| Chase Freedom Flex, Freedom Rise | EW 12/48, PP 120d $500 | read from Chase's Freedom benefits page (covers Flex, Unlimited, Rise) |
| Chase Sapphire Reserve | EW 12/48, PP 120d $10k, RP 90d $500/$1k yr | read from Chase's SR page; confirm against the Guide to Benefits PDF (SR changed in 2025) |
| Amazon Prime Rewards Visa Signature | EW 12/48, PP 120d $500 | read from Chase's Prime Visa page |
| Amex Gold (earlier), Amex Platinum | EW +12, PP 90d, RP 90d $300/$1k | Amex pages are script-rendered; terms came from search snippets of americanexpress.com pages, not a page read. Open each URL once to confirm |
| Citi Double Cash | EW doubles up to 24 months (orig. 24 or less), $10k | terms came from a search summary of Citi's Mastercard guide PDF; the PDF itself would not load. Confirm |
| Citi Strata Premier | EW +24, up to 7 yrs, $10k | same: summary of Citi's guide, PDF not read |
| Capital One Venture X, Costco Citi (earlier) | EW | |

PP = purchase protection, RP = return protection, EW = extended warranty.

## Researched, nothing seeded
- **Wells Fargo Active Cash:** the official Guide to Benefits lists cell phone protection, auto rental, travel and concierge. **No extended warranty, purchase or return protection.** (Cell phone protection is not a benefit kind we model yet.)
- **Discover it (all):** Discover dropped purchase protection, return guarantee and extended warranty in Feb 2018. Secondary sources only; confirm on discover.com.
- **Capital One Venture, VentureOne, Savor, SavorOne, Quicksilver, QuicksilverOne:** Capital One's help page says they have extended warranty but gives no terms ("depend on your card"). Per secondary sources it doubles a warranty of 24 months or less, up to $10,000 per claim. Need the Cardholder Benefits Guide per card (Discover network) from the account.
- **Citi Custom Cash:** reported (Doctor of Credit, FrequentMiler) to match Double Cash. Need Citi's Mastercard guide.
- **Bank of America Customized Cash:** secondary sources say a Visa Signature extended warranty (+1 year, warranties of 3 years or less). Need the BofA benefits guide; confirm the card is Visa Signature, not Mastercard.

## Not yet researched from the top 20
Amex Green, Blue Cash Preferred, Blue Cash Everyday, Citi Strata Elite, Chase Freedom Unlimited return protection (none stated).

## Pattern notes
- Chase tiers share one pattern: EW +1 year (to 4 yrs total), PP 120 days; only the per-item cap changes ($500 vs $10,000 on SR).
- "No benefit" is a fact worth recording (Wells Fargo, Discover). The data model has no row for it; the card page shows "No policies on file", which reads the same as "unknown". Consider a `no_purchase_benefits` flag on `card_products`.
