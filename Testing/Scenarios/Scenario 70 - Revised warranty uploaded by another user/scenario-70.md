# Scenario 70: Revised warranty uploaded by another user (intended behavior)

**Accounts:** Test1 (Alice) **personal account** = User A; Test2 (Bob) **personal account** = User B. Do not run this in the shared business P34-Alice Repairs.
**Preconditions:** clock offset **0**, app date **2026-11-11** (America/New_York) at step 1. If the offset is not 0, stop and ask QA Controller: Alice's return window (to Dec 7, 2026) has to be open at step 1. Step 5 **advances the global clock by 120 days**, which moves every account, so **QA Controller must OK it** and no other run may be in progress. Reader on, or record **reader off**. Maker **UAT Kestrel Home Robotics** and model **AeroClean R7 / KR7-200** are fictional and **not seeded**. Both testers must type exactly the same maker and model (see "Known rough edges": the two accounts may otherwise never be matched). No database change was made for this pack.
**Time:** about 45 min, plus the clock step.
**Built per:** Scenario 1 document order; Scenario 54 (registration, terms in days); push 26 ("probably replaced" note, a document warranty replaces the maker warranty on an ordinary item); push 29 (notices with Keep it / dismiss); Scenarios 68 and 69 (pack layout).
**Why this plan:** a warranty is set when you buy the product. The terms that came in the box keep applying to the first buyer even after the maker revises them. When another user later uploads the revised terms, the app should store them as a **newer, dated version** of the maker's warranty for that product, apply them to purchases on or after their effective date, and **tell** the earlier owner, without silently changing that owner's coverage.

> **This scenario tests the intended behavior that Steve agreed on (2026-11-11).** The current build may not do all of it yet (see "Known rough edges"). Record each expected result as Pass, Partial, Fail or **Not built**. Not built is a finding for CC, not a tester error.

## The story (answer key)

| Fact | User A: Alice (Test1) | User B: Bob (Test2) |
|---|---|---|
| Item name to use | **UAT S70 Kestrel AeroClean R7 (A)** | **UAT S70 Kestrel AeroClean R7 (B)** |
| Maker / model (type exactly) | UAT Kestrel Home Robotics / AeroClean R7, model **KR7-200** | same |
| Category | Robot vacuum, under home appliances or floor care (pick the closest; use the same one on both) | same |
| Seller (printed) | **UAT Harborline Electronics**, Store #070, 170 Example Harbor Plaza, Testville, ME 00000, (207) 555-0173 | same store |
| Customer on paper | UAT Sample Buyer A, 70 Example Lane, Testville, ME 00000, (207) 555-0170 | UAT Sample Buyer B, 71 Example Lane, Testville, ME 00000, (207) 555-0171 |
| Purchase date (paper → ISO) | 11/07/2026 → **2026-11-07** | 03/06/2027 → **2027-03-06** |
| Receipt # / serial | HL-070-26-118407 / KR7200-26K07-00701 | HL-070-27-030611 / KR7200-27C02-00711 |
| Price / tax / total | $449.99 / $24.75 / **$474.74** | $449.99 less $20.00 promo = $429.99 / $23.65 / **$453.64** |
| App date when added | 2026-11-11 (offset 0) | 2027-03-11 (offset 120) |
| Return policy | 30 days → **to 2026-12-07** ("RETURN BY: 12/07/2026") | 30 days → **to 2027-04-05** ("RETURN BY 04/05/2027") |
| Maker warranty that applies | **v1, Rev. 03/2026** (in the box) | **v2, Rev. 02/2027** (in the box, uploaded by Bob) |
| Robot and dock | 12 months → **2027-11-07** | 12 months → **2028-03-06**; **24 months → 2029-03-06 if registered by 2027-04-05** |
| Battery | 12 months → **2027-11-07** | 6 months → **2027-09-06** |
| Registration | Optional, no to-do | Required for the 24-month term: **register by 2027-04-05** (30 days) |
| Transfer | Transfers to later owners | Original purchaser only |
| Claims | Phone (207) 555-0172, then mail-in with prepaid label | Online only at kestrel-home.example/claim, with a photo of the serial plate and of the fault. Advance replacement if registered |

Day terms end N days after the start (push 26): 2026-11-07 + 30 days = 2026-12-07, and 2027-03-06 + 30 days = 2027-04-05. Month terms use the same calendar day.

## v1 and v2, side by side

