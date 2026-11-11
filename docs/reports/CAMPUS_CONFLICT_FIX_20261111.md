# editors_campus_conflict_fix_20261111

Published 2026-11-11 (Asia/Taipei) as a Directory freeze on top of `editors_school_unit_rematch_20261111` (PR #63). User-approved follow-up for the seven campus-conflict rows that freeze left unmatched, because the earlier rematch file had targeted the wrong home campus.

## Applied (7 of 7; 0 skips)

`raw_affiliation` is left as the printed masthead. UK Nottingham `01ee9ar58` and Northumbria `049e6bc10` were not assigned. Both target RORs were API-verified active and already on the published panels. No new ROR.

- `#18543` Kingsley Dogah, `#20062` Jie Wang, `#803` Frithjof Arp, `#3138` Bruno Deschamps → University of Nottingham Ningbo China `03y4dt428` (China)
- `#18450` Marianna Sigala, `#27171` Alison Dean, `#24283` Mojtaba Barari → University of Newcastle Australia `00eae9z71` (Australia)

## Left as printed

Two other unmatched NUBS China mastheads were not in this file: `#4924` Patrick Chau (`University of Nottingham Business School China, Ningbo, China`) and `#5221` Y. Ye (`University of Nottingham Business School China, China`). The “Nottingham University Business School China” display name therefore remains. Held campus and two-place rows from the previous send stay as printed.

## Panels

Published current panels were updated in place by `editor_row_key`. Collector-only extras stay out (FT50 `#577`/`#578`; ten ajg1 navigation rows). No pilots. `CITATION.cff` is unchanged.

| Panel | Rows | Changed | `ror_id` |
|---|---:|---:|---|
| `editors_ft50_current.csv` | 10,047 | 0 | 9,795 (unchanged) |
| `editors_ft50_current_with_ror.csv` | 10,047 | 0 | 9,870 (unchanged) |
| `editors_abdc_a_star_current.csv` | 25,596 | 1 | 23,886 (was 23,885) |
| `editors_abdc_a_current.csv` | 45,889 | 1 | 41,650 (was 41,649) |
| `editors_abdc_b_current.csv` | 42,558 | 2 | 38,201 (was 38,199) |
| `editors_abdc_c_current.csv` | 27,719 | 3 | 22,633 (was 22,630) |
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 0 | 2,627 (unchanged) |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,462 | 0 | 4,949 (unchanged) |
| `editors_abs_ajg_gap_ajg1_current.csv` | 12,316 | 0 | 9,252 (unchanged) |

Directory diff: 35 cells (`canonical_name`, `ror_id`, `ror_name`, `lat`, `lon` on each of the 7 keys). Verified 0 missing keys and 0 old-value mismatches against the pre-update published panels; all 35 new values landed.

## Long table

`data/editors/releases/editors_campus_conflict_fix_20261111/editor_affiliations.csv.gz` keeps the published 181,449 parts (Collector table restricted to published keys; B `#13` web e-mail-scrub note kept). 7 parts changed: `ror_id` / `ror_name` / `is_panel_ror` on 7; no `raw_aff_part` edits. gzip -9 -n; md5 `137fc0c7ceb03e0a760f98ee26955b0e`.

## Directory

Local `scripts/build_site.py` should reproduce: Institutions 11,077 (was 11,078), 6,698 with a ROR id, countries 169, shared names 43 (guard stays 43). Institutions fell by 1 because the Newcastle Australia display name folded into University of Newcastle Australia, which already had a ROR. Appointments 162,575, editors 112,719, journals 2,853, and 13,415 appointments without an institution are unchanged.
