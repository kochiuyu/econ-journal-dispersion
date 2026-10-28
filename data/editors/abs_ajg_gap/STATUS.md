# Editors — ABS/AJG gap

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — URL-to-university chase is freeze `editors_ajg_gap_url_aff_20261028` (2026-10-28 15:05 Asia/Hong_Kong). That supersedes `editors_ajg_gap_faculty_remiss_20261028`. Names on ajg1 and ajg2 are still `editors_blank_rescrape_20261028`. Sociology of Health and Illness on prio43 is still `editors_blank_rescrape_browser_20261028`. The journal set is still `editors_abs_ajg_gap_20261025`. Fourteen drop-quality chrome rows stay out.

Current boards for AJG journals that are not already in the FT50 or ABDC editor freezes:

| File | Panel | Rows | Empty `editor_name` | `faculty_profile_url` | Journals |
|------|--------|-----:|--------------------:|----------------------:|---------:|
| `editors_abs_ajg_gap_prio43_current.csv` | AJG 4*, 4, and 3 | 3,166 | 0 | 102 | 46 (9 grade 4, 37 grade 3; no 4* left outside FT50/ABDC) |
| `editors_abs_ajg_gap_ajg2_current.csv` | AJG 2 | 4,983 | 0 | 386 | 105 |
| `editors_abs_ajg_gap_ajg1_current.csv` | AJG 1 | 11,218 | 0 | 616 | 289 |

Notes: `releases/current/RELEASE_NOTES.md`.

Excluded: collector `raw/`, QC logs, and the browser-scrape audit CSVs.

## Scope

One current snapshot, not a multi-year panel. Grades on the public directory come from the journal’s 2024 title in `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`, and they must sit in the panel above. These files do not add FT50 or ABDC badges.

`editor_name` is the name the directory shows. Empty `editor_name` is 0. Sociology of Health and Illness is 56 rows. `faculty_profile_url` is filled on 1,104 of 19,367 published rows (prio43 102, ajg2 386, ajg1 616). The collector file has 1,105 URLs; Vincent Pan on Advances in Decision Sciences stays out with the other thirteen chrome rows. Rows with no `raw_affiliation` are 2,894. A faculty URL with no university is 0 (was 53). A faculty URL with no `ror_id` is 0 (was 62). Host-map fills are 59, ROR rematches on an existing affiliation are 3, and 3 junk URLs were cleared. `ror_id` is filled on 16,056 of 16,473 nonempty affiliations (97.5%): ajg1 8,694/8,899 (97.7%), ajg2 4,653/4,805 (96.8%), prio43 2,709/2,769 (97.8%). High or medium confidence only. Eight prio43 rows whose name is `Email` stay out of the directory. A bare country is not an institution. No name, ROR id, affiliation, or faculty URL was invented.

The full Academic Journal Guide is still larger than the boards in the directory. Rankings keeps every AJG title.
