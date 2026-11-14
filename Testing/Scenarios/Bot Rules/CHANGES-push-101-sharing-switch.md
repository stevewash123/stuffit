# Push 101: a sharing switch in Settings (S6.1.6, the on/off part)

API and UI together, with a migration (`AccountSharing`, adds `share_with_community`, default on). Terms version moves from 2026-11-13 to **2026-11-13.2** (API and UI), so **every existing account is asked to accept again once** (Alice, Bob, Ops and the rest). That screen is part of what to test.

## What it does
- **Settings > Privacy and data > "Sharing what you add"** (the first card). One checkbox, "Share the policy facts from what I add", ticked by default. The text under it says what is and is not shared, with a "Read exactly what is shared" link that opens the Terms in the reader window.
- **Turning it off** applies from then on: nothing more the account adds is offered to the shared data (the warranty-terms offer, the store/brand/issuer/card claims, and the alias note all check it). It also **takes back what an operator has not yet checked**: the account's pending candidate policies and its place in claims that are still open. What was already checked and added to the shared data stays, and says nothing about who added it. A message says all this after the change.
- **In a business account** the switch is the owner's call: an employee does not see the card, and the server refuses them (403).
- **Wording:** the Terms' "Your choice" paragraph now says you can turn sharing off in Settings (and to email us to stop using something already shared); the Privacy Policy, the sign-up box and the "terms updated" screen say the same.

## What to check
1. **Existing account (Alice):** sign in; "Our terms have been updated" appears, with "what changed" saying you can turn sharing off in Settings. Read the Terms in the window ("Your choice" paragraph), press I agree, and carry on.
2. **Settings > Privacy and data:** the "Sharing what you add" card is first. The box is ticked. Untick it: the message "Sharing is off. Nothing more of what you add will be shared, and anything we had not yet checked has been taken back." Reload the page: still unticked. Tick it again: "Sharing is on."
3. **"Read exactly what is shared"** opens the Terms window on the "What is shared and what never is" section.
4. **Business account:** the owner sees and can use the card; an employee (e.g. Bob in a business Alice owns) does not see it.
5. **Effect (optional, needs a store or brand not in the shared list):** with sharing off, add a new private store/brand name; the operator's claims list (Ops > Claims) should not count this account for it. With sharing on, it does.
6. **New account:** sign-up box says "you can turn sharing off at any time in Settings"; a new account has the box ticked in Settings.
