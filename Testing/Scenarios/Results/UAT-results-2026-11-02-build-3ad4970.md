# StuffIt UAT results: build 3ad4970
**Build:** commit 3ad4970, startedAt 2026-11-02T21:38:25Z (4:38 PM ET), Staging.
**Run:** Nov 2, 2026, 4:41–5:04 PM ET.
**Scope:** retests of the three fixes (sign-up, reset links, export) and the new plans FS-33, FS-34 and FS-35 from `Testing\Scenarios`. The other plans weren't rerun; their results are in the d1ed2c0 report. The simulated clock wasn't used.

## Summary
| Plan | Area | Pass | Partial | Fail | Headline |
|---|---|---|---|---|---|
| Fix: FS-25-12 | Sign-up with a taken address | 1 | 0 | 0 | Same page for taken and new addresses; the owner gets an email. |
| Fix: FS-25-17 | Two reset links | 1 | 0 | 0 | The older link is refused and the newest one works. |
| Fix: FS-27-13/14 | Data export | 1 | 0 | 1 | Prepares in 6 s, but "Download (5 KB)" says "That download is no longer available." |
| FS-33 | What to track | 14 | 2 | 0 | The setting works. 2 of 12 receipt lines are missing from New Items. |
| FS-34 | Color theme | 11 | 4 | 0 | Works with no flash. The partials are test limits (device dark mode, private-window sign-in, true phone width). |
| FS-35 | Send feedback | 17 | 0 | 0 | Works. Long messages overflow the page. |

## Issues (most important first)
1. **Export download fails (FS-27-14).** The row says "Ready until Nov 9, 2026", but clicking Download gives "That download is no longer available. Prepare a new one." every time, including after a reload. No file is saved. Delete-account still tells people to download first.
2. **Receipt lines missing from New Items (FS-33-3).** On the 12-line Pine Street receipt, WOOD GLUE 16OZ ($6.99) and SANDPAPER 80G x5 ($12.45) never appeared. The list reads "Showing 10 of 10". I didn't check the Dismissed tab. These are the two cheapest lines, so they may have been dropped instead of placed under "Smaller things".
3. **Work gloves aren't demoted (FS-33).** Work gloves at $25.98 are labelled "Under $50" and "Under $250", but they stay in the main list at both settings, while other lines under the minimum move.
4. **Long feedback overflows (FS-35-9).** A 4,000-character message makes the page scroll sideways. Typing also stops at 4,000 silently, with no counter or message.
5. **Possible sign-up timing leak (FS-25-12).** A taken address seemed to take over 4 s to respond, against a quicker response for a new one. This wasn't measured precisely, so it's worth checking with timing in the API.
6. **Small things.**
   - The FS-33 note still says "Using the standard amount" after clicking Everything, until you save.
   - The feedback page's own footer and menu links nest `from` (`from=%2Ffeedback%3Ffrom%3D…`).
   - The "Write a message first." error isn't announced as an alert.
   - The older reset email has no "Requested at" line (only later ones do).
   - The page title is "WarrantyBank".
   - There's 1 console error on /login.

## Fixed and confirmed
- Reset links: only the newest link works now.
- Sign-up no longer reveals which emails are registered.
- The export job now prepares. The download step is still broken, as issue 1 describes.

## Test data left behind
- **Alice:**
  - 10 pending Pine Street lines in New Items
  - 5 feedback messages
  - Her password was set to the same saved value through the newest reset link.
- **Bob:**
  - 1 feedback message
  - 1 prepared export
- **Sign-up probe:** an unconfirmed request for `stevewash123.test+probe1102@gmail.com`. Nothing was created.
- Everything else is as listed in the d1ed2c0 report.

