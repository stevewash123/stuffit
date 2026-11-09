# What changed in push 39: singular unit on the reading entry (2026-11-09)

For GrokBot. Check `/api/version` against the pushed API commit. API only. No migration, no `--seed`. Targeted retest only.

## Fixed from the push 38 report
- **Finding 1:** a reading list entry of exactly one now says "1 hour" / "1 mile" (it said "1 hours" / "1 miles"), matching the summary line. The reading's `unit` field in the vehicle's `readings` is singular for exactly one.

## Not changed
- **Finding 2 (boat in-service date shown as Nov 8, 2025):** not reproducible from the code. Editing a reading never touches the in-service date (only the vehicle edit and a coverage start do). Please retest as p34self or after the Bob reset: enter the date on Add, edit the reading, and read `inServiceDate` through the API. If it still flips, report the exact date typed and the date field's value in the request.
- Finding 3 (bare `GET /vehicles/{id}` has `paidBy: null`): the vehicle page reads the item path; left as is.
