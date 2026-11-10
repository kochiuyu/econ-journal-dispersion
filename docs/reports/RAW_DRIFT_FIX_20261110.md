# Raw-drift fix — editors_raw_drift_fix_20261110

Published 2026-11-10 (Asia/Taipei). It supersedes `editors_post_review_fix_20261110` and is stacked on PR #53.

## Why

In the comparison of the Directory panels against the Collector source panels (`raw_drift_20261110.csv`), 39 rows had a different `raw_affiliation` and 6 Directory keys were missing on the Collector side.

The cause was the Collector's 2026-10-28/29 `institution_*` scripts. They wrote derived names into `raw_affiliation`: a ROR name, a stripped core, or a new raw value. When the derived name came from a wrong ROR, such as National Law University, it replaced the printed text. The ROR was later removed, but the text and the India country stayed.

In `editors_ror_consistency3b_20261101`, the Directory restored the printed text on those rows (commit 4c3cf76). It kept the stale Institution fields, though, so 21 rows still showed India. The Collector has now restored the printed text and fixed the Institution fields at the source, and has patched its scripts so they leave raw text untouched.

## What changed

The Collector's whole row was taken on these 40 publish rows, keyed by `editor_row_key`:

| Group | Rows |
|---|---:|
| Former `National Law University` rows: real ROR and country instead of India (Lyon, Wellington, Bucharest, Toronto, Adelaide, Keele, Newcastle AU, Leiden ×3, University of Law, Witwatersrand ×2, Zhongnan, Louisiana Lafayette ×3, Tilburg, Plovdiv, Albany, La Verne) | 21 |
| HKUST (Guangzhou) on `050h0vm43` / China. C #27613 moved off the HKUST Hong Kong ROR `00q4vv597`; the other 10 differed only in match notes | 11 |
| Kagoshima University `03ss88z23` (was Nihon University); MIT `042nb2s44` (was Ikon Science); Gradient `014qf4206` (was Korea Telecom); ENSAI `00k206f19`; Springer Nature (Shanghai, China) `01f9pza55` | 5 |
| FT50 #2955 Tiffany Trzebiatowski → Colorado State University `03k1gpj17`, in both FT50 files | 2 |
| ajg1 #10149 Lawrence Sweet → `IZZI Inc`, as printed on the live board page. The earlier Rosalind Franklin text came from a faculty-search hit for a different Lawrence Sweet | 1 |

The 40 matching long-table rows were synced as well. New `ror_id`s on the panels, each checked on the ROR API v2: `00bge3r76`, `0545p3742`, `0558j5q12`, `03ss88z23`, `014qf4206`, `01f9pza55`. No ROR id is invented.

The following were not taken:
- The Collector's three Top 5 seats (#10046–#10048) were already in the Directory panels and are not duplicated. The long table keeps 181,443 rows.
- The two Pompeu Fabra institution-as-name rows and the 10 AJG1 navigation rows stay out.
- Pilot panels are not published.

## Directory

| | Before (#53 head eedf784) | After | Collector |
|---|---:|---:|---:|
| Institutions | 14,195 | 14,176 | 14,176 |
| with ROR (= distinct ROR) | 6,379 | 6,384 | 6,384 |
| Countries | 162 | 162 | 162 |
| Appointments without an institution | 12,659 | 12,658 | |
| Shared display names | 49 | 49 | 49 |

## Checks

- **Scrub:** the site data has 0 e-mail addresses and 0 phone patterns, and the changed rows and the pinned folder have none either.
- **Protected names:** 11KBW, UNSW Sydney, INSEAD France / Singapore / UAE, 1 Decembrie 1918 University and Bank of England are intact.
- **Near-miss pairs:** Bolton/Boston, IIT/Indiana, Queen's Belfast/Canada, Tokyo Tech/Science Tokyo, Petru Maior/Palade and Aachen/RWTH stay separate.
- **Row counts:** ajg1 12,316, ajg2 5,462, FT50 10,047. The long table has 181,443 rows and 20 columns.
- **Untouched files:** CITATION.cff, core49 and `scripts/build_site.py` (guard 49 and the scrub patch were already in).

## Still open (Collector leak scan, not changed)

`RAW_DRIFT_leak_scan_20261110.csv` lists 166 more rows where an `institution_*` script wrote a canonical or ROR name into the raw text. The Directory carries the same text on all of them.
- 120 are same-organisation normalisations.
- 46 look like a different organisation. Examples: 17 Pakistan rows → National Institute of Oceanography, 9 → AM Publications, 4 Japan rows → Temple University.

Restoring them needs a separate approval.
