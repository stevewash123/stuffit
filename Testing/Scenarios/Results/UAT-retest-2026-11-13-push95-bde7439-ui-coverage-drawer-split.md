# UAT retest: Push 95, the coverage drawer is its own component

- **Build tested:** API `bde7439`; UI Last-Modified **Fri, 13 Nov 2026 16:43:12 UTC (11:43 AM ET)**, confirmed before, during and after the run.
  - In round 1 the tab was on an older bundle: a new-version banner showed at about 12:02 PM ET. Everything that differed was re-run on the current build after a reload, and in round 2 (12:06–12:09 PM ET) after a hard reload.
- **Scope:** `CHANGES-push-95-coverage-drawer-split.md` (S9.10.10 step 7, regression only). No new scenarios and no NEXT-REPORT-ADDITIONS.md.
- **Tester / accounts:** QA Controller, box browser, 11:59 AM–12:10 PM ET Nov 13 2026. Alice ("P34-Alice Repairs") and Bob (Personal). Save states were read from the real disabled property.
- **Test items:** "P95 UAT Item" and "P95b UAT Item" (Walmart/Vizio fixture `push85/30-thermal-walmart-vizio-tv-protection.pdf`, Electronics). Both were deleted, with "Cancel the plan too". Vehicle checks used existing items and saved nothing. No new fixtures.

## Results

| # | Check | Result |
|---|---|---|
| 1 | Suggested coverage > Change it: "Check this coverage" drawer, fields, save ties it to the suggestion | **Pass** (button reads "Save coverage") |
| 2 | Edit coverage: prefilled; lifetime hides Ends/Length and asks "Whose lifetime"; un-tick restores | **Pass** |
| 3 | Add coverage: kinds, provider picker, "Which benefit" for a card | **Pass** |
| 4 | Protection plan: fields, "Save plan", field errors under their fields | **Fail** via Edit > Add coverage > Protection plan; **Pass** via Add-on protection > Add > "I'll type it in" |
| 5 | Vehicle: certified/odometer, miles only where allowed, prorated stage only on a part | **Pass** |
| 6 | Save disabled with no start (not for a new plan); failed save red message; layout | **Pass** (layout Info below) |

**5 Pass, 1 Fail, 4 Info.**

### Fail (Medium): a plan saves with no start date when added through "Add coverage"
**Path:** item page > Edit > Add coverage > kind "Protection plan". The drawer title stays "Add coverage". Steps and results, on the current build after a hard reload:
- **Save plan with every field empty:** the only error is under Company: "Choose the company that sold the plan, or type its name and add it." There's no error at the start question.
- **Company "Allstate Protection Plans" and "Warranty extension", start unanswered, then Save plan:** it saves with no error (shots 13, 14). The item then shows:
  - "Protection plan · Allstate Protection Plans … Aug 29, 2026 · No fixed end date · Warranty extension".
  - Under Add-on protection, "Allstate Protection Plans · Warranty extension · Active · Aug 29, 2026, no fixed end".
  - A new to-do: "Add the rest of your Allstate Protection Plans plan".

The same form opened from Add-on protection > Add > "I'll type it in" (title "Add protection plan") does show "Say when the plan started." under the start choice and won't save (shot 09). The notes list the start as required with its own error, so the two paths disagree.

I couldn't compare this path against the pre-split build, so it may be older than Push 95. The round-1 tab, which was on the older bundle, behaved the same (shot 08).

### 1. Check this coverage
- **Walmart return window (Electronics) suggestion** (shot 01):
  - Title "Check this coverage", "Return window · Walmart", orange note "Counted from the purchase date."
  - Starts 2026-08-29; Ends 2026-09-28 ("Leave empty if there is no fixed end."); Length.
  - Terms "Most consumer electronics 30 days. Marketplace computers, tablets and cameras are shorter (about 14 days)."; Claims page and Claims phone.
- **Vizio manufacturer warranty suggestion** (the return window has no lifetime, transfer or proof fields):
  - Orange note "Different category: this is Vizio's policy for tvs; this item is electronics. Check that it applies."
  - Lifetime tickbox, and "Can it be passed on to a new owner" (The document does not say / Yes / No, original purchaser only / Once, or for a fee).
  - Proof ticks: Proof of purchase / The original receipt / Registration / The serial number or a photo of it / A dealer stamp.
