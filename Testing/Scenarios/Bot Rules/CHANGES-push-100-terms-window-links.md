# Push 100: a link inside the Terms window no longer moves the sign-up page (fix for the Push 99 Low)

UI only (API unchanged at 929bc63). Push 99 (the Terms reader, download and sharing wording) passed 4 of 5; the Low: clicking a link inside the Terms window (for example "Disclaimer") opened a new tab but also sent the sign-up tab itself to that page, losing the typed email. Cause: the page's router handles a link click before the reader's own handler ran. The reader now catches the click first (capture phase), opens the link in a new tab, and stops the router from acting on it.

## What to check (/signup, and the "Our terms have been updated" screen)
1. Open the Terms of Service window on /signup, type an email in the form first. Click each link inside the text (Disclaimer, Text message reminders, Privacy Policy and any other): each opens in a **new tab**, and the sign-up tab stays on /signup with the email still typed and the Terms window still open.
2. Same in the Privacy Policy window.
3. On the "Our terms have been updated" screen (an existing account that has not accepted yet), the same links in the window open new tabs and the screen stays put.
4. Nothing else changed: Download, Close, Esc, the backdrop click.
