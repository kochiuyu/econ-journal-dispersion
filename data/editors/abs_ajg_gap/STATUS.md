# Editors — ABS/AJG gap

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — freeze `editors_institution_nonsense_20261028` (2026-10-28 15:34 Asia/Hong_Kong). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay on rows this freeze did not replace. African Affairs is the 2024-04-27 Wayback board (40 rows; live OUP is Cloudflare-blocked). Nature Human Behaviour `Email` and `Biography` rows are out. The journal set is still `editors_abs_ajg_gap_20261025`. Fourteen drop-quality chrome rows stay out, and the navigation rows this freeze put back stay out.

Current boards for AJG journals that are not already in the FT50 or ABDC editor freezes:

| File | Panel | Rows | Empty `editor_name` | `faculty_profile_url` | Journals |
|------|--------|-----:|--------------------:|----------------------:|---------:|
| `editors_abs_ajg_gap_prio43_current.csv` | AJG 4*, 4, and 3 | 3,104 | 0 | 82 | 46 (9 grade 4, 37 grade 3; no 4* left outside FT50/ABDC) |
| `editors_abs_ajg_gap_ajg2_current.csv` | AJG 2 | 4,982 | 0 | 386 | 105 |
| `editors_abs_ajg_gap_ajg1_current.csv` | AJG 1 | 11,217 | 0 | 616 | 289 |

Notes: `releases/current/RELEASE_NOTES.md`.

Excluded: collector `raw/`, QC logs, and the browser-scrape audit CSVs.

## Scope

One current snapshot, not a multi-year panel. Grades on the public directory come from the journal’s 2024 title in `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`, and they must sit in the panel above. These files do not add FT50 or ABDC badges.

`editor_name` is the name the directory shows. Empty `editor_name` is 0. Sociology of Health and Illness is unchanged by this freeze. African Affairs is 40 rows (was 86). `faculty_profile_url` is filled on 1,084 of 19,303 published rows (prio43 82, ajg2 386, ajg1 616). Vincent Pan on Advances in Decision Sciences stays out, including the collector URL that pointed at UNSW and a Geneva business-school ROR. Rows with no `raw_affiliation` are 2,874. A faculty URL with no university is 0. A faculty URL with no `ror_id` is 0. `ror_id` is filled on 16,042 of 16,429 nonempty affiliations (97.6%): ajg1 8,692/8,895 (97.7%), ajg2 4,650/4,788 (97.1%), prio43 2,700/2,746 (98.3%). High or medium confidence only. `Email` and `Biography` rows are no longer in the prio43 file. A bare country is not an institution. No name, ROR id, affiliation, or faculty URL was invented.

The full Academic Journal Guide is still larger than the boards in the directory. Rankings keeps every AJG title.
