# Push 55: a repair order's job list is offered even when the reader was unsure (2026-11-10)

API only. No migration, no prompt change.

## Why
Push 53 order 08 (Tucson collision repair) showed no jobs. Run by hand against the same PDF with the same model, the reader returns all 8 jobs (bumper cover, refinish, A/C condenser, A/C recharge, radar calibration, alignment, paint materials, hazardous waste) and flags the list "medium" confidence. A repair order's job list was dropped whenever the reader marked it low, which it can do on another run. The person confirms every job before anything is saved, so a low-confidence list is now still offered. The date, odometer, order number and shop still need to be sure.

## What to check
| Change | What to check |
|---|---|
| Order 08 lists its jobs | Tucson order 08: Read it. The card should list the jobs (kept, or under "N other jobs were left out" with tick boxes). The expected answer is that none are service on a covered part: tick any that should be kept |
| Nothing else changes | Orders 03, 06, 07, 09, 12 read as in push 54 |

## If order 08 still shows no jobs
Please run this read-only query on Neon and put the result in the report (the stored reading shows whether the list was dropped, and why):
`select kind, prompt_version, model, created_at, result_json from document_readings where kind = 'service_record' order by created_at desc limit 3;`
Look for the `lines` entry: its `Confidence` and any `Issue`.
