# Sweep: a data export expires after a week

**Needs:** the simulated clock and key. **Account:** Alice (a scenario reset is fine). **Time:** 5 min. API calls only, signed in as Alice.

## Setup
1. Read Alice's account id from the `account_id` claim of her access token. Call it `A`.
2. `GET /api/maintenance/clock` and note the offset (should be 0).

## Steps
| # | Call | Expected |
|---|---|---|
| 1 | `POST /api/exports` (as Alice) | 202 with an export `id`, status `queued` or `building` |
| 2 | `GET /api/exports/{id}` every few seconds, up to a minute | status becomes `ready`; `expiresAt` is about 7 days after `readyAt` |
| 3 | `GET /api/exports/{id}/download` | 200, a zip |
| 4 | `POST /api/maintenance/clock/advance?days=8` | clock moved |
| 5 | `GET /api/exports/{id}/download` | **404**: expired even before the cleanup has run |
| 6 | `POST /api/maintenance/run-export-expiry?accountId=A` | exactly `Expired 1 export(s).` |
| 7 | `GET /api/exports/{id}` | status `expired` |
| 8 | `POST /api/maintenance/run-export-expiry?accountId=A` again | `Expired 0 export(s).`: nothing is expired twice |
| 9 | `POST /api/maintenance/clock/reset` | offset back to 0 |

A step 6 answer other than 1 is a Fail (0 means the sweep missed it; more than 1 means Alice had an older export, so say so and clear her exports first).
