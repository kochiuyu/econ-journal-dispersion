# editors_edpacs_marks_country_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_paren_num_leftover_fix_20261110` (Directory PR #50) for the Directory current panels. It is a keyed, user-approved follow-up on three ABDC C EDPACS seats. No ROR ids change and there is no site filter. The long table and change log are in `data/editors/releases/editors_edpacs_marks_country_fix_20261110/`. Report: `docs/reports/EDPACS_MARKS_COUNTRY_FIX_20261110.md`.

The three AJG-gap files are unchanged.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,434 (6,387 with a ROR id), were 15,435 / 6,387. Countries stay 159. 12,067 appointments have no institution (was 12,066: Marks' seat no longer falls back to his printed bio). Shared display names stay 69. The only parenthesis- and number-start Institutions left are the 14 kept numbered organisations.

## Previous freeze: editors_paren_num_leftover_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_tokyo_other_inst_fix_20261110` (Directory PR #49) for the Directory current panels. It is a keyed, user-approved fix for the parenthesis- and number-start Institutions left as REVIEW. Only institution fields are changed, the printed `raw_affiliation` is kept, and the guardrail and history notes stay in `ror_notes` with a `paren_num_leftover_fix_20261110:` token appended. No new ROR ids and no site filter. The long table and change log are in `data/editors/releases/editors_paren_num_leftover_fix_20261110/`. Report: `docs/reports/PAREN_NUM_LEFTOVER_FIX_20261110.md`.

`editors_abs_ajg_gap_ajg1_current#7504` (Neha Gangwar, `(GGSIPU) Periyar Management and Computer College, India`) is rematched to Guru Gobind Singh Indraprastha University `https://ror.org/034q1za58`, which was already on 3 panel rows. ajg1 `ror_id` 8,698 (was 8,697). ajg1 stays 12,316 rows: the collector file's ten extra navigation keys stay out. prio43 and ajg2 are unchanged.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,435 (6,387 with a ROR id), were 15,438 / 6,387. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The remaining parenthesis- and number-start Institutions are the 14 kept numbered organisations, plus Norman Marks' printed bio, which still shows through the printed-text fallback.

## Previous freeze: editors_tokyo_other_inst_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_tokyo_gatech_fix_20261110` (Directory PR #48) for the Directory current panels. It is a keyed ABDC-only fix for the 35 seats whose `canonical_name` was the bare `Tokyo` with a blank ROR. The collector's copies of those seats had the place-strip rewrite `Italian Cultural Institute`, and the Directory guardrail had already restored the printed text. The three AJG-gap files are unchanged. There is no site filter. The long table and change log are in `data/editors/releases/editors_tokyo_other_inst_fix_20261110/`. Report: `docs/reports/TOKYO_OTHER_INST_FIX_20261110.md`.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,438 (6,387 with a ROR id), were 15,432 / 6,381. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The unmatched `Tokyo` (Japan) Institutions row falls from 35 appointments to 1.

## Previous freeze: editors_tokyo_gatech_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_inst_punct_split_20261110` (Directory PR #47) for the Directory current panels. It is a keyed panel-only fix on the AJG-gap files. It rematches University of Tokyo seats whose ROR the Directory guardrail (`directory_guardrail_restore_20261101`) had left blank to The University of Tokyo `https://ror.org/057zh3y96`, and rematches the Decision Sciences `Georgia Inst of Technology` seat to `https://ror.org/01zkghx44`. The printed `raw_affiliation` is kept, and the Directory guardrail note stays in `ror_notes` with the fix token appended. There is no site filter. The long table and change log are in `data/editors/releases/editors_tokyo_gatech_fix_20261110/`. Report: `docs/reports/TOKYO_GATECH_FIX_20261110.md`.

| File | Rows | Rows patched | `ror_id` (was) |
|---|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 1 | 2,546 (2,545) |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,462 | 2 | 4,746 (4,744) |
| `editors_abs_ajg_gap_ajg1_current.csv` | 12,316 | 3 | 8,697 (8,694) |

The ajg1 / ajg2 navigation rows stay out. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,432 (6,381 with a ROR id), were 15,434 / 6,381. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The University of Tokyo is one Institutions row (`057zh3y96`, 173 appointments); `Georgia Inst of Technology` is no longer a separate unmatched row.

## Previous freeze: editors_inst_punct_split_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_inst_drop_rematch_20261110` (Directory PR #46) for the Directory current panels. It is a panel-only Institutions cleanup on the AJG-gap files: leftover punctuation-start junk is blanked (DROP), high-confidence name splits are rematched onto existing panel ROR twins (REMATCH; printed `raw_affiliation` kept; `canonical_name` set to the twin `ror_name`), and three name-only variants are unified with a blank ROR (UNIFY). REVIEW and KEEP flags were excluded. There is no site filter in `scripts/build_site.py`. The long table and change log are in `data/editors/releases/editors_inst_punct_split_20261110/`. Report: `docs/reports/INST_PUNCT_SPLIT_20261110.md`.

**What changed.** All three AJG-gap current panels are patched by the collector delta applied onto the published Directory copy of `editors_inst_drop_rematch_20261110` (prio43 9, ajg2 14, ajg1 51 REMATCH rows; no DROP or UNIFY). The twelve ajg1 navigation rows (including Vincent Pan) and the two ajg2 Policy Design and Practice navigation rows stay out; the collector ajg1 file still has ten of those extra keys, which were not added. Published ajg1 remains 12,316 and ajg2 remains 5,462.

| File | Rows | `ror_id` (was) | Nonempty `raw_affiliation` | Empty `editor_name` |
|---|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 2,545 (2,536) | 2,723 | 3 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,462 | 4,744 (4,730) | 5,224 | 0 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 12,316 | 8,694 (8,643) | 9,997 | 15 |

`faculty_profile_url` stays prio43 82, ajg2 386, ajg1 615. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,434 (6,381 with a ROR id), were 15,612 / 6,381. Countries stay 159. 12,066 appointments have no institution (were 12,052). Shared display names 69 (were 125).

## Previous freeze: editors_inst_drop_rematch_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_nonlatin_inst_20261110` (Directory PR #45) for the Directory current panels. It is a panel-only Institutions cleanup on the AJG-gap files (DROP junk bios and address lines; REMATCH singleton variants onto existing panel ROR twins; printed `raw_affiliation` kept). REVIEW and KEEP flags were excluded. There is no site filter in `scripts/build_site.py`. The long table and change log are in `data/editors/releases/editors_inst_drop_rematch_20261110/`. Report: `docs/reports/INST_DROP_REMATCH_20261110.md`.

**What changed.** All three AJG-gap current panels are patched by the collector delta applied onto the published Directory copy of `editors_nonlatin_inst_20261110`. The twelve ajg1 navigation rows (including Vincent Pan) and the two ajg2 Policy Design and Practice navigation rows stay out; the collector ajg1 file still has ten of those extra keys, which were not added. Directory guardrail restores and contact scrub stay. Published ajg1 remains 12,316 and ajg2 remains 5,462. One GAP row, `The Universidad Nacional Experimental Politécnica`, keeps its printed name and a blank ROR.

| File | Rows | `ror_id` (was) | Nonempty `raw_affiliation` (was) | Empty `editor_name` |
|---|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 2,536 (2,534) | 2,723 (2,723) | 3 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,462 | 4,730 (4,686) | 5,224 (5,224) | 0 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 12,316 | 8,643 (8,454) | 9,997 (9,998) | 15 |

`faculty_profile_url` stays prio43 82, ajg2 386, ajg1 615. `11KBW`, UNSW Sydney, and INSEAD stay. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,612 (6,381 with a ROR id), were 16,234 / 6,381. Countries stay 159. 12,052 appointments have no institution (were 11,991).

## Previous freeze: editors_nonlatin_inst_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_ror_consistency3b_20261101` (Directory PR #41) for the Directory current panels. The files in this folder are unchanged. The only panel edit is on ABDC C (19 bio/CV blurbs blanked, 60 rematches onto existing Latin ROR twins, printed non-Latin names kept). Long table: `data/editors/releases/editors_nonlatin_inst_20261110/editor_affiliations.csv.gz`. Report: `docs/reports/NONLATIN_INST_20261110.md`.

## Previous freeze: editors_ror_consistency3b_20261101

Published 2026-11-01 (Asia/Hong_Kong) with user approval. This supersedes `editors_browser_single_20261029` (Directory PR #40). The collector packs between the two (`editors_ror_consistency2`, `editors_ror_consistency`, `editors_ror_multiaff`, `editors_ror_campus2`, `editors_ror_campus`, `post15`, the profile `pilot`, the scale-parse packs, and the t39 / institution-fix freezes) were never published and are retired. The long table and audit logs are in `data/editors/releases/editors_ror_consistency3b_20261101/`; reports in `docs/reports/` (`PREPUBLISH_CHECK_20261101.md`, `ROR_PREPUBLISH_FIX_20261101.md`, `ROR_CONSISTENCY3_20261101.md`). The core49 backfill `editors_backfill_scale_ror_20261031` is pinned at the same time under `data/editors/core49/releases/`.

**Columns.** After `board_urls` and `board_url_count` every panel adds `board_status`, `tenure_start_year`, `tenure_end_year`, `snapshot_date`, `snapshot_source`, `board_year`, `editor_row_key`, `affiliation_count`, `ror_id_aff_rank`, `primary_aff_basis`, `former_flag`, and `other_ror_ids`. The slim `editors_ft50_current.csv` also gains `ror_id`, `ror_name`, `ror_country`, and `continent`. The board columns are no longer the last two. A single `board_urls` entry may now appear on any journal.

**ROR.** The collector blanks a ROR id when the masthead text cannot be matched to one organization without guessing (strict matching, multi-affiliation parsing, campus splits). So `ror_id` coverage is lower than in `editors_browser_single_20261029` on every panel except ajg2, and a few correct ids were blanked as ambiguous. Nothing was invented. Display affiliation is still `ror_name`, then `canonical_name`, then `raw_affiliation`; country is `ror_country`.

**Directory guardrails kept.** The twelve ajg1 navigation rows (including Vincent Pan on Advances in Decision Sciences) and the two ajg2 Policy Design and Practice navigation rows stay out. Collector institution-string rewrites that were wrong (for example Tokyo mastheads rewritten to `Italian Cultural Institute`, and HKUST (Guangzhou) collapsed onto HKUST) are reverted to the published text: 95 rows plus two `editor_name_raw` restores, listed in `DIRECTORY_GUARDRAILS_restored_rows_20261101.csv`. `11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate; ESSEC is France `02dga6j42`. A blank or country-only affiliation is not an institution. Emails and phone or fax numbers that the collector left in text cells (mostly `source_note`) were removed.

**Directory.** Appointments 162,575 (were 160,104). Editors 112,718 (were 111,229). Journals 2,853. Institutions 16,283 rows, 6,381 with a ROR id (were 11,344 / 8,665). 11,972 appointments have no institution; 650 country-only, 12 bracket-only, and 7 address-only appointments stay off Institutions. Countries 159 (were 175).

| File | Rows (was) | `ror_id` (was) | Empty `editor_name` |
|---|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 (3,104) | 2,534 (2,651) | 3 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,462 (4,982) | 4,686 (4,574) | 0 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 12,316 (11,544) | 8,454 (8,625) | 15 |

Ten ajg1 rows in the collector file are removed here (the navigation keys plus a blank Journal of Information Technology Management row); the build name filter drops the rest. Contact text removed from ajg1 30 and ajg2 6 cells.

## Previous freeze: editors_browser_single_20261029

Frozen 2026-10-30 07:09 Asia/Taipei. This supersedes `editors_single_editor_20261029` (Directory PR #39). The collector added browser-captured boards on three ABDC journals: Journal of Derivatives (A, 1 to 18), Journal of Portfolio Management (A, 1 to 73), and Arts and the Market (C, 1 to 55). The three AJG-gap files are unchanged in this publish. The collector copies are byte-identical to `editors_single_editor_20261029`. See `data/editors/abdc/releases/current/RELEASE_NOTES.md`.

Directory appointments are 160,104, were 159,961. Editors are 111,229, were 111,154. Journals stay 2,853. Institutions are 11,344 rows (8,665 with a ROR id), were 11,276 (8,663). 12,307 appointments have no institution. 642 country-only, 3 bracket-only, and 5 street, PO Box, or postal-code appointments stay off that page. `11KBW`, UNSW Sydney, and INSEAD stay. Twelve ajg1 navigation rows stay out, including Vincent Pan on Advances in Decision Sciences.

## Previous freeze: editors_single_editor_20261029

Fuller boards for four AJG 1 journals that had one editor row, plus two browser-board replacements carried in this freeze. Frozen 2026-10-29 23:18 Asia/Taipei. This supersedes `editors_browser_boards_20261029`. prio43 and ajg2 row counts are unchanged. African Affairs stays the 40-row Wayback board. Rankings were not edited. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. Empty `editor_name` is 3 on prio43, 0 on ajg2, and 16 on ajg1. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

Every current editor CSV ends with `board_urls` and `board_url_count`. `board_urls` is a pipe-separated list of public board-page URLs, filled only when that board spans more than one page. On these files that is PASOS Journal of Tourism and Cultural Heritage. `board_url_count` is the number of those URLs. Both cells are blank on every other row. `source_url` stays the primary board link. The build selects columns by name and does not write `board_urls` to the site.

The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. Live OUP for African Affairs is still Cloudflare-blocked. See `african_affairs_needs_browser.md`.

This publish replaces the rows of six ajg1 journals. Other rows stay as published in `editors_apjiht_board_fix_20261029`, including the three-journal board fix and the place-suffix and country corrections from earlier freezes. Small Business International Review stays parked (6 rows). The collector ajg1 file again included 12 navigation or citation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them. His collector row carries `Architecture Business School` and `https://ror.org/04facnr46`. No replacement ROR was added. The collector file counted ajg1 as 11,295 to 11,556 because those 12 rows were still in it. The published file is 11,244 to 11,544.

## Boards

| Journal | Was | Now |
|---|---:|---:|
| International Journal of Innovation and Technology Management | 1 | 96 |
| PASOS Journal of Tourism and Cultural Heritage | 1 | 87 |
| Pacific Journal of Optimization | 1 | 54 |
| Quantitative Finance and Economics | 11 | 43 |
| Strategic Behavior and the Environment | 1 | 28 |
| Foundations and Trends® in Information Systems | 6 | 13 |

International Journal of Innovation and Technology Management is 96 people, from the 2022-08-14 Wayback snapshot. The live World Scientific page returned 403. Source `https://web.archive.org/web/20220814200834/https://www.worldscientific.com/page/ijitm/editorial-board`. ROR ids already on these boards are attached on 65 of 96 (63 high, 2 medium).

PASOS Journal of Tourism and Cultural Heritage is 87 people. `board_urls` lists the editorial team, the scientific council, and the about page (`board_url_count` 3), all Wayback copies. ROR ids already on these boards are attached on 4 of 87, all high.

Pacific Journal of Optimization is 54 people. The old row was `Order Form`. Source `https://web.archive.org/web/20251117200040/http://manu71.magtech.com.cn/Jwk3_pjo/EN/column/column2.shtml`. ROR ids already on these boards are attached on 33 of 54, all high.

Quantitative Finance and Economics is 43 people. The old rows were navigation labels. Source `https://www.aimspress.com/qfe/news/solo-detail/editorialboard`. One ROR id already on these boards is attached (Jinyu Chen, Central South University, high).

Strategic Behavior and the Environment is 28 people. Source `https://web.archive.org/web/20260321070732id_/https://www.emerald.com/sbe/pages/editorial-board`. The publisher line is not on this board. ROR ids already on these boards are attached on 21 of 28, all high.

Foundations and Trends® in Information Systems is 13 people. The old rows were navigation labels and two blank names. Source `https://www.emerald.com/ftisy/pages/editorial-board`. ROR ids already on these boards are attached on all 13, all high.

Small Business International Review stays the 6 parked rows. The site was unreachable.

The new rows contain no email address, phone number, or photo.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2. The collector CSV again included 12 ajg1 navigation or citation rows and 2 ajg2 navigation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, blank affiliation | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 3 | 82 | 2,723 | 2,651 | 1 | 2 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,982 | 0 | 386 | 4,727 | 4,574 | 0 | 7 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,544 | 16 | 616 | 9,159 | 8,625 | 2 | 7 |
| Total | 19,630 | 19 | 1,084 | 16,609 | 15,850 | 3 | 16 |

`ror_id` on a nonempty affiliation is 15,850 / 16,609 (95.4%): ajg1 8,625 / 9,159 (94.2%), ajg2 4,574 / 4,727 (96.8%), prio43 2,651 / 2,723 (97.4%). Gap `ror_id` was 15,715. The added ids were already on these boards. Gap `ror_id` values are high or medium confidence only. A faculty URL with a blank affiliation is 3. Sixteen faculty URLs have no `ror_id`. No name, ROR id, affiliation, or URL was invented.

## Public site

Directory journals stay 2,853. Directory appointments are 159,961, were 158,747. Editors are 111,154, were 110,424. Countries stay 175. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796). Faculty profile links stay 24,817. The Institutions page has 11,276 rows (8,663 with a ROR id), were 10,824 (8,662), and 12,309 appointments with no institution. 641 appointments are omitted because the affiliation is only a country or territory, were 633. Three are omitted because the affiliation is only a bracketed fragment. Ten are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country. `11KBW`, UNSW Sydney, and INSEAD stay.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
