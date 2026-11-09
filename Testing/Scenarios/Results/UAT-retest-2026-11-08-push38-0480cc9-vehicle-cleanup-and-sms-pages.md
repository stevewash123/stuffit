# UAT retest — Push 38: vehicle clean-up and text-reminders pages (Nov 8, 2026)

- **Build:** API 0480cc9, started 10:19:11 PM ET. UI Last-Modified 10:18:02 PM ET. Staging.
- **Source:** CHANGES-push-38-vehicle-cleanup-and-text-reminders-page-2026-11-08.md (2751 B); HANDOFF-push38-0480cc9-retest.txt.
- **Scope:** the Fixed items from the push 37 follow-up report, plus the new public text-reminders pages. Targeted only; no regression; no migration or seed.
- Left out (Not changed, do not report): combobox lag; document-reading items; the text-message opt-in itself (not built); Terms/Privacy bracketed placeholders and draft banner.
- **Run:** ~10:39–10:50 PM ET. API as Alice (P34-Alice Repairs owner). UI as p34self Personal ("P34 Self") after Bob's login was rejected once and not retried.
- **Clock:** Offset 0 at the end.

## Results

| Result | Count |
|---|---|
| Pass | 11 |
| Partial | 1 |
| Fail | 0 |
| Inconclusive | 1 |

## Per-step results

| # | Check | Who / how | Result |
|---|---|---|---|
| 1a | Retail: Save purchase disabled while the Ford part/accessory question is unanswered | p34self, UI | **Pass** |
| 1b | Retail: Save purchase disabled while a vehicle model of the brand is typed (e.g. Yes, a part + Bronco) | — | **Inconclusive** (path not exercised) |
| 2 | Boat kind → Hours; 0.8 reads "0.8 hours" | UI + API | **Pass** |
| 3 | Singular "1 hour" / "1 mile" | UI + API | **Partial** |
| 4 | "First put in service (optional)" on Add for New | UI | **Pass** |
| 5 | "Date of that reading" on Add; future date refused (`odometerReadOn`) | UI + API | **Pass** |
| 6 | Lease line "$0.25 per mile over"; Paid by on vehicle page | UI | **Pass** |
| 7 | Lease mileage notice "$0.25 per mile" (currency) | Alice, API + email | **Pass** |
| 8 | /sms "Text message reminders", no draft banner, full copy, support@ | UI (+ SPA JS) | **Pass** |
| 9 | Terms "Text message terms (SMS)" | UI | **Pass** |
| 10 | Privacy "Mobile numbers and text messages"; mobile under What we keep | UI | **Pass** |
| 11 | Redirects /warrantycat → /sms, …/privacy → /privacy, …/terms → /terms | UI (client routes) | **Pass** |
| 12 | support@microsaasbuilders.com on legal pages | UI + SPA JS | **Pass** |

### Step details

**1a / 1b — Bronco Save disabled.**
- Notes: Save is disabled while a vehicle model of the brand is typed, **and** while the part/accessory question is unanswered.
- **1a Pass:** Ford with the question unanswered → Save purchase disabled; message "Ford makes vehicles. Is this a part or accessory, not a vehicle?" Shots: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/d792c0e50ccd4111cdce92a35e3103f3a1bc1e830565a4f2965c846447313e30.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/3d3915f68a6800b27421c7e7675aba78d1c4c6271acb6a458087d5a6e286e56e.png.
- **1b Inconclusive:** Choosing "No, it is a vehicle" switches straight to /add/vehicle (nickname and Ford carried). The retail path with a vehicle model typed (for example answering Yes, it is a part, then typing Bronco) was not exercised, so that half of the notes was not confirmed.

**2 — Boat Hours / 0.8 hours: Pass.**
- Kind Boat auto-selected Hours. Item 01a1be6a-8363-75c2-86c4-a681608c135d. Summary and entry showed "0.8 hours". API boat 01a1be63-e570-… latestLine "0.8 hours on Nov 8, 2026". Shots: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/b706d1489dcd3021634bdb30d6ca662da78fd259d5b3a9cb5c82bacffcb48898.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/d4388ef23276b40b52246eb31d473a72240d218a7f44f747c34ce63ac7ac01f5.png.

