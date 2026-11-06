# UAT sweeps, 2026-11-06: export-expiry and reminder-send

**Host:** https://stuffit-ui.onrender.com/api. Maintenance key from env `MAINT_KEY` was sent in the `X-Maintenance-Key` header and never printed. Each script reset the clock in a `finally` block, so the reset ran even if a step failed.
**Clock control:** the maintenance clock endpoints were called directly. DB Stager was not used, because this executor has no SendToAgent.
**Accounts:** Carol `01a1ab5b-94a4-727c-b509-02ee753bbd2c` and Bob `01a1ab5b-46fc-7c6c-bbbf-3cc18c9e0135`. Both log in with Eastern time, `reminderTime` null (default), and warranty_expiring email and in-app on (default, unchanged).
**Not touched:** Alice and Ops. No existing Bob or Carol data was edited or deleted. run-email-retry and run-signup-purge were not run.

## Totals
| Sweep | Pass | Fail | Blocked |
|---|---|---|---|
| Export-expiry (9 steps) | 9 | 0 | 0 |
| Reminder-send, as the doc is written (+10 days, 9 steps) | 4 | 5 | 0 |
| Reminder-send, timing fixed (+18 days, 9 steps + 3 extra checks) | 12 | 0 | 0 |

The 5 failures in the doc-literal run come from the doc's timing, not from the app. The app sends warranty reminders **7 days** before the end date. The doc's +10 days leaves the warranty 15 days out, so nothing was due yet. At +18 days (7 days left) all behaviour passed: the reminder is sent once, only to the account the sweep was run for, and a second run sends no duplicate. Details are in Needs CC.

---
## Sweep 1: export-expiry (Carol), 6:22 PM ET (America/New_York)
| # | Call | HTTP | Evidence | Result |
|---|---|---|---|---|
| Pre | GET clock | 200 | Offset 0 | Pass |
| Setup | login Carol | 200 | the `account_id` in her token matched Carol's account; she had no exports before (`[]`) | Pass |
| 1 | POST /exports | 202 | id `01a1b32c-05b3-71d8-87a8-2a0bd0641a96`, `queued` | Pass |
| 2 | GET /exports/{id} | 200 | `ready`; readyAt 23:22:50Z, expiresAt 2026-11-13T23:22:50Z (+7 days) | Pass |
| 3 | download | 200 | application/zip, 4610 bytes | Pass |
| 4 | clock advance 8 | 200 | Offset 8, app time 2026-11-14 | Pass |
| 5 | download | 404 | problem+json, expired before the sweep ran | Pass |
| 6 | run-export-expiry?accountId=Carol | 200 | `Expired 1 export(s).` | Pass |
| 7 | GET /exports/{id} | 200 | `expired` | Pass |
| 8 | run-export-expiry again | 200 | `Expired 0 export(s).` | Pass |
| 9 | clock reset | 200 | Offset 0; separate GET: Offset 0 at 23:22:55Z | Pass |

Notifications: Carol only got "Your data export is ready". No notification was sent when the export expired.

---
## Sweep 2: reminder-send (Carol = A, Bob = B), 6:27–6:28 PM ET

### Fixtures created (all new, SWEEP prefix, through the app API)
| Account | Purchase | Item | Coverage |
|---|---|---|---|
| Carol | `01a1b330-2cdf-75e6-9658-e1474861526a` (date 2025-12-01, notes "SWEEP reminder-send fixture 2026-11-06") | `01a1b330-2d2a-7024-9863-11217d9a3784` "SWEEP Reminder Kettle (Carol)" $49.99 | `01a1b330-5253-723f-a64a-99d1c95132db` manufacturer, 2025-12-01 → 2026-12-01 (25 days out), 12 months |
| Bob | `01a1b330-36a8-7897-9795-272590b6b43a` (same) | `01a1b330-36a8-7a80-9c5f-51853eadb0e7` "SWEEP Reminder Kettle (Bob)" $49.99 | `01a1b330-56d7-7203-b519-71a6095679d7` same terms |

