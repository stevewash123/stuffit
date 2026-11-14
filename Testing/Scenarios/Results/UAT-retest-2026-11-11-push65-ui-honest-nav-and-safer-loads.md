# UAT retest: Push 65, honest menus, a bell that says when it failed, safer loads (Nov 11, 2026)

- **Build:** UI only. UI Last-Modified 3:25:40 PM ET (20:25:40 UTC). API unchanged at `1d48a72` (started 2:08 PM ET). No migration (per notes). The new behaviours ("Start a claim", returnUrl handling) were visible, so the 3:25 PM UI was the one running.
- **Source:** `CHANGES-push-65-honest-nav-and-safer-loads.md` (Bot Rules, written 3:24:54 PM ET). Notes: `/workspace/uat/push65/p65-notes.md`. Screenshots: `p65-01` to `p65-08` in `/workspace/uat/push65/shots/`.
- **Accounts:** Alice and Ops (secure fill plus TOTP).
- **Clock:** moved to Offset 9 for the closed-window check, then reset. **Final Offset 0.**
- **Fixtures:** QA made no new fixtures.
- **Not reported:** the notes' "Not built yet" list.

## Results

| Result | Count |
|---|---|
| Pass | 5 |
| Partial | 0 |
| Fail | 0 |
| Not checked (optional, low priority per notes) | 1 |

| # | Change | Result |
|---|---|---|
| 65-returns | Menu > Returns and typed /returns open "Returns in progress" | **Pass** |
| 65-ops-menu | Operator menu has no Review | **Pass** (the notice click-through couldn't be checked) |
| 65-bell | Bell says it could not load | **Not checked** |
| 65-claim | Closed-window item link reads "Start a claim" | **Pass** |
| 65-signin | Off-app sign-in return links land on Home | **Pass** |
| 65-items | Opening a second item quickly always shows the second | **Pass** |

## Details

**65-signin Pass.** As Alice, signed out, each `/login?returnUrl=…` then sign-in:

| returnUrl | Landed on |
|---|---|
| `%2Fsettings` (control) | `/settings/profile` |
| `%5C%5Cexample.com` | `/` (Home, "Welcome, QA") |
| `%2F%5Cexample.com` | `/` |
| `%2F%2Fexample.com` | `/` |
| `https%3A%2F%2Fexample.com` | `/` |

None went to example.com.

**65-returns Pass.** Menu > Returns lands on `/returns/in-progress`, heading "Returns in progress". Typing `/returns` redirects there too. Low observation: a click on Returns made right after sign-in, while Home was still loading, did nothing; a second click after the page settled worked.

**65-items Pass.** Two items, **UAT P65 Item One** ($10) and **UAT P65 Item Two** ($20). Six fast switches (four via My Items, one via Back, one by pasting One's URL then Two's): every time the page settled on Item Two at $20.00.

**65-claim Pass.** At Offset 9 (app 2026-11-20), Item One's Amazon window (last day Nov 19) shows "Return window closed. The return window ended on Nov 19, 2026. A store may still accept a courtesy return, but it is a request, not a right. [Ask for a courtesy return anyway]". The bottom link reads exactly **"Start a claim"** after navigating and after a reload. It opens `/items/<id>/refund`, headed "Refund or claim" / "Why do you want to return it or make a claim?"; nothing was submitted. On Item Two (window open) there is a "Start a return" button and "Start a claim" at the bottom. Both items were deleted afterwards.

**65-ops-menu Pass.** Ops lands on `/admin`. The menu shows exactly Companies, Shared data, Businesses, Feedback, plus a "Customer view" button; no Review. Typing `/review` lands on `/admin` (Shared data). There was no "Shared data ready to review" notice in the Ops bell (only "Add a credit card and confirm its benefits" and "New feedback: problem", Nov 4), so the notice opening Companies could not be checked.

**65-bell Not checked.** The notes call it hard to see on staging and low priority. QA didn't block the notifications request in DevTools.

## Seen again (known)

Alice signs in straight to "P34-Alice Repairs" with no "Where to?" chooser, and after switching to Personal a full reload showed "P34-Alice Repairs" again in the account select. This is the known header account-select display issue. The P65 items probably went into the business account, which doesn't affect these checks.

## Data left behind

None. Both P65 items were deleted.
