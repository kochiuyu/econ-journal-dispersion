# editors_review_resolved_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Keyed, user-approved review-resolved fix on the published Directory copy of `editors_weird_inst_fix_20261110` (PR #53), which it supersedes. Collector pack: `/workspace/econ-journal-editors/releases/editors_review_resolved_fix_20261110`.

Only the publish-set cells of the field-level change log were written, keyed by `editor_row_key`. Long-table cells are keyed by `editor_row_key` + `panel_file` + `aff_rank`. The e-mail removal cells have no `aff_rank`; for those, the part whose redacted value equals the logged `old` was used.

Every cell was checked against its `old` value, with 0 mismatches. 2,022 cells already equalled the freeze value because the Directory had removed those addresses earlier. Pilot rows are not applied, and `*_with_profile_pilot.csv` is not published. The one new `ror_id` (`05a8bts04`, Hainan Vocational University of Science and Technology) was verified by the Collector against the ROR API; every other new `ror_id` already exists on the panels.

Web addition: a malformed e-mail address in ABDC B `#13` (`raw_affiliation`, `canonical_name`, long `raw_aff_part`) was removed, with a trace in the notes.

| File | Rows changed |
|---|---:|
| editors_abdc_a_star_current.csv | 79 |
| editors_abdc_a_current.csv | 120 |
| editors_abdc_b_current.csv | 131 (+1 e-mail scrub) |
| editors_abdc_c_current.csv | 155 |
| editors_abs_ajg_gap_prio43_current.csv | 9 |
| editors_abs_ajg_gap_ajg2_current.csv | 23 |
| editors_abs_ajg_gap_ajg1_current.csv | 56 |
| editors_ft50_current_with_ror.csv | 37 |
| editors_ft50_current.csv | 35 |
| **Panels total** | **645 (+1)** |
| editor_affiliations.csv.gz (long rows) | 539 (+1) |

Row counts are unchanged. ajg1 is 12,316 and ajg2 is 5,462 with the navigation rows out; FT50 is 10,047.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,530,489 bytes; 63,500,169 bytes uncompressed, md5 `786d5c0170104bef9259877dfc6ae1dd`). 181,443 rows, same 20 columns, starts from the `editors_weird_inst_fix_20261110` table.

## Files

- `editor_affiliations.csv.gz` — long table
- `REVIEW_RESOLVED_changes_20261110.csv` — Collector field-level change log, incl. pilot rows; addresses logged as `[email removed]`
- `REVIEW_RESOLVED_skipped_20261110.csv` — 57 skips with reasons
- `review_item3_names_20261110.json` — over-stripped name restores
- `WEB_build_site_scrub_word_boundary.patch` — scrub patch applied to `scripts/build_site.py`
- `SENDTO_BLURB.txt`, `COLLECTOR_RELEASE_NOTES.md` — Collector notes
- `README.md` — this file
