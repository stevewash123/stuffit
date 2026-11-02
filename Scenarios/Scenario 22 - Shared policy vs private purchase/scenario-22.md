# Scenario 22: Shared policy data is visible to all; purchases stay private

**Status:** DRAFT.

**Accounts:** Alice, Bob
**Preconditions:** UAT database seeded with reference data (`--seed`). Both users signed up. Pick a seeded store/maker with a known return window (e.g. New Balance, Pflueger).
**Time:** 15 min

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Alice | Add a purchase from a seeded store with a recent date | Suggested coverage appears from the shared policy, with the "usual window, can differ for your item" note |
| 2 | Bob | Add a purchase from the same store | Same suggested policy and window, computed from Bob's own date |
| 3 | Both | Compare the policy text/source link shown | Same policy, source link opens the store's page |
| 4 | Alice | Change the return end date on her coverage only | Her coverage changes |
| 5 | Bob | Reopen his item | Bob's coverage unchanged (coverage is a personal snapshot) |
| 6 | Alice | Look for a way to see other users' purchases or counts of them | None exists; nothing identifies Bob |
| 7 | Alice | Submit a new policy for a store with the "share" box checked | Accepted as "unverified" |
| 8 | Bob | Browse the same store's policies | The unverified submission is labelled unverified (or not shown as confirmed); never shown as official |
