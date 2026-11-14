# UAT retest: Push 99, Terms reader, download and sharing wording (S7.2.2)

- **Date:** Fri Nov 13, 2026, 3:48 to 3:56 PM ET
- **Build tested:**
  - API `929bc63` (startedAt 2026-11-13 19:55:43 UTC)
  - UI Last-Modified Fri, 13 Nov 2026 19:54:22 UTC (2:54 PM ET)
- **Notes:** `Bot Rules\CHANGES-push-99-terms-reader-and-sharing-wording.md` (2:53:38 PM ET). The UI is newer than the notes, so the build matches.
- **Accounts:** signed out, Alice (P34-Alice Repairs), and a new account `stevewash123.tester2+p99a@gmail.com` ("P99 Tester")

## Result: 4 Pass, 1 Fail (Low), 2 Info

| # | Check | Result |
|---|---|---|
| 1 | Sign-up (personal and business): sharing box, Terms/Privacy windows, closing, form kept, box unticked, "Please agree to continue." | **Fail (Low)**: one sub-check fails; everything else passes |
| 2 | Download in the window | **Pass** |
| 3 | /terms and /privacy: Download, 3 shared and 4 never-shared bullets, "Your choice" | **Pass** |
| 4 | Existing account (Alice): re-accept screen, window, "I agree" returns to the target, no second prompt | **Pass** |
| 5 | New account after this build: no re-accept screen | **Pass** |

## Fail (Low): a link inside the Terms window leaves the sign-up form
- **What happened:** In the Terms window on /signup, I clicked the "Disclaimer" link in the text. The link has no `target` attribute.
  - It opened a new /disclaimer tab.
  - It also sent the sign-up tab itself to /disclaimer.
  - Going back to /signup showed the typed email was gone.
- **Expected (notes):** links inside the text open in a new tab, and nothing typed is lost.

## Check 1 detail
- **Sharing box heading:** "WarrantyCat runs on shared knowledge, and sharing is on by default"
  - "Shared: the policy facts in what you add: store and brand names, return windows, warranty terms and conditions. Other people see them only after we have checked them, and never see who added them."
  - "Never shared: your receipts, photos and documents themselves, what you bought and paid, your credit cards, and your account details. The Terms list exactly what is and is not shared and how to ask us to stop."
- **Agreement line:** "I have read and agree to the Terms of Service and the Privacy Policy."
- **Terms window:**
  - It opens over the form.
  - Draft notice: "Draft for review. This text has not yet been read by a lawyer."
  - Version line: "Version 2026-11-13 · last updated November 13, 2026"
  - It includes "Sharing is on by default."
  - It scrolls, and it has Download and Close buttons.
  - Esc, a backdrop click and Close all close it.
  - After closing, the typed email was still there and the box was still unticked (checked=false).
  - Shots 05 and 07.
- **Privacy window:** same behaviour (shot 08).
- **"Create account" without ticking:** shows "Please agree to continue." (shot 09).
- **Business:** "For my business" adds a Business name field. The box is the same, and the Terms window opens and closes (shot 10).

## Check 2 detail
- **Terms file:** `WarrantyCat-Terms-of-Service-2026-11-13.txt`. It starts "Terms of Service", "Version 2026-11-13 · last updated November 13, 2026", then the full text ("What WarrantyCat is", …).
- **Privacy file:** `WarrantyCat-Privacy-Policy-2026-11-13.txt`. It starts "Privacy Policy", then the version line, then "What we keep", …

## Check 3 detail
- Download sits by the version line on both pages and saves the files named above.
- **What is shared (3 bullets):**
  - store, brand or credit card issuer names as printed, plus other names they go by
  - return windows, warranty lengths, conditions, exclusions, coverage terms and the links that state them
  - counts with no personal details
- **What is never shared (4 bullets):**
  - receipts, photos and documents themselves ("we may share the policy facts they state, never the files")
  - what you bought and paid, and order, serial and contract numbers
  - credit cards, including the last four digits
  - notes, name, email, phone, address and account details
- **"Your choice":** "You cannot turn sharing off inside the app yet, and a fact cannot be pulled back once it has been used. To ask us to stop sharing from your account, or not to use something you added, email support@warrantycat.com and we will act on it. [Lawyer to confirm this wording.]"
- "official warranty documents" appears nowhere on the pages or in either downloaded file.

## Check 4 detail (Alice)
- Going to /plans signed out sent me to /login?returnUrl=%2Fplans. Signing in led to /accept-terms?returnUrl=%2Fplans (shot 12), which says:
  - "Our terms have been updated"
  - "Please read the current Terms of Service and Privacy Policy and agree to carry on."
  - "What changed: the Terms now say plainly that sharing is on by default, exactly what is and is not shared, and how to ask us to stop."
  - Buttons: "I agree" and "Sign out".
- The screen has no nav. Going to /items was redirected back to /accept-terms.
- The Terms link opens the window (shot 13).
- "I agree" went to /plans (shot 14), and it stayed there after a reload.
- After signing out and back in, there was no prompt (shot 15). The final sign-in also had no prompt (shot 19).

## Check 5 detail (new account)
- Sign-up with the box ticked showed "Check your email … Nothing is created until you do." (shot 11).
- The confirmation link signed the account straight in on /orientation ("Welcome to WarrantyCat, P99", shot 16).
- /items and /plans opened normally, with no /accept-terms redirect (shots 17 and 18).

## Info
1. **Confirmation email in spam:** the confirmation email ("Confirm your email to start with WarrantyCat", from noreply@stuff.microsaasbuilders.com, 20:51:34 UTC) landed in Gmail **Spam** for tester2. Also, its link points to `dev.warrantycat.com`. I opened the same path on stuffit-ui.onrender.com.
2. **Stale first load:** the first page load in the existing tab still ran the old build, with no "new version" banner. It showed an old-style /accept-terms with no "What changed" line, and the old sharing box saying "official warranty documents … are shared" (shots 01 and 02). A hard reload loaded the new build. All results above are from the new build.

## Fixtures and leftovers
- No fixture files.
- The new test account `stevewash123.tester2+p99a@gmail.com` ("P99 Tester") now exists and is empty. It can be deleted or reused.
- Alice has accepted terms version 2026-11-13. Bob and Ops will still get the prompt on their next sign-in.

Screenshots are in the box folder `/workspace/uat/push99/shots/` (01 through 19).
