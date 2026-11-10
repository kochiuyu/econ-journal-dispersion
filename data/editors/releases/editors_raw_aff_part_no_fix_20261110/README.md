# editors_raw_aff_part_no_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Long-table-only fix on the published Directory copy of `editors_edpacs_marks_country_fix_20261110` (PR #51), which it supersedes. Collector pack: `/workspace/econ-journal-editors/releases/editors_raw_aff_part_no_fix_20261110`.

`raw_aff_part` values that were exactly `no` (an `affiliation_imputed` flag leaked into the text column on seats whose panel `raw_affiliation` is blank) are set to blank, keyed by `editor_row_key` + `panel_file`. No panel CSV changes, no ROR changes, no site filter, and `*_with_profile_pilot.csv` is not published.

- Collector change log: 13,703 rows = 9,705 publish-set + 3,998 profile-pilot (pilot rows not applied).
- Applied: **9,695** long-table rows. The other 10 publish-set keys are not in the Directory copy on purpose: 9 ajg1 navigation/chrome rows (#10668, #10749, #10998, #11210, #11280, #11354, #12013, #12254, #12255) and the REStud institution-as-name row `editors_ft50_current_with_ror#578` (Universitat Pompeu Fabra).
- Per panel: A* 112, A 2,668, B 2,237, C 1,564, FT50 slim 104, FT50 with_ror 99, prio43 358, ajg2 236, ajg1 2,317.
- `raw_aff_part == 'no'`: 9,695 before → 0 after. Every keyed seat has a blank panel `raw_affiliation`.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,493,840 bytes; 63,385,575 bytes uncompressed, md5 `8e8427521162d8f0408eb9341e6d19df`). 181,443 rows, same 20-column schema, starts from the #51 table; exactly 9,695 lines differ.

## Files

- `editor_affiliations.csv.gz` — long table
- `RAW_AFF_PART_NO_changes_20261110.csv` — collector change log (13,703 rows, incl. pilot rows not applied)
- `COLLECTOR_RELEASE_NOTES.md` — collector freeze notes
- `README.md` — this file
