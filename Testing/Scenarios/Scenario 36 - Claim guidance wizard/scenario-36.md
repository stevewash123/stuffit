# Scenario 36: Ask what to do about a broken or unwanted item (claim guidance wizard)

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25). The 8 general claim guides are loaded on the site (the staging bot confirms with a count of the `claim_guides` table). Test1 has:
- an item **"UAT Blender"**: Best Buy, brand Cuisinart, category Small appliances, price 89.99, bought today. It has a store return window and a maker warranty (add it by hand and tick both suggested coverages)
- a credit card **"UAT Card"** that has confirmed benefits (the Chase Sapphire Preferred from the catalog) and an item **"UAT Card Item"** paid with it, so a card benefit coverage exists
- an item **"UAT Plan Item"** covered by an extended warranty plan (add a plan on its item page, as in Scenario 31)
**Time:** 35 min
**Built per:** S5.4.12, S5.4.13, S5.4.14 and S9.2.6, first slice. NOT built, so not planned: store-specific guides (every route says "General guidance"), saving an attempt, the prepared message, transit-aware deadlines, free-text intake and chat.
**Why this plan:** this is the answer to "something broke, what do I do". It must rank the routes honestly, say when it is unsure, never promise an outcome, and never show another account's item.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open **UAT Blender** | A **Refund** link in the header and a panel with **Start a refund or claim**. Both are present for an item that is still owned |
| 2 | Test1 | Click **Refund** | Opens `/items/<id>/refund`. "Step 1 of 3". Seven reasons, each with a short line under it: "I changed my mind", "It does not work or it broke", "It arrived damaged", "It is not what I expected", "I found it cheaper", "I damaged it by accident", "It was stolen or lost". Next is not possible until one is chosen |
| 3 | Test1 | Choose **It does not work or it broke** and continue | "Step 2 of 3", "A few quick questions". The intro says we already know what you bought, where and when. Each question has Yes, No and Not sure. Record the questions. The serial-number question appears only if no serial is saved |
| 4 | Test1 | Answer Yes to every question and continue | "Step 3 of 3". Intro reads "You said It does not work or it broke. Here is what may apply to your UAT Blender, best option first." (the reason in the person's own capitals) |
| 5 | Test1 | Read the first route | **Return window · Best Buy**, marked **Best option** and **Applies**, with "N days left (until <date>)", numbered steps, and a "have ready" list. "Your receipt or order confirmation" says what we know (You have it / Not on file). A red warning says returning the item usually ends the maker's warranty and card protection. The label says "General guidance for a store return. We have not checked Best Buy's own page." |
| 6 | Test1 | Read the second route | **Manufacturer warranty · Cuisinart**, **Applies**, days left to its end, steps, a have-ready list ("The model and serial number" Not on file, "Photos or a short video of the problem" Check you have it), and "General guidance for a maker's warranty claim" |
| 7 | Test1 | Tick off two steps; reload the page | Ticks are for this visit (note whether they are kept after reload). Record it |
| 8 | Test1 | Read the bottom of the result | The standing note: StuffIt shows what companies have published and general guidance; the company decides every claim; terms can change; not legal advice; nothing is sent for you; no one can promise approval. No sentence anywhere says a claim "will" be approved or refunded |
| 9 | Test1 | Go back to step 1. Choose **I changed my mind**. Leave the questions unanswered and continue | Questions about unopened/like new, original box, all parts. The result: Best Buy return is **Might apply** (it depends on something you were not sure about) and has no "Best option" badge. The **maker's warranty is "Does not apply"**, dimmed, with no steps, saying the warranty does not cover changing your mind |
| 10 | Test1 | Answer the "unopened" question **No** and look again | The store route still shows, with its conditions as a note or "Might apply" (stores vary). Record exactly what it says |
| 11 | Test1 | Choose **I found it cheaper** | A price-protection style route appears only if a coverage supports it; otherwise the page says nothing applies and offers the nearest options clearly labelled as requests, not rights. Record which |
| 12 | Test1 | Open **UAT Card Item**, start a refund, reason **It does not work or it broke** | A **card benefit** route appears (for example the card's purchase protection or extended warranty) with its own days left, steps and "General guidance" label. The route order puts the one closing soonest first. Record each route and its verdict |
| 13 | Test1 | Open **UAT Plan Item**, start a refund, reason **It does not work or it broke** | An **extended plan** route appears with the plan provider and dates. Record its verdict and steps |
| 14 | Test1 | On an item whose coverage has all ended (use one from Scenario 24 after the clock moved past its window, or set a past end date by hand), start a refund | Routes that have ended say **Does not apply** (with why) or are absent; nothing says the window is open. If nothing applies, the page says so and offers the nearest options labelled as requests |
| 15 | Test1 | Mark **UAT Blender** returned (Mark returned, any refund) and open the item | The **Refund** link and the panel are gone for a returned item |
| 16 | Test1 | Type `/items/<UAT Blender id>/refund` in the address bar | A plain message that a returned item cannot start a refund; no error page, no stack trace |
| 17 | Test2 | Open `/items/<Test1's item id>/refund` | "Not found." Nothing of Test1's item is shown |
| 18 | Test1 | Open `/items/sample/refund` | The old design mock still loads: "Design mock with sample data. Nothing here is saved or sent." |
| 19 | Test1 | Sign out and open `/items/<id>/refund` | Redirected to sign in |

Also record: any wording that sounds like legal advice or a promise, any route that names a store's own steps (there should be none: all guidance is general), the order of routes each time, and anything that took over 3 seconds.
