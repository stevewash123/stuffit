# UAT results: Claim guidance (refund wizard), build dc33d8a

- **Build:** commit `dc33d8a`, startedAt 2026-11-02T23:28:01Z (6:28 PM ET), Staging
- **Run:** Mon Nov 2, 2026, about 6:45 PM ET
- **Account:** Alice (Test1)
- **Type:** exploratory test against the release notes (there is no numbered scenario plan yet)
- **Guides loaded?** Yes. Real guidance appeared, with no "no guidance" text anywhere. A DB check also found 8 general guides in `claim_guides`, and both the Recoveries and ClaimGuidance migrations applied.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Refund link opens `/items/:id/refund` | Pass |
| 2 | Defective reason: questions, ranked routes, steps, checklist, warnings, "General guidance" label, no approval promise | Pass |
| 3 | "Changed my mind" reason changes the questions and the route statuses | Pass |
| 4 | Card benefit / extended plan routes | Not tested (none of Alice's items has a card or plan) |
| 5 | `/items/sample/refund` mock still loads | Pass |
| 6 | Wording and layout | 2 minor issues |

## Item used

"UAT Blender 2"

- Cuisinart, bought at Best Buy on Nov 1, 2026 for $89.99
- https://stuffit-ui.onrender.com/items/01a19878-cdaf-7d02-b0c0-e88cf2cee40f
- Coverage: a Best Buy return window ("14 days left", until Nov 16, 2026) and a Cuisinart manufacturer warranty (until Nov 1, 2027)

## Step 1: Pass

Both the "Refund" link and the "Start a refund or claim" button open `/items/01a19878-cdaf-7d02-b0c0-e88cf2cee40f/refund`.

## Step 2: Pass ("It does not work or it broke")

**Reason options**

| Option | Subtext |
|---|---|
| "I changed my mind" | "It works, I just do not want it." |
| "It does not work or it broke" | "A defect or a failure." |
| "It arrived damaged" | "Damage you did not cause." |
| "It is not what I expected" | "Wrong item, missing parts, not as described." |
| "I found it cheaper" | "A lower price after I bought it." |
| "I damaged it by accident" | "A drop, a spill, a crack." |
| "It was stolen or lost" | "I no longer have it." |

**Questions (Step 2 of 3, "A few quick questions")**

Intro: "We already know what you bought, where and when, so we only ask what changes the answer. Not sure is always fine."

Each question is answered Yes / No / Not sure. Both were answered Yes:

- "Has it only been used as intended, with no drops, spills or changes?"
- "Can you read the serial number on it?"

**Result**

Intro: "For **it does not work or it broke**. Here is what may apply to your UAT Blender 2, best option first."

1. **Return window · Best Buy**, marked "Best option" and "Applies"
   - Summary: "It fits your situation and closes soonest."
   - Detail: "The return window covers something that stopped working, and is open until Nov 16, 2026."
   - Days left: "14 days left (until Nov 16, 2026)"
   - Steps:
     1. "Find the store's return policy on its website or on your receipt, and check the return deadline."
     2. "Gather the item, its packaging, all its parts and accessories, and your receipt or order number."
     3. "Return it the way the store allows: in the store, by mail, or through its online returns page. Ask for a return receipt or confirmation."
     4. "Keep the confirmation, and check that the refund arrives."
   - Have ready:
     - "Your receipt or order confirmation" (You have it)
     - "The order number" (Not on file)
   - Warnings:
     - Shown in red: "Once the item is returned you no longer own it, so the maker's warranty and any card protection for it usually end too."
     - "Fees and limits. Some stores charge a restocking fee, or refund only as store credit, for certain items. Check before you go."
     - "Stores set their own rules, and the rules differ by item."
   - Label: "General guidance for a store return. We have not checked Best Buy's own page."
2. **Manufacturer warranty · Cuisinart**, marked "Applies"
   - Detail: "The maker's warranty covers something that stopped working, and is open until Nov 1, 2027."
   - Days left: "364 days left (until Nov 1, 2027)"
   - Steps:
     1. "Find the warranty terms in the manual, the box, or on the maker's support website."
     2. "Write down the model and serial number, and note when the problem started."
     3. "Contact the maker's support or warranty service and describe the problem."
     4. "Follow their instructions for a repair or replacement. Keep any case or reference number they give you."
   - Have ready:
     - "Your receipt, as proof of the purchase date" (You have it)
     - "The model and serial number" (Not on file)
     - "Photos or a short video of the problem" (Check you have it)
   - Warnings:
     - "Fees and limits. Some warranties ask you to pay for shipping, or cover parts but not labor. The warranty terms say which."
     - "Warranties usually cover defects, not damage from drops, spills, misuse or normal wear. Changing your mind is not covered."
   - Label: "General guidance for a maker's warranty claim. We have not checked Cuisinart's own page."

**Footer:** "StuffIt shows what companies have published and general guidance. The company decides every claim and return, its terms can change, and this is not legal advice. Nothing is sent for you, and no one can promise a request will be approved."

There is no approval promise and there are no store-specific steps.

## Step 3: Pass ("I changed my mind")

**Questions**

- "Is it unopened, or still like new?"
- "Do you still have the original box and packaging?"
- "Do you still have all the parts and accessories that came with it?"

These were left unanswered, so they count as not sure.

**Result**

- **Return window · Best Buy** changes to "Might apply": "The return window may cover changing your mind, but it depends on something you were not sure about: the item is unopened, or still like new." The "Best option" badge is gone.
- **Manufacturer warranty · Cuisinart** shows "Does not apply": "The maker's warranty does not cover changing your mind." It is dimmed and has no steps or checklist.

## Step 4: Not tested

UAT Laptop, UAT Guitar, UAT Fridge and UAT22 Alice Shoes have only a store return window. Alice has no item with a card benefit or an extended plan.

Next run: test this with Bob (who has cards) or with the FS-31 extended plan item.

## Step 5: Pass

`/items/sample/refund` loads with "Design mock with sample data. Nothing here is saved or sent." It shows "Step 1 of 3" and six options: the first five real-wizard reasons plus "Something else". The mock lacks "I damaged it by accident" and "It was stolen or lost". That's expected for an old mock and is noted only.

## Step 6: Wording and layout

- **Minor:** the result intro lowercases the reason inside bold, as in "For **i changed my mind**." The lone "i" should be "I", and "For it does not work or it broke" reads awkwardly.
- **Note:** the "Mark returned" and "Refund" controls sit side by side on the item page. Neither "Mark returned" nor "Mark refunded" was clicked, so the Money recovered feature is not covered by this run.
- There were no visible errors on the wizard pages. The known console error on `/login` is still there.

## Not covered in this run

- Money recovered (the item card, the Home "Recovered" total, `recoveries.csv`)
- The admin Feedback queue
- Retests of the date, bell, plans, feedback, tracking and receipt-line fixes

## Data left behind

None. The wizard saved nothing and nothing was edited.
