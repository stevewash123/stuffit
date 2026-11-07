# What changed in push 34: business accounts, one login for personal and business, and the digest in-app fix (2026-11-06)

For GrokBot. API `d356106` and UI `0ce7781`. Check `/api/version` (`commit` must be `d356106`). Migration **`BusinessAccounts`** is applied to staging before this push. Every existing person becomes the **owner** of their own (personal) account; nothing changes for anyone who never joins a business. Stories S8.1.1 to S8.1.6. Also includes API `188faba` (digest fix, below).

## New: a business account (S8.1.1)
- **Sign-up** now asks **For myself / For my business**. A business gives its **business name** (held until the emailed link is opened). The Google sign-up button is hidden when "For my business" is chosen (Google always makes a personal account).
- **Settings > Profile:** a personal account can be **changed to a business** (owner, confirm, nothing lost; refused if others share the account). A business can be changed back to personal only while nobody else is on it and no invitation is waiting. The owner can **rename** it. The business name shows in the header.
- Everything else (items, purchases, plans, vehicles, reminders, claim guidance) works the same as a personal account. The export's `account.json` carries the business name and the people with roles.

## New: the owner invites employees (S8.1.2)
- **Settings > People:** only the **owner** invites, by email. The invitation email comes from the business, with a **single-use link that expires in 7 days**. The owner can **resend**, **revoke** and **remove** people; an employee can **Leave** (confirm). A daily invitation limit per account applies. The owner gets a notification when an invitation is accepted.
- **A brand-new address** opens the link, signs up, and gets the business membership **and an empty personal account**. **An existing login** opens the link, **signs in** (the signed-in email must equal the invited address), accepts, and the business is **added** to their memberships; their personal account stays.
- When someone leaves or is removed, the items stay with the business, "entered by" keeps their name, reminders for items they followed go to the owner; their business token stops working at once.

## New: one login, a personal account and a business (S8.1.6)
- After sign-in: **one membership goes straight in**. **Two or more:** a one-screen chooser at `/choose-account` (when none is remembered yet). The app remembers the **last account used**.
- The **header switcher** (shown only with two or more accounts) switches the session to the other account (the page reloads); it refuses an account you are not in (403). The switcher shows the other account's unread count.
- The accounts never mix: items, plans, documents, exports and settings are per account. **Roles are per account** (owner of your personal account and employee of a business at once). Preferences, time zone and digest stay per person; a notice names its account ("Acme Plumbing: ...") when you have more than one; the notification list and unread count are for the account in use.

## New: owner and employee (S8.1.3)
- **Employees** see all the business's items and can add, edit and delete items, purchases, receipts, coverages and documents, open claims, and set their own notification preferences. They see **names only** (no email addresses) in People, the members list and item people.
- **Owner only (an employee gets 403):** invite, resend, revoke, remove, rename, convert, ownership offer, plan page and billing portal, every export, delete the account.
- An item an **employee** enters is owned by the employee with the business owner as a follower; the item page shows **Entered by** in a business account.
- **Ownership transfer:** the owner offers it to an employee, who accepts from an emailed link while signed in; the old owner becomes an employee. No manager role.

## New: asset tag and location (S8.1.4)
- Business accounts only: **Asset tag** (40) and **Location** (80) on an item (add and item page). **Search** finds an item by either; My Items filters **Location** (places typed so far) and **Has no asset tag**. **Tags are unique per account** (case-insensitive); a duplicate is refused naming the item that holds it; a deleted item frees its tag. Both are in `items.csv` and shown on the item page and the list row. A personal account is refused any value and shows nothing.

## New: free year for a business (S8.1.5)
- A business is **free for a year** for **the owner plus two employees** (length and limit are configuration). The plan page shows "Free until <date>", then "Free year ended" (stays readable, nothing charged). Inviting beyond the limit (pending invitations count) is refused with "Your business account includes you and two employees."
- **Operator:** Admin > **Businesses** can extend the free year and raise the person limit (audited with who).
- Plans `business_small` (3 employees) and `business_unlimited` are named in configuration only. **Not priced or charged** (F8.2).

