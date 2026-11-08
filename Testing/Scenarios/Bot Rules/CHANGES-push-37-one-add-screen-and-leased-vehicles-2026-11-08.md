# What changed in push 37: one Add screen (retail or vehicle), vehicle payment, and leased vehicles (2026-11-08)

For GrokBot. Check `/api/version` against the pushed API commit. Migrations **`PurchasePaidBy`**, **`VehicleLease`** and **`PartyVehicleMaker`**, **`PartyDealer`** (applied on startup if `Database:MigrateOnStart` is on). **Run `--seed` on staging after deploy**: it loads about 180 vehicle models (category Vehicles) for Ford, Toyota, Honda, Chevrolet, GMC, Dodge, Ram, Jeep, Subaru, Nissan, Hyundai, Kia, Mazda, Volkswagen, BMW, Tesla and Harley-Davidson; the model checks below do nothing without them. Stories S3.5.7 and S3.5.8.

## New: one Add screen (S3.5.7)
- The My Items header now has one **Add** button (the separate "Add a vehicle" button is gone). `/add/new` and `/add/vehicle` both show two tiles at the top: **Retail purchase** and **Vehicle** (radio-group behaviour). Choosing the other tile switches forms and carries over brand/make, model, price, date and seller.
- The tiles do not show when you arrive from a New Item (`?pending=`) or to add a part to a vehicle (`?vehicle=`).
- **Retail form:** the Category list has no **Vehicles**. A brand that makes vehicles (for example Ford) asks once: "Is this a part or accessory, not a vehicle?" (Yes, a part or accessory / No, it is a vehicle). A model that is one of that brand's vehicle models (for example Ford **Bronco**, case and spacing ignored) is refused with "Bronco is a Ford vehicle. Add it as a vehicle so its odometer, parts and mileage coverage work." and a **Switch to the vehicle form** button; Save is blocked. The server refuses it too (400, field `model`), on create and on editing an item (a vehicle's own model is fine). Vehicle models are no longer suggested in the retail model list.
- **Vehicle form:** "Bought from" is now **Dealer or seller**. New **Paid by**: Payment plan, Credit card (with a card list), Cash or check; none is allowed. A card is kept only with Credit card. The vehicle form has no order number.

## Changed: the Make list on the vehicle form is vehicle makers only
- The vehicle form's Make no longer offers every brand (no more Abu Garcia). Parties have a new **vehicle maker** flag (`isVehicleMaker`); `--seed` tags about 78 makers (cars, trucks, motorcycles, boats, RVs, snowmobiles). A make the person types that is not on the list is added as their own vehicle maker. The `--seed` run on staging sets the flags (it only adds roles). The Add screen's two choices are now real buttons (the chosen one filled).

## Changed: the Dealer list on the vehicle form is dealers only
- "Dealer or seller" no longer offers ordinary stores (no Best Buy, Home Depot). Parties have a **dealer** flag (`isDealer`). A dealer is also a store (it appears in the retail Store list); a store is not a dealer. Seeded dealers: CarMax, Carvana, AutoNation, Camping World, and **Private sale** (a person selling a vehicle). A dealer the person types is saved as their own dealer. The vehicle form's model year now starts as this year.

## New: leased vehicles (S3.5.8)
- **You have it: Bought / Leased** on Add a vehicle and in the vehicle's details (pencil). Leased asks for **Lease ends**, **Allowed per year** and an optional **Fee per mile over**. A lease cannot end before the date the vehicle was got (400, `leaseEndDate`). Choosing Bought clears the lease fields.
- The vehicle page shows "Leased until <date> · N miles a year allowed" and: "If you bought GAP coverage or an extended warranty with this car, you may be owed a partial refund. Check with your dealer or lender."
- **Lease-end to-do:** one per leased vehicle with an end date ("<vehicle>: your lease ends soon", due on the end date, nudging from 90 days before, carrying the same note). Moving the end date moves it; choosing Bought or clearing the date finishes it.
- **Lease mileage check** is a new notification type (category Expiring, email and in-app, on the settings grid). It asks the person to check their odometer against the allowance. Sent halfway through each lease year (6 months after the lease began, then every 12 months) and once three months before the end, only for a leased, owned vehicle with an allowance, once per owner per point; a point missed by more than 14 days is skipped. WarrantyCat does not track miles. Reminder run summary has a new `LeaseMileage` count.

## Steps to try
1. Add (header) > Retail purchase: confirm no Vehicles category; pick brand Ford; answer the part/accessory question; type model Bronco: refused; Switch to the vehicle form: Ford and Bronco carried over.
2. Vehicle: Paid by Payment plan; Leased, end date, 12,000 a year; save. Vehicle page shows the lease line and note; To do has the lease-end item.
3. Edit the vehicle to Bought: the lease line and the to-do go.
4. With the clock moved to 6 months after the lease began, run the reminder job: one "halfway through a lease year" notice; again the same day: none. Turn the type off in Settings > Notifications: the app notice still appears, no email.

## Decided, do not report
- "Add a vehicle" and "Add a purchase" are one button now.
- Not tracking miles against the allowance is deliberate (reminders only).
- Payment-plan details (lender, monthly amount, term) and lease-agreement reading are not built.
- Paid by is not yet shown on the vehicle page or in the export.
