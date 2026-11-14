# Push 95: the coverage drawer is its own component (S9.10.10, step 7)

UI only (API unchanged at bde7439). Push 94 (the "Edit item" drawer) passed. This is the biggest of the drawers: the one that opens for "Check this coverage" (a suggestion), "Edit coverage" and "Add coverage" / "Add protection plan" is now `ItemCoverageDrawerComponent`, with the coverage form's types (`CoverageDraft`, `PlanDetails`) moving with it. Nothing should look or behave differently. The production build was checked locally before this push.

## What to check (item page, regression)
1. Suggested coverage > Change it: the drawer is titled "Check this coverage", shows the kind (and provider), the notes in orange, Starts / Ends / Length, the lifetime tickbox, the transfer question, "Proof the warranty asks for" ticks, Terms, Claims page and Claims phone. Save changes works and ties the coverage to the suggestion.
2. Edit on a saved coverage: "Edit coverage", same fields prefilled. Ticking "This is a lifetime warranty" removes Ends and Length and asks "Whose lifetime". Un-ticking shows them again.
3. Add coverage (new): "What kind of coverage" (Store warranty / Protection plan / Manufacturer warranty / Return window / Credit card benefit) and the provider picker (or "Which benefit" for a card).
4. Add protection plan: choosing "Protection plan" shows Company (required), What it is (required), Plan name, Price, Paid, Starts (with the start-basis choice), Ends, Length (with the "end date counted from the start" note), Waiting period, Contract number, "More details" (service fee, claim phone, claim website), "Covers <item>"; the button reads "Save plan" and the field errors (company, start, end, claim website) appear under their fields.
5. On a vehicle: "Certified or dealer-added" and the odometer reading; miles limit and "unlimited miles" appear only where allowed; "prorated stage" only on a part.
6. Save is disabled with no start date (except a new plan), or while saving; a failed save shows the red message; layout unchanged.
