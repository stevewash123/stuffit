# Scenario 55: "Lifetime" with no end date, and who it belongs to

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Reader on. Clock offset 0 (2026-11-04). Item from Scenario 53 step 17 is not required; this scenario adds its own.
**Time:** 40 min
**Built per:** S3.1.8 (lifetime scope, transferability, "Lifetime, can end"), S3.1.9 (proof of purchase asked for), S2.4.1. **Built in push 16 (2026-11-05): lifetime and proof asked, ending with a reason, export, claim guidance.** NOT built, mark **Not built** (not Fail): the yearly check-in (step 8), given away or sold (steps 10 and 11: there is no such flow; "Mark disposed" is thrown out, not given away), the list of what WarrantyCat holds that could serve as proof (part of step 5), and a lifetime on one component (step 12). A step that shows a missing screen for anything else is a Fail. A step that shows a guessed number of years, or a permanent "Lifetime" green with no way to end it, is a **Fail** whether built or not.
**Why this plan:** "lifetime" is the word most likely to be turned into a number or a promise. The app must show what it really is: no end date, whose lifetime, whether it can be passed on, and that it can still end.

Documents: `Testing/SampleData/warranties/standard-lifetime-limited-reel.pdf` (Penn Battle III 4000, BTLIII4000: "for the lifetime of the product", original purchaser, not transferable, proof of purchase required, not saltwater corrosion from failing to rinse, not lost or stolen) and `multi-item-kitchen-suite-warranty.pdf` (dishwasher stainless tub "lifetime against rust-through", scope and transfer **not stated**).

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Add "UAT Penn Reel", brand Penn, model BTLIII4000, bought 2026-06-01, $119. Upload `standard-lifetime-limited-reel.pdf` | Model matches. Terms read with quotes: lifetime; original purchaser; not transferable; proof of purchase required |
| 2 | Test1 | Read the suggestion | Term is **Lifetime** with **no end date**: not 0, not a guessed number of years, not 99. Whose lifetime: **the product** (the document says "lifetime of the product"). Transfer: **not transferable (original purchaser only)** |
| 3 | Test1 | Accept and open the item page | Plain words, for example "Lifetime of the product. Original purchaser only. Not transferable. The maker decides when it has worn out." Shown as **"Lifetime, can end"**, not a permanent green tick. The list of what could end it is on the page |
| 4 | Test1 | Check what the item says it excludes | Saltwater corrosion from not rinsing, and lost or stolen reels, appear as exclusions (not left out, not turned into a term) |
| 5 | Test1 | Check proof of purchase | "Asks for: proof of purchase." It does **not** say the original paper is required. (The list of what WarrantyCat holds that could serve as proof is **Not built**) |
| 6 | Test1 | Look at the shared Penn warranty (12 months from `penn.json`) for this item | The item does not carry **two contradictory** warranties unexplained. Record how the document's lifetime term sits beside the shared 12-month brand policy (replaces it, or both shown with sources). Either is acceptable if clear |
| 7 | Test1 | Move the clock 30 years forward (T1) and open Home and the item | No expiry reminder fires for a coverage with no end date. Record that Home does not show it as "ending soon" |
| 8 | Test1 | **Not built.** Move the clock one year forward | A yearly check-in "still covered? still have the receipt?" is offered. Answering "still have the receipt: no" keeps the coverage but records the answer; answering "no longer covered" ends it with a reason. Instead, check **End this coverage** on the item page offers reasons |
| 9 | Test1 | Item page: **End this coverage**, reason **the maker dropped the model** | Coverage shows **expired** with the reason and the date; it keeps its history; the last covered day is the day before the date you chose. **Re-open** brings it back as a running lifetime with no end date and no reminder |
| 10 | Test1 | **Not built.** Add a second reel "UAT Penn Reel 2" the same way. Mark it **given away** (or sold) | Because the lifetime coverage is not transferable it says it **ends with the owner**, and asks before ending it. The other coverages on the item follow their own rules |
| 11 | Test1 | **Not built.** Add a third copy and mark it **sold**, then **undo** within the session | The coverage returns to the before state |
| 12 | Test1 | Add "UAT Dishwasher HS-D24" (Hearthstone, bought 2026-03-03) and upload `multi-item-kitchen-suite-warranty.pdf` to it (the whole suite is tested in Scenario 56; only the tub matters here) | The stainless tub's "lifetime against rust-through" is read as a lifetime term on the tub only (not the dishwasher, which is 1 year). Scope and transfer are **"not stated"**, not guessed to match the reel. **Not built:** a lifetime on one component; expect the tub line to stay as text or be missing. Record what you see; do not call a guessed number of years anything but a Fail |
| 13 | Test1 | Correct the tub line by hand: set whose lifetime to "original purchaser" and transfer to "not transferable" | Saved; the item page text updates and says "You entered or corrected: whose lifetime, transfer" (it does not claim the document said so) |
| 14 | Test1 | Check for any arithmetic on lifetime | No yearly cost, no "years remaining", no end-date reminder for lifetime lines |
| 15 | Test1 | Check a lifetime coverage in the claim flow ("Something broke") | The claim guidance shows the lifetime term, the exclusions and the proof asked for; it does not promise acceptance. Record any wording that promises a repair |
| 16 | Test1 | Export the claim log or the items (F5.3) | The lifetime coverage is exported as "Lifetime" with scope and transfer, not as a blank or a number |
| 17 | Test2 | Open Test1's reel by address | Not found |

Also record: any end date or years-remaining figure on a lifetime line, any place "Lifetime" is shown as permanent, and any claim of transferability the document does not make.
