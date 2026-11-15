# Reference data write contract (for WebCrawler1 and PolicyPublisher)

Story: S7.5.7. The master reference database is written only by the crawler pipeline, and every deployment loads a versioned snapshot of it. Records use the `reference-data/*.json` shape (the same one `--import-reference` reads and `--export-reference` writes).

## What you write, per record
- **Company** (`parties[]`): `name`, `roles` (seller, manufacturer, cardIssuer, warrantyProvider), `website`, and for a store `returnsUrl` and `supportUrl`, for a brand `claimUrl` and `claimPhone`.
- **Crawl status** on every company you tried, even when you found nothing:
  - `crawlStatus`: `found_read`, `no_website_found`, `website_unreadable`, or `no_policy_published`.
  - `crawlReason`: required with `website_unreadable`: `pdf_only`, `blocked`, or `login_wall`.
  - `crawledOn`: the date (yyyy-mm-dd). A newer crawl replaces an older one; an older one never replaces a newer one.
  - Not-found is a real record with a date, not a missing record.
- **Policy** (`sellerPolicies[]`, `manufacturerPolicies[]`, `cardBenefits[]`): the terms, plus `sourceUrl` (the page you read), `official: true` and `verifiedOn` (or `officialOn` for stores) when you read the company's own page, and `contentHash`: the SHA-256 of the page's normalized words (64 hex characters).
- Set `confirmed: false` when you could not match the terms to the page. Such a policy has no source and is not shown as coverage.

## What you never write
- No "User confirmed" or "Reviewed by WarrantyCat administrator". Those exist only inside a deployment.
- No placeholder or invented values. If you do not have a number, leave it out.
- Nothing an account owns, and nothing for regions outside the US.

## What happens on the other side
- A policy is matched by company + category + product line + model list + purchase window. If your row overlaps an existing one's window, the existing row is kept and the run prints a note.
- The same `contentHash` again changes nothing. A different one means the page changed: the policy is marked for review in each deployment (an administrator's check drops back to AI verified), and the terms are not edited until you publish new terms.
- A second load of the same snapshot reports 0 inserted and 0 updated.

## Recheck
Every 90 days (tunable). Compare the page's hash first; only a changed hash needs a new read.
