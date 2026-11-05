# What changed in push 22: Read it offers the optional coverage; a missed to-do reads Missed (2026-11-05)

For GrokBot. API `bb416b8` and UI `97bcb77`; check `/api/version` and record the `commit` you see (it must be `bb416b8`). The migration `AiUsageError` is applied to the staging database. This follows your push 21 retest (Scenario 54 Part B steps 16b and 19).

## Fixed
| Where | What |
|---|---|
| Step 16b: item page, **Edit > Receipts and files > Read it** on a warranty file that came with the purchase | Read it now offers the optional coverage. Before, it said "Nothing to add" because the file belonged to the purchase and was not found. The choice screen appears after you close the facts panel: the base coverage is not offered again (it is already on the item) and the optional 3-year coverage is unticked. Tick it and press **Add**: it is added beside the base one with its to-do, and nothing is doubled |
| Step 19: closed to-dos | A registration to-do closed because the deadline passed now reads **Missed** with the line "The registration window ended <date>, so this was closed as missed...". One you set aside yourself with Not applicable still reads Not applicable |

## Retest
1. **Step 16b**: Add a purchase with `edge-registration-required.pdf`, accept only the 90 days. On the item page open **Edit > Receipts and files**, press **Read it** on the file, close the facts panel (it may say "Nothing to add"; that is about the item's details, not the warranty), then tick the optional coverage and **Add**. Expect two coverages ("3 years if you register by <date>. Not counted yet.") and one to-do "Register <item> by <date>..."; pressing Read it again must not add it twice.
2. **Step 19** again: move the clock to 2026-11-25 and open the To-dos page, then the closed list. Expect the entry labelled **Missed** with the missed sentence.
3. The 15-second Undo toast from push 21 is still unchecked: if you can catch it, say how long it stayed.

## Also in this build (not for scenarios)
- A failed document read now keeps the provider's error in the usage ledger. If the reader fails on staging, report the time so the cause can be read.
- Test-only sweep triggers exist for the scheduled jobs. See `Testing/Scenarios/Sweeps/README.md`; they are not part of Scenario 54.

## Not changed, do not report as new
- Reopening a done registration to-do does not undo "I registered": the coverage's Undo does that.
- Not built: shared policies with a registration rule; adding the optional coverage by typing it in; yearly check-in, given away or sold, proof list, component lifetime.
