# UAT retest: push 68 (UI-only), coverage preview states on Add a purchase

- **Build:** the UI was redeployed at 8:12 PM ET Nov 11 2026 (Last-Modified 01:12:03 UTC). The API is unchanged at `7051bb3`.
- **Run:** 8:33 to 8:43 PM ET, as Alice. The app clock was not moved and is at offset 0.
- **Scope:** CHANGES-push-68-coverage-preview-states.md, rows 1 to 5.
- **Lookup request:** `POST /api/pending-items/coverage-preview`. I slowed it with Chrome DevTools "3G" throttling and failed it with DevTools "Block request URL".

## Summary: 4 Pass, 1 Fail (Medium)

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | "Checking what applies…" shows while the lookup runs | **Pass** | I picked Power tools, then DeWalt. About 0.5 s later the preview changed from "Fill in the store, brand and category to see what applies." to "Checking what applies…". About 2.5 s later it showed "DeWalt warranty · Manufacturer · 3 years · Confirmed" and "Counted from today until you give the date." Shots `p68-01-checking.png` and `p68-01b-list.png`. |
| 2 | Quick changes end on the last choice | **Pass** | I changed the category Major appliances, Power tools, Major appliances, Lawn and garden, about 0.4 s apart. "Checking what applies…" showed above the old list while it loaded. It settled on the last choice at about 4.6 s with "DeWalt warranty · Manufacturer · 3 years · Likely" (unticked) and "Not added. Tick it to add it when you save, or add it later from the item page." It never flipped back during 20 more seconds, and the older requests show as cancelled in Network. Shot `p68-02-final.png`. |
| 3 | A failed lookup shows a message and Try again | **Pass** | With the request blocked, the preview read "We could not check the coverage just now. Try again", with a Try again button. "Nothing found yet" never appeared. After I removed the block, Try again showed "Checking what applies…" and then reloaded "DeWalt warranty · Manufacturer · 3 years · Confirmed". Shots `p68-03-failed.png` and `p68-03b-retry.png`. |
| 4 | Two items each have their own state | **Fail (Medium)** | Item 1, "P68 DeWalt drill", showed "DeWalt warranty · Manufacturer · 3 years · Confirmed". Item 2, "P68 Samsung fridge", showed "Samsung warranty · Manufacturer · 1 year · Confirmed". With the request blocked, I changed only item 2's category to Refrigerators. **Both** rows then showed "We could not check the coverage just now. Try again". Network showed two blocked coverage-preview calls, so a change to one item reloads every item's lookup, and item 1 lost a list that was already good. After I unblocked, Try again on item 2 reloaded both rows. Removing item 1 does work: item 2 kept its own "Samsung warranty · Manufacturer · 1 year · Confirmed". Shots `p68-04-two-items.png`, `p68-04-one-blocked-both-failed.png` and `p68-04b-after-remove.png`. |
| 5 | Receipt attach and the PayPal card question behave as before | **Pass** | **Receipt:** `homedepot-receipt-01.pdf` showed "What we found in your document". The store was Home Depot (Shared, Verified). The brand had a conflict, "Keep yours: Samsung" or "Use the document's: Milwaukee". It also read 199.00, 2026-08-15, a 417.53 total and order 3456. After applying, the form showed "Attached: Receipt (PDF) (added here)". **PayPal:** Alice had no cards, so I added a test card ("P68 Test Visa", last 4 only) and PayPal under Credit cards. On Add a purchase, picking PayPal showed "Which credit card is behind PayPal?" with "Not sure yet" or "P68 Test Visa", plus "PayPal's receipt doesn't say. That credit card's benefits are the ones that apply, so pick it." The item page showed "Paid with PayPal" and "Credit card behind PayPal: P68 Test Visa". In Edit purchase I changed it to "Not sure yet" and back. Each change stayed after a reload. Shots `p68-05-paypal-item.png`, `p68-06-add-paypal.png` and `p68-06b-item-paypal.png`. |

## Lows and notes (not part of this push)
- The item's Receipts section says "PayPal (credit card) is not in our shared list yet…", which calls PayPal a credit card.
- The only console error was a 401 on `/api/auth/refresh` before sign-in, which is expected.

## Needs CC
- Row 4: changing one item's details should re-run only that item's coverage lookup. Today it re-runs every item's lookup, so one failure blanks the other rows.

## Cleanup
"P68 Samsung fridge" and "P68 PayPal drill" are deleted, and Alice's My Items shows "Nothing here yet". The test card and the PayPal entry are deleted, and Credit cards shows "No credit cards yet." Alice is signed out.

## Fixtures
None new. I used `reg-982952c/rcpt/homedepot-receipt-01.pdf`.
