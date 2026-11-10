# raw_aff_part 'no' fix — editors_raw_aff_part_no_fix_20261110

Published 2026-11-10 (Asia/Taipei). Supersedes `editors_edpacs_marks_country_fix_20261110` (PR #51). Long-table-only.

## Problem

In `editor_affiliations.csv.gz`, `raw_aff_part` held the literal `no` on seats whose panel `raw_affiliation` is blank — the `affiliation_imputed` flag value leaking into the text column. (PR #51 fixed 8 EDPACS parts; this clears the rest.)

## Change

- 9,695 long-table rows: `raw_aff_part` `no` → blank. `'no'` count 9,695 → 0.
- Collector log has 9,705 publish-set keys; 10 are absent from the Directory copy by design (9 ajg1 navigation/chrome rows, 1 dropped REStud institution-as-name row, FT50 with_ror #578). 3,998 profile-pilot rows not applied.
- Per panel: A* 112, A 2,668, B 2,237, C 1,564, FT50 104 / 99 (slim / with_ror), prio43 358, ajg2 236, ajg1 2,317.

## Checks

- Long table 181,443 rows, 20 columns, gzip -9 -n; exactly 9,695 lines differ from the #51 table; no other column changed.
- Panel CSVs, CITATION.cff, core49 and `scripts/build_site.py` untouched; no pilot files.
- `build_site.py` (it does not read the long table): appointments 162,575, editors 112,718, journals 2,853, Institutions 15,434 (6,387 with ROR), countries 159, 12,067 appointments without an institution, shared names 69 — all unchanged.
