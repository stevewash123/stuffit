# Push 102: sharing really is on by default (fix for the Push 101 Medium), and the Terms link opens at the right section

API and UI, with a migration (`AccountSharingOnByDefault`). Push 101 passed 4 of 6; the Medium was real: the first migration created `accounts.share_with_community` with a database default of **false**, so 13 of 14 existing accounts were silently opted out, contradicting the Terms. Fixed:
- The column default is now **true**, and the app always sends the value it holds, so a false the person chose is saved as false.
- One-time: the migration turns every existing account **on** (the documented default). Accounts you had flipped off while testing Push 101 are on again; flip them again if the test needs them off. The migration has already been applied to the shared dev/Staging database, so the accounts are already on when you read this.
- The Low: "Read exactly what is shared" now opens the Terms at the "What is shared and what never is" section.
No change to the Terms wording, so no new terms version and no re-accept screen this time.

## What to check
1. **Existing accounts are on:** Settings > Privacy and data > "Sharing what you add": the box is **ticked** for Alice (personal and the business), Bob and Ops without touching anything. Read-only SQL: `accounts.share_with_community` is true for every row, and `column_default` is true.
2. **New account:** sign up a new account (any email): the box is ticked on first view, and the column is true for it.
3. **Untick and retick** still work and persist across a hard reload (Push 101 check 2).
4. **"Read exactly what is shared":** opens the Terms window already scrolled to "What is shared and what never is" (the heading is at the top of the visible text). The Terms opened from sign-up still open at the top.
5. Still untested from Push 101 if you can: Ops's re-accept screen; an employee's 403 on `PUT /api/privacy/sharing`; the Ops > Claims effect (an opted-out account is not counted for a new store or brand).
