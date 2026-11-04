# Scenario 51: Cancel a plan and record the refund

**Built per:** S3.4.15 (cancel a plan and get the refund), push 9. The waiting period, decision panel and "bought later" parts of Scenario 45 are not built and stay deferred there.

**Accounts:** Alice and Bob after a DB Stager scenario reset. Alice has "UAT Phone" ($900) and "UAT Tablet" ($500), bought 10 days ago. Clock offset 0.
**Time:** 30 min

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Alice | Add a protection plan on UAT Phone: company typed in, yearly $120, starts 10 days ago, 12 months, **renews automatically**, contract number, claim phone | Plan card on the item; Protection plans lists it Active |
| 2 | Alice | Plan page: look at the buttons | **Cancel this plan** is separate from **End this plan** |
| 3 | Alice | Cancel this plan | "What do you want to do?": **Stop it renewing**, **Cancel it now**, **It already ended or I cancelled it** |
| 4 | Alice | Choose Stop it renewing | Shows what is saved: the plan's cancellation terms if any, or "No cancellation terms saved for this plan."; contract number with Copy; claim phone and website; "Check your contract for any cancel-for-refund window." Nothing says what Alice is entitled to |
| 5 | Alice | Confirm | Plan page and item: "Ends <date> (will not renew)"; "renews automatically" no longer shown; the renewal to-do now reads "ends on ... Renew or replace it", not "renews on ... Cancel or compare"; coverage still runs to the end date |
| 6 | Alice | Add a second plan on UAT Tablet: $79 one payment, 2 years, starts 5 days ago, no auto-renew | Active. **Stop it renewing** is not offered for it |
| 7 | Alice | Cancel it now, date today, "How": by phone | Confirmation with **Undo** (10 seconds) and a **Record a refund** step |
| 8 | Alice | Press Undo within 10 seconds | Plan Active again with its original end date; the tablet's coverage restored; no refund to-do |
| 9 | Alice | Cancel it now again; at the refund step press "I haven't got it yet" | Plan reads **Cancelled** (expired tone) with "Cancelled <today>, refund not recorded yet" and a Record a refund link; the tablet's coverage ends the day before the cancellation date (last-covered-day rule); a to-do "Check that your refund arrived" is due in 14 days |
| 10 | Alice | Record a refund: amount 0, then empty, then -5 | "Enter an amount greater than zero." each time; nothing saved |
| 11 | Alice | Record a refund: $79, today, by card | "Cancelled <today>, refunded $79.00"; the to-do is done; **Money recovered** shows $79.00 labelled **Plan refund** (not a returned item) |
| 12 | Alice | Record the refund again: $75 | The refund changes to $75; Money recovered still has **one** entry for the plan, now $75 |
| 13 | Alice | Read Protection plans and Home | The cancelled plan is not counted as running; the yearly cost total excludes it; the 60-day count excludes it; My Items filters Has a protection plan / Plan ending soon do not count it; the plan icon is gone from UAT Tablet |
| 14 | Alice | Cancelled plan page: look at the buttons | No Cancel, no End, no Stop covering. **Re-open this plan** and Delete are offered |
| 15 | Alice | Re-open this plan with the note "changed my mind" | Plan Active again; the refund, the Money recovered entry and the refund to-do are gone; coverage back to the original end date |
| 16 | Alice | Choose "It already ended or I cancelled it" on the phone plan | The existing End-this-plan date flow; records the date only, no refund step |
| 17 | Alice | Reload the plan page with `?refund=1` on a cancelled plan | The refund step opens |
| 18 | Bob | Open any of Alice's plan addresses, and call cancel, refund and reopen on one | Not found for all |

Also record: any money figure that disagrees with the arithmetic, any date that disagrees with the simulated today, and any wording that reads as legal advice or says what the person is entitled to.
