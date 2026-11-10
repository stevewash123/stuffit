# Push 59: asking for service on a plan, and the push 58 fix (2026-11-10)

Story S3.4.8, first slice. API and UI. Migration `PlanServiceRequests` (new table plan_service_requests).

## Push 58 fix: a linked line no longer keeps an age estimate
| Change | What to check |
|---|---|
| Picking an item on a plan line hides "About how old, in years" and sends no estimate | Add or Change a line: choose an item you own. The estimate field disappears; clear the item and it returns. Saving a linked line stores no estimate (export `plan_lines.csv` "age years" is empty for it) |
| The lines card blurb reads the same on any plan | "What the contract lists as covered, with the limit and age limit it states..." (not home-warranty wording on a phone plan) |

## Asking for service (S3.4.8)
| Change | What to check |
|---|---|
| An **"Asking for service"** card on every plan page, under the lines card | Has "What to have ready when you ask": the claim phone (tappable), website, contract number, service fee ("$75.00 a visit") and, on a plan inside its waiting period, "You are inside the waiting period. Claims can start <date>". A plan with none of those says to add them |
| **Record a request** | Day (defaults to today), what broke (required), which line of the plan, which item you own, who they sent and their phone, the service fee you paid, what the company decided (Waiting to hear / Covered / Partly covered / Denied), what the company paid or replaced, follow up. For Denied or Partly covered the form also asks for the company's reason in their words and the contract text it points to |
| The request list | Newest first: what broke, a decision badge, the day, the line or item, who was sent, fee paid, what the company paid, their reason, the contract text, follow up. Change and Remove (Remove asks first) |
| **Plan year counts** | "N requests this plan year" and, when the plan states a claim cap (Phone or device insurance: "Claims allowed in 12 months"), "1 of 2 claims used; resets <date>". The plan year starts on the plan's anniversary. Also "fees you paid $X" and "the company paid $Y" when there are any |
| **Past the cap is flagged, not blocked** | With a cap of 2, record three requests in one plan year: the third saves and shows "This was past the plan's limit of 2 claims a year. It may not be covered. Check the contract." |
| **A line's limit used** | Give a line a limit (say $2,000). Record a Covered request for that line with "what the company paid" $180: the line shows "limit $2,000.00, $180.00 of it used this plan year". A Denied request adds nothing; a request in an earlier plan year is not counted |
| Bad input | A request needs a name for what broke; a negative fee or amount, a future day, a line or item that is not the plan's are refused with a message |
| The export | `plan_service_requests.csv` is in the zip and listed in README.txt |

## Not built yet (do not report)
- Joining these requests to a general claim log or to Money recovered, attaching photos and the company's email to a request, the claim wizard offer on a denial, adding fees to the "what the plan cost me" figure on the plan decision panel, and "Request service" from a single line's row (the card is on the plan). Home appliance plan extras (Add to your plan? for a new item, replacing an appliance under the plan, the cost view) are next.
