# editors_ajg_gap_faculty_remiss_20261028

Faculty profile URLs for AJG-gap editors who still had no `faculty_profile_url`, plus host-map affiliations and high/medium ROR where the profile identified a university. Frozen 2026-10-28 14:57 Asia/Hong_Kong. This supersedes the held join/cache pass `editors_ajg_gap_faculty_url_20261028`. ABDC stays freeze `editors_nonft50_url_aff_20261028`. FT50 stays freeze `editors_ft50_url_aff_20261028`.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Empty `editor_name` is 0. The build does not invent a name, a ROR id, an affiliation, or a faculty URL. A bare country is not an institution. `faculty_home_page` is not written to the site. A profile URL that contains an email address is not published.

Names stay the blank-rescrape boards: ajg1 and ajg2 are `editors_blank_rescrape_20261028`; Sociology of Health and Illness on prio43 is `editors_blank_rescrape_browser_20261028`. The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Rankings were not edited.

## Collector freeze

The remiss searched editors who still had no faculty URL and no university. Person-like queries: 1,750, of which 409 matched (23.4%). Junk non-person cache hits demoted: 9. Junk URLs cleared on apply: 27.

| Panel | Rows in the collector file | Faculty URL | Miss aff | URL, no university | URL, no ROR |
|---|---:|---:|---:|---:|---:|
| prio43 | 3,166 | 49 → **102** | 450 → **402** | 0 → 5 | 0 → 5 |
| ajg2 | 4,985 | 265 → **388** | 306 → **206** | 0 → 27 | 0 → 28 |
| ajg1 | 11,230 | 403 → **618** | 2,565 → **2,350** | 0 → 21 | 0 → 29 |
| Total | 19,381 | **717 → 1,108** | **3,321 → 2,958** | 0 → 53 | 0 → 62 |

URLs applied this pass: prio43 53, ajg2 127, ajg1 238.

## Published in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2, the same exclusion as `editors_abs_ajg_gap_20261025`. They are publisher navigation, a paper title, and similar. None of those fourteen is a new person on the published boards. One of them, Vincent Pan on Advances in Decision Sciences, has a collector URL (`https://www.unsw.edu.au/staff/vincent-pang`) and a ROR for EU Business School, Geneva. That row stays out with the other thirteen. Published faculty URLs are therefore **1,107**, not 1,108. Published rows with no `raw_affiliation` are **2,946**, not 2,958.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, no university | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,166 | 0 | 102 | 2,764 | 2,704 | 5 | 5 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,983 | 0 | 388 | 4,778 | 4,626 | 27 | 28 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,218 | 0 | 617 | 8,879 | 8,666 | 21 | 29 |
| Total | 19,367 | 0 | 1,107 | 16,421 | 15,996 | 53 | 62 |

`ror_id` on a nonempty affiliation is 15,996 / 16,421 (97.4%): ajg1 8,666 / 8,879 (97.6%), ajg2 4,626 / 4,778 (96.8%), prio43 2,704 / 2,764 (97.8%). New ROR ids on this publish are high or medium only. Eight prio43 rows whose `editor_name` is `Email` stay in the CSV and stay out of the directory. Rows that still have no university stay blank. No name, ROR id, affiliation, or URL was invented.

## Public site

Directory appointments stay 158,716. Editors stay 110,383. Journals stay 2,853. Countries stay 173. FT50 seats stay 10,045 across 50 journals. Top 5 stays 363. UTD24 stays 5,178 across 24 journals. ABDC chips stay A* 25,174, A 45,352, B 42,124, C 26,719. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796).

Faculty profile links on the directory are 24,840 (were 23,735 after the ABDC freeze alone). Institutions are 10,093 (9,684 with a ROR id), were 10,065 (9,659 with a ROR id). Appointments with no institution are 10,724 (were 11,084). 28 country-only affiliations and 1 bracket-only fragment stay off that page. Parked blank `editor_name` rows are 0. Eight `Email` names on prio43 stay out of the directory.
