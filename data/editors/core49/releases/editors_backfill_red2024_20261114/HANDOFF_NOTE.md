# HANDOFF NOTE: editors_backfill_red2024_20261114 (HELD; not published, no PR)

For Journal-Editor-Web: this freeze replaces live core49 `editors_backfill_ra_pack2_20261113` (PR #72). It adds RED 2024 (Review of Economic Dynamics), which was a whole-board coverage gap.

- **No header changes.** No line-ending changes (CRLF kept). No existing row changed: the live panel and long files are byte prefixes of the new ones.
- Panel 15,917 (+44, keys #15873–#15916). Long 12,164 (+44).
- Changed files:
  - panel and long (append only);
  - inventory (RED 2024 row only);
  - gaps (RED 2024 queued → resolved, plus 3 SED officer lines);
  - match_rates (RED row only, 0.9965 → 0.9969).
- All other files are byte-identical to live.
- ROR: 44 of 44 matched, 0 blank. No new ROR id; all 29 ids are already in the backfill and re-verified active in the ROR API on 2026-11-14.
- Source: the official journal front matter, RED Vol 52 (April 2024), page ii. DOI 10.1016/S1094-2025(24)00006-1. https://www.sciencedirect.com/science/article/pii/S1094202524000061

Publish:
- the 5 changed CSVs plus the other unchanged CSVs;
- `RED_2024_board_changes_20261114.csv`, `RED_2024_match_rate_changes_20261114.csv`, `red_2024_board_extracted.csv`;
- `RED_2024_board_source_20261114.md`;
- README, CHANGES, QC_REPORT, `_build.json`, `_summary_20261114.json`, the scripts and the logs.

**Do NOT publish any PDF.**
- The RED 2024 PDF is deliberately not in this folder (it stays at `abs_ajg/reports/`).
- The inherited `JBES_2019_editorial_board.pdf` / `JBES_2020_editorial_board.pdf` print staff contacts.
- The inherited `RED_2025_editorial_board.pdf` should also stay unpublished.

Repeat these checks after publishing:
- panel 15,917 / long 12,164;
- keys #15873–#15916 unique;
- inventory RED 2024 `ok_issue_front_matter` 44/44;
- RED match rate 0.9969.

QC: `qc_red2024_20261114.py`, result in `qc_red2024_20261114.log` / `QC_REPORT.md`. Directory and `build_site.py`: no change.

Still open, not touched: JBES 2025 and JRU 2023 whole-board gaps; JMID re-harvest (user decision).