| | **v1, Rev. 03/2026** (file 02, form KW-R7-LW-0326) | **v2, Rev. 02/2027** (file 04, form KW-R7-LW-0227) | More or less generous? |
|---|---|---|---|
| Effective / applies to | March 1, 2026: purchases on or after 2026-03-01, until replaced | **February 15, 2027: purchases on or after 2027-02-15**. Supersedes Rev. 03/2026 | n/a (dating) |
| Robot and dock | 12 months parts and labor | 12 months, **24 months if registered within 30 days** | More, if registered |
| Battery | 12 months | **6 months** | **Less** |
| Registration | Optional, not required | **Required for the 24-month term** (within 30 days) | Adds a condition |
| Exclusions | Consumables, cosmetic, accident, misuse, liquids, wrong voltage, commercial use, altered serial | Same, **plus** non-Kestrel batteries, brushes or filters; non-Kestrel firmware; **wet floors or outdoors** | **Less** |
| Claim process | Phone, then mail-in with a prepaid label, about 10 business days | **Online only**, photo of the serial plate and of the fault; **advance replacement** if registered | Different |
| Transfer | Transfers to later owners | **Original purchaser only** | **Less** |
| Earlier buyers (Section 9 of v2) | n/a | Owners who bought before 2027-02-15 **keep Rev. 03/2026**. They **may choose** v2 by registering and selecting "Apply revised terms" **by 2027-06-30**. The choice replaces the old terms in full, counts from the original purchase date, and cannot be undone | Owner's choice |

So v2 is **not** simply better or worse. It is a real trade-off, which is why A has to be asked, not switched.

## Files, in the order to use them

