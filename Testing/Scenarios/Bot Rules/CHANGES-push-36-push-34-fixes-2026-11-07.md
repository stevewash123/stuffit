# What changed in push 36: fixes from the Push 34 UAT (2026-11-07)

For GrokBot. Check `/api/version` against the pushed API commit. No migration.

## Fixed
- **B2 step 7:** "Change back to a personal account" is disabled while anyone else is on the business or an invitation is waiting.
- **Employee sees Download everything / Delete my account:** both sections are hidden from an employee in a business (the owner and personal accounts still see them).
- **B12 link back:** a replacement's page now shows "Replacement for <old item>" as a link to the old item (`replaces` on the item).
- **B13:** cancelling or ending a plan finishes its "Add the rest of your plan" to-do.
- **Admin Businesses:** "1 person" instead of "1 people".

## Not changed (please re-read)
- **'Van 1' search returns Van 2:** search matches every word separately ("Van" and "1" anywhere in the item, here "AT-010"). That is by design; use the Location filter for an exact place.
- **B5 chooser not shown:** accepting an invitation counts as "last used account", so sign-in goes straight in; the chooser shows only when no account is remembered. By design in S8.1.6; say if you want it different.
- **Notice names account / Switch account link:** done in push 35 (API `c103d4a`), after the build you tested.
- **B13 identical replacement name:** the name is what the person typed; not changed.
- Inconclusive items (Google button, switcher reload, admin audit line) need a human look.
