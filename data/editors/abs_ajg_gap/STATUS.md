# Editors — ABS/AJG gap

Updated: 2026-10-29 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — freeze `editors_apjiht_board_fix_20261029` (2026-10-29 22:28 Asia/Taipei). It supersedes `editors_institution_country_place_20261029`. Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. African Affairs is still the 2024-04-27 Wayback board (40 rows; live OUP is Cloudflare-blocked). Nature Human Behaviour `Email` and `Biography` rows stay out. The journal set is still `editors_abs_ajg_gap_20261025`. Fourteen drop-quality chrome rows stay out, and the navigation rows the collector put back stay out.

Current boards for AJG journals that are not already in the FT50 or ABDC editor freezes:

| File | Panel | Rows | Empty `editor_name` | `faculty_profile_url` | Journals |
|------|--------|-----:|--------------------:|----------------------:|---------:|
| `editors_abs_ajg_gap_prio43_current.csv` | AJG 4*, 4, and 3 | 3,104 | 3 | 82 | 46 (9 grade 4, 37 grade 3; no 4* left outside FT50/ABDC) |
| `editors_abs_ajg_gap_ajg2_current.csv` | AJG 2 | 4,982 | 0 | 386 | 105 |
| `editors_abs_ajg_gap_ajg1_current.csv` | AJG 1 | 11,244 | 18 | 616 | 289 |

Notes: `releases/current/RELEASE_NOTES.md`.

Excluded: collector `raw/`, QC logs, and the browser-scrape audit CSVs.

## Scope

One current snapshot, not a multi-year panel. Grades on the public directory come from the journal’s 2024 title in `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`, and they must sit in the panel above. These files do not add FT50 or ABDC badges.

`editor_name` is the name the directory shows. Empty `editor_name` is 3 on prio43, 0 on ajg2, and 18 on ajg1. African Affairs is 40 rows. `faculty_profile_url` is filled on 1,084 of 19,330 published rows (prio43 82, ajg2 386, ajg1 616). Vincent Pan on Advances in Decision Sciences stays out. Rows with no `raw_affiliation` are 3,037. A faculty URL with a blank affiliation is 3 (prio43 1, ajg1 2). A faculty URL with no `ror_id` is 16. `ror_id` is filled on 15,715 of 16,293 nonempty affiliations (96.5%): ajg1 8,490/8,843 (96.0%), ajg2 4,574/4,727 (96.8%), prio43 2,651/2,723 (97.4%). High or medium confidence only. This publish replaces ajg1 rows on three journals (7 to 34). prio43 and ajg2 are unchanged. Twelve navigation rows in the collector ajg1 file stay out. A bare country is not an institution. No name, ROR id, affiliation, or faculty URL was invented. The 12 new `ror_id` values were already on these boards. `11KBW`, UNSW Sydney, and INSEAD stay.

The full Academic Journal Guide is still larger than the boards in the directory. Rankings keeps every AJG title.
