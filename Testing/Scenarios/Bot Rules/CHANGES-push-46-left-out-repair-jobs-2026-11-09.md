# Push 46: left-out repair-order jobs can be added anyway (2026-11-09)

Applies to a vehicle with a repair order read on the item page ("Service on covered parts" card).

| Change | What to check |
|---|---|
| The card lists each job the rules left out, each with a tick box | Tires, wipers and shop supplies on the Honda order show as unticked rows under "N other jobs were left out" |
| Ticking a job shows a coverage picker (default "No coverage (history only)") | Pick Powertrain for one job, leave another on none |
| The Add button counts the ticked jobs ("Add to service history, with 2 left-out jobs") | Confirming adds the normal entries plus the ticked ones; ticking nothing behaves as before |
| Entries added this way read "added by you" in the Service history list | Not shown on entries the rules kept |
| An order with only left-out jobs (and no odometer) now still offers the card, so a job can be added | Before, it said nothing on this order was service on a covered part and offered nothing |

Not changed: which jobs are kept or left out by default. Nothing is saved until Add is pressed. A coverage id that is not on this vehicle is ignored.

New column: `service_entries.added_anyway` (migration ServiceEntryAddedAnyway). It is the record of a miss: those rows are the jobs the rules got wrong, to read when deciding whether a word belongs in `ServiceRecordRules.cs`.
