# editors_post_review_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Keyed, user-approved post-review Institution fix on the published Directory copy of `editors_review_resolved_fix_20261110` (PR #53), which it supersedes. Collector pack: `/workspace/econ-journal-editors/releases/editors_post_review_fix_20261110`.

Only the publish-set cells of the field-level change log were written, keyed by `editor_row_key`. Long-table cells are keyed by `editor_row_key` + `panel_file` + `aff_rank`. Contact-removal cells have no `aff_rank`; for those, the part whose value equals the logged `old` was used. The logs write removed contact text as `[email removed]` / `[phone removed]`, so those `old` values were checked by pattern.

Every cell was checked against its `old` value, with 0 mismatches. 21 cells already equalled the freeze value, because the Directory had removed that contact text earlier. Pilot rows are not applied, and `*_with_profile_pilot.csv` is not published. The one new `ror_id` on publish rows (`033xgn512`, IIESS, Bahía Blanca, Argentina) was verified against the ROR API. Every other new `ror_id` already exists on the panels.

| File | Rows changed |
|---|---:|
| editors_abdc_a_star_current.csv | 41 |
| editors_abdc_a_current.csv | 82 |
| editors_abdc_b_current.csv | 107 |
| editors_abdc_c_current.csv | 98 |
| editors_abs_ajg_gap_prio43_current.csv | 1 |
| editors_abs_ajg_gap_ajg2_current.csv | 16 |
| editors_abs_ajg_gap_ajg1_current.csv | 17 |
| editors_ft50_current_with_ror.csv | 4 |
| editors_ft50_current.csv | 2 |
| **Panels total** | **368** |
| editor_affiliations.csv.gz (long rows) | 260 |

Row counts are unchanged. ajg1 is 12,316 and ajg2 is 5,462 with the navigation rows out; FT50 is 10,047.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,535,388 bytes; 63,518,994 bytes uncompressed, md5 `61c18e057c3c27ba3bb06a5302a923b4`). It has 181,443 rows and the same 20 columns, and starts from the `editors_review_resolved_fix_20261110` table. It has no e-mail addresses and no labelled phone numbers in `editor_name` or `raw_aff_part`.

## Files

- `editor_affiliations.csv.gz`: the long table.
- `POST_REVIEW_changes_20261110.csv`: the Collector's field-level change log, including pilot rows. Contact text is logged as `[email removed]` / `[phone removed]`.
- `POST_REVIEW_skipped_20261110.csv`: the skips, with reasons.
- `post_review_decisions_20261110.py`: the per-name decisions.
- `HANDOFF.md`, `SENDTO_BLURB.txt`, `COLLECTOR_RELEASE_NOTES.md`: the Collector's notes.
- `README.md`: this file.
