# Scenarios

Whole purchases to run through the app by hand: documents in the order to use them, and an answer key for what the app should show. Each folder has a `scenario-N.md` (the answer key, steps and expected coverage) and every file it needs (`.eml`, `.pdf`, and a `.jpg` twin of each PDF; scenario 14 also has the images that come with its email).

All scenarios use the **test client** (`stevewash123.test@gmail.com`, with My Items and New Items empty) and its **Chase Freedom Unlimited** card (ending 1111), except where a scenario changes that. Scenario 1 is the happy path; each of 2 to 14 changes one thing about it. Emails are sent to the test mailbox with `Testing\TestEmails\send_scenario.py N` (it asks for the Gmail app password; `--list` shows what each scenario sends), then run Check Emails.

| # | Folder | Store / item | What is different from the happy path |
|---|---|---|---|
| 1 | Scenario 1 | Home Depot / Milwaukee hammer drill | Nothing: the happy path |
| 2 | Scenario 2 - No order email | Lowe's / DeWalt circular saw | No order confirmation email; the receipt creates the item |
| 3 | Scenario 3 - Store not in shared data | Quillfeather Mercantile / Makita circular saw | The store is not in the shared data (no return policy) |
| 4 | Scenario 4 - Brand not in shared data | Target / Hexaquill screwdriver set | The brand is not in the shared data (no manufacturer policy) |
| 5 | Scenario 5 - Store policy unverified | Kohl's / KitchenAid stand mixer | The store is shared, but its return policy is unverified |
| 6 | Scenario 6 - Brand policy unverified | Best Buy / Sony headphones | The brand is shared, but its warranty policy is unverified |
| 7 | Scenario 7 - No warranty document | Walmart / Black+Decker hedge trimmer | No warranty document; the warranty comes from shared data |
| 8 | Scenario 8 - Store protection plan | Best Buy / LG OLED TV + Geek Squad plan | A store protection plan on the receipt, with its own document |
| 9 | Scenario 9 - Card not on the account | Walmart / Garmin Forerunner 265 | Paid with VISA 7777, which is not one of the test client's cards |
| 10 | Scenario 10 - Online order, no receipt | Amazon / Dyson V15 | Online order: order, shipping and delivery emails, no receipt |
| 11 | Scenario 11 - Warranty for a different model | Lowe's / Black+Decker drill/driver | The warranty document is for another model; the right move is to reject it |
| 12 | Scenario 12 - Receipt PDF attached to the email | Home Depot / DeWalt drill/driver kit | The receipt is a PDF attached to the email; the email body has no order details |
| 13 | Scenario 13 - Warranty attached to the order email | Walmart / Makita impact driver | The manufacturer's warranty PDF is attached to the order email (it is sorted as a warranty, not read as a receipt) |
| 14 | Scenario 14 - Marketing images attached to the email | Walmart / DeWalt combo kit | A logo, a promo banner and an app-store badge come with the email; none is a document, so none is kept |
| 15 | Scenario 15 - Maker line - heated gear | Home Depot / Milwaukee M12 heated jacket | Own account. Same store and maker as 16 and 17; the item falls under Milwaukee's Heated gear warranty line (12 months) |
| 16 | Scenario 16 - Maker line - digital levels | Home Depot / Milwaukee 48 in. digital level | Own account. Milwaukee's Digital levels line (36 months) |
| 17 | Scenario 17 - Maker line - portable generators | Home Depot / Milwaukee portable generator | Own account. Milwaukee's Portable generators line (24 months) |

| 18 | Scenario 18 - Three accounts, same unverified data | Quillfeather Mercantile, Hexaquill, Sony | Four accounts and an operator: three accounts report the same store, brand and warranty; an operator verifies them; a fourth account sees them shared. `python scripts/run_scenarios.py 18` |
| 19 | Scenario 19 - Shared retailer Gabes Hardware | Gabe's Hardware / Makita impact driver | A regional store not in the shared data, reported by three people and verified with its return policy; what changes for them; then a longer name offered as an alias. `python scripts/run_shared.py 19` |
| 20 | Scenario 20 - Shared manufacturer Hexaquill | Target / Hexaquill screwdriver set (files of scenario 4) | A brand and its warranty reported by three people (each with their own private brand), verified brand first and then warranty; what changes for them and for a fourth person. `python scripts/run_shared.py 20` |
| 21 | Scenario 21 - Shared credit card | Home Depot / Makita reciprocating saw, paid with Gabe's Rewards Visa | A card, its issuer and an extended-warranty benefit reported by three people, verified in order; what changes for them and for a fourth person who picks the card from the list. `python scripts/run_shared.py 21` |
| 22 | Scenario 22 - Shared policy vs private purchase | n/a (browser plan) | DRAFT. Two people buy from the same store: both see the same shared policy, each keeps a private coverage, and an unverified submission is never shown as official |
| 23 | Scenario 23 - Three reports confirm | n/a (browser plan) | DEFERRED (S6.1.4). Three people report the same policy; the count alone does not confirm it, and an administrator reviews and rejects a submission |
| 24 | Scenario 24 - Time travel and reminders | n/a (browser plan) | DRAFT. The simulated clock moves forward so a return window ends and the reminder email and notification arrive once |
| 25 | Scenario 25 - Account lifecycle and email | n/a (browser plan) | Two real accounts: sign-up, email confirmation, sign-in, password reset, and a reset requested twice in ten minutes |
| 26 | Scenario 26 - Purchases, items and privacy | n/a (browser plan) | Purchases added by hand, suggested coverage, receipt upload (Upload waits while the document is read), search and filter, and one account never seeing another's items |
| 27 | Scenario 27 - Cards, notifications and export | n/a (browser plan) | Credit cards, notification and email settings, data export, and account deletion |
| 28 | Scenario 28 - Administrator sign-in and shared data | n/a (browser plan) | An administrator enrols two-step sign-in, signs in with a code, and uses the Shared data page; an ordinary account is refused; claims are checked by API only |

