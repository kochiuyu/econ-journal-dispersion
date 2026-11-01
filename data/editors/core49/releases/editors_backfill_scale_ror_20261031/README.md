# editors_backfill_scale_ror_20261031 — pinned in this repo (2026-11-01)

**Publish note (2026-11-01, Asia/Hong_Kong).** The user approved publishing this multi-year core49 backfill
together with `editors_ror_consistency3b_20261101`. It is pinned here as a release; the Directory site
does not read it (the site shows current boards only). The collector's README follows below the line; its
"HELD" status is historical.

- Panel: `editors_backfill_scale_ror_panel.csv` — 15,446 rows, 39 journals, 301 journal-years; 96.83% ROR
  match on rows with a printed affiliation. Long table `editor_affiliations.csv` (11,661 rows).
- `editors_backfill_scale_row_key_crosswalk.csv` maps old to new `editor_row_key` (8,723 keys shifted after
  a parse fix).
- No `raw_html/` is in the repo. `source_file` columns name collector capture paths only (not in repo).
- Every file is byte-identical to the collector pack except `editors_backfill_scale_spotcheck.csv`: 55
  fragments of publisher subscription text that carried telephone/fax numbers were removed from 30
  `reverse_residue_examples` cells (`|| `-separated QC snippets). Its md5 in `_build.json` is therefore the
  pre-scrub value.
- No file is over 50 MB, so nothing here is gzipped.

Known gaps: RED 2021–25; JBES 2018–20 and 2025; JRU 2023; JUE 2018–19 partial; EJ 2018 low confidence;
about 4,017 names-only rows (AER, AER: Insights, JPE, JOLE, JLE and QJE print no affiliations and are
intentionally blank). Open ROR decisions stay blank: Virginia University Charlottesville→UVA,
INRA-AgroParisTech, Adelaide / Cergy-Pontoise successors, ECARES/CORE, Cowles, CEU Budapest.
Report: `docs/reports/BACKFILL_scale_ror_20261031.md`; QC: `docs/reports/PREPUBLISH_CHECK_20261101.md`.

---

# editors_backfill_scale_ror_20261031 — HELD (not published, not pushed, not handed to Web)

ROR harmonization of the backfill scale panel (`releases/editors_backfill_scale_20261101` — the input-fixed parse release, 39 journals, board years 2018–2025, 15,446 rows). Rebuilt 2026-11-01 (Asia/Taipei, UTC+8) against the local ROR v2.15 dump, following the backfill pilot ROR pack (`editors_backfill_pilot_ror_20261031`) and the latest multi-affiliation pack (`editors_ror_multiaff_20261031`). The source release and every earlier release are unchanged (md5 baseline re-verified after the build). Full report: `reports/BACKFILL_scale_ror_20261031.md`. Code: `reports/backfill_scale_work/ror2/` (s0–s8).

All CSVs keep the source CRLF line endings and UTF-8 encoding.

## 2026-11-01 rebuild: source change and user decisions
This pack was rebuilt in place (still HELD, never published) on the input-fixed parse release `releases/editors_backfill_scale_20261101` (report `reports/BACKFILL_scale_parse_20261101.md`) instead of `editors_backfill_scale_20261031`.

