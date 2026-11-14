# Push 99: read the Terms in a window, download them, and say plainly what is shared (S7.2.2)

API and UI together. Terms version moves from 2026-10-01 to **2026-11-13** (API `LegalVersions.Current` and the UI `TERMS_VERSION`). **Every existing account, including the QA accounts (Alice, Bob, Ops), is asked to accept the new terms once** the next time they sign in or the page loads: they see "Our terms have been updated" and must press "I agree" before anything else opens. That screen is part of what to test.

## What changed
- **Sign-up.** The Terms of Service and Privacy Policy links in the agreement line now open the text in a window over the form, so nothing typed is lost (they still work as normal links if the window cannot open). The box stays unticked until the person ticks it.
- **The window.** Title, version and date, the draft notice, the text, a **Download** button (a .txt file named like `WarrantyCat-Terms-of-Service-2026-11-13.txt`) and **Close**. Esc, the backdrop and Close all close it; links inside the text open in a new tab.
- **Download on the pages too.** /terms and /privacy have a Download button by the version line.
- **The wording.** The Terms now say: sharing is **on by default**; what **is** shared (the name of a store, brand or card issuer as printed and other names it goes by; return windows, warranty lengths, conditions, exclusions, terms and links; counts with no personal details); what is **never** shared (receipts, photos and documents themselves, what you bought and paid, order/serial/contract numbers, credit cards including last four digits, notes, name, email, phone, address, account details); that others never see who added a fact; and, plainly, that sharing **cannot be turned off inside the app yet** (email to ask us to stop). The old text said uploaded "official warranty documents" are shared; the app only shares the policy facts in them, so that claim is gone. The Privacy Policy's sharing paragraph says the same in short. The sign-up box carries a short plain-language version.
- The "terms updated" screen has the same reader and says what changed.

## What to check
1. **Sign-up** (/signup, personal and business): the "shared knowledge, and sharing is on by default" box lists Shared and Never shared. Click "Terms of Service": the window opens over the form with the draft notice, Version 2026-11-13 and the Sharing is on by default text. Scroll; Esc/Close/outside click closes it; the email you typed is still there; the agreement box is still unticked. Same for "Privacy Policy". Creating the account without ticking still says "Please agree to continue."
2. **Download** in the window: a text file starts with the title, version and date, then the whole text.
3. **/terms and /privacy** pages: Download button works; the Terms show the two bullet lists (3 shared, 4 never shared) and the "Your choice" paragraph.
4. **Existing account:** sign in as Alice (or any existing account): the "Our terms have been updated" screen appears with the line about what changed; the Terms link opens the window; "I agree" lets you through to where you were going; after that, no more prompts.
5. A new account created after this build records the new version (no re-accept screen on first sign-in).
Everything else should be unchanged.
