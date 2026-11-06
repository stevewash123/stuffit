# What changed in push 25: when vehicle coverage starts, and who it follows (S3.5.4) (2026-11-05)

For GrokBot. API `2f52761`, UI `b7011c1`. Check `/api/version` (`commit` must be `2f52761`). The UI has no version marker: record its Last-Modified, and note that the item page's To do card (push 24) is the proof the new UI is there. Migration `VehicleCoverageStart` is applied to staging. No new scenario number yet: run the steps below on Alice.

## Also
- Step 16b of Scenario 54 was marked Blocked on the push 24 UI. The UI is deployed (the commit is not in the bundle because there is no marker). Please run 16b now.
- Fixed from push 23: errors on the vehicle page (changing the unit, a future reading date) now read as a plain message, not "One or more validation errors occurred."

## Steps
1. Add a vehicle bought **new**, no in-service date. Attach a maker warranty document (for example 3 years or 36,000 miles) and apply it. Expect the coverage counted from the purchase date, marked **Start date to confirm**, and a to-do "Enter the date <vehicle> was first put in service."
2. Enter the in-service date on the coverage. Dates, parts, the to-do and the vehicle's in-service date all update.
3. Add a vehicle bought **used**, no in-service date. The page says "Add the date this vehicle was first put in service to see what factory coverage is left." Apply the document: the coverage reads **Start not known**, has no end date, and is not counted (not in days left, Home or reminders; the item shows needs info).
4. Edit vehicle details and enter the in-service date. The coverage and its parts get dates.
5. Used vehicle, document marked not transferable: shows "Original owner only. Not transferable. The factory warranty does not apply to you." and "Not counted: not transferable". A transferable one says "Transfers to the next owner."
6. Add a coverage with **Certified or dealer-added**, its own start date and start odometer. Then read a factory document. Both coverages remain, and the miles are measured from the start odometer.
7. An appliance with a registration or installation start behaves as before.

## Decided, do not report
- A vehicle with no condition stated is treated like a new one. A used vehicle bought from a dealer also has a not-transferable factory warranty marked not counted.
- A start-not-known coverage never ends by miles. A printed start or end date in the document wins over the vehicle's start. Only the maker's whole-product warranty follows the in-service date.
- Changing an in-service date already entered does not move coverages already dated. An in-service date cannot be in the future (1900 floor).
- Certified coverage is made by hand; the reader does not recognise it. There is no admin option yet to mark a shared policy "from first use".

## Still open from push 23 (not changed)
Reading a warranty replaces hand-typed maker coverages on a vehicle; the "14 months ago" label is missing on the estimated line; the bill-of-sale reader missed the model.
