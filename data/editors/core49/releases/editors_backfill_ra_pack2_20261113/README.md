# editors_backfill_ra_pack2_20261113 — pinned in this repo (2026-11-13)

**Publish note (2026-11-13, Asia/Taipei).** Published pending PR merge. It supersedes `editors_backfill_red_jbes_20261113` (PR #71) as the current core49 backfill. The older folders (`editors_backfill_red_jbes_20261113`, `editors_backfill_red_gap_20261112`, `editors_ra_ta_merge_rebuild_20261112`, `editors_backfill_scale_ror_20261031`) stay in the tree. The Directory site does not read core49 (it shows current boards only), so Directory counts are unaffected and `build_site.py` is unchanged. The collector's README follows below the line; its "HELD" status is historical. The collector's release notes are in `COLLECTOR_RELEASE_NOTES.md`.

- Panel `editors_backfill_scale_ror_panel.csv`: 15,873 rows (unchanged). Exactly 19 existing rows are updated in place (same keys, same order); every other line is byte-identical to `editors_backfill_red_jbes_20261113`.
- Long table `editor_affiliations.csv`: 12,120 rows (was 12,102; +18 appended, one per names-only fill: rank 1, sole, `is_panel_ror=1`). The only changed existing long row is the Kuersteiner row (`#2046`); all other live long rows are byte-identical.
- RA pack 2 names-only fills (18 rows, `affiliation_imputed=yes`, flag `ra_pack2_filled_20261113`), from year-specific CVs or faculty pages: AER 2018–2022 (#999, #1055, #1089, #1205, #1260), AER: Insights 2021–2022 (#1630, #1662), JPE 2021–2023 (#12660, #12694, #12737), JOLE 2021–2023 (#11338, #11356, #11368), JLE 2020–2021 (#11452, #11461), QJE 2020–2022 (#14135, #14157, #14206). Names, roles and board source URLs are unchanged.
- Econometric Theory 2018 G. Kuersteiner (`#2046`): campus ROR `047s2c258` (University of Maryland, College Park) from CV evidence under the campus-from-CV rule; the printed raw "University of Maryland" is kept.
- Match rates were recomputed for the 7 touched journals only. The recount also includes 17 earlier 2026-11-06 RA-TA / RA-fix fills that the live match-rate file had not reflected (`RA_pack2_match_rate_changes_20261113.csv`). Econometric Theory 0.9469 → 0.9490 (465 of 490 matched); AER, AER: Insights, JPE, JOLE, JLE and QJE are now 1.0000 on their few affiliated rows (previously blank). All other journal rows are byte-identical.
- All 15 distinct RORs on the 19 changed rows were re-checked as active in the ROR v2 API at publish; none is new to the backfill. `#3864` (CEPR, Montreal) and `#5947` (European U. Institute) stay ROR-blank.
- Inventory, gaps, staff rows, matched/unmatched, crosswalk and `editors_backfill_scale_spotcheck.csv` are byte-identical to `editors_backfill_red_jbes_20261113`. The spotcheck is the phone/fax-scrubbed web copy (md5 da6059469d1eee4d841cc9f2a58626f3).
- **The inherited source PDFs (`JBES_2019_editorial_board.pdf`, `JBES_2020_editorial_board.pdf`, `RED_2025_editorial_board.pdf`) were deliberately not published** (staff contact data). The RA pack 2 CV evidence is not published either. `_live_manifest_sha256.txt` (checksums of the collector's own working copy) is not published.
- CRLF line endings and headers are unchanged on every CSV. No emails, phones, or images.
- Still open: JRU 2023, RED 2024 and JBES 2025 (whole-board gaps); JUE 2018–2019 partial; EJ 2018 low confidence; remaining names-only rows; open ROR decisions S19 (CEPR, Montreal) and S21 (European U. Institute).

---

# core49 backfill freeze `editors_backfill_ra_pack2_20261113` — HELD, unpublished

Base: an exact copy of live `editors_backfill_red_jbes_20261113` (PR #71, squash `ceea925`). All base rows are byte-identical, including the scrubbed spotcheck.

This freeze applies only the 19 reviewed RA pack 2 person-row edits, which Collector worked in-house at the user's request (t242u). No whole-board year is added.

| Edit | Keys | Panel | Long |
|---|---|---|---|
| Names-only fills (S01–S18): raw, institution and ROR filled from a CV or faculty page covering the board year | 18 | 18 rows updated | 18 rows appended |
| S20 Kuersteiner, Econometric Theory 2018: campus ROR 047s2c258 (College Park, from his CV); printed raw kept | #2046 | 1 row updated | its existing long row updated |

- Totals: panel 15,873 (unchanged); long 12,120 (12,102 + 18). No new `editor_row_key`.
- Files changed vs live: panel, long, and match_rates (7 touched journals only).
- New files: `RA_pack2_changes_20261113.csv`, `RA_pack2_match_rate_changes_20261113.csv`, the builder and QC scripts with their logs, and `_live_manifest_sha256.txt`.
- All other files are byte-identical to live: gaps, inventory, spotcheck, staff rows, matched/unmatched strings, crosswalk, the earlier change CSVs and the PDFs.
- No Directory or `build_site.py` change.

Builder: `build_ra_pack2_20261113.py`. QC: `qc_ra_pack2_20261113.py` (see `qc_ra_pack2_20261113.log`).

Evidence (CVs and faculty pages) stays in `releases/RA_pack2_collector_work_20261113/evidence/`. It is DO NOT PUBLISH, because most of those files print emails or phones, and it is not copied here. Each changed row's `ror_notes` and `source_note` carries the public source URL.
