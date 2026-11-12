# editors_backfill_red_jbes_20261113 — pinned in this repo (2026-11-13)

**Publish note (2026-11-13, Asia/Taipei).** Published pending PR merge. It supersedes `editors_backfill_red_gap_20261112` (PR #70) as the current core49 backfill. The older folders (`editors_backfill_red_gap_20261112`, `editors_ra_ta_merge_rebuild_20261112`, `editors_backfill_scale_ror_20261031`) stay in the tree. The Directory site does not read core49 (it shows current boards only), so Directory counts are unaffected and `build_site.py` is unchanged. The collector's README follows below the line; its "HELD, unpublished" status is historical. The collector's release notes are in `COLLECTOR_RELEASE_NOTES.md`.

- Panel `editors_backfill_scale_ror_panel.csv`: 15,873 rows (was 15,664; +209 appended, base rows byte-identical). Long table `editor_affiliations.csv`: 12,102 rows (was 11,896; +206 appended).
- Review of Economic Dynamics 2025: 44 rows, `#15664`–`#15707`, from the RED Vol 55 (2025-01) issue front matter (re-used verbatim from the collector's intermediate freeze `editors_backfill_red_2025_20261113`). Inventory `ok_issue_front_matter` 44/44; 44 long rows.
- Journal of Business and Economic Statistics 2019: 87 rows, `#15708`–`#15794`, from Vol 37 No. 1 (January 2019) front matter, https://www.jstor.org/stable/45181150. Inventory `ok_issue_front_matter` 87/84; 87 long rows (3 two-place rows split; 3 panel-only rows with no printed affiliation).
- Journal of Business and Economic Statistics 2020: 78 rows, `#15795`–`#15872`, from Vol 38 No. 1 (January 2020) front matter, https://www.jstor.org/stable/45282197. Inventory `ok_issue_front_matter` 78/75; 75 long rows.
- Match rates: JBES 0.9302 (681 non-staff rows, 546 matched, 41 unmatched; was 0.9322); RED 0.9965 (282 rows, 281 matched; was 0.9958). Gaps: 4,620 rows (was 4,568): RED 2025 `queued` → `resolved`, plus RED 2025 society-officer exclusions and the JBES 2019/2020 ASA Committee on Publications exclusions and no-affiliation rows. Staff rows: 225 (was 223; editorial coordinator 2019 and 2020).
- Two printed accents restored in the 2020 rows only, after a visual check of the 2020 page: `#15843` Marcelo Medeiros, "Pontificia Universidade Católica" (left unmatched, ROR blank: several PUCs, no campus printed); `#15853` Christoph Rothe, "Universität Mannheim" (ROR `031bsb921`, University of Mannheim). 2021–2024 rows are unchanged.
- One ROR is new to the backfill: `02jkmyk67` (Academy of Mathematics and Systems Science, CAS). All 83 distinct RORs on the new rows were re-checked as active in the ROR v2 API at publish (collector QC re-run: 51 PASS, 0 FAIL).
- **The source PDFs (`JBES_2019_editorial_board.pdf`, `JBES_2020_editorial_board.pdf`, and `RED_2025_editorial_board.pdf`) were deliberately not published.** The JBES front matter prints staff contact emails and a phone number. The transcriptions and extracts here carry no contact data.
- `editors_backfill_scale_spotcheck.csv` is byte-identical to the phone/fax-scrubbed web copy (md5 da6059469d1eee4d841cc9f2a58626f3, the same file as in `editors_backfill_red_gap_20261112`).
- Byte-prefix: the live base bytes are an exact prefix of the new panel, long table, and staff rows. The collector's intermediate freeze (base + RED 2025) is an exact prefix of the panel, long, gaps, and staff files. The gaps file is not a byte prefix of the live base, because the RED 2025 `queued` row was resolved in place.
- CRLF line endings and headers are unchanged on every CSV. No `raw_html/`, emails, phones, or photos.
- Still open: RED 2024 (RA pack 2 item S22); JBES 2025 (RA pack 2 item S23); JRU 2023.

---

# core49 backfill freeze `editors_backfill_red_jbes_20261113` — HELD, unpublished

Base: live `editors_backfill_red_gap_20261112` (Directory PR #70, edj-web `21df6bd`). Base rows byte-identical (scrubbed spotcheck kept).

Adds on top of the base:

| Layer | Panel keys | Panel | Long | Source |
|---|---|---|---|---|
| RED 2025 (re-used verbatim from `editors_backfill_red_2025_20261113`) | #15664–#15707 | 44 | 44 | RED Vol 55 (2025-01) front matter |
| JBES 2019 | #15708–#15794 | 87 | 87 | JBES Vol 37 No. 1 (Jan 2019) front matter p.3, https://www.jstor.org/stable/45181150 |
| JBES 2020 | #15795–#15872 | 78 | 75 | JBES Vol 38 No. 1 (Jan 2020) front matter p.3, https://www.jstor.org/stable/45282197 |

Totals: panel 15,873 (= 15,708 + 165), long 12,102 (= 11,940 + 162). JBES 2019 has 3 two-place rows (Frölich, Scaillet, Tarozzi), split as in 2018, so it gets 87 long rows. Hutchens, Martin and Zellner are panel-only.

Conventions follow JBES 2018 (`jbes_2018_board_20261106`):
- Roles as printed.
- `editor_name_raw` = "Name - Affiliation".
- The Committee on Publications is excluded and logged in gaps.
- The 2019 page reprints the 2018 list exactly: 86 names, same order, same affiliations, plus Hutchens. Each 2018 row and long row was cloned with 2019 provenance, so the ROR decisions are identical.
- For 2020, a printed string already on a JBES row (2018, 2021–2024) reuses that decision, including deliberate blanks. A new string gets a ROR only on an exact or accent-folded ROR name match that is API-active.

Files changed vs base: panel, long, inventory (JBES 2019/2020 and RED 2025 rows only), gaps (appended; RED 2025 row resolved), match_rates (JBES and RED rows only), staff_rows (Hutchens 2019/2020 appended). All other data files are byte-identical. No Directory or `build_site.py` change.

Builder: `backfill_red_jbes_20261113.py` (also `abs_ajg/scripts/`). QC: `qc_red_jbes_20261113.py`, 51 PASS / 0 FAIL (see log).
