# editors_raw_drift_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Keyed, user-approved raw-drift fix on the published Directory copy of `editors_post_review_fix_20261110` (PR #53), which it supersedes. Collector pack: `/workspace/econ-journal-editors/releases/editors_raw_drift_fix_20261110`.

This freeze takes the Collector's whole row, keyed by `editor_row_key`, on the 40 publish rows where the Directory differed on raw text or the Institution fields:
- 3 raw-text rows: FT50 #2955 in both files, and ajg1 #10149.
- 27 Institution-field rows: the 21 former National Law University / India rows, plus ENSAI, Kagoshima, MIT, Springer Shanghai, Gradient and HKUST (Guangzhou) C #27613.
- 10 HKUST (Guangzhou) rows, where only `ror_match_method` / `ror_notes` differed.

The long-table rows for those keys (`editor_row_key` + `panel_file` + `aff_rank`, 40 rows) take the Collector's values.

What was not taken from the Collector:
- The three Top 5 seats (#10046–#10048) were already in the Directory panels, so they were not added again. The long table stays at 181,443 rows and does not get the Collector's 6 added long rows for those seats.
- The two Pompeu Fabra institution-as-name rows (#577/#578) and the 10 AJG1 navigation rows stay out.
- Pilot panels are not published.

Six `ror_id`s are new to the panels. All six were checked on the ROR API v2 (active):
- `00bge3r76` The University of Law
- `0545p3742` Plovdiv University
- `0558j5q12` Politehnica București
- `03ss88z23` Kagoshima University
- `014qf4206` Gradient (United States)
- `01f9pza55` Springer Nature (Shanghai, China)

| File | Rows changed |
|---|---:|
| editors_abdc_a_star_current.csv | 3 |
| editors_abdc_a_current.csv | 10 |
| editors_abdc_b_current.csv | 11 |
| editors_abdc_c_current.csv | 10 |
| editors_abs_ajg_gap_prio43_current.csv | 2 |
| editors_abs_ajg_gap_ajg2_current.csv | 1 |
| editors_abs_ajg_gap_ajg1_current.csv | 1 |
| editors_ft50_current_with_ror.csv | 1 |
| editors_ft50_current.csv | 1 |
| **Panels total** | **40** |
| editor_affiliations.csv.gz (long rows) | 40 |

Row counts are unchanged: ajg1 12,316, ajg2 5,462, FT50 10,047.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,536,924 bytes; 63,522,818 bytes uncompressed, md5 `2f59f0a8292fcb1443bdbd7a45b9e63a`). It has 181,443 rows and the same 20 columns.

## Files

- `editor_affiliations.csv.gz`: the long table.
- `RAW_DRIFT_changes_20261110.csv`, `RAW_DRIFT_skipped_20261110.csv`, `RAW_DRIFT_source_verification_20261110.csv`, `RAW_DRIFT_directory_drift_after_20261110.csv`: the Collector's logs.
- `RAW_DRIFT_leak_scan_20261110.csv`: 166 other rows where a script wrote a canonical or ROR name into the raw text. Not changed here; changing them needs a separate approval.
- `raw_drift_fix_20261110.py`, `HANDOFF.md`, `SENDTO_BLURB.txt`, `COLLECTOR_RELEASE_NOTES.md`: the Collector's script and notes.
- `README.md`: this file.

The folder contains no e-mail addresses or phone numbers.
