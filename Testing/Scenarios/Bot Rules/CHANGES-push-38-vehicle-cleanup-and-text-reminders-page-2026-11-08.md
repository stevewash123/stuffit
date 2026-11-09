# What changed in push 38: vehicle clean-up and the text-reminders page (2026-11-08)

For GrokBot. Check `/api/version` against the pushed API commit. No migration, no `--seed`. Small push: items from your push 37 follow-up report, and the new public pages.

## Fixed from the push 37 reports
- **Bronco refusal (item 13):** on the retail form, **Save purchase is disabled** while a vehicle model of the brand is typed, and while the "part or accessory?" question for a vehicle brand is unanswered (the message beside the model says why).
- **Boat unit (item 6):** choosing kind **Boat** makes the odometer count **Hours** (and any other kind, Miles), unless the person has chosen a unit themselves. Hours of 0.8 now read "0.8 hours" (a fraction keeps one decimal; whole numbers are unchanged) and one reads "1 hour" / "1 mile" (singular for exactly one).
- **In-service date for a new vehicle (item 7):** "First put in service" is on the Add form for New as well as Used (optional for New).
- **Reading date (item 8):** when an odometer is entered on Add, a **Date of that reading** field appears (empty = the date bought; a future date is refused, field `odometerReadOn`).
- **Fee per mile (item 12):** the vehicle page's lease line shows "$0.25 per mile over". The lease mileage notice says "$0.25 per mile" (currency symbol).
- **Paid by** is shown on the vehicle page ("Paid by payment plan / credit card / cash or check").

## New: public text-reminders pages (S3.5.x not applicable; toll-free verification groundwork)
- **`/sms`** ("Text message reminders", linked in the footer and the legal nav): the program, the opt-in method, frequency, rates, STOP and HELP, privacy line and contact. No draft banner.
- **Terms** has a new "Text message terms (SMS)" section; **Privacy** has "Mobile numbers and text messages" (no sale or sharing of numbers or opt-in data) and lists the mobile number under what we keep. The contact email on the legal pages is now support@microsaasbuilders.com. The Terms version is unchanged (no re-acceptance).
- `/warrantycat`, `/warrantycat/privacy` and `/warrantycat/terms` redirect to `/sms`, `/privacy` and `/terms`.
- Terms and Privacy still show bracketed placeholders (company, address, governing law, minimum age) and the draft banner: known, not yet filled.

## Not changed, do not report
- The combobox showing the previous results briefly while typing fast: it waits 200 ms and cancels older searches; the short wait is the search itself.
- Document-reading items (60,000-mile powertrain limit, plan fields, multi-term certificates, model split, the part form's year) are the next push.
- The text-message opt-in itself (settings checkbox and number) is not built yet; the pages describe the planned flow.
