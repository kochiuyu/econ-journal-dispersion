# editors_trailing_country_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_raw_aff_part_no_fix_20261110` (Directory PR #52) for the Directory current panels. It is a keyed, user-approved fix for Institution names that ended in a printed country. 6,036 publish-panel rows get the country stripped from `canonical_name` and `ror_country` / `continent` set from it (137 Institutions are rematched to an existing panel twin, reusing that twin's ROR id where it has one; no ROR id is invented). The printed `raw_affiliation` is unchanged. The audit's REVIEW and KEEP names are untouched, and 11 rows whose stripped name would end in a dangling `and` / `&` (e.g. `Court of Appeal of England and`) are held back. No site filter. The long table, change log and skip list are in `data/editors/releases/editors_trailing_country_fix_20261110/`. Report: `docs/reports/TRAILING_COUNTRY_FIX_20261110.md`.

Rows changed: with_ror 84 (name + country), slim 81 (country only).

**Directory.** Institutions 15,166 (was 15,434), 6,387 with a ROR id (unchanged). Countries 162 (was 159: Guinea, Haiti, Timor-Leste). 12,068 appointments have no institution (was 12,067: a printed `…, Haiti` row now falls to the country-only filter). Appointments 162,575, editors 112,718, journals 2,853. Shared display names stay 69.

## Previous freeze: editors_raw_aff_part_no_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_edpacs_marks_country_fix_20261110` (Directory PR #51) for the Directory current panels. It is a long-table-only fix: `raw_aff_part` `no` → blank on 9,695 parts of `data/editors/releases/editors_raw_aff_part_no_fix_20261110/editor_affiliations.csv.gz`. The panel CSVs are unchanged. Report: `docs/reports/RAW_AFF_PART_NO_FIX_20261110.md`.

FT50 long parts blanked: 104 (slim) / 99 (with_ror).

**Directory.** Unchanged: appointments 162,575, editors 112,718, journals 2,853, Institutions 15,434 (6,387 with a ROR id), countries 159, 12,067 appointments without an institution, shared display names 69.

## Previous freeze: editors_edpacs_marks_country_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_paren_num_leftover_fix_20261110` (Directory PR #50) for the Directory current panels. It is a keyed, user-approved follow-up on three ABDC C EDPACS seats. No ROR ids change and there is no site filter. The long table and change log are in `data/editors/releases/editors_edpacs_marks_country_fix_20261110/`. Report: `docs/reports/EDPACS_MARKS_COUNTRY_FIX_20261110.md`.

