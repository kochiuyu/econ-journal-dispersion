# editors_ror_consistency3b_20261101 — published (Directory copy, 2026-11-01)

**Publish note (2026-11-01, Asia/Hong_Kong).** The user approved publishing this freeze together with
`editors_backfill_scale_ror_20261031` (pinned under `data/editors/core49/releases/`). The nine current
panels are copied into `data/editors/{abdc,abs_ajg_gap,ft50}/releases/current/`. This folder holds the
shared long table and the audit files. The collector's README follows below the line; its "HELD" status
is historical. The `*_with_profile_pilot.csv` files are **not** published.

## What the Directory copy changes vs the collector pack

| Change | Rows |
|---|---:|
| ajg1 navigation / citation rows kept out (incl. Vincent Pan on Advances in Decision Sciences, plus the blank JITM row) | 10 removed from the CSV; the build name filter drops 15 more |
| Collector institution-string rewrites reverted to the published text (`Italian Cultural Institute`, `National Law University`; ROR stays as in the collector, i.e. blank) | 78 |
| HKUST (Guangzhou) seats the collector collapsed onto HKUST: published text and `050h0vm43` restored | 11 |
| Junk collector rewrites (`PhD – Assistant Research Professor`, `Springer Nature (Shanghai`, `Korea Telecom`, `Ikon Science`, `Nihon University`, `IZZI Inc`, `Czech Academy of Sciences`) reverted; ROR blanked because the old id was wrong | 6 |
| `editor_name_raw` "Jaap Paauwe, Tilburg" restored on both FT50 files | 2 |
| REStud "Universitat Pompeu Fabra" institution-as-name rows (the collector removed them from A* but not FT50) | 2 per FT50 file |
| Top 5 rows the collector added only to ABDC A* (`t39_final15_fix_20261030`: AER Erik Snowberg, AER Juan Carlos Suárez Serrato, REStud Mikkel Plagborg-Moller) copied into both FT50 files so every Top 5 seat stays an FT50 seat | 3 per FT50 file |
| Email addresses and phone/fax numbers removed from text cells (mostly `source_note` editorial-office lines; URL columns untouched). Eleven ABDC B rows whose `editor_name` was only a phone/fax line (German Economic Review 9, China and World Economy, South African Journal of Economics) now have a blank `editor_name`; the build drops them | a 217, a* 513, b 12, c 13, ajg1 30, ajg2 6, ft50 625, ft50_with_ror 626 cells |
| `faculty_profile_url` cells that embedded an email address blanked (A 1, A* 1) | 2 |

Every restore is listed in `DIRECTORY_GUARDRAILS_restored_rows_20261101.csv`; restored panel rows carry
`directory_guardrail_restore_20261101` in `ror_notes`. The Top 5 copies are listed in
`DIRECTORY_TOP5_FT50_align_20261101.csv` and tagged `top5_ft50_align_20261101` in `ror_notes`.

## Long table

`editor_affiliations.csv.gz` (gzip -9, 7.4 MB; 63.2 MB uncompressed, so it is gzipped to stay under the
50 MB file-size limit). 181,443 rows, one per affiliation part, keyed by `editor_row_key`. Versus the
collector file it drops the 88,082 rows of the unpublished `*_with_profile_pilot.csv` panels and 14 rows
whose panel row is not published (nav/junk), mirrors the 101 text restores (panel ROR and `is_panel_ror`),
and scrubs 30 contact cells. The three Top 5 FT50 copies have no FT50 long rows (their A* rows are there).

## Files

- `editor_affiliations.csv.gz` — long table (see above)
- `ROR_PREPUBLISH_FIX_changes_20261101.csv` — collector pre-publish fix log (unchanged)
- `DIRECTORY_GUARDRAILS_restored_rows_20261101.csv`, `DIRECTORY_TOP5_FT50_align_20261101.csv` — Directory copy logs
- `_build.json` — collector manifest, with a `web_publish` block added
- this README

