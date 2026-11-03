# Scenario 42: Policy note and source link, getting dismissed to-dos back, and the polish items (DRAFT)

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com), Ops (stevewash123.tester4@gmail.com) for one step
**Preconditions:** Both customer accounts exist (Scenario 25) and are clean. Reference data is loaded; New Balance and Best Buy have shared policies; at least one shared policy has a source address (New Balance's return policy has `https://www.newbalance.com/returns`). Test1 has an item **"UAT Todo Item"** (any store, today) with no to-dos.
**Time:** 40 min
**Built per:** S3.2.5 (policy source and confidence), S3.1.2 (suggest coverage), S4.6.2 (to-dos you can get back) and S9.1.8 (polish). **DRAFT:** the exact wording of the note, the link text and the section name is confirmed once the build is deployed; record what you see. NOT built, so not planned: an overdue to-do reminder, the "Is yours one of these?" card prompt, the over-limit insurance note.
**Why this plan:** these were found in every earlier round. The note keeps the app from sounding more certain than it is; the link lets a person check; to-dos must not vanish; small roughness adds up.

**Part A: policy note and source link**

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Add a purchase: New Balance, today, any shoe. Look at the suggested coverage in the form | The suggested return window shows the note **"usual window, can differ for your item"** (or the story's wording) because the policy is unconfirmed. It also shows a **Source** link |
| 2 | Test1 | Look at the Source link without following it (read its address) | An `https://` address on the store's own site (for example `https://www.newbalance.com/returns`). It opens in a new tab. Do not leave the StuffIt site |
| 3 | Test1 | Save the item and open it | Each coverage that came from a policy with a source shows a **Source** link on the item page; the note still shows on an unconfirmed policy |
| 4 | Test1 | Add a coverage by hand (Add coverage, your own terms) | It has **no** Source link and no invented note. A private policy with no address never shows a link |
| 5 | Test1 | Find a **confirmed** policy (one marked Confirmed) in the suggestions | The "can differ" note is **not** shown (or is softer); the Source link is shown. Record the wording |
| 6 | Test2 | Add the same purchase | Same note and link; nothing of Test1's data |

**Part B: Suggest coverage**

| # | Persona | Action | Expected |
|---|---|---|---|
| 7 | Test1 | On the item, in edit mode, click **Suggest coverage** | Either something is suggested (what and why), or the page says plainly that nothing new can be suggested. It does **not** do nothing and then grey out. If the button is gone, record that |

**Part C: to-dos you can get back**

| # | Persona | Action | Expected |
|---|---|---|---|
| 8 | Test1 | On **UAT Todo Item**, add three to-dos: "UAT done", "UAT dismiss", "UAT n/a" | Three open to-dos |
| 9 | Test1 | Mark "UAT done" as done, dismiss "UAT dismiss" (Dismiss for now), mark "UAT n/a" Not applicable | All three leave the open list |
| 10 | Test1 | Find the **Done and dismissed** section on the item's To do card (collapsed by default) and open it | Three rows, each with its status (Done, Dismissed, Not applicable) and an **Undo** or **Reopen** action |
| 11 | Test1 | Reopen "UAT dismiss" | It returns to the open list, and leaves the Done and dismissed section |
| 12 | Test1 | Open the To do page (`/todos`) | The same section is there (collapsed), listing the two that remain done or not applicable, and a Reopen on each; reopening one from here also works |
| 13 | Test2 | Open the To do page and the same item address | None of Test1's to-dos; the item is "Not found." |

**Part D: polish**

| # | Persona | Action | Expected |
|---|---|---|---|
| 14 | Test1 | Click the avatar in the header once | The account menu opens on the **first** click (it used to need two) |
| 15 | Test1 | In Add purchase, type "New Bal" in the store field and click away without choosing from the list | Either the store is selected (New Balance), or the form clearly says no store was selected. It does not silently keep unselected text |
| 16 | Test1 | On an item with a coverage, click **Stop covering** | It asks first (or offers Undo). Cancel keeps the coverage; confirming stops it |
| 17 | Test1 | Attach a small file to an item, then click its delete | It asks first (or offers Undo); Cancel keeps the file |
| 18 | Test1 | Open **Insurance**, add a policy, open the delete dialog | The dialog has **one** clearly labelled delete button (not two "Delete policy") |
| 19 | Test2 | Type `/settings/security` | Redirected away (to Home or Settings) without the text "You cannot do that." |
| 20 | Ops | Open `/settings/security` | The page opens normally |
| 21 | Test1 | Start a return on an item and read the note | "Return in progress since Nov 2, 2026." with no space before the full stop |
| 22 | Test1 | Insurance with one item linked | The sentence reads correctly for one: "1 item, which costs $…" |

Also record: any wording that makes a policy sound certain when it is unconfirmed, the exact text of the note, the Source link and the new section, and anything that took over 3 seconds. Skipped polish items from the build report are listed in the Results file; do not test those.
