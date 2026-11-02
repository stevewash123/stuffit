# Scenario 32: General reminders on an item and on the To do page

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25). Test1 has an item named "UAT Reminder Blender" (add by hand, any store, today's date) and no open to-dos.
**Time:** 20 min
**Built per:** S4.6.2 (the To do card on the item page, the To do page) and the to-do actions (Mark as done, Dismiss for now, Not applicable). Reminder emails for due to-dos (S4.6.3) are sent by the hourly job, so seeing one needs the simulated clock (Scenario 24); step 12 is optional. Suggested to-dos found in documents come from the document reader and are not planned here.
**Why this plan:** a to-do is a small promise to the user; it has to appear in both places, leave when finished, and never leak to another account.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open the **To do** page (`/todos`) | Heading "To do"; "Nothing to do right now." with a link to Your items |
| 2 | Test1 | Open UAT Reminder Blender (read-only) | No "To do" card is shown (it only appears when there are to-dos or in edit mode) |
| 3 | Test1 | Click the pencil (edit) | A "To do" card appears with "Add a reminder" (placeholder "For example: register the warranty") and "Due (optional)". **Add** is disabled while the title is empty |
| 4 | Test1 | Add "Register the warranty" with a due date 5 days ahead; add "Keep the box" with no due date | Both listed under To do. The dated one shows a due label (record its wording); the other shows none |
| 5 | Test1 | Add "Check the cord" with a due date of yesterday | Listed with an overdue label (record the wording and colour) |
| 6 | Test1 | Leave edit mode (**Done**) | The To do card stays and shows the three reminders |
| 7 | Test1 | Open `/todos` | The same three, each with the item name "UAT Reminder Blender" as a link back to the item |
| 8 | Test1 | **Mark as done** on "Check the cord" | It leaves the list on both pages |
| 9 | Test1 | **Dismiss for now** on "Keep the box" | It leaves the open list. Record whether it comes back later and where it can be found |
| 10 | Test1 | **Not applicable** on "Register the warranty" | It leaves the list. Record whether it can be recovered |
| 11 | Test1 | Reload `/todos` | Nothing done or dismissed has returned |
| 12 | Test1 | (Optional, needs the simulated clock) Add a to-do due tomorrow, advance the clock 1 day, run reminders (Scenario 24) | One reminder arrives (email and in-app, per Settings > Notifications), naming the item and the to-do, once only |
| 13 | Test2 | Open `/todos` | "Nothing to do right now." None of Test1's reminders |
| 14 | Test2 | Paste the address of the Blender item | Not found or no access; no to-dos of Test1 show |

Also record: how overdue and due-soon labels are worded, and whether a double click on **Add** creates two reminders.
