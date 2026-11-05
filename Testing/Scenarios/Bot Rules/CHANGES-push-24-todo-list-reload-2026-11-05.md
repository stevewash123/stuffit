# What changed in push 24: the item's to-do list updates at once; a correction to the push 22 notes (2026-11-05)

For GrokBot. UI only (`bd82dda`); API stays at `1ed55e3` from push 23. Check `/api/version` (`commit` must be `1ed55e3`) and record the UI build time. No migration. This answers your push 22 retest. Push 23 (Vehicles and Private sale, Scenario 61) is also out: run it too.

## Fixed
- **Step 16b, the Register to-do appeared only after a browser reload.** The To do card on the item page now loads again whenever the page reloads, so after you tick the optional coverage and press **Add** (or press **I registered**) the to-do shows, or is marked done, at once.

## A correction to my push 22 notes (not a defect)
My notes said Read it would not offer the base coverage again. It does: when the item already has a manufacturer's warranty, the choice screen lists both rows, the base row **unticked** with the line "This item already has a manufacturer's warranty. Adding this one again replaces it." That is the design. Expect exactly that. If you tick only the optional coverage and press Add, you get two coverages and nothing is replaced. Please also try ticking the base row too and report whether the base is replaced (not doubled).

## Retest
1. Scenario 54 **step 16b** again: Add a purchase with `edge-registration-required.pdf`, accept the base only, Edit > Receipts and files > Read it, close the facts panel, tick the optional coverage, **Add**. Expect two coverages and the Register to-do on the same page with no reload. Then read it again and tick the optional coverage a second time: expect "This item already has that optional coverage." and no third coverage.
2. Then run **Scenario 61** (push 23), Parts A to F.

## Still unchecked
- The 15-second Undo toast (Scenario 54 step 18): say how long it stays if you can catch it.
