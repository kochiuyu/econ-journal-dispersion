# Trailing-country fix — editors_trailing_country_fix_20261110

Published 2026-11-10 (Asia/Taipei). Supersedes `editors_raw_aff_part_no_fix_20261110` (PR #52).

## What changed

Institution names that ended in a printed country (`…, USA`, `… - UK`, `…, People's Republic of China`) had the country stripped from `canonical_name`, and the country written to `ror_country` / `continent`. The audit (`/workspace/institutions_trailing_country_20261110.csv`) sent 5,009 Institutions; the Collector applied 4,906 (STRIP_AND_SET_COUNTRY 4,546, STRIP 220, STRIP_AND_FIX_COUNTRY 3, REMATCH 137) and skipped 96 Institutions + 7 rows. The Directory applied the publish-set delta to 6,036 panel rows and 6,036 long rows, holding back 11 rows whose stripped name would end in a dangling `and` / `&`.

## Directory

| | Before (#52) | After |
|---|---:|---:|
| Institutions | 15,434 | 15,166 |
| with ROR | 6,387 | 6,387 |
| Countries | 159 | 162 (+Guinea, Haiti, Timor-Leste) |
| Appointments without an institution | 12,067 | 12,068 |
| Appointments / editors / journals | 162,575 / 112,718 / 2,853 | unchanged |
| Shared display names | 69 | 69 |

The Collector's read-only build reported 15,165. The one-row difference is `University of the North, Barranquilla, .` (the freeze's stripped canonical keeps a trailing `, .`), which stays separate from `University of the North, Barranquilla`.

## Checks

- Examples: `IE Business School, Madrid` → Spain (20); `Leeds University Business School, Leeds` → United Kingdom (15); `Thunderbird School of Global Management` → United States (17); `National Chiao Tung University` → Taiwan (17).
- None of the audit's 190 REVIEW names changed (e.g. `University of Illinois, USA`, `Indian Institute of Technology, India`, `London, UK` stay blank-country as before).
- Protected names unchanged. No ROR id invented; existing ROR ids unchanged.
- Row counts, nav rows, no pilot files, no contact data; CITATION.cff, core49 and `scripts/build_site.py` untouched.

## Open: printed country evidently wrong for the organisation

The fix trusts the printed country. Where the masthead printed a wrong country (usually the editor's location or a typo), the Institution now shows it. See the PR description for the list; these need a follow-up keyed fix.
