# Scenario 35: Send feedback and see your messages

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25) and neither has sent feedback. Test1 has at least one item (Scenario 26). The rate limit is 5 messages per account per hour, so run this plan once an hour at most per account.
**Time:** 20 min
**Built per:** S7.1.8, customer side: the form, the "What will be sent" panel, "Your messages" with status, the rate limit, and the entries in the footer and account menu. NOT built, so not planned: attachments, the administrator queue (S7.1.9), so the In progress and Answered statuses and replies cannot be tested here, email replies, and "Report a problem with this" from a notification.
**Why this plan:** the form sends something about the person to the team, so it must show exactly what goes, send nothing more, and keep each account's messages private.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Find **Send feedback** in the footer and in the Account (avatar) menu and on the Account page | All three are present |
| 2 | Test1 | From My Items, click the footer **Send feedback** | Page "Send feedback" opens. "What will be sent with your message" shows "Page you were on:" with the items page address (`/items`), "App version:" with a short build id or "unknown", and "Nothing else about your items, purchases or cards is sent." No item line |
| 3 | Test1 | Open one item, then use the Account menu **Send feedback** | The panel shows that item's page address and an "Item:" line with its id |
| 4 | Test1 | Click **Send** with the message empty | "Write a message first."; nothing sent; "Your messages" unchanged |
| 5 | Test1 | Choose **Question**, type "UAT question one" and **Send** | The button shows "Sending…", then "Thank you. We received your message." The form is ready for another |
| 6 | Test1 | Look at "Your messages" | One row: "Question · <today's date>", status "Received", the message text. It is the newest at the top |
| 7 | Test1 | Send a **Suggestion** "UAT suggestion" and a **Problem** "UAT problem" | Each appears with its own type label and status Received. Three rows, newest first |
| 8 | Test1 | Reload the page | All three are still listed |
| 9 | Test1 | Paste a very long message (over 4000 characters) | Typing stops at the limit, or it is refused with a clear message; no error page. Record which |
| 10 | Test1 | Send a message containing `<b>bold</b> & "quotes"` | Shown exactly as typed, not as bold text |
| 11 | Test1 | Send two more messages (five in the hour in all) | Both are accepted |
| 12 | Test1 | Send a sixth message | Refused with a clear "too many" style message; nothing added to "Your messages". Record the exact text. The typed message is not lost |
| 13 | Test2 | Open **Send feedback** | "You have not sent any messages yet." None of Test1's messages |
| 14 | Test2 | Send "UAT question from Test2" | Accepted (Test1's limit does not apply to Test2) and listed alone |
| 15 | Test1 | Open **Send feedback** | Test1 sees only their own messages, not Test2's |
| 16 | Test1 | Open `/feedback?from=https://example.com/x` | The panel does not show an outside address as the page you were on (it shows "none" or ignores it) |
| 17 | Test1 | Sign out and open `/feedback` | Redirected to sign in; nothing shown |

Also record: the type labels and status wording as displayed, whether the page address in the panel matches where you came from each time, and any step that felt slow (over 3 seconds).
