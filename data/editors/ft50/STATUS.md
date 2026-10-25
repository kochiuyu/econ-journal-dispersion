# Editors — FT50

Updated: 2026-10-25 (Asia/Hong_Kong)

## Release in this repo

`releases/current/`

| File | Notes |
|------|-------|
| `editors_ft50_current.csv` | Current boards (year≈2026) |
| `editors_ft50_current_with_ror.csv` | Same + ROR enrichment |

Excluded: `raw/`, `*.before_impute.*`, Excel duplicates.

## Scope

Current editorial boards only (no Wayback history in this stream). Catalog: `journals/catalog_ft50.csv` (FT Research rank list, Apr 2026 revision). The catalog `field` column is the McMaster LibGuide subject area (https://libguides.mcmaster.ca/ft-top50) used on Rankings. The directory field stays the ABDC `field_for`.

Freeze `editors_display_names_20261025`: `editor_name` is the cleaned display name (degrees and leading titles removed, ALL-CAPS names in title case, bare initials expanded only from another row with the same identity evidence). When the name changed, the previous value is `editor_name_raw`. The directory shows `editor_name`. Notes: `releases/current/RELEASE_NOTES.md`.

Faculty columns are still freeze `editors_ft50_faculty_20261025`. Both files carry `faculty_profile_url`, `faculty_home_page`, `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key`. `faculty_profile_url` is filled on 8,199 of 10,050 rows (81.6%), up from 4,724 (47.0%) in `editors_current_20261025`. 1,851 rows are still blank. Those columns were not edited by the display-name freeze. `editors_ft50_current_with_ror.csv` keeps its ROR columns.

The same display-name freeze updates ABDC (`../abdc/releases/current/`) and the AJG-gap panels (`../abs_ajg_gap/releases/current/`).

The public directory also tags two subsets of this freeze. Top 5 (`journals/catalog_top5.csv`) is AER, Econometrica, JPE, QJE, and ReStud. Twenty-three UTD24 journals (`journals/catalog_utd24.csv`) are tagged here as well. Neither tag is a separate editor release.
