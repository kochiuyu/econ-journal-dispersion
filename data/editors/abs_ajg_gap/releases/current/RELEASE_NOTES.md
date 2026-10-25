# editors_display_names_20261025

Display names on the ABS/AJG gap current boards, cleaned 2026-10-25 20:20 Asia/Hong_Kong. The journal set is still freeze `editors_abs_ajg_gap_20261025`: AJG titles that are not already in the FT50 or ABDC editor files. Grades, tenure columns, and the empty ROR columns were not edited. There is still no `faculty_profile_url`.

`editor_name` is the name the directory shows. `editor_name_raw` is the pre-clean value when the name changed, and blank when it did not. The build does not invent a name and does not display `editor_name_raw`.

`CHANGE_LOG.csv` from the collector freeze is about 6MB and is not used by the site. It is not in this repository.

## Files in this repository

The collector cleaned the live panels (11,288 / 5,032 / 3,490). Fourteen of those rows were already excluded from `editors_abs_ajg_gap_20261025` as drop-quality chrome (publisher navigation, a paper title, a metrics line, and similar). They stay out of these files. One of the fourteen was a case fix (`INFORMATION FOR` → `Information For`), so the committed ajg1 file has 602 changed names rather than 603.

| File | Rows | Changed | Degrees stripped | Case fixed | Initials expanded | Bare initials left |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,490 | 52 | 48 | 0 | 4 | 257 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,030 | 106 | 87 | 1 | 18 | 272 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,276 | 602 | 496 | 108 | 10 | 167 |

Degree, case, and initial columns for ajg1 are the collector's live-panel counts except the one excluded case fix. The other excluded rows were not name changes.

Collector totals across every live panel, including both FT50 files: 179,571 rows, 21,732 changed, 17,757 degrees stripped, 2,933 case fixes, 1,306 initials expanded, 2,928 bare initials left as printed. After the fourteen-row exclusion, the files committed here (all panels) are 179,557 rows and 21,731 changed names.

## Rules

Strip trailing degrees and leading titles, turn ALL-CAPS person names into title case, and expand a bare given initial only from another row with the same initial, surname, and `ror_id`, normalized affiliation, or faculty URL. No invented givens. Bare initials with no such evidence stay as printed.

## Public site

`scripts/build_site.py` reads these three CSVs. ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site. There is no `faculty_profile_url`, so person names stay plain text. A board link is `source_url` when that value is http(s).

Eight prio43 rows whose `editor_name` is `Email` (Nature Human Behaviour) stay in the CSV and are omitted from the directory by the existing non-person name filter. The ROR columns are empty, so those appointments group by affiliation text.

Do not merge these boards into the ABDC files.
