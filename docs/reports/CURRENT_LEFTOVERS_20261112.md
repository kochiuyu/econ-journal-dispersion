# editors_current_leftovers_20261112

Published 2026-11-12 (Asia/Taipei) as a Directory freeze on top of `editors_leftover_fixes_20261112` (PR #69; web main was c4d24a7, icons/CSS only, data identical). Collector freeze of evidenced current-board leftovers under the user's “Yes, unless you think only RA can fix, you can fix those?”.

## Applied

Taken through `CURRENT_LEFTOVERS_directory_diff_20261112.csv` (341 cells, 0 missing keys, 0 old-value mismatches against the published panels) and applied cell by cell from `CURRENT_LEFTOVERS_changes_20261112.csv` (472 panel cells, 238 long cells) on published `editor_row_key`s, in place and in published row order. Every changed published row now matches the Collector row exactly; no other published cell differs from the Collector panels.

- **D. Official-board name-field fixes (26 rows: 7 attaches, 19 Marks-style DROPs).** European Transport (ABDC C): Angela Carboni #15764 → Politecnico di Torino `00bgk9508` and Medeghini #15760 → Brescia Mobilità (no ROR, Italy), with their phantom name rows #15765 and #15761 blanked; JMID (AJG1): Péter Biró #11088 → Hungarian Academy of Sciences `02ks8qq67`, Sergei Izmalkov #11102 → New Economic School `033904843`, Flip Klijn #11108 → Universitat Autònoma de Barcelona `052g8jq94`, Gleb Koshevoy #11111 → Russian Academy of Sciences `05qrfxd25`, Utku Ünver #11142 → Boston College `02n2fzt79`, with their 5 phantom rows (#11089, #11103, #11109, #11112, #11143) blanked, plus 12 JMID non-person rows blanked (a section header, site-policy links, a sentence fragment and article titles: #11149, #11167–#11170, #11173, #11175, #11183, #11187, #11207–#11209). DROPs blank `editor_name` only; the row stays and the printed text is in `ror_notes`.
- **E. School-unit rule (27 rows).** Rematched to API-active catalog RORs, the school's own ROR or the parent named in the printed school: A 7, B 12, C 1, AJG1 5, AJG2 2. `raw_affiliation` is left as printed.
- **F. Printed-country fills (68 rows).** `ror_country` / `continent` from the printed final country token; no ROR assigned: FT50 with_ror 2, A* 14, A 15, B 16, C 11, prio43 1, AJG2 2, AJG1 7.

Rows changed per panel: FT50 with_ror 2 (slim 0), A* 14, A 22, B 28, C 16, prio43 1, AJG2 4, AJG1 34 (121). Row counts, headers and LF line endings unchanged.

Not published (as before): FT50 #577/#578 (published FT50 stays 10,047 rows vs Collector 10,049) and the 10 AJG1 navigation rows (published 12,316 vs Collector 12,326), including the JMID nav row #11210 the Collector also skipped. Pilots (`editors_abdc_*_current_with_profile_pilot.csv`) are byte-identical in the Collector freeze and are not published.

## Long table

`editor_affiliations.csv.gz` stays at 181,449 parts (180,025 unique `editor_row_key`s), aligned on (`editor_row_key`, `aff_rank`). The long table changes 117 parts on 117 keys (`ror_country` 76, `ror_id` / `ror_name` / `is_panel_ror` 32, `ror_match_note` 49, `editor_name` blanked on 17 JMID phantom/non-person parts); no `raw_aff_part` edits; the 4 European Transport keys have no long-table part and none was invented. Panel–long mismatches on the changed keys: 0. The `web_email_scrub_20261110` note on `editors_abdc_b_current#13` is preserved (the only residual difference from the Collector long table on published parts).

## Build guard change

`scripts/build_site.py`, `AJG_GAP_FILES`, `ajg1`: `expected_dropped` 15 → 32. The site builder drops rows with a blank `editor_name` and no ROR; the 17 blanked JMID rows are such rows, and without this change the build stops with “editors_abs_ajg_gap_ajg1_current.csv dropped 32 names, expected 15”. `ajg2` stays 1. No other guard changed; the shared-name guard stays at 43. (The two blanked European Transport rows are dropped from ABDC C, 6 → 8; ABDC has no dropped-row guard.)

## Directory

Institutions 11,065 (was 11,074), 6,698 with a ROR id (unchanged; distinct 6,698), countries 169 (unchanged), shared display names 43 (unchanged; the build guard stays 43); appointments 162,555 (was 162,574), editors 112,699 (was 112,718), journals 2,853, appointments without an institution 13,387 (was 13,413). The drop of 19 appointments and editors is the 19 blanked DROP rows.

## Held (unchanged; see `COLLECTOR_RELEASE_NOTES.md`)

JMID rest of board (needs a whole-board re-harvest); European Transport blank-affiliation fills (Di Matteo #15763, Bonera #15767); EDHEC UK/Singapore campus rows; Edinburgh Business School #29393; “University of New York School of Law” #35355; NWU Business School #8580; INCAE, One School of Business, PKU HSBC, IFoA; schools that need outside knowledge; F skips. Henley Africa #18374, the 40 held campus rows, two-place rows, HKU and unplaced editors are untouched. The slim-vs-with_ror FT50 divergence (82 `ror_id` / 81 country / 45 raw) is held for a decision.

Sidecars: `data/editors/releases/editors_current_leftovers_20261112/`.
