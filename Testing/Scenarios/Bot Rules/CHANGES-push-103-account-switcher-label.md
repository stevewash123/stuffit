# Push 103: the account switcher shows the account that is really active (from the Push 101/102 Info)

UI change plus an API test (no API behaviour change). Push 102 passed (4 Pass, 3 Not tested). Its Info: the header's account switcher kept showing the wrong account: after switching to Personal it still said "P34-Alice Repairs", and Bob's switcher said "Personal" while the page and header were the business. Cause: the dropdown set its value before its options were built, so the browser fell back to the first option whatever the active account was. Each option now says whether it is the selected one.

## What to check (any account that belongs to more than one: Alice has Personal and P34-Alice Repairs; Bob is an employee in the business)
1. Switch from the business to Personal (and back): after each switch and the page reload, the switcher shows the account you are really in, and the header (business name shown or not) and Settings > Privacy and data (file count, sharing card) agree with it.
2. Hard reload on each account: the switcher still shows that account.
3. Sign in fresh as Bob (his last-used account may be the business): the switcher matches the header, not the first item in the list.
4. After ticking or unticking sharing in Settings, the switcher label does not change.
5. Unchanged: the "(n new)" notice counts on the other account's option, the account menu, and the chooser page.

## Also in this push (API, tests only)
`PUT /api/privacy/sharing` as an employee of a business gets 403 and changes nothing; the owner can turn sharing off. This was Not tested in Push 101 and 102 because it needs a raw API call.

## Not a code change (for Steve, from the same report)
The sign-up confirmation email lands in Spam and its link points at dev.warrantycat.com. Sender-domain authentication (Resend: SPF, DKIM) and the app's base-URL setting have to be right on the deployment Ramesh will use.
