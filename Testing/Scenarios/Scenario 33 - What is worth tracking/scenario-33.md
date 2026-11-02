# Scenario 33: Set what is worth tracking, see New Items follow it

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25). Test1 has an empty New Items list. A receipt file with several lines of different prices, including at least one small line (a filter, cable, hose or similar under $50) and one large line: use the receipt PDF or image from any Full Scenarios folder, or any receipt you have for testing. Record which file and its lines and prices before starting.
**Time:** 25 min
**Built per:** S9.8.5, the Settings control only (tab "What to track", `GET/PUT /api/me/tracking`) and S9.2.11 (New Items groups small lines under "Smaller things"). NOT built, so not planned: the audit log entry on change, the "Lower the amount to $20?" suggestion, and the per-person currency.
**Why this plan:** a setting that changes what a person sees first is only worth having if the list really follows it and one person's setting never changes another's.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open Settings. Find the tab **What to track** | Tab is in the Settings tab row |
| 2 | Test1 | Open it | Heading "What is worth tracking" with the explanation that smaller lines are listed under "Smaller things" in New Items, are not ticked for you, and nothing is hidden or deleted. Field "Track things worth at least". A note: "Using the standard amount, $50.00. Zero tracks everything." Record the exact text |
| 3 | Test1 | Open **New Items** and upload the receipt (the upload route in Scenario 26 step 9 or the New Items page) | Pending lines appear. Note which line sits under "Smaller things (N)" (collapsed) with its reason, and which are in the main list |
| 4 | Test1 | Back on **What to track**, click **Everything** | The field shows 0 |
| 5 | Test1 | Click **Save** | Status shows "Saving…" then "Saved" (and a toast). Record the wording |
| 6 | Test1 | Reload the page | The field still shows 0; the note no longer says "Using the standard amount" |
| 7 | Test1 | Open New Items | Nothing, or far fewer, lines are under "Smaller things"; small lines are now in the main list. Record what moved. Items already accepted (if any) did not change |
| 8 | Test1 | Click **Only larger purchases**, **Save** | Field shows 250; Saved. New Items now puts more lines under "Smaller things" than at the standard amount. Record the count |
| 9 | Test1 | Type 100001 and **Save** | Refused with "Choose an amount from 0 to 100,000."; nothing saved; the previous value is still there after a reload |
| 10 | Test1 | Type -5 and **Save** | Same refusal; nothing saved |
| 11 | Test1 | Clear the field completely and **Save** | Handled sensibly (a message, or treated as the standard amount); no error page. Record which |
| 12 | Test1 | Type 20 and **Save**, then open New Items | Lines of $20 or more are not demoted on price; lines under $20 with a small-line reason are. Check against the receipt prices you recorded |
| 13 | Test1 | Click **Use the standard amount** | Saved; the note says "Using the standard amount, $50.00." again; New Items matches step 3 |
| 14 | Test2 | Open Settings, **What to track** | Shows the standard amount, not Test1's last value (set Test1 to 250 first if step 13 reset it) |
| 15 | Test2 | Open New Items | Test2's own list only; nothing from Test1's receipt |
| 16 | Test1 | Sign out, sign in, open **What to track** | Test1's saved value is still there (it follows the person, not the browser) |

Also record: the exact label for each button and message, whether a line's reason text mentions the amount you set, and any page slow to load (over 3 seconds).
