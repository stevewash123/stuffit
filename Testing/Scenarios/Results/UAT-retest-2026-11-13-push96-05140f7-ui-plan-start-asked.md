# UAT retest: Push 96, a plan added through "Add coverage" asks when it started

- **Build tested:** UI `05140f7`, Last-Modified **Fri, 13 Nov 2026 17:21:15 UTC (12:21 PM ET)**, newer than the 12:20 PM notes and confirmed before and after the run; API `bde7439`. Hard reload first, and no new-version banner.
- **Scope:** `CHANGES-push-96-plan-start-asked.md`, the fix for the Push 95 Medium.
- **Tester / account:** QA Controller, box browser, Alice ("P34-Alice Repairs"), about 12:29–12:32 PM ET on Nov 13 2026.
- **Test item:** "P96 UAT Item" (Walmart/Vizio fixture `push85/30-thermal-walmart-vizio-tv-protection.pdf`, Electronics), deleted afterwards. No new fixtures.

## Results

| # | Check | Result |
|---|---|---|
| 1 | Add coverage > Protection plan: start empty, "Say when the plan started." on save, nothing saved; with a start it saves | **Pass** |
| 2 | Switching back to another kind puts the purchase date back in Starts | **Pass** |
| 3 | Other kinds through Add coverage still default Starts to the purchase date and save | **Pass** (1 Low, below) |
| 4 | "Add protection plan" / "I'll type it in" unchanged | **Pass** |

**4 Pass, 0 Fail, 1 Low.** The Push 95 Medium is fixed.

### 1. Protection plan through Add coverage
- After picking Protection plan, "When did the plan start? (required)" had no option chosen (shot 01).
- With Allstate Protection Plans and Warranty extension set, Save plan gave **"Say when the plan started."** under the start question, and the panel stayed open (shot 02).
- Nothing was saved: Your coverage still said "No coverage confirmed yet.", Add-on protection had no entry, and there was no new to-do.
- With "Same day as the purchase" and Length 24, the save showed "Allstate Protection Plans plan added to your P96 UAT Item". The item then showed:
  - "Protection plan · Allstate Protection Plans — Aug 29, 2026 to Aug 28, 2028"
  - Add-on protection "started same day as the purchase … The end date was counted from the start, Aug 29, 2026, plus 24 months.", Active
  - The to-do "Add the rest of your Allstate Protection Plans plan" (shot 03)

### 2. Switching kinds
- The panel opened as Store warranty with Starts 2026-08-29, which cleared when Protection plan was picked.
- Switching back to Store warranty showed 2026-08-29 again, and so did Manufacturer warranty and Return window.

### 3. Other kinds still default and save
- A Store warranty with provider "Walmart", Starts 2026-08-29 (default) and Length 12 saved as "Store warranty — Aug 29, 2026 · No fixed end date" (shot 04).
- With Credit card benefit picked, Starts defaulted to 08/29/2026 (shot 05).

### 4. Other plan routes
- Add-on protection > Add > "I'll type it in" opened "Add protection plan" with no start option chosen (shot 06).
- An empty save showed "Choose the company that sold the plan, or type its name and add it." under Company and "Say when the plan started." under the start question, and nothing was saved (shot 07).

## Low (probably not from this push)
- **A store warranty with Length 12 and Ends empty saves with no end date.** The item says "No fixed end date", and on reopening, Length is 12 but Ends is empty. A plan's Length is counted into an end date ("plus 24 months"), but a store warranty's isn't. The saved line also doesn't show the provider name (Walmart). I haven't checked whether this predates Push 96.

## Cleanup
- "P96 UAT Item" was deleted with "Cancel the plan too" ("Ends the plan on Nov 13, 2026.").
- My Items "P96" shows "No items match." (shot 08).

Screenshots: `/workspace/uat/push96/shots/` (01–08).
