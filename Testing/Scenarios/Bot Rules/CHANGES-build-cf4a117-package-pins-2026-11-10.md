# Build cf4a117: package versions pinned (2026-11-10)

API only. No UI change, no migration, **no behavior change**. The API project's floating `9.0.*` package references are now pinned to the versions already in use (9.0.22, Npgsql 9.0.4). A fresh restore had started picking the half-published 9.0.23 set and failing, which would have broken the next clean build on Render.

## What to check
- Nothing new. A quick smoke is enough: sign in, open an item, open a repair order's Service history. This build is the same code as push 52 (75b770d).

The next note, push 53, is written but its code is not pushed yet. It will appear here when the build is live: test that one then, not this build.
