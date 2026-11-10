# editors_tokyo_other_inst_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_tokyo_gatech_fix_20261110` (Directory PR #48) for the Directory current panels. It is a keyed ABDC-only fix for the 35 seats whose `canonical_name` was the bare `Tokyo` with a blank ROR. The collector's copies of those seats had the place-strip rewrite `Italian Cultural Institute`, and the Directory guardrail had already restored the printed text. There is no site filter. The long table and change log are in `data/editors/releases/editors_tokyo_other_inst_fix_20261110/`. Report: `docs/reports/TOKYO_OTHER_INST_FIX_20261110.md`.

The printed `raw_affiliation` is kept, `canonical_name` is set to the printed institution, and the Directory guardrail note stays in `ror_notes` with the fix token appended.

| File | Rows | Rows patched (rematched / ROR blank) | `ror_id` (was) |
|---|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,596 | 1 (0 / 1, Kojima) | 23,399 (23,399) |
| `editors_abdc_a_current.csv` | 45,889 | 7 (4 / 3) | 40,578 (40,574) |
| `editors_abdc_b_current.csv` | 42,558 | 13 (10 / 3) | 36,945 (36,935) |
| `editors_abdc_c_current.csv` | 27,719 | 14 (9 / 5) | 21,549 (21,540) |

ROR ids: Tokyo University of Science `05sj3n476` (7), Tokyo Metropolitan University `00ws30h19` (3), Tokyo University of Agriculture and Technology `00qg0kr10` (3), Tokyo International University `01g9ekh39` (3), Tokyo University of Marine Science and Technology `048nxq511` (2), Tokyo Keizai University `03b0ym704` (2), Tokyo Gakugei University `00khh5r84` (1), Tokyo Women's Medical University `03kjjhe36` (1), Tokyo University of Foreign Studies `027tyzk91` (1). Six of them (`00ws30h19`, `048nxq511`, `03b0ym704`, `00khh5r84`, `03kjjhe36`, `027tyzk91`) are new to the published panels and were checked against the public ROR API (active, same display name, Japan). Tokyo Institute of Technology (11) keeps a blank ROR and is not mapped to Institute of Science Tokyo. `ror_country` Japan is kept on the 12 blank-ROR seats.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,438 (6,387 with a ROR id), were 15,432 / 6,381. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The unmatched `Tokyo` (Japan) Institutions row falls from 35 appointments to 1.

## Previous freeze: editors_tokyo_gatech_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_inst_punct_split_20261110` (Directory PR #47) for the Directory current panels. It is a keyed panel-only fix on ABDC A*, A, B, and C. It rematches University of Tokyo seats whose ROR the Directory guardrail (`directory_guardrail_restore_20261101`) had left blank to The University of Tokyo `https://ror.org/057zh3y96`, and rematches the Decision Sciences `Georgia Inst of Technology` seat to `https://ror.org/01zkghx44`. The printed `raw_affiliation` is kept, and the Directory guardrail note stays in `ror_notes` with the fix token appended. There is no site filter. The long table and change log are in `data/editors/releases/editors_tokyo_gatech_fix_20261110/`. Report: `docs/reports/TOKYO_GATECH_FIX_20261110.md`.

| File | Rows | Rows patched | `ror_id` (was) |
|---|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,596 | 5 (4 Tokyo + 1 Georgia Tech) | 23,399 (23,394) |
| `editors_abdc_a_current.csv` | 45,889 | 5 | 40,574 (40,569) |
| `editors_abdc_b_current.csv` | 42,558 | 5 | 36,935 (36,930) |
| `editors_abdc_c_current.csv` | 27,719 | 3 | 21,540 (21,537) |

`raw_affiliation` counts and `faculty_profile_url` are unchanged. Invented ROR ids: 0. The 35 other Tokyo-institution seats that the collector still has as `Italian Cultural Institute` keep their Directory printed text and the bare `Tokyo` canonical name. They are not touched here.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,432 (6,381 with a ROR id), were 15,434 / 6,381. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The University of Tokyo is one Institutions row (`057zh3y96`, 173 appointments); `Georgia Inst of Technology` is no longer a separate unmatched row.

