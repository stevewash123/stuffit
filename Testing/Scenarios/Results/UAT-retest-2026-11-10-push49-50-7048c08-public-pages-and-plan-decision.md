# UAT retest — Push 49+50: public pages, picker names, plan decision (Nov 10, 2026)

- **Build:** API 7048c08, started 12:16:06 AM ET. UI originally 12:14 AM ET, then rebuilt **12:36 AM ET** after setting `WARRANTYCAT_CONTACT_EMAIL=support@warrantycat.com` and `WARRANTYCAT_BUSINESS_NAME=WarrantyCat` on StuffIt_UI (`srv-db9sab8m7kps73eibvlg`); deploy `dep-dbpaqg942hec73c43310` went live. Staging.
- **Migrations:** Push 49 none. Push 50 `PlanDecision` (`20261110044133_PlanDecision`) verified on Neon StuffIt (project `square-tree-53585492`, db `stuffit`): `warranty_plans.renewal_price`, `decision_snoozed_until`, `decision_dismissed_for`.
- **Source:** CHANGES-push-49-public-pages-and-footer-2026-11-10.md; CHANGES-push-50-plan-decision-2026-11-10.md; TESTPLAN.md; p4950-findings.md.
- **Account:** P34 Self personal. No Alice reset. Banner "A new version of WarrantyCat is ready" appeared on /login; Reload clicked first (`s49-pre-reload-banner.png`).
- **Clock:** Advanced +11 days to Nov 21, 2026 for 50-8 and 50-10, then reset. Confirmed **Offset 0** after the run (app time 2026-11-10 05:50:22Z).
- **Fixtures:** QA made no new fixture files. Picker checks reused P46-01 (Scenario 68 file 07) on P45 Honda CR-V and S69 Outback orders 12 / 07.
- **Not built (skipped, do not report as fails):** mobile number / text-reminder consent / sms-optin.png; mailing-address placeholder; logged-in footer; money paid out / service fees in cost; a separate "Cancelled" after the date; renewal-reminder email naming the panel; plan types as shared data, phone/device insurance, home appliance plans.

## Results

| Result | Count |
|---|---|
| Pass | 17 |
| Partial | 1 |
| Fail | 0 |
| Inconclusive | 0 |

Plus **Lows / ODDs** on the footer separators (49-2), leftover history labels and left-out count (49-6), and several push 50 display oddities (term spans, cancel/end dates, Home-tile wording, cost doubled after the date). All required push 50 rows passed.

## Per-step results

### Push 49 — public pages and footer

| # | Check | Result |
|---|---|---|
| 49-1 | Login blurb | **Pass** |
| 49-2 | Public footer on login / sign-up / reset | **Pass** (Low: no ` · ` separators; copyright on its own line) |
| 49-3 | Same footer on legal pages | **Pass** |
| 49-4 | `/about` content | **Pass** |
| 49-5 | Contact is support@warrantycat.com | **Pass** |
| 49-6 | Picker names Bumper-to-bumper / Powertrain | **Partial** (Low) |
| 49-7 | Untick / retick keeps Powertrain | **Pass** |
| 49-8 | Non-powertrain jobs left out after B2B ended | **Pass** |

**49-1:** Exact blurb under "Sign in": **"WarrantyCat tracks your return windows and warranty expirations and reminds you before they close. Currently in private beta."** (`s49-login.png`)

**49-2 Low:** Links are correct (About `/about`, Privacy `/privacy`, Terms `/terms`, `mailto:support@warrantycat.com`) and the copyright is **"© 2026 WarrantyCat"**. The expected middle-dot separators (`About · Privacy · Terms · …`) are **missing**; items are only spaced, and the copyright sits on its own line. Same on `/login`, `/signup`, `/forgot-password`. (`s49-footer-login.png`, `s49-footer-signup.png`, `s49-footer-reset.png`)

**49-3:** About, Terms, Privacy, Disclaimer, and Text reminders all end with the same public footer. Disclaimer and Text reminders are linked from a **second legal row** on those pages (`Terms of Service · Privacy Policy · Disclaimer · Text reminders`), not from the login footer. (`s49-footer-about.png`, `s49-footer-terms.png`, `s49-footer-privacy.png`, `s49-footer-disclaimer.png`, `s49-footer-sms.png`)

