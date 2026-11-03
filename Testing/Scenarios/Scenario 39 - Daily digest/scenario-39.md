# Scenario 39: Choose the daily digest and get one email instead of several

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** The app runs with `Clock:Simulated=true` and a `Maintenance:Key` (as in Scenario 24); the bot has the key and the API address from `RUN-CONFIG.md`, and the simulated clock is at offset 0 at the start. Reminder emails go to the test mailboxes. Both accounts exist (Scenario 25) and are clean (no items). Test1's profile time zone is America/New_York and reminder time is the default (9:00).
**Time:** 40 min
**Built per:** S4.2.1 to S4.2.4, first slice: a per-type choice "At once" or "In my daily digest" on the four digest-able types, an hourly digest job that sends one email per person at their own reminder time, an urgent bypass for coverage notices with 3 or fewer days left, and a burst collapse. The digest job is run on demand with `POST /api/maintenance/run-digest`. NOT built, so not planned: a weekly digest, overdue to-dos that never had a reminder appearing in the digest.
**Why this plan:** the digest holds back emails the person would otherwise get at once. It must hold only what they chose, send exactly one email a day, never send something twice or lose it, and never let an urgent notice wait.

Maintenance calls use header `X-Maintenance-Key`. Clock: `POST /api/maintenance/clock/advance` with the number of days (as in Scenario 24), `POST /api/maintenance/run-reminders`, `POST /api/maintenance/run-digest`. Record each response text exactly.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open Settings > Notifications | A "Daily digest" row with a switch (on by default) and a note saying when it arrives and what it holds. The four types (Return window closing, Warranty expiring, Extended plan expiring, Info needed) each have a choice **At once** / **In my daily digest**, default At once |
| 2 | Test1 | Add an item **"UAT Digest One"**, Best Buy, today, with its return window (the suggested 14-day coverage ticked) | Saved. Note the window end date |
| 3 | Test1 | Set **Return window closing** to **In my daily digest**; reload | The choice is kept |
| 4 | (maintenance) | Advance the clock so that 7 days of the window remain; run `run-reminders` | The response says the reminder ran. Test1 gets an **in-app** notification "UAT Digest One: return window ends in 7 days". **No separate email** for it arrives in Test1's inbox |
| 5 | (maintenance) | Run `run-digest` | Response like "Digest run: sent 1, skipped N (…), failed 0." If Test1 is "not their digest time yet", set Test1's reminder time earlier in Settings and run it again; record this |
| 6 | Test1 | Open the inbox | **One** email, a digest, listing UAT Digest One's return window ending in 7 days with a link to the item, plus manage and unsubscribe links. Record the subject and exact wording |
| 7 | (maintenance) | Run `run-digest` again, on the same simulated day | Sent 0 (already sent today). No second email |
| 8 | (maintenance) | Run `run-reminders` again | Nothing new for the same item and day; no duplicate |
| 9 | Test1 | Add **five** items today at Best Buy, "UAT Burst 1" to "UAT Burst 5", each with its return window. Advance the clock to 7 days before their end; run `run-reminders` then `run-digest` (next simulated day) | **One** digest email. The five return windows are collapsed into one line such as "5 return windows are closing" (more than 3 of one kind collapse), not five lines |
| 10 | Test1 | Add **"UAT Urgent"**, Best Buy, today, with its window. Advance the clock to 2 days before its end; run `run-reminders` | An **email arrives at once** for UAT Urgent ("ends in 2 days") even though the type is set to the digest: urgent notices (3 days or fewer) are never held. Run `run-digest`: it does not repeat that item |
| 11 | Test1 | Turn the **Daily digest** master switch **off** in Settings > Notifications | The type choices are kept but nothing is held from now on |
| 12 | Test1 | Add **"UAT Instant"**, Best Buy, today. Advance the clock to 7 days before its end; run `run-reminders` | A separate email arrives at once (nothing is held when the master switch is off) |
| 13 | Test1 | Turn the master switch **on**, then set **Return window closing** back to **At once** | Choices saved. A new reminder after this arrives as a separate email |
| 14 | Test2 | Check Test2's settings and inbox throughout | Test2's choices are At once, Test2's inbox received none of Test1's digests or reminders, and Test2 sees none of Test1's items |
| 15 | Test1 | Click **unsubscribe** or **manage** in a digest email | The preferences page opens for Test1 without exposing anything of Test2's. Return it to its original state |
| 16 | (maintenance) | Reset the clock (`clock/reset`) | "Offset 0 day(s)" |

Also record: the exact response of every `run-digest` and `run-reminders` call, the digest email's subject and sender, whether the in-app notification exists for held items, and whether the digest arrives at the profile reminder time or at once when run. If `run-digest` returns 404, the simulated clock is not on: stop and report it.