## Previous freeze: editors_inst_punct_split_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_inst_drop_rematch_20261110` (Directory PR #46) for the Directory current panels. It is a panel-only Institutions cleanup on ABDC A*, A, B, and C: leftover punctuation-start junk is blanked (DROP), high-confidence name splits are rematched onto existing panel ROR twins (REMATCH; printed `raw_affiliation` kept; `canonical_name` set to the twin `ror_name`), and three name-only variants are unified with a blank ROR (UNIFY). REVIEW and KEEP flags were excluded. There is no site filter in `scripts/build_site.py`. The long table and change log are in `data/editors/releases/editors_inst_punct_split_20261110/`. Report: `docs/reports/INST_PUNCT_SPLIT_20261110.md`.

**What changed.** All four ABDC current panels are patched by the collector delta applied onto the published Directory copy of `editors_inst_drop_rematch_20261110`: A* 88 REMATCH; A 89 REMATCH; B 7 DROP + 88 REMATCH + 2 UNIFY (`39 Essex Chambers`); C 7 DROP + 79 REMATCH + 2 UNIFY (`Izmir Bakircay University`; `Global Labor Organization (GLO), Essen, Germany`). The collector copies were not overlaid. Directory guardrail restores and contact scrub stay. `*_with_profile_pilot.csv` is not published.

| File | Rows | `ror_id` (was) | `raw_affiliation` (was) | Empty `editor_name` |
|---|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,596 | 23,394 (23,306) | 24,202 (24,202) | 1 |
| `editors_abdc_a_current.csv` | 45,889 | 40,569 (40,480) | 43,159 (43,159) | 1 |
| `editors_abdc_b_current.csv` | 42,558 | 36,930 (36,842) | 40,187 (40,190) | 11 |
| `editors_abdc_c_current.csv` | 27,719 | 21,537 (21,458) | 24,845 (24,851) | 6 |

`faculty_profile_url` stays 12,522 / 6,236 / 3,509 / 1,379. `11KBW`, UNSW Sydney, and INSEAD stay. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,434 (6,381 with a ROR id), were 15,612 / 6,381. Countries stay 159. 12,066 appointments have no institution (were 12,052). Shared display names 69 (were 125).

## Previous freeze: editors_inst_drop_rematch_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_nonlatin_inst_20261110` (Directory PR #45) for the Directory current panels. It is a panel-only Institutions cleanup on ABDC A*, A, B, and C (DROP junk bios and address lines; REMATCH singleton variants onto existing panel ROR twins; printed `raw_affiliation` kept). REVIEW and KEEP flags were excluded. There is no site filter in `scripts/build_site.py`. The long table and change log are in `data/editors/releases/editors_inst_drop_rematch_20261110/`. Report: `docs/reports/INST_DROP_REMATCH_20261110.md`.

**What changed.** All four ABDC current panels are patched by the collector delta applied onto the published Directory copy of `editors_nonlatin_inst_20261110`. Directory guardrail restores, contact scrub, and held-out AJG1 navigation rows stay. The collector copies were not overlaid, because they predate those Directory-only edits. `*_with_profile_pilot.csv` is not published.

| File | Rows | `ror_id` (was) | `raw_affiliation` (was) | Empty `editor_name` |
|---|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,596 | 23,306 (23,285) | 24,202 (24,210) | 1 |
| `editors_abdc_a_current.csv` | 45,889 | 40,480 (40,410) | 43,159 (43,164) | 1 |
| `editors_abdc_b_current.csv` | 42,558 | 36,842 (36,765) | 40,190 (40,194) | 11 |
| `editors_abdc_c_current.csv` | 27,719 | 21,458 (21,297) | 24,851 (24,887) | 6 |

