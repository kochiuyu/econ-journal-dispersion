# editors_trailing_country_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Keyed, user-approved trailing-country fix on the published Directory copy of `editors_raw_aff_part_no_fix_20261110` (PR #52), which it supersedes. Collector pack: `/workspace/econ-journal-editors/releases/editors_trailing_country_fix_20261110`.

Only the fields in the publish-set rows of the field-level change log were written (`canonical_name`, `ror_country`, `continent`; plus `ror_id` / `ror_name` / `lat` / `lon` / `is_panel_ror` on REMATCH-with-ROR rows), keyed by `editor_row_key`, each checked against its `old` value (0 mismatches). The printed `raw_affiliation` and long `raw_aff_part` are untouched. Pilot rows (10,722) are not applied and `*_with_profile_pilot.csv` is not published. Every `ror_id` written already exists on the panels.

**Held back (11 rows, 44 cells):** rows whose stripped `canonical_name` would end in a dangling conjunction — `Italy &`, `Greece and`, `SE`, `Justice of the Supreme Court, England and`, `Lord Justice of Appeal, Court of Appeal of England and`, `Court of Appeal of England and`, `Court of Appeal, England and`, `Independent Scholar - Iran &`, `Solicitor, Australia, New Zealand and`, `Independent Scholar, UK and`, `Finland and`. They keep their printed name and blank country.

| File | Rows changed |
|---|---:|
| editors_ft50_current_with_ror.csv | 84 |
| editors_ft50_current.csv (country only) | 81 |
| editors_abdc_a_star_current.csv | 273 |
| editors_abdc_a_current.csv | 1,096 |
| editors_abdc_b_current.csv | 1,682 |
| editors_abdc_c_current.csv | 1,728 |
| editors_abs_ajg_gap_prio43_current.csv | 52 |
| editors_abs_ajg_gap_ajg2_current.csv | 198 |
| editors_abs_ajg_gap_ajg1_current.csv | 842 |
| **Panels total** | **6,036** |
| editor_affiliations.csv.gz (long rows) | 6,036 |

Row counts unchanged; ajg1 12,316 and ajg2 5,462 with the navigation rows out.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,514,482 bytes; 63,439,165 bytes uncompressed, md5 `b3b40188b8455e283b5f22ab8ed53aac`). 181,443 rows, same 20 columns, starts from the #52 table.

## Files

- `editor_affiliations.csv.gz` — long table
- `TRAILING_COUNTRY_changes_20261110.csv` — collector field-level change log (34,364 rows incl. pilot and held rows)
- `TRAILING_COUNTRY_skipped_20261110.csv` — collector skip list (96 Institutions + 7 rows)
- `SENDTO_BLURB.txt`, `COLLECTOR_RELEASE_NOTES.md` — collector notes
- `README.md` — this file
