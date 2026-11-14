# Scenario 72: Return window last day, and reminders that fire once

**Accounts:** one **personal** account only (P34 Self, or Alice's personal account if it exists). Do not run this in the shared business P34-Alice Repairs.
**Preconditions:** clock offset **0**, app date **2026-11-11** (America/New_York). Profile time zone **America/New_York**, reminder / digest time the default **9:00** (or set it to 01:00 if you will run jobs when the simulated clock is still early in the day — the reminder job sends at the person's own local time; a run before that time sends nothing). **QA Controller must OK every clock advance.** The clock is global. Reset it to **0** at the end. Reader on, or record **reader off**.
**Time:** about 40 min, plus the clock steps.
**Built per:** Scenario 24 (clock and return reminders); Scenario 40 / the soft-closed return-window note (a closed window hides Start a return and offers a courtesy-return request); push 26 (day terms end N days after the start); push 31 (weekly digest); the reminder-send sweep (no duplicate on the same day; job is per account). UAT of Scenario 24 on builds d1ed2c0 and 982952c found the return-reminder leads are **7, 3 and 1 days**, not the 10 days the draft of Scenario 24 guessed.
**Why this plan:** returning a day late is a real money loss. The window must still be open on the last calendar day in the person's time zone, and closed the next morning. Each lead reminder must arrive once, not twice.

## The story (answer key)

The store is **Amazon**, taken from a read-only look at the development database on 2026-11-11 (America/New_York). The shared, verified, general (no category) seller policy is: `return_days = 30`, `return_from_delivery = false`, no restocking fee, `no_returns = false`, still effective. The stored conditions mention "30 days of delivery" and a **2025** holiday extension (purchases in November and December 2025). This pack uses a purchase on **October 20, 2026**, so it is outside that holiday season, and it counts 30 days from the **purchase date** because the seeded flag is not "from delivery."

| Fact | Main item | Digest extras (for the weekly-digest steps) |
|---|---|---|
| Item name | **UAT S72 Instant Pot Duo** | **UAT S72 Digest Toaster** and **UAT S72 Digest Kettle**, added by hand |
| Store | **Amazon** (seeded, verified 30-day general policy) | Any seeded store, or Amazon |
| Customer on paper | UAT Sample Buyer, 72 Example Lane, Testville, ME 00000, (207) 555-0172 | n/a |
| Purchase date | 10/20/2026 → **2026-10-20** (delivered 10/21/2026 on the paper, not used for the count) | Today at the step they are added (offset 0 is fine) |
| Order # / model | 111-0712047-0172047 / DUO60 V3 | n/a |
| Price / tax / total | $89.99 / $4.95 / **$94.94** (shipping $0.00) | A small amount is enough |
| Return window | 30 days from purchase → **last day 2026-11-19** | Not the focus |
| Maker warranty on the Instant Pot | Optional: Instant Brands, 12 months → **2027-10-20**, still active after the window ends | Typed warranties **ending 2026-12-05** (about 15 days after the Friday digest run) |

Day terms (push 26): 2026-10-20 + 30 days = **2026-11-19**. The last day is inclusive.

### Clock plan (global — QA Controller OK, then reset)

Run reminder and digest jobs **after** the person's reminder / digest time on that simulated day. After every jump, **fully reload** the item page (a stale page after a clock move is a known issue).

| After this advance | Offset | App date (America/New_York) | What to check |
|---|---|---|---|
| (start) | 0 | Wed 2026-11-11 | Window open, **8 days left**. No 7-day reminder yet |
| `advance?days=1` | 1 | Thu 2026-11-12 | **7-day** return reminder, once |
| Same day, run reminders again | 1 | Thu 2026-11-12 | **No second** reminder |
| `advance?days=4` (total 5) | 5 | Mon 2026-11-16 | **3-day** reminder (urgent: sent at once, not held for a digest — push 31) |
| `advance?days=2` (total 7) | 7 | Wed 2026-11-18 | **1-day** reminder ("ends tomorrow") |
| `advance?days=1` (total 8) | 8 | Thu 2026-11-19 | **Last day: window still open.** Start a return still works |
| `advance?days=1` (total 9) | 9 | Fri 2026-11-20 | Window **ended** (soft-closed). Weekly digest Friday, after digest time |
| `clock/reset` | 0 | 2026-11-11 | Required cleanup |

## Files, in the order to use them

Each file is one PDF plus a JPG of its first page with the same name.

| # | File (.pdf + .jpg) | What it is | Who uploads it, and when | Where it goes |
|---|---|---|---|---|
| 01 | `01-receipt-amazon-instant-pot-duo` | Amazon order invoice dated 10/20/2026, with "Return by: 11/19/2026" | The personal-account tester, step 1, offset 0 | Add a purchase / item attachment, Read it |

The digest toaster and kettle have no files; add them by hand.

## Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Tester | Confirm the **personal** account, time zone America/New_York, offset **0**. Add a purchase: attach receipt **01**, Read it. Name it **UAT S72 Instant Pot Duo**. Store **Amazon** | One item, purchase **2026-10-20**, $89.99 (total $94.94). **Return policy 30 days, active, last day Nov 19, 2026** (8 days left). If the app uses the delivery date 10/21 or a 2026 holiday extension instead, **stop, record the actual last day, and slide every later clock step to match** — see open questions. Optional: add a 12-month Instant Brands warranty to 2027-10-20 |
| 2 | Tester | Settings > Notifications: return-window reminders **At once**, email and in-app on. Set **Warranty ending soon** to **In my weekly digest** and pick **Friday**. Add **UAT S72 Digest Toaster** and **UAT S72 Digest Kettle** by hand, each with a typed manufacturer warranty ending **2026-12-05**. Reload settings | The weekday choice stays Friday and is shared by every weekly type (push 31). The digest items are **not** emailed at once for that type (held). If no warranty-ending notice is created yet because the lead is shorter than 24 days, record the lead and continue |
| 3 | QA Controller / Tester | **With QA Controller's OK:** `POST /api/maintenance/clock/advance?days=1`. Confirm offset **1** (Thu Nov 12). After reminder time, `POST /api/maintenance/run-reminders` (account-scoped if that is how you run it). Reload the Instant Pot and Notifications; check mail | Run summary lists a return reminder. Email and bell: along the lines of **"UAT S72 Instant Pot Duo: return window ends in 7 days"** and names **November 19, 2026**. One notice, unread. The window is still open |
| 4 | QA Controller / Tester | Run reminders **again the same simulated day** | `Sent = 0` (or no new return reminder). Still **one** notice, not two (Scenario 24, reminder-send sweep) |
| 5 | QA Controller / Tester | Advance **4** more days (offset **5**, Mon Nov 16). Run reminders after reminder time | **3-day** reminder, once. This is **urgent** (3 or fewer days left) and is sent **at once**, not held for the weekly digest (push 31). Window still open |
| 6 | QA Controller / Tester | Advance **2** more days (offset **7**, Wed Nov 18). Run reminders | **1-day** reminder, once, wording along the lines of **"ends tomorrow"** / ends Nov 19. Window still open |
| 7 | QA Controller / Tester | Advance **1** more day (offset **8**, Thu Nov 19). **Fully reload** the Instant Pot | **Last day, window still open.** Days left: **0** or "last day" — **verify** the wording. **Start a return**, Refund and Mark returned are still offered. No "Return window closed" badge yet. The optional manufacturer warranty is still active. Record whether a separate "ends today" reminder is sent (not specified; see open questions) |
| 8 | Tester | On Nov 19, start a return on the Instant Pot, then cancel it (or leave it unsubmitted) so you have seen that the action is allowed | Start a return works on the last day. Cancel leaves the item as it was |
| 9 | QA Controller / Tester | Advance **1** more day (offset **9**, Fri Nov 20). Fully reload the Instant Pot | **Window ended.** "Return window closed" (or equivalent), the soft-closed copy from Scenario 40, Start a return / Refund / Mark returned hidden, **Ask for a courtesy return anyway** behind a confirmation. The courtesy override lasts for the browser visit only. The manufacturer warranty, if added, is **still active**. No new "act now" reminder for the ended window |
| 10 | QA Controller / Tester | Still Friday Nov 20, **after** digest time: `POST /api/maintenance/run-digest` (or the documented digest job). Check mail and Notifications. Run the digest job **again the same week** | **One** weekly digest email listing the held warranty-ending notices (the toaster and kettle, if those notices exist), and an in-app "Weekly digest". A second run the same week (Mon–Sun in the person's local calendar) sends **nothing** (push 31). Return-window reminders were "At once," so they are **not** listed as held digest lines. Then `POST /api/maintenance/clock/reset` to **offset 0** |

## What to check, in short

1. **Last day is inclusive** in America/New_York: Nov 19 still open, Nov 20 closed (soft-closed, Scenario 40).
2. **Leads 7, 3 and 1 fire once** and do not repeat on the same day.
3. **Urgent** (3-day and 1-day) bypasses the weekly digest (push 31).
4. **One weekly digest** on Friday, no second run the same week, then the clock goes back to 0.
5. A manufacturer warranty is not ended by the return window.

## Cleanup

- Delete **UAT S72 Instant Pot Duo**, **UAT S72 Digest Toaster** and **UAT S72 Digest Kettle**, their documents, notices and to-dos, in the personal account only.
- Put notification settings back if you changed them (warranty-ending type off weekly / back to At once, if that was not the default).
- **Clock must be offset 0.** Ask QA Controller if it is not. The clock is global.

## Checked when this was made

- Built 2026-11-11 on the box (`generate_all.py` in `/workspace/uat/scen-71-74/`). Order number, totals and tax (5.5% ME), purchase date, return-by date and model were found in the PDF text layer (`validation.json`). The JPG twin was checked by eye.
- The purchase date 2026-10-20 is in the past at step 1 (app date 2026-11-11).
- Amazon policy facts came from a **read-only** development-database query on 2026-11-11. No database write was made.

## Known rough edges and open questions for CC (not part of the answer key)

- **Purchase date vs delivery date.** The seeded Amazon row has `return_from_delivery = false`, so this pack counts from 2026-10-20 → last day 2026-11-19. The conditions text says "30 days of delivery" (the paper also shows delivered 10/21/2026). If the app uses delivery, the last day is Nov 20 and every clock step must move by one day. Which date is authoritative?
- **2026 holiday extension.** The stored conditions only spell out the 2025 season. This purchase is in October, so it should not matter. If a 2026 November–December extension is applied anyway, record the actual last day.
- **"Ends today" reminder.** Leads 7/3/1 are known from UAT. A reminder on the last day itself is **not specified**. Record whether one is sent, as a question, not a fail.
- **Warranty-ending lead** for the digest items is not pinned in a CHANGES note (the reminder-send sweep used a warranty about 15 days out). If no held notice appears by Friday, record the lead and treat an empty digest as "nothing held, nothing sent" (push 31), not as a fail of the return-window steps.
- **Crossing a lead between runs.** UAT of Scenario 39 noted that an item which crosses the 3-day mark between reminder runs may get no urgent email until the next lead day. This pack **lands on** each of 7, 3 and 1 so that gap should not appear. If a run is skipped, record it.
- **Clock:** every advance is global and forward until reset. Run this one alone, with QA Controller's OK, and reset to 0.
