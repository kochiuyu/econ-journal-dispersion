# Editors — ABDC

Updated: 2026-11-10 (Asia/Taipei)

## Release in this repo

`releases/current/` — current boards by ABDC rating. Freeze `editors_inst_drop_rematch_20261110` (published 2026-11-10) is the current board. It supersedes `editors_nonlatin_inst_20261110`. A*, A, B, and C are patched for DROP + REMATCH affiliation cleanup (junk bios and address lines blanked; singleton variants rematched onto existing panel ROR twins; printed `raw_affiliation` kept). No site filter. Twelve columns follow `board_urls` and `board_url_count` (see `docs/README.md`). Emails and phone numbers left in text cells were already removed in the consistency3b Directory copy; those restorations stay. Long table and the change log: `data/editors/releases/editors_inst_drop_rematch_20261110/`. Reports: `docs/reports/`. Details: `releases/current/RELEASE_NOTES.md`. The history below describes earlier freezes.

Previous: freeze `editors_ror_consistency3b_20261101` (published 2026-11-01). Then: freeze `editors_browser_single_20261029` (2026-10-30 07:09 Asia/Taipei). It supersedes `editors_single_editor_20261029`, which superseded `editors_browser_boards_20261029`. Faculty URLs from `editors_nonft50_url_aff_20261028` stay. 

| File | Rating | Rows | Empty `editor_name` | `faculty_profile_url` | `raw_affiliation` | `ror_id` |
|------|--------|-----:|--------------------:|----------------------:|------------------:|---------:|
| `editors_abdc_a_star_current.csv` | A* | 25,596 | 1 | 12,522 (48.9%) | 24,202 (94.6%) | 23,306 |
| `editors_abdc_a_current.csv` | A | 45,889 | 1 | 6,236 (13.6%) | 43,159 (94.0%) | 40,480 |
| `editors_abdc_b_current.csv` | B | 42,558 | 11 | 3,509 (8.2%) | 40,190 (94.4%) | 36,842 |
| `editors_abdc_c_current.csv` | C | 27,719 | 6 | 1,379 (5.0%) | 24,851 (89.7%) | 21,458 |

Excluded: `*.before_ror.csv`, `*.before_url_aff_nonft50_20261028`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Freeze `editors_browser_single_20261029` adds browser-captured fuller boards on Journal of Derivatives (A, 1 to 18), Journal of Portfolio Management (A, 1 to 73), and Arts and the Market (C, 1 to 55): 143 new rows, 60 with a ROR id reused from these panels or the crosswalk. `ror_id` on A is now 42,088 and on C 23,226. `board_urls` is filled on the two pm-research journals. A*, B, and every other row are as published in `editors_single_editor_20261029`.

Freeze `editors_single_editor_20261029` replaced heading and navigation rows and expands journals that had a single editor row. On these files that is A 2 rows to 411, B 13 rows to 219, and C 12 rows to 309. A* is unchanged. Other rows stay as published in `editors_apjiht_board_fix_20261029`, including the eight-journal board fix and the place-suffix and country corrections. Rematches on the new rows use a ROR id already on these boards, or one exact crosswalk hit. `ror_id` is 23,600 / 42,065 / 38,876 / 23,189. The one id that was not already on these boards is Galgotias College of Engineering & Technology, `https://ror.org/04a85ht85`. Sam Kirshner stays UNSW Sydney (`https://ror.org/03r8z3t63`) and Kai Hockerts stays INSEAD (`https://ror.org/05ynf4333`). Faculty URL counts stay A* 12,523, A 6,237, B 3,509, and C 1,379. Empty `editor_name` is 2 on A*, 1 on A, 0 on B, and 11 on C. A faculty URL with no `ror_id` is 67 on A*, 50 on A, 21 on B, and 4 on C. `board_urls` is filled on IEEE Transactions on Intelligent Transportation Systems, Acta Turistica, and Management: Journal of Contemporary Management Issues. University of Goma and EAE Business School stay held on the Journal of Marketing Research seats. `11KBW` stays on two Public Law rows. UNSW Sydney and INSEAD stay. The directory does not list a blank name. A bare country is not an institution. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