Both FT50 files are unchanged.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,434 (6,387 with a ROR id), were 15,435 / 6,387. Countries stay 159. 12,067 appointments have no institution (was 12,066: Marks' seat no longer falls back to his printed bio). Shared display names stay 69. The only parenthesis- and number-start Institutions left are the 14 kept numbered organisations.

## Previous freeze: editors_paren_num_leftover_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_tokyo_other_inst_fix_20261110` (Directory PR #49) for the Directory current panels. It is a keyed, user-approved fix for the parenthesis- and number-start Institutions left as REVIEW. Only institution fields are changed, the printed `raw_affiliation` is kept, and the guardrail and history notes stay in `ror_notes` with a `paren_num_leftover_fix_20261110:` token appended. No new ROR ids and no site filter. Both FT50 files are unchanged. The long table and change log are in `data/editors/releases/editors_paren_num_leftover_fix_20261110/`. Report: `docs/reports/PAREN_NUM_LEFTOVER_FIX_20261110.md`.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,435 (6,387 with a ROR id), were 15,438 / 6,387. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The remaining parenthesis- and number-start Institutions are the 14 kept numbered organisations, plus Norman Marks' printed bio, which still shows through the printed-text fallback.

## Previous freeze: editors_tokyo_other_inst_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_tokyo_gatech_fix_20261110` (Directory PR #48) for the Directory current panels. It is a keyed ABDC-only fix for the 35 seats whose `canonical_name` was the bare `Tokyo` with a blank ROR. The collector's copies of those seats had the place-strip rewrite `Italian Cultural Institute`, and the Directory guardrail had already restored the printed text. Both FT50 files are unchanged. There is no site filter. The long table and change log are in `data/editors/releases/editors_tokyo_other_inst_fix_20261110/`. Report: `docs/reports/TOKYO_OTHER_INST_FIX_20261110.md`.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,438 (6,387 with a ROR id), were 15,432 / 6,381. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The unmatched `Tokyo` (Japan) Institutions row falls from 35 appointments to 1.

## Previous freeze: editors_tokyo_gatech_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_inst_punct_split_20261110` (Directory PR #47) for the Directory current panels. It is a keyed panel-only fix on FT50. It rematches University of Tokyo seats whose ROR the Directory guardrail (`directory_guardrail_restore_20261101`) had left blank to The University of Tokyo `https://ror.org/057zh3y96`, and rematches the Decision Sciences `Georgia Inst of Technology` seat to `https://ror.org/01zkghx44`. The printed `raw_affiliation` is kept, and the Directory guardrail note stays in `ror_notes` with the fix token appended. There is no site filter. The long table and change log are in `data/editors/releases/editors_tokyo_gatech_fix_20261110/`. Report: `docs/reports/TOKYO_GATECH_FIX_20261110.md`.

| File | Rows | `ror_id` (was) | `raw_affiliation` |
|---|---:|---:|---:|
| `editors_ft50_current.csv` | 10,047 | 9,622 (9,620) | 9,936 |
| `editors_ft50_current_with_ror.csv` | 10,047 | 9,701 (9,699) | 9,941 |

Two rows per file: Eric Weese (Econometrica) and Fuhito Kojima (Journal of Political Economy). Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,432 (6,381 with a ROR id), were 15,434 / 6,381. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The University of Tokyo is one Institutions row (`057zh3y96`, 173 appointments); `Georgia Inst of Technology` is no longer a separate unmatched row.

## Previous freeze: editors_inst_punct_split_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_inst_drop_rematch_20261110` (Directory PR #46) for the Directory current panels. It is a panel-only Institutions cleanup on FT50: leftover punctuation-start junk is blanked (DROP), high-confidence name splits are rematched onto existing panel ROR twins (REMATCH; printed `raw_affiliation` kept; `canonical_name` set to the twin `ror_name`), and three name-only variants are unified with a blank ROR (UNIFY). REVIEW and KEEP flags were excluded. There is no site filter in `scripts/build_site.py`. The long table and change log are in `data/editors/releases/editors_inst_punct_split_20261110/`. Report: `docs/reports/INST_PUNCT_SPLIT_20261110.md`.

**What changed.** Both FT50 files are patched by the collector delta applied onto the published Directory copy of `editors_inst_drop_rematch_20261110` (13 slim + 20 with_ror REMATCH rows; no DROP or UNIFY). The collector copies were not overlaid. Directory guardrail restores, contact scrub, and the FT50 Top 5 alignment stay. `*_with_profile_pilot.csv` is not published.

| File | Rows | `ror_id` (was) | `raw_affiliation` |
|---|---:|---:|---:|
| `editors_ft50_current.csv` | 10,047 | 9,620 (9,607) | 9,936 |
| `editors_ft50_current_with_ror.csv` | 10,047 | 9,699 (9,679) | 9,941 |

`11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,434 (6,381 with a ROR id), were 15,612 / 6,381. Countries stay 159. 12,066 appointments have no institution (were 12,052). Shared display names 69 (were 125).

## Previous freeze: editors_inst_drop_rematch_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_nonlatin_inst_20261110` (Directory PR #45) for the Directory current panels. It is a panel-only Institutions cleanup (DROP junk bios and address lines; REMATCH singleton variants onto existing panel ROR twins; printed `raw_affiliation` kept). REVIEW and KEEP flags were excluded. There is no site filter in `scripts/build_site.py`. Long table: `data/editors/releases/editors_inst_drop_rematch_20261110/editor_affiliations.csv.gz`. Report: `docs/reports/INST_DROP_REMATCH_20261110.md`.

**What changed.** Both FT50 files are patched by the collector delta applied onto the published Directory copy of `editors_nonlatin_inst_20261110`. Directory guardrail restores, contact scrub, held-out AJG1 navigation rows, and the FT50 Top 5 alignment stay. The collector copies were not overlaid, because they predate those Directory-only edits. Slim `editors_ft50_current.csv` also blanks Tiffany Trzebiatowski's Journal of Management Studies CV (the collector only patched the with_ror copy of that row). Elizabeth M. Lee's slim rematch to Saint Joseph's University is not copied onto with_ror (that file already blanks the id as PA vs NY ambiguous).

| File | Rows | `ror_id` (was) | `raw_affiliation` (was) |
|---|---:|---:|---:|
| `editors_ft50_current.csv` | 10,047 | 9,607 (9,600) | 9,936 (9,941) |
| `editors_ft50_current_with_ror.csv` | 10,047 | 9,679 (9,673) | 9,941 (9,946) |

`11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,612 (6,381 with a ROR id), were 16,234 / 6,381. Countries stay 159. 12,052 appointments have no institution (were 11,991).

## Previous freeze: editors_nonlatin_inst_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_ror_consistency3b_20261101` (Directory PR #41) for the Directory current panels. The files in this folder are unchanged. The only panel edit is on ABDC C (19 bio/CV blurbs blanked, 60 rematches onto existing Latin ROR twins, printed non-Latin names kept). Long table: `data/editors/releases/editors_nonlatin_inst_20261110/editor_affiliations.csv.gz`. Report: `docs/reports/NONLATIN_INST_20261110.md`.

## Previous freeze: editors_ror_consistency3b_20261101

Published 2026-11-01 (Asia/Hong_Kong) with user approval. This supersedes `editors_browser_single_20261029` (Directory PR #40). The collector packs between the two (`editors_ror_consistency2`, `editors_ror_consistency`, `editors_ror_multiaff`, `editors_ror_campus2`, `editors_ror_campus`, `post15`, the profile `pilot`, the scale-parse packs, and the t39 / institution-fix freezes) were never published and are retired. The long table and audit logs are in `data/editors/releases/editors_ror_consistency3b_20261101/`; reports in `docs/reports/` (`PREPUBLISH_CHECK_20261101.md`, `ROR_PREPUBLISH_FIX_20261101.md`, `ROR_CONSISTENCY3_20261101.md`). The core49 backfill `editors_backfill_scale_ror_20261031` is pinned at the same time under `data/editors/core49/releases/`.

**Columns.** After `board_urls` and `board_url_count` every panel adds `board_status`, `tenure_start_year`, `tenure_end_year`, `snapshot_date`, `snapshot_source`, `board_year`, `editor_row_key`, `affiliation_count`, `ror_id_aff_rank`, `primary_aff_basis`, `former_flag`, and `other_ror_ids`. The slim `editors_ft50_current.csv` also gains `ror_id`, `ror_name`, `ror_country`, and `continent`. The board columns are no longer the last two. A single `board_urls` entry may now appear on any journal.

**ROR.** The collector blanks a ROR id when the masthead text cannot be matched to one organization without guessing (strict matching, multi-affiliation parsing, campus splits). So `ror_id` coverage is lower than in `editors_browser_single_20261029` on every panel except ajg2, and a few correct ids were blanked as ambiguous. Nothing was invented. Display affiliation is still `ror_name`, then `canonical_name`, then `raw_affiliation`; country is `ror_country`.

**Directory guardrails kept.** The twelve ajg1 navigation rows (including Vincent Pan on Advances in Decision Sciences) and the two ajg2 Policy Design and Practice navigation rows stay out. Collector institution-string rewrites that were wrong (for example Tokyo mastheads rewritten to `Italian Cultural Institute`, and HKUST (Guangzhou) collapsed onto HKUST) are reverted to the published text: 95 rows plus two `editor_name_raw` restores, listed in `DIRECTORY_GUARDRAILS_restored_rows_20261101.csv`. `11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate; ESSEC is France `02dga6j42`. A blank or country-only affiliation is not an institution. Emails and phone or fax numbers that the collector left in text cells (mostly `source_note`) were removed.

**Directory.** Appointments 162,575 (were 160,104). Editors 112,718 (were 111,229). Journals 2,853. Institutions 16,283 rows, 6,381 with a ROR id (were 11,344 / 8,665). 11,972 appointments have no institution; 650 country-only, 12 bracket-only, and 7 address-only appointments stay off Institutions. Countries 159 (were 175).

| File | Rows (was) | `ror_id` (was) |
|---|---:|---:|
| `editors_ft50_current.csv` | 10,047 (10,046) | 9,600 (no column) |
| `editors_ft50_current_with_ror.csv` | 10,047 (10,046) | 9,673 (9,864) |

Two Review of Economic Studies rows whose `editor_name` was `Universitat Pompeu Fabra` are dropped (the collector removed them from ABDC A* only). Three Top 5 seats the collector added only to ABDC A* (`t39_final15_fix_20261030`: American Economic Review Erik Snowberg and Juan Carlos Suárez Serrato; Review of Economic Studies Mikkel Plagborg-Moller) are copied into both FT50 files, tagged `top5_ft50_align_20261101` in `ror_notes`, so every Top 5 seat is an FT50 seat. Their long-table rows are the A* ones. Empty `editor_name` is 1. `faculty_profile_url` stays 8,375. Contact text removed from 625 / 626 cells.

## Previous freeze: editors_browser_single_20261029

Frozen 2026-10-30 07:09 Asia/Taipei. This supersedes `editors_single_editor_20261029` (Directory PR #39). The collector added browser-captured boards on three ABDC journals: Journal of Derivatives (A, 1 to 18), Journal of Portfolio Management (A, 1 to 73), and Arts and the Market (C, 1 to 55). Both FT50 files are unchanged in this publish. The collector copies are byte-identical to `editors_single_editor_20261029`. See `data/editors/abdc/releases/current/RELEASE_NOTES.md`.

Directory appointments are 160,104, were 159,961. Editors are 111,229, were 111,154. Journals stay 2,853. Institutions are 11,344 rows (8,665 with a ROR id), were 11,276 (8,663). 12,307 appointments have no institution. 642 country-only, 3 bracket-only, and 5 street, PO Box, or postal-code appointments stay off that page. `11KBW`, UNSW Sydney, and INSEAD stay. Twelve ajg1 navigation rows stay out, including Vincent Pan on Advances in Decision Sciences.

## Previous freeze: editors_single_editor_20261029

Fuller boards on ABDC A, ABDC B, ABDC C, and AJG 1, including the five browser-board replacements carried in this freeze. Frozen 2026-10-29 23:18 Asia/Taipei. This supersedes `editors_browser_boards_20261029`. Both FT50 files stay 10,046 rows. The only change on these two files is two trailing columns, `board_urls` and `board_url_count`, and both are blank on every FT50 row. Empty `editor_name` is 1. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

`board_urls` is a pipe-separated list of public board-page URLs, filled only on multi-page boards in the ABDC and AJG-gap files. `board_url_count` is the number of those URLs. The build selects columns by name and does not write `board_urls` to the site. `source_url` stays the primary board link.

## What this publish changed

The collector freeze replaces heading and navigation rows on five journals and expands fifteen journals that had a single editor row. This publish pins those journals on the ABDC A, ABDC B, ABDC C, and AJG 1 files. By panel that is A 2 rows to 411, B 13 rows to 219, C 12 rows to 309, and ajg1 21 rows to 321. The FT50 files, ABDC A*, prio43, and ajg2 are unchanged apart from the two blank columns. A rematch on a new row uses a ROR id already on these boards, or one exact crosswalk hit (`https://ror.org/04a85ht85`, Galgotias College of Engineering & Technology). No ROR id was invented.

Other rows stay as published in `editors_apjiht_board_fix_20261029`. The collector CSV also rewrote institution strings outside those journals. Those rows stay as published, including Tokyo mastheads that the collector would have replaced with `Italian Cultural Institute`. Twelve ajg1 navigation rows stay out, including Vincent Pan on Advances in Decision Sciences. Small Business International Review stays parked. `11KBW`, UNSW Sydney, and INSEAD stay.

The slim file still has no ROR columns.

| Metric | This publish |
|---|---:|
| Rows | 10,046 |
| Empty `editor_name` | 1 |
| `faculty_profile_url` | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,946 (99.0%) |
| `ror_id` on the ROR file | 9,864 (98.2%) |
| Faculty URL, no `ror_id` | 48 |

The slim file has `raw_affiliation` on 9,942 rows and no ROR columns.

## Publish holds

Two medium hits that name a different organization stay unpublished.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. That id stays off. The masthead is `ESADE Business School`. Country stays Spain.

Jaap Paauwe’s display name stays `Jaap Paauwe`. `editor_name_raw` stays `Jaap Paauwe, Tilburg`.

`canonical_name` values cleared in earlier institution freezes stay clear on rows this publish did not edit. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page. No person name or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments are 159,961, were 158,747. Editors are 111,154, were 110,424. Journals stay 2,853. Countries stay 175. FT50 seats stay 10,044 across 50 journals. Top 5 stays 362. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 11,276 rows (8,663 with a ROR id), were 10,824 (8,662). 12,309 appointments have no institution. 641 appointments are omitted because the affiliation is only a country or territory, were 633. Three are omitted because the affiliation is only a bracketed fragment. Ten are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
