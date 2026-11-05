# What changed in push 18: the reader now finds the lifetime term (2026-11-05)

For GrokBot. API only; check `/api/version` and record it. No migration.

## Fixed
- **A lifetime warranty document was read but its lifetime was thrown away.** For `standard-lifetime-limited-reel.pdf` the reader answered "lifetime: true", and the code only understood "yes", so the document ended with "The document does not give one clear length or end date. Add the coverage yourself." and no "Manufacturer's warranty found" offer. True and false are now understood everywhere the reader answers yes or no.

## Redo (the same list as push 17, on the right door)
Scenario 55 steps 2, 3, 5, 9, 13, 15 and 16, reaching the coverage through **Add a purchase** (attach the PDF; a "Manufacturer's warranty found" box should now appear before you save) or by uploading the PDF as paperwork on the item page. Not through Add-on protection. Delete the leftover Penn item on Alice first.

What you should now see: Lifetime with no end date, the product's lifetime, not transferable, proof of purchase asked (and not the original paper), a **Lifetime, can end** label on the item page, **End this coverage** with reasons, and the lifetime columns filled in the export.

## Also try, since the same fix touches other yes/no answers
- A normal warranty document that says "registration required" or "transferable": the notes the app shows about registration and passing it on should now appear (they were silently dropped when the reader answered true or false). Record anything that looks wrong.

## Decided, do not report
- Items list and Home still show "Active" for an item with only a lifetime coverage; the label is on the item page.
- Not built: yearly check-in, given away or sold, the list of what WarrantyCat holds as proof, a lifetime on one component.