Each file is one PDF plus a JPG of its first page with the same name. File 04 is two pages long (page 2 is the maker's own "Summary of changes" table).

| # | File (.pdf + .jpg) | What it is | Who uploads it, and when | Where it goes |
|---|---|---|---|---|
| 01 | `01-receipt-userA-kestrel-aeroclean-r7` | Full-page Harborline sales receipt dated 11/07/2026, with a return-policy box ("RETURN BY: 12/07/2026") | Alice, step 1, offset 0 | Add a purchase / item attachment, Read it |
| 02 | `02-kestrel-limited-warranty-v1` | Kestrel limited warranty, **Rev. 03/2026**, effective March 1, 2026 (the card in Alice's box) | Alice, step 2, offset 0 | Alice's item > warranty document, Read it |
| 03 | `03-receipt-userB-kestrel-aeroclean-r7` | Narrow till receipt dated 03/06/2027 with the return policy printed ("RETURN BY 04/05/2027") | Bob, step 7, offset 120 | Add a purchase / item attachment, Read it |
| 04 | `04-kestrel-limited-warranty-v2` | Kestrel **REVISED** limited warranty, **Rev. 02/2027**, effective February 15, 2027, with an orange "REVISED TERMS" box and a change summary | Bob, step 8, offset 120 | Bob's item > warranty document, Read it |

## Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Confirm the **personal account** and clock offset **0** (app date 2026-11-11). Add a purchase: attach receipt **01** and Read it. Name the item **UAT S70 Kestrel AeroClean R7 (A)**. Type maker **UAT Kestrel Home Robotics**, model **AeroClean R7**, model number **KR7-200**, serial from the key | One item. Seller Harborline, 2026-11-07, $449.99 (total $474.74), serial as keyed. **Return policy: 30 days, active, to Dec 7, 2026.** The seller is fictional with no shared policy, so the return term comes from the receipt text. If it is not read, add it by hand (30 days, from purchase) and record **reader miss** |
| 2 | Test1 | On the item, attach warranty **02**, Read it, accept the maker warranty | Maker warranty **Kestrel, Rev. 03/2026**: robot and dock 12 months **to Nov 7, 2027**, battery 12 months **to Nov 7, 2027** (as a second line, or noted in the terms: **verify**), transferable, phone or mail-in claims. **No registration to-do** (v1 says optional). Source = document |
| 3 | Test1 | Write down the baseline: screenshot the item page (coverages, start and end dates, terms, source), the Notifications count and the To do list | This is the "before" for steps 6, 10 and 12. Nothing to pass yet |
| 4 | Test2 | Optional isolation check from Bob's **personal** account: open Alice's item address | Not found or no access |
| 5 | QA Controller | **With QA Controller's OK only:** `POST /api/maintenance/clock/advance?days=120` (maintenance key header). Then check the offset | Offset **120**, app date **2027-03-11** for **every** account. Write down the offset in the run log |
| 6 | Test1 | Reload Alice's item (full reload, because a stale page after a clock move is a known issue). Open Notifications | **Return policy ended Dec 7, 2026** ("Return window closed"; refund and return actions hidden, as in the soft-closed fix). **Maker warranty unchanged** from the baseline, still active to Nov 7, 2027. **No "new warranty terms" notice yet**, because nobody has uploaded v2 |
| 7 | Test2 | Confirm Bob's **personal** account and offset 120. Add a purchase: attach receipt **03**, Read it. Name **UAT S70 Kestrel AeroClean R7 (B)**, the same maker, model, model number and category as Alice, serial from the key. **Before** attaching file 04, look at what maker warranty (if any) the app suggests | Seller Harborline, 2027-03-06, $429.99 (total $453.64). **Return policy 30 days, active, to Apr 5, 2027.** Bob never sees Alice's item, receipt or warranty file. If the app suggests Kestrel's Rev. 03/2026 from a shared catalog, record it. That is acceptable only while v2 is unknown |
| 8 | Test2 | On Bob's item, attach **REVISED** warranty **04**, Read it, accept | Bob's maker warranty is **Kestrel Rev. 02/2027**: robot and dock 12 months **to Mar 6, 2028**, extended to **24 months / Mar 6, 2029 if registered**; battery 6 months **to Sep 6, 2027**; original purchaser only; online claims. **A registration to-do for Bob, due Apr 5, 2027** (push 20 registration split). It applies to Bob because **2027-03-06 is on or after the effective date 2027-02-15** |
| 9 | Test2 | Open Bob's Notifications | **No** "new warranty terms" notice for Bob. Bob uploaded v2, and v2 is already his terms |
| 10 | Test1 | Reload Alice's item and compare it with the step 3 baseline | **Nothing changed:** still Kestrel **Rev. 03/2026**, robot and dock and battery to **Nov 7, 2027**, start **Nov 7, 2026**, transferable, same terms text and source. **No** registration to-do. **No** "Probably replaced" badge or other silent swap. Return policy still **ended Dec 7, 2026** |
| 11 | Test1 | Open Notifications (if notices are made by the reminders run, have QA Controller run the account-scoped reminders for Alice first and record that) | **Exactly one** notice, along the lines of: **"UAT S70 Kestrel AeroClean R7 (A) has new warranty terms available. Check whether they apply to your Kestrel AeroClean R7."** It names the item, the maker and Rev. 02/2027 or its effective date. It does not say A's terms have changed |
| 12 | Test1 | Open the notice. Look at the compare view, then choose **Keep my current terms** (or dismiss the notice, whichever the UI offers) | The compare view shows v1 (yours) against v2 (newer) with the differences from the table above, and says v2 is for purchases **on or after Feb 15, 2027**. Earlier owners may choose it (v2 Section 9, **by Jun 30, 2027**). After Keep or dismiss: Alice's warranty is **exactly the step 3 baseline**, the notice is finished or gone, and after a reload it **does not come back** |
| 13 | Test2 | Read file **04** again on Bob's item (or attach the **JPG twin** of 04 and Read it) | **No second version** of Kestrel's warranty. Bob's coverage is the same as at step 8, with no duplicate lines and no second registration to-do |
| 14 | Test1 | Reload Notifications (and run the reminders again if they were used at step 11) | **No second notice** for the same v2. The count matches step 12 |
| 15 | Test1 / Test2 | Reload both items one last time | Alice: v1, unchanged, return ended. Bob: v2, return active to Apr 5, 2027, registration to-do open. Each account sees only its own item and files |

### Optional branch: Alice adopts v2 (run instead of step 12's Keep)

Run this only if the build offers an "Apply these terms" (or similar) choice. Otherwise record **Not built**.

| # | Persona | Action | Expected |
|---|---|---|---|
| 12B | Test1 | Open the notice, compare, choose **Apply revised terms** and confirm the warning | A warning before confirming that the choice **replaces** the old terms in full and **cannot be undone** (v2 Section 9). It also lists what Alice loses: battery 12 → 6 months, transfer → original purchaser only |
| 13B | Test1 | Reload Alice's item | **Changes:** maker warranty is now Kestrel **Rev. 02/2027**. Robot and dock **24 months from the original purchase → Nov 7, 2028**, which depends on registration (choosing v2 means registering, so either it is marked registered or a **registration to-do due Jun 30, 2027** appears: **verify** which). Battery **6 months → May 7, 2027** (still active on 2027-03-11). Not transferable. Online claims. **Does not change:** purchase date, **start date Nov 7, 2026**, seller, price, serial, receipt and v1 document still on the item, **return policy still ended Dec 7, 2026**. The v1 coverage is kept as history (shown as replaced), not deleted. Bob is not affected. No new notice to anyone |

## What to check, in short

1. **No silent swap:** A's coverage after B's upload equals the step 3 baseline in every field.
2. **Versioning:** Kestrel AeroClean R7 has **two dated versions**: Rev. 03/2026 for purchases from 2026-03-01 to 2027-02-14, and Rev. 02/2027 from 2027-02-15. A re-upload of the same v2 does not make a third.
3. **Applies by purchase date:** B (bought 2027-03-06) gets v2. A (bought 2026-11-07) keeps v1.
4. **One notice to A only**, never to B. It goes once per new version, and Keep or dismiss leaves A unchanged.
5. **Return policies are untouched** by any warranty change: A's ended Dec 7, 2026, B's active to Apr 5, 2027.
6. **Privacy:** B's upload never exposes B's receipt, serial or name to A, and A's never to B. The notice and compare view show only the maker's terms.

## Cleanup

- Delete **UAT S70 Kestrel AeroClean R7 (A)** in Alice's personal account and **(B)** in Bob's personal account, with their documents. Clear the S70 notices and to-dos.
- **Clock:** the offset stays at +120 until someone resets it. Ask QA Controller to have DB Stager set it back to 0 after the run, when no other run needs it. It is global.
- Any Kestrel maker, model or policy rows made by the uploads (account-owned or shared, including candidate or proposed policies) are fictional and test-marked. Leave them for DB Stager to remove at the next reset. Testers do not delete shared reference data.

## Checked when this was made

- Built 2026-11-11 on the box from one generator (`generate_fixtures_70.py`, kept on the build box in `/workspace/uat/scen-70-revised-warranty/`, not copied to the share). The receipts' totals and tax (5.5% ME), receipt numbers, serials, return-by dates, revision labels, form numbers and effective dates were all found in each PDF's text layer (`validation.json`). The JPG twins were checked by eye.
- Every printed date is in the past for the app date at the step where it is used: files 01 and 02 at 2026-11-11, files 03 and 04 at 2027-03-11 (after the 120-day advance).
- No app, database, mail or sign-in was used. Schema notes below come from an earlier read-only schema snapshot (Nov 7), not a new query.

## Known rough edges and open questions for CC (not part of the answer key)

- **Are warranty versions supported at all?** The schema has `manufacturer_policies.effective_from` / `effective_to`, `purchased_from` / `purchased_to`, `model_numbers` and `verified_at`; `coverages.source_policy_id` and `replaced_by_coverage_id`; and `candidate_policies` (a user submission with a review status). That looks like the base for versions, but **verify** whether reading a user's warranty document creates or updates a **shared** dated version, or only a coverage on that one item. If only the item gets it, steps 11–14 will be **Not built**.
- **Same product across two accounts:** the maker and model are not seeded, so each account may create its **own** "UAT Kestrel Home Robotics" maker (an account-owned party). Then nothing links A's item to B's upload. Choices for CC: match on maker name and model number, or have DB Stager seed a shared maker and model before the run (Steve or QA Controller to decide; this pack made no DB change).
- **Effective date vs purchase date:** the rule is **purchase date on or after the effective date** (2027-02-15), not upload date or app date. Edge cases to decide: a purchase on the effective date itself (should get v2); a product bought before the effective date but **first used or registered** after it (should keep v1); a v2 uploaded **with no readable effective date** (should not replace anything, and should probably go to review); a v2 whose date is **later than the app date** (store it but apply it to nobody yet).
- **Less generous revision:** when v2 is worse on every line, A must keep v1 and the app should **not** suggest switching. Should A get a notice at all, or a quieter "terms changed for new buyers" note? This pack's v2 is mixed (longer robot term, shorter battery), so a notice is right here.
- **Who triggers the notice, and when:** right away on B's upload, after a review or `verified_at` on the shared version, or on the reminders run? If it waits for review, add a step for the Ops reviewer and record it.
- **Duplicate detection:** "the same v2" should be matched on maker + model + revision label or effective date, not on the file. The JPG and the PDF of 04 are the same version. A different revision (for example a later Rev. 06/2027) should give A one new notice.
- **Push 26 interaction:** on an ordinary item, applying a **document** warranty replaces the item's maker warranty. That must stay limited to **the item where the document was attached** (B's), never A's. The "Your own entry may be out of date" note is for **typed** coverages only. Alice's v1 came from a document, so it should not show.
- **Adopting v2 (branch):** v2's 24-month robot term depends on registration. When an earlier owner chooses v2, should the app treat that as registering (registered on the choice date) or create a to-do due Jun 30, 2027? Also, is the old coverage kept as history (`replaced_by_coverage_id`) and can a mistaken choice be undone in the app, even though the paper says the choice is final?
- **Clock:** the clock is global and forward-only. Step 5 moves Alice, Bob, Carol and Ops together, so another scenario's time-sensitive checks may change. Run this one alone, with QA Controller's OK.
