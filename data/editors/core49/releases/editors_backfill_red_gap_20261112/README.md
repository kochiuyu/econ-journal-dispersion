# editors_backfill_red_gap_20261112 — pinned in this repo (2026-11-12)

**Publish note (2026-11-12, Asia/Taipei).** Published with the current-board freeze `editors_current_leftovers_20261112`, pending PR merge. It supersedes `editors_ra_ta_merge_rebuild_20261112` (PR #69) as the current core49 backfill. The older folders (`editors_ra_ta_merge_rebuild_20261112`, `editors_backfill_scale_ror_20261031`) stay in the tree. The Directory site does not read core49 (it shows current boards only), so Directory counts are unaffected and `build_site.py` is unchanged for this pack. The collector's README follows below the line; its "UNPUBLISHED" status is historical.

- Panel `editors_backfill_scale_ror_panel.csv`: 15,664 rows (was 15,578; +86 appended, base rows byte-identical). Long table `editor_affiliations.csv`: 11,896 rows (was 11,810; +86 appended, one per new key).
- Review of Economic Dynamics 2022 (43 rows, `#15578`–`#15620`) and 2023 (43 rows, `#15621`–`#15663`) are now filled, from the Society for Economic Dynamics "Our Editors" page via Wayback (page versions modified 2021-04-14 and 2023-02-21; captures 20220219234913 and 20230324123429). These are the web page as printed, not the issue front matter.
- RED 2021 inventory fix: the inventory row now reads `ok_issue_front_matter`, rows_parsed 45, rows_with_affiliation 45, matching the 45 panel rows `#15446`–`#15490`. This clears the inconsistency noted at the PR #69 publish.
- Gaps: RED 2021–2023 `blocked` → `resolved` (row count unchanged at 4,568). Match rates: the RED row is recomputed (238 non-staff rows, 237 matched, 1 unmatched). Inventory: 3 rows changed, 312 rows.
- 31 distinct RORs on the new rows, all `active` in the ROR v2 API (re-checked at publish). One new row has no ROR and stays blank: `#15638` Anmol Bhandari (raw "Economics, Minneapolis, MN 55455", no institution printed).
- `editors_backfill_scale_spotcheck.csv` is byte-identical to the phone/fax-scrubbed web copy (md5 da6059469d1eee4d841cc9f2a58626f3, the same file as in `editors_ra_ta_merge_rebuild_20261112` and `editors_backfill_scale_ror_20261031`).
- CRLF line endings are preserved on every CSV. No `raw_html/`, emails, phones, or photos.
- Still open: RED 2024 (RA pack 2 item S22) and RED 2025; JBES 2019–2020 and 2025; JRU 2023.

---

# editors_backfill_red_gap_20261112 — core49 backfill: RED 2022/2023 boards and RED 2021 inventory fix (UNPUBLISHED)

**Base:** the live core49 backfill `editors_ra_ta_merge_rebuild_20261112`, as on edj-web main 59652942. It includes the **web's scrubbed `editors_backfill_scale_spotcheck.csv`** (byte-identical to the web copy), not the unscrubbed original. The Directory does not read core49.

## Changes
- **RED 2021 inventory fix (web follow-up B):** blocked/0 → `ok_issue_front_matter`, rows_parsed 45, rows_with_affiliation 45. The note now matches the 45 rows already published (#15446–#15490).
- **RED 2022 and 2023 boards (C):** 43 + 43 rows appended as backfill adds, keys `editors_backfill_scale_panel#15578`–`#15663`. Each has a matching long-table row. Source: the SED official "Our Editors" page (https://www.economicdynamics.org/editors/) via Wayback, since the ScienceDirect issue pages return 403 to the shell.
  - 2022: capture 20220219234913, page version modified 2021-04-14, unchanged in 20220629190402.
  - 2023: capture 20230324123429, page version modified 2023-02-21, unchanged in 20231211221936.
  - Recorded as printed on the page. The web page can differ from the printed issue; e.g. Bassetto is at FRB Chicago in the 2021 issue and at FRB Minneapolis on the page.
  - Inventory rows keep their issue labels (Vol 43 / Vol 47) and are marked ok_wayback with archive_url and snapshot_timestamp.
- **gaps:** RED 2021–2023 blocked → resolved. **match_rates:** RED row recomputed. The change list is in `RED_2022_2023_board_changes_20261112.csv`.
- **RORs:** 31 RORs, all API-active with fitting names and countries. University systems are not used; Wisconsin is the Madison campus 01y2jtd41, by evidence. One row has no ROR: #15638 Anmol Bhandari, raw "Economics, Minneapolis, MN 55455", because no institution is printed.
- **Contacts:** emails and phones are scrubbed from the raw text, and street lines are dropped (flag `street_lines_dropped`).

## QC
- All base rows are unchanged: 86 appended to the panel (15,578 → 15,664) and 86 to the long table (11,810 → 11,896). Headers are the same and CRLF is preserved on every file.
- The inventory, gaps and match_rates files change only the rows listed above, with no row-count changes. Keys are unique and there are no emails or phones in the new rows.
- The derived lists `editors_backfill_scale_ror_matched/unmatched.csv` and `row_key_crosswalk.csv` were not regenerated, same as in the base rebuild.

## Still open (not in this pack)
- **RED 2025:** unreachable. There is no Wayback capture of the 2025 board, and the live SED page returns 404. Needs the ScienceDirect Vol 55 (2025-01) Editorial Board front matter (https://www.sciencedirect.com/journal/review-of-economic-dynamics/vol/55; front matter PII S1094202524000541). That requires the box browser or CUHK Easy Access.
- **JBES 2019 and 2020:** unreachable. Needs JSTOR front matter for Vol 37 No 1 (Jan 2019) and Vol 38 No 1 (Jan 2020) via CUHK Easy Access (as for 2018: https://www.jstor.org/stable/44867911). There is no Wayback board-page capture, and Crossref only lists "Editorial Collaborators" items (10.1080/07350015.2019.1670479, 10.1080/07350015.2020.1826254), which are not boards.
- **RA pack 2 items** (RED 2024 S22, JBES 2025 S23, JRU 2023 FIX06) are untouched.
