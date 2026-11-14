# Scenario 71: Business accounts — invite, switch, keep data apart

**Accounts:** a **throwaway business owner** (new sign-up, "For my business", suggested name **UAT S71 Pine Rivet Repairs**); Test2 (Bob) as an invited employee who already has a login; one **throwaway new email** for a new-address invite; Test3 (Carol) as an outsider. **Do not run this in the live shared business P34-Alice Repairs**, and do not convert Alice's or Bob's existing accounts if a QA run is using them. Do not use Test1 (Alice) unless QA Controller has confirmed she again has a personal space and the shared shop will not be touched.
**Preconditions:** clock offset **0**, app date **2026-11-11** (America/New_York). Reader on, or record **reader off**. Step 8 **advances the global clock by 8 days** so an unused invitation can expire; **QA Controller must OK it**, and no other run may be in progress. Reset the clock to 0 afterwards. Maker **DeWalt** and model **DCD794D1** may be typed; the seller **UAT Northline Tool Supply** is fictional and not seeded.
**Time:** about 50 min, plus the clock step and two invitation emails.
**Built per:** pushes 34–36 (business accounts, invitations, roles, account switcher, asset tag and location, per-account upload queue, account name on notices). Scenario 26 (privacy between personal accounts). Scenario 70 pack layout.
**Why this plan:** a shop and a person's own things must never mix. An employee who can add a drill must not see other people's email addresses, open billing, export the shop, or take the shop's papers with them when they leave.

## The story (answer key)

| Fact | Value |
|---|---|
| WarrantyCat account to use | A **new** business, not P34-Alice Repairs. Suggested name **UAT S71 Pine Rivet Repairs** |
| Item name | **UAT S71 DeWalt 20V MAX drill** |
| Seller (printed) | **UAT Northline Tool Supply**, Store #171, 171 Example Trade Road, Testville, ME 00000, (207) 555-0175 |
| Customer on paper | UAT Sample Buyer, 71 Example Lane, Testville, ME 00000, (207) 555-0171 |
| Purchase date (paper → ISO) | 11/04/2026 → **2026-11-04** |
| Receipt # / serial / model | NL-171-26-110415 / 794D1-26K04-00715 / **DCD794D1** |
| Price / tax / total | $119.99 / $6.60 (5.5% ME) / **$126.59** |
| Return on the receipt | 30 days → **to 2026-12-04** ("Return by 12/04/2026"). The seller is fictional, so this term comes from the document (or is added by hand if the reader misses it) |
| Maker warranty | DeWalt limited warranty, Rev. 03/2026, form DW-20V-LW-0326: **3 years** from purchase → **2029-11-04**, transferable |
| Asset tag / location (business only) | **PR-DRILL-001** / **Bay 2** |

Day terms end N days after the start (push 26): 2026-11-04 + 30 days = 2026-12-04. Month terms use the same calendar day: 2026-11-04 + 36 months = 2029-11-04.

## Files, in the order to use them

Each file is one PDF plus a JPG of its first page with the same name.

| # | File (.pdf + .jpg) | What it is | Who uploads it, and when | Where it goes |
|---|---|---|---|---|
| 01 | `01-receipt-northline-dewalt-drill` | Northline sales receipt dated 11/04/2026, with a 30-day return box | The business owner, step 2, offset 0 | Add a purchase / item attachment, Read it |
| 02 | `02-dewalt-20v-limited-warranty` | DeWalt 20V limited warranty, Rev. 03/2026, three years from purchase | The business owner, step 3, offset 0 | The shop item > warranty document, Read it |

