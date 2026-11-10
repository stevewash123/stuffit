# Push 49: About page, login blurb, public footer, configurable contact values (2026-11-10)

UI only. No API change, no migration. Not pushed yet: waiting for your Scenario 69 run to finish.

## Action for QA, before testing this build: set two Render variables on the UI static site
Render > the UI service (StuffIt_UI) > Environment:

| Variable | Value |
|---|---|
| `WARRANTYCAT_CONTACT_EMAIL` | `support@warrantycat.com` |
| `WARRANTYCAT_BUSINESS_NAME` | `WarrantyCat` |

They are read at BUILD time (a prebuild script writes them into `environment.ts`), so the UI must be rebuilt/redeployed after they are set. If they are not set, the footer shows `© 2026 [Business name]` and the contact address defaults to `support@warrantycat.com`. Values with quotes, backslashes, `$`, `<` or `>` make the build fail on purpose.

## What changed
| Change | What to check |
|---|---|
| Login page: one-line blurb above the form | "WarrantyCat tracks your return windows and warranty expirations and reminds you before they close. Currently in private beta." |
| Public footer on the login page and every signed-out screen (sign-up, reset password, etc.) | About · Privacy · Terms · support@warrantycat.com · © 2026 WarrantyCat. Links work; the email opens a mail draft |
| Same footer under the legal pages | Terms, Privacy, Disclaimer, Text reminders and About all end with it |
| New public page `/about` (no login) | What it is, private beta, email reminders and optional text reminders (1 to 5 a month, Msg & data rates may apply, STOP/HELP), contact with business name and email |
| Terms/Privacy/Text reminders contact line | Now shows support@warrantycat.com (was support@microsaasbuilders.com) |

## Not changed / not built yet (do not report)
- The mobile number field and the unchecked text-reminder consent box in notification settings, and the sms-optin.png screenshot: not built yet.
- The mailing address on Privacy/Terms is still a bracketed placeholder.
- The logged-in app footer is unchanged.