`faculty_profile_url` stays 12,522 / 6,236 / 3,509 / 1,379. `11KBW`, UNSW Sydney, and INSEAD stay. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,612 (6,381 with a ROR id), were 16,234 / 6,381. Countries stay 159. 12,052 appointments have no institution (were 11,991).

## Previous freeze: editors_nonlatin_inst_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_ror_consistency3b_20261101` (Directory PR #41) for the Directory current panels. It is a panel-only Institutions fix for non-Latin-start names on ABDC C. There is no site filter in `scripts/build_site.py`. The long table and change log are in `data/editors/releases/editors_nonlatin_inst_20261110/`. Report: `docs/reports/NONLATIN_INST_20261110.md`.

**What changed.** Only `editors_abdc_c_current.csv` is patched, and only by the collector delta (79 appointments) applied onto the published Directory copy of consistency3b. Directory guardrail restores, contact scrub, held-out AJG1 navigation rows, and the FT50 Top 5 alignment stay. The other eight current panels are unchanged; the collector copies of those files were not overlaid, because they predate those Directory-only edits.

| Action | Count |
|---|---:|
| DROP bio/CV blurbs (blank `raw_affiliation` and `canonical_name`; no ROR) | 19 |
| REMATCH to an existing Latin ROR twin already on these panels (printed non-Latin names kept) | 60 |
| GAP, no Latin twin on these panels (printed name kept, ROR left blank; no panel-field change) | 8 |
| Stale flag not on the consistency3b panel | 1 |
| Appointments touched | 87 |
| Invented ROR ids | 0 |

Boards: Journal of the New Economic Association, Applied Econometrics, Academia Economic Papers, and Journal of the Japan Statistical Society. `11KBW`, UNSW Sydney, and INSEAD stay.

ABDC C stays 27,719 rows. `ror_id` is 21,297 (was 21,237). `raw_affiliation` is 24,887 (was 24,906). Empty `editor_name` stays 6; `faculty_profile_url` stays 1,379.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 16,234 (6,381 with a ROR id), were 16,283 / 6,381. Countries stay 159. 11,991 appointments have no institution (were 11,972): the 19 dropped blurbs are now blank affiliations.

## Previous freeze: editors_ror_consistency3b_20261101

