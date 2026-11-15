# UAT retest: Pushes 104 and 105, policy source badge and 90-day recheck

- **Notes:**
  - CHANGES-push-104-policy-source-badge.md (written 10:12:21 AM ET)
  - CHANGES-push-105-recheck-sweep.md (written 10:12:21 AM ET)
- **Build tested:**
  - API `c593687`, read from /api/version. It started at 10:03 AM ET (15:03:44 UTC).
  - UI Last-Modified Sat, 14 Nov 2026 15:02:26 UTC (10:02 AM ET).
  - The notes file is 10 minutes newer than the UI. Steve said the notes were written after the push and cover UI `0194421`. The live UI bundle contains the badge component (`app-policy-source-badge`), the "AI confirmed" date line and the new company wording.
- **Data:**
  - Testing was paused at 10:27 AM ET because Neon `stuffit` didn't have the ski data yet. It still held the Oct 27 placeholders and had no Rossignol, K2 or Smith policies.
  - DevOps Controller removed the placeholders and loaded the ski files.
  - Before resuming, I checked with read-only SQL:
    - Placeholder evidence: 0.
    - Accounts: 15.
    - Rossignol has 1 policy, K2 has 3 and Smith has 1, each with its brand's warranty URL.
    - evo, Christy Sports, Backcountry and L.L.Bean each have 1 return policy. Backcountry and L.L.Bean have no `verified_at`.
  - Steve confirmed the data and gave the go at 4:18 PM ET.
- **Run:**
  - Sat Nov 14 2026, 4:20 to 5:00 PM ET.
  - Box browser, with real mouse and keyboard input.
  - A hard reload came first.
- **Accounts:**
  - Alice (QA Test 1), in P34-Alice Repairs.
  - Ops (QA Test 4).

## Summary
8 Pass, 0 Fail, 2 Not tested, 4 Info.

| # | Check | Result |
|---|-------|--------|
| 104-1 | Re-accepting the Terms on sign-in, and the new paragraph | Pass (Alice and Ops) |
| 104-2 | Rossignol, K2 and evo badges: "AI verified from company website", the confirm prompt, 11/13/2026, the brand's link opening in a new tab | Pass |
| 104-3 | The Backcountry return line says there is no source on file | Pass |
| 104-4 | Report a problem: Feedback opens as a prefilled Problem, sends, and appears in Alice's list and in Admin > Feedback | Pass |
| 104-5 | A company with no policy shows "We don't have this company's terms yet." | Pass |
| 104-6 | `GET /api/policy-source/...`: 401 when signed out, the status, label and URLs, and no account ids | Pass |
| 105-1 | The drill-down reads "AI confirmed 11/13/2026", with no admin line and no recheck note | Pass |
| 105-2 | Nothing else on screen changed | Pass (within what this run touched) |
| 105-3 | The 90-day recheck sweep (02:00 UTC job) | Not tested, as the notes say. It hasn't run yet (`policy_source_checks` has 0 rows). |
| - | Old scenarios that relied on placeholder terms (Vizio "not the real terms") | Not tested, as the notes say |

## Details
1. **Terms (shots 01, 32)**
   - Alice got the re-accept screen after signing in, and so did Ops ("Our terms have been updated"). Both accepted, and Alice's account is now on version 2026-11-14.1.
   - The paragraph headed "Reminders are a convenience, not a promise." now says the following (quoted in part): "The policy information in WarrantyCat comes from public sources, mostly the companies' own web pages read automatically, and sometimes from documents that accounts upload. It may be out of date or wrong, and it is not a guarantee that anything is covered. Every policy shows where its terms came from, and when, and how far they have been checked ... Where we have no source for a company's terms, we say so instead of guessing. You can report a problem with any policy from its source details."
