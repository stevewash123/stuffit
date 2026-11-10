# Push 53: Scenario 69 leftovers, and the push 52 Medium (2026-11-10)

API and UI. No migration. The reader prompt for repair orders changed (service-record-v5), so **read order 08 again**.

## Push 52 Medium: a hand-added job is merged even when it is worded differently
| Change | What to check |
|---|---|
| Re-adding an order replaces a hand-added ("added by you") row with the rules' copy of the same job even when the words differ | F-150 order 06: the hand rows "Rear tire: Flat repair - plug/patch ... billed to road hazard plan" and "Tires: Rotate & balance - lifetime (no charge)" are replaced by the rules' "Rear right tire: Flat repair plug/patch (nail in tread)" and "Tires: Rotate & balance (lifetime, original invoice 08-552190)". Each job once, none marked "added by you" |
| The same fuzzy match decides whether a left-out job is already added | Read order 06 again after adding the wiper blades by hand: wipers shows "already added by you" and stays hand-added (this is the "stay hand-added" check that had no fixture) |
| Two different jobs are not merged | "Rotate & balance" and "Mount & balance" on the tires stay two rows |

## Scenario 69 leftovers
| Change | What to check |
|---|---|
| A part has its own **Maintenance** panel | F-150 tire part page: add "Tire rotation, 7,500 mi". It is counted from the truck's service history and odometer: last done Feb 11, 2026 at 31,890 miles (order 06's rotation), next due by 39,390 miles. A toaster or other non-vehicle item still cannot be given maintenance |
| The shop's wording meets the paper's | "Tire rotation" matches "Tires: Rotate & balance" and "Rotated tires"; it does not match a flat repair or wipers |
| Each **kept** job on the card has a tick box; untick one and it is not saved | Order 12 (Outback): untick the CVT service, Add: only the rest are saved. "Untick a job that should not be kept." sits under the list |
| Order 08 (body shop collision repair, Tucson) reads its jobs | Condenser, refrigerant, labor and sublet lines appear as jobs (kept or in "N other jobs were left out" with tick boxes). Before, the card listed none. Read it again, because the prompt changed |

## Not done (do not report as new)
- The Low items not listed above. Plan types, phone and home appliance plans are later pushes.
