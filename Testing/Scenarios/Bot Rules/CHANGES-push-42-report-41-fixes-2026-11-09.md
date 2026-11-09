# What changed in push 42: fixes from the push 41 report (2026-11-09)

For GrokBot. Check `/api/version` against the pushed API commit (UI changed too). No migration, no `--seed`. The reader prompt changed (triage v4, document v23), so the first item is a live-reader check.

## Fixed from the push 41 report
- **S68 water-pump repair order:** a dealer repair or service order is now its own class (`service_record`). Read it on one keeps it as a paper on the vehicle: no purchase facts are taken from it (no price, store or brand updates), nothing is offered as "Start a plan from it", and an emailed one is kept with the item instead of becoming a new item. The $0 warranty repair is not turned into a plan, claim or coverage; it does not touch the factory powertrain term. The service history itself (what was done, on which covered part) is the next push, so there is nothing to see of it yet.
- **Sign-in redirects:** a request that got a 401 because another call had just refreshed the token now retries with the new token instead of refreshing again. A refresh that fails because the server is restarting (a deploy) or the connection dropped is tried once more after 1.5 seconds, and only a refused refresh signs the person out.

## Not changed
- **Powertrain narrative (P41-3):** cannot reproduce from the data. With a Ford-style reading (36 months / 36,000 miles whole, Powertrain 60 months / 60,000 miles) the API returns the powertrain coverage with Terms "Parts and labor 5 years, or 60,000 miles, whichever comes first" and the miles line "Until Nov 7, 2031 or 60,000 miles ... 59,982 miles left". The 36 months / 36,000 miles text is the whole-vehicle coverage's own Terms. Please report which screen and which heading shows it (item page coverage card, details drawer, or the claim wizard) and the exact words.
- **Data-protection keys not persisted across deploys:** needs a database table (migration), so it goes in with the service-history push.
- Low items: the CPO popup still says "manufacturer's warranty"; absolute end miles not printed as 40,400 / 52,400 totals.

## Tests at push
API unit 1212, integration 510 (+2 opt-in skipped); UI 1361. Updated: the document prompt version expectation (v22 to v23). Added: a service order is kept as a paper and not read as a purchase or plan; two interceptor specs (retry with the newer token; a restarting server does not sign out).
