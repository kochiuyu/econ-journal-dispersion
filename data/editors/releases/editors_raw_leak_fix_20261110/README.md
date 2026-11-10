# editors_raw_leak_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** This is a keyed, user-approved raw-leak fix on the published Directory copy of `editors_raw_drift_fix_20261110` (PR #53), which it supersedes. Collector pack: `/workspace/econ-journal-editors/releases/editors_raw_leak_fix_20261110`.

## What was applied

- **`RAW_LEAK_directory_diff_20261110.csv`:** all 341 cells, keyed by file and `editor_row_key`. Every `directory_value` matched the Directory copy (0 mismatches).
  - 161 `raw_affiliation` cells.
  - 44 `canonical_name` cells.
  - The matching `ror_id`, `ror_name`, `ror_country`, `continent`, `lat` and `lon` cells.
- **`ror_notes`:** the Collector's `raw_leak_fix_20261110` trace was appended on those rows and on Qiang Meng A* #18960, which stays NUS with a note. The slim FT50 file has no `ror_notes` column.
- **Long table:** the 161 matching parts take the Collector's `raw_aff_part`, `ror_*`, `is_panel_ror` and `ror_match_note`. The 6 parts for the Top 5 seats FT50 #10046–#10048 (both FT50 files) are added from the Collector's table at their panel position, so the table goes from 181,443 to 181,449 rows.

## Not taken from the Collector

- **`faculty_profile_url`:** it stays blank on A #15895 and A* #13053, because the Collector's value carried an e-mail address.
- **FT50 #3821 (Jaap Paauwe):** it already has `editor_name` `Jaap Paauwe` and Tilburg University `04b8v1s79` in both files. `editor_name_raw` keeps `Jaap Paauwe, Tilburg`. The ABDC A* HRM copy of this seat (#2545) still has that spelling as its `editor_name`, and the build uses `editor_name_raw` to merge the FT50 row with its ABDC copy. With it blank, the build's check that every FT50 row has an ABDC partner fails.
- **Excluded rows:** the Pompeu Fabra rows and the AJG1 navigation rows stay out.
- **Pilot panels:** not published.

## New ROR ids on the panels

Both were checked on the ROR API v2 (active):
- `03m7qjm52` Universitas Galuh
- `05534qc24` SAGE Publishing (United States)

## Rows changed

| File | Rows changed |
|---|---:|
| editors_abdc_a_star_current.csv | 12 |
| editors_abdc_a_current.csv | 31 |
| editors_abdc_b_current.csv | 45 |
| editors_abdc_c_current.csv | 47 |
| editors_abs_ajg_gap_prio43_current.csv | 3 |
| editors_abs_ajg_gap_ajg2_current.csv | 6 |
| editors_abs_ajg_gap_ajg1_current.csv | 13 |
| editors_ft50_current_with_ror.csv | 3 |
| editors_ft50_current.csv | 2 |
| **Panels total** | **162** |
| editor_affiliations.csv.gz | 161 changed + 6 added |

Panel row counts are unchanged: ajg1 12,316, ajg2 5,462, FT50 10,047.

## Long table

`editor_affiliations.csv.gz`: gzip -9 -n, 7,542,833 bytes; 63,538,172 bytes uncompressed; md5 `35820c8fb728a380a9792373164c8c05`. It has 181,449 rows and 20 columns.

## Files

- `RAW_LEAK_changes_20261110.csv`, `RAW_LEAK_directory_diff_20261110.csv`, `RAW_LEAK_skipped_20261110.csv`, `RAW_LEAK_source_verification_20261110.csv`: the Collector's logs.
- `raw_leak_fix_20261110.py`, `HANDOFF.md`, `SENDTO_BLURB.txt`, `COLLECTOR_RELEASE_NOTES.md`: the Collector's script and notes.
- `README.md`: this file.

The folder contains no e-mail addresses or phone numbers.
