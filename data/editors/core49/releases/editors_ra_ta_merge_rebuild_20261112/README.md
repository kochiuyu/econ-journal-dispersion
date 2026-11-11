# editors_ra_ta_merge_rebuild_20261112 — pinned in this repo (2026-11-12)

**Publish note (2026-11-12, Asia/Taipei).** The user approved publishing this core49 backfill rebuild onto the public backfill. It replaces `editors_backfill_scale_ror_20261031` (PR #41) as the current core49 backfill; the older folder stays in the tree. The Directory site does not read core49 (it shows current boards only), so Directory counts are unaffected. The collector's README follows below the line; its "HELD" status is historical.

- Panel `editors_backfill_scale_ror_panel.csv`: 15,578 rows (was 15,446; +132 new, 20 changed, base key order kept). Long table `editor_affiliations.csv`: 11,810 rows (was 11,661; +149 inserted, 3 updated).
- Review of Economic Dynamics 2021 (45 rows, `#15446`–`#15490`) and Journal of Business and Economic Statistics 2018 (87 rows, `#15491`–`#15577`) are now filled. 20 RA/TA and FIX-retry rows updated (S01–S20). JRU 2023 is still missing.
- Gaps 4,568 rows (was 4,539); staff rows 223 (was 222); inventory 312 rows. 83 distinct RORs on new or changed rows, all active in the ROR API (re-checked at publish). Blanks stay blank (S19 Adelaide, S20 ECARES).
- `editors_backfill_scale_spotcheck.csv` is the web copy from `editors_backfill_scale_ror_20261031`, not the collector file: the collector file still carries the 55 phone/fax fragments in 30 `reverse_residue_examples` cells that were removed at the PR #41 publish. Its content is otherwise unchanged in this rebuild, and its md5 in `_build.json` is the pre-scrub value.
- Known inconsistency carried from the collector pack: the inventory row for Review of Economic Dynamics 2021 still reads `status=blocked`, `rows_parsed=0` (only its source columns were updated), although the panel now has its 45 rows. It is published as delivered.
- CRLF line endings match the base on every base file. No `raw_html/`, emails, phones, or photos.

---

# editors_ra_ta_merge_rebuild_20261112 (HELD, unpublished, historical backfill)

This is a rebuild of held pack `editors_ra_ta_merge_20261106` onto the published backfill `editors_backfill_scale_ror_20261031`. That backfill is in the web repo at `data/editors/core49/releases/` (PR #41), and the web copy is byte-identical to the local base. The user approved publishing this onto the public backfill on 2026-11-12. Collector has not published it or opened a PR.

The Directory site does not read the backfill (core49 STATUS.md), so this pack has no effect on current-panel Directory counts. It does not conflict with editors_school_unit_leftover_20261112 or editors_leftover_fixes_20261112.

## Content (unchanged from the held pack)
- **20 updated rows:** 17 RA TA merge rows (S01–S10, S12, S13, S15–S19) and 3 FIX retries (S11 Lochner → Western Ontario; S14 Carlton → Chicago Booth; S20 Castanheira → ECARES with ROR blank).
- **Review of Economic Dynamics 2021:** 45 new rows (`#15446`–`#15490`), from the ScienceDirect Vol 39 editorial board page. The three SED officers are excluded and listed in the gaps file.
- **Journal of Business and Economic Statistics 2018:** 87 new rows (`#15491`–`#15577`), from the JSTOR Vol 36 No 1 front matter. The ASA Committee on Publications is excluded and listed in the gaps file. Editorial coordinator Jamie Hutchens is in staff_rows.
- **Not included:** JRU 2023 (not found).

## Counts
| File | Base | This pack |
|---|---:|---:|
| editors_backfill_scale_ror_panel.csv | 15,446 | 15,578 (+132 new, 20 changed, base key order kept) |
| editor_affiliations.csv | 11,661 | 11,810 (+149 inserted, 3 updated) |
| editors_backfill_scale_gaps.csv | 4,539 | 4,568 (+29) |
| BACKFILL_SCALE_ROR_staff_rows | 222 | 223 |
| inventory | 312 | 312 (RED 2021 and JBES 2018 status rows updated) |

The match-rate rows for RED and JBES were updated. All other support files are byte-identical to the base.

## Mechanical fixes compared with the held pack
1. The held pack wrote 6 files with LF line endings; the base uses CRLF. All of them are CRLF again.
2. The held pack blanked the inventory cell `n/a` for AER: Insights 2018 (an NA-coercion side effect). It is restored.

Apart from fix 2, every value is identical to the held pack.

## QC
- All 83 distinct RORs (142 rows) are active in the ROR API, and the name and country fit each row.
- No invented RORs; blanks stay blank (S19 Adelaide, S20 ECARES).
- No duplicate panel keys, panel–long ROR desync 0, headers identical, 0 emails and 0 phones.
- There are no pilot files in the backfill.

## Publish note for Journal-Editor-Web
Replace `data/editors/core49/releases/editors_backfill_scale_ror_20261031/` with the files in this folder, or add it as a new release folder and point core49 STATUS.md at it. Then update the STATUS.md row counts (panel 15,578; long 11,810) and the coverage gaps: RED 2021 and JBES 2018 are now filled. No site rebuild is needed for the Directory, which does not read core49.
