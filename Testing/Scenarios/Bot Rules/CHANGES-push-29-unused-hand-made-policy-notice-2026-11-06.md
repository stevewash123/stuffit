# What changed in push 29: a notice for a hand-made policy that nothing uses (2026-11-06)

For GrokBot. API `6503be1` and UI `4b6f46d`. Check `/api/version` (`commit` must be `6503be1`); the UI proof is the two new buttons on the notification below. Migration **`UnusedPolicyNotice`** (adds `unused_notice_dismissed_at` to `manufacturer_policies` and `seller_policies`) is applied to staging before this push. No reference seed change. Story S3.2.13.

## New (S3.2.13)
The reminder sweep (the hourly `run-reminders` job, the same one that sends reminders) now also looks for **policies a person made by hand** that no item uses, and sends **one** notification per policy: "Your own <maker> warranty (<n> months) is not used by any item. Delete it?" with **Delete it** and **Keep it**.
- **Which policies:** account-owned maker and store policies whose only evidence is "typed in by hand" (Manual / UserTyped). A policy a document, receipt or any other source also backs is **never** reported.
- **Not used = no item** (not deleted, purchase not deleted) has a coverage from it or one that matches it: for a maker policy the same maker (or its parent company), same category (or a parent), same term in months; for a store policy a return coverage from that store with the same number of days. Vehicles and their parts always count as using it.
- **Not before 7 days** old (simulated clock honoured).
- **Once only:** any earlier notice for that policy, even one deleted from the list, blocks another. **Keep it** stores the answer on the policy: never again. **Delete it** retires the policy (ends it yesterday, or at its start date if later).
- A waiting notice is **cancelled** by the next sweep if the policy is used again, retired, answered or gone.
- It goes to one person: whoever entered the policy if still on the account, else the earliest member. The kind is "Info needed" (the settings text for it mentions this notice).
- The notice's "See it" link opens the store or brand page where the policy is shown.

## Steps to run
1. Test1: type a maker warranty by hand on an ordinary item with a brand and category (12 months). It becomes Test1's own policy for that maker (push 28).
2. Delete that item (or replace its warranty by applying a document). Nothing else of Test1's uses the policy.
3. Run the reminder sweep now: **nothing** (younger than 7 days).
4. Advance the clock 8 days (offset), run the sweep: one new notification "Your own <maker> warranty (12 months) is not used by any item. Delete it?" with Delete it / Keep it.
5. Run the sweep again: no second notice. Press **Keep it**: it finishes; advance and sweep again: never again for that policy.
6. Repeat steps 1-4 with a second policy and press **Delete it**: the policy is retired (no longer offered on a new item from that maker).
7. Repeat 1-4 but, before the sweep, add another item from the same maker, category and 12-month term: the policy is in use, no notice (and a notice already waiting is cancelled at the next sweep).
8. Test2 does not see or get Test1's notice; Test2 cannot answer Test1's notice.
Reset the clock to offset 0 afterwards.

## Known, not a bug
A restricted maker policy (model list, purchase window, product-tree place) is judged by maker, category and term only, so it leans towards "in use" and may not be reported.

## Not changed, do not report as new
Items listed under pushes 26 to 28 "Not changed".
