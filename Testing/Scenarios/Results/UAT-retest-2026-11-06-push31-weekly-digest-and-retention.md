# UAT retest, 2026-11-06: Push 31 steps 2–7 (weekly digest and notification retention), run on Carol

**Build:** API `14fa6e8` (`/api/version`, started 7:42 PM ET), which includes Push 31. **Host:** https://stuffit-ui.onrender.com/api. The maintenance key from env `MAINT_KEY` was sent in `X-Maintenance-Key` and never printed.
**Approval:** at 10:21 PM ET Steve approved moving the clock and sending digest emails for Push 31 steps 2–7, for this run only.
**Account:** Carol (stevewash123.tester3@gmail.com, account `01a1ab5b-94a4-727c-b509-02ee753bbd2c`). Time zone America/New_York; `reminderTime` is null, so the default digest time applies (the API doesn't return that default). Every Friday run was at about 10:28 PM local time, which is after any default digest time.
**Why Carol and not Alice:** at about 10:23 PM ET I tried one Alice sign-in with env `QA_NEW_PASSWORD_ALICE` and got **401** "Invalid email or password". That adds **one** to Alice's failed sign-in count. I didn't try `QA_PASSWORD_ALICE`, because it already failed on Nov 5. I didn't reset Alice's password. Steve said earlier that Alice or Carol is fine, so the run was moved to Carol, whose password worked today.
**Sign-ins:** one Carol API sign-in (200) at 10:23 PM ET, with the token reused for every call. No further sign-ins.
**Inbox:** Carol's Gmail (connector tester3), read only.
**Not touched:** Alice (apart from the one failed sign-in above), Bob, Ops, the P32 fixtures, and the SWEEP Reminder Kettle fixture.

## Grades
| Step | Grade | One-line reason |
|---|---|---|
| 2 Weekly setting + held notices | **Pass** | Both types saved as weekly on Friday. 5 warranty notices were `held`, and no email was sent for them |
| 3 Friday digest, once per week, not on other days | **Pass** | Friday: `sent 1 (1 weekly)`, one email, and an in-app "Weekly digest". A second run the same day sent 0. Saturday sent 0. Monday: `skipped 1 (not their weekly day)` |
| 4 More than 3 of one type become one line with a link | **Pass** | "6 warranties are ending", linking to https://stuffit-ui.onrender.com/items |
| 5 A notice with 3 days or less is sent at once | **Inconclusive** | The reminder job never produced a warranty notice with 3 days or less left, so the bypass could not be exercised. See Needs CC 3 |
| 6 Weekly digest email off: no email, in-app still appears | **Fail** | No email (pass), but **no in-app weekly digest was created** even though In-app was on. Side effects listed below |
| 7 Retention | **Partial** | `NotificationsPurged = 1`: the old read notice was removed, and the unread, held and recent-digest notices stayed. No pending-action notice existed, so that case wasn't checked |

**Trigger name:** `POST /maintenance/run-digests` returns **401** with the key (called 6 times, no effect). `POST /maintenance/run-digest` works (200). The Push 31 notes say `run-digests`, and that's wrong.

## Run 1 (10:27:15–10:27:29 PM ET), mostly void for the digest checks
Run 1 called the digest through `run-digests`. That got 401, so **no digest ran in run 1**. What run 1 still showed:
- Setup and step 2: `PUT /notification-preferences/warranty_expiring {mode:weekly, weeklyDay:friday}` and the same for `todo_reminder`, both 200. A GET showed both as weekly with `weeklyDay: friday`, so they share one day. I created P31 Held Toaster 1–5, with warranties ending 2026-11-16. `run-reminders` at offset 0 (10 days left) sent 0. At +3 (sim Mon Nov 9, 7 days left) it sent 5. All 5 notices had `emailStatus: held` and `emailSentAt: null`, for example `01a1b40b-e289-7601-af8b-ac7a93b1aaea` (Toaster 1). **No Toaster email ever reached Carol's inbox.**
- Monday digest (`run-digest`, the only time run 1 used the right name): `Digest run: sent 0, skipped 1 (not their weekly day: 1), failed 0`.
- **Urgent check:** at +7 I added P31 Urgent Blender, with a warranty ending 2026-11-15 (2 days left). `run-reminders` sent 0 and **no notice was created**. The Toasters, at 3 days left, got no further reminder either.
- **Weekly digest email off, then two new weekly-type notices:** at +9, P31 Week2 Kettle A and B (7 days left) were **emailed at once** (`emailStatus: sent`). Gmail `1a1b40bf9a20c6c1` (A) and `1a1b40bf89ccc5f1` (B), both 10:27:25 PM ET. This happened while `warranty_expiring` was still set to weekly.
- Run 1 retention at +105: `NotificationsPurged = 0`. Toaster 1 (read at sim Nov 20) was 91 days old but still `held`, because no digest had run. "Held is never removed" held true.
- Run 1 cleanup: the clock was reset in `finally` (Offset 0 at 10:27:29 PM ET) and the preferences were restored and checked against the originals. A leftover from run 1: notice `01a1b40c-023a-7e1a-a68c-7e2579b50892` (P31 Held Late Lamp) was created at sim time Feb 20, 2027, still `held` when the clock was reset.

## Run 2 (10:28:18–10:28:27 PM ET), using `run-digest`
| # | Sim day | Call | Evidence | Result |
|---|---|---|---|---|
| Pre | +0 | GET clock | Offset 0 | — |
| Pre | +0 | run-digests | 401 (name check) | Notes doc wrong |
| S2 | +0 | PUT warranty_expiring and todo_reminder weekly/friday | 200, 200. GET: both `weekly`, `friday` | Pass |
| — | +0 | Fixtures P31b Week3 Mixer A/B (end Nov 22), C (end Nov 23), P31b Recent Fan (end Feb 19 2027), P31b Late Lamp (end Feb 26 2027) | all 201 | — |
| S3 | +7 Fri Nov 13 | run-digest | `Digest run: sent 1 (1 weekly), skipped 0, failed 0.` | Pass |
| S3 | +7 | GET notifications | `01a1b40c-d660-7f5c-8f88-9fbf30c9f2f5` typeLabel **Weekly digest**, "6 things need your attention this week", unread | Pass |
| S3 | +7 | Gmail | `1a1b40cd8e86b6a4`, "6 things need your attention this week", **10:28:22 PM ET**, the only email from that run | Pass |
| S4 | +7 | email body and payload | `- 6 warranties are ending: https://stuffit-ui.onrender.com/items` (HTML: a single `<li><a href=".../items">`). Payload `count 6`, `lines "6 warranties are ending\t/items"`. The 6 are Toasters 1–5 and run 1's held Late Lamp notice; all 6 went from `held` to `sent` | Pass |
| S3 | +7 | run-digest again, same week | `sent 0, skipped 0, failed 0`. No new notice and no email | Pass |
| S3 | +8 Sat | run-digest | `sent 0, skipped 0, failed 0` | Pass |
| S6 | +9 Sun | run-reminders (weekly email still ON) | Sent 2. Mixer A `01a1b40c-da08-78a4-b0d5-1198d12de268` and Mixer B `01a1b40c-da08-7e7a-af67-de859d48f530` both `held` | — |
| S6 | +9 | PUT weekly_digest `{email:false}` | 200 | — |
| S6 | +10 Mon | run-reminders (weekly email OFF) | Sent 1. Mixer C `01a1b40c-dca9-7abb-a7d8-d887c2b752ed` **emailed at once** (`sent`). Gmail `1a1b40ce09f6b690`, 10:28:24 PM ET | Observation (Needs CC 2) |
| S6 | +14 Fri Nov 20 | run-digest | `sent 0, skipped 1 (weekly digest email is off: 1), failed 0.` No weekly email in Gmail | Pass (no email) |
| S6 | +14 | GET notifications | **No new Weekly digest notice.** The only weekly_digest notice is still the +7 one. Mixer A/B went from `held` to **`none`**, so they were never emailed and never listed | **Fail** (in-app expected) |
| S6 | +14 | PUT weekly_digest `{email:true}` | 200, restored | — |
| S7 | +14 | Toaster 1 already read | readAt = sim Nov 20 2026 (from run 1) | — |
| S7 | +98 Fri Feb 12 2027 | run-reminders | `Sent 2, Cancelled 3`. Recent Fan (7 days) and Late Lamp (14 days, which shows there is a 14-day lead as well as the 7-day one), both held | — |
| S7 | +98 | run-digest | `sent 1 (1 weekly)`. Notice `01a1b40c-e2b4-7ebb-81ca-c94969af60c3` "2 things need your attention this week", listing both items as separate lines with /items/{id} links (3 or fewer, so not consolidated). Gmail `1a1b40ce75a44607`, 10:28:26 PM ET | Pass (also step 3/4 control) |
| S7 | +105 Fri Feb 19 2027 | run-reminders | Sent 1. Late Lamp 7-day notice `01a1b40c-e4c3-7c23-a3a9-4a00445710f0` `held` (no digest was run that day) | — |
| S7 | +105 | run-retention | `RetentionRunSummary { NoticesSent = 0, PurchasesCleared = 0, FilesRemoved = 0, NotificationsPurged = 1 }`. Count 18 → 17 | Pass |
| S7 | +105 | what was removed | Toaster 1 `01a1b40b-e289-7601-af8b-ac7a93b1aaea` (read, 91 days) is **gone** | Pass |
| S7 | +105 | what was kept | **Unread:** Toasters 2–5 (created sim Nov 10, about 101 days, unread). **Held:** `01a1b40c-e4c3…`. **Recent digest:** `01a1b40c-e2b4…` (7 days). Also kept: the +7 digest `01a1b40c-d660…` (98 days, unread), the export notice, and the SWEEP Kettle notice | Pass |
| S7 | +105 | pending-action notice | Carol had none, and the brief allowed only new P31 fixtures, so this case wasn't checked | Not run |
| S7 | +105 | run-retention again | `NotificationsPurged = 0` | Pass |
| End | → 0 | `clock/reset` in `finally`, then GET | "Back to real time. Offset 0", then GET **Offset 0** at 10:28:27 PM ET. A separate GET at 10:29:17 PM ET also showed **Offset 0** | Pass |
| End | — | Preferences restored | warranty_expiring and todo_reminder set back to `instant` with weeklyDay null, weekly_digest email on. **The categories JSON is identical to the original snapshot** (`prefs-original.json`) | Pass |

## Emails sent to Carol's test inbox this run (5, all from noreply@stuff.microsaasbuilders.com)
| Gmail id | Time (ET) | Subject | Why |
|---|---|---|---|
| `1a1b40bf9a20c6c1` | 10:27:25 PM | P31 Week2 Kettle A: manufacturer warranty ends in 7 days | run 1, weekly digest email off, so sent at once |
| `1a1b40bf89ccc5f1` | 10:27:25 PM | P31 Week2 Kettle B: manufacturer warranty ends in 7 days | same |
| `1a1b40cd8e86b6a4` | 10:28:22 PM | 6 things need your attention this week | run 2 weekly digest at +7 |
| `1a1b40ce09f6b690` | 10:28:24 PM | P31b Week3 Mixer C: manufacturer warranty ends in 7 days | run 2, weekly digest email off, so sent at once |
| `1a1b40ce75a44607` | 10:28:26 PM | 2 things need your attention this week | run 2 weekly digest at +98 |
No Toaster, Mixer A/B, Recent Fan, Late Lamp or Blender email was sent on its own.

## SWEEP Reminder Kettle (left alone)
Its notice `01a1b331-0c89-7309-b9b2-76a3b82d1db2` (from the earlier sweep) was unchanged. The fixture produced no new notices or emails during either run, and retention kept the notice.

## Fixtures left on Carol (all new; purchase / item / coverage)
| Name | Purchase | Item | Coverage | Warranty end |
|---|---|---|---|---|
| P31 Held Toaster 1 | `01a1b40b-d3ba-7cef-bb43-68a19cc31e7f` | `01a1b40b-d3ba-7af2-9fdc-0e173b6c321f` | `01a1b40b-d5b6-7388-9d1f-18d65de4d12a` | 2026-11-16 |
| P31 Held Toaster 2 | `01a1b40b-d682-71bc-b876-81fa9fb3ab05` | `01a1b40b-d682-7746-a181-42074459c7f9` | `01a1b40b-d87f-7a1f-b8ce-6efa6f83f507` | 2026-11-16 |
| P31 Held Toaster 3 | `01a1b40b-d9a4-729a-8f20-5211287f5f18` | `01a1b40b-d9a4-7a1e-963c-4625d5e065c8` | `01a1b40b-db6a-77ca-acdc-b9eb2863ae52` | 2026-11-16 |
| P31 Held Toaster 4 | `01a1b40b-dc30-7239-9bc9-a46220c6a611` | `01a1b40b-dc31-7f81-8c32-4fde7009061f` | `01a1b40b-ddf3-7fd7-9d16-b8b05350ce28` | 2026-11-16 |
| P31 Held Toaster 5 | `01a1b40b-deb8-734c-b693-e6f966417ecb` | `01a1b40b-deb8-7439-b25b-2d4f75de8eb2` | `01a1b40b-e056-7521-bf1e-3f76db57d861` | 2026-11-16 |
| P31 Urgent Blender | `01a1b40b-e9a2-77ea-a48c-dc40b0ea64e0` | `01a1b40b-e9a3-7d8f-8c79-e682bb13af66` | `01a1b40b-eb77-7810-a773-bac03e9c593d` | 2026-11-15 |
| P31 Week2 Kettle A | `01a1b40b-eedb-7e92-b43e-e0a92b286c92` | `01a1b40b-eedb-7619-8e15-97b6361979e6` | `01a1b40b-f12f-7423-831e-35b2c55574e7` | 2026-11-22 |
| P31 Week2 Kettle B | `01a1b40b-f1f5-783a-a463-2069333bd708` | `01a1b40b-f1f5-74ed-8bd7-fc615ddd176d` | `01a1b40b-f389-7777-b945-bef1fc6d2661` | 2026-11-22 |
| P31 Recent Fan | `01a1b40b-fad8-79a0-8cbd-8c34607d1849` | `01a1b40b-fad8-7c07-80af-c032b4b8f55a` | `01a1b40b-fc90-7955-a914-473f25672d92` | 2027-02-19 |
| P31 Held Late Lamp | `01a1b40b-ff0c-71a0-8e3c-a6e95db7ee03` | `01a1b40b-ff0d-7ac6-b3d1-c317163d37a1` | `01a1b40c-00ce-7d95-9b80-1398a3aaee2b` | 2027-02-26 |
| P31b Week3 Mixer A | `01a1b40c-c7d8-7d2d-a1a1-0d80fb7c1c21` | `01a1b40c-c7d9-73e9-a3f4-1920848a9f5e` | `01a1b40c-c97b-73c8-8e1b-de73245aaf5b` | 2026-11-22 |
| P31b Week3 Mixer B | `01a1b40c-ca39-7766-869f-2cc5cd9f77a5` | `01a1b40c-ca39-76e8-b1ce-79e4d82c7cd4` | `01a1b40c-cbbd-7e30-9b8e-1528b1130f0e` | 2026-11-22 |
| P31b Week3 Mixer C | `01a1b40c-cc71-7181-bb31-18088d6ae2c7` | `01a1b40c-cc72-7b6e-88d6-9c19e25afc2a` | `01a1b40c-ce15-7fd6-acd9-6dde5cde0de8` | 2026-11-23 |
| P31b Recent Fan | `01a1b40c-cec8-7c3d-aa10-458f9b652b95` | `01a1b40c-cec9-7eff-b4bc-4ae807f7076b` | `01a1b40c-d066-759a-8f9c-307f5a800226` | 2027-02-19 |
| P31b Late Lamp | `01a1b40c-d11c-7a8c-8827-2953caf3122e` | `01a1b40c-d11c-7aa8-846d-4845dea91d1d` | `01a1b40c-d312-7674-b92a-bc1557ba0325` | 2027-02-26 |
Carol now has 17 notifications. Many carry simulated future `createdAt` dates (Nov 10 2026 to Feb 20 2027). One notice, `01a1b40c-e4c3…` (Late Lamp), is still `held` even though warranty_expiring is back to `instant`.

## Needs CC
1. **Fail, step 6:** with Weekly digest set to Email off and In-app on, the Friday run answered `skipped 1 (weekly digest email is off)` and created **no in-app "Weekly digest" notice**. The notes say the in-app notice should still appear.
2. **Question, step 6 behaviour:** while Weekly digest email is off, new weekly-type notices are **emailed at once** (Kettle A/B, Mixer C), but notices already held when it was switched off are dropped to `emailStatus: none`, so they are never emailed or listed (Mixer A/B). Is "send at once when the weekly digest email is off" intended? If so, should already-held notices be sent then, rather than dropped?
3. **Step 5 can't be tested through reminders:** warranty reminders seem to come only at 14 and 7 days before the end. A warranty added with 2 days left (P31 Urgent Blender) got **no notice at all**, and the held items got none at 3 days or 1 day left. Give a way to create a notice with 3 days or less (or name the urgent types), or confirm whether a late-added warranty should get a catch-up reminder.
4. **Doc fix, Push 31 notes:** the trigger is `run-digest`. `run-digests` returns 401 with a valid key. sweeps/README already says `run-digest`.
5. **Minor:** a held notice created at a later simulated time (run 1's Late Lamp, sim Feb 20 2027) was included in the Nov 13 digest after the clock reset. This only happens when the clock is moved back, but it inflated the count to 6.
6. **Not covered:** the pending-action notice in step 7 (Carol had none). The 365-day unread/important purge wasn't run either.
7. **Cleanup:** the 15 P31/P31b fixtures above and 5 test emails in Carol's inbox. Alice's failed sign-in count is now 1, and the right Alice password for `QA_NEW_PASSWORD_ALICE`/`QA_PASSWORD_ALICE` needs confirming.

## Clock
The final state is **Offset 0**: reset in `finally` and checked by GET at 10:28:27 PM ET, and again at 10:29:17 PM ET.

Logs (no secrets): `/workspace/work/p31/run-20261106.log`, `run2-20261106.log`, `prefs-original.json`, `prefs-final.json`, `fixtures.json`, `fixtures2.json`.
