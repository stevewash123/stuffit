# Scenario 56: Conditions, exclusions, a used item, accessories, and a document with four products

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Reader on (otherwise "reader off"). Clock offset 0 (2026-11-04). The Chase Freedom Unlimited card ending 1111 is on Test1.
**Time:** 55 min
**Built per:** S2.4.1 (reader), S3.1.8, S3.1.9, S3.2.8 (components). Documents are all existing fixtures in `Testing/SampleData/warranties`: `edge-exclusions-and-voiding-conditions.pdf`, `edge-used-item-30-day-dealer.pdf`, `standard-power-tool-5yr.pdf`, `multi-item-kitchen-suite-warranty.pdf`; receipt `receipts/pdf/41-thermal-homedepot-milwaukee-hammer-drill.pdf`.
**Why this plan:** these fixtures have been read by the reader (T2 B9 to B12) but no run has checked what the **item page** does with them. Reducing "2 years residential, 90 days commercial, void if..." to "2 years" is the failure this plan hunts.

**Part A: conditions that change the term (GardenMaster GM-21 mower)**

Bought **2026-04-10**, $749, card 1111.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Add "UAT Mower", brand GardenMaster, model GM-21, bought 2026-04-10. Upload `edge-exclusions-and-voiding-conditions.pdf` | Terms read with quotes; nothing saved until accepted |
| 2 | Test1 | Read the suggestion | **Two** terms: **2 years residential** (ends **2028-04-10**) and **90 days commercial or rental** (ends 2026-07-09). The app does not pick 2 years as the only answer without saying residential use is assumed. It asks or labels it. Record which |
| 3 | Test1 | Read the other conditions on the page | **Wear items** (blades, belts, spark plugs, filters, tires) covered **30 days** only (ended 2026-05-10). **Void if** oil not changed once per season, shown by records; **engine coverage void** with fuel over 10% ethanol. **Original purchaser only**; ends if sold or given away. **Authorized dealer** service; shipping is the owner's cost. Each is shown, in the document's words or close to them |
| 4 | Test1 | Check the item page headline | Not simply "2 years". It shows the term **and** a visible "conditions apply" with the list one tap away |
| 5 | Test1 | Mark the mower given away | The app says the warranty ends with the owner (original purchaser only) and asks before ending it. Record whether it offers "transfer" at all (it should not) |
| 6 | Test1 | Check for a maintenance prompt | The oil-change condition may produce a prompt to keep service records. Record whether it does. Not required; note as **Idea** if not |

**Part B: a used item (Second Spin laptop)**

Sold **2026-09-12**, $329, cash or card 1111.

| # | Persona | Action | Expected |
|---|---|---|---|
| 7 | Test1 | Add "UAT Used Laptop", brand not listed, model L-14, serial 7731-XA, bought 2026-09-12. Upload `edge-used-item-30-day-dealer.pdf` | Dealer warranty **30 days**, ends **2026-10-12**, on defects present at sale. Shown **ended** on 2026-11-04 |
| 8 | Test1 | Read the end of the term | "Sold as is, no warranty of any kind, after 30 days" is shown as **a boundary**, not a blank and not a failed read. The page does not just say "expired"; it says nothing covers it from 2026-10-13 |
| 9 | Test1 | Check the battery | Excluded (a wear item). Shown as an exclusion on the dealer coverage |
| 10 | Test1 | Check the maker's warranty | The document says the original manufacturer's warranty "is not transferred by this sale". The app **does not propose** a maker or shared-brand warranty for this item. If a brand were known, the proposal would carry the not-transferred note |
| 11 | Test1 | Check the card benefits | The Chase extended warranty is not offered, or is offered with "used items are not eligible" (the sample card guide excludes used items). Record which. It must not extend the dealer's 30 days |
| 12 | Test1 | Check reminders | None for an item whose only coverage has ended |

**Part C: main product and accessories (Milwaukee 2904-20)**

Receipt 41 is Home Depot, 2026-09-14, tool only (no battery).

| # | Persona | Action | Expected |
|---|---|---|---|
| 13 | Test1 | Upload receipt 41, add the item, then upload `standard-power-tool-5yr.pdf` to it | Tool: 5 years, ends **2031-09-14**. Serial on the document (M18-4471902) differs from the receipt's (M18F26B3305172). Record whether the app flags the serial mismatch |
| 14 | Test1 | Read the battery and charger term | "Batteries and chargers carry a separate **3 year** warranty" (**2029-09-14** if shown). This item was sold **tool only**, so the battery line should not be added as a coverage for this item. Record whether it is offered, attached or only noted |
| 15 | Test1 | Read what is not covered | Accessories and wear items (chucks, brushes, bits) listed as not covered |
| 16 | Test1 | Check registration | "Register within 90 days to record your purchase date. **Not required** for service when you have a dated receipt." The app does **not** ask whether it was registered (contrast Scenario 54 Part B) |
| 17 | Test1 | Check the Chase extension | Does **not** apply to the 5-year tool warranty (card adds only to warranties of 3 years or less). It would apply to a 3-year battery if one is a separate item. Record what it shows |

**Part D: one document, four products with two levels each (known gap)**

The Hearthstone Signature kitchen suite, bought together **2026-03-03**. Terms from the document:

| Appliance | Model | Full warranty | Extra limited coverage |
|---|---|---|---|
| Range, 30 inch gas | HS-R30G | 2 years parts and labor | Burners: 5 years parts |
| Dishwasher | HS-D24 | 1 year parts and labor | Stainless tub: lifetime against rust-through |
| Over-the-range microwave | HS-M16 | 1 year parts and labor | Magnetron: 5 years parts |
| Refrigerator | HS-F36 | 2 years parts and labor | Sealed system: 7 years parts |

Start: the **installation date**, or **purchase plus 6 months** if installation is not documented, **whichever comes first**.

| # | Persona | Action | Expected |
|---|---|---|---|
| 18 | Test1 | Add four items by hand with the models above, all bought 2026-03-03, brand Hearthstone | Four items |
| 19 | Test1 | Upload `multi-item-kitchen-suite-warranty.pdf` to the **range** | **Known gap (T2 B12):** it may read as one plan. Expected: the range gets 2 years full and burners 5 years parts, and the other three appliances are **offered** their own lines (matched by model), never attached silently |
| 20 | Test1 | With installation **not documented**, check start | Start = **2026-09-03** (purchase + 6 months). Range **2028-09-03**, burners parts **2031-09-03**; dishwasher **2027-09-03**; microwave **2027-09-03**, magnetron **2031-09-03**; refrigerator **2028-09-03**, sealed system parts **2033-09-03** |
| 21 | Test1 | Enter an installation date of **2026-03-20** on the dishwasher | Start moves to 2026-03-20 (earlier than 2026-09-03): ends **2027-03-20** |
| 22 | Test1 | Enter an installation date of **2026-10-01** on the microwave | Start stays **2026-09-03** (whichever comes first); the later installation date does not push it back. Record how the app explains this |
| 23 | Test1 | Check the dishwasher's tub | Lifetime against rust-through on the tub only (see Scenario 55); the dishwasher body is 1 year |
| 24 | Test1 | Read the conditions | "All appliances must be installed by a licensed installer" is kept as a condition on all four |
| 25 | Test2 | Open Test1's items by address | Not found |

Also record: any condition dropped, any end date that disagrees with the key by a day, any place a limited term is shown as the whole-product term, and the **count of appliances attached** after step 19 (this is the known-gap result: 1, 2, 3 or 4).
