# Editors — core49

Updated: 2026-11-13 (Asia/Taipei)

## Release in this repo

`releases/editors_backfill_red_jbes_20261113/` — current multi-year core49 editor backfill with ROR, published 2026-11-13. It supersedes `editors_backfill_red_gap_20261112` (PR #70): Review of Economic Dynamics 2025 (44 rows, `#15664`–`#15707`, RED Vol 55 (2025-01) issue front matter; inventory `ok_issue_front_matter` 44/44), Journal of Business and Economic Statistics 2019 (87 rows, `#15708`–`#15794`, Vol 37 No. 1 front matter, JSTOR stable/45181150; inventory `ok_issue_front_matter` 87/84) and 2020 (78 rows, `#15795`–`#15872`, Vol 38 No. 1 front matter, JSTOR stable/45282197; inventory `ok_issue_front_matter` 78/75) added, with 206 long-table rows. JBES match rate 0.9302 (was 0.9322); RED 0.9965. 83 distinct RORs on the new rows, all API-active; one new to the backfill (`02jkmyk67`, CAS Academy of Mathematics and Systems Science). Two printed accents restored in 2020 rows only: #15843 Marcelo Medeiros, “Pontificia Universidade Católica” (unmatched, ROR blank: several PUCs, no campus); #15853 Christoph Rothe, “Universität Mannheim” (`031bsb921`). The ASA Committee on Publications and SED officers are in gaps; the editorial coordinator is in staff rows. The JSTOR and publisher source PDFs are not published (the JBES front matter prints staff contact emails and a phone number). `editors_backfill_scale_spotcheck.csv` is byte-identical to the phone/fax-scrubbed web copy. Change logs: `RED_2025_board_changes_20261113.csv`, `JBES_2019_board_changes_20261113.csv`, `JBES_2020_board_changes_20261113.csv`. The directory site does not read it.

In `editors_backfill_red_gap_20261112` (published 2026-11-12 with user approval, PR #70, kept in the tree): It supersedes `editors_ra_ta_merge_rebuild_20261112` (PR #69): Review of Economic Dynamics 2022 (43 rows, `#15578`–`#15620`) and 2023 (43 rows, `#15621`–`#15663`) added from the Society for Economic Dynamics “Our Editors” page via Wayback (page versions modified 2021-04-14 and 2023-02-21; captures 20220219234913 and 20230324123429), each with a matching long-table row; the RED 2021 inventory row is fixed to `ok_issue_front_matter` 45/45; RED 2021–2023 gaps `blocked` → `resolved`; the RED match-rate row recomputed. 31 distinct RORs on the new rows, all API-active; #15638 Anmol Bhandari stays blank (no institution printed). `editors_backfill_scale_spotcheck.csv` is byte-identical to the phone/fax-scrubbed web copy. Change log: `RED_2022_2023_board_changes_20261112.csv`. The directory site does not read it.

In `editors_ra_ta_merge_rebuild_20261112` (published 2026-11-12 with user approval, kept in the tree): It is a mechanical rebuild of the held `editors_ra_ta_merge_20261106` onto `editors_backfill_scale_ror_20261031`: 20 RA/TA and FIX-retry rows updated (S01–S20; S11 Lochner → Western Ontario, S14 Carlton → Chicago Booth, S20 Castanheira → ECARES with ROR blank), Review of Economic Dynamics 2021 added (45 rows, `#15446`–`#15490`; three SED officers in gaps), and Journal of Business and Economic Statistics 2018 added (87 rows, `#15491`–`#15577`; the ASA Committee on Publications in gaps, editorial coordinator Jamie Hutchens in staff rows). The directory site does not read it; it shows current boards only. `editors_backfill_scale_spotcheck.csv` keeps the phone/fax-scrubbed copy from `editors_backfill_scale_ror_20261031`. Change logs: `RA_TA_merge_changes_20261106.csv`, `RA_FIX_retry_changes_20261106.csv`, `RED_2021_board_changes_20261106.csv`, `JBES_2018_board_changes_20261106.csv`.

Previous: `releases/editors_backfill_scale_ror_20261031/` — published 2026-11-01 with user approval together with the current-board freeze `editors_ror_consistency3b_20261101`; kept in the tree.

| File | Rows | Notes |
|------|-----:|-------|
| `editors_backfill_scale_ror_panel.csv` | 15,873 | 39 journals; was 15,664 (+209 RED 2025, JBES 2019/2020). In `editors_backfill_red_gap_20261112`: 15,664, was 15,578 (+86 RED 2022/2023). In `editors_ra_ta_merge_rebuild_20261112`: 15,578, was 15,446 (+132 new, 20 changed). In `editors_backfill_scale_ror_20261031`: 301 journal-years. Matched 11,021; unmatched 360; no affiliation 4,017; staff excluded 48 |
| `editor_affiliations.csv` | 12,102 | One row per affiliation part, keyed by `editor_row_key` |
| `editors_backfill_scale_row_key_crosswalk.csv` | 15,446 | Old to new `editor_row_key` (8,723 keys shifted after a parse fix) |
| `editors_backfill_scale_matched.csv` / `_unmatched.csv` | 1,847 / 86 | Distinct affiliation strings and their ROR decision |
| `editors_backfill_scale_gaps.csv` | 4,620 | Journal-years and rows with missing coverage |
| `editors_backfill_scale_inventory.csv` | 312 | Journal-year source inventory |
| `editors_backfill_scale_spotcheck.csv` | 301 | QC sample. Phone/fax fragments removed from 30 cells |
| `BACKFILL_SCALE_ROR_*.csv`, `_build.json`, `README.md` | | Small audit logs and the collector manifest |

The inventory row for Review of Economic Dynamics 2021 reads `ok_issue_front_matter`, 45 of 45 rows (fixed in `editors_backfill_red_gap_20261112`; it read `blocked` / 0 in `editors_ra_ta_merge_rebuild_20261112`). RED 2025 and JBES 2019/2020 read `ok_issue_front_matter` (44/44, 87/84, 78/75) in `editors_backfill_red_jbes_20261113`.

No `raw_html/`, scrape caches, emails, phones, or photos are in the repo. `source_file` columns name collector capture paths only. No file is over 50 MB, so nothing is gzipped. Report: `docs/reports/BACKFILL_scale_ror_20261031.md`.

## Known coverage gaps

- Review of Economic Dynamics 2024 (RA pack 2 item S22). Filled: 2021 in `editors_ra_ta_merge_rebuild_20261112`; 2022 and 2023 in `editors_backfill_red_gap_20261112`; 2025 in `editors_backfill_red_jbes_20261113`.
- Journal of Business & Economic Statistics 2025 (RA pack 2 item S23). Filled: 2018 in `editors_ra_ta_merge_rebuild_20261112`; 2019 and 2020 in `editors_backfill_red_jbes_20261113`.
- Journal of Risk and Uncertainty (JRU) 2023 (still not found).
- Journal of Urban Economics 2018–2019 partial.
- Economic Journal 2018 low confidence.
- About 4,017 names-only rows: AER, AER: Insights, JPE, JOLE, JLE, and QJE print no affiliations, so those rows are intentionally blank.

## Open ROR decisions (left blank, not guessed)

"Virginia University, Charlottesville" → University of Virginia (`0153tk833`?), INRA-AgroParisTech, the Adelaide and Cergy-Pontoise successor organizations, ECARES / CORE, the Cowles Foundation, and CEU Budapest.

## Superseded

The older collector panels (`editors_panel_2018_2026_with_ror.csv` and window slices) and the scale-parse packs are superseded by this release and are not copied here.
