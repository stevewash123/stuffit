# Data to add: a Tablets category and a Subscriptions and services category (2026-11-03)

For GrokBot. Your push 6 retest could not run **C-0 (tablet half of the device default, C43-7)** or **B-8 (the plan question is hidden for a subscription or service)** because those categories did not exist. Add them with one of the routes below, then run the rows.

The seed file now has both (`reference-data.json`). The seeder only inserts missing rows, so a build that includes this change adds them on its next start. **Check first**: open the category list on Add purchase. If "Tablets" (under Electronics) and "Subscriptions and services" are there, do nothing. Until a build with this change is deployed, use the database route.

| Category | Parent | Why |
|---|---|---|
| Tablets | Electronics | A device: the type-it-in drawer starts on Insurance, monthly (C-0). Also counts as Electronics, so the plan question shows for it |
| Subscriptions and services | none (top level) | Not one of the five plan-question roots, so the question must be hidden (B-8) |

## Route 1: database (staging, shared reference data)
Run once; each insert skips a name that already exists.
```sql
INSERT INTO categories (id, name, parent_id, created_at)
SELECT gen_random_uuid(), 'Tablets', (SELECT id FROM categories WHERE name = 'Electronics' LIMIT 1), now()
WHERE NOT EXISTS (SELECT 1 FROM categories WHERE lower(name) = 'tablets');

INSERT INTO categories (id, name, parent_id, created_at)
SELECT gen_random_uuid(), 'Subscriptions and services', NULL, now()
WHERE NOT EXISTS (SELECT 1 FROM categories WHERE lower(name) = 'subscriptions and services');
```
Reference data is shared by all accounts, so DB Stager resets do not remove it.

## Route 2: through the app
There is no screen for adding a shared category. Use Route 1, or restart on a build with this change.

## Then run
| Row | Steps | Expect |
|---|---|---|
| C-0 / C43-7 | Add an item "UAT Tablet", category **Tablets**. Item page > Add-on protection > Add > I'll type it in | The drawer starts on **Insurance, monthly** (same as phone and laptop) |
| C-0b | Add purchase from a shared store (Best Buy), item in Tablets, price $400 | The "Did you buy additional protection..." question **shows** |
| B-8 | Add purchase from a shared store (Best Buy), item in **Subscriptions and services**, price $400 | The question is **not** shown |
| B-8b | Same, item price $5 in Smartphones | Not shown (below the tracking minimum, control) |
