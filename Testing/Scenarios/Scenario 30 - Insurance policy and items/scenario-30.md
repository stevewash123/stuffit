# Scenario 30: Record a renter's policy, link items, see the notes on the item

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25). Test1 has no insurance policies. Test1 has three items (add by hand, any store, today's date): "UAT Guitar" price 1800.00, "UAT Laptop" price 1200.00, "UAT Lamp" price 40.00.
**Time:** 35 min
**Built per:** S3.4.1 (policy form, limits for kinds of things, what it covers, per-item links, notes comparing cost with limits, the Insurance card on an item). "Start from your policy" needs the document reader: run steps 17 to 19 only if the reader is on in this environment, otherwise note "reader off". The "Listed separately on the document" panel needs a real policy document and is not planned here.
**Why this plan:** insurance is a whole screen with arithmetic (limits against prices) that a person will trust, so wrong numbers matter.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open **Insurance** from the Account menu (`/insurance`) | Heading "Insurance"; "No policies yet." with "Add your first policy" |
| 2 | Test1 | Click **Add a policy**. Without typing anything, click **Save policy** | Required fields are called out; nothing saved. Record which are flagged |
| 3 | Test1 | Fill: Insurer "UAT Insurer" (create inline if not listed), Name "UAT Renter's policy", Kind "Renter's", Policy number "UAT-001", Starts = a date 6 months ago, Ends = a date 6 months ahead | No error on those fields |
| 4 | Test1 | Set an end date BEFORE the start date and save | A clear error on the end date; nothing saved. Put it right again |
| 5 | Test1 | Cost and limits: Premium 240, Paid "a year", Deductible 500, Personal property limit 20000 | Accepted |
| 6 | Test1 | Under "Limits for kinds of things", click **Add a limit** twice: "Musical instruments" 1500 and "Electronics" 2500. Click **Add a limit** a third time, leave it blank, then save | The blank row is ignored or called out (record which); the two real limits are kept |
| 7 | Test1 | What it covers: choose "All my items, except the ones I leave out". Claim phone "800-555-0100", Claim website `https://example.com/claims`. Save policy | Saved; the policy page opens read-only |
| 8 | Test1 | Read the policy page | Title and "Renter's · UAT Insurer · policy UAT-001"; a status badge; Term, Premium "$240.00 a year", Deductible $500.00, Personal property limit $20,000.00, claim phone as a tap-to-call link, claim website link; limits listed ("Musical instruments: $1,500.00", "Electronics: $2,500.00") |
| 9 | Test1 | Look at "What it covers" | "All your items except the ones left out below: N items, which cost $..." where N and the total match the items the account has (check the sum yourself); "No exceptions: every item is covered." |
| 10 | Test1 | Click **Leave out or set terms for an item**, pick UAT Guitar, choose limit "Musical instruments ($1,500.00)", set "Listed on the policy at" 1800, save | The Guitar appears in the list with its terms. Record the wording next to it |
| 11 | Test1 | Look for notes at the top of the policy page | A note comparing the Guitar's price ($1,800) with the $1,500 instrument limit (it is over the limit), followed by the line that these are not advice. Record the exact text. Nothing is said about the Lamp |
| 12 | Test1 | Open UAT Guitar from the link, then find its **Insurance** card | Card shows the policy name as a link, "UAT Insurer · until <date>", "Deductible $500.00. Limit for Musical instruments: $1,500.00. Listed on the policy at $1,800.00.", the same over-limit note, **Call 800-555-0100** and **Make a claim online** |
| 13 | Test1 | Open UAT Lamp | The same policy shows on its Insurance card (all items are covered), with the deductible and no instrument limit |
| 14 | Test1 | On the policy, **Leave out or set terms**, pick the Lamp, tick "Leave this out of the policy", save. Reload the Lamp item page | The Lamp has no Insurance card now. The policy's covered count drops by one and the covered cost drops by $40.00 |
| 15 | Test1 | Edit the policy (pencil), change "What it covers" to "Only the items I choose", save | Summary changes to "Only the items you link below": count and cost follow the items still linked. Record the numbers and check them |
| 16 | Test1 | Open **Insurance** (the list) | One row: the name, a status badge, "Renter's · UAT Insurer · covers N items · $500.00 deductible"; above it "$240.00 a year for the policies still running." |
| 17 | Test1 | (Reader on only) **Add a policy**, add a small image or PDF of a policy page under "Add the policy or declarations page", click **Read it** | The button says "Reading your document…" and is disabled while it works; afterwards a review panel lists what was read; nothing is filled in until each is accepted |
| 18 | Test1 | (Reader on only) Accept one suggestion, dismiss another | Only the accepted one fills the form; a note says what changed |
| 19 | Test1 | (Reader on only) Leave the page with typed changes unsaved | A warning about unsaved changes appears (the form must not be lost silently) |
| 20 | Test2 | Open **Insurance** and paste the address of Test1's policy | Empty list; Test1's policy address gives not found or no access; no name, number or limits of Test1's show |
| 21 | Test1 | Delete the policy (trash icon), confirm | It leaves the list; the Guitar no longer shows an Insurance card |

Also record: money amounts that look wrong, any note that reads like advice to buy something, and any date label that disagrees with today's date.
