# Scenario 40: Retest the fixes from the 2026-11-02 UAT rounds

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25) and are clean. The app runs with `Clock:Simulated=true` and a `Maintenance:Key` (Scenario 24); the clock is at offset 0. Cloudinary (file storage) is configured on the site, with its **PDF and ZIP files delivery** setting enabled (the staging owner confirms this). The receipt `Testing/SampleData/receipts/pdf/12-thermal-long-many-items.pdf` and a small PDF receipt (any file from `receipts/pdf`) are available to upload.
**Time:** 45 min
**Built per:** the fixes listed in `Results/UAT-results-2026-11-02-build-d1ed2c0.md` and `...-3ad4970.md`. This plan only rechecks them. Each row names the finding it closes.
**Why this plan:** these were found by testing; a fix is not done until the same person finds it gone.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | **Item page dates (FS-24-9).** Add item "UAT Clock Shoes", New Balance, today, with its return window (30 days). Advance the clock 31 days; reload the item page and /items | The item page and the items list agree: it says the window has ended. No "30 days left", no "Covered 1 policy", no **Start a return** button. The badge and "Next to end" line show the window as ended |
| 2 | Test1 | On the item, add a to-do "UAT overdue" due the day before the simulated today (the To do box) | /todos says **Overdue** (since the date), not "Due in 1 day". Notification and to-do times follow the simulated date |
| 3 | Test1 | **Bell badge (FS-24-6).** With unread notifications and a to-do waiting, look at the bell | The number on the badge equals the number of unread notifications listed. A lone to-do (nothing unread) shows a dot, not a number |
| 4 | Test1 | **Notification title (FS-24-6).** On /notifications, click the **title** of a notification (not "View item") | It opens the same place as View item and marks it read |
| 5 | Test1 | **Plan ended today (FS-31-16/17/18).** Add a plan covering "UAT Clock Shoes" (as Scenario 31). Open **End this plan** | The "It ended on" box is **empty** and **End this plan** is disabled until a date is chosen |
| 6 | Test1 | Choose today's simulated date and end the plan | The plan row says **Ended <date>**, is dimmed, and is **not** in the yearly total or the "covering items worth" figure. The item's coverage no longer lists the plan as running |
| 7 | Test1 | **Export (FS-27-13/14).** Settings > Privacy & data > **Download everything**; wait for it; click **Download** | A zip file is saved. It opens and lists the readable files (README, account, purchases, items, coverage and others). **No** "That download is no longer available" message |
| 8 | Test1 | **PDF receipts (Cloudinary delivery).** Add an item, upload a small PDF receipt to it, then click **View** on the file | The PDF opens. If it fails, record the exact message: this is the storage setting for PDFs |
| 9 | Test1 | **Feedback overflow (FS-35-9).** Open Send feedback and paste a 4,000-character message with no spaces, then one with ordinary words | The page does **not** scroll sideways. A counter reads "<n> / 4,000" and turns to a warning at the limit with a plain sentence. Sending and "What will be sent" / "Your messages" wrap long text |
| 10 | Test1 | **Nested link.** From /feedback, click the footer **Send feedback** link and the Account menu link, twice each | The address never grows `from=...from=...`. The panel's "Page you were on" is the page before the form, not the form |
| 11 | Test1 | **Tracking note (FS-33).** Settings > What to track: type 250, then click **Everything** (do not save) | The note under the amount reads the standard amount is $50.00, not "Using the standard amount", and follows the field. Save to 0 and check it again |
| 12 | Test1 | **Receipt lines past the cap (FS-33-3).** Upload `12-thermal-long-many-items.pdf` with the tracking minimum at the standard $50 | New Items shows **all 12 lines** across the main list and **Smaller things**: no line is missing. WOOD GLUE 16OZ ($6.99) and SANDPAPER 80G x5 ($12.45) are under **Smaller things** with the reason "Cheaper than the lines kept". The upload note says how many more lines are under Smaller things |
| 13 | Test1 | **Work gloves (rule kept by design).** Look for the Work gloves line ($25.98) | It is labelled "Under $50" and stays in the main list. Record that it is still there: this is expected, not a failure |
| 14 | (outsider) | **Sign-up leak (FS-25-12).** In a private window, sign up with Test2's address, then with a brand-new address; time each from pressing the button to the "Check your email" page, three times each | The same page for both. The times are close to each other (record all six in seconds). Test2 receives an "already have an account" email and the new address receives the confirmation link |
| 15 | (outsider) | **Reset links (FS-25-17).** Request a password reset for Test2 twice, a minute apart | The older link is refused with "This link has already been used or has expired."; the newer link works |
| 16 | Test1 | **Console.** Open the browser console on /login, Home, an item page, /notifications and /feedback; reload each | Record every console error with its text and URL (for example from /login). None should come from a page that is working |
| 17 | (maintenance) | Reset the clock | "Offset 0 day(s)" |

Also record: for any row that fails, whether it fails the same way as in the earlier report, and the exact message. Rows 7 and 8 depend on storage settings, not on the app; say so if they fail.