---
# Retest of fixes — build 3ad4970 (startedAt 2026-11-02T21:38:25Z, 4:38 PM ET)
| Plan step | Result | Notes |
|---|---|---|
| FS-25-12 sign-up with taken address | **Pass** | Taken (stevewash123.test@gmail.com) and new (+probe1102) both land on /signup "Check your email" — "We sent a link to <email>. Open it to finish creating your account. It works for 24 hours." / "Nothing is created until you do…". Identical apart from the address. Owner got "You already have a WarrantyBank account" ("Someone tried to sign up for WarrantyBank with this email address, but you already have an account…"); new address got "Confirm your email to start with WarrantyBank". Note: taken-address submit still showed "Sending…" after ~4 s (not measured precisely; possible timing leak). |
| FS-25-17 two reset requests | **Pass** | Requests 4:42 and 4:43 PM ET; both "If that email is registered, we sent a link…". Newest email says "Requested at 4:43 PM. If you asked more than once, use the newest email." Older link: "This link has already been used or has expired. Request a new one." Newest link: "Your password was changed. Sign in with the new one." Sign-in works. (Older email lacks the "Requested at" line — only the second carries it.) |
| FS-27-13 prepare download | **Pass** | 4:46:30 PM "Preparing your download…" → 6 s later "Nov 2, 2026 · Ready until Nov 9, 2026", "Download (5 KB)". |
| FS-27-14 download the zip | **Fail** | Clicking "Download (5 KB)" → red alert "That download is no longer available. Prepare a new one." Same after reload. No file. Row still says ready until Nov 9. |
Screenshots: older link 7a1ccdb6….png, newest e19dcc58….png, download error eda64bad….png
Other: page title "WarrantyBank"; 1 console error on /login (not inspected). Probe sign-up left an unconfirmed +probe1102 request (nothing created).

---
# FS-33 What is worth tracking — build 3ad4970 (4:48–4:53 PM ET). Alice, Bob. Receipt: SampleData 12-thermal-long-many-items.pdf (Pine Street Hardware, 12 lines, $485.95).
Precondition met: Alice New Items "Nothing waiting…".
| # | Result | Notes |
|---|---|---|
| 1 | Pass | Settings tab "What to track". |
| 2 | Pass | "What is worth tracking". "Track things worth at least this much. Smaller lines on a receipt are listed under "Smaller things" in New Items and are not ticked for you. Nothing is hidden or deleted, and one click tracks any of them." Field "Track things worth at least" = 50; note "Using the standard amount, $50.00. Zero tracks everything." Buttons Everything / Only larger purchases / Use the standard amount / Save. First load "Loading…" ~2.3 s. |
| 3 | **Partial** | "Smaller things (6)" ("Under your tracking minimum and probably not worth a warranty. Track any you want, or dismiss the rest together."): supply line $14.99, ext cord $24.99, LED bulb $21.98, tarp $18.99, painters tape $23.16, roller cover $17.98, each "Under $50 · <reason>". Main list: Work gloves $25.98 ("Under $50" but not demoted), paint $116.97, deck screws $65.98, stud $110.16. **WOOD GLUE $6.99 and SANDPAPER $12.45 missing**: "Showing 10 of 10" for a 12-line receipt (Dismissed tab not checked). |
| 4 | Pass | Everything → 0. |
| 5 | Pass | "Saving…" → "Saved" + toast "Saved." |
| 6 | Pass | 0 after reload; note "The standard amount is $50.00. Zero tracks everything." |
| 7 | Pass | No Smaller things section; all 10 in main list. |
| 8 | Pass | 250, Saved; "Smaller things (9)" vs 6; only Work gloves left in main list. |
| 9 | Pass | 100001: "Not saved" "Choose an amount from 0 to 100,000."; 250 kept. |
| 10 | Pass | -5: same; 250 kept. |
| 11 | Pass | Empty → saved as standard (50), "Using the standard amount, $50.00…"; no message, no error. |
| 12 | Pass | At 20: Smaller things (3) supply line $14.99, tarp $18.99, roller cover $17.98 ("Under $20 · …"); $21.98–$25.98 lines stay in main list. |
| 13 | Pass | "Use the standard amount": Saved; note back; Smaller things (6) as step 3. |
| 14 | Pass | Bob shows 50 "Using the standard amount" while Alice = 250. |
| 15 | Pass | Bob New Items "Nothing waiting…"; nothing of Alice's. |
| 16 | Partial | 250 seen in step 14, but the value on re-sign-in wasn't captured (tool error); restored to standard afterwards. |
Other: Work gloves ($25.98) is labelled "Under $50"/"Under $250" but stays in the main list at both. Reason text mentions the amount ("Under $20", "Still to check. Under your $N minimum."). Before Save, the note still says "Using the standard amount" with 0 in the field.
Left: Alice New Items has 10 pending Pine Street lines; setting back to 50.
Screenshots: 2 3b5ef7e8….png, 3 7d2ebacd….png, 8 e90a092a….png, 12 79116c3e….png

