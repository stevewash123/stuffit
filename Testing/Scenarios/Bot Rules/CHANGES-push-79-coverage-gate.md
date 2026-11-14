# Push 79: test coverage gate (S9.10.11)

No change to the app. Adds `karma.conf.js` and points the UI test target at it, so a test run with `--code-coverage` fails if statement/branch/function/line coverage drops below a floor. The UI redeploys, but nothing a person sees changed. No QA run is needed; if you do a quick smoke (sign in, open My Items) it should look exactly as in Push 78.
