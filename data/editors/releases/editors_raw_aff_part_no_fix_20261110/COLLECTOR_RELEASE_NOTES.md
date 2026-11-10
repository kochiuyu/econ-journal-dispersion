# RELEASE NOTES — editors_raw_aff_part_no_fix_20261110

**When (Asia/Taipei):** 2026-11-10 16:39 Asia/Taipei
**Base:** `editors_edpacs_marks_country_fix_20261110` (Directory PR #51, ceb89dd0)
**Scope:** `editor_affiliations.csv` only, field `raw_aff_part`, only where the value is exactly `no`. These values had leaked from the panel `affiliation_imputed` flag while the panel's raw_affiliation is blank, and they are set to `''`. No other field is touched and no notes are appended. All panel CSVs are byte-identical to base; panel `affiliation_imputed = no` is a real flag (“not imputed”) and is left as is.

## Counts
- Before: 13703 rows with raw_aff_part `no` (variants {'no': 13703}); after: 0
- Changed: 13703. Publish-set panels: 9705; pilot-sourced long rows: 3998
- editors_abdc_a_current.csv: 2668
- editors_abs_ajg_gap_ajg1_current.csv: 2326
- editors_abdc_b_current.csv: 2237
- editors_abdc_b_current_with_profile_pilot.csv: 2052
- editors_abdc_a_current_with_profile_pilot.csv: 1946
- editors_abdc_c_current.csv: 1564
- editors_abs_ajg_gap_prio43_current.csv: 358
- editors_abs_ajg_gap_ajg2_current.csv: 236
- editors_abdc_a_star_current.csv: 112
- editors_ft50_current.csv: 104
- editors_ft50_current_with_ror.csv: 100

## Examples
- `editors_abdc_c_current#12375` Dan Swanson (editors_abdc_c_current.csv): raw_aff_part `no` → `''`; panel raw_affiliation `` (blank), panel affiliation_imputed `no` (unchanged); other long fields identical: True
- `editors_ft50_current#83` John G. Riley (editors_ft50_current.csv): raw_aff_part `no` → `''`; panel raw_affiliation `` (blank), panel affiliation_imputed `no` (unchanged); other long fields identical: True
- `editors_abs_ajg_gap_ajg1_current#71` Arthur Trognon (editors_abs_ajg_gap_ajg1_current.csv): raw_aff_part `no` → `''`; panel raw_affiliation `` (blank), panel affiliation_imputed `no` (unchanged); other long fields identical: True

## Verification (ok=True)
- Unexpected diffs (any other field, or any other row): 0; ror_id / is_panel_ror changes: 0; protected org fields changed: 0 (protected-org rows where only raw_aff_part `no` was cleared, org untouched: ['editors_abdc_b_current#16541'])
- panel↔long desync on changed keys (raw, ror_id, is_panel_ror): 0
- Long rows 269539 → 269539; header identical True; EOL same True
- Panels byte-identical (incl. pilots): True; working panels identical: True
- AJG1 12326 file rows = 12316 published + 10 nav rows; AJG2 5462
- Short real values untouched (base → new): {'UK': 99, 'USA': 88, 'LSE': 55, 'MIT': 20, 'US': 0, 'NBER': 0, 'CEPR': 2, 'IMF': 2} → {'UK': 99, 'USA': 88, 'LSE': 55, 'MIT': 20, 'US': 0, 'NBER': 0, 'CEPR': 2, 'IMF': 2}
- 11KBW True; UNSW Sydney True; INSEAD FR+SG True
