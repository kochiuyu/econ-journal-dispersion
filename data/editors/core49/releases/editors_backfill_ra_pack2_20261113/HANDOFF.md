# HANDOFF — editors_backfill_ra_pack2_20261113 (HELD; not published, no PR)

Status: built and QC'd but **not handed to Journal-Editor-Web**. When it is approved, this freeze replaces live core49 `editors_backfill_red_jbes_20261113` (PR #71).

What it changes:
- 19 person-row updates:
  - 18 RA pack 2 names-only fills (S01–S18), each with one new long row;
  - S20 Kuersteiner, Econometric Theory 2018: campus ROR 047s2c258 on the existing row and long row.
- Changes are keyed in `RA_pack2_changes_20261113.csv`.
- match_rates rows are recomputed for the 7 touched journals; see `RA_pack2_match_rate_changes_20261113.csv` and RELEASE_NOTES.
- Panel 15,873 (unchanged); long 12,120 (+18).

Unchanged:
- The three whole-board gaps: JRU 2023 (no_snapshot), RED 2024 (queued) and JBES 2025 (no_snapshot). No rows were added, and the inventory and gaps files are byte-identical to live.
- S19 (#3864 CEPR, Montreal) and S21 (#5947 European U. Institute) stay ROR-blank.

Publish:
- the panel, long and match_rates CSVs, plus the other unchanged CSVs;
- `RA_pack2_changes_20261113.csv` and `RA_pack2_match_rate_changes_20261113.csv`;
- the docs, scripts and logs.

**Do NOT publish** the inherited `JBES_2019_editorial_board.pdf` / `JBES_2020_editorial_board.pdf`: their front matter prints staff contacts. The RA pack 2 CV evidence is not in this folder; it stays in the work folder, which is DO NOT PUBLISH.

Directory and `build_site.py`: no change.

QC path: `releases/editors_backfill_ra_pack2_20261113/qc_ra_pack2_20261113.py`, output in `qc_ra_pack2_20261113.log`.

Repeat these checks after publishing:
- panel 15,873 / long 12,120;
- the 19 keys listed in `RA_pack2_changes_20261113.csv` are matched;
- Econometric Theory match rate 0.9490.
