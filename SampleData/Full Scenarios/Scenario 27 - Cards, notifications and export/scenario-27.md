# Scenario 27: Cards, notifications and preferences, data export

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com). Test2 is deleted at the end; Test1 stays.
**Preconditions:** Both accounts exist (Scenario 25). Test1 has at least one purchase from Scenario 26. The test inboxes receive mail from the app.
**Time:** 40 min
**Why this plan:** the card list, the notification centre and email preferences were checked end to end, and the export and account deletion are built with tests. This exercises settings pages, a state change that clears a notice, and a real destructive flow.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test2 | Open the bell/Notifications page on a brand-new account | A standing notice about confirming card benefits (or an empty state if none). Record the exact text |
| 2 | Test2 | Go to Credit cards. Add a card from the list of known card products (for example a Chase or Discover card the list offers), nickname "UAT Card", last 4 `4242` | Saved and shown in the list |
| 3 | Test2 | Open the card's detail page | Shows its benefits; each is marked verified or unverified. Record which |
| 4 | Test2 | Add a second card with a made-up name that is not in the list, last 4 `0001` | Saved as an unlisted card; the page asks whether it is one of the known ones ("Is yours one of these?") |
| 5 | Test2 | Add a card with the same last 4 `4242` again | Handled sensibly (a warning or refusal), no error page |
| 6 | Test2 | Return to Notifications | The standing card notice has changed or cleared according to whether a card now has confirmed benefits. Record what changed and whether that is consistent |
| 7 | Test1 | Open Settings, then Notifications | A list of notification types in groups, each with email and in-app toggles. Mandatory ones are locked |
| 8 | Test1 | Turn email off for one optional type, leave another on, reload the page | Both settings persisted after the reload |
| 9 | Test1 | Open Settings, Email | The email address shown is the Test1 address; no way shown to break the account by clearing it |
| 10 | Test1 | Open the To do page (/todos) and the Returns page | To do loads with a friendly empty state. Returns loads without error but is a labelled first design ("First design: example data") showing sample returns, not Test1's; see Scenarios 29 and 32 for the real ones |
| 11 | Test1 | Open a reminder email if one has arrived in the inbox (the app may send nothing yet; if so, note "none arrived") | If one exists: it names the item, the date is right, it has an unsubscribe link |
| 12 | Test1 | If a reminder email arrived, open its unsubscribe link | A page confirms which notification type was turned off. Sign in and check Settings, Notifications agrees |
| 13 | Test1 | Open Settings, Privacy and find **Export my data** | An export starts or downloads; record the file name and type |
| 14 | Test1 | Inspect the export (open it) | Contains Test1's items and settings only. No Test2 data, no password hashes |
| 15 | Test2 | Open Settings, Privacy and find **Delete my account** | A clear warning about what is removed; a confirmation step is required |
| 16 | Test2 | Cancel out of it | Nothing is deleted; still signed in |
| 17 | Test2 | Delete the account and confirm | Signed out; message says it was deleted |
| 18 | Test2 | Try to sign in with the Test2 address and its password | Refused with the generic failure message |
| 19 | Test1 | Reload My Items | Test1's data is untouched |
| 20 | Test2 | Sign up again with the Test2 address | Allowed (or a clear explanation if deleted accounts are held for a period). Record which |

If step 17 deletes Test2, the next run starts again from Scenario 25 for that account.
