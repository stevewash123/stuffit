# What changed in push 41: fixes from the push 40 report (2026-11-09)

For GrokBot. Check `/api/version` against the pushed API commit (UI changed too). No migration, no `--seed`. Targeted retest: S64 certificate (finding 1, 2) and S63 powertrain (finding 3).

## Fixed from the push 40 report
- **Finding 1, CPO header:** a certified or dealer-added coverage is labelled "Certified or dealer-added coverage", not "Manufacturer warranty". Its provider is the company the certificate names (for example UAT CertifiedCare), not the vehicle's maker (Toyota).
- **Finding 2, sharing notice:** a certificate with separate terms offers nothing to the community, and the "terms are shared with the WarrantyCat community" note no longer shows after it is applied. (The server did not share it before either; only the note was wrong.)
- **Finding 3, powertrain narrative:** a vehicle part with its own mile limit says so in its own line ("Parts and labor 5 years, or 60,000 miles, whichever comes first"). I could not see which screen showed 36 months / 36,000 miles, so please report the exact place if it still shows.

## Not changed, do not report
- Finding 4 (plan "What is it" not set, waiting days blank, auto-renew unchecked): the paper does not state them.
- Certified box on a hand-added plan; part form year / "came with"; Bob's API password (yours to restore).

## Tests at push
API unit 1212, integration 509 (+2 opt-in skipped); UI 1359. Added: provider name for a certificate, the part narrative, and a UI spec for the label and the missing sharing note.
