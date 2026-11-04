# What changed in push 10: feedback notifies the administrator (2026-11-04)

For GrokBot. API `eef82e3`, UI unchanged (`90106c7`). No migration. Check `/api/version` and record it. Push 9 (Scenario 51) is still the main run; this is a small addition.

| Change | What you should see |
|---|---|
| Admin notice on feedback | Sign in as Alice (customer), footer **Send feedback**, send a Problem with a long message (over 120 characters). Then sign in as the administrator: the bell has a new notice titled **New feedback: problem** (or suggestion / question), whose text is the first 120 characters followed by an ellipsis, with an **Open feedback** link to `/admin/feedback` |
| Queue count | The admin feedback queue shows the message and its "N new" count went up by one |
| Customer side | Alice gets no notification for her own message; her feedback list is as before |
| In the app only | No email is sent |

## Decided, do not report
- Every administrator is notified of every message; there is no per-administrator opt-out yet.
