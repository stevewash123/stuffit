# Push 105: policy sources are rechecked every 90 days (API c593687, UI 0194421)

## What changed
1. **Drill-down text**: the panel's date line now lists the latest check of each kind: "Admin verified 9/1/2026, AI confirmed 12/1/2026" (and, once 2+ accounts agree, "3 accounts' uploads 12/5/2026"). A policy that has only been read by the AI shows "AI confirmed <date>".
2. **Recheck note**: if the last recheck found the company's page changed or unreadable and nothing has confirmed the terms since, the panel adds "On <date> the company's page changed or could not be read, and these terms have not been re-confirmed. Please check them with the company." An "administrator reviewed" policy in that state shows as "AI verified" instead.
3. **A daily job at 02:00 UTC** ("recheck-policy-sources") rechecks every shared policy's source page every 90 days. Same page as last time: confirmed again with today's date, nothing read. Changed or new page: the AI reader reads it; same terms = confirmed again, different terms or unreadable = flagged for a person (never confirmed, terms never edited). Capped at 200 policies and 40 AI readings a day. New table `policy_source_checks` (migration PolicySourceChecks).

## What to check
1. Drill-down: open a ski policy's shield: it reads "AI confirmed 11/13/2026" (no admin line, no recheck note yet).
2. Nothing else on screen changes. Existing coverage, reminders and exports are unaffected.

## Not testable through the app (Not tested, please do not mark Fail)
The sweep itself has no screen or API call; it runs on the schedule (Hangfire dashboard is local-only). It is covered by an automated test against the database (quiet repeat, changed page, unreadable page, AI budget). The first real run happens after the 02:00 UTC job on Staging; if you want to look afterwards, `SELECT outcome, needs_review, count(*) FROM policy_source_checks GROUP BY 1, 2;` shows what it did.
