# Push 104: every policy shows where its terms came from (API f7d2dd1, UI d8033ce)

New feature plus wording. No placeholder data any more: `--seed-placeholders` is removed, and the Dev database has no "[placeholder]" policies (checked: 0 to remove). Ski data (Rossignol, K2, Smith helmets; evo and Christy Sports returns; unconfirmed Backcountry and L.L.Bean) was loaded into Dev on 2026-11-14.

## What changed
1. **Source badge** (a small shield button) on each suggested coverage line (the "Suggested coverage" list). Tap it: the panel shows the status, the date, the page(s) the terms came from (https links, new tab), and "Report a problem with this policy". The source is fetched only when the panel is opened.
   - Statuses: "AI verified from company website" (with "Please confirm this matches your item."), "User confirmed from multiple uploads" (2+ different accounts' documents), "Reviewed by WarrantyCat administrator" (an operator checked it).
   - A policy with no real source (placeholder, typed by hand, name-only seed, or an unconfirmed entry) says "We don't have this company's terms on file yet ... Please check it with the company." Extended plans have no badge.
2. **Report a problem**: the link opens Feedback ready to send as a Problem, the message starting "About this policy: <company and kind> (<type>/<id>)". It goes to the existing feedback queue.
3. **Company page** with no policy: "We don't have this company's terms yet." (was "No warranty recorded yet."). The New Items line "No warranty found yet" is unchanged.
4. **Terms** (the "Reminders are a convenience" paragraph) now say policy information comes from public sources, may be out of date, is not a guarantee of coverage, and that each policy shows its source and status. **The Terms version changed (2026-11-14.1): every existing account, including Alice, Bob and Ops, is asked to accept the Terms again at next sign-in.** That is expected, not a bug.
5. API: `GET /api/policy-source/{seller|manufacturer|cardBenefit}/{policyId}` for any signed-in user (401 without sign-in, 404 for an unknown or invisible policy). Dates are date-only (`2026-11-13`), no account ids, only a count.

## What to check
1. Sign in as any account: the Terms re-acceptance appears; accept it and continue. Read the new paragraph in the Terms window.
2. Add a purchase from evo with a Rossignol or K2 item (or Smith helmet). In Suggested coverage, open the shield on the manufacturer line: status "AI verified from company website", a date of 11/13/2026, a link to the brand's own warranty page, and the confirm prompt. The evo return line should show a link to evo.com/pages/returns.
3. On a Backcountry or L.L.Bean return line: the panel says there is no source on file (they are unconfirmed on purpose).
4. "Report a problem with this policy": Feedback opens with type Problem and the message pre-filled; send it; it appears in your list and in Admin > Feedback.
5. As Ops (operator), Admin > Companies for a store or brand with no policy shows "We don't have this company's terms yet." on its public company page.
6. API: `GET /api/policy-source/manufacturer/<id>` for a Rossignol policy id: `status` is `aiVerified`, `label` as above, `urls` has the rossignol.com page, no account ids anywhere in the body.

## Expected differences from before
Scenarios that relied on fake placeholder terms (for example the Vizio "not the real terms" lines) no longer have them. Mark those Not tested, not Fail.
