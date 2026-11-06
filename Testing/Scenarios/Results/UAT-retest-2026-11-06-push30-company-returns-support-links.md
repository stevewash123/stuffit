# UAT retest: Push 30, company returns and support links, plus list-note and start-date fixes

**Date:** Friday Nov 6, 2026, run 4:55 to 5:53 PM ET
**Build:** API `bc78d21` (live 3:32 PM ET), UI `0bb9a5b` (bundle `main-P5GKIYLK.js`). Both match the notes.
**Notes:** `CHANGES-push-30-company-returns-support-links-2026-11-06.md`
**Scope:** S3.2.14 steps 1 to 7, and the two fixed rows (My Items superseded note, To do card start date). No regression run.
**Data:** new `P30 …` fixtures only. No account resets. App clock stayed at offset 0, and no emails were sent.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Admin Stores: same-site https returns link saves with date; other-site https and http refused | **Pass**, but the refusal message is generic |
| 2 | Admin: support link add, clear, re-add | **Pass** |
| 3 | Alice claim wizard return: "Start with <store>'s returns page" plus support, new tabs; store with no links unchanged | **Pass** |
| 4 | Maker with claim page shows "<maker>'s warranty and support page"; support-only maker shows "customer support" | **Pass** |
| 5 | Stale-link banner after advancing the clock more than 12 months | **Not run**: needs Steve's approval for the clock change |
| 6a | Private sale: no returns link | **Pass**, with a wording nit |
| 6b | Not-returnable store: support only | **Pass** |
| 7a | Alice's private company returns link shows in her guidance | **Partial**: only support showed, since there was no return window on file (see below) |
| 7b | Bob cannot see Alice's private company | **Pass** |
| F1 | My Items superseded note (document, then typed Samsung 12-month) | **Pass** |
| F2 | Item To do card start date: unread drops and the Notifications notice shows done | **Partial**: unread dropped, but the notice stayed actionable |
| Opt | Push 28 typed-offer correction | **Not run** |

**Totals:** 9 Pass, 2 Partial, 0 Fail, 2 Not run.

## Details

### Batch A: Ops admin (Admin > Companies > "Edit pages")
The create dialog only takes Name, Website and "Claims or support page". The returns, warranty-claim and support links and their source page are set through "Edit pages".
- **P30 Returns Store** `01a1b301-ff58-708e-8e44-21f1202325c6`, website https://www.example.com
  - Step 1: the page showed "Returns page: https://www.example.com/returns · confirmed Nov 6, 2026 · read on this page".
  - Refusals: `https://www.iana.org/returns` and `http://www.example.com/returns` were both refused with "One or more validation errors occurred." The saved value stayed unchanged. **Observation:** the message doesn't say what's wrong (another site, or not https).
  - Step 2: the support link was added (confirmed Nov 6, 2026), cleared ("Customer support page: none"), then re-added.
- **P30 NoReturns Store** `01a1b304-44b1-754a-99f0-1754831f003c`: set to "No returns (the store says it takes none)", with support only.
- **P30 ClaimMaker** `01a1b304-6ee1-745f-a760-6427c87b6160`: warranty-claim page https://www.example.com/warranty plus support.
- **P30 SupportMaker** `01a1b304-8e4b-731e-90da-bd6212209d97`: support only.
- **Ops sign-in:** the Ops authenticator codes were rejected and Ops locked out. DB Stager reset Ops's two-step at 5:28 PM ET with Steve's OK, and Steve re-enrolled it. Admin screens are gated until two-step is on (screenshot `00-admin-gated-by-2step.png`).

