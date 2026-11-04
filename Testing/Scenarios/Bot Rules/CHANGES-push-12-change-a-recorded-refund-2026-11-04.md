# What changed in push 12: change a recorded refund from the plan (2026-11-04)

For GrokBot. UI only; API stays at `e5b588a`. No migration. Re-run Scenario 51 step 12.

| Change | What you should see | Your row |
|---|---|---|
| Change the refund link | On a cancelled plan that has a refund recorded, the cancel line ("Cancelled ..., refunded $79.00") ends with **Change the refund**. It opens the refund step pre-filled with the saved amount, date and method; saving replaces the one entry (Home and the item's Money recovered show the new amount) | A3 / S51 step 12 |

## Decided, do not report
- **Open feedback in the bell (B2):** the bell dropdown shows the notice text only; the **Open feedback** button is on the notifications page. Same for every notification type.
- **Stale "Nothing recorded yet" on first item load (A2):** the UI was redeployed during your run, so the first load used the old page; it is gone after a reload. Report it again only if it shows on a build you did not redeploy mid-run.
- **No email for feedback (B2):** by design, in the app only; nothing to check.
