# Editors — ABS/AJG gap

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — ajg1 and ajg2 are freeze `editors_blank_rescrape_20261028`. The prio43 file includes freeze `editors_blank_rescrape_browser_20261028` for Sociology of Health and Illness (supersedes the Taylor & Francis-only browser pass). The journal set is still `editors_abs_ajg_gap_20261025`. Fourteen drop-quality chrome rows stay out.

Current boards for AJG journals that are not already in the FT50 or ABDC editor freezes:

| File | Panel | Rows | Empty `editor_name` | Journals |
|------|--------|-----:|--------------------:|---------:|
| `editors_abs_ajg_gap_prio43_current.csv` | AJG 4*, 4, and 3 | 3,166 | 0 | 46 (9 grade 4, 37 grade 3; no 4* left outside FT50/ABDC) |
| `editors_abs_ajg_gap_ajg2_current.csv` | AJG 2 | 4,983 | 0 | 105 |
| `editors_abs_ajg_gap_ajg1_current.csv` | AJG 1 | 11,218 | 0 | 289 |

Notes: `releases/current/RELEASE_NOTES.md`.

Excluded: collector `raw/`, QC logs, and the browser-scrape audit CSVs.

## Scope

One current snapshot, not a multi-year panel. Grades on the public directory come from the journal’s 2024 title in `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`, and they must sit in the panel above. These files do not add FT50 or ABDC badges.

`editor_name` is the name the directory shows. Empty `editor_name` is 0. Sociology of Health and Illness is 56 rows. `ror_id` is filled on 15,636 of 16,059 nonempty affiliations (97.4%): ajg1 8,456/8,665 (97.6%), ajg2 4,524/4,678 (96.7%), prio43 2,656/2,716 (97.8%). High or medium confidence only. `faculty_profile_url` is not on these files. Eight prio43 rows whose name is `Email` stay out of the directory. A bare country is not an institution.

The full Academic Journal Guide is still larger than the boards in the directory. Rankings keeps every AJG title.