Published 2026-11-01 (Asia/Hong_Kong) with user approval. This supersedes `editors_browser_single_20261029` (Directory PR #40). The collector packs between the two (`editors_ror_consistency2`, `editors_ror_consistency`, `editors_ror_multiaff`, `editors_ror_campus2`, `editors_ror_campus`, `post15`, the profile `pilot`, the scale-parse packs, and the t39 / institution-fix freezes) were never published and are retired. The long table and audit logs are in `data/editors/releases/editors_ror_consistency3b_20261101/`; reports in `docs/reports/` (`PREPUBLISH_CHECK_20261101.md`, `ROR_PREPUBLISH_FIX_20261101.md`, `ROR_CONSISTENCY3_20261101.md`). The core49 backfill `editors_backfill_scale_ror_20261031` is pinned at the same time under `data/editors/core49/releases/`.

**Columns.** After `board_urls` and `board_url_count` every panel adds `board_status`, `tenure_start_year`, `tenure_end_year`, `snapshot_date`, `snapshot_source`, `board_year`, `editor_row_key`, `affiliation_count`, `ror_id_aff_rank`, `primary_aff_basis`, `former_flag`, and `other_ror_ids`. The slim `editors_ft50_current.csv` also gains `ror_id`, `ror_name`, `ror_country`, and `continent`. The board columns are no longer the last two. A single `board_urls` entry may now appear on any journal.

**ROR.** The collector blanks a ROR id when the masthead text cannot be matched to one organization without guessing (strict matching, multi-affiliation parsing, campus splits). So `ror_id` coverage is lower than in `editors_browser_single_20261029` on every panel except ajg2, and a few correct ids were blanked as ambiguous. Nothing was invented. Display affiliation is still `ror_name`, then `canonical_name`, then `raw_affiliation`; country is `ror_country`.

**Directory guardrails kept.** The twelve ajg1 navigation rows (including Vincent Pan on Advances in Decision Sciences) and the two ajg2 Policy Design and Practice navigation rows stay out. Collector institution-string rewrites that were wrong (for example Tokyo mastheads rewritten to `Italian Cultural Institute`, and HKUST (Guangzhou) collapsed onto HKUST) are reverted to the published text: 95 rows plus two `editor_name_raw` restores, listed in `DIRECTORY_GUARDRAILS_restored_rows_20261101.csv`. `11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate; ESSEC is France `02dga6j42`. A blank or country-only affiliation is not an institution. Emails and phone or fax numbers that the collector left in text cells (mostly `source_note`) were removed.

**Directory.** Appointments 162,575 (were 160,104). Editors 112,718 (were 111,229). Journals 2,853. Institutions 16,283 rows, 6,381 with a ROR id (were 11,344 / 8,665). 11,972 appointments have no institution; 650 country-only, 12 bracket-only, and 7 address-only appointments stay off Institutions. Countries 159 (were 175).

| File | Rows (was) | `ror_id` (was) | Empty `editor_name` |
|---|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,596 (25,178) | 23,285 (23,600) | 1 |
| `editors_abdc_a_current.csv` | 45,889 (45,866) | 40,410 (42,088) | 1 |
| `editors_abdc_b_current.csv` | 42,558 (42,345) | 36,765 (38,876) | 11 |
| `editors_abdc_c_current.csv` | 27,719 (27,160) | 21,237 (23,226) | 6 |

Row gains are fuller boards and multi-affiliation seats from the collector. On B the eleven empty names are rows whose `editor_name` was only a telephone or fax line (German Economic Review 9, China and World Economy 1, South African Journal of Economics 1); the text was removed and the directory does not list an empty name. One A* and one A `faculty_profile_url` that embedded an email address are blank. Contact text removed from A* 513, A 217, B 12, C 13 cells.

## Previous freeze: editors_browser_single_20261029

Browser-captured fuller boards for three journals that had one editor row. Frozen 2026-10-30 07:09 Asia/Taipei. This supersedes `editors_single_editor_20261029` (published in Directory PR #39). Only `editors_abdc_a_current.csv` and `editors_abdc_c_current.csv` change. A* and B are unchanged. Headers are unchanged, including the trailing `board_urls` and `board_url_count`.

## What this publish changed

| Journal | Rating | Was | Now | New rows with a ROR id |
|---|---|---:|---:|---:|
| Journal of Derivatives | A | 1 | 18 | 13 of 17 |
| Journal of Portfolio Management | A | 1 | 73 | 10 of 72 |
| Arts and the Market (formerly Arts Marketing) | C | 1 | 55 | 37 of 54 |

That is 143 new rows: A 45,777 to 45,866 and C 27,106 to 27,160. The original editor row on each journal stays (Thomas Ho, Frank Fabozzi, Ben Walmsley). Duplicate listings of the same person on a second tab or section are not a second row. Peter L. Bernstein (Founding Editor) and Amit Partani have no affiliation. Arts and the Market's commissioning editor, editorial office, and supplier project manager are publisher staff and are not on this board. Their contact e-mails are not in the release.

`board_urls` is filled on Journal of Derivatives and Journal of Portfolio Management: the pm-research editor and editorial-board tabs (`board_url_count` 2) on every row of those two journals, including the original editor row. Arts and the Market is one page, so both cells stay blank.

ROR ids on the new rows are reused only from these panels and the crosswalk, with a country and name check. 60 of 143 new rows have one. No ROR id was invented. Rejected hits stay blank with the reason in `ror_notes`: Korea University (the crosswalk record is a different, Japan-based school), ESCP Business School - UK (ROR record in France), Kingston University - UK, Queens University Belfast, and York University - Canada (records in other countries).

Every other row is as published in `editors_single_editor_20261029`. The seven other collector panels are byte-identical to the prior freeze, and the published copies of those files are unchanged in this publish. The collector rows that were held back in earlier publishes stay held back.

The new rows contain no email address, phone number, or photo.

## Previous freeze: editors_single_editor_20261029

Fuller boards for journals that had one editor row, plus the five browser-board replacements carried in this freeze. Frozen 2026-10-29 23:18 Asia/Taipei. This supersedes `editors_browser_boards_20261029`. A* row count is unchanged. Empty `editor_name` is 2 on A*, 1 on A, 0 on B, and 11 on C. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

Every current editor CSV ends with `board_urls` and `board_url_count`. `board_urls` is a pipe-separated list of public board-page URLs, filled only when that board spans more than one page. `board_url_count` is the number of those URLs. Both cells are blank on every other row. `source_url` stays the primary board link. `scripts/build_site.py` selects columns by name and does not write `board_urls` to the site.

This publish replaces the rows of fourteen journals on these files. Other rows stay as published in `editors_apjiht_board_fix_20261029`, including the eight-journal board fix and the place-suffix and country corrections from earlier freezes. The collector CSV also rewrote institution strings on other journals, including `Italian Cultural Institute` on Tokyo mastheads. Those rows stay as published. A rematch on a new row uses a ROR id already on these boards, or one exact crosswalk hit. No ROR id was invented.

## Boards

Heading and navigation rows on three journals are replaced with the people on those boards. Eleven journals that had a single editor row now have the fuller board. Defense Transportation Journal stays one row: the junk line is replaced by the named managing editor. Raw affiliation is the masthead text.

| Journal | Rating | Was | Now |
|---|---|---:|---:|
| IEEE Transactions on Intelligent Transportation Systems | A | 1 | 299 |
| Academy of Management Perspectives | A | 1 | 112 |
| Naval Research Logistics | B | 8 | 119 |
| Journal of Personnel Psychology | B | 1 | 65 |
| New Directions for Evaluation | B | 4 | 35 |
| Journal of Eastern Asia Society for Transportation Studies | C | 1 | 90 |
| Acta Turistica | C | 1 | 51 |
| Management: Journal of Contemporary Management Issues | C | 1 | 51 |
| Journal of International Technology and Information Management | C | 1 | 34 |
| Economic Affairs | C | 4 | 32 |
| Agricultural Economics Review | C | 1 | 20 |
| Applied Econometrics | C | 1 | 19 |
| Electronic Journal of Knowledge Management | C | 1 | 11 |
| Defense Transportation Journal | C | 1 | 1 |

IEEE Transactions on Intelligent Transportation Systems is 299 people. The `journal` cell stays blank, as on the old row; the id is `ieee_transactions_intelligent_transportation_systems`. Source `https://ieee-itss.org/pub/t-its/board/`. `board_urls` is `https://ieee-itss.org/pub/t-its/|https://ieee-itss.org/pub/t-its/board/` (`board_url_count` 2) on all 299 rows. ROR ids are attached on 107 of 299 (102 high, 5 medium). One of those ids was not already on the published panels: Sachin Kumar, Galgotias College of Engineering & Technology, `https://ror.org/04a85ht85`, an exact crosswalk hit. Xingwang Li stays on the masthead string Henan Polytechnic University, with no ROR id.

Academy of Management Perspectives is 112 people. Source `https://www.aom.org/publications/journals/perspectives/perspectives-editorial-team/`. ROR ids already on these boards are attached on 24 of 112 (23 high, 1 medium).

Naval Research Logistics is 119 people. The department stays in the role text. Source `https://onlinelibrary.wiley.com/page/journal/15206750/homepage/editorialboard.html`. ROR ids already on these boards are attached on 94 of 119.

Journal of Personnel Psychology is 65 people. Source `https://www.hogrefe.com/us/journal/journal-of-personnel-psychology`. ROR ids already on these boards are attached on 49 of 65, all high.

New Directions for Evaluation is 35 people. Source `https://onlinelibrary.wiley.com/page/journal/1534875x/homepage/editorialboard.html`. ROR ids already on these boards are attached on 21 of 35.

Journal of the Eastern Asia Society for Transportation Studies is 90 people. Source `https://www.jstage.jst.go.jp/browse/easts/_pubinfo/-char/en`. The old row was the association address. ROR ids already on these boards are attached on 60 of 90 (59 high, 1 medium).

Acta Turistica is 51 people. `board_urls` lists the Srce editorial team and the faculty editorial board (`board_url_count` 2). ROR ids already on these boards are attached on 37 of 51, all high.

Management: Journal of Contemporary Management Issues is 51 people. `board_urls` lists the Srce editorial team and the about page (`board_url_count` 2). No ROR id is attached.

Journal of International Technology and Information Management is 34 people. Source `https://iima.org/wp/jitim/`. ROR ids already on these boards are attached on 19 of 34, all high.

Economic Affairs is 32 people, including four Previous Editors with `is_current` false and a blank affiliation. Source `https://onlinelibrary.wiley.com/page/journal/14680270/homepage/editorialboard.html`. ROR ids already on these boards are attached on 11 of 32, all high.

Agricultural Economics Review is 20 people. The original Antonios REZITIS row stays Managing Editor. The page's Antony Rezitis spelling is not a second row. One further ROR id already on these boards is attached.

Applied Econometrics is 19 people. The original editor row stays, including its low-confidence ROR id. The new rows add no ROR id.

Electronic Journal of Knowledge Management is 11 people. The old row was the `One moment, please...` interstitial. Reviewers are not on this board. No ROR id is attached.

Defense Transportation Journal stays one row. Barbara Parus, Managing Editor, replaces the interstitial. No ROR id is attached.

The new rows contain no email address, phone number, or photo.

## Files

| File | Rows | Empty `editor_name` | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 2 | 23,806 (94.6%) | 23,600 | 12,523 (49.7%) | 67 |
| `editors_abdc_a_current.csv` | 45,866 | 1 | 43,147 (94.1%) | 42,088 | 6,237 (13.6%) | 50 |
| `editors_abdc_b_current.csv` | 42,345 | 0 | 39,985 (94.4%) | 38,876 | 3,509 (8.3%) | 21 |
| `editors_abdc_c_current.csv` | 27,160 | 11 | 24,260 (89.3%) | 23,226 | 1,379 (5.1%) | 4 |

The table is this publish. In `editors_browser_single_20261029`, `ror_id` on A goes 42,065 to 42,088 and on C 23,189 to 23,226. In `editors_single_editor_20261029`, `ror_id` was 23,600 / 41,935 / 38,720 / 23,069 before, and the increases were A 130, B 156, and C 120. All but one of those ids were already on these boards. The exception is `https://ror.org/04a85ht85`. A* `ror_id` stays 23,600. Empty `editor_name` stays 2 / 1 / 0 / 11. Faculty URL counts stay A* 12,523, A 6,237, B 3,509, and C 1,379. A faculty URL with no `ror_id` stays 67 on A*, 50 on A, 21 on B, and 4 on C.

## Holds carried forward

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. Kai Hockerts stays INSEAD, `https://ror.org/05ynf4333`. Sam Kirshner stays UNSW Sydney, `https://ror.org/03r8z3t63`.

The same two medium hits withheld on the FT50 file stay withheld on the ABDC copy of that seat.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School. Country is Spain.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments are 160,104, were 159,961. Editors are 111,229, were 111,154. Journals stay 2,853. ABDC chips are A* 25,172 (219 journals), A 45,854 (626), B 42,330 (836), and C 27,148 (732). Countries stay 175. Institutions are 11,344 rows (8,665 with a ROR id), were 11,276 (8,663). 12,307 appointments have no institution, were 12,309. 642 country-only appointments, were 641, plus 3 bracket-only appointments and 5 street, PO Box, or postal-code appointments, were 10, stay off that page. State Street Global Advisors and State Street Associates are firms, not street addresses, so their 8 appointments (5 already published, 3 new on Journal of Portfolio Management) are now on Institutions.
