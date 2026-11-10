# Push 47: re-adding a repair order keeps "added by you" rows (2026-11-09)

Fix for the push 46 Medium. Re-adding an order already in history replaces only the entries the rules kept; jobs added by hand ("added by you") stay. Ticking the same left-out job again does not duplicate it. The card now says "jobs you added by hand stay". The no-odometer card no longer says "Its odometer reading can still be kept".

Check: P46-01 add oil + tires + wipers, then re-read and Add with nothing ticked: oil only replaced, tires and wipers still there, still "added by you".
Not changed: the three Low notes (picker names, picker reset on retick).

## Request for QA: put your fixtures in the shared folder
Your report suggested promoting `P46-01-service-tires-wipers-2026-10.pdf` and `P46-02-counter-tires-wipers-only-2026-11.pdf` into the scenario set. Yes, please do. They exist only in your workspace (`/workspace/uat/push46/`), and Claude Code cannot read that.

- Copy both PDFs into `Testing/Scenarios/Scenario 68 - Backdated car with service records/` (the first-page JPG twin too, if you make them), numbered after the existing files (07 and 08).
- Do this from now on for any fixture you make: save it in the matching `Testing/Scenarios/Scenario N - .../` folder (or `Testing/SampleData/` for general ones), and name the file in your report.
- When done, say so in the push 47 report. Claude Code will then add the steps to `scenario-68.md`.
