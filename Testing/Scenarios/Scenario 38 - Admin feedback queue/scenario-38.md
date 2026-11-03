# Scenario 38: The administrator reads the feedback queue and sets a status

**Accounts:** Ops (stevewash123.tester4@gmail.com, administrator), Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Ops is an administrator with two-step sign-in enrolled (Scenario 28; use the setup key in `RUN-CONFIG.md` to compute codes). Test1 and Test2 exist and have sent **no** feedback this hour (the limit is 5 per account per hour). Test1 has at least one item.
**Time:** 25 min
**Built per:** S7.1.9, first slice: a list of every account's messages, filters by status and type, one message with its context, and a status control (Received, In progress, Answered). NOT built, so not planned: replying to the sender, attachments, a Closed status, search by sender or text, grouping into tracked issues, the "new" count on the admin home.
**Why this plan:** the queue reads other people's messages, so it must be open to administrators only, show who sent what and where, and change nothing but the status.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Send three messages from **Send feedback**: Question "UAT admin question", Suggestion "UAT admin suggestion", Problem "UAT admin problem" (send the Problem from an item page so an item is attached) | All three appear under "Your messages", status Received |
| 2 | Test2 | Send one Problem "UAT admin bob problem" | Appears, status Received |
| 3 | Ops | Sign in with password and code, open the admin **Feedback** page | The page lists all four messages, newest first, each with its type, status, sender and time. A count of new (Received) messages shows (at least 4). It is not the old "Not built yet" placeholder |
| 4 | Ops | Read the row for Test1's Problem | Sender email and display name; type Problem; the page address; app version; the item name (Test1's item); the message text. Record what is shown |
| 5 | Ops | Filter by **Problem** | Only the two Problems (Test1's and Test2's) |
| 6 | Ops | Filter by status **Received**, then clear filters | Filtering and clearing both work; the list returns to all messages |
| 7 | Ops | Open Test2's Problem and set its status to **In progress** | The status changes at once. Reload: still In progress |
| 8 | Ops | Open Test1's Problem and set it to **Answered** | Changes; reload keeps it |
| 9 | Test2 | Open **Send feedback** | Their Problem's status reads **In progress** (the change reaches the customer) |
| 10 | Test1 | Open **Send feedback** | The Problem reads **Answered**; the Question and Suggestion still read Received. Test1 sees only their own three |
| 11 | Ops | Filter by status **Answered** | Only Test1's Problem |
| 12 | Ops | Try to edit the message text or the sender | Not possible (read-only) |
| 13 | Test2 | Type `/admin/feedback` in the address bar | Redirected away (to Home); nothing of the queue is shown. Test2 has no Admin menu |
| 14 | Test1 | Same | Same |
| 15 | (not signed in) | Open `/admin/feedback` | Redirected to sign in |
| 16 | Ops | Look at the message that has an attached item | The item's name shows to the administrator but no other detail of the item (price, store, receipt) |

Also record: the order the list uses (the story says oldest first for a work queue, the first build is newest first), the status wording, and whether the list pages (if there are more than a page of messages). Leave Ops's two-step as it is for Scenario 28.
