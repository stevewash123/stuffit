# UAT retest — Push 39: singular reading entry and boat in-service (Nov 9, 2026)

- **Build:** API 6a9d94c, started 7:04:33 AM ET. UI unchanged (API-only push). Staging.
- **Source:** CHANGES-push-39-reading-entry-singular-2026-11-09.md (1002 B); HANDOFF-push39-6a9d94c-retest.txt.
- **Scope:** (1) reading entry of exactly one says "1 hour" / "1 mile" (`readings[].unit` singular); (2) boat in-service date after reading edit — enter on Add, edit reading, read `inServiceDate` via API. Targeted only; no regression; no migration or seed.
- **Not changed:** bare GET `/vehicles/{id}` has `paidBy: null` (left as is).
- **Run:** ~7:35–7:40 AM ET. UI as p34self Personal (browser already signed in). API as Alice (P34-Alice Repairs owner). Bob's env password works again (200); p34self has no env password (vault only), so Alice/Bob cannot GET p34self items (404).
- **Clock:** Offset 0 throughout (no clock moves).

## Results

| Result | Count |
|---|---|
| Pass | 2 |
| Partial | 0 |
| Fail | 0 |
| Inconclusive | 0 |

## Per-step results

| # | Check | Who / how | Result |
|---|---|---|---|
| 1 | Reading entry of exactly one is singular ("1 hour" / "1 mile"; `unit` = `hour` / `mile`) | p34self UI + Alice API | **Pass** |
| 2 | Boat `inServiceDate` unchanged after reading edits (typed 2026-10-15) | p34self UI + Alice API reproduction | **Pass** |

### Step 1 — Singular unit: Pass

**UI (p34self boat 01a1c04d-b4f5-7df5-9ddf-9333d14122f8, Yamaha X1, Hours):**
- Summary: "1 hour on Nov 9, 2026".
- Entry: "1 hour on Nov 9, 2026 · You entered it".
- At 2: "2 hours". Back to 1: "1 hour".
- Screenshots: /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/8ebb4d1bec816ccb555afe3af309b8bd7333a7772df216d1ea9bccc9e3cfce63.png ; /cursor/stores/user/grok-bot/agents/11d2507a-1e1a-4a89-b309-0783c8a32d08/assets/831d5a2216a1674912cddb48132606a814fa4b4b3e19c553b794b0395fc8ad54.png
- Car 1-mile reading was not checked in the UI.

**API (Alice, fresh fixtures):**
- Boat 01a1c050-5f53-7272-b224-eae2dc745d5d: value 1 → `unit` **"hour"**, latestLine **"1 hour on Nov 9, 2026"**; value 2 → `unit` **"hours"**, latestLine "2 hours on Nov 9, 2026"; back to 1 → **"hour"** / **"1 hour…"**.
- Car 01a1c050-626d-7906-aa1c-6bd4132db66d: value 1 → `unit` **"mile"**, latestLine **"1 mile on Nov 9, 2026"**.

### Step 2 — In-service date after reading edit: Pass

**UI (p34self boat 01a1c04d-…):**
- Bought new; First put in service typed **2026-10-15** (shown 10/15/2026).
- Detail before and after adding reading 1 and editing 1→2→1: **"in service Oct 15, 2026"**; edit form still **10/15/2026**. No flip.

**API:**
- p34self boat / earlier push-38 boat 01a1be6a-… / car 01a1be6c-…: Alice and Bob GET → **404** (vault-only login; not readable over API from those accounts).
- Alice reproduction boat 01a1c050-5f53-… created with `inServiceDate` **"2026-10-15"** (no timezone off-by-one). After PUT `/api/vehicles/readings/{id}` to 2, then 1, then 2, then 1: `inServiceDate` remained **"2026-10-15"** every time. Editing a reading does not change in-service.

Push 38 finding 2 (UI showed Nov 8, 2025) was not reproduced here in UI or API.

## Needs follow-up

- None for scope. Optional: store an API-reachable password for p34self if future runs must GET that account's items without a browser session.

## Needs code changes

- None.

## Test data

- **p34self UI:** boat 01a1c04d-b4f5-7df5-9ddf-9333d14122f8
- **Alice API:** boat 01a1c050-5f53-7272-b224-eae2dc745d5d; car 01a1c050-626d-7906-aa1c-6bd4132db66d

## Evidence

- /workspace/uat/push39/api-boat-cycle.json
- Screenshots listed under Step 1
