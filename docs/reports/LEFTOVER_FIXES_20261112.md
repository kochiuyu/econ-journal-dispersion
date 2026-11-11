# editors_leftover_fixes_20261112

Published 2026-11-12 (Asia/Taipei) as a Directory freeze on top of `editors_school_unit_leftover_20261112` (PR #68). User-approved leftover fixes (Collector chat, 2026-11-12).

## Applied

Taken through `LEFTOVER_FIXES_directory_diff_20261112.csv` (24 cells, 0 missing keys, 0 old-value mismatches against the published panels) and applied cell by cell from `LEFTOVER_FIXES_changes_20261112.csv` on published `editor_row_key`s. Every changed published row now matches the Collector row exactly.

- **A. UK Henley (3 rows).** AJG1 #1185, #2555 (Abby Ghobadian) and #2583 (Marc Day): Henley Business School / blank ROR → University of Reading `05v62cm79`, United Kingdom (`canonical_name`, `ror_id`, `ror_name`, `lat`, `lon`, `ror_notes`). `raw_affiliation` stays “Henley Management College, UK”. Henley Africa (ABDC B #18374) is untouched.
- **B. Name-field phantoms.**
  - FT50 REStud #577/#578 (and with_ror twins; `editor_name` “Universitat Pompeu Fabra”) are dropped in the Collector source. The published FT50 panels never carried them (10,047 rows each vs Collector 10,049), so nothing is published for them. Real editors #640 Enikolopov, #608 Penta and #627 Vanasco are unchanged.
  - AJG2 #5449 Sônia Miriam Draibe → Universidade Estadual de Campinas (UNICAMP) `04wffgt70`, Brazil, South America; `affiliation_count` 0 → 1, `ror_id_aff_rank` 1, `primary_aff_basis` single. `raw_affiliation` is left blank; the printed text is in `ror_notes`.
  - AJG2 #5450 JLAS phantom: `editor_name` / `editor_name_raw` “Universidade Estadual de Campinas, Brazil” blanked; the text is in `ror_notes`. The row stays in the CSV (5,462 rows).
- **C. Long-table country sync.** 874 parts where the panel had a country and the long-table primary part was blank now carry the panel `ror_country`. All 874 are on published parts (0 on unpublished parts). Panel–long mismatches 874 → 0. 2,879 panel keys still have no long-table part; none was invented.

The long table stays at 181,449 parts (180,025 unique `editor_row_key`s). 877 parts changed (874 `ror_country`; 3 Henley parts on `ror_id` / `ror_name` / `is_panel_ror` / `ror_match_note`). No `raw_aff_part` edits. #5449 and #5450 have no parts. The `web_email_scrub_20261110` note on `editors_abdc_b_current#13` is preserved.

## Build guard change

`scripts/build_site.py`, `AJG_GAP_FILES`, `ajg2`: `expected_dropped` 0 → 1. The site builder drops rows with a blank `editor_name` and no ROR; the blanked phantom #5450 is such a row, and without this change the build stops with “dropped 1 names, expected 0”. No other guard changed; the shared-name guard stays at 43.

## Directory

Institutions 11,074 (was 11,075), 6,698 with a ROR id (distinct 6,698), countries 169, shared display names 43. Appointments 162,574 (was 162,575), editors 112,718 (was 112,719), appointments without an institution 13,413 (was 13,415). The drop of one is the blanked #5450.

No new ROR ids (`05v62cm79` and `04wffgt70` were API-verified as active and were already on the panels). Pilots are not published. No emails or phones. Untouched: #640, #608, #627, #18374, JLAS neighbours #5448 and #5451, the Nielsen/SEARCA/Diamond keys, and the 40 held rows.

Sidecars: `data/editors/releases/editors_leftover_fixes_20261112/`.
