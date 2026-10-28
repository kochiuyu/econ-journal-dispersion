# Editors — FT50

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/`

| File | Notes |
|------|-------|
| `editors_ft50_current.csv` | Current boards (year≈2026). 10,046 rows. `raw_affiliation` on 9,944. No ROR columns |
| `editors_ft50_current_with_ror.csv` | Same rows, plus ROR. This is the file the directory reads. `raw_affiliation` on 9,948. `ror_id` on 9,885 |

Excluded: `raw/`, `*.before_impute.*`, Excel duplicates, and collector audit CSVs.

## Scope

Current editorial boards only (no Wayback history in this stream). Catalog: `journals/catalog_ft50.csv` (FT Research rank list, Apr 2026 revision). The catalog `field` column is the McMaster LibGuide subject area (https://libguides.mcmaster.ca/ft-top50) used on Rankings. The directory field stays the ABDC `field_for`.

Freeze `editors_institution_empty_country_20261028` is the current board (2026-10-28 20:41 Asia/Hong_Kong). It supersedes `editors_institution_post31_touchup_20261028` for Directory Institutions. Both files stay 10,046 rows. Empty `editor_name` is 1 (`Read more` on Review of Economic Studies). The directory reads `editors_ft50_current_with_ror.csv` and does not list an empty name.

`faculty_profile_url` is filled on 8,375 of 10,046 rows (83.4%) in both files. On the ROR file, `raw_affiliation` is filled on 9,948 rows (99.0%) and `ror_id` on 9,885 (98.4%). The slim file has `raw_affiliation` on 9,944 rows and no ROR columns. A faculty URL with no `ror_id` is 39. Two medium hits that name a different organization stay unpublished (University of Goma for University of Maryland, EAE Business School for ESADE). Tom P. Moliterno uses the Citadel ROR already on these boards, `https://ror.org/01vwr6t80`. No name, ROR, or URL was invented. Jaap Paauwe’s display name is `Jaap Paauwe`; `editor_name_raw` keeps `Jaap Paauwe, Tilburg` so the ABDC copy of that Human Resource Management seat stays one row. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay. Notes: `releases/current/RELEASE_NOTES.md`.

ABDC and AJG-gap panels are the same freeze, in their own `releases/current/` folders.

The public directory also tags two subsets of this freeze. Top 5 (`journals/catalog_top5.csv`) is AER, Econometrica, JPE, QJE, and ReStud. Twenty-three UTD24 journals (`journals/catalog_utd24.csv`) are tagged here as well. Neither tag is a separate editor release.
