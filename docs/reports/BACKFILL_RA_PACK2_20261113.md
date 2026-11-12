# core49 backfill — RA pack 2 names-only fills and Kuersteiner campus ROR (2026-11-13)

Freeze: `data/editors/core49/releases/editors_backfill_ra_pack2_20261113/` (collector freeze of the same name). It supersedes `editors_backfill_red_jbes_20261113` (PR #71), which stays in the tree with `editors_backfill_red_gap_20261112`, `editors_ra_ta_merge_rebuild_20261112` and `editors_backfill_scale_ror_20261031`. The Directory site does not read core49, so Directory panels, catalogs and `scripts/build_site.py` are unchanged.

## What changed

| | Before (`editors_backfill_red_jbes_20261113`) | After |
|---|---:|---:|
| Panel rows (`editors_backfill_scale_ror_panel.csv`) | 15,873 | 15,873 (19 rows updated in place) |
| Long rows (`editor_affiliations.csv`) | 12,102 | 12,120 (+18 appended; 1 existing row updated) |
| Inventory / gaps / staff rows | 312 / 4,620 / 225 | byte-identical |
| Econometric Theory match rate | 0.9469 | 0.9490 |

### 18 names-only fills (RA pack 2)

Each fill comes from a year-specific CV or faculty page. `raw_affiliation`, `institution` and `canonical_name` are filled; `affiliation_imputed=yes`; `parse_flags` `no_affiliation_printed` → `ra_pack2_filled_20261113`; the source is appended to `source_note`; ROR fields are filled. Names, roles, `source_url` and `board_urls` are unchanged. Each fill has one new long row (rank 1, sole, `is_panel_ror=1`).

| Key | Journal, year | Editor | Institution | ROR |
|---|---|---|---|---|
| #999 | AER 2018 | Esteban Rossi-Hansberg | Princeton University | 00hx57361 |
| #1055 | AER 2019 | Moritz Meyer-ter-Vehn | University of California, Los Angeles | 046rm7j60 |
| #1089 | AER 2020 | Pierre-Olivier Gourinchas | University of California, Berkeley | 01an7q238 |
| #1205 | AER 2021 | Loukas Karabarbounis | University of Minnesota | 017zqws13 |
| #1260 | AER 2022 | Nageeb Ali | Pennsylvania State University | 04p491231 |
| #1630 | AER: Insights 2021 | Markus K. Brunnermeier | Princeton University | 00hx57361 |
| #1662 | AER: Insights 2022 | Andrés Rodríguez-Clare | University of California, Berkeley | 01an7q238 |
| #12660 | JPE 2021 | Alexander Cappelen | Norwegian School of Economics | 04v53s997 |
| #12694 | JPE 2022 | Wilbert van der Klaauw | Federal Reserve Bank of New York | 05hwvzg47 |
| #12737 | JPE 2023 | David Yanagizawa-Drott | University of Zurich | 02crff812 |
| #11338 | JOLE 2021 | Canice J. Prendergast | University of Chicago (Booth) | 024mw5h28 |
| #11356 | JOLE 2022 | Itay Saporta-Eksten | Tel Aviv University | 04mhzgx49 |
| #11368 | JOLE 2023 | Christian Dustmann | University College London | 02jx3x895 |
| #11452 | JLE 2020 | Dhammika Dharmapala | University of Chicago | 024mw5h28 |
| #11461 | JLE 2021 | Richard Holden | UNSW Business School / UNSW Sydney | 03r8z3t63 |
| #14135 | QJE 2020 | Gerard Padró i Miquel | Yale University | 03v76x132 |
| #14157 | QJE 2021 | Stefanie Stantcheva | Harvard University | 03vek6s52 |
| #14206 | QJE 2022 | Matthew Notowidigdo | University of Chicago (Booth) | 024mw5h28 |

### Econometric Theory 2018 G. Kuersteiner (#2046)

Campus ROR `047s2c258` (University of Maryland, College Park) under the campus-from-CV rule: the March 2023 vita gives Professor, University of Maryland since 2013, with a College Park address. The printed raw “University of Maryland” and the institution are kept; only ROR fields changed on the panel row and its existing long row (`is_panel_ror` 0 → 1). Never a system ROR.

### Match rates

Rows were recomputed from the panel for the 7 touched journals only; every other journal row is byte-identical. The recount also picks up 17 earlier 2026-11-06 RA-TA / RA-fix fills that the live file had not reflected (AER 5, AER: Insights 2, JPE 3, JOLE 3, JLE 2, QJE 2). Details: `RA_pack2_match_rate_changes_20261113.csv`.

| Journal | With affiliation | Matched | Rate |
|---|---|---|---|
| AER | 0 → 10 | 0 → 10 | blank → 1.0000 |
| AER: Insights | 0 → 4 | 0 → 4 | blank → 1.0000 |
| JPE | 0 → 6 | 0 → 6 | blank → 1.0000 |
| JOLE | 0 → 6 | 0 → 6 | blank → 1.0000 |
| JLE | 0 → 4 | 0 → 4 | blank → 1.0000 |
| QJE | 0 → 5 | 0 → 5 | blank → 1.0000 |
| Econometric Theory | 490 → 490 | 464 → 465 | 0.9469 → 0.9490 |

## Checks at publish (2026-11-13, Asia/Taipei)

- Panel key order is identical; exactly the 19 keys in `RA_pack2_changes_20261113.csv` differ, and every other panel line is byte-identical to `editors_backfill_red_jbes_20261113`. All 19 are `matched`.
- Long table: the live rows are byte-identical except the one #2046 row; 18 rows are appended, one per fill, and agree with the panel ROR.
- The 15 distinct RORs on changed rows were re-checked in the ROR v2 API: all active, and the display name and country match. None is new to the backfill.
- #3864 (S19, CEPR, Montreal) and #5947 (S21, European U. Institute) are unchanged and ROR-blank.
- Inventory, gaps, staff rows, matched/unmatched, crosswalk and the spot check are byte-identical to the previous web copy. `editors_backfill_scale_spotcheck.csv` md5 `da6059469d1eee4d841cc9f2a58626f3` (phone/fax-scrubbed web copy).
- CRLF line endings and headers are unchanged on every CSV.
- The collector QC (`qc_ra_pack2_20261113.py`) was re-run against the web folders: 60 PASS / 0 FAIL (`qc_ra_pack2_20261113_web_rerun.log`; the collector-manifest check is skipped because that file is not published; collector run 61/61).
- Privacy: no emails, phone numbers, PDFs or images in the published folder.

## Not published

- `JBES_2019_editorial_board.pdf`, `JBES_2020_editorial_board.pdf`, `RED_2025_editorial_board.pdf` (inherited source PDFs; staff contact data).
- The RA pack 2 CV evidence (collector work folder, not in the freeze).
- `_live_manifest_sha256.txt` (checksums of the collector's own working copy).

## Still open

JRU 2023 (`no_snapshot`), RED 2024 (`queued`) and JBES 2025 (`no_snapshot`); JUE 2018–2019 partial; EJ 2018 low confidence; remaining names-only rows; open ROR decisions S19 and S21. See `data/editors/core49/STATUS.md`.
