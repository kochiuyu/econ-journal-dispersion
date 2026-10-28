# Editors — FT50

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/`

| File | Notes |
|------|-------|
| `editors_ft50_current.csv` | Current boards (year≈2026). 10,046 rows. `raw_affiliation` on 9,942. No ROR columns |
| `editors_ft50_current_with_ror.csv` | Same rows, plus ROR. This is the file the directory reads. `raw_affiliation` on 9,946. `ror_id` on 9,864 |

Excluded: `raw/`, `*.before_impute.*`, Excel duplicates, and collector audit CSVs.

## Scope

Current editorial boards only (no Wayback history in this stream). Catalog: `journals/catalog_ft50.csv` (FT Research rank list, Apr 2026 revision). The catalog `field` column is the McMaster LibGuide subject area (https://libguides.mcmaster.ca/ft-top50) used on Rankings. The directory field stays the ABDC `field_for`.

Freeze `editors_institution_residual_post35_20261028` is the current board (2026-10-28 23:40 Asia/Hong_Kong). It supersedes `editors_institution_dept_country_20261028` for Directory Institutions. Both FT50 files stay 10,046 rows and are unchanged in this publish: the collector’s FT50 touches would have copied `Italian Cultural Institute` onto University of Tokyo mastheads, and those rows stay as published. Empty `editor_name` is 1 (`Read more` on Review of Economic Studies). The directory reads `editors_ft50_current_with_ror.csv` and does not list an empty name.

`faculty_profile_url` is filled on 8,375 of 10,046 rows (83.4%) in both files. On the ROR file, `raw_affiliation` is filled on 9,946 rows (99.0%) and `ror_id` on 9,864 (98.2%). The slim file has `raw_affiliation` on 9,942 rows and no ROR columns. A faculty URL with no `ror_id` is 48. Two medium hits that name a different organization stay unpublished (University of Goma for University of Maryland, EAE Business School for ESADE). Tom P. Moliterno uses the Citadel ROR already on these boards, `https://ror.org/01vwr6t80`. No name, ROR, or URL was invented. Jaap Paauwe’s display name is `Jaap Paauwe`; `editor_name_raw` keeps `Jaap Paauwe, Tilburg` so the ABDC copy of that Human Resource Management seat stays one row. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay. Notes: `releases/current/RELEASE_NOTES.md`.

ABDC and AJG-gap panels are the same freeze, in their own `releases/current/` folders.

The public directory also tags two subsets of this freeze. Top 5 (`journals/catalog_top5.csv`) is AER, Econometrica, JPE, QJE, and ReStud. Twenty-three UTD24 journals (`journals/catalog_utd24.csv`) are tagged here as well. Neither tag is a separate editor release.
