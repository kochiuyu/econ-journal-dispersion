# editors_display_names_20261025

Display names on the ABDC current boards, cleaned 2026-10-25 20:20 Asia/Hong_Kong. Faculty-profile columns, tenure columns, and `ror_id` are the `editors_current_20261025` values and were not edited. FT50 notes are in [`../../../ft50/releases/current/RELEASE_NOTES.md`](../../../ft50/releases/current/RELEASE_NOTES.md).

`editor_name` is the name the directory shows. `editor_name_raw` is the pre-clean value when the name changed, and blank when it did not. The build does not invent a name and does not display `editor_name_raw`.

`CHANGE_LOG.csv` from the collector freeze is about 6MB and is not used by the site. It is not in this repository.

## Rules

1. Strip trailing degrees and credentials and leading titles (Dr., Prof., Professor).
2. Turn ALL-CAPS person names into title case. Particles such as `van` and `de` stay lowercase in the middle of a name.
3. Expand a bare given initial only from another row with the same initial, the same surname, and the same `ror_id`, normalized `raw_affiliation`, or faculty URL. Conflicts stay as printed.

## Files

| File | Rows | Changed | Degrees stripped | Case fixed | Initials expanded | Bare initials left |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,190 | 3,996 | 3,093 | 548 | 391 | 496 |
| `editors_abdc_a_current.csv` | 45,363 | 6,803 | 5,855 | 565 | 419 | 683 |
| `editors_abdc_b_current.csv` | 42,193 | 4,268 | 3,268 | 931 | 226 | 542 |
| `editors_abdc_c_current.csv` | 26,915 | 3,139 | 2,744 | 383 | 34 | 267 |

Collector totals across every live panel, including both FT50 files: 179,571 rows, 21,732 changed, 17,757 degrees stripped, 2,933 case fixes, 1,306 initials expanded, 2,928 bare initials left as printed.

A few cells differed from the previous public file only by a repeated space, a tab, or a non-breaking space (`Serdar  Simsek`, `Masaaki Fukasawa`). `editor_name_raw` is blank on those rows. The directory already collapsed that whitespace.

Journal of Operations Management associate editor `S. Dhanorkar` stays `S. Dhanorkar` on the A* file. The FT50 copy of that seat was expanded to `Suvrat Dhanorkar` because the faculty URL is on the FT50 row. The directory shows the FT50 name and keeps the ABDC A* badge. The A* cell was not rewritten.

## Examples

| Change | Before | After |
|---|---|---|
| Degree | `John Campbell, PhD` | `John Campbell` |
| Case | `EDWARD MAYDEW` | `Edward Maydew` |
| Case | `LISA DE SIMONE` | `Lisa de Simone` |
| Initial | `A. Azadegan` | `Arash Azadegan` |

Names that already have a full given after an initial stay as printed (`R. Preston McAfee`). A bare initial with no matching fuller row stays as printed.

## Unchanged from editors_current_20261025

| File | Rows | `faculty_profile_url` | `faculty_home_page` |
|---|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,190 | 8,467 (33.6%) | 3,565 (14.2%) |
| `editors_abdc_a_current.csv` | 45,363 | 5,202 (11.5%) | 1,758 (3.9%) |
| `editors_abdc_b_current.csv` | 42,193 | 3,129 (7.4%) | 1,192 (2.8%) |
| `editors_abdc_c_current.csv` | 26,915 | 1,228 (4.6%) | 486 (1.8%) |

`scripts/build_site.py` passes a non-empty `faculty_profile_url` into the directory. The directory links the person name only when that URL is http(s) and does not contain an email. Tenure columns stay on the CSVs. The public directory does not display them. Emails, phone numbers, and photos are not written to the site. There is no raw HTML in this release.
