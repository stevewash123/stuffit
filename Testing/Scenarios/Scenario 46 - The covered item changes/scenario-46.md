# Scenario 46: Returned, replaced, sold: what happens to the plan

**DEFERRED until implemented: S3.4.16 (and S3.4.15).** Do not run before then. Steps that need a not-yet-built screen say what to look for and will fail on build 982952c.

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Test1 has four items, each with its own one-item Geek Squad 3-year plan ($120): "UAT A Returned", "UAT B Replaced", "UAT C Sold", "UAT D Deleted".
**Time:** 40 min
**Built per:** S3.4.16, S3.4.15, S2.4.13, S5.4.20, S3.4.8 (requests, for the replacement path).
**Why this plan:** plans outlive or die with their items in different ways; a silent drop or a silent keep each costs the person money or coverage.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | UAT A: Mark returned | Asks "Did you return the plan too?": Yes refunded / Yes no refund / No I'm keeping it / Not sure. Default Yes refunded when the plan type says it is refunded with the item |
| 2 | Test1 | Choose Yes, refunded: $120 | Plan ends on the return date, "Cancelled <date>, refunded $120"; Money recovered shows item refund and plan refund once each |
| 3 | Test1 | Repeat on another item and choose No, I'm keeping it | Plan stays, flagged "covers an item you returned"; to-do to cancel or move it |
| 4 | Test1 | UAT B: Replaced by the plan | Creates the replacement (brand, model, serial editable, today) and asks: continues / ends / restarts. Choose continues |
| 5 | Test1 | Open the replacement and the old item | Replacement shows the plan with the original dates; old item marked replaced with history and files kept; the plan lists the replacement |
| 6 | Test1 | Repeat on another item and choose restarts | New term from the replacement date; old term kept in the plan's history |
| 7 | Test1 | UAT C: mark sold or given away | Asks about the plan: cancel if not transferable, or leave it with the new owner if transferable; other covered items keep the plan |
| 8 | Test1 | UAT D: delete the item | Asks before dropping it from the plan, naming the plan |
| 9 | Test1 | Remove every item from a one-item plan | Shows "Covers nothing" with Add items / Cancel / Keep |
| 10 | Test1 | Undo one answer within the session | Plan and coverage match the before state |
| 11 | Test1 | Clock to a plan's renewal while its item is returned | No renewal reminder for it; the reminder asks about the item first |
| 12 | Test2 | Check Test1's items and plans | Not visible |

Also record: any item still showing a plan after it was removed, any plan still listing a returned item, and any refund counted twice.
