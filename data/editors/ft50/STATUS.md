# Editors — FT50

Updated: 2026-11-01 (Asia/Hong_Kong)

## Release in this repo

`releases/current/`

| File | Notes |
|------|-------|
| `editors_ft50_current.csv` | Current boards (year≈2026). 10,047 rows. `raw_affiliation` on 9,941. ROR columns added in `editors_ror_consistency3b_20261101`; `ror_id` on 9,600 |
| `editors_ft50_current_with_ror.csv` | Same rows, plus ROR. This is the file the directory reads. `raw_affiliation` on 9,946. `ror_id` on 9,673 (was 9,864) |

Excluded: `raw/`, `*.before_impute.*`, Excel duplicates, and collector audit CSVs.

## Scope

Current editorial boards only (no Wayback history in this stream). Catalog: `journals/catalog_ft50.csv` (FT Research rank list, Apr 2026 revision). The catalog `field` column is the McMaster LibGuide subject area (https://libguides.mcmaster.ca/ft-top50) used on Rankings. The directory field stays the ABDC `field_for`.

Freeze `editors_ror_consistency3b_20261101` (published 2026-11-01) is the current board. It supersedes `editors_browser_single_20261029` and retires the unpublished collector packs in between (consistency2, consistency, multiaff, campus2, campus, post15, pilot, the scale-parse packs, and the t39 / institution-fix freezes). Twelve columns follow `board_urls` and `board_url_count` (see `docs/README.md`), so the board columns are no longer last. The collector blanks ambiguous ROR ids, so `ror_id` coverage is lower. Emails and phone numbers left in text cells were removed. Long table and audit logs: `data/editors/releases/editors_ror_consistency3b_20261101/`. Reports: `docs/reports/`. Details: `releases/current/RELEASE_NOTES.md`. The history below describes earlier freezes. On FT50 two Review of Economic Studies `Universitat Pompeu Fabra` institution-as-name rows are dropped and three Top 5 seats the collector added only to ABDC A* (Erik Snowberg and Juan Carlos Suárez Serrato on AER, Mikkel Plagborg-Moller on REStud) are copied in, so both files are 10,047 rows.

Previous: freeze `editors_browser_single_20261029` (2026-10-30 07:09 Asia/Taipei). It supersedes `editors_single_editor_20261029`, which superseded `editors_browser_boards_20261029`. Both FT50 files are unchanged in `editors_browser_single_20261029`; its board changes are on ABDC A and C. Both FT50 files stay 10,046 rows. Each file gains blank `board_urls` and `board_url_count` columns. The board changes are on ABDC A, ABDC B, ABDC C, and AJG 1. Empty `editor_name` is 1 (`Read more` on Review of Economic Studies). The directory reads `editors_ft50_current_with_ror.csv` and does not list an empty name.

`faculty_profile_url` is filled on 8,375 of 10,046 rows (83.4%) in both files. On the ROR file, `raw_affiliation` is filled on 9,946 rows (99.0%) and `ror_id` on 9,864 (98.2%). The slim file has `raw_affiliation` on 9,942 rows and no ROR columns. A faculty URL with no `ror_id` is 48. Two medium hits that name a different organization stay unpublished (University of Goma for University of Maryland, EAE Business School for ESADE). Tom P. Moliterno uses the Citadel ROR already on these boards, `https://ror.org/01vwr6t80`. No name, ROR, or URL was invented. Jaap Paauwe’s display name is `Jaap Paauwe`; `editor_name_raw` keeps `Jaap Paauwe, Tilburg` so the ABDC copy of that Human Resource Management seat stays one row. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay. Notes: `releases/current/RELEASE_NOTES.md`.

ABDC and AJG-gap panels are the same freeze, in their own `releases/current/` folders.

The public directory also tags two subsets of this freeze. Top 5 (`journals/catalog_top5.csv`) is AER, Econometrica, JPE, QJE, and ReStud. Twenty-three UTD24 journals (`journals/catalog_utd24.csv`) are tagged here as well. Neither tag is a separate editor release.