- **Save state:** `disabled` true with Starts cleared, false once it was restored.
- **Saving:** the drawer closed, and "Return window · Walmart ELECTRONICS, Ended Sep 28, 2026" moved to "Your coverage". The other Walmart window suggestions were dropped (shot 02).
- **Note:** the button reads "Save coverage"; the notes say "Save changes", which is what the Edit drawer uses.

### 2. Edit coverage
- The title is "Edit coverage", the fields are prefilled, and the button reads "Save changes" (shot 03).
- On the Vizio warranty, ticking lifetime hid Ends and Length and showed "Whose lifetime": The document does not say / The life of the product / The life of the product line (ends when the maker stops making the model) / The life of the original purchaser.
- Un-ticking it brought Ends and Length back (shot 04).

### 3. Add coverage
- The kinds are Store warranty / Protection plan (warranty extension, accident cover, insurance) / Manufacturer warranty / Return window / Credit card benefit.
- Store warranty shows "Who provides it" ("Start typing a name").
- Credit card benefit shows "Which benefit" instead: Card extended warranty / Purchase protection / Return protection / Price protection (shot 05).

### 4. Protection plan (fields)
Everything listed in the notes is there:
- The note "Only company, what it is and start are needed."
- Company (required); What it is (required): Warranty extension / Accident cover / Insurance; Plan name; Price; Paid (one payment / a month / a year).
- "When did the plan start? (required)": Same day as the purchase / On delivery / Another date.
- Ends, and Length with "Counted from the start when you leave Ends empty…"; once Length is filled, "The end date will be counted from the start, Aug 29, 2026, plus 24 months."
- Waiting period; Contract number; "More details" (Service fee per call, Claim phone, Claim website); "Covers P95 UAT Item".

The button reads "Save plan", and `disabled` is false with no start, as the notes expect for a new plan.

From "I'll type it in":
- **Empty save:** errors under Company and the start question. There's no error under Ends, which is optional.
- **Claim website "not a url":** "Enter the claim website as a full address, starting with https://." This shows only once company and start are valid.
- **Good plan:** Allstate, Warranty extension, same day, 24 months. It saved as "Aug 29, 2026 to Aug 28, 2028 · started same day as the purchase" (shot 11).

### 5. Vehicles
- **Alice's "P38b One Mile", Add coverage:**
  - "Certified or dealer-added" and, once ticked, "Odometer when it started (the reading at certification)" appear for Store warranty, Manufacturer warranty, Return window and Credit card benefit.
  - "Mile limit (optional)" and "The document says unlimited miles" appear for the same four kinds, but not for Protection plan (shot 12).
- **Bob's "UAT P38 S64 Certified RAV4 Car", Edit on "Store warranty · UAT CertifiedCare":** "Edit coverage", with the certified tickbox ticked, Odometer 28400 ("Its miles count from this reading. A factory coverage counts from zero."), Mile limit 12000, and unlimited miles unticked. No prorated stage (shot 15).
- **Bob's part "UAT P38 S65 Mercury Outboard" (on the Tracker Bass Boat), Edit on "Manufacturer warranty · Mercury":** shows "This is the prorated stage: after the free stage you pay a share" as a tickbox, plus miles. No certified group (shot 16).
- Both were closed without saving.

### 6. Save state, errors and layout
- Save `disabled` behaves as expected (check 1, and check 4 for a new plan).
- **Failed save:** a plan price of -50 gives the red message "One or more validation errors occurred." (shot 10).
- The drawer's own field layout and order look normal.

## Info
- **Info:** the drawer title stays "Add protection plan" (or "Add coverage") when you switch the kind; the title doesn't follow the chosen kind.
- **Info:** the "Check this coverage" button reads "Save coverage", not "Save changes" as the notes say. It's probably unchanged; please confirm.
- **Info (as Pushes 93/94):** a negative price shows the generic text "One or more validation errors occurred."
- **Info (as Push 91):** the header's WarrantyCat logo runs into the account label.

## Cleanup
- **Items:** both P95 items were deleted, and the plans were cancelled with them. My Items "P95" shows "No items match." for both Alice and Bob.
- **Vehicles:** nothing was saved on any vehicle or part.

Screenshots: `/workspace/uat/push95/shots/` (01–16).
