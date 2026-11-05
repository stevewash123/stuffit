# What changed in push 17: Manage membership after Back, and how to reach the lifetime fields (2026-11-05)

For GrokBot. UI only; check `/api/version` and the UI build time. No migration.

## Fixed
- **Manage membership stuck on "Opening..." after the browser Back button (Scenario 59 step 4).** Coming back from Stripe with Back now clears it: the button reads Manage membership and is on, no reload needed.

## Scenario 55: use the right door
Your Scenario 55 run attached the Penn reel PDF through **Add-on protection > I have the paperwork**. That door reads **plan** paperwork and makes a protection plan (which is why you saw "PENN Fishing Tackle plan", Cancel it now, and a blank export). The new lifetime fields, the "Lifetime, can end" label, **End this coverage** with its reasons, and the claim and export wording belong to the **maker's warranty coverage on the item**. Reach them like this:
1. **Add a purchase** page: attach the PDF with the purchase. A box "Manufacturer's warranty found" should appear before you save. Accept it. Or
2. On the **item page**, upload the PDF as paperwork for the item (not as a Receipt, not through Add-on protection) and accept the warranty it offers.
If neither door ever offers a manufacturer's warranty for `standard-lifetime-limited-reel.pdf`, that is a real finding: record which door, what the document was classed as, and what the page said.
Then redo Scenario 55 steps 2, 3, 5, 9, 13, 15 and 16 on that coverage.

## Decided, do not report
- The license end date reads Nov 4 in the app and Nov 5 in Stripe for a sign-up made late in the evening Eastern: the app shows the local date, Stripe shows UTC.
- A Stripe portal address opened in another window stays usable until Stripe expires it; that is Stripe's own rule.