| 29 | Scenario 29 - Returns in progress | n/a (browser plan) | Start a return, cancel one, group the working list by store, mark returned with a partial refund, undo with "I have it again"; another account never sees it |
| 30 | Scenario 30 - Insurance policy and items | n/a (browser plan) | A renter's policy with limits, items left out or linked, the over-limit note and the item-page Insurance card; the arithmetic is checked by hand |
| 31 | Scenario 31 - Extended warranty plan | n/a (browser plan) | A third-party plan covering several items, yearly cost arithmetic, files, ending the plan switches it off on every item |
| 32 | Scenario 32 - Reminders and to-dos | n/a (browser plan) | To-dos added on an item, shown on the To do page, done, dismissed, not applicable; never shown to another account |

| 33 | Scenario 33 - What is worth tracking | n/a (browser plan) | The "What to track" setting, its shortcuts and limits, New Items following it, kept per person |
| 34 | Scenario 34 - Color theme | n/a (browser plan) | Three themes and Light / Dark / Match my device, kept on the device, no flash on load |
| 35 | Scenario 35 - Send feedback | n/a (browser plan) | The feedback form, what will be sent, Your messages, the 5-per-hour limit, privacy between accounts |
| 36 | Scenario 36 - Claim guidance wizard | n/a (browser plan) | The Refund wizard: reasons, questions, ranked routes (store return, maker warranty, card benefit, extended plan), general-guidance labels, no promise of approval, privacy |
| 37 | Scenario 37 - Money recovered | n/a (browser plan) | Mark refunded and card payouts, Home total with cash apart from credit, no double count with Mark returned, export file, privacy |
| 38 | Scenario 38 - Admin feedback queue | n/a (browser plan) | The administrator reads every account's feedback, filters, sets status; customers see the status; non-administrators refused |
| 39 | Scenario 39 - Daily digest | n/a (browser plan) | Choosing the digest holds emails, one digest a day, no repeats, urgent notices bypass it, bursts collapse; uses the simulated clock and run-digest |
| 40 | Scenario 40 - Retest of the UAT fixes | n/a (browser plan) | Dates on the item page, bell badge, notification title, ended plan, export download, PDF receipts, feedback overflow, receipt lines past the cap, sign-up leak, console errors |

Scenarios 22 to 40 are browser plans for the test bot (Grok). The bot rules and the report format are in `Bot Rules\README.md` and `Bot Rules\_template.md`. The accounts are Alice stevewash123.test@gmail.com, Bob stevewash123.tester2@gmail.com, Carol stevewash123.tester3@gmail.com and Ops stevewash123.tester4@gmail.com (administrator).

The shared-data facts (which stores, brands and policies are verified) were read from the development database on 2026-10-24. If that data is re-seeded, re-check the "in shared data / verified" rows before relying on a scenario.

Scenarios 15 to 17 (made by `scripts/make_maker_scenarios.py`) each run on their own new account; `python scripts/run_scenarios.py 15 16 17` prints `CHECK PASS` or `CHECK FAIL` against the answer key. Last result: `last-run-maker-lines.txt`.

## Scenarios 18 to 21: shared data being verified

Each needs several accounts and an **operator**, so each has a runner that plays every person on new accounts and prints `PASS` or `FAIL` per check: `python scripts/run_scenarios.py 18` and `python scripts/run_shared.py 19 20 21`. Documents for 19 and 21 are made by `make_shared_scenarios.py`; scenario 20 reuses the files of scenario 4. Last results: `last-run-claims.txt` (18) and `last-run-shared.txt` (19 to 21).

The operator steps are **API calls**; there is no claims screen yet. The runner makes its own operator account (two-step sign-in set up through the API, and the operator flag set with the scratchpad `q.js`). By hand, sign in as an operator with two-step sign-in and call, with that token:

- `GET /api/admin/claims` lists the claims (`?readyOnly=true` for the ready ones); `POST /api/admin/claims/evaluate` recounts and returns the ready ones.
- `POST /api/admin/claims/approve` with `{ "id": "<claim id>" }`, plus what fits the claim: `sourceUrl` (a warranty or a card benefit: the page the operator read), `effectiveFrom` (a new version of a verified one), `name` (the shared name, if the spelling needs correcting), `returnPolicy` (a store: `days`, `fromDelivery`, `conditions`, `restockingFeePercent`, and the required `sourceUrl`).
- `POST /api/admin/claims/reject` with `{ "id": "<claim id>", "note": "<why>" }`.

Clean up after a run: the throwaway accounts (`scenarios+...@example.test`) and the shared entries the run made stay in the development database. In `tools` (run `npm install` there once; the scripts read the connection string from the API's user-secrets):

- `node cleanup18.js` after scenario 18: removes its accounts, the shared Quillfeather and Hexaquill entries and their claims, and puts the Sony warranty back as it was.
- `node cleanup_shared.js` after 19, 20 or 21 (run it between them, since they share names): removes the accounts and the shared Gabe's Hardware, Gabe's Credit Union and Hexaquill entries, with their policies, evidence and claims.
- `node q.js "<sql>"` runs one statement (the runners use it to make their operator account).
