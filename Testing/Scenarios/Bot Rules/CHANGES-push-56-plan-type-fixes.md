# Push 56: plan type fixes from the push 54 report (2026-11-10)

API and UI. No migration.

| Change | What to check |
|---|---|
| **Medium: Edit plan no longer shows a blank type** after the type was versioned | The demo plan bought under the old Basic: Edit plan. The "What kind of plan is it?" select still shows **Basic (earlier version, the one you bought under)** selected, beside the company's current Basic. Saving keeps the link (`plan_type_id` unchanged) |
| **Low: the plan page names its type** | Open the plan (not Edit): "Plan type: Basic (an earlier version)" under the plan name. A plan with no type shows no line |
| **Low/Medium: operators can see earlier versions** | Admin > Companies > Extended warranty plans: tick **Show earlier versions**. The old Basic appears with "an earlier version, ended <date>; plans bought under it keep these terms", and no Change button. Unticked, only current versions show |
| **Low: empty-address message** | Confirm with an empty address: "Enter the address of the page you read it on." (was "The SourceUrl field is required.") |

## Not done (do not report as new)
- Companies added by a person through the Sold-by Add cannot be verified from this page: that is the existing shared-data candidate queue, not plan types.
- The item's quick "Add protection plan" dialog has no type select.
- Order 08 and the push 55 re-read are reported separately.
