# Scenario 37: Record money you got back, and see the total

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25) and have no recoveries. Test1 has four items added by hand, any store, today's date: **"UAT Rec One"** 120.00, **"UAT Rec Two"** 60.00, **"UAT Rec Three"** 45.00, **"UAT Rec Four"** 200.00. Test2 has one item **"UAT Rec Bob"** 50.00.
**Time:** 30 min
**Built per:** S5.4.11 and S9.2.5, first slice: the "Money recovered" card on the item page (Mark refunded, Add a card payout), the Home "Recovered" total, the data export file. NOT built, so not planned: the entry on the Something-broke view and the items list, the billing-page line, a household people filter.
**Why this plan:** the number on Home is money, so it must add up, keep cash apart from store credit, never count the same refund twice, and never mix two people's amounts.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open Home | The "Recovered" card is absent or shows a one-line prompt that nothing is recorded yet. Record which. No amount |
| 2 | Test1 | Open **UAT Rec One**, find the **Money recovered** card | Buttons **Mark refunded** and **Add a card payout**. An empty list |
| 3 | Test1 | **Mark refunded**: amount 120.00, received today, method "Back to the original payment", note "UAT refund" | Saved. The list shows one row: store refund, 120.00, date, method, note. The item is now **Returned** |
| 4 | Test1 | Open Home | "Recovered" shows 120.00 cash, 0 credit, 1 item. Record the exact wording |
| 5 | Test1 | Open **UAT Rec Two**, **Mark refunded** 60.00 with method **Store credit** | Saved. On Home: cash 120.00, **credit 60.00 shown apart**, total across both stated clearly. Record the wording; the 60.00 must not be added into the cash figure |
| 6 | Test1 | Open **UAT Rec Three**, **Add a card payout**: 45.00, today, note "UAT card payout" | Saved as a card reimbursement. The item is **not** marked Returned (a card payout does not change its status). Home: cash 165.00 (120 + 45), credit 60.00. Check the arithmetic |
| 7 | Test1 | On **UAT Rec One**, add a **second** recovery of 8.99 (store refund for shipping) | Two rows on the item. Home cash 173.99. The item stays Returned |
| 8 | Test1 | On **UAT Rec One**, edit the 8.99 row to 9.99 | Saved; Home cash 174.99 |
| 9 | Test1 | Remove the 9.99 row | Gone from the list; Home cash 165.00. The item stays Returned (the 120.00 refund remains) |
| 10 | Test1 | Open **UAT Rec Four**. Use **Mark returned** (the return form, not the recovery card) with refund amount 200.00, method original payment | The item is Returned and the Money recovered card now shows **one** row of 200.00 for it (the return form's refund is mirrored). Home cash 365.00. It is **not** 565.00: nothing is counted twice |
| 11 | Test1 | Edit the refund amount in the return form to 190.00 | The recovery row and Home follow: cash 355.00 |
| 12 | Test1 | Remove the only store refund from **UAT Rec Four** (the card row) | Asks or offers "I have it again". Keep it Returned if that is the default; record the exact wording and what happens to the item's status and to Home |
| 13 | Test1 | Try a received date more than a day in the future | Refused with a clear message; nothing saved |
| 14 | Test1 | Try a negative or empty amount | Refused with a clear message; nothing saved |
| 15 | Test1 | On Home, switch the period (this year / last 12 months / all time) and reload | The totals follow the period; the choice is still selected after reload on this device. Record the options and whether the numbers change (they should not, today) |
| 16 | Test1 | Expand the item list under the Recovered total | Each item with its amount; the items match what was entered; no item Test2 owns |
| 17 | Test2 | Open Home, then **UAT Rec Bob** | Test2's Recovered shows nothing from Test1. Test2 records a store refund of 50.00: Home shows 50.00 only |
| 18 | Test2 | Open Test1's item address | "Not found." |
| 19 | Test1 | Settings > Privacy & data > **Download everything**, wait for it, download the file | The zip includes a recoveries file (`recoveries.csv`) with Test1's rows only: kind, amount, date, method, note. No row for Test2's 50.00. (If the download link fails, record the message: see Scenario 40) |
| 20 | Test1 | Sign out and open Home | Redirected to sign in; no amounts visible |

Also record: how each kind is labelled (store refund, card reimbursement, warranty payout), whether "Exchange" is offered as a method (it should not be), and any step over 3 seconds.
