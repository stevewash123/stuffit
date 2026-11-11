# Push 66: a record of how stores and brands are matched (2026-11-11)

API only. **One migration** (`MatchDecisions`: a new table, nothing else changes). Story S2.8.1.

Nothing a person sees should change. Every store and brand match made while reading a receipt, a warranty paper or an email now also leaves a row saying which rule decided and how sure it was. The same names must bind to the same stores and brands as before.

| Change | What to check |
|---|---|
| **No visible change** | Upload a receipt, add a purchase with a document, accept a New Item: the store, brand and coverage proposed are what they were before this push. Anything different is a bug |
| **Operator summary** | As an administrator, `GET /api/admin/match-decisions/summary?days=30` (needs the admin sign-in) returns counts per field (store, brand), rule and band. After a few receipts it shows rows such as store / exact / high |
| **A failure to log never fails a receipt** | Not testable by hand; covered by a test |

## Not built yet (do not report)
- Joining requests to Money recovered, the claim wizard offer on a denial, the phone-insurance cost view, the three-layer explanation, a person adding their own plan type, receipt-to-plan-type matching, a seeded provider list.
