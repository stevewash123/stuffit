# What changed in push 27: parts on a vehicle, and part warranties counted by miles from install (2026-11-06)

For GrokBot. API `3b58d0e` and UI `0a2435c`. Check `/api/version` (`commit` must be `3b58d0e`); the UI has no version marker, so use the **Parts** section on a vehicle page as proof it is deployed. Migration `PartsOnAVehicle` must be applied to staging first (it is applied). Reference seed unchanged except `document-kinds.json` (reader fields, below).

## New (S3.5.5 and S3.5.6): run Scenario 62
- A vehicle page has a **Parts** list, **Add a part**, and **Link an item you already have**. A part is an ordinary item (its own purchase, receipt, coverages, people, reminders) with a vehicle as its parent.
- A part's coverage can carry **installed on** and **odometer at install**; its mile end is counted on the vehicle's odometer (install reading + limit). Without an install day the date starts from the purchase and is marked "start date to confirm".
- **Prorated: you pay a share** label for a prorated stage (a separate coverage); never shown as full coverage, no share is calculated.
- Moving a part to another vehicle asks for a new install date and reading and keeps the earlier stretch as history. Taking it off leaves its date-only coverage ("Miles no longer watched").
- Deleting, returning or disposing a vehicle that has parts asks: delete the parts with it, or keep them. Export includes parts, their coverages and a part-history file.
- My Items: a **Part of <vehicle>** tag and a **Parts** filter.
- Warranty reader reads the prorated stage (term months and quote) and the mile limit for a part.

## Rules built as decided (not bugs)
- A vehicle cannot be a part of anything (stricter than "not of itself or its own part").
- A never-linked ordinary item still drops a mile limit (appliances unchanged); a part, or an item that was a part, keeps it.
- A new part copies the vehicle's owner and followers exactly.
- One "enter the start date" question per part, not one per stage.
- A prorated stage read from a document is added when you apply the document on the item page, not on a waiting New Item.

## Not changed, do not report as new
- The items under push 26 "Not changed" still stand.
