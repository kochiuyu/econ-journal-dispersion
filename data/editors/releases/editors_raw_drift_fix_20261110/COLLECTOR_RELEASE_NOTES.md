# editors_raw_drift_fix_20261110

Base: `editors_post_review_fix_20261110`. Built 2026-11-10 23:14 (Asia/Taipei). User-approved via Econ-Journal-Web. Every edit is keyed on editor_row_key. Comparison file: `/workspace/raw_drift_20261110.csv` (39 differing rows + 6 missing keys).

## Changes
- **Items 1+2 (37 rows): printed raw restored and institution fixed.**
  - 21 'National Law University' rows: printed text restored, the India country removed, and each row set to the real ROR.
  - 11 HKUST (Guangzhou) rows: printed '(Guangzhou)' restored and set to 050h0vm43 / China. #27613 is set to 050h0vm43 too; the Directory row still shows 00q4vv597 / Hong Kong there.
  - Kagoshima (#25991): Nihon University replaced by Kagoshima University.
  - MIT Connection Science (#27660): Ikon Science replaced by MIT.
  - Gradient (prio43 #2898): Korea Telecom replaced by Gradient (United States).
  - Truncated strings restored: Springer Nature (Shanghai, China) and Chauvet / ENSAI.
  - Long table: raw_aff_part, ror_id, ror_name, ror_country and is_panel_ror synced, with a trace in ror_match_note.
- **Item 3:** FT50 #2955 Tiffany Trzebiatowski (both ft50 files). The bio paragraph is replaced by 'Colorado State University', ROR 03k1gpj17 (panel ROR, checked against the CSU directory).
- **Item 4:** 3 Top-5 seats (#10046–#10048) added to both ft50 files. Each is a verbatim copy of the Directory row, in Directory order. Matching long rows were added (+6).
  - The 2 UPF editor_name rows (#577/#578) are unchanged.
- **Item 5:** the 5 remaining role-prefix names from the audit are fixed by the item 2 rows (Adelaide, Newcastle AU, Leiden, Toronto, Tilburg+Leiden). Keele is also fixed.
- **New RORs.** All were checked against the ROR API v2:
  - 0558j5q12 Politehnica București
  - 0545p3742 Plovdiv University
  - 03ss88z23 Kagoshima University
  - 014qf4206 Gradient (United States)
  - 00k206f19 ENSAI
  - 01f9pza55 Springer Nature (Shanghai, China)
- **Skipped (1):** ajg1 #10149 Lawrence Sweet. The live source prints 'IZZI Inc', so our raw is kept (see the skipped CSV).

## Counts
- Rows: ft50_current and ft50_current_with_ror 10,046 → 10,049. All other panels are unchanged (AJG1 12,326 incl. 10 nav rows, AJG2 5,462). Long table 269,539 → 269,545.
- Directory build (Institutions / with ROR / distinct ROR / countries / shared names): 14,195 / 6,379 / 6,379 / 162 / 49 → 14,176 / 6,384 / 6,384 / 162 / 49.

## Files
- `RAW_DRIFT_changes_20261110.csv`
- `RAW_DRIFT_skipped_20261110.csv`
- `RAW_DRIFT_source_verification_20261110.csv`
- `RAW_DRIFT_leak_scan_20261110.csv`: other canonical-into-raw rewrites; not changed, needs approval.
- `RAW_DRIFT_directory_drift_after_20261110.csv`
- `_summary_20261110.json`
- `raw_drift_fix_20261110.py`

Pilot files are byte-identical to the base.