### Batch B: Alice guidance
- **Staging:** I gave P30 Returns Store a current 30-day return window ("Everything else") so a return option exists.
- **Step 3:** P30 Store Return Item `01a1b307-dd0b-7243-be31-d82dfb758e0f`. The wizard showed "Start with P30 Returns Store's returns page" (https://www.example.com/returns) and "P30 Returns Store's customer support". Both links have `target=_blank`.
- **Control:** P30 NoLinks Item `01a1b309-f941-7c75-8db1-5a70e37bca27` at Home Depot showed the usual guidance with no company link lines.
- **Step 4:**
  - P30 ClaimMaker Item `01a1b30a-b157-75ff-88c2-2c0aa584a13d` showed "P30 ClaimMaker's warranty and support page" and customer support, both opening in new tabs.
  - P30 SupportMaker Item `01a1b30c-fc80-7fb8-ac0a-0b06c20d7747` showed "P30 SupportMaker's customer support" only.
  - Both needed a typed 12-month maker warranty before the warranty path appeared.
- **Step 6b:** P30 NoReturns Item `01a1b30f-ffb7-75d5-8cc5-7a932f8365a8` showed "None of your coverage fits this reason…" and a courtesy-return ask, plus "P30 NoReturns Store's customer support" only.

### Batch D: Alice private company and Bob
- **Step 7a, Partial.**
  - Setup: P30 Private Shop `01a1b2e6-1a3d-7e7e-8b72-06d18f6ca00f` (Mine, UNVERIFIED). Its Edit details form saved Returns page `https://example.com/returns` and Customer support `https://example.com/support`, and later Website `https://example.com`.
  - Result: on P30 PrivateCo Item `01a1b2e6-3c36-7043-af13-3c944288d659`, all three wizard reasons ended at "Nothing we know of covers this". They showed only "P30 Private Shop's customer support", which opens in a new tab.
  - Why Partial: Batch B shows the returns link appears only when a return window is on file, and the private company had none. So the link not showing may be by design. It's still unconfirmed whether a private company's returns link shows once a return window exists.
  - **Question for CC:** should a private company's returns page show even with no return window, the way "support" does?
- **Step 6a, Pass.** P30 PrivateSale Item `01a1b2e9-14c5-757e-8599-1060f749c1d0` showed no returns or support link. **Nit:** the text reads "Ask Private sale whether it will make a courtesy return…", treating "Private sale" as a company name.
- **Step 7b, Pass.** As Bob, searching "P30" in Stores & brands gives "Nothing matches"; the store picker offers only Add "P30 Private".

### Batch C: fixed rows (Alice)
- **F1, Pass.**
  - Item: P30 NoteAfterDoc `01a1b2dc-5126-7ed7-8e04-c10a62695240` (Samsung refrigerator). I applied the PDF, then added a typed Samsung 12-month warranty.
  - The item page showed the amber "Probably replaced by the policy read from your document".
  - My Items showed "Your own entry may be out of date". Dismissing it with the X stayed gone after a reload.
- **F2, Partial.**
  - Item: P30 StartDate `01a1b2e1-4749-7faf-aa2e-f6eece33ce53` (Sub-Zero). Saving Nov 6, 2026 on the To do card dropped the unread count from 5 to 4 and marked the To do entry Done.
  - Problem: in Notifications, "Enter the start date of your Sub-Zero warranty" still showed its "Enter the date" button (plus Flag, Mark unread, Delete). It was not shown as done.
  - The notice was created fresh for this new item; no reset was involved. Commits: API `bc78d21`, UI `0bb9a5b`.

## Needs CC
1. F2: the Notifications start-date notice isn't marked done when the date is saved from the item's To do card.
2. Admin link refusals show only "One or more validation errors occurred." It should name the rule (another site, or https only).
3. Clarify 7a: should a private company's returns page show when no return window is on file?
4. Wording: "Ask Private sale whether…" on private-sale items.

## Not run
- Step 5 (stale-link banner after more than 12 months): needs a clock advance and Steve's approval.
- The optional Push 28 typed-offer correction.

## Evidence
Screenshots are in `/workspace/uat/retest-bc78d21/batchA`, `batchB`, `batchC` and `batchD`, each with a `results.md`.
