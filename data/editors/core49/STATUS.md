# Editors — core49

Updated: 2026-11-01 (Asia/Hong_Kong)

## Release in this repo

`releases/editors_backfill_scale_ror_20261031/` — multi-year core49 editor backfill with ROR, published 2026-11-01 with user approval together with the current-board freeze `editors_ror_consistency3b_20261101`. The directory site does not read it; it shows current boards only.

| File | Rows | Notes |
|------|-----:|-------|
| `editors_backfill_scale_ror_panel.csv` | 15,446 | 39 journals, 301 journal-years. Matched 11,021; unmatched 360; no affiliation 4,017; staff excluded 48 |
| `editor_affiliations.csv` | 11,661 | One row per affiliation part, keyed by `editor_row_key` |
| `editors_backfill_scale_row_key_crosswalk.csv` | 15,446 | Old to new `editor_row_key` (8,723 keys shifted after a parse fix) |
| `editors_backfill_scale_matched.csv` / `_unmatched.csv` | 1,847 / 86 | Distinct affiliation strings and their ROR decision |
| `editors_backfill_scale_gaps.csv` | 4,539 | Journal-years and rows with missing coverage |
| `editors_backfill_scale_inventory.csv` | 312 | Journal-year source inventory |
| `editors_backfill_scale_spotcheck.csv` | 301 | QC sample. Phone/fax fragments removed from 30 cells |
| `BACKFILL_SCALE_ROR_*.csv`, `_build.json`, `README.md` | | Small audit logs and the collector manifest |

No `raw_html/`, scrape caches, emails, phones, or photos are in the repo. `source_file` columns name collector capture paths only. No file is over 50 MB, so nothing is gzipped. Report: `docs/reports/BACKFILL_scale_ror_20261031.md`.

## Known coverage gaps

- Review of Economic Dynamics 2021–2025.
- Journal of Business & Economic Statistics 2018–2020 and 2025.
- Journal of Risk and Uncertainty (JRU) 2023.
- Journal of Urban Economics 2018–2019 partial.
- Economic Journal 2018 low confidence.
- About 4,017 names-only rows: AER, AER: Insights, JPE, JOLE, JLE, and QJE print no affiliations, so those rows are intentionally blank.

## Open ROR decisions (left blank, not guessed)

"Virginia University, Charlottesville" → University of Virginia (`0153tk833`?), INRA-AgroParisTech, the Adelaide and Cergy-Pontoise successor organizations, ECARES / CORE, the Cowles Foundation, and CEU Budapest.

## Superseded

The older collector panels (`editors_panel_2018_2026_with_ror.csv` and window slices) and the scale-parse packs are superseded by this release and are not copied here.
