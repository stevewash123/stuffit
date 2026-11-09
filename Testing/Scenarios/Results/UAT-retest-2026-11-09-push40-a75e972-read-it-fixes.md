# UAT retest — Push 40: Read it fixes (Nov 9, 2026)

- **Build:** API a75e972, started 8:21:01 AM ET. UI unchanged (API-only). Staging.
- **Source:** CHANGES-push-40-read-it-fixes-2026-11-09.md (2560 B); HANDOFF-push40-a75e972-retest.txt; p40-ui-checklist.md.
- **Scope:** live-reader retest of S63, S64, S65 only (four rows). Targeted; no regression; no migration or seed.
- **Skipped (Not changed):** Certified box on hand-added plan; part form year / "came with"; push 38 in-service finding; S63 model/trim suggestions; Read it before save on Add.
- **Run:** Bob Personal via vault fill (vault_2453777_username/password). Fresh P40 items (did not reuse push-37 fixtures). One mid-run session-refresh 401; re-authed; no duplicate created.
- **API post-checks:** blocked — Bob env passwords return 401. Evidence is UI only.
- **Clock:** Offset 0 (no clock moves).

## Results

| Result | Count |
|---|---|
| Pass | 3 |
| Partial | 1 |
| Fail | 0 |
| Inconclusive | 0 |

## Per-step results

| # | Check | Who / how | Result |
|---|---|---|---|
| 1 | S63 Ford warranty: whole vehicle 36 mo / 36,000 mi; Powertrain 60 mo / 60,000 mi ("59,982 left" at 18 mi) | Bob, UI | **Pass** |
| 2 | S64 protection plan paper → plan record fields (Company, Plan name, Contract, Price, Service fee, phone, website, start answer) | Bob, UI | **Pass** |
| 3 | S64 CPO certificate → two certified coverages (ends 40,400 / 52,400 mi); labelled certified; not merged with factory; not offered to shared data | Bob, UI | **Partial** |
| 4 | S65 "Pro Team 175 TXW" stays whole in model (no Size 175 / Model TXW split) | Bob, UI | **Pass** |

### 1 — S63 powertrain mile limit: Pass

- Item: https://stuffit-ui.onrender.com/items/01a1c089-2f2f-757e-810c-c55774b41ad0
- Read it suggested bumper-to-bumper 3 years / 36,000 miles and powertrain 5 years / 60,000 miles.
- Saved summaries: **35,982** and **59,982** miles left; ends **2029-11-07** and **2031-11-07**.
- **Low:** powertrain detail narrative text still says 36 months / 36,000 miles though the summary shows 60 / 60,000.
- Screens: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/8f9d00ee5a29e2acc9155ef2ea079dcca2d14ce4b7fb47aaacef73ad074b5595.png ; /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/bb4c448c9e450acad692e1da29b746babd8d700605d5a8c148b7940ea3ad5a0a.png ; /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/f4d015fe1b79b737acf51ac3d39bb494866343bde58d82de14c1023696df899a.png

### 2 — S64 protection plan record: Pass

- Item: 01a1c08c-e6c6-778b-a349-6c1ff773c81a
- Plan: https://stuffit-ui.onrender.com/plans/01a1c091-2087-7e81-8b27-9749616169d5
- Company **UAT RoadGuard Administration** (Unverified); Plan **Select mechanical breakdown**; contract **UAT-P38-064-PLAN**; **$1,800** one payment; **$100** per call; phone **(202) 555-0165**; website https://roadguard.example/claims; start **Same day as the purchase** (2026-11-06); end **2029-11-06**.
- **Low:** "What is it" Not set; waiting-period-days blank though text says no waiting period; auto-renew unchecked.
- Screens: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/3fd8e1c8d212780bc8e115ca9b28011f185fae9c8b91f394c02ed4133b27fc16.png ; /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/bc53620786975ca591ba683b1168b6c2fd54bdc708e0d5f0fbff4953bee65b73.png ; /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/3d0b77fccf6c96a193fcc8f432a3eabd267c61c1152eab1390b1464289a4c3ca.png

### 3 — S64 CPO two terms: Partial

- Two terms offered and accepted: certified comprehensive **1 year / 12,000 mi** and certified powertrain **2 years / 24,000 mi**, separate from the RoadGuard plan, both from **2026-11-06 at 28,400**; ends **2027-11-06 / 40,400** and **2028-11-06 / 52,400**.
- Provider **UAT CertifiedCare**; plan UAT-P38-064-CPO; phone (202) 555-0164; $0 fee.
- Details say certified / dealer-added, not factory.
- **But:** coverage headers say **"Manufacturer warranty · Toyota"** (mislabel).
- A community-sharing notice appeared (terms would be shared with the WarrantyCat community after review). Notes say certified coverages must **not** be offered to shared data. **"Not sure"** selected; OK not clicked.
- Screens: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/915e6fc8fa16ad3f73e1aafa50f3f8081cd0e39b791686429003bfb3e2779f94.png ; /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/d0e8a50b35853f71411f4a37c5b5748619510b7d8ab9fc534d34cabca7f3c4fb.png ; /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/dca61cc933d0a94248975aa687d7f3afb38b378e24a7532704098e8f61955fac.png

### 4 — S65 model stays whole: Pass

- Item: 01a1c098-0e70-776d-8e1a-bd45ed648e5a
- Read it suggested only Size or variant: **Aluminum** (low confidence). No model / model-number suggestion; **no 175 / TXW split**. Model stays **Pro Team 175 TXW**.
- Notes: doc price conflicts ($18,000 item vs $29,000 total) shown; order no UAT-P38-065 flagged duplicate (exists from earlier run) so not added.
- Screens: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/27bdada359e71cc389177fffc86611855ae4d94adeaa8ea972289b0bd06b1958.png ; /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/312b58a23167dfd334f2b5aae0c144f057fb982d8987661eb06b74e0f3c67780.png ; /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/491464340bbbf89ec97a9b3d380a2bd0ff462ed248d470870c6e64f7734adafd.png

## Findings, ranked

### Medium

1. **S64 CPO coverage headers say "Manufacturer warranty · Toyota"** while details correctly say certified / dealer-added, not factory.
2. **S64 CPO offered a community-sharing notice** though notes say certified coverages must not be offered to shared data ("Not sure" selected; not confirmed).

### Low

3. **S63 powertrain detail narrative** still says 36 months / 36,000 miles while the summary correctly shows 60 months / 60,000 and 59,982 left.
4. **S64 plan:** "What is it" Not set; waiting-period-days blank though text says no waiting period; auto-renew unchecked.

## Needs code changes

- CPO header label must match certified / dealer-added (not "Manufacturer warranty · Toyota").
- Do not offer certified / dealer-added terms to shared data.
- Align powertrain narrative text with the 60-month / 60,000-mile summary.

## Needs follow-up

- Restore Bob's API password to env (or another non-cookie auth path) so post-UI coverage/plan GETs are possible. Vault browser login works; env login currently 401.

## Test data (Bob Personal, fresh P40)

- S63 Bronco: 01a1c089-2f2f-757e-810c-c55774b41ad0
- S64 RAV4: 01a1c08c-e6c6-778b-a349-6c1ff773c81a
- S64 RoadGuard plan: 01a1c091-2087-7e81-8b27-9749616169d5
- S65 Tracker boat: 01a1c098-0e70-776d-8e1a-bd45ed648e5a

## Evidence

- /workspace/uat/p40-ui-checklist.md
- /workspace/uat/push40/docs/ (PDFs used)
- Screenshots listed under each step
