# UAT retest: build e5b588a (pushes 10 and 11)
Date: Nov 4 2026, ~7:20-7:25 AM ET. API e5b588a (Staging), UI redeployed 7:20 AM ET. Mode: Full-only (browser). No reset; continued from Alice's Scenario 51 data on 18dec35 (tablet plan cancelled, refund not recorded; phone plan ended).

**Totals: 3 Pass, 2 Partial, 0 Fail, 1 Not checked**

| Row | Grade | Notes |
|---|---|---|
| A1 push 11, S51 step 13: Home plan tile | Pass | Cancelled and ended plans not counted as running. With no plan running the Protection plans tile is hidden, so no "N running" line to quote. Row: "0 Return windows closing, 0 Ending in 30 days, 0 Ending in 60 days, 1 To do, 0 Need info" |
| A2 push 11, S51 step 11: plan refund on item and Home | Pass | Item Money recovered: "$79.00 · Plan refund · Nov 4, 2026, card, UAT Tablet Plan: change it on the plan", link opens the plan; no edit/remove buttons. Home "$79.00 on 1 item". First item load showed stale "Nothing recorded yet" until reload |
| A3 push 11, S51 step 12: change refund | Partial | One entry, now $75.00; Home "$75.00 on 1 item". Plan page has no link to change a recorded refund (buttons: Edit plan, Delete plan, Cover items, Re-open this plan); only ?refund=1 reaches the form (pre-filled 79) |
| B1 push 10: Alice sends feedback | Pass | "Thank you. We received your message."; listed once as Problem, Received; Alice's bell has no notice about it |
| B2 push 10: admin notice | Partial | Ops bell: "New feedback: problem", text cut at exactly 120 characters plus "…". "Open feedback" is not in the bell dropdown; it is a button on /notifications and lands on /admin/feedback ("1 new · 1 shown", message Received). Count before sending not observable |
| B2 no email | Not checked | Admin inbox not checked for an email |

## Notes
- Ops signed in with password and two-step code; no recovery code used.
