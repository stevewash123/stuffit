# What changed in push 44: fixes from the push 43 report (2026-11-09)

For GrokBot. Check `/api/version` against the pushed API commit (UI changed too). No migration, no `--seed`. The reader prompt changed (service record v2), so the first two items are live-reader checks. Retest S68 step 5 and the two-tab sign-in race.

## Fixed from the push 43 report
- **"N other jobs were left out" (S68-04):** the reader is now asked for every job on a repair order, and the app decides which are on a covered part. Cabin filter, inspection, shop supplies and the like are listed as left out ("3 other jobs were left out") instead of vanishing before the app sees them. Inspections, shop supplies, disposal or environmental fees and taxes are never kept as service on a covered part.
- **Which coverage covered a job:** a coverage is now named with the day it ends, for example "Manufacturer warranty (to Nov 8, 2027)" and "Manufacturer warranty (to Nov 8, 2029)", so two terms from one maker are told apart. When two whole-vehicle coverages are not named, engine, transmission, drive and cooling work goes to the longer one (the powertrain) and everything else to the shorter (the bumper-to-bumper).
- **Two-tab sign-in race (and the unexplained redirect at +75s):** a refresh token that was rotated out a moment ago and shows up again within 30 seconds (the second tab, or a request that raced a reload) now gets a fresh session of its own instead of ending every session. A rotated-out token presented after 30 seconds is still treated as theft and ends all sessions. Retest: reload two tabs at the same moment; both should stay signed in.
- **Back after sign-out shows old pages:** a page the browser restores from its back/forward cache is now loaded again, so a signed-out person who presses Back lands on the sign-in page, not on the last person's items.

## Not changed, do not report
- **Odometer in, not out:** the service history and the reading use the mileage **in** (20,800), not mileage out (20,802). That is the reading when the car arrived, and it is what the reader is told to take. The S68 answer key's 20,802 is the same visit; please treat 20,800 as correct.
- **Powertrain narrative (P41-3):** still waiting for the screen and the exact words.
- **Low, not done:** the Edit drawer has no Cancel (only the X); Read it does not run on files attached in the Add a vehicle form; a repair order uploaded twice is stored twice.

## Tests at push
API unit 1222, integration 511 (+2 opt-in skipped); UI 1368. Added: two-whole-coverage and shop-charge rules, a shop-supplies job in the repair order test, a rapid-reuse refresh and a back/forward-cache spec. Updated: the refresh-token reuse test now ages the old token past the 30 second window before it checks that a stolen copy ends the session, and also checks that an immediate reuse is accepted.
