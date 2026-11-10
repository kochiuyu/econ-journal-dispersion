# Editors — ABDC

Updated: 2026-11-10 (Asia/Taipei)

## Release in this repo

`releases/current/` — current boards by ABDC rating. Freeze `editors_weird_inst_fix_20261110` (published 2026-11-10) is the current board. It supersedes `editors_country_misprint_fix_20261110`: weird Institution-name fix (A* 117, A 352, B 350, C 427 rows; `ror_id` A* 23,406, A 40,588, B 36,963, C 21,567; DROP rows have `raw_affiliation` blanked with the printed text in `ror_notes`). In `editors_country_misprint_fix_20261110`: It supersedes `editors_trailing_country_fix_20261110`: country-misprint and fragment-name fix (A* 2, A 13, B 14, C 10 rows; C `ror_id` 21,552 (was 21,551).). In `editors_trailing_country_fix_20261110`: It supersedes `editors_raw_aff_part_no_fix_20261110`. Trailing printed countries are stripped from `canonical_name` and written to `ror_country` / `continent` on A* 273, A 1,096, B 1,682 and C 1,728 rows (printed `raw_affiliation` kept; REVIEW/KEEP names and 11 dangling-`and` rows held back). `ror_id` B 36,946 (was 36,945), C 21,551 (was 21,550) from REMATCH to existing twins. In `editors_raw_aff_part_no_fix_20261110` the four ABDC files were unchanged; only the long table changes (`raw_aff_part` `no` blanked on 9,695 parts). In `editors_edpacs_marks_country_fix_20261110` only C changed: Norman Marks' printed bio (#12402) is blanked from `raw_affiliation` with the original kept in `ror_notes`, and Aditya Birla Group (#12412) gets India / Asia and New York State Comptroller (#12391) United States / North America (no ROR). C `raw_affiliation` 24,844 (was 24,845); `ror_id` unchanged. In `editors_paren_num_leftover_fix_20261110`, which it supersedes, the freeze fixed the user-approved parenthesis- and number-start leftovers on A and C:
- A: Hengeler Mueller.
- C: nine EDPACS organisation-only names, Norman Marks' cleaned name dropped, and Égert to OECD `0438wbg98`.

It also appends a note on the 12 Tokyo Institute of Technology / Kojima seats. In `editors_tokyo_other_inst_fix_20261110`, which it supersedes, the fix gave 35 bare-`Tokyo` seats (A* 1, A 7, B 13, C 14) their printed Tokyo institution: 23 rematched, 11 Tokyo Institute of Technology with blank ROR, and Kojima's printed `Tokyo` unmatched. Before that, `editors_tokyo_gatech_fix_20261110`: A*, A, B, and C are patched for a keyed fix: University of Tokyo seats rematched to `057zh3y96` (A* 4, A 5, B 5, C 3) and the Decision Sciences `Georgia Inst of Technology` seat rematched to `01zkghx44` (A*); printed `raw_affiliation` kept. No site filter. Twelve columns follow `board_urls` and `board_url_count` (see `docs/README.md`). Emails and phone numbers left in text cells were already removed in the consistency3b Directory copy; those restorations stay. Long table and the change log: `data/editors/releases/editors_weird_inst_fix_20261110/`. Reports: `docs/reports/`. Details: `releases/current/RELEASE_NOTES.md`. The history below describes earlier freezes.

Previous: freeze `editors_ror_consistency3b_20261101` (published 2026-11-01). Then: freeze `editors_browser_single_20261029` (2026-10-30 07:09 Asia/Taipei). It supersedes `editors_single_editor_20261029`, which superseded `editors_browser_boards_20261029`. Faculty URLs from `editors_nonft50_url_aff_20261028` stay. 

| File | Rating | Rows | Empty `editor_name` | `faculty_profile_url` | `raw_affiliation` | `ror_id` |
|------|--------|-----:|--------------------:|----------------------:|------------------:|---------:|
| `editors_abdc_a_star_current.csv` | A* | 25,596 | 1 | 12,522 (48.9%) | 24,202 (94.6%) | 23,399 |
| `editors_abdc_a_current.csv` | A | 45,889 | 1 | 6,236 (13.6%) | 43,159 (94.0%) | 40,578 |
| `editors_abdc_b_current.csv` | B | 42,558 | 11 | 3,509 (8.2%) | 40,187 (94.4%) | 36,946 |
| `editors_abdc_c_current.csv` | C | 27,719 | 6 | 1,379 (5.0%) | 24,844 (89.6%) | 21,551 |

Excluded: `*.before_ror.csv`, `*.before_url_aff_nonft50_20261028`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Freeze `editors_browser_single_20261029` adds browser-captured fuller boards on Journal of Derivatives (A, 1 to 18), Journal of Portfolio Management (A, 1 to 73), and Arts and the Market (C, 1 to 55): 143 new rows, 60 with a ROR id reused from these panels or the crosswalk. `ror_id` on A is now 42,088 and on C 23,226. `board_urls` is filled on the two pm-research journals. A*, B, and every other row are as published in `editors_single_editor_20261029`.

Freeze `editors_single_editor_20261029` replaced heading and navigation rows and expands journals that had a single editor row. On these files that is A 2 rows to 411, B 13 rows to 219, and C 12 rows to 309. A* is unchanged. Other rows stay as published in `editors_apjiht_board_fix_20261029`, including the eight-journal board fix and the place-suffix and country corrections. Rematches on the new rows use a ROR id already on these boards, or one exact crosswalk hit. `ror_id` is 23,600 / 42,065 / 38,876 / 23,189. The one id that was not already on these boards is Galgotias College of Engineering & Technology, `https://ror.org/04a85ht85`. Sam Kirshner stays UNSW Sydney (`https://ror.org/03r8z3t63`) and Kai Hockerts stays INSEAD (`https://ror.org/05ynf4333`). Faculty URL counts stay A* 12,523, A 6,237, B 3,509, and C 1,379. Empty `editor_name` is 2 on A*, 1 on A, 0 on B, and 11 on C. A faculty URL with no `ror_id` is 67 on A*, 50 on A, 21 on B, and 4 on C. `board_urls` is filled on IEEE Transactions on Intelligent Transportation Systems, Acta Turistica, and Management: Journal of Contemporary Management Issues. University of Goma and EAE Business School stay held on the Journal of Marketing Research seats. `11KBW` stays on two Public Law rows. UNSW Sydney and INSEAD stay. The directory does not list a blank name. A bare country is not an institution. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
