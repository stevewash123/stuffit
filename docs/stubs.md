# What is stubbed or placeholder (checked 2026-10-01; bell, Notification Center and notification settings are real as of M4)

Every stub points to the story that replaces it. If you add a stub, add a row here and a Status note on that story.

| Stub | Where | What it does today | Replaced by |
|---|---|---|---|
| Card terms finder | `StubCardPolicyFinder` (`ICardPolicyFinder`) | Waits 3 s, returns canned terms for names containing custom cash, venture, savor, quicksilver, freedom, prime; nothing otherwise. Quotes say "STUB RESULT". No web or LLM | S6.1.3 (flow and UI are real: S3.3.4) |
| Email sender | `LoggingEmailSender` (`IEmailSender`) | Writes the email to the API log. Verification and password-reset emails are not delivered | S7.6.4 |
| File storage | `LocalFileStore` (`IFileStore`) | Files on local disk | S7.6.3 |
| Operator creation | `--make-operator`, `--create-user ... --operator` command line | Grants administrator with no two-step sign-in and no audit entry | S7.1.5 |
| Plan and billing tab | UI placeholder route | Same | S1.2.4 |
| Theme selector | `data-theme="teal"` fixed in `index.html` | One preselected theme; all colors are tokens | S9.8.2 |

## Real, not stubbed (so no replacement needed)
- Changing a card's number: `POST /api/payment-methods/{id}/last4` with `replaceCurrent` (S3.3.5)
- Card catalog and picker (S3.3.6); the seeded card names are real data but not verified against issuers (S3.2.4)
- Seeded policies: 12 cards with an issuer source URL each. Three rows (Amex Platinum, Citi Double Cash, Citi Strata Premier) still need a one-time check against the page (S3.2.4, `docs/card-policy-worklist.md`)

## Known gaps that are not stubs
- Last 4 is required by the add-card form but not by the API (S3.3.1)
- Tests added 2026-10-01 for the card catalog, number change, card-terms search (API: `CardApiTests.cs`; UI: `cards.page.spec.ts`, `card-detail.page.spec.ts`, `party-picker.spec.ts`)