---
# FS-34 Color theme — build 3ad4970 (4:54–5:00 PM ET). Alice, Bob. Box Chrome, device set to light.
| # | Result | Notes |
|---|---|---|
| 1 | Pass | "Appearance"; Color theme Teal/Indigo/Berry with swatches; Light or dark: Match my device / Light / Dark. Start: Teal + Match my device ("Using light because that is your device's setting."). Note: "This choice is kept on this device. It is not yet saved to your profile, so other devices keep their own." |
| 2 | Pass | Indigo applied at once, no reload (header, heading, tab underline, avatar, pills). |
| 3 | Pass (note) | Home, My Items, New Items, item page, Settings all Indigo. Fixed colours (look intentional): green "Quick set-up is not finished" box, red/orange warning cards, blue "Link your email" and orange "Add an item" buttons. |
| 4 | Pass | Berry then Teal at once; Teal same as start. |
| 5 | Pass | Dark readable on all pages checked (badges, warning cards, fields, notices). "Returned" row and grey small print dim but legible. |
| 6 | Pass | Light back. |
| 7 | Partial | Light line shown and correct; couldn't switch the device to dark, so the dark variant not seen. |
| 8 | Pass | Berry dark reload: first frame plain dark maroon, no teal/light flash. |
| 9 | Pass | New tab: Berry dark. |
| 10 | Pass | Sign-in page uses the saved theme. |
| 11 | Pass | Bob in same browser sees Berry + Dark (per device). |
| 12 | Partial | Incognito sign-in page shows default Teal light; couldn't sign Bob in there (saved login fill not available in that window). |
| 13 | Pass | Cleared site data → default Teal / Match my device; works; "Alpha test…" banner reappears. |
| 14 | Pass (approx.) | Tested by zoom (~427 px wide), not a true 390 px: phone layout with bottom nav, choices fit; only the Settings tab row scrolls sideways (own scrollbar). |
| 15 | Pass | /terms and /disclaimer use Berry dark, readable. |
No colour clearly ignored the theme; no unreadable dark-mode text; no flash. Reset to Teal + Light at end.
Screenshots: 1 c07ccc4a….png; 3 4990a382…, 9d8332cd…, 068a7ec6…, a3f82738….png; 5 f300b339…, 30e792ea….png; 8 62c4fae8…, 92597053….png; 14 e44f4eba….webp; 15 b730d382…, 27721c97….png

---
# FS-35 Send feedback — build 3ad4970 (5:00–5:04 PM ET). Alice, Bob. Precondition met ("You have not sent any messages yet.").
| # | Result | Notes |
|---|---|---|
| 1 | Pass | Footer, Account menu, and /account ("Send feedback – Ask a question, suggest something or report a problem."). The /account link has no `from=`. |
| 2 | Pass | "What will be sent with your message" — "Page you were on: /items", "App version: 3ad4970", "Nothing else about your items, purchases or cards is sent."; no Item line. |
| 3 | Pass | "Page you were on: /items/01a19c7d-…", "Item: 01a19c7d-8300-74db-840f-dfb6bc678e73". |
| 4 | Pass | "Write a message first." (red, under the box; appears ~1 s late; not announced as an alert). Nothing sent. |
| 5 | Pass | "Sending…" → "Thank you. We received your message." (~1–1.7 s); box cleared. |
| 6 | Pass | "Question · Nov 2, 2026", "Received", "UAT question one". |
| 7 | Pass | Problem / Suggestion / Question, newest first, all "Received". |
| 8 | Pass | All three after reload. |
| 9 | Pass (note) | maxlength 4000: typing stops silently at 4000, no message. Sent and accepted. **The long text overflows its card and makes the page scroll sideways.** |
| 10 | Pass | Shown literally as `<b>bold</b> & "quotes"`. |
| 11 | Pass | Five accepted (steps 5, 7, 9, 10). |
| 12 | Pass | "You have sent several messages in the last hour. Please try again a little later." Nothing added; "UAT sixth" kept in the box. |
| 13 | Pass | Bob: "You have not sent any messages yet."; none of Alice's. |
| 14 | Pass | Bob "UAT question from Test2" accepted and listed alone. |
| 15 | Pass | Alice sees only her five. |
| 16 | Pass | `?from=https://example.com/x` → "Page you were on: none". |
| 17 | Pass | Signed out → /login?returnUrl=%2Ffeedback. |
Other: types "Question", "Suggestion", "Problem"; status "Received". Footer/menu links while on /feedback carry a nested from (from=%2Ffeedback%3Ffrom%3D…), so "Page you were on" would show /feedback. Loads ~2–2.8 s.
Left: Alice 5 feedback messages, Bob 1 (can't rerun 13 on Bob without new data; rate limit 5/hour).
Screenshots: 3 f0216d60….png, 7 2e49bccf….png, 12 f4363128….png (2 and 13 not captured).

---
