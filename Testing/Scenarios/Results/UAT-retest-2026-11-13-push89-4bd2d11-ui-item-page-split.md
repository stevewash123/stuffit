# UAT retest: Push 89 (4bd2d11), item page split (Suggested coverage + People components)

- **Build tested:** API `bde7439` (/api/version, startedAt 2026-11-13 03:58 UTC); UI Last-Modified **Fri, 13 Nov 2026 11:57:52 UTC (6:57 AM ET)**, bundle `main-J6ITP7WQ.js`. This is Push 89 (`4bd2d11`), which **replaces Push 88 (`f4dc531`, never deployed**; production build failed, site stayed on the Push 87 build until 6:57 AM ET).
- **Scope:** `CHANGES-push-89-fix-build-and-people-split.md` (covers the Push 88 checks too). Regression only: nothing should look or behave differently. NEXT-REPORT-ADDITIONS.md: none.
- **Tester / account:** QA Controller in the box browser, Alice ("P34-Alice Repairs"). Run 7:00–7:05 AM ET, Nov 13 2026.
- **Test items:** "P88 UAT Vizio TV" (Walmart/Vizio fixture `push85/30-thermal-walmart-vizio-tv-protection.pdf`, TVs) and "P88 UAT Hammer Drill" (`push75/homedepot-receipt-01.pdf`, Power tools), saved on `/add/new` with all coverage unticked. All deleted afterwards (named "P88" because the run started before the relabel). No new fixtures.

## Results

| # | Check | Result |
|---|---|---|
| 1 | Suggested coverage list looks/behaves as in Push 83/87 (ticks, certainty words + word tooltips, badges, dates, Source links, notes) | **Pass** |
| 2 | Change it / Doesn't apply / Not sure yet, and "Verify the above N policies apply" | **Pass** |
| 3 | People card (Owner, "(you)", Make owner, Add a person, Remove) | **Pass** |
| 4 | Layout and spacing of both blocks | **Pass** |

**3 behaviour checks + layout: 4 Pass, 0 Fail.**

### 1. Suggested coverage list
**Hammer Drill (Home Depot / Milwaukee):** heading "Suggested coverage", "Tick what applies.", 7 lines.
- Ticked by default: Return window · Home Depot (no badge), Aug 15–Nov 13 2026, "Home Depot return policy · checked Sep 29, 2026 · Confirmed", notes "General policy; none for this category." / "Counted from the purchase date.", Source link. Tooltip "Policy checked: very sure. Fit for this purchase: very sure: A store's usual window can differ for an item".
- Ticked by default: Manufacturer warranty · Milwaukee [POWER TOOLS], Aug 15 2026–Aug 15 2031, Confirmed, Source link. Tooltip "Policy checked: very sure. Fit for this purchase: very sure".
- Unticked: five alternative Milwaukee product-line warranties (165' Laser Detector, 8 Gallon Dust Extractor, AIRSNAKE accessories, Drain Cleaning Cables, Job Site Radios), Likely, each with "Not ticked: we could not tell if this is …" and a matching "fairly sure: We could not tell…" tooltip.
- Same two Confirmed policies as the Push 84 quick add / Add Details result.

**Vizio TV (Walmart):** 3 lines, all unticked, same as Push 78/83/87:
- Return window · Walmart [ELECTRONICS] Aug 29–Sep 28 2026, Confirmed: **ended, not ticked**.
- Return window · Walmart general Aug 29–Nov 27 2026, Likely, "Tick it instead if that is what your item is."
- Manufacturer warranty · Vizio [TVS] Aug 29 2026–Aug 29 2027, Unconfirmed, placeholder notes, no Source link. Tooltip "Policy checked: not sure. Fit for this purchase: very sure".

No tooltip contains "%". Shots `01-B-suggested-default.png`, `02-B-certainty-hover.png`, `05-A-suggested-fullwidth.png`.

### 2. Buttons and Verify
- Two ticked: "Verify the above 2 policies apply" (enabled). None ticked: "Verify the above policies apply", disabled. One ticked: "Verify the above policy applies" (singular wording, same as Push 78).
- Verify with only the Milwaukee 5-year warranty ticked added exactly that one policy ("Try this first"). The five alternative Milwaukee lines left the list with it; the Home Depot window stayed. Same alternate-group behaviour as Push 78.
- Change it (Vizio) opened the "Check this coverage" drawer prefilled (Manufacturer warranty · Vizio, 2026-08-29 to 2027-08-29, 12 months, transfer "The document does not say", placeholder terms). Closed without saving.
- Doesn't apply on the Walmart electronics window: list went 3 → 1 (the general Walmart alternate window went with it, same grouping). Not sure yet on Vizio: 1 → 0, block disappears, Your coverage "No coverage confirmed yet."
- Shots `03-B-all-unticked-verify-disabled.png`, `04-B-after-verify-one.png`, `06-A-change-it-drawer.png`, `07-A-after-doesnt-apply-not-sure.png`.

### 3. People card
On a fresh Hammer Drill item: lists "QA Test 1" marked Owner "(you)". Add button disabled until someone is picked; picked QA Test 2, Add added them; the picker then hid (nobody left to add). QA Test 2's row shows "Make owner" and "Remove"; "Make owner" only on the non-owner row. Remove took them off immediately, picker returned with Add disabled. "Take me off" is not shown for the owner, so it was not exercised (only one non-owner member and Alice is owner). Shots `p89-people-default.png`, `p89-people-after-add.png`, `p89-people-after-remove.png`.

### 4. Layout
Suggested coverage block spans the main column (955 px inside 1024 px) with normal spacing; People card normal. No squashing or overlap.

## Notes (unchanged from earlier builds, not new)
- **Info (known Low, Push 78/87):** on the item page the ended Walmart electronics window's checkbox is not disabled and shows no "ended" note, so it can be ticked by hand (Add form refuses it).
- **Info (known Low, Push 78):** acting on one line of an alternate group (Verify or Doesn't apply) also removes its alternates, so after a wrong pick the other alternative can't be chosen.
- **Info:** "Take me off" not covered: needs a non-owner signed-in member (e.g. sign in as QA Test 2) in a future run if wanted.

## Cleanup
"P88 UAT Vizio TV" and both "P88 UAT Hammer Drill" items deleted in the app; My Items search for "P88" returns nothing. No plans attached.

Screenshots: `/workspace/uat/push89/shots/`.
