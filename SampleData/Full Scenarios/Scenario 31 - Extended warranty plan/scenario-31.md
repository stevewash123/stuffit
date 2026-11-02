# Scenario 31: Record a third-party warranty plan and cover items with it

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25). Test1 has no plans. Test1 has items "UAT Fridge" (price 900.00) and "UAT Washer" (price 600.00) (add by hand, any store, today's date).
**Time:** 30 min
**Built per:** S3.4.2 (plan page, cost and billing, claim details, items covered, files, ending a plan). A plan sold with a single item at the store (S3.4.3) is added on that item and is not planned here. "Start from your contract" needs the document reader: run steps 14 and 15 only if the reader is on, otherwise note "reader off".
**Why this plan:** one plan covers many items and every item must show it; ending the plan must switch it off everywhere.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open **Extended warranties** (`/plans`) from the Account menu | Heading "Extended warranties"; "No plans yet." with "Add your first plan"; text that a plan bought at the store for one item is added on that item |
| 2 | Test1 | **Add a plan**, then save with nothing filled in | Required fields are called out; nothing saved. Record which |
| 3 | Test1 | Fill: Company "UAT Home Warranty Co" (create inline if not listed), Name "UAT Home protection", Starts 2 months ago, Ends 10 months ahead | No error |
| 4 | Test1 | Put the end date before the start date and save | A clear error on the dates; nothing saved. Correct it |
| 5 | Test1 | Cost: price 30.00, Paid "a month"; fee per service call 75.00 | Accepted |
| 6 | Test1 | Claim phone "800-555-0111", claim website `https://example.com/plan`, "What it covers" "Refrigerators, washers, dryers", exclusions "Cosmetic damage". Save | Saved; plan page opens read-only |
| 7 | Test1 | Read the plan page | Term with start and end dates; Cost "$30.00 a month" with a yearly figure of $360.00 (30 x 12); "Per service call $75.00"; claim phone and link; the coverage text and "Exclusions and limits" |
| 8 | Test1 | In "What it covers" click **Cover items**, choose UAT Fridge and UAT Washer, confirm | Both are listed with their prices; "No items yet." is gone |
| 9 | Test1 | Open **Extended warranties** (the list) | One row: name, status badge, "UAT Home Warranty Co · 2 items · $360.00 a year"; above it "$360.00 a year for the plans still running, covering items that cost $1,500.00 in all." Check 900 + 600 |
| 10 | Test1 | Open UAT Fridge | The plan shows as a coverage on the item with its dates and claim details. Record the wording and where it sits in the order of coverages |
| 11 | Test1 | On the plan page remove the Washer with "Stop covering" | Washer leaves the list; the plans list now reads "1 item", covering items that cost $900.00 |
| 12 | Test1 | Attach a small image under "Contract and paperwork" and click **Upload** | File listed with its size; **View** opens it; it can be deleted |
| 13 | Test1 | Edit the plan (pencil), change the price to 25.00, save | Read-only page shows $25.00 a month and $300.00 a year |
| 14 | Test1 | (Reader on only) New plan, add a contract image under "Add the contract or terms", **Read it** | "Reading your document…" while it works; a review panel lists suggestions; nothing fills until each is accepted |
| 15 | Test1 | (Reader on only) On an existing plan use "Update from a newer document" and read a document | Only what differs from what is saved is listed; you accept each one |
| 16 | Test1 | In "Cancelled or lapsed?" leave the date empty | **End this plan** is disabled |
| 17 | Test1 | Enter an end date of today, click **End this plan** | Status shows ended; the plan row is dimmed in the list. The yearly total no longer includes it |
| 18 | Test1 | Open UAT Fridge | The plan no longer shows as active coverage from that date. Record what it shows (ended, or gone) |
| 19 | Test2 | Open **Extended warranties** and paste the address of Test1's plan | Empty list; the address gives not found or no access; nothing of Test1's plan shows |
| 20 | Test1 | Delete the plan if a delete is offered; otherwise leave it and note "no delete" | Leaves the list, or noted |

Also record: any money figure that disagrees with the arithmetic above, and any item that still shows the plan after it was removed or ended.
