# What changed in push 35: business gaps and the per-account upload queue (2026-11-07)

For GrokBot. Pushed together with push 36 (API `619cfcd`, UI `c7a7367`; push 35 itself is API `c103d4a`, UI `8752182`). Check `/api/version` (`commit` must be `619cfcd`). No migration. Stories S8.1.1, S8.1.5, S8.1.6. Push 34 UAT findings are NOT fixed in this push; they follow in push 36.

## Business gaps
- **Free-year reminder (S8.1.5):** the owner of a business gets a notice (and email) at 30 and at 7 days before the free year ends (once per point per end date; Business:FreeYearReminderDays). The plan page shows the matching wording.
- **Account name on notices (S8.1.6):** emails and digest lines name the account ("Acme Plumbing: ...") when the person has more than one account.
- **Switch account link:** a "Switch account" link in the account menu for people with two or more accounts.

## Upload queue is per account and per person (UI)
- A photo queued on the phone while in one account is only listed and sent while that account (and person) is in use. Previously it went into whichever account was active when it sent.
- Old queued batches with no account: a single-membership person adopts them; a multi-account person is asked (a prompt) which account they belong to. Files received through the share sheet are stamped with the account they arrived in.

## Check
1. Queue a photo in the business, switch to personal, confirm it is not listed or sent there; switch back, it sends into the business.
2. A person with two accounts sees notices naming the account.
3. Business owner near free-year end receives one reminder at 30 days and one at 7 days, no repeats.
