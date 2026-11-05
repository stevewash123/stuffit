# What changed in push 19: the lifetime offer on Add a purchase (2026-11-05)

For GrokBot. API only; check `/api/version` and record it. No migration.

## Fixed
- **Add a purchase never offered a lifetime warranty.** With the purchase not yet saved, a document with a lifetime and no length was described as "does not give one clear warranty length", so no "Manufacturer's warranty found" box appeared. It now appears as "Lifetime, with no end date", counted from the purchase date.

## Retest
1. **Add a purchase**, attach `standard-lifetime-limited-reel.pdf`. Expect the box **Manufacturer's warranty found** with "PENN Fishing Tackle: Lifetime, with no end date, counted from the purchase date", ticked.
2. Save. The item should carry the lifetime coverage (the same as the item-paperwork door): Lifetime, can end; no end date; whose lifetime; proof asked. Record anything different from that door.
3. A document that gives neither a length nor a lifetime must still say it gives no clear length and offer nothing.

## Known, not in this push (do not report as new)
- `edge-registration-required.pdf` (a short term that becomes three years if you register): the reader finds no single length, so no coverage is offered. A term that depends on registering is a separate piece of work (Scenario 54 Part B shape), not part of the lifetime build.
- Not built: yearly check-in, given away or sold, the list of what WarrantyCat holds as proof, a lifetime on one component.
- Items list and Home show "Active" for an item with only a lifetime coverage.
