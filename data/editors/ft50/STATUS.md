# Editors — FT50

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/`

| File | Notes |
|------|-------|
| `editors_ft50_current.csv` | Current boards (year≈2026). 10,046 rows |
| `editors_ft50_current_with_ror.csv` | Same rows, plus ROR. This is the file the directory reads |

Excluded: `raw/`, `*.before_impute.*`, Excel duplicates, and the collector audit CSVs from freeze `editors_name_swap_abdc_ajg_20261028`.

## Scope

Current editorial boards only (no Wayback history in this stream). Catalog: `journals/catalog_ft50.csv` (FT Research rank list, Apr 2026 revision). The catalog `field` column is the McMaster LibGuide subject area (https://libguides.mcmaster.ca/ft-top50) used on Rankings. The directory field stays the ABDC `field_for`.

Freeze `editors_name_swap_abdc_ajg_20261028`: name and institution corrections on both files. This supersedes `editors_name_swap_20261028`. Review of Economic Studies has no orphan rows named `CEMFI` or `Sciences Po`. Kurt Mitman is affiliated to CEMFI with ROR `https://ror.org/035h6g182` (high). Two LMU-only orphan rows were dropped after the person rows were filled. `editor_name` is the directory name. These files have no empty `editor_name`. `faculty_profile_url` is filled on 8,360 of 10,046 rows (83.2%) in both files. Twelve URLs present only on the slim file were copied onto blank ROR rows. Notes: `releases/current/RELEASE_NOTES.md`.

The same freeze updates ABDC A*, A, B, and C (`../abdc/releases/current/`) and the AJG-gap panels (`../abs_ajg_gap/releases/current/`).

The public directory also tags two subsets of this freeze. Top 5 (`journals/catalog_top5.csv`) is AER, Econometrica, JPE, QJE, and ReStud. Twenty-three UTD24 journals (`journals/catalog_utd24.csv`) are tagged here as well. Neither tag is a separate editor release.
