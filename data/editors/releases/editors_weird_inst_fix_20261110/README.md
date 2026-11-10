# editors_weird_inst_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Keyed, user-approved weird Institution-name fix (DROP / STRIP / SET_COUNTRY / REMATCH / University of Georgia) on the published Directory copy of `editors_country_misprint_fix_20261110` (PR #53), which it supersedes. Collector pack: `/workspace/econ-journal-editors/releases/editors_weird_inst_fix_20261110`.

Only the publish-set cells of the field-level change log were written, keyed by `editor_row_key` (long: `editor_row_key` + `panel_file` + `aff_rank`), each checked against its `old` value. 2 cells differed from the Directory copy and were resolved by hand (A* #11663 `ror_notes`: DROP trace appended to the published note; C #12376 `canonical_name`: Collector `old` still had an email the Directory had removed, set to `Dan Swanson & Associates`). Every other changed panel row equals the Collector freeze row. Pilot rows are not applied and `*_with_profile_pilot.csv` is not published. Every new `ror_id` already exists on the panels.

| File | Rows changed |
|---|---:|
| editors_abdc_a_star_current.csv | 117 |
| editors_abdc_a_current.csv | 352 |
| editors_abdc_b_current.csv | 350 |
| editors_abdc_c_current.csv | 427 |
| editors_abs_ajg_gap_prio43_current.csv | 22 |
| editors_abs_ajg_gap_ajg2_current.csv | 54 |
| editors_abs_ajg_gap_ajg1_current.csv | 81 |
| editors_ft50_current_with_ror.csv | 18 |
| editors_ft50_current.csv | 8 |
| **Panels total** | **1,429** |
| editor_affiliations.csv.gz (long rows) | 630 |

Row counts unchanged; ajg1 12,316 and ajg2 5,462 with the navigation rows out; FT50 10,047.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,525,533 bytes; 63,476,954 bytes uncompressed, md5 `f4a9efd156cf95f52cf85695247b2d6a`). 181,443 rows, same 20 columns, starts from the `editors_country_misprint_fix_20261110` table.

## Files

- `editor_affiliations.csv.gz` — long table
- `WEIRD_INST_changes_20261110.csv` — collector field-level change log (incl. pilot rows); one email address in the `old` cell of C #12376 removed before publishing
- `WEIRD_INST_skipped_20261110.csv` — 160 Institution skips + 120 row skips (over-stripped rows kept), with reasons
- `weird_strip_overrides_20261110.tsv`, `weird_rematch_skips_20261110.json` — collector rule inputs
- `SENDTO_BLURB.txt`, `COLLECTOR_RELEASE_NOTES.md` — collector notes
- `README.md` — this file
