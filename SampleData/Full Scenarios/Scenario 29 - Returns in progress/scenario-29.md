# Scenario 29: Start a return, work the returns list, mark it returned

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25). Test1 has no purchases named "UAT Return ..." (Scenario 26 items may stay). Reference data is loaded so a store with a known return policy can be picked.
**Time:** 30 min
**Built per:** S9.2.8 (start, cancel, list, group by store) and the Mark returned form (date, refund, method, difficulty, problems). NOT covered: the refund wizard and "I got my money back" recoveries (S5.4.11 and S5.4.12 are not built; `/items/sample/refund` is a mock).
**Why this plan:** the returns list is the one return feature that is built end to end, and it changes what the item page offers.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Add three purchases by hand (as in Scenario 26), all dated today: (a) store Home Depot, item "UAT Return Drill", price 120.00; (b) store Home Depot, item "UAT Return Saw", price 80.00; (c) store Target, item "UAT Return Kettle", price 30.00. Use another store from the list if one is missing and note which | Three items saved, each with a suggested return window (store policy) |
| 2 | Test1 | Open `/returns/in-progress` | Heading "Returns in progress"; empty state "Nothing to return right now." and the line about choosing **Start a return** |
| 3 | Test1 | Open UAT Return Drill. Find **Start a return** | Button is shown (it only appears for an owned item that has at least one coverage). Record whether it appears on each of the three |
| 4 | Test1 | Click **Start a return** | A green note: "Return in progress since <today>. It is on your returns list until you mark it returned." with **Mark returned** and **Cancel return**. The item is still owned; its coverages and dates are unchanged. The **Start a return** button is gone |
| 5 | Test1 | Reload the item page | The in-progress note is still there |
| 6 | Test1 | Start a return on UAT Return Saw and on UAT Return Kettle too | Same note on each |
| 7 | Test1 | Open `/returns/in-progress` | Three rows, closing soonest first. Each shows the name, "Bought <date> · <price>", the store name, and "Return window ends <date>" with a days-left badge. Record the order and the days left |
| 8 | Test1 | Tick **Group by store** | One section per store, A to Z: "Home Depot" with "2 items · $200.00", "Target" with "1 item · $30.00". The store name leaves the row text. Untick: back to one list |
| 9 | Test1 | Click the Kettle row | Opens the item page |
| 10 | Test1 | Click **Cancel return** on the Kettle | The note disappears; **Start a return** is offered again. No "The return" summary appears (cancelling leaves no record) |
| 11 | Test1 | Return to `/returns/in-progress` | Two rows (Drill and Saw); Kettle is gone |
| 12 | Test1 | Open UAT Return Drill, click **Mark returned** (in the note) | A drawer "Mark as returned" opens with Date returned = today, Refund amount = 120.00 (the item price), "Paid back by" (starts at "Not sure / not yet"), "How hard was it?" 1 to 5, "Problems getting paid" |
| 13 | Test1 | Clear the date and look at the submit button | Disabled while the date is empty. Put today's date back |
| 14 | Test1 | Set Refund amount 100.00 (a partial refund), pick a "Paid back by" option, hard = 2, problems "Restocking fee", submit | Drawer closes. A card "The return" shows Returned <date>, Refund $100.00 with the method, "How hard 2 of 5" with its word, Problems "Restocking fee". The item is no longer owned (status Returned) |
| 15 | Test1 | Look at the item's buttons | **Mark returned** and **Start a return** are gone; **I have it again** is offered. Record what the page says about reminders or coverage, if anything |
| 16 | Test1 | Open `/returns/in-progress` | Only UAT Return Saw is left |
| 17 | Test1 | On the Drill, click the edit icon on "The return", change the refund to 110.00, save | The summary shows $110.00 |
| 18 | Test1 | Click **I have it again** | Status returns to owned; the item is not on the returns list. Record whether the "The return" summary stays or goes |
| 19 | Test2 | Open `/returns/in-progress` | Empty state. None of Test1's items or stores appear |
| 20 | Test2 | Paste the address of Test1's UAT Return Saw item page | Not found or no access; nothing of Test1's shows |
| 21 | Test1 | Mark the Saw returned with a date but no refund amount and no method | Saves; the summary says Refund "Not paid yet" |

Also record: the exact days-left wording at each stage, and anything on the Returns page (`/returns`, from the menu) that looks like real data. That page is labelled "First design: example data" (Sony headphones, Ninja air fryer, Keurig, Bosch). It must not show your real returns yet, and it must not be mistaken for the working list.
