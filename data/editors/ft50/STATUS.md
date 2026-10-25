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

Freeze `editors_current_20261025`: both files in `releases/current/` add `faculty_profile_url`, `faculty_home_page`, `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key`. The slim CSV is the freeze file. `editors_ft50_current_with_ror.csv` keeps its existing ROR columns and receives those `faculty_*` values from the same row order. Notes: `releases/current/RELEASE_NOTES.md` and `../abdc/releases/current/RELEASE_NOTES.md`.

The public directory also tags two subsets of this freeze. Top 5 (`journals/catalog_top5.csv`) is AER, Econometrica, JPE, QJE, and ReStud. Twenty-three UTD24 journals (`journals/catalog_utd24.csv`) are tagged here as well. Neither tag is a separate editor release.
