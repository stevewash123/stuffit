# Spec for CC: shared WarrantyCat reference database

## Goal
One master reference database holds the public facts about stores, manufacturers and credit cards. Crawler bots fill it in. Every WarrantyCat/StuffIt deployment (Dev, alpha, later production) gets a versioned snapshot of it through the existing idempotent `--import-reference`. Deployments never read the master live.

## Architecture
- **Master:** a new Neon project, `warrantycat-reference`, with reference tables only and no accounts. The crawler pipeline is the only writer: WebCrawler1 crawls, and PolicyPublisher writes proposals and approved rows.
- **Publish:** an export command writes a versioned snapshot (the `reference-data/*.json` format or a successor) tagged with a version and date.
- **Consume:** each deployment runs `--import-reference <snapshot>`. That covers reseeding a deployment, and each deployment can pin a version, so QA can test against a known one.
- **Why not live reads:** a bad crawl would hit every site at once, every deployment would need a second connection string, and Dev and alpha would no longer be isolated.

## Stable identity (required)
- Every company, category, card and policy has a stable natural key or ID that is the same in the master and in every deployment.
- The import upserts by that key. It never duplicates a row, and it never trips the overlap constraints. Today's clash with `ex_manufacturer_policies_no_overlap` against hand-loaded rows is the case to design out.
- A second import of the same snapshot inserts 0 and updates 0.

## Data to gather
### Stores
- **Return policy:** window in days, what starts the clock (purchase or delivery), holiday extensions, and category exceptions (electronics, opened items, final sale). Also restocking fees, receipt or proof-of-purchase rules, and whether a return gets a refund, store credit or an exchange.
- **Warranty-related:** price adjustment or price match windows, store protection or extension plans, and membership benefits.
- **Where to start a return:** the return portal URL, phone number, whether in-store returns are accepted, and return-by-mail instructions.

### Manufacturers
- Warranty length by category or product line, what's covered, exclusions, whether registration is required, and whether the warranty transfers.
- Where to start a claim: claim page URL, phone and email.

### Credit cards
- Extended warranty (how much it adds and the cap), purchase protection, and return protection.
- The benefit administrator's claim URL and phone, and the guide-to-benefits URL.

## Tracking on every record
- **Sources:** source URL(s), capture date, and a content hash of each source page.
- **Crawl status:** `found_read`, `no_website_found`, `website_unreadable` (with the reason: PDF only, blocked, or login wall), or `no_policy_published`. Not-found results are stored as real rows with a date. They count as data and they show the gaps.
- **Source label:** the master only ever sets "AI verified from company website — please confirm this matches your item."
- **Recheck:** the starting interval is 90 days and can be tuned. A recheck compares the content hash, and only a changed hash triggers a re-read.

## Source status rules (per deployment)
- "User confirmed from multiple uploads" (2+ distinct accounts) and "Reviewed by WarrantyCat administrator" are only ever set inside a deployment.
- An import must never overwrite or downgrade those upgrades, unless the master marks the source changed (new content hash). In that case the policy goes back to AI verified, as in the earlier CC brief.
- A policy with no source isn't shown as coverage.

## Deliverables for CC
1. Schema for the master (it can reuse the app's reference tables, plus the crawl status, content hash and recheck fields).
2. An export command that writes a versioned snapshot.
3. Import changes: upsert by stable key, never downgrade, reset to AI verified when the source changes, and report inserted, updated and unchanged counts.
4. A one-time backfill of today's `reference-data` into the master.
5. A short note for WebCrawler1 and PolicyPublisher on the write contract (fields, statuses, how to report not-found).

## Out of scope for now
Regional variants (US only for now), live reads from deployments, and user-submitted data in the master.
