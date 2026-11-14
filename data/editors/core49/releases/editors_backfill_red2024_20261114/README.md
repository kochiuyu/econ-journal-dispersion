# editors_backfill_red2024_20261114 — pinned in this repo (2026-11-14)

**Publish note (2026-11-14, Asia/Hong_Kong).** Published pending PR merge. It supersedes `editors_backfill_ra_pack2_20261113` (PR #72) as the current core49 backfill. The older folders (`editors_backfill_ra_pack2_20261113`, `editors_backfill_red_jbes_20261113`, `editors_backfill_red_gap_20261112`, `editors_ra_ta_merge_rebuild_20261112`, `editors_backfill_scale_ror_20261031`) stay in the tree. The Directory site does not read core49 (it shows current boards only), so Directory counts are unaffected and `build_site.py` is unchanged. The collector's README follows below the line; its "HELD" status is historical. The collector's release notes are in `COLLECTOR_RELEASE_NOTES.md`.

- Adds one journal-year, **Review of Economic Dynamics 2024** (previously a whole-board coverage gap), from the official RED Vol 52 (April 2024) Editorial Board, page ii: https://www.sciencedirect.com/science/article/pii/S1094202524000061 (DOI 10.1016/S1094-2025(24)00006-1).
- Panel `editors_backfill_scale_ror_panel.csv`: 15,917 rows (was 15,873; +44 appended, keys `editors_backfill_scale_panel#15873`–`#15916`). The live panel is an exact byte prefix of the new file: no existing row changed.
- Long table `editor_affiliations.csv`: 12,164 rows (was 12,120; +44 appended, one per new key: rank 1, sole, `is_panel_ror=1`). The live long table is an exact byte prefix: no existing long row changed.
- Roles as printed: CO-ORDINATING EDITOR 1, EDITORS 9, ASSOCIATE EDITORS 30, EDITORIAL ADVISORY BOARD 4. Conventions follow RED 2021/2025.
- ROR: 44 of 44 matched, 0 blank; 29 distinct ids, all already used in the backfill, all re-checked as active in the ROR v2 API at publish. No new ROR id.
- The 3 SED society officers (President, Treasurer, Secretary) are excluded from the panel and logged in gaps.
- Inventory: only the RED 2024 row changed (`queued` → `ok_issue_front_matter`, 44/44). Gaps: only the RED 2024 line changed (`queued` → `resolved`) plus the 3 officer lines appended. Match rates: only the RED row changed, 0.9965 (281/282) → 0.9969 (325/326).
- Staff rows, matched/unmatched, crosswalk and `editors_backfill_scale_spotcheck.csv` are byte-identical to `editors_backfill_ra_pack2_20261113`. The spotcheck is the phone/fax-scrubbed web copy (md5 da6059469d1eee4d841cc9f2a58626f3).
- **No PDF is published.** The inherited `JBES_2019_editorial_board.pdf`, `JBES_2020_editorial_board.pdf` and `RED_2025_editorial_board.pdf` (staff contact data) were deliberately withheld; the RED 2024 PDF was never in the freeze (the inventory/gaps `source_file` path refers to the collector's private copy). `_live_manifest_sha256.txt` (checksums of the collector's own working copy) is not published.
- CRLF line endings and headers are unchanged on every CSV. No emails, phones, or images.
- Still open: JBES 2025 and JRU 2023 (whole-board gaps); JUE 2018–2019 partial; EJ 2018 low confidence; remaining names-only rows; open ROR decisions S19 (CEPR, Montreal) and S21 (European U. Institute).

---

# core49 backfill freeze `editors_backfill_red2024_20261114`: HELD, unpublished

Base: live `editors_backfill_ra_pack2_20261113` (Directory PR #72). The base folder was copied, and its checksums were recorded in `_live_manifest_sha256.txt` before the build. QC confirms the base folder is unchanged.

This freeze adds one journal-year, **Review of Economic Dynamics 2024**. Before this freeze it was a whole-board coverage gap, with inventory and gaps both set to `queued`. No existing row is changed.

| Layer | Panel keys | Panel | Long | Source |
|---|---|---|---|---|
| RED 2024 | #15873–#15916 | 44 | 44 | RED Vol 52 (April 2024), Editorial Board, page ii. DOI 10.1016/S1094-2025(24)00006-1. https://www.sciencedirect.com/science/article/pii/S1094202524000061 |

- Totals: panel 15,917 (15,873 + 44); long 12,164 (12,120 + 44).
- Roles as printed:
  - CO-ORDINATING EDITOR 1
  - EDITORS 9
  - ASSOCIATE EDITORS 30
  - EDITORIAL ADVISORY BOARD 4
- `role_class`: editor 10, board 30, advisory 4.
- ROR: 44 of 44 matched, 0 blank. 29 distinct ids, all already used in the backfill, and all re-verified as active in the ROR v2 API on 2026-11-14. No new ROR id.
- SED society officers are excluded and logged in gaps: President Ellen McGrattan, Treasurer Erwan Quintin and Secretary Marina Azzimonti.
- RED match rate: 0.9965 (281/282) before, 0.9969 (325/326) after.

Conventions are copied verbatim from RED 2025 (`backfill_red_2025_20261113.py`), which follows RED 2021:
- printed heading = `role`;
- initials kept as printed, so `editor_name_raw` is the printed form;
- the 4 advisory-board names are expanded to prior RED full names in `editor_name`, as in 2021 and 2025;
- `raw_affiliation` is the printed address lines joined by a space;
- `institution` is the raw text without the trailing country;
- one printed affiliation per person, so primary is `single` with one long row (rank 1, `sole`);
- the curly apostrophe in La’O is stored as a straight one, as on 2021 and 2025;
- the misprint "V. Venkateswaren" is kept as printed.

The `pdftotext -raw` text of the 2024 page is byte-identical to the 2025 page. The builder asserts that every new panel row and long row equals its RED 2025 twin on all non-provenance fields.

Files changed vs base:
- panel and long (append only; the base files are byte prefixes);
- inventory (RED 2024 row only: `queued` → `ok_issue_front_matter`, 44/44);
- gaps (RED 2024 `queued` → `resolved`, plus 3 officer lines appended);
- match_rates (RED row only).

All other files are byte-identical to base.

New files:
- `RED_2024_board_changes_20261114.csv`
- `RED_2024_match_rate_changes_20261114.csv`
- `red_2024_board_extracted.csv`
- `RED_2024_board_source_20261114.md` (transcript)
- the builder `backfill_red2024_20261114.py` and its log
- the QC script `qc_red2024_20261114.py` and its log
- `_summary_20261114.json`, `_live_manifest_sha256.txt`
- the docs

**The source PDF is not in this folder.** It stays unpublished at `abs_ajg/reports/RED_2024_editorial_board.pdf`. The CUHK proxy URL is not recorded in any data file.

There are no header changes and no line-ending changes; CRLF is kept on every changed CSV. There are no emails or phones. No Directory or `build_site.py` change.
