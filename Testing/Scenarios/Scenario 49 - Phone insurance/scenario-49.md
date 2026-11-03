# Scenario 49: Monthly phone insurance with deductibles, a claim cap, and an upgrade

**DEFERRED until implemented: S3.4.19 (with S3.4.10, S3.4.6, S3.4.8, S3.4.16).** Do not run before then. Steps that need a not-yet-built screen say what to look for and will fail on build 982952c.

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Test1 has "UAT Phone" ($999, bought 200 days ago, paid with the Chase Freedom Unlimited card, so a card extended warranty may apply) and no plans.
**Time:** 45 min
**Built per:** S3.4.19, S3.4.10, S3.4.6, S3.4.8, S3.4.15, S3.4.16, S3.4.13. Uses the simulated clock. Reader steps need the reader on.
**Why this plan:** phone insurance is the plan most people actually hold: monthly, no receipt, a deductible that depends on the loss, a claim cap, and it must follow the phone on upgrade.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | UAT Phone > Add a protection plan | **Phone or device insurance** is offered as a starting point |
| 2 | Test1 | Choose it; provider "UAT Carrier", $14 monthly, started 100 days ago, IMEI 356938035643809 | Saved as a plan on the phone; no end date; next billing date shown; the IMEI is on the plan and the item |
| 3 | Test1 | Add the deductibles: screen $29, other damage $99, loss $199, theft $199; claims cap 2 per 12 months | Shown as a small table on the plan |
| 4 | Test1 | Upload a photo of a carrier bill line or enrolment email (reader on) | Provider, price, start date and device read with quotes; unclear values stay blank; saved only after accept |
| 5 | Test1 | Open the phone's page | Layers named plainly: maker's warranty (defects), card extended warranty (defects, extended), phone insurance (accidents, loss); distinct labels; no advice |
| 6 | Test1 | Make a claim > broken screen | Shows the provider phone/site, the account or contract number, the IMEI and the **$29** deductible for the chosen loss |
| 7 | Test1 | Make a claim > lost | Shows **$199**; the maker's warranty and card benefit are not offered (not defects) |
| 8 | Test1 | Record two claims in 12 months (screen $29, then other $99) | Plan shows "2 of 2 used; resets <date>"; a third request is flagged, not blocked |
| 9 | Test1 | Read the cost view | $168 a year (12 x 14) plus $128 deductibles paid; no worth-it verdict |
| 10 | Test1 | Add "UAT Phone 2" ($1,099, today) | The app asks about the plan: Move it to the new phone / Cancel / Not sure |
| 11 | Test1 | Choose **Move it**; enter the new IMEI | Plan now covers the new phone from today; old phone keeps its history; monthly billing and renewal date unchanged; claim count reset only if the plan says so |
| 12 | Test1 | Choose **Cancel it** on a second plan, then record "I cancelled" with no refund | Plan ends on that date; to-do "Check that your refund arrived" due in 14 days |
| 13 | Test1 | Clock +1 year | Monthly plan still active; renewal reminder "cancel or compare" shows once per cycle, not 12 times |
| 14 | Test2 | Look for Test1's IMEI or plan | Not visible anywhere |

Also record: any place the app calls the insurance a warranty or the warranty insurance, any deductible shown without its source, and any figure that disagrees with the arithmetic above.
