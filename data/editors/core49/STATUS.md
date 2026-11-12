# Editors — core49

Updated: 2026-11-12 (Asia/Taipei)

## Release in this repo

`releases/editors_backfill_red_gap_20261112/` — current multi-year core49 editor backfill with ROR, published 2026-11-12. It supersedes `editors_ra_ta_merge_rebuild_20261112` (PR #69): Review of Economic Dynamics 2022 (43 rows, `#15578`–`#15620`) and 2023 (43 rows, `#15621`–`#15663`) added from the Society for Economic Dynamics “Our Editors” page via Wayback (page versions modified 2021-04-14 and 2023-02-21; captures 20220219234913 and 20230324123429), each with a matching long-table row; the RED 2021 inventory row is fixed to `ok_issue_front_matter` 45/45; RED 2021–2023 gaps `blocked` → `resolved`; the RED match-rate row recomputed. 31 distinct RORs on the new rows, all API-active; #15638 Anmol Bhandari stays blank (no institution printed). `editors_backfill_scale_spotcheck.csv` is byte-identical to the phone/fax-scrubbed web copy. Change log: `RED_2022_2023_board_changes_20261112.csv`. The directory site does not read it.

In `editors_ra_ta_merge_rebuild_20261112` (published 2026-11-12 with user approval, kept in the tree): It is a mechanical rebuild of the held `editors_ra_ta_merge_20261106` onto `editors_backfill_scale_ror_20261031`: 20 RA/TA and FIX-retry rows updated (S01–S20; S11 Lochner → Western Ontario, S14 Carlton → Chicago Booth, S20 Castanheira → ECARES with ROR blank), Review of Economic Dynamics 2021 added (45 rows, `#15446`–`#15490`; three SED officers in gaps), and Journal of Business and Economic Statistics 2018 added (87 rows, `#15491`–`#15577`; the ASA Committee on Publications in gaps, editorial coordinator Jamie Hutchens in staff rows). The directory site does not read it; it shows current boards only. `editors_backfill_scale_spotcheck.csv` keeps the phone/fax-scrubbed copy from `editors_backfill_scale_ror_20261031`. Change logs: `RA_TA_merge_changes_20261106.csv`, `RA_FIX_retry_changes_20261106.csv`, `RED_2021_board_changes_20261106.csv`, `JBES_2018_board_changes_20261106.csv`.

Previous: `releases/editors_backfill_scale_ror_20261031/` — published 2026-11-01 with user approval together with the current-board freeze `editors_ror_consistency3b_20261101`; kept in the tree.

| File | Rows | Notes |
|------|-----:|-------|
| `editors_backfill_scale_ror_panel.csv` | 15,664 | 39 journals; was 15,578 (+86 RED 2022/2023). In `editors_ra_ta_merge_rebuild_20261112`: 15,578, was 15,446 (+132 new, 20 changed). In `editors_backfill_scale_ror_20261031`: 301 journal-years. Matched 11,021; unmatched 360; no affiliation 4,017; staff excluded 48 |
| `editor_affiliations.csv` | 11,896 | One row per affiliation part, keyed by `editor_row_key` |
| `editors_backfill_scale_row_key_crosswalk.csv` | 15,446 | Old to new `editor_row_key` (8,723 keys shifted after a parse fix) |
| `editors_backfill_scale_matched.csv` / `_unmatched.csv` | 1,847 / 86 | Distinct affiliation strings and their ROR decision |
| `editors_backfill_scale_gaps.csv` | 4,568 | Journal-years and rows with missing coverage |
| `editors_backfill_scale_inventory.csv` | 312 | Journal-year source inventory |
| `editors_backfill_scale_spotcheck.csv` | 301 | QC sample. Phone/fax fragments removed from 30 cells |
| `BACKFILL_SCALE_ROR_*.csv`, `_build.json`, `README.md` | | Small audit logs and the collector manifest |

The inventory row for Review of Economic Dynamics 2021 now reads `ok_issue_front_matter`, 45 of 45 rows (fixed in `editors_backfill_red_gap_20261112`; it read `blocked` / 0 in `editors_ra_ta_merge_rebuild_20261112`).

No `raw_html/`, scrape caches, emails, phones, or photos are in the repo. `source_file` columns name collector capture paths only. No file is over 50 MB, so nothing is gzipped. Report: `docs/reports/BACKFILL_scale_ror_20261031.md`.

## Known coverage gaps

- Review of Economic Dynamics 2024–2025 (2021 filled in `editors_ra_ta_merge_rebuild_20261112`; 2022 and 2023 filled in `editors_backfill_red_gap_20261112`). RED 2024 is RA pack 2 item S22; RED 2025 needs the ScienceDirect Vol 55 front matter.
- Journal of Business & Economic Statistics 2019–2020 and 2025 (2018 filled in `editors_ra_ta_merge_rebuild_20261112`).
- Journal of Risk and Uncertainty (JRU) 2023 (still not found).
- Journal of Urban Economics 2018–2019 partial.
- Economic Journal 2018 low confidence.
- About 4,017 names-only rows: AER, AER: Insights, JPE, JOLE, JLE, and QJE print no affiliations, so those rows are intentionally blank.

## Open ROR decisions (left blank, not guessed)

"Virginia University, Charlottesville" → University of Virginia (`0153tk833`?), INRA-AgroParisTech, the Adelaide and Cergy-Pontoise successor organizations, ECARES / CORE, the Cowles Foundation, and CEU Budapest.

## Superseded

The older collector panels (`editors_panel_2018_2026_with_ror.csv` and window slices) and the scale-parse packs are superseded by this release and are not copied here.
