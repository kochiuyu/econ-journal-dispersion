# Editors — FT50

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/`

| File | Notes |
|------|-------|
| `editors_ft50_current.csv` | Current boards (year≈2026). 10,046 rows |
| `editors_ft50_current_with_ror.csv` | Same rows, plus ROR. This is the file the directory reads |

Excluded: `raw/`, `*.before_impute.*`, Excel duplicates, and collector audit CSVs.

## Scope

Current editorial boards only (no Wayback history in this stream). Catalog: `journals/catalog_ft50.csv` (FT Research rank list, Apr 2026 revision). The catalog `field` column is the McMaster LibGuide subject area (https://libguides.mcmaster.ca/ft-top50) used on Rankings. The directory field stays the ABDC `field_for`.

Freeze `editors_ft50_url_aff_20261028` is the current board (2026-10-28, Asia/Hong_Kong). It fills `raw_affiliation` and ROR for editors who already had `faculty_profile_url` and a missing or unusable institution. Both files stay 10,046 rows. Empty `editor_name` is 0. The directory reads `editors_ft50_current_with_ror.csv` and does not list an empty name.

`faculty_profile_url` is filled on 8,375 of 10,046 rows (83.4%) in both files. `raw_affiliation` is filled on 9,960 rows (99.1%). A faculty URL with no university is 0. A faculty URL with no `ror_id` is 3: three medium ROR hits were not published because the ROR name is a different organization (University of Goma, EAE Business School, The Citadel Foundation). The affiliation text on those rows stays. No name, ROR, or URL was invented. Jaap Paauwe’s display name is `Jaap Paauwe`; `editor_name_raw` keeps `Jaap Paauwe, Tilburg` so the ABDC copy of that Human Resource Management seat stays one row. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). Notes: `releases/current/RELEASE_NOTES.md`.

ABDC and AJG-gap panels are not part of this freeze.

The public directory also tags two subsets of this freeze. Top 5 (`journals/catalog_top5.csv`) is AER, Econometrica, JPE, QJE, and ReStud. Twenty-three UTD24 journals (`journals/catalog_utd24.csv`) are tagged here as well. Neither tag is a separate editor release.
