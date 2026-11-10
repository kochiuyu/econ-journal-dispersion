# Editors — ABS/AJG gap

Updated: 2026-11-10 (Asia/Taipei)

## Release in this repo

`releases/current/` — Freeze `editors_edpacs_marks_country_fix_20261110` (published 2026-11-10) is the current board. It supersedes `editors_paren_num_leftover_fix_20261110`; the three AJG-gap files are unchanged (the fix is ABDC C only). In `editors_paren_num_leftover_fix_20261110` only ajg1 changed: GGSIPU Periyar (`editors_abs_ajg_gap_ajg1_current#7504`) is rematched to Guru Gobind Singh Indraprastha University `034q1za58`, with the printed text kept. In `editors_tokyo_other_inst_fix_20261110` these three files were unchanged from `editors_tokyo_gatech_fix_20261110` (the fix is ABDC-only). In `editors_tokyo_gatech_fix_20261110`, which it supersedes, University of Tokyo seats are rematched to `057zh3y96` (prio43 1, ajg2 2, ajg1 3); printed `raw_affiliation` kept. The twelve ajg1 navigation rows (including Vincent Pan) and the two ajg2 Policy Design and Practice navigation rows stay out. Twelve columns follow `board_urls` and `board_url_count` (see `docs/README.md`). Emails and phone numbers left in text cells were already removed in the consistency3b Directory copy and were not reintroduced. Long table and the change log: `data/editors/releases/editors_edpacs_marks_country_fix_20261110/`. Reports: `docs/reports/`. Details: `releases/current/RELEASE_NOTES.md`. The history below describes earlier freezes.

Previous: freeze `editors_ror_consistency3b_20261101` (published 2026-11-01). Then: freeze `editors_browser_single_20261029` (2026-10-30 07:09 Asia/Taipei). It supersedes `editors_single_editor_20261029`, which superseded `editors_browser_boards_20261029`. These three files are unchanged in `editors_browser_single_20261029`; its board changes are on ABDC A and C. Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. African Affairs is still the 2024-04-27 Wayback board (40 rows; live OUP is Cloudflare-blocked). Nature Human Behaviour `Email` and `Biography` rows stay out. The journal set is still `editors_abs_ajg_gap_20261025`. Fourteen drop-quality chrome rows stay out, and the navigation rows the collector put back stay out. Small Business International Review stays parked.

Current boards for AJG journals that are not already in the FT50 or ABDC editor freezes:

| File | Panel | Rows | Empty `editor_name` | `faculty_profile_url` | Journals |
|------|--------|-----:|--------------------:|----------------------:|---------:|
| `editors_abs_ajg_gap_prio43_current.csv` | AJG 4*, 4, and 3 | 3,104 | 3 | 82 | 46 (9 grade 4, 37 grade 3; no 4* left outside FT50/ABDC) |
| `editors_abs_ajg_gap_ajg2_current.csv` | AJG 2 | 5,462 | 0 | 386 | 105 |
| `editors_abs_ajg_gap_ajg1_current.csv` | AJG 1 | 12,316 | 15 | 615 | 289 |

Notes: `releases/current/RELEASE_NOTES.md`.

Excluded: collector `raw/`, QC logs, and the browser-scrape audit CSVs.

## Scope

One current snapshot, not a multi-year panel. Grades on the public directory come from the journal’s 2024 title in `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`, and they must sit in the panel above. These files do not add FT50 or ABDC badges.

`ror_id` in `editors_edpacs_marks_country_fix_20261110` (unchanged from `editors_paren_num_leftover_fix_20261110`): prio43 2,546 of 2,723 nonempty affiliations, ajg2 4,746 of 5,224, ajg1 8,698 of 9,997.

As of `editors_browser_single_20261029`: `editor_name` is the name the directory shows. Empty `editor_name` is 3 on prio43, 0 on ajg2, and 16 on ajg1. African Affairs is 40 rows. `faculty_profile_url` is filled on 1,084 of 19,630 published rows (prio43 82, ajg2 386, ajg1 616). Vincent Pan on Advances in Decision Sciences stays out. Rows with no `raw_affiliation` are 3,021. A faculty URL with a blank affiliation is 3 (prio43 1, ajg1 2). A faculty URL with no `ror_id` is 16. `ror_id` is filled on 15,850 of 16,609 nonempty affiliations (95.4%): ajg1 8,625/9,159 (94.2%), ajg2 4,574/4,727 (96.8%), prio43 2,651/2,723 (97.4%). High or medium confidence only. This publish replaces ajg1 rows on six journals (21 to 321). prio43 and ajg2 are unchanged. Twelve navigation rows in the collector ajg1 file stay out. Small Business International Review stays parked. `board_urls` is filled on PASOS Journal of Tourism and Cultural Heritage. A bare country is not an institution. No name, ROR id, affiliation, or faculty URL was invented. The added `ror_id` values were already on these boards. `11KBW`, UNSW Sydney, and INSEAD stay.

The full Academic Journal Guide is still larger than the boards in the directory. Rankings keeps every AJG title.
