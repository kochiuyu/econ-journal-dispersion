# editors_country_misprint_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Keyed, user-approved country-misprint and fragment-name fix on the published Directory copy of `editors_trailing_country_fix_20261110` (PR #53), which it supersedes. Collector pack: `/workspace/econ-journal-editors/releases/editors_country_misprint_fix_20261110`.

Only the publish-set fields of the field-level change log were written (`canonical_name`, `ror_country`, `continent`; `ror_id` / `ror_name` / `lat` / `lon` on the Imperial College rematch; long `ror_country` / `ror_id` / `ror_name` / `is_panel_ror`), keyed by `editor_row_key` (long: `editor_row_key` + `panel_file` + `aff_rank`), each checked against its `old` value (0 mismatches). For the 11 rows held back in PR #53 the trailing-country cells were applied together with this freeze's cells, checked against the PR #53 `old` values, so the rows now equal the freeze. Every changed panel row equals the Collector freeze row. Pilot rows are not applied and `*_with_profile_pilot.csv` is not published. `ror_id` `041kmwe10` already exists on the panels.

| File | Rows changed |
|---|---:|
| editors_abdc_a_star_current.csv | 2 |
| editors_abdc_a_current.csv | 13 |
| editors_abdc_b_current.csv | 14 |
| editors_abdc_c_current.csv | 10 |
| editors_abs_ajg_gap_prio43_current.csv | 1 |
| editors_abs_ajg_gap_ajg1_current.csv | 2 |
| **Panels total** | **42** (30 country, 11 fragment, 1 Barranquilla) |
| editor_affiliations.csv.gz (long rows) | 41 |

FT50 and ajg2 unchanged. Row counts unchanged; ajg1 12,316 and ajg2 5,462 with the navigation rows out.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,514,555 bytes; 63,439,254 bytes uncompressed, md5 `cfba6af6e371b46c7388fedea330d05c`). 181,443 rows, same 20 columns, starts from the #53 table.

## Files

- `editor_affiliations.csv.gz` — long table
- `COUNTRY_MISPRINT_changes_20261110.csv` — collector field-level change log (incl. pilot rows)
- `COUNTRY_MISPRINT_skipped_20261110.csv` — collector left-as-is list
- `SENDTO_BLURB.txt`, `COLLECTOR_RELEASE_NOTES.md` — collector notes
- `README.md` — this file