2. **Badges on the item page (shots 11 to 16, 20, 23, 26)**
   - I used two new items: "Rossignol Experience 82 skis 2" from evo (order P104-EVO-2) and "K2 Mindbender 99Ti skis 2" from Backcountry (order P104-BC-2). Their item pages have a "Suggested coverage" card.
   - The panels for the Rossignol manufacturer line, the evo return line and the K2 manufacturer line each read: "AI verified from company website / Please confirm this matches your item. / AI confirmed 11/13/2026".
   - The links were https://www.rossignol.com/us-en/ls-warranty-policy.html, https://www.evo.com/pages/returns and https://k2snow.com/en-us/support/warranty-policy. Each opened in a new tab.
   - The panels fit the card without overlapping or clipping. No extended plan was involved, so I saw no badge on one.
3. **Backcountry (shot 25):** the panel read "We don't have this company's terms on file yet, so this one is not backed by a source. Please check it with the company." It had no link.
4. **Report a problem (shots 17, 18, 22, 24, 34, 35)**
   - From the K2 panel, Feedback opened with Problem selected and this message prefilled: "About this policy: K2 Manufacturer warranty (manufacturer/01a1dbde-0a54-71bc-a5db-0fe4d632d52f)".
   - After sending, it shows in Alice's "Your messages" as "Problem · Nov 14, 2026", with status Received.
   - Ops sees it in Admin > Feedback as a Problem from QA Test 1, sent 4:51:08 PM, with status Received.
5. **Company wording (shots 36, 37, 39, 40)**
   - A. O. Smith has no policy. Its company page reads "We don't have this company's terms yet." The old "No warranty recorded yet." didn't appear, and the Brands list shows "No warranty on file".
   - Rossignol's page shows its confirmed 2-year warranty and a source link.
6. **API**
   - Signed out, curl got 401 for both `/api/policy-source/manufacturer/<id>` and `/api/policy-source/seller/<id>`.
   - Signed in, I read the requests the app made in the DevTools Network tab. Rossignol, evo and K2 each returned 200.
     - Rossignol's body was: `{"status":"aiVerified","label":"AI verified from company website","prompt":"Please confirm this matches your item.","accounts":0,"latestOn":"2026-11-13","reviewedOn":null,"urls":["https://www.rossignol.com/us-en/ls-warranty-policy.html"],"adminVerifiedOn":null,"aiConfirmedOn":"2026-11-13","userConfirmedOn":null,"recheckNote":null}`.
     - All dates were date-only. There was only a count, and no account ids.
   - Backcountry returned 404 (see Info 2).
   - No headers or tokens were copied.

## Info
1. **The shield appears only on the item page.** The Add form also has a "Suggested coverage" list, with Source links that open the company's page directly, but it has no shield. The notes don't say which list. The badge appears on the item page's card, so I passed it there. If the Add form should have it too, that's a gap (shots 02, 03).
2. **An unconfirmed policy returns 404.** The UI handles it and shows the no-source text, but in the API an unconfirmed policy looks the same as an unknown one. The notes list 404 only for "unknown or invisible". If you'd rather have a `none` status, that's a small API change.
3. **K2 suggestion for skis.** The K2 skis got "K2 warranty, 1 year, Likely", tagged with a different category (SKI BOOTS AND BINDINGS). Its own text says it covers ski boots, snowboard boots and snowboard bindings, not skis. K2 has 12-, 24- and 36-month policies, so the 1-year boots/bindings one was offered for skis. This is a data or category-matching question, not a badge bug.
4. **The Terms screen doesn't show the version.** It says "Our terms have been updated" and doesn't name 2026-11-14.1. That's only cosmetic.

## Test data left behind (staging)
- Alice, P34-Alice Repairs: purchases P104-EVO-1 (Rossignol skis and a Smith helmet from evo), P104-BC-1 (K2 skis from Backcountry), P104-EVO-2 and P104-BC-2.
- One Problem feedback from Alice.
- Alice and Ops have both accepted Terms 2026-11-14.1. Bob and the others will be asked at their next sign-in.
- No fixture files were created.