**Row-count change: 15,436 → 15,446 panel rows (+10).** The 10 added rows are inserted in journal/year order (new positions #6713–#8739), so **8,723 later rows shift position and get a new `editor_row_key`**; the crosswalk `editors_backfill_scale_row_key_crosswalk.csv` maps old → new `editor_row_key` (15,416 unchanged, 20 row_fixed, 10 row_added). Long table stays 11,661 parts (bleed text split off before is now fixed in the input; the added rows add parts). Rate: 96.94% (11,015/11,363) → **96.83% (11,013/11,373)**.

Rows changed versus the previous build (15,384 rows identical):

| change | rows | effect |
|---|---|---|
| System records with no campus printed blanked (University of Nebraska 0238rvs44 ×7, University of Alaska 01mtkd993 ×4, University of Hawaii 03tzaeb71 ×1) | 12 | matched → unmatched (`curated_block`, note names the old record) |
| Korea University (bare) kept blank; wrong Tokyo record 05m1gnk07 not applied | 20 | `ror_notes` wording only (already blank) |
| American, Western, ENS, Heidelberg (bare) — kept blank, proposed ids not applied | 0 | already blank; `BACKFILL_SCALE_ROR_unmatched_strings_*` text updated |
| 11 post15-blanked strings kept blank; 22 system_no_campus strings kept blank (no campus in print, city or profile domain) | 0 | already blank; category/proposed_handling text updated |
| ESSEC: France 02dga6j42 unless Singapore printed | 0 | all 21 rows already France (none print Singapore) |
| CEU stays 02zx40v98 | 0 | 5 rows, unchanged (1 prints Budapest, Hungary — country conflict kept by decision) |
| Parse fix: Michigan rows (text) | 6 | text only, ROR unchanged |
| Parse fix: de Mesquita rows | 4 | unmatched → University of Chicago 024mw5h28 |
| Parse fix: split-override rows lose bleed text (Iowa State 4, Oxford 2, Imperial 2, FRB St. Louis 2) | 10 | ROR unchanged; `affiliation_count` changes 222 → 212 |
| Parse fix: rows added | +10 | X L ×4 → Fudan 013q1eq08; R. Dieci ×2 → Bologna 01111rn36; R. Boucekkine ×4 → unmatched (Aix-Marseille, post15 blank kept) |

Matched arithmetic: 11,015 − 12 + 4 + 6 = 11,013.
Header changes versus the previous build: none in any existing file; one new file (the crosswalk).

## Counts
- Panel rows 15,446 (same row set and order as the source). Status: matched 11,021; unmatched 360; no_affiliation 4,017; staff_excluded 48 (new status).
- **Non-staff rows (the metric base): 15,224; with an affiliation 11,373; matched 11,013 = 96.83%**; unmatched 360; no affiliation 3,851.
- Confidence of matched non-staff rows: high 8,704 · medium 2,244 · low 65.
- Staff rows (role_class=staff): 222, excluded from all metrics — 8 matched (staff rows whose text is the editor's university affiliation), 48 staff_excluded (office/staff text, no ROR), 166 with no affiliation. Listed in `BACKFILL_SCALE_ROR_staff_rows_20261031.csv`.
- Names-only journals (no affiliations printed, all rows no_affiliation; nothing inferred from other years): AER, AER: Insights, JPE, JOLE, JLE, QJE.
- 474 distinct ROR ids. Long table: 11,661 printed affiliation parts (source table 11,457).

| journal | rows (non-staff) | with affiliation | matched | high | medium | low | unmatched | no affiliation | match rate | staff rows |
|---|---|---|---|---|---|---|---|---|---|---|
| AEJ: Applied Economics | 256 | 45 | 45 | 36 | 9 | 0 | 0 | 211 | 100.0% | 19 |
| AEJ: Economic Policy | 310 | 49 | 49 | 31 | 18 | 0 | 0 | 261 | 100.0% | 19 |
| AEJ: Macroeconomics | 139 | 29 | 26 | 21 | 5 | 0 | 3 | 110 | 89.7% | 18 |
| AEJ: Microeconomics | 171 | 29 | 29 | 29 | 0 | 0 | 0 | 142 | 100.0% | 20 |
| AER | 609 | 0 | 0 | 0 | 0 | 0 | 0 | 609 | n/a (names only) | 19 |
| AER: Insights | 154 | 0 | 0 | 0 | 0 | 0 | 0 | 154 | n/a (names only) | 9 |
| American Journal of Agricultural Economics | 297 | 297 | 269 | 208 | 60 | 1 | 28 | 0 | 90.6% | 0 |
| Econometric Theory | 490 | 490 | 464 | 383 | 81 | 0 | 26 | 0 | 94.7% | 0 |
| The Economic Journal | 390 | 390 | 380 | 307 | 73 | 0 | 10 | 0 | 97.4% | 13 |
| Economic Theory | 692 | 684 | 679 | 595 | 80 | 4 | 5 | 8 | 99.3% | 0 |
| Energy Economics | 317 | 317 | 309 | 242 | 67 | 0 | 8 | 0 | 97.5% | 0 |
| European Economic Review | 648 | 648 | 631 | 508 | 118 | 5 | 17 | 0 | 97.4% | 0 |
| Experimental Economics | 470 | 470 | 466 | 340 | 123 | 3 | 4 | 0 | 99.2% | 1 |
| Games and Economic Behavior | 262 | 262 | 254 | 201 | 53 | 0 | 8 | 0 | 97.0% | 4 |
| Health Economics | 391 | 383 | 380 | 217 | 163 | 0 | 3 | 8 | 99.2% | 8 |
| Journal of Applied Econometrics | 550 | 550 | 535 | 372 | 160 | 3 | 15 | 0 | 97.3% | 19 |
| Journal of Business and Economic Statistics | 432 | 344 | 320 | 262 | 58 | 0 | 24 | 88 | 93.0% | 4 |
| Journal of Development Economics | 646 | 640 | 639 | 499 | 140 | 0 | 1 | 6 | 99.8% | 0 |
| Journal of Econometrics | 568 | 485 | 480 | 408 | 72 | 0 | 5 | 83 | 99.0% | 6 |
| Journal of Economic Behavior and Organization | 662 | 595 | 566 | 412 | 131 | 23 | 29 | 67 | 95.1% | 1 |
| Journal of Economic Dynamics and Control | 573 | 569 | 555 | 449 | 102 | 4 | 14 | 4 | 97.5% | 0 |
| Journal of Economic Growth | 281 | 281 | 273 | 217 | 56 | 0 | 8 | 0 | 97.2% | 0 |
| Journal of Economic Literature | 239 | 16 | 16 | 16 | 0 | 0 | 0 | 223 | 100.0% | 17 |
| Journal of Environmental Economics and Management | 564 | 564 | 494 | 441 | 52 | 1 | 70 | 0 | 87.6% | 0 |
| Journal of the European Economic Association | 589 | 60 | 60 | 34 | 26 | 0 | 0 | 529 | 100.0% | 2 |
| Journal of Financial Econometrics | 447 | 447 | 425 | 335 | 84 | 6 | 22 | 0 | 95.1% | 8 |
| Journal of Health Economics | 363 | 363 | 356 | 281 | 75 | 0 | 7 | 0 | 98.1% | 0 |
| Journal of International Economics | 540 | 540 | 538 | 416 | 120 | 2 | 2 | 0 | 99.6% | 0 |
| Journal of Labor Economics | 195 | 0 | 0 | 0 | 0 | 0 | 0 | 195 | n/a (names only) | 0 |
| Journal of Law and Economics | 55 | 0 | 0 | 0 | 0 | 0 | 0 | 55 | n/a (names only) | 0 |
| Journal of Monetary Economics | 451 | 424 | 414 | 370 | 44 | 0 | 10 | 27 | 97.6% | 0 |
| Journal of Money, Credit and Banking | 638 | 126 | 126 | 126 | 0 | 0 | 0 | 512 | 100.0% | 0 |
| Journal of Political Economy | 238 | 0 | 0 | 0 | 0 | 0 | 0 | 238 | n/a (names only) | 0 |
| Journal of Risk and Uncertainty | 271 | 271 | 260 | 192 | 68 | 0 | 11 | 0 | 95.9% | 7 |
| Journal of Urban Economics | 355 | 355 | 354 | 268 | 86 | 0 | 1 | 0 | 99.7% | 4 |
| Quarterly Journal of Economics | 275 | 0 | 0 | 0 | 0 | 0 | 0 | 275 | n/a (names only) | 8 |
| RAND Journal of Economics | 282 | 282 | 260 | 198 | 49 | 13 | 22 | 0 | 92.2% | 8 |
| Review of Economic Dynamics | 107 | 107 | 107 | 70 | 37 | 0 | 0 | 0 | 100.0% | 0 |
| Review of Economics and Statistics | 307 | 261 | 254 | 220 | 34 | 0 | 7 | 46 | 97.3% | 8 |
| **all (non-staff)** | 15224 | 11373 | 11013 | 8704 | 2244 | 65 | 360 | 3851 | **96.83%** | 222 |

## Header changes — flag for Web
`editors_backfill_scale_ror_panel.csv` (vs `editors_backfill_scale_panel.csv`):
- **13 columns inserted before `ror_match_status`** (same names and order as the pilot ROR block): `institution`, `other_affiliations`, `canonical_name`, `ror_id`, `ror_name`, `ror_country`, `continent`, `lat`, `lon`, `ror_match_method`, `ror_match_score`, `ror_confidence`, `ror_notes`.
- **4 columns appended at the end** (multiaff convention): `ror_id_aff_rank`, `primary_aff_basis`, `former_flag`, `other_ror_ids`.
- `ror_match_status` was `not_attempted` everywhere; now `matched` / `unmatched` / `no_affiliation` / **`staff_excluded` (new value)**.
- `affiliation_count` (existing column) **recomputed on 212 rows** where printed parts were split (two institutions printed in one part, or another editor's text bled into the row); every change is in `BACKFILL_SCALE_ROR_affiliation_count_changes_20261031.csv`.
- Every other existing column (incl. `raw_affiliation`, `source`, `source_note`, `parse_flags`, `is_former`, `editor_row_key`) is byte-identical to the source.
- `editor_affiliations.csv` keeps its 20 columns; the ROR columns are now filled and rows were added for split parts (11,457 → 11,661). `editor_row_key` values unchanged (prefix `editors_backfill_scale_panel#…`).

### Panel ROR columns
| column | definition |
|---|---|
| `institution` | first printed affiliation part with street/ZIP/city/country segments removed; `raw_affiliation` is not altered |
| `other_affiliations` | further printed parts in print order, ` \| ` separated (all also in `editor_affiliations.csv`) |
| `canonical_name` | ror.org display name of `ror_id` (blank if unmatched) |
| `ror_id` | ROR id of the panel affiliation = the first matched, non-former printed part (rank in `ror_id_aff_rank`); blank if none |
| `ror_name`, `ror_country`, `continent`, `lat`, `lon` | from the ror.org record (v2.15; country is ror.org's, e.g. "The Netherlands") |
| `ror_match_method` | how it matched, e.g. `exact_text+ror_org_name_20261031` (high), `exact_text+ror_org_alias_20261031`, `curated_alias+…`, `curated_scale+…`, `campus_text_evidence+…`, `research_institute_named_20261031`, `approved_exception`, `exact_text+ror_org_name+consistency2_prior_tiebreak`; suffixes `+cleaned`, `+segment`, `+affix`, `+split_override`, `+wrap_join` give the text step. For unmatched rows the reason: `curated_block`, `no_exact_match`, `post15_blank_kept`, `ambiguous_name`, `inactive_blank`, `country_conflict` |
| `ror_match_score` | 1.0 on every matched row (matching is string equality, as in the pilot; the grading is in `ror_confidence`); blank otherwise |
| `ror_confidence` | `high` / `medium` / `low` (pilot levels) / `unmatched`; blank for no_affiliation and staff_excluded |
| `ror_notes` | evidence for the match or the reason for a blank |
| `ror_id_aff_rank` | printed part (1 = first) the panel `ror_id` comes from; blank if no ror |
| `primary_aff_basis` | `single` (one part), `unknown` (2+ parts, no printed evidence of primary), `none` (no text). No primary/secondary is asserted without printed evidence |
| `former_flag` | 1 if any printed part is marked former/retired/previously (0 rows here; past editors stay labelled by the existing `is_former`/`role_class=past`) |
| `other_ror_ids` | distinct matched ROR ids of the other printed parts, `;` separated (192 rows) |

### `editor_affiliations.csv` (one row per printed part)
`editor_row_key, panel_file, row_index, journal, year, editor_name, aff_text_source` (as source); `aff_rank` (print order); `raw_aff_part`; `split_basis` (single, first, and, ampersand, semicolon, comma_ror, **and_split_override** = two institutions printed in one part split here, **bleed_split_override** = next editor's text split off); `ror_id, ror_name, ror_country`; `ror_match_kind` (panel, exact_name, exact_alias, curated, curated_scale, blocked, none, inactive_blank, input_bleed_blank, staff_excluded); `ror_match_note`; `aff_role` (sole, unknown, emeritus …); `role_basis` (single / print_order / explicit_word); `role_evidence`; `relation_to_primary` (same / distinct / hierarchy / blank); `is_panel_ror` (1 = the part the panel ror points to).

## Files
- `editors_backfill_scale_ror_panel.csv` — the panel (above).
- `editor_affiliations.csv` — long table (above).
- `editors_backfill_scale_ror_matched.csv` (1,847 strings) / `editors_backfill_scale_ror_unmatched.csv` (86 strings) — one row per distinct printed `raw_affiliation` (pilot format: rows, journals, years, ROR block, status); staff excluded.
- `editors_backfill_scale_gaps.csv` — the source gaps file byte-for-byte as a prefix, plus 360 appended `ror_unmatched` rows (one per unmatched panel row).
- `editors_backfill_scale_inventory.csv`, `editors_backfill_scale_spotcheck.csv` — copied byte-for-byte from the source.
- `BACKFILL_SCALE_ROR_unmatched_strings_20261031.csv` — 91 unmatched printed part strings (379 long rows, non-staff) with `category` and `proposed_handling`.
- `BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv` — the table above.
- `BACKFILL_SCALE_ROR_spotcheck_20261031.csv` — stratified audit, 370 matched rows (ok 295, ok_low 60, ok_manual 15, 0 errors) (`spotcheck_reason`, `check_result`, `check_note`).
- `BACKFILL_SCALE_ROR_crosscheck_20261031.csv` — rule-8 cross-check vs consistency2 and the pilot (49 non-agreeing strings, each with a note; donor is consistency2 — none of the ids corrected or blanked in `editors_ror_consistency3_20261101` occur in this pack).
- `BACKFILL_SCALE_ROR_affiliation_count_changes_20261031.csv` (212), `BACKFILL_SCALE_ROR_ri_decisions_20261031.csv` (research-institute decisions), `BACKFILL_SCALE_ROR_curated_log_20261031.csv` (every curated map applied or rejected), `BACKFILL_SCALE_ROR_staff_rows_20261031.csv` (222).
- `editors_backfill_scale_row_key_crosswalk.csv` — **new file**, copied byte-for-byte from the source: old (20261031) → new (20261101) `editor_row_key`, `change` (unchanged / row_fixed / row_added).
- `_build.json` — source/output/doc md5s, new columns, status HELD.

## Matching rules (summary; details in the report)
1. Strict: only an **active** ROR v2.15 record whose name/label/alias equals the printed institution (after case/accent/punctuation folding), unique (within the printed country), and country-consistent. Never a guess: blank with a reason instead.
2. Curated short forms/typos are allowed only to an exact ror.org name (medium); misprinted names that do not exist are `low` with a `LOW:` note.
3. System → campus only with printed campus evidence (University of California / Maryland / Wisconsin / Illinois / North Carolina / Colorado / Texas / Massachusetts / Toulouse… stay blank). System *records* are not used either when no campus is printed: University of Nebraska 0238rvs44, University of Alaska 01mtkd993, University of Hawaii 03tzaeb71 are blanked (user decision 2026-11-01).
4. Research institutes with their own record get it (NBER, CEPR, IFS, CREST, CREI, EIEF, Hoover, LEDa …); units without one go to the printed parent only when the parent is printed.
5. Every printed part is kept in print order; the panel ror is the first matched non-former part; primary/secondary only with printed evidence.
6. Standing exceptions unchanged: 11KBW blank, UNSW → UNSW Sydney 03r8z3t63 (UNSW Canberra rule), INSEAD France 00ghzk478 / Singapore 05ynf4333 by printed campus, ESSEC France 02dga6j42 unless Singapore is printed (04be2h179), CEU → 02zx40v98 (ror.org country Austria; printed Budapest).
7. Names-only rows stay blank; nothing is inferred from other years or other journals.
8. Staff rows get no ROR unless the row is the editor's university affiliation (Data Editors).
