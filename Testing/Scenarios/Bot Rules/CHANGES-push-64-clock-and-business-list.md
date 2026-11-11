# Push 64: the app clock everywhere, and a business's whole list (2026-11-11)

API and UI. No migration.

| Change | What to check |
|---|---|
| **The page follows the app clock without a reload** | Every API answer now carries the app clock (`X-App-Now`). After the test clock is moved, an open item page counts days from the new day: the day after a return window's last day the card says the window ended (no "Ends today"), the return path is hidden and "Ask for a courtesy return anyway" is offered (S72-9). Move the clock and just navigate, no reload |
| **Add-purchase date check uses the app clock** | At +120 days, a purchase dated a few days before the app date is accepted; "not in the future" is judged against the app date, not the browser's (S70-7) |
| **A business's My Items lists everyone's items by default** | On a business account an employee sees every item of the shop, not only those they follow. "Show everyone's items" is ticked by default; unticking it shows only their own. Personal accounts are unchanged (S71-5b) |

## Not changed
- Business sign-up still creates only the business. The earlier notes promise an empty personal account only to people who are invited.
- The halfway lease mileage notice is an ordinary notification set to email and in-app; the code sends its email like the three-month one. If it did not arrive, please check that notification's email status in Neon.

## Not built yet (do not report)
- Joining requests to Money recovered, the claim wizard offer on a denial, the phone-insurance cost view, the three-layer explanation, a person adding their own plan type, receipt-to-plan-type matching, a seeded provider list.