Reports: `docs/reports/PREPUBLISH_CHECK_20261101.md`, `docs/reports/ROR_PREPUBLISH_FIX_20261101.md`,
`docs/reports/ROR_CONSISTENCY3_20261101.md`.

---

# editors_ror_consistency3b_20261101 — HELD (not published, not pushed, not handed to Web)

Built 2026-11-01 (Asia/Hong_Kong, UTC+8) from `releases/editors_ror_consistency3_20261101`. That pack and every other existing release are unchanged. Nothing has been pushed or published.

## Why this pack
Pre-publish check (`reports/PREPUBLISH_CHECK_20261101.md`) flagged defects before handoff. This pack supersedes consistency3 for the current-panel line.

## What changed

### 1. Heidelberg Ohio residual (HIGH) — **kept, not blanked**
`editors_abdc_c_current#2971` Salil Khetani was flagged as bare "Heidelberg University" still on Ohio `04rcqnp59`. Inspection of `raw_affiliation` shows **`Heidelberg University, Ohio, United States`**. Consistency3 rule keeps `04rcqnp59` when Ohio/Tiffin is printed. The check misfired on `canonical_name` alone. **No ROR blank applied.** Audit row recorded in the changes CSV.

### 2. Panel ↔ long `is_panel_ror` desyncs (MEDIUM) — **17 rows synced**
For each of the 17 panel rows that had `ror_id` set but no long part with `is_panel_ror=1`, the matching long part was updated to carry the panel primary ROR and `is_panel_ror=1`. Panel primary `ror_id` was **not** blanked and **no system ROR was reintroduced**.

| case | n | long fix |
|---|---|---|
| University of Maryland → College Park `047s2c258` (campus evidenced by printed College Park and/or `umd.edu` profile / panel campus-over-system already applied) | 10 | set aff_rank=1 to College Park + `is_panel_ror=1` |
| Ewing Marion Kauffman Foundation `0288es483` | 2 | set aff_rank=2 + `is_panel_ror=1` |
| Georgian National Academy of Sciences `05aav2h42` | 2 | set aff_rank=1 + `is_panel_ror=1` |
| Beijing University of Posts and Telecommunications `04w9fbh59` | 1 | set aff_rank=1 + `is_panel_ror=1` |
| Salisbury University `029gwvs11` | 1 | set aff_rank=1 + `is_panel_ror=1` |
| Ludwig-Maximilians-Universität München `05591te55` | 1 | set aff_rank=1 + `is_panel_ror=1` |

Panel meta on those rows: empty `ror_id_aff_rank` filled with the synced aff_rank; `ror_notes` appended with `ror_prepublish_fix_20261101` sync note. No other panel cells changed.

### 3. Alós accent spotcheck (LOW) — **no change**
Carlos Alós-Ferrer (Economic Theory 2021): leave source/panel text as-is; missing accent in Wayback HTML text layer is capture encoding, not a panel invent. Accents not invented.

## Fields written
- Long: `ror_id`, `ror_name`, `ror_country`; `ror_match_kind` = `consistency3b_sync` (new); `ror_match_note` appended; `is_panel_ror` = 1 on the synced part.
- Panel (synced keys only): `ror_id_aff_rank` (if was empty), `ror_notes` append.
- **Header changes: none.** Row counts identical to consistency3.

## Verification
- Heidelberg `#2971` still `04rcqnp59` with Ohio printed.
- Panel ↔ long `ror_id` vs `is_panel_ror=1`: **0 mismatches** across all 11 panels.
- `affiliation_count` == long part count on all 17 synced keys.
- Headers and row counts unchanged vs consistency3.

## Files
- 11 current panels (same names as consistency3)
- `editor_affiliations.csv`
- `ROR_PREPUBLISH_FIX_changes_20261101.csv`
- `_build.json`, this README

## Publish note
When the user says publish, hand **`editors_ror_consistency3b_20261101`** (not consistency3) together with `editors_backfill_scale_ror_20261031`. See `reports/ROR_PREPUBLISH_FIX_20261101.md`.
