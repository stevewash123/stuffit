# Retest notes for the next build (written 2026-11-03, after UAT of 982952c)

For GrokBot. Read with the plan for each area. Record the commit from `/api/version` in the report.

## Fixed, please retest
| Area | What to check | Plan |
|---|---|---|
| Full Add keeps receipt plans | Upload `21-letter-bestbuy-email-marketing-geek-squad.pdf`; Add Details lists the Geek Squad plan with a tick (ticked) and a stated warranty with a tick (unticked); a full Add attaches the ticked ones. Quick add still holds back low confidence | FS-41 steps 2 to 4, 10, 11, 17 |
| Stated-only item | `17-thermal-unknown-store-generator-single.pdf`: quick add now creates the item without the warranty (no validation error); ticking the warranty on Add Details creates a 'Stated on receipt' coverage | FS-41-11 |
| Empty Save | Save with nothing ticked shows 'Tick at least one policy' (in the page banner, red style is expected) | FS-41-4 |
| Quick-add note | 'Not added by a quick add: we are not sure enough it applies. Tick it on Add Details to keep it.' has text after the colon | FS-41-10 |
| PDF and ZIP reads | Export download works; a PDF receipt opens with View. If either still gives HTTP 500, quote the response and tell Steve; do not retry more than twice | FS-27-13, FS-37-19, FS-40-7, FS-40-8 |
| Wizard | Answers survive a reload; courtesy ask does not say the window 'has passed' on an item with no window | FS-36-7, FS-36-12, FS-36-14 |
| Usual-window note | Shown on a general or not-Verified policy and on the saved item; NOT shown on a Confirmed policy | FS-42-3, FS-42-5 |
| Bell and Notifications | The bell count and the Notifications page agree on the card notice | FS-27-1, FS-32 |
| To-do reminder | The email and bell entry name the item | FS-32-12 |
| Home Recovered card | Visible when every item is returned and something was recorded | FS-37-17 |
| Upload note | 'N lines past the limit for one receipt were put under Smaller things' matches the list | FS-40-12 |
| Profile time zone | Shows the stored zone, not 'Not set (UTC)' | FS-39 |
| Store field | Typing a partial store name shows '"X" is not selected yet' with add as new | FS-42-15 |
| Shared data filter | Reads 'Brands (makers)' | FS-28-9 |

## Still known, do not report as new
No 'Is yours one of these?' card prompt; no over-limit insurance note; no days-left badge on return rows; the order total can show as the price on the headphones and dishwasher rows (S2.4.15, later); to-do reminder unsubscribe category is 'Info needed' (left as is).

## Decided by Steve, do not report
- A plan is still valid on its last day: 'Ends today' and still covered on the item is correct. No special wording or reminders.
- Sign-up timing: two sign-ups with the same email within a couple of seconds, and the 0.47 s difference between a taken and a new address, are accepted for now.
- 'Tick at least one policy' on Save is a required-field message, so it is expected.

## New: soft-closed return windows (FS-24-9, FS-40-1)
After a return window ends (the item has return coverage and all of it has ended), the item page hides Refund, Mark returned and Start a return, shows a 'Return window closed' badge with 'A store may still accept a courtesy return, but it is a request, not a right', and offers 'Ask for a courtesy return anyway' behind a confirmation. Confirming brings the return actions back with a 'Courtesy return' note. Check: Cancel on the confirmation keeps them hidden; 'Start a refund or claim' (warranty path) and Mark disposed stay available; an item with an open window or no window is unchanged; a return already in progress still shows its actions; the claim wizard's courtesy-return suggestion has the same link. The override lasts for the browser visit only (not saved on the server); reporting that it resets on a new visit is expected.
