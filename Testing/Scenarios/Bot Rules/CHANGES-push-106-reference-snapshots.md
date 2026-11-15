# Push 106: reference-data import and export groundwork (API 40b8cb6, no UI change)

## What changed
Nothing a person sees in the app. This is data plumbing (story S7.5.7), and it changes what the command-line reference import prints and what the database holds.
1. **Import report**: `--import-reference` now prints, per kind, "inserted / updated / unchanged" instead of "inserted / already present". A second run of the same files must say inserted 0 and updated 0.
2. **Overlap clash fixed**: a file's manufacturer policy that overlaps an existing policy's purchase window (for example a hand-loaded one with an open window) is no longer inserted and no longer fails the run. The existing row stays and a "kept the existing policy" note is printed.
3. **New command**: `--export-reference <folder> --version <tag>` writes `reference-snapshot-<tag>.json`, in the same shape the import reads. It only reads the database.
4. **Crawl status and page fingerprint**: companies can carry how the last crawl went (found_read, no_website_found, website_unreadable with a reason, no_policy_published) and a date. A policy's source page can carry a content hash; a different hash on a later load records a "needs review" check (the terms are not edited, and an administrator's check shows as AI verified until someone looks).
5. **Migration `ReferenceCrawlTracking`** adds 4 columns: `parties.crawl_status`, `crawl_reason`, `crawled_at` and `policy_evidence.content_hash`. It runs when the API starts on Staging.

## What to check
1. After the API restarts on Staging: the site still loads and sign-in works. Nothing on screen should differ from push 105.
2. Read-only SQL: `SELECT column_name FROM information_schema.columns WHERE table_name='parties' AND column_name LIKE 'crawl%';` returns 3 rows, and `policy_evidence.content_hash` exists.

## Not testable through the app (Not tested, please do not mark Fail)
The import, export and overlap handling are command-line only and are covered by automated tests against the database. There is no screen or API call for them.