**3 — Singular: Partial.**
- Summary lines are singular: "1 hour", "1 mile" (UI and API latestLine).
- The reading **entry** still says **"1 hours"** / **"1 miles"** ("You entered it"). Shots: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/d4388ef23276b40b52246eb31d473a72240d218a7f44f747c34ce63ac7ac01f5.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/8dbcc6dddc0f95915cbf744f9501f83cf4326256dbc55de5b3ef82d616edbabd.png.

**4 — In-service on New: Pass.** Field "First put in service (optional)" on Add for New. Shot: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/5035700aaa4917c2409cc6efeea1423dd7b9426d9f0658636ab3c648d24a9c16.png.

**5 — Reading date: Pass.** Field appears when an odometer is entered. Future date refused with "The odometer reading date cannot be later than today." Car 01a1be6c-1828-7749-a48c-c82e6965cfc5 summary "1 mile on Nov 5, 2026". API: 400 on field `odometerReadOn`. Shots: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/eca5dc33d8b2483e174abdd87f37100fbd4f0a37926a7631e8f6101a5efe5fe1.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/8dbcc6dddc0f95915cbf744f9501f83cf4326256dbc55de5b3ef82d616edbabd.png.

**6 — Fee and Paid by on page: Pass.** Lease 01a1be6c-9454-7d24-99f2-d6962069a7cd: "Paid by payment plan", "Leased until Nov 8, 2027 · 12,000 miles a year allowed · $0.25 per mile over". Cash or check also shown. Shot: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/9e912a4f2e010dcc5f55b921f220392f546504afb011f0fa821f050e2c6a2e32.png.

**7 — Notice currency: Pass.** After +182 days, LeaseMileage=1. In-app and email: "Going over costs $0.25 per mile." (Alice vehicle 01a1be63-e0ff-…). Clock reset to 0 after.

**8–12 — Public pages: Pass.** /sms title "Text message reminders", no draft banner, opt-in/1–5 month/rates/STOP/HELP/privacy/support@. Terms and Privacy sections present. Client redirects confirmed in the browser. Shots: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/e37a3cfae45a562ffe1eabd26ea754a235966655a781dfda021efd5eab4f3851.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/2015e1a997298712ebb20181274b81806a456e9174121986e19e94e4a669b2d8.png, /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/0ec365a40bc083dcd2350f4db47082e65ee9bdf7d122999b6b36a85793066765.png.

## Findings, ranked

### Medium

1. **Reading entry still plural for exactly one.** Summary is "1 hour" / "1 mile", but the reading list entry shows "1 hours" / "1 miles".

2. **Boat in-service date showed Nov 8, 2025 after the reading was edited**, though Nov 8, 2026 was entered on Add (boat 01a1be6a-8363-75c2-86c4-a681608c135d). Seen in the UI only. Not confirmed via API: the item belongs to p34self, Alice's GET returned 404, and p34self has no API password in env (vault only). Marked **seen in UI, not confirmed**.

### Low / notes

3. Bare GET `/vehicles/{id}` returns `paidBy: null`; the item and purchase paths return `paymentPlan`. The vehicle page shows Paid by correctly via the item path.

4. Curl alone cannot prove the public redirects (SPA returns 200 for every path). Browser confirmed the client redirects; SPA JS has `redirectTo: "sms"|"privacy"|"terms"`.

## Needs follow-up

- **Bob's password needs a reset before the next run.** Vault login was rejected once ("Invalid email or password") and was not retried. Signed-in UI work used p34self Personal instead.
- Confirm the boat in-service Nov 8, 2025 display under p34self (or after a Bob reset), including whether Edit reading changed in-service.
- Exercise the retail "Yes, a part or accessory" path with a vehicle model (Bronco) typed, to close 1b.

## Needs code changes

- Singular wording on the reading **entry** line ("1 hours" → "1 hour", "1 miles" → "1 mile"), matching the summary.
- Investigate in-service date flipping to the previous year after a reading edit (if API confirms).

## Test data created

- **Alice API:** P38b Lease Fee 01a1be63-e0ff-…; Boat Hours 01a1be63-e570-…; One Hour 01a1be63-e722-…; One Mile 01a1be63-e7f9-…
- **p34self UI:** Boat 01a1be6a-8363-…; car with reading date 01a1be6c-1828-…; lease 01a1be6c-9454-…

## Evidence

- /workspace/uat/push38-findings.md
- /workspace/uat/push38/run-log.jsonl
- /workspace/uat/p38b-ui-findings.md
- /workspace/uat/p38b-ui-checklist.md
- Screenshots (full paths above in step details)
