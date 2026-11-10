# Country-misprint and fragment fix — editors_country_misprint_fix_20261110

Published 2026-11-10 (Asia/Taipei). Supersedes `editors_trailing_country_fix_20261110` (PR #53).

## What changed

It is a keyed, user-approved fix on top of `editors_trailing_country_fix_20261110` (PR #53): 30 publish rows get the real country for 27 Institutions whose printed country was wrong (e.g. ESADE Business School → Spain, TU Berlin → Germany, Queens University Belfast → United Kingdom); Imperial College of London (C #17649) is rematched to the existing panel ROR `041kmwe10` Imperial College London. 11 fragment rows (the 11 held back in PR #53) get a clean `canonical_name` or a blank one: the Court of Appeal / Supreme Court rows become `Court of Appeal of England and Wales` / `Supreme Court of the United Kingdom` (UK), the two Independent Scholar rows become `Independent Scholar`, and `Greece and`, `Italy &`, `Finland and`, `SE` and the Solicitor row are blanked, so the Directory falls back to the printed text (e.g. `Greece and UK`). `University of the North, Barranquilla, .` loses its trailing `, .` and merges with its twin. The printed `raw_affiliation` is unchanged; no ROR id is invented.

42 publish-panel rows (30 country, 11 fragment, 1 Barranquilla) and 41 long rows. Details and the file table: `data/editors/releases/editors_country_misprint_fix_20261110/README.md`.

## Directory

| | Before (#53) | After |
|---|---:|---:|
| Institutions | 15,166 | 15,160 |
| with ROR | 6,387 | 6,387 |
| Countries | 162 | 162 |
| Appointments without an institution | 12,068 | 12,068 |
| Appointments / editors / journals | 162,575 / 112,718 / 2,853 | unchanged |
| Shared display names | 69 | 69 |

The Collector's read-only build reported 15,165 → 15,159. The change (−6) matches; the one-row offset in the starting count carries over from PR #53. The PR #53 report attributed it to `University of the North, Barranquilla, .`, but that row is now merged and the offset remains, so the cause is still open.

## Checks

- Imperial College London 215 → 216 appointments; Independent Scholar (UK) 23 → 25; University of the North, Barranquilla 1 → 2; Court of Appeal of England and Wales (UK) 3.
- Country-only raw fallback (canonical blanked by the Collector, page shows the printed text): `Greece and UK`, `Italy & UK`, `Finland and Tanzania` and the Solicitor string (blank country), and `SE, UK` (United Kingdom). Removing them needs a Web-side rule or an approved DROP.
- University of New South Wales (2) now Australia, ROR still blank; UNSW Sydney `03r8z3t63` unchanged.
- Protected names unchanged. No ROR id invented. Row counts, nav rows, no pilot files, no contact data; CITATION.cff, core49 and `scripts/build_site.py` untouched.
