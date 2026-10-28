# Editors — FT50

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/`

| File | Notes |
|------|-------|
| `editors_ft50_current.csv` | Current boards (year≈2026). 10,046 rows. `raw_affiliation` on 9,957 |
| `editors_ft50_current_with_ror.csv` | Same rows, plus ROR. This is the file the directory reads. `raw_affiliation` on 9,956. `ror_id` on 9,867 |

Excluded: `raw/`, `*.before_impute.*`, Excel duplicates, and collector audit CSVs.

## Scope

Current editorial boards only (no Wayback history in this stream). Catalog: `journals/catalog_ft50.csv` (FT Research rank list, Apr 2026 revision). The catalog `field` column is the McMaster LibGuide subject area (https://libguides.mcmaster.ca/ft-top50) used on Rankings. The directory field stays the ABDC `field_for`.

Freeze `editors_institution_paren_geo_20261028` is the current board (2026-10-28 16:39 Asia/Hong_Kong). It supersedes `editors_institution_nonsense_20261028`. Both files stay 10,046 rows. Empty `editor_name` is 0. The directory reads `editors_ft50_current_with_ror.csv` and does not list an empty name.

`faculty_profile_url` is filled on 8,375 of 10,046 rows (83.4%) in both files. On the ROR file, `raw_affiliation` is filled on 9,956 rows (99.1%) and `ror_id` on 9,867 (98.2%). The slim file has `raw_affiliation` on 9,957 rows. A faculty URL with no `ror_id` is 57. Three of those are medium hits that name a different organization (University of Goma, EAE Business School, The Citadel Foundation). The affiliation text on those rows stays. No name, ROR, or URL was invented. Jaap Paauwe’s display name is `Jaap Paauwe`; `editor_name_raw` keeps `Jaap Paauwe, Tilburg` so the ABDC copy of that Human Resource Management seat stays one row. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay. Notes: `releases/current/RELEASE_NOTES.md`.

ABDC and AJG-gap panels are the same freeze, in their own `releases/current/` folders.

The public directory also tags two subsets of this freeze. Top 5 (`journals/catalog_top5.csv`) is AER, Econometrica, JPE, QJE, and ReStud. Twenty-three UTD24 journals (`journals/catalog_utd24.csv`) are tagged here as well. Neither tag is a separate editor release.
