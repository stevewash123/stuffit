# Push 65: honest menus, a bell that says when it failed, safer loads (2026-11-11)

UI only. No API change, no migration. Stories S9.10.1, S9.10.2, S9.10.3, S9.10.9, S9.10.11 (from the design review).

| Change | What to check |
|---|---|
| **Returns in the menu is the real list** | Menu > Returns opens "Returns in progress". Typing /returns in the address bar lands there too |
| **Operator menu has no Review** | Admin menu: Companies, Shared data, Businesses, Feedback. The notice "Shared data ready to review" opens Companies |
| **The bell says when it could not load** | If the notification list fails, the bell shows "Could not load your notifications. Try again" instead of "You are all caught up" (hard to see on staging; low priority to test) |
| **"Start a claim"** | On an item whose return window is closed, the link at the bottom now reads "Start a claim" (was "Start a refund or claim") |
| **Sign-in return links** | A sign-in link that points off the app (for example with a backslash) lands on Home |
| **Moving between items** | Open an item, then another quickly: the second item is always the one shown |

## Not built yet (do not report)
- Joining requests to Money recovered, the claim wizard offer on a denial, the phone-insurance cost view, the three-layer explanation, a person adding their own plan type, receipt-to-plan-type matching, a seeded provider list.
