# editors_school_unit_leftover_20261112

Published 2026-11-12 (Asia/Taipei) as a Directory freeze on top of `editors_theory_decision_title_20261112` (PR #67). User-approved school-unit leftover rematches; match fields only.

## Applied (13 of 13; 0 skips)

Only `canonical_name`, `ror_id`, `ror_name`, `lat` and `lon` changed on the panels; `raw_affiliation` is left as printed.

- NUBS China, 2 rows (`editors_abdc_a_current` #4924 Patrick Chau, #5221 Y. Ye) → University of Nottingham Ningbo China `03y4dt428`, China. UK Nottingham `01ee9ar58` was not used.
- UK Henley Management School/College, 3 rows (`editors_abdc_b_current` #30182, #30664 Yipeng Liu; #31832 Abby Ghobadian) → University of Reading `05v62cm79`, United Kingdom. Henley Africa #18374 is untouched.
- RSM Erasmus, 8 rows (A* #14113, #24564; A #40739; B #18143, #32487, #39125; C #20763, #22989) → Erasmus University Rotterdam `057w15z03`, Netherlands.

The long table syncs `ror_id` / `ror_name` / `is_panel_ror` on 13 parts. No `raw_aff_part` edits. The `web_email_scrub_20261110` note on `editors_abdc_b_current#13` is preserved. No new ROR ids; all three targets were API-verified as active and were already on the published panels.

## Not applied

- Six name-field DROPs were not approved and are unchanged: FT50 REStud #577/#578 (and with_ror twins; these stay out of the published panels) and AJG2 #5449/#5450.
- Three AJG1 rows printed “Henley Management College, UK” (#1185, #2555 Abby Ghobadian; #2583 Marc Day) were not in this freeze and are still as printed. They are candidates for the same University of Reading rematch if approved.

## Directory

Institutions 11,075 (was 11,077), 6,698 with a ROR id (distinct 6,698), countries 169, shared display names 43 (build guard stays 43). The drop of 2 is the blank-ROR names “Nottingham University Business School China” and “Rotterdam School of Management, Erasmus University” folding into existing ROR entries.

Sidecars: `data/editors/releases/editors_school_unit_leftover_20261112/`.