**49-4:** About covers what it is, **"WarrantyCat is in private beta…"**, email reminders and optional text reminders, **"typically 1 to 5 a month"**, **"Msg & data rates may apply"**, **"Reply STOP to opt out, HELP for help"**, contact **"WarrantyCat · support@warrantycat.com"**. (`s49-about.png`)

**49-5:** Terms / Privacy / Text reminders show **support@warrantycat.com**. "microsaasbuilders" does not appear. (Mailing address is still the expected placeholder.)

**49-6 Partial / Low:** On P45 Honda, re-read of P46-01: kept oil **"Powertrain (to Nov 8, 2029)"**. Picker options exactly: **"No coverage (history only)"**, **"Powertrain (to Nov 8, 2029)"**, **"Bumper-to-bumper (to Nov 8, 2027)"** — no "Manufacturer warranty (to …)" in the picker (the push 46 Low is fixed on the card). **Existing Service history still says "Manufacturer warranty (to Nov 8, 2029)"**, and Your coverage lists two **"Manufacturer warranty · Honda"**. The card also said **"1 other job was left out"** while listing three rows (Tires and Wipers already-added, Shop supplies tickable) — likely leftover from the push 48 count vs already-added rows. (`s49-picker-honda.png`)

**49-7:** Shop supplies ticked → Powertrain → untick → tick again: picker still shows **"Powertrain (to Nov 8, 2029)"** selected. Not now; nothing added. (`s49-retick.png`)

**49-8:** Outback order 12: A/C **left out** ($223.95); CVT and rear diff kept as **"Powertrain (to Oct 14, 2026)"**; N=4. Order 07: brake fluid **left out** ($131.85); CVT goodwill kept; N=5. Not now on both. History still shows the old P48 keeps with stale **"Manufacturer warranty (to Nov 8, 2026)"** vs the card's Powertrain (to Oct 14, 2026) — leftover labels, not a regression of the new leave-out. (`s49-outback-12.png`, `s49-outback-07.png`)

### Push 50 — plan decision

All required rows **Pass**. Plans (company **UAT P50 Care Co**, term Nov 20, 2025 → Nov 20, 2026, yearly billing; items $49.99 bought Oct 15, 2024, no maker warranty on file):

| Plan | Item | Used for |
|---|---|---|
| UAT P50 Auto-renew care ($120/yr, auto) | Toaster A | 50-1, 50-3, 50-4 (stopped renewing) |
| UAT P50 Ends care ($60/yr) | Toaster B | 50-1, 50-5 (renewed to Nov 20, 2027) |
| UAT P50 Cancel care ($60) | Toaster C | 50-7, 50-6 (cancelled) |
| UAT P50 Nothing care ($60) | Toaster D | 50-9 (dismissed) |
| UAT P50 Leftover auto care ($120/yr, auto) | Toaster E | 50-10 (ended Nov 21) |
| UAT P50 Snooze care ($60) | Toaster F | 50-8 (snoozed 14 days, left unanswered) |

| # | Check | Result |
|---|---|---|
| 50-1 | Panel facts and header wording | **Pass** |
| 50-2 | No verdict / no red-green | **Pass** |
| 50-3 | Enter renewal price | **Pass** |
| 50-4 | Stop it renewing | **Pass** |
| 50-5 | I renewed it | **Pass** (Low: one 2-year span) |
| 50-6 | Cancel it | **Pass** (Low: item end day-before; Term unchanged) |
| 50-7 | Replace it with another | **Pass** |
| 50-8 | Remind me later; snooze does not run past the end | **Pass** (Low: cost doubled after the date) |
| 50-9 | Nothing to do | **Pass** |
| 50-10 | After the date: "Did this renew?" | **Pass** (Low: Term still "renews automatically") |
| 50-11 | Home tile | **Pass** (Low: tile says "ends" for auto-renew; 60-day count includes decided plans) |

**50-1:** Auto: **"This plan renews in 10 days"** / "Renews on Nov 20, 2026" / renewal price **"Not known: ask the company"** / cost **"About $120.00 (worked out from the price and how it is billed)"**. Non-auto: **"This plan ends in 10 days"** / "Ends on Nov 20, 2026" / About **$60.00**. Item line: name, **$49.99**, bought **Oct 15, 2024**, **2 years old**. **"the maker's warranty has ended"** and **"N other coverages still running"** were **not tested** (these items had no maker warranty). (`s50-01-panel.png`, `s50-01-panel-ends.png`)

