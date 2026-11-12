# Release notes — editors_backfill_ra_pack2_20261113 (HELD)

Base: live `editors_backfill_red_jbes_20261113` (PR #71), copied byte for byte.

## RA pack 2 person rows (Collector in-house, 13 Nov 2026)

These follow the RA-fix pattern of `RA_FIX_retry_changes_20261106.csv` and `RA_TA_merge_changes_20261106.csv`:
- `editor_name`, role, `source_url` and `board_urls` are unchanged. The board still printed nothing for these names.
- `raw_affiliation` / `institution` / `canonical_name` are filled.
- `affiliation_imputed=yes`.
- `parse_flags`: `no_affiliation_printed` is replaced by `ra_pack2_filled_20261113`.
- `source_note` gets an appended `| ra_pack2_20261113: … source=…; evidence=…`.
- The ROR fields are filled, with `ror_match_method=ra_pack2_20261113+panel_crosswalk`. For S15 it is `+ror_api_exact_name` instead.
- `ror_notes` carries the source URL and the year-covering CV evidence. Each fill gets one long row: rank 1, sole, single, `is_panel_ror=1`.

| Item | Key | Journal, year | Editor | Raw / institution | ROR |
|---|---|---|---|---|---|
| S01 | #999 | AER 2018 | ESTEBAN ROSSI-HANSBERG | Princeton University | 00hx57361 |
| S02 | #1055 | AER 2019 | MORITZ MEYER-TER-VEHN | University of California, Los Angeles | 046rm7j60 |
| S03 | #1089 | AER 2020 | PIERRE-OLIVIER GOURINCHAS | University of California, Berkeley | 01an7q238 |
| S04 | #1205 | AER 2021 | LOUKAS KARABARBOUNIS | University of Minnesota (Twin Cities, Minneapolis evidenced) | 017zqws13 |
| S05 | #1260 | AER 2022 | Nageeb Ali | Pennsylvania State University | 04p491231 |
| S06 | #1630 | AER: Insights 2021 | MARKUS K. BRUNNERMEIER | Princeton University | 00hx57361 |
| S07 | #1662 | AER: Insights 2022 | ANDRÉS RODRÍGUEZ-CLARE | University of California, Berkeley | 01an7q238 |
| S08 | #12660 | JPE 2021 | Alexander Cappelen | Norwegian School of Economics | 04v53s997 |
| S09 | #12694 | JPE 2022 | Wilbert van der Klaauw | Federal Reserve Bank of New York | 05hwvzg47 |
| S10 | #12737 | JPE 2023 | David Yanagizawa-Drott | University of Zurich | 02crff812 |
| S11 | #11338 | JOLE 2021 | CANICE J. PRENDERGAST | University of Chicago (Booth School of Business) | 024mw5h28 |
| S12 | #11356 | JOLE 2022 | ITAY SAPORTA-EKSTEN | Tel Aviv University | 04mhzgx49 |
| S13 | #11368 | JOLE 2023 | CHRISTIAN DUSTMANN | University College London | 02jx3x895 |
| S14 | #11452 | JLE 2020 | Dhammika Dharmapala | University of Chicago (CV: Chicago Law School 2015–2020) | 024mw5h28 |
| S15 | #11461 | JLE 2021 | Richard Holden | raw UNSW Business School / institution UNSW Sydney | 03r8z3t63 |
| S16 | #14135 | QJE 2020 | Gerard Padró i Miquel | Yale University | 03v76x132 |
| S17 | #14157 | QJE 2021 | Stefanie Stantcheva | Harvard University | 03vek6s52 |
| S18 | #14206 | QJE 2022 | Matthew Notowidigdo | University of Chicago (Booth School of Business) | 024mw5h28 |
| S20 | #2046 | Econometric Theory 2018 | G. Kuersteiner | printed "University of Maryland" kept | 047s2c258 University of Maryland, College Park |

ROR checks:
- All 15 distinct ids were re-checked in the ROR v2 API on 2026-11-13. All are active, and the name and country match.
- Every id was already used on live rows. Geo fields are copied from those rows.
- No EUI, UW-system or CEPR-UK id was assigned.

S20 details:
- `ror_match_method=campus_cv_evidence+ra_pack2_20261113`, `ror_confidence=medium`, as for the other campus-evidence rows.
- `ror_notes` records the March 2023 vita (Professor, University of Maryland since 2013; College Park address) and the university-system rule.

Not changed:
- #3864 (S19, CEPR, Montreal; ROR blank by user decision) and #5947 (S21, European U. Institute; ROR blank; 0031wrj91 not assigned).
- The non-substitute rows #11665, #14899, #6483, #433, #14257 and #15446.

## Match rates (touched journals only)

The rows are recomputed from the panel with the same formula used for JBES and RED in PR #71. These rows had not been recomputed when the earlier RA-TA / RA-fix fills (2026-11-06) were applied. The new counts therefore also include those 17 earlier fills: AER 5, AER: Insights 2, JPE 3, JOLE 3, JLE 2, QJE 2.

| Journal | With affiliation (before → after) | Matched | Rate |
|---|---|---|---|
| AER | 0 → 10 | 0 → 10 (5 new + 5 earlier) | n/a → 1.0000 |
| AER: Insights | 0 → 4 | 0 → 4 (2 + 2) | n/a → 1.0000 |
| JPE | 0 → 6 | 0 → 6 (3 + 3) | n/a → 1.0000 |
| JOLE | 0 → 6 | 0 → 6 (3 + 3) | n/a → 1.0000 |
| JLE | 0 → 4 | 0 → 4 (2 + 2) | n/a → 1.0000 |
| QJE | 0 → 5 | 0 → 5 (3 + 2) | n/a → 1.0000 |
| Econometric Theory | 490 → 490 | 464 → 465; unmatched 26 → 25 | 0.9469 → 0.9490 |

`rows_non_staff`, `no_affiliation` and `staff_rows_excluded` are taken from the recount (see `RA_pack2_match_rate_changes_20261113.csv`). The rows for all other journals are byte-identical.

## Kept as-is (documented, not edited)

- `editors_backfill_scale_gaps.csv` is byte-identical to live. The `no_affiliation_printed` gap rows for the 18 names stay, because the boards still print no affiliation (the same as for the earlier RA fills). The Econometric Theory 2018 `ror_unmatched` gap row for Kuersteiner is now superseded by the campus ROR on #2046, but it is kept: no gap rows are deleted.
- `editors_backfill_scale_ror_matched.csv` / `_unmatched.csv` (string-level summaries) are byte-identical to live. They were not rebuilt for the earlier RA fills either, and "University of Maryland" there still reads 47 rows / unmatched.
- Inventory is byte-identical. Journal-year coverage did not change.

## Whole-board collection outcomes (recorded only; no boards added)

- **FIX06 JRU 2023:** only the 2023 Springer home-page captures (Wayback 2023-05-04 and 2023-08-10) name the Editor-in-Chief, W. Kip Viscusi. No full dated board was found, so it is left as a gap (inventory no_snapshot / 0). No one-row Viscusi board was added.
- **S22 RED 2024:** the ScienceDirect editorial-board page for Vol 52, April 2024 (DOI 10.1016/S1094-2025(24)00006-1, free access) loaded, but the PDF hit a security-verification bot wall. The Wayback 2024-02-10 HTML has no board names (PDF-only, as for 2025). Left as a gap (inventory queued / 0). The SED society-page Wayback list from 2024-05-18 was not used as a 2024 board.
- **S23 JBES 2025:** JSTOR's journal holdings end at Vol 38 No 4 (2020). The T&F TOC for Vol 43 Issue 1 (2025) lists research articles only, with no Front Matter PDF. Left as a gap (inventory no_snapshot / 0). No undated T&F editorial-board page was used.
