# WarrantyCat testing list (2026-10-06)

Automated tests pass (API unit 264, integration 354, UI 688). This is what they cannot tell us. Nothing built since 2026-10-03 has been checked in a real browser, and nothing has run against the real model.

Order: 1 first (everything on the reader path depends on it), then 2, then the rest.

## 1. Real model (reader) — needs an API key in user-secrets (`Ai:Provider` = `anthropic`, `Ai:AnthropicApiKey`)
Build the labelled set first (S2.4.1): your own real documents, with the right answer written next to each.
- [ ] Receipts: 10+ printed receipts (store, online order PDF, phone photo, crumpled, two-page). Check store, date, total, order number, last 4, items. Count wrong values at high confidence (target: zero) and values correctly flagged low.
- [ ] Policies: your renter's or homeowner's declarations page. Check insurer, number, dates, deductible, limits, items listed separately.
- [ ] Plans: one extended-warranty contract. Check provider, term, price, what it covers.
- [ ] Cost and speed: look at `ai_usage` after the run. One receipt should cost cents and finish in seconds; the same file again must be free (cached by hash).
- [ ] Refusals and failures: provider off, daily limit hit, unreadable photo. The page must say so plainly and let you type it in.

## 2. Browser pass (desktop and phone width) — use `--seed-demo` data
- [ ] New Items: upload a receipt, an `.eml`, a burst of photos. Accept, Add details, Dismiss and Undo, attach to an existing item. A low-confidence value shows "Not sure of" and holds quick add.
- [ ] Item page: read-only by default, pencil turns on edit, add coverage, receipt upload, mark returned, start a return, suggested coverage.
- [ ] Policy page: "Start from your policy", the found-values review, fill, save, "Listed separately on the document" matching, update from a newer document.
- [ ] Plans page: start from a contract, update from a newer one.
- [ ] Notifications: bell count, list, Needs action filter, Done / Remind me later / Dismiss / Not now, already-handled message, acknowledge.
- [ ] To-dos: item card, Home tile, /todos page, snooze and done.
- [ ] Settings and Account menu: preference grid, avatar menu, four phone tabs, export, delete account, legal pages and consent.
- [ ] Looks: dark mode, keyboard-only use, screen reader labels on the icon buttons, nothing cut off at 360 px wide.

## 3. Reminders, end to end
- [ ] A coverage nearing its end, a dated to-do, a card with no confirmed benefits: each nudges at your local send time, once only.
- [ ] Two to-dos ready the same day: one joined message, link opens /todos.
- [ ] Real email through Resend (set `Email:ResendApiKey`, run the delivery tests): arrives, unsubscribe link works, preference off suppresses it.
- [ ] The job after a server sleep or restart: no duplicates, no missed nudges.

## 4. Real devices
- [ ] Install the app on a real iPhone and an Android phone. Phone capture, multi-page scan, Wi-Fi-only upload, waiting-to-send box, blur check, crop.
- [ ] HEIC photos read correctly on the Linux host (not just Windows).
- [ ] Android phone camera permission and back-button behaviour in the installed app.

## 5. Data and security
- [ ] A second account cannot see or answer the first account's items, notifications or policies (try URLs and ids by hand).
- [ ] Household: two people on one account, an item with owner and follower, who is told about what.
- [ ] Export: open the zip, check every table and file is there. Delete account: gone, and the 90-day purge rule holds.
- [ ] Admin two-step sign-in and operator screens.
- [ ] Test database stays separate: dev data never touched by the suite.

## 6. Open facts to confirm (not code)
- [ ] New Balance 30-day return window (our fetch got 403): check newbalance.com.
- [ ] Seed rows added after a database was seeded (Pflueger website, Amazon link) are not picked up by existing databases: decide on a one-time fix.
- [ ] Sony omitted from the seed (its site blocks the crawler).
- [ ] Before launch: lawyer review of legal pages, trademark and domain check, `Email:MailingAddress`, rotate the DB password in docs/security.md and the credentials in the public ConsignmentGenie repo, backup period in the privacy policy.

## Not tested because not built
Email-link quick actions, multi-item orders as one purchase, later delivery email for an accepted order, background reading status, inventory report for a claim (F5.3), billing (Stripe), storage cap, 90-day purge job.
