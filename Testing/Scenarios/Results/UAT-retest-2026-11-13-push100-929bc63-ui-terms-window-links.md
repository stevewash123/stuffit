# UAT retest: Push 100, links inside the Terms window no longer move the page (fix for the Push 99 Low)

- **Date:** Fri Nov 13, 2026, 4:06 to 4:10 PM ET
- **Build tested:** API `929bc63` (unchanged) and UI Last-Modified Fri, 13 Nov 2026 21:02:04 UTC (4:02 PM ET)
- **Notes:** `Bot Rules\CHANGES-push-100-terms-window-links.md` (4:01:04 PM ET). The UI is newer than the notes, so the build matches.
- **Accounts:** signed out (/signup), Bob (who had not yet accepted terms 2026-11-13), Alice

## Result: 4 Pass, 0 Fail. The Push 99 Low is fixed.

| # | Check | Result |
|---|---|---|
| 1 | Terms window on /signup: each link opens a new tab; the sign-up tab stays on /signup with the email typed and the window open | **Pass** |
| 2 | The same in the Privacy Policy window | **Pass** |
| 3 | The same on the "Our terms have been updated" screen | **Pass** |
| 4 | Download, Close, Esc and backdrop click are unchanged | **Pass** |

## Detail
**/signup** (signed out, email `p100check@example.com` typed with real keystrokes):

| Window | Link | New tab | Page stays, window open, email kept |
|---|---|---|---|
| Terms | Disclaimer | /disclaimer | Yes |
| Terms | Text message reminders | /sms | Yes |
| Terms | Privacy Policy | /privacy | Yes |
| Privacy | Terms | /terms | Yes |
| Privacy | Text message reminders | /sms | Yes |

Regression checks:
- **Download:** saves `WarrantyCat-Terms-of-Service-2026-11-13.txt` and `WarrantyCat-Privacy-Policy-2026-11-13.txt`, and the window stays open. The box browser saved them with " (2)" added because of earlier copies.
- **Closing:** Close, Esc and a backdrop click each close both windows.
- **Form state:** afterwards the email was still typed and the agreement box was unticked. No account was created.

**/accept-terms (Bob):**
- Signing in landed on /accept-terms?returnUrl=%2F.
- The same three Terms-window links and two Privacy-window links each opened a new tab. The screen stayed on /accept-terms with the window open.
- Esc closes the window.
- "I agree" went to / ("Welcome, QA") at 21:08:56 UTC.

## Notes
- **Stale tab:** an older open tab showed the "A new version of WarrantyCat is ready" banner; it was closed. The test tab had a hard reload and showed no banner.
- **Bob:** Bob has now accepted terms 2026-11-13. Ops is still unprompted.
- **Missing shots:** there are no screenshots of the windows open on /accept-terms (the captures failed). The results come from the tab and URL readings.
- **State at the end:** Alice was signed back in on / at 21:09:23 UTC.

## Fixtures and cleanup
None. No accounts or items were created.

## Screenshots
In box `/workspace/uat/push100/shots/` (01 to 07):
- signup Terms open
- signup Terms after links
- signup Privacy after links
- signup after regression
- accept-terms
- Bob home after agreeing
- Alice signed in
