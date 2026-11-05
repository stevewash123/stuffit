# What changed in push 21: the missed registration to-do closes when you look, plain late-date message, longer Undo (2026-11-05)

For GrokBot. API and UI; check `/api/version` and record the `commit` you see. No migration. This follows your push 20 retest (Scenario 54 Part B).

## Fixed
| Where | What |
|---|---|
| To-do list, item page (step 19) | After the registration deadline, an unregistered optional coverage's to-do is now **closed as missed** (shown under closed, text "The registration window ended <date>, so this was closed as missed...") as soon as the to-dos are opened. Before, it waited for the daily job and read "Overdue" |
| **I registered** with a day after the deadline (step 19b) | The banner now says "That day is after the deadline (Nov 19, 2026). Give the day you registered, or leave this coverage as not earned." (item page and to-do). It no longer reads "One or more validation errors occurred." |
| Undo after **I registered** | The toast with the Undo button now stays 15 seconds (it was 5). The Undo button on the coverage itself stays for the rest of the visit, as before |

## Retest
1. Scenario 54 Part B **step 19**: with the optional coverage never marked registered, move the clock to 2026-11-25 and open the item page and the To-dos page. Expect "Not earned: the registration window ended Nov 19, 2026", the 90 days still counting, and the to-do **not** in the open list; it is under closed with the missed text. You do not need to run the daily job.
2. **Step 19b**: press **I registered** with 2026-11-22 (from the coverage and from the to-do). Expect the plain "after the deadline" sentence above, and the coverage stays Not earned. Then 2026-11-10 with the confirm box still activates it.
3. **Step 18**: press Undo on the toast within 15 seconds; or use the coverage's own Undo button.
4. Please also run **step 16b** (not checked last time): remove the item, add it with the optional coverage unticked, then **Read it** from the item page. Expect the optional coverage and its to-do to appear beside the base one, with nothing doubled.

## Not changed, do not report as new
- Reopening a done registration to-do does not undo "I registered": the coverage's Undo does that. Left as it is; the message "You have already said you did this." is the intended answer.
- The list refresh after **I registered**: not reproduced here. If the item page still shows "Not counted yet" after the toast, say which screen you pressed it on (item page or to-do list) and report it.
- Not built, as before: shared policies with a registration rule; adding the optional coverage by hand; yearly check-in, given away or sold, proof list, component lifetime.
