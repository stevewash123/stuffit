# What changed in push 45: maintenance the warranty asks for, and reminders (2026-11-09)

For GrokBot. Check `/api/version` against the pushed API commit (UI changed too). **New migration `MaintenanceRequirements`** (one new table, `maintenance_requirements`; Render migrates on start). No `--seed`. Retest S68 with a warranty paper that lists required maintenance. The reader prompt changed (item warranty v7), so reading a warranty paper on a vehicle is a live-reader check.

## New: Maintenance on a vehicle, with reminders
- **From the warranty paper.** Read it on a vehicle's warranty now also picks up upkeep the paper says the owner MUST keep up to keep the warranty valid (for example an oil change every 7,500 miles or 12 months). It leaves out maintenance the paper only recommends. After applying, the result says "It asks for N kinds of maintenance to keep it valid". Reading the same paper again replaces what it gave and adds no duplicates; anything the owner typed in stays.
- **Maintenance panel on the vehicle page** (under Service history): each requirement with how often, where it stands (On track, Due soon, Overdue) and why: "Last done Aug 15, 2025 at 9,800 miles. Next due by Aug 15, 2026 or 17,300 miles, whichever comes first." In edit mode you can add your own (what, every miles, every months) and delete one. An empty vehicle shows the panel only in edit mode.
- **It works out the due date from the service history.** A repair order you add to the Service history (a matching job, for example "Engine | Oil and filter change") restarts the count from that visit. With nothing done yet it counts from the day the coverage started, using the odometer reading at purchase. Time or distance, whichever comes first; a distance is turned into a day only when two readings give a pace. Due soon is 30 days out, or within 10% of the interval (at most 500 miles) of the distance.
- **Reminders.** A new notification type, **Maintenance due** (email and in the app, in the preferences grid), tells the owners when a requirement is coming due, and again when it goes overdue: each stage once per cycle, at the owner's local time. Adding the service settles it, and the next stage starts from that visit. Nothing here changes a coverage.
- **Export:** `maintenance.csv` (task, distance, months, whether it came from a paper).

## Also fixed from the push 44 report
- **Left-out count (S68-04):** the reader is now asked to list no-charge jobs, shop supplies and disposal or environmental fees too, so the cabin air filter, the 10k inspection and the shop supplies are all counted: "3 other jobs were left out" (service record v3).
- **Coolant diagnosis:** coolant, antifreeze and thermostat work now goes to the powertrain term with the other cooling work, not the bumper-to-bumper.

## What to try in S68
- Read the Honda warranty on the CR-V. If the paper lists required maintenance, the Maintenance panel fills in; if it lists none, add "Engine oil and filter change, 7,500 miles, 12 months" by hand.
- With the four repair orders already in the history, the oil change should show the last visit (Aug 15, 2025 at 9,800) and the next due date counted from it, and the CVT fluid job should settle a "Transmission fluid service" requirement.
- Report any requirement the reader invents that the paper does not state, or any required maintenance it misses.

## Not changed, do not report
- The text-message opt-in is still to come; maintenance reminders go by email and in the app only.
- A repair order that does not name a task the same way (for example "Lube, oil, filter" for "Engine oil and filter change") may not match; the match needs the words that name the job. Report any real order that should have matched and did not.
- Low items from push 43 (Edit drawer Cancel, Read it before saving on Add) and the powertrain narrative (P41-3) are unchanged.

## Tests at push
API unit 1231, integration 514 (+2 opt-in skipped), reference suite 278 passed on the merge; UI 1371. Added: the due-date rules (7 tests), maintenance parsing, a reminder test across the whole cycle (not yet due, coming due, rerun the same day, overdue, settled by a service), add/edit/delete and the vehicle-only rule, a warranty paper that lists maintenance (once, owner's own kept), the export file, and three component specs.