## Steps and what should happen

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Throwaway owner | Confirm the clock is **0** and you are **not** in P34-Alice Repairs. Sign up with a new address, choose **For my business**, name it **UAT S71 Pine Rivet Repairs** (or another unique UAT name), open the emailed link | The header shows the business name. Settings > People lists you as **Owner**. Google sign-up is hidden on the business choice (push 34). The new login also has, or is later offered, a personal account — **verify** when it appears (push 34: a brand-new address gets the business membership **and an empty personal account**) |
| 2 | Owner | Add a purchase: attach receipt **01**, Read it. Name the item **UAT S71 DeWalt 20V MAX drill**. Type seller **UAT Northline Tool Supply**, model **DCD794D1**, serial from the key. On the item, set **Asset tag** `PR-DRILL-001` and **Location** `Bay 2` | One item. Seller Northline, 2026-11-04, $119.99 (total $126.59), serial as keyed. **Return policy 30 days, active, to Dec 4, 2026.** Asset tag and location show on the item and in My Items (push 34). If the return term is not read, add it by hand (30 days from purchase) and record **reader miss** |
| 3 | Owner | Attach warranty **02**, Read it, accept | Maker warranty **DeWalt, 3 years, to Nov 4, 2029**, transferable, source = document. The receipt stays on the item |
| 4 | Owner / Test2 | Owner: Settings > People, invite **Bob's existing address**. Bob opens the link, **signs in as Bob** (the signed-in email must equal the invited address) and accepts | Bob now has two memberships: his personal account and this business (push 34). The owner gets a notice that the invitation was accepted. On Bob's next sign-in, a chooser appears if no account is remembered (`/choose-account`); afterwards the app opens the last account used. The **header switcher** swaps accounts and reloads (push 34). A notice names the account when Bob has more than one (push 35) |
| 5 | Test2 / Owner / Test3 | Isolation checks: (a) Bob, in **personal**, pastes the shop item's address. (b) Bob, in **business**, opens My Items and the drill. (c) Owner looks at Bob's personal items. (d) Carol, who was never invited, pastes the shop item address and searches for the drill | (a) Not found or no access; no title, price, papers or tag. (b) Bob can see and edit the shop drill. His personal items are **not** in the business list. (c) The owner never sees Bob's personal items. (d) Carol sees nothing. In People, an employee sees **names only, not email addresses** (push 34) |
| 6 | Test2 | As **employee**, try Settings > People (invite, resend, revoke, remove), rename the business, the plan / billing page, Export, and Delete the account. Then add a second cheap shop item, e.g. **UAT S71 Shop markers**, by hand | Each owner-only action is **refused (403)** (push 34). The employee can add and edit items. The new item shows **Entered by** (Bob). The owner is a follower of it and would get its reminders. The items belong to the business, not to Bob personally |
| 7 | Owner / throwaway new address | Invite a **new** email. Open the link in a private window, sign up, join. Then, as owner, **resend** a *different* unused invite if one is handy; try to use an already-accepted link a second time | The new person joins as **Employee** and also has an **empty personal account** (push 34). Resend delivers a fresh link. A second use of the same single-use link is refused |
| 8 | Owner / QA Controller | Leave **one unused invitation** unopened. **With QA Controller's OK only:** `POST /api/maintenance/clock/advance?days=8`, then check the offset. Open the leftover link | Offset **8**, app date **2026-11-19** for every account. The leftover link is **refused as expired** (invitations expire in 7 days, push 34). Then ask QA Controller to `POST /api/maintenance/clock/reset` back to **offset 0** before the next steps |
| 9 | Owner / Test2 | After the clock is back at 0: **Remove** Bob, or have Bob **Leave** (confirm) | The shop items **stay with the business**, including the drill, its papers, tag and "Entered by". Bob keeps his login and personal account. His business session / token stops at once (push 34). He can no longer open the shop item |
| 10 | Owner | Optional checks: try a second item with asset tag `PR-DRILL-001`; search My Items for `PR-DRILL-001` and for `Bay 2`; open a **personal** account (the owner's or Bob's) and look for Asset tag / Location | A duplicate tag is refused and **names the item that already holds it** (push 34). Search and the Location / "Has no asset tag" filters find the drill. A personal account is refused any tag value and shows no such fields |

## What to check, in short

1. **No mixing:** shop items, documents, tags, exports and queued uploads stay in the business; personal items stay personal (pushes 34 and 35).
2. **Roles:** only the owner can invite, rename, bill, export or delete the account. An employee can add and edit items.
3. **Invitations:** existing login vs new address, single use, resend, 7-day expiry.
4. **Leave / remove** does not take the shop's items or papers with the person.
5. Carol, and anyone in the wrong account, never sees the shop data.

## Cleanup

- Delete **UAT S71 DeWalt 20V MAX drill**, **UAT S71 Shop markers** (if added), their documents, notices and to-dos, in the **throwaway business only**.
- Remove leftover invitations. The throwaway owner and the throwaway new email are test data; leave them for DB Stager to remove at the next reset, or delete those accounts only if QA Controller agrees. **Do not touch P34-Alice Repairs, Alice's or Bob's standing test data, or Steve's admin accounts.**
- **Clock:** if it is not already at 0, ask QA Controller to have DB Stager reset it. The clock is global.

## Checked when this was made

- Built 2026-11-11 on the box (`generate_all.py` in `/workspace/uat/scen-71-74/`, not copied to the share). Receipt totals and tax (5.5% ME), receipt number, serial, return-by date, form number and the three-year end date were found in each PDF's text layer (`validation.json`). The JPG twins were checked by eye.
- The purchase date 2026-11-04 is in the past for the app date at step 1 (2026-11-11, offset 0).
- No app, database write, mail or sign-in was used to build the pack.

## Known rough edges and open questions for CC (not part of the answer key)

- **When does the personal account appear for a brand-new business sign-up?** Push 34 says a new address gets the business **and** an empty personal account. Record whether that personal space is there immediately after the confirmation link, or only later.
- **Invitation expiry boundary:** this pack treats a link left unused for 8 days as expired. Is a link still valid at the end of day 7 in the owner's time zone, and is expiry based on `expires_at` from when it was first sent or last resent?
- **Ownership transfer** (owner offers, employee accepts from email) is built (push 34) but not run here, to keep the clock and accounts smaller.
- **Free-year seat limit** (owner plus two employees) and the free-year-ending reminder (push 35) are not run here. They need more invitations or a year-scale clock move.
- **Per-account upload queue** (push 35) is hard to prove on a desktop browser. If a phone queue is not available, record **N/A**, not a fail.
- **Clock:** step 8 is global. Run this scenario alone, with QA Controller's OK, and reset to 0 before any other time-sensitive run.
