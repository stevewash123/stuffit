# Scenario 28: Administrator sign-in with two-step, and the shared data screens

**Accounts:** Ops = stevewash123.tester4@gmail.com (administrator), Bob = stevewash123.tester2@gmail.com (an ordinary account, to prove he is refused)
**Preconditions:** Ops exists and has been made an administrator by the operator's command-line task (`--make-operator`); the bot cannot do that. Bob exists (Scenario 25). If Ops has already set up two-step sign-in, skip steps 1 to 3 and use the setup key already in `RUN-CONFIG.md` to compute the codes.
**Time:** 25 min
**Why this plan:** two-step sign-in is required for administrators, and no admin screen opens until it is on. The shared data screen is the one place an operator sees every shared store, brand and issuer. Labels below are quoted from the app's code; where the code does not make a message certain, the plan says to record the exact text.

Bot rules and the report format: `Bot Rules\README.md` and `Bot Rules\_template.md`. The setup key goes in `RUN-CONFIG.md`, never in the report.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Ops | Sign in with the email and password only (no code is asked yet) | Signed in, and sent to Settings > Security (`/settings/security`) because two-step sign-in is not set up yet. The page is headed "Two-step sign-in" and says "Administrator accounts need two-step sign-in before any admin screen opens." |
| 2 | Ops | Press "Set up two-step sign-in" | A QR code (alt text "QR code to add WarrantyBank to your authenticator app") and a line "Or type this key" with the setup key. A 6-digit code field is shown. Put the key in `RUN-CONFIG.md`, not in the report |
| 3 | Ops | Compute the current 6-digit code from the key (or read it from the authenticator), type it in "6-digit code" and press "Turn on". If the page shows recovery codes ("Two-step sign-in is on. Save these recovery codes now."), save them in `RUN-CONFIG.md`, tick "I have saved my recovery codes" and press "Done" | Enrolment is confirmed: the page shows "Two-step sign-in is on." and an "Administrators" list that includes Ops with the badge "Two-step on". The admin screens now open. If the first code is refused, record the exact message, wait for the next code and try again |
| 4 | Ops | Open "Admin view" if the page is not already in the admin navigation | The admin navigation shows Review, Companies, Shared data, Feedback, and an "Admin" badge. A "Customer view" button switches to the customer screens |
| 5 | Ops | Sign out. Sign in again with the email and password only | The sign-in page asks for a code: a field labelled "Authenticator code" with the hint "The 6 digits from your authenticator app, or one of your recovery codes." Record the message shown above it (label from code: "Enter your authenticator code.") |
| 6 | Ops | Enter a wrong code (for example `000000`) and submit | Refused with a clear message; not signed in. Record the exact text (label from code: "That code is not correct.") |
| 7 | Ops | Enter the right current code and submit | Signed in, and lands on the admin dashboard at `/admin`, headed "Shared data" (administrators land on `/admin` unless they chose the customer view). Record the address shown |
| 8 | Ops | Choose "Customer view", then go to the app's home address `/` | Customer Home opens (the customer view was chosen). Switch back with "Admin view". Record what you saw |
| 9 | Ops | On the "Shared data" page, check what it lists: the heading under "Shared data" (label from code: "Shared stores, brands and issuers"), the "Search" box, and the "Show" filter. Search for a store you know is shared (for example "Home Depot") and a brand (for example "Milwaukee") | A list of shared stores, brands and issuers. It shows shared entries only; nothing that belongs to a single account (Alice's or Bob's own private entries) is listed. Record the number of rows and whether each shared entry shows its verified or unverified state |
| 10 | Ops | Open one entry from the list | Its detail page opens (`/admin/parties/<id>`) with the shared policies and their sources. Record what it shows |
| 11 | Ops | Open Companies, Review and Feedback in turn | Companies opens. Review and Feedback are placeholder pages for now (label from code: titles "Review" and "Feedback and issues"); record what each shows |
| 12 | Bob | In a second browser context, sign in as Bob (an ordinary account) and look at the navigation and the account menu | No Admin badge, no "Admin view" button, no Security tab in Settings |
| 13 | Bob | Type each address directly: `/admin`, `/admin/companies`, `/admin/review`, `/admin/feedback`, `/settings/security` | Each one is refused or sends Bob back to Home (`/`). No admin data is shown. Record where each address ended up |
| 14 | Bob | If the tester can call the API with Bob's signed-in token: `GET /api/admin/parties` | Refused (record the status code). No shared admin data is returned |

## Claims by API (optional)

There is **no claims screen**: operators use the API. Do these steps only if the tester can call the API with the signed-in token (Ops, after step 7). Do not look for a screen for them. See "Scenarios 18 to 21" in the Full Scenarios `README.md` and Scenario 18 for how claims work.

| # | Persona | Action | Expected |
|---|---|---|---|
| 15 | Ops | `GET /api/admin/claims` | The list of claims (each with the number of accounts that reported it and whether it is ready). Add `?readyOnly=true` to list only the ready ones. Record how many there are |
| 16 | Ops | `POST /api/admin/claims/evaluate` | Recounts and returns the claims that are ready |
| 17 | Ops | Note that `POST /api/admin/claims/approve` and `POST /api/admin/claims/reject` exist but need a recent second-factor check. Do not approve or reject anything in this plan unless the operator has asked for it | Nothing is changed. If you do call one without a recent check, record the exact refusal |
| 18 | Bob | If the tester can call the API with Bob's token: `GET /api/admin/claims` | Refused (record the status code); no claims are returned |

## Report back (copy this table, fill every row)
| # | Pass/Fail | What you saw (exact text) | Evidence (URL/screenshot) |
|---|---|---|---|

Also list anything odd you noticed that no step asked about (layout, wording, slow loads, console errors), clearly separated from the step results.