**50-2:** No renew advice; no red/green on value.

**50-3:** Entered **$135**; panel shows **"Renewal price $135.00 · Change"**. (`s50-03-price.png`)

**50-4:** No confirmation step (toast "Plan updated."). Panel gone. Header **"Ends Nov 20, 2026 (will not renew)"**; Term no longer says "· renews automatically". (`s50-04-stop.png`)

**50-5:** Form prefilled **2027-11-20**. After save, plan and Toaster B run until **Nov 20, 2027**; panel gone. **Low:** Term shows one span **"Nov 20, 2025 to Nov 20, 2027"** instead of a new term starting Nov 20, 2026. (`s50-05-renewed-form.png`)

**50-6:** Confirms first: **"Cancel this plan now?"** / **"Coverage on every item it covers ends today."** Then **"Cancelled Nov 10, 2026, refund not recorded yet"**. **Low:** Toaster C coverage shows **"Nov 20, 2025 to Nov 9, 2026"** (day before today); the plan Term still says Nov 20, 2025 to Nov 20, 2026. (`s50-06-cancel-confirm.png`, `s50-06-cancelled.png`)

**50-7:** Add-plan form opened with **"Covers UAT P50 Toaster C"** ticked; cancelled without saving. (`s50-07-replace.png`)

**50-8:** After clock to Nov 21, snoozed plan's **"Did this renew?"** panel reappeared ("Its term ended Nov 20, 2026 and we have not heard what happened."), so the 14-day snooze **did not run past the Nov 20 end date**. **Low:** cost **"About $120.00"** on a $60/yr plan. (`s50-08-snooze-reappear.png`)

**50-9:** Dismiss hides the panel for this term (stays gone after reload). (`s50-09-nothing.png`)

**50-10:** **"Did this renew?"** with **Renewed** / **Ended or cancelled** / **Not sure yet**. "Ended or cancelled" recorded end **Nov 21, 2026** (day after last day). **Low:** Term still says **"Nov 20, 2025 to Nov 20, 2026 · renews automatically"** after it was marked ended. Cost **"About $240.00"** on a $120/yr plan — same double-count as 50-8. (`s50-10-did-this-renew.png`, `s50-10-ended.png`)

**50-11:** Home lists plans to decide, soonest first, links work. After the date: **"UAT P50 Snooze care: did it renew?"**. **Lows:** auto-renewing plans say **"ends in 10 days"** on the Home tile while their panel says **"renews in 10 days"**; the **"N end within 60 days"** count still includes already-decided plans. (`s50-11-home-before.png`, `s50-11-home.png`, `s50-11-home-after-date.png`)

**Cost Low (after the date):** Snooze care ($60/yr) showed About **$120.00**; Leftover auto ($120/yr) showed About **$240.00** — double the yearly price once the end date has passed.

## Needs code / product follow-up

1. **Low:** put ` · ` separators in the public footer (and keep the copyright on the same line if that was the intended layout).
2. **Low / Partial:** refresh existing Service history "covered by" labels and Your coverage titles to **Powertrain** / **Bumper-to-bumper**; left-out count should not include already-added rows (push 48 leftover).
3. **Low:** after "I renewed it", show a new term starting at the old end date rather than one stretched span.
4. **Low:** Cancel: item coverage should end **today** (not the day before); plan Term should match the cancelled state. After "Ended or cancelled", Term should not still say "renews automatically".
5. **Low:** Home tile should say "renews in N days" for auto-renewing plans; the 60-day count should drop already-decided plans.
6. **Low:** Cost so far should not double the yearly price after the term date.

## Evidence

- `/workspace/uat/push49-50/p4950-findings.md`
- `/workspace/uat/push49-50/CHANGES-push-49-public-pages-and-footer-2026-11-10.md`
- `/workspace/uat/push49-50/CHANGES-push-50-plan-decision-2026-11-10.md`
- Screenshots under `/workspace/uat/push49-50/shots/`
