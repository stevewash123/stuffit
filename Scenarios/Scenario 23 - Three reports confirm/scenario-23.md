# Scenario 23: Three independent matching reports confirm a policy

**Status:** DEFERRED (see S6.1.4): three matching reports do not confirm on their own; an administrator is pinged at 3 (built, hourly) and the claim is approved by the operator, or automatically at 20 (auto-approve not built).

**Accounts:** Alice, Bob, Carol, Ops
**Preconditions:** All signed up; Ops is administrator with two-step sign-in set up. Use a store or maker with no existing policy: most seeded stores already have one, so a fixture store with none is created through the database (listed in the report, removed afterward); makers (brands) with no warranty policy also work, with a warranty term in place of "30 days". Skip the Ops steps (7 and 8) until an administrator is available to the bot.
**Time:** 25 min

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Alice | Submit a return policy for the store: 30 days, quote the exact sentence and give a source link, share box checked | Status: unverified |
| 2 | Alice | Submit the identical policy again | Not counted as a second independent report |
| 3 | Bob | Submit the same policy (30 days) with his own quote | Still unverified (2 independent) |
| 4 | Carol | Submit a DIFFERENT value (e.g. 45 days) | Does not count toward the 30-day match; status stays unverified |
| 5 | Carol | Replace with the matching 30 days | Third independent match: now confirmed (or queued for confirmation, per product rule) |
| 6 | Alice | View the store policy | Shows the confirmed value with its source |
| 7 | Ops | Sign in (two-step), open the review queue | The submissions are listed with who/when/source; actions are audited |
| 8 | Ops | Reject one submission | Policy state updates; the rejection appears in the audit trail |
| 9 | Alice | Check for any credit/contribution tally | Credits only for confirmed contributions (if the feature exists; otherwise note "not built") |
| 10 | Bob | Try to open an admin URL directly | Refused; no admin data shown |