## Fixed (from your push 33 results)
| Where | What |
|---|---|
| **Replaced by the plan**: no plan choice (your Gate / 3 End / 3 Restart fails) | The plan question on the replacement now has **nothing ticked**: **Carry on / End / Restart from the replacement date** are all offered, and **Save stays disabled until one is chosen**. Before, "Carry on" came ticked, so Save went straight through and the plan auto-carried. The API already refused a replacement with an unanswered running plan (409 naming the plan). Retest each of the three answers with **different** dates: End must end the plan on the replacement date; Restart must start it on the replacement date |
| Replacement model/serial | The replacement item takes the brand, model, serial and date typed (tests assert it). The replace form **pre-fills the model from the old item** (the serial starts blank); that is a choice, not a bug. If the replacement page shows the old serial, tell us what you typed and where |

## Please check (not changed)
**"Yes, refunded" preselected on a manual plan (your 1a).** By the code, "Yes, refunded" is preselected only for a plan read from the item's receipt; a plan added on the item page has nothing preselected. Your fixture may have been created with `readFrom: receipt`. Please tell us **how P33-Plan-Ret-Refund was added** (which screen, or the API) and, if it was the item page's Add plan form, record what the Notifications/plan page says about where it was read from.

## Fixed: the digest in-app summary (from your push 31 results)
With the digest email switched **off** and its in-app channel **on**, the weekly (and daily) **in-app digest summary** is now created on the person's digest day and time (once per week or day), with no email, and the held notices are marked as not emailed (they remain individual in-app notices). With **both** channels off, nothing is made, as before. New weekly-type notices are still emailed at once while the weekly digest email is off.

## Steps to run
1. **Sign up as a business** (new address): business name; open the emailed link; the header shows the business name; Settings > People shows you as Owner.
2. **Convert** a personal account (Alice) to a business: it works, nothing lost; **change back** is refused while a person or an invitation is waiting.
3. **Invite a new address** (Settings > People): the email arrives; open the link in a private window; sign up; you join as Employee and also have a personal account. **Resend**, **revoke** (the old link stops working), single use (a second use is refused), expired link refused.
4. **Invite an address that already has a login** (Bob): open the link, **sign in** as Bob, accept; Bob now has two accounts: the **chooser** on next sign-in, then straight in to the last one; the **header switcher** swaps accounts; items do not mix; unread count per account.
5. **Roles:** as the employee, try People/invite, rename, plan page, billing, export, delete account: each is refused (403). Employee can add and edit items; the item shows **Entered by**; the owner is a follower of it and gets its reminders. Employee sees names, no emails.
6. **Remove / Leave:** remove an employee: their business token stops at once, they keep their login and personal account; items stay; **Leave** as an employee does the same.
7. **Asset tag and location:** add tags and locations; a duplicate tag is refused naming the item; search by tag and by location; the Location and "Has no asset tag" filters; items.csv has both; a personal account shows no such fields.
8. **Free year limit:** invite until the limit (owner plus two): the next invitation is refused with the message; the operator raises the limit in Admin > Businesses and the invitation then works.
9. **Ownership transfer:** the owner offers; the employee accepts from the email while signed in; roles swap.
10. **Digest:** Settings > Notifications: weekly digest **email off**, **in-app on**; held weekly notices; on the digest day (clock) run `run-digest`: one in-app "Weekly digest" and no email; a second run sends nothing. Reset the clock to offset 0 afterwards.
11. **Personal accounts are unchanged:** sign up "For myself", add an item: no business fields anywhere.

## Known gaps (not built; do not report as new)
- The owner is **not reminded before the free year ends** (the existing billing banners read the Stripe date, not this one).
- Business name is on **invitation emails only**; notification and digest emails have no business footer. **Digest lines** are not individually prefixed with the account name (the digest message is).
- **Switching reloads the whole app** instead of switching in place. Once an account is remembered, the chooser is reached only through the header switcher.
- Asset tags on plans (plans have none). No "assigned to"; no business-use flag; no manager role; seat pricing and invoices (F8.2).

## Not changed, do not report as new
Items listed under pushes 26 to 33 "Not changed".
