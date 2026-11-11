# Push 63: Push 62 fixes, and asking for service from a line (2026-11-11)

API and UI. No migration. Stories S3.4.8, S3.4.20.

| Change | What to check |
|---|---|
| **Delete-request dialog mentions the files** | Plan > Asking for service > remove a request: "... is taken off the record, along with any photos and papers attached to it. The plan itself stays." |
| **Export ids tell things apart** | The ids in export folder and file names are now the last 8 characters of the id (the first 8 were the same for anything made together). Plan folder, request folder and file prefix now differ. Applies to all export folders (purchases, insurance, plans, requests). File names keep their id prefix so two files with one name never collide |
| **Ask for service from a line** | Plan > "What it covers, line by line": each line the contract covers has **Ask for service**. It opens the request form on the Asking for service card, scrolled into view, with that line (and its item, if linked) already chosen. Lines the contract leaves out have no button. Pressing it again resets the form for that line |

## Not built yet (do not report)
- Joining requests to Money recovered, the claim wizard offer on a denial, the phone-insurance cost view, the three-layer explanation, a person adding their own plan type, receipt-to-plan-type matching, a seeded provider list.