Created with POST /purchases (201) and POST /items/{id}/coverages (201). They were **left in place**. Before the run: Carol had 1 notification (the export one) and Bob had 0.

### Run A: as the doc is written (+10 days)
| # | Call | HTTP | Evidence | Result |
|---|---|---|---|---|
| Pre | GET clock | 200 | Offset 0 | Pass |
| 1 | advance 10 | 200 | Offset 10, app time 2026-11-16 23:27Z | Pass |
| 2 | run-reminders?accountId=Carol | 200 | `Sent = 0, Failed = 0` | Fail (nothing due yet) |
| 3 | Carol notifications | 200 | no warranty reminder | Fail |
| 4 | Bob notifications | 200 | none | Pass |
| 5 | run Carol again | 200 | Sent 0 | Pass (but proves nothing, since nothing was sent) |
| 6 | Carol notifications | 200 | 0 reminders | Fail |
| 7 | run-reminders?accountId=Bob | 200 | Sent 0 | Fail |
| 8 | Bob notifications | 200 | none | Fail |
| 9 | reset | 200 | Offset 0 at 23:27:48Z | Pass |

### Run B: timing fixed. Stepped +11, +15, +18 days and ran Carol at each, then ran the full checks once something sent
| # | Call | HTTP | Evidence | Result |
|---|---|---|---|---|
| diag | run Carol at +11 and +15 | 200 | Sent 0 both times | info |
| 1 | clock at +18 | 200 | app time 2026-11-24 23:28Z (warranty ends in 7 days) | Pass |
| 2 | run-reminders?accountId=Carol | 200 | `Sent = 1, Failed = 0` | Pass |
| 3 | Carol notifications | 200 | `01a1b331-0c89-7309-b9b2-76a3b82d1db2` warranty_expiring "SWEEP Reminder Kettle (Carol): manufacturer warranty ends in 7 days", unread | Pass |
| 4 | Bob notifications (Bob not run) | 200 | 0 reminders | Pass |
| 5 | run Carol again | 200 | `Sent = 0` | Pass |
| 6 | Carol notifications | 200 | still 1 reminder | Pass |
| 7 | run-reminders?accountId=Bob | 200 | `Sent = 1, Failed = 0` | Pass |
| 8 | Bob notifications | 200 | `01a1b331-109d-78f5-a66f-80c7e8142133` "SWEEP Reminder Kettle (Bob): …ends in 7 days", unread | Pass |
| 8b | run Bob again | 200 | `Sent = 0`; Bob still has 1 reminder, Carol still has 1 | Pass |
| E1 | Carol inbox (Gmail tester3, read only) | n/a | exactly 1 email, id `1a1b331115d3abdb`, from noreply@stuff.microsaasbuilders.com, same subject, 23:28:18Z | Pass |
| E2 | Bob inbox (Gmail tester2, read only) | n/a | exactly 1 email, id `1a1b331122a25bc5`, same subject for Bob, 23:28:19Z | Pass |
| 9 | reset | 200 | "Back to real time. Offset 0" | Pass |

## Clock confirmation
- Export-expiry: separate GET at 23:22:55Z (6:22 PM ET) showed Offset 0.
- Reminder run A: GET at 23:27:48Z showed Offset 0.
- Reminder run B: GET at 23:28:20Z (6:28 PM ET) showed **Offset 0**. This is the final state.

## Needs CC
1. **Doc fix, reminder-send.md:** the app sends warranty_expiring reminders 7 days before the end date, not 15 or more. With a warranty 25 days out, the doc's `advance?days=10` sends nothing. Change it to advance 18 days (or create the warranty about 17 days out and advance 10). If the intended lead time is longer than 7 days, treat this as an app defect.
2. **Question, export-expiry:** no notification is sent when an export expires. Is that intended?
3. **Cleanup:** the SWEEP fixtures listed above remain on Carol and Bob. Each test inbox has one real reminder email.

Logs (no secrets): /workspace/work/sweep-ee-20261106.log, sweep-rs-20261106.log, sweep-rs-diag-20261106.log
