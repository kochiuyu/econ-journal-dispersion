# Editors — ABS/AJG gap

Updated: 2026-10-29 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — freeze `editors_institution_country_place_20261029` (2026-10-29 00:37 Asia/Hong_Kong). It supersedes `editors_institution_residual_post35_20261028` for Directory Institutions. Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. African Affairs is still the 2024-04-27 Wayback board (40 rows; live OUP is Cloudflare-blocked). Nature Human Behaviour `Email` and `Biography` rows stay out. The journal set is still `editors_abs_ajg_gap_20261025`. Fourteen drop-quality chrome rows stay out, and the navigation rows the collector put back stay out.

Current boards for AJG journals that are not already in the FT50 or ABDC editor freezes:

| File | Panel | Rows | Empty `editor_name` | `faculty_profile_url` | Journals |
|------|--------|-----:|--------------------:|----------------------:|---------:|
| `editors_abs_ajg_gap_prio43_current.csv` | AJG 4*, 4, and 3 | 3,104 | 3 | 82 | 46 (9 grade 4, 37 grade 3; no 4* left outside FT50/ABDC) |
| `editors_abs_ajg_gap_ajg2_current.csv` | AJG 2 | 4,982 | 0 | 386 | 105 |
| `editors_abs_ajg_gap_ajg1_current.csv` | AJG 1 | 11,217 | 19 | 616 | 289 |

Notes: `releases/current/RELEASE_NOTES.md`.

Excluded: collector `raw/`, QC logs, and the browser-scrape audit CSVs.

## Scope

One current snapshot, not a multi-year panel. Grades on the public directory come from the journal’s 2024 title in `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`, and they must sit in the panel above. These files do not add FT50 or ABDC badges.

`editor_name` is the name the directory shows. Empty `editor_name` is 3 on prio43, 0 on ajg2, and 19 on ajg1. African Affairs is 40 rows. `faculty_profile_url` is filled on 1,084 of 19,303 published rows (prio43 82, ajg2 386, ajg1 616). Vincent Pan on Advances in Decision Sciences stays out. Rows with no `raw_affiliation` are 3,044. A faculty URL with a blank affiliation is 3 (prio43 1, ajg1 2). A faculty URL with no `ror_id` is 16. `ror_id` is filled on 15,703 of 16,259 nonempty affiliations (96.6%): ajg1 8,478/8,809 (96.3%), ajg2 4,574/4,727 (96.8%), prio43 2,651/2,723 (97.4%). High or medium confidence only. This publish changes prio43 8, ajg2 2, and ajg1 2 rows. A place suffix is stripped. A bare country is not an institution. No name, ROR id, affiliation, or faculty URL was invented. Ian Martin Johnson’s Aberdeen Business School masthead is Robert Gordon University (`https://ror.org/04f0qj703`, United Kingdom). Adelaide University variants use `https://ror.org/028g18b61`, already on these boards. Mahmoud Rajablu is `Canadian Business Success Centre (CBSC)`, country Canada. Weiru Chen is `Alibaba Group`, country China. Jack T Boorman’s institution is `IMF's Independent Evaluation Office`. A. Berland Inc. is blank. `11KBW`, UNSW Sydney, and INSEAD stay.

The full Academic Journal Guide is still larger than the boards in the directory. Rankings keeps every AJG title.
