# RELEASE NOTES — editors_tokyo_gatech_fix_20261110

**When (Asia/Taipei):** 2026-11-10 14:10 Asia/Taipei
**Base:** `editors_inst_punct_split_20261110` (PR #47, b15c2032)
**Scope:** panel-only fix — University of Tokyo rows rewritten to “Italian Cultural Institute”, and one Georgia Tech row.

## Fixed (publish panels)
- University of Tokyo → `https://ror.org/057zh3y96` (The University of Tokyo, Japan): 27 rows (25 with the FT50 pair collapsed)
- Georgia Inst of Technology → `https://ror.org/01zkghx44` (Georgia Institute of Technology): 1 row
- Printed raw_affiliation restored from the Directory copy: 28 rows (our raw had been overwritten)
- Patched panels: `editors_ft50_current.csv`, `editors_ft50_current_with_ror.csv`, `editors_abdc_a_star_current.csv`, `editors_abdc_a_current.csv`, `editors_abdc_b_current.csv`, `editors_abdc_c_current.csv`, `editors_abs_ajg_gap_prio43_current.csv`, `editors_abs_ajg_gap_ajg2_current.csv`, `editors_abs_ajg_gap_ajg1_current.csv`
- profile_pilot panels: no changes needed (their University of Tokyo rows already carry `https://ror.org/057zh3y96`); carried through byte-identical, **not for publish**.
- Keys not found in base: none

## Root cause
- `abs_ajg/scripts/institution_residual_post35_fix_20261028.py` (freeze `editors_institution_residual_post35_20261028`, ror_notes `residual_post35_strip_place_20261028`).
- Earlier (`editors_current_20261024`), a “powerful_key=Tokyo” ROR backfill matched Tokyo-printed rows to `https://ror.org/015e2vx95` “Italian Cultural Institute, Tokyo”.
- The post35 strip_place step stripped the place token from that ROR name, wrote the remainder “Italian Cultural Institute” into both raw_affiliation and canonical_name, and cleared the ROR.
- `t39_plus_fix_20261029.py` later rejected that pair, but only for new matches; it did not repair the already-rewritten rows.
- The Directory masked this with `directory_guardrail_restore_20261101`.

Georgia Tech: `institution_dept_country_fix_20261028` rewrote the row to “Czech Academy of Sciences” (`053avzc18`). Before that it was `Georgia Inst of Technology` with an unrelated ROR, `01qj7sc02`.

## Other “Italian Cultural Institute” rows — NOT fixed
35 rows on the publish panels are still “Italian Cultural Institute” in raw and canonical with blank ROR, while the Directory's printed text names a different Tokyo institution (Tokyo Institute of Technology, Tokyo University of Science, Tokyo Metropolitan, etc.).
Full list: `ITALIAN_CULTURAL_INSTITUTE_other_rows_20261110.csv`. Examples:
- `editors_abdc_a_star_current#11663` Fuhito Kojima: Directory raw “Tokyo”
- `editors_abdc_a_current#9804` Takashi Seo: Directory raw “Tokyo University of Science, Shinjuku City, Japan”
- `editors_abdc_a_current#9827` Aki Ishii: Directory raw “Tokyo University of Science, Shinjuku City, Japan”
- `editors_abdc_a_current#17473` Masayoshi Noguchi: Directory raw “Tokyo Metropolitan University, Japan”
- `editors_abdc_a_current#21122` Yuuya Tachiki: Directory raw “Tokyo Metropolitan University”
- `editors_abdc_a_current#21199` Junichi Iijima: Directory raw “Tokyo Institute of Technology, Japan”
- `editors_abdc_a_current#22061` Yuriko Sato: Directory raw “Tokyo Institute of Technology, Japan”
- `editors_abdc_a_current#43614` Takafumi Kanamori: Directory raw “Tokyo Institute of Technology, Tokyo”
- `editors_abdc_b_current#116` Kota Ogasawara: Directory raw “Tokyo Institute of Technology”
- `editors_abdc_b_current#5891` S. Nakada: Directory raw “Tokyo University of Science, Shinjuku City, Japan”
- `editors_abdc_b_current#6467` Fumio Mizoguchi: Directory raw “Tokyo University of Science, Japan”
- `editors_abdc_b_current#8940` Toshihiko Kuwabara: Directory raw “Tokyo University of Agriculture and Technology, Tokyo, Japan”

## Verification
- invented_ror_ids: []
- unlogged changes vs base: 0; protected rows changed: 0
- panel↔long desync: 0 (long parts 28, missing 0)
- 11KBW True; UNSW Sydney True; INSEAD FR+SG True
- “Italian Cultural Institute” rows remaining by panel: {'editors_abdc_a_star_current.csv': 1, 'editors_abdc_a_current.csv': 7, 'editors_abdc_b_current.csv': 13, 'editors_abdc_c_current.csv': 14}
