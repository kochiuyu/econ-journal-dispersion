# editors_tokyo_gatech_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Keyed panel-only fix on the published Directory copy of `editors_inst_punct_split_20261110` (PR #47). It supersedes the `editors_inst_punct_split_20261110` current panels. The collector pack is at `/workspace/econ-journal-editors/releases/editors_tokyo_gatech_fix_20261110`. There is no site filter, `*_with_profile_pilot.csv` is not published, and no ROR id was invented.

## What changes

Only the 28 changelog keys were written (affiliation fields only); the collector panels were not overlaid. Row counts are unchanged on every panel.

| Change | Published panel rows |
|---|---:|
| REMATCH_TOKYO → The University of Tokyo `https://ror.org/057zh3y96` | 27 (25 with the FT50 pair collapsed) |
| REMATCH_GATECH → Georgia Institute of Technology `https://ror.org/01zkghx44` (`editors_abdc_a_star_current#22331`, Soumen Ghosh, Decision Sciences) | 1 |

By panel: FT50 slim 2, FT50 with_ror 2, A* 5 (4 Tokyo + Georgia Tech), A 5, B 5, C 3, prio43 1, ajg2 2, ajg1 3.

The 27 Tokyo rows break down as follows:
- 22 rows had `canonical_name` `University of Tokyo` and a blank ROR.
- 2 rows are the matching slim FT50 rows (Weese, Kojima). The slim file has no `canonical_name`.
- 3 rows have a printed University of Tokyo text with the bare `canonical_name` `Tokyo` and a blank ROR: Yuiko Fujita "Tokyo University, Japan", Takamasa Iryo "Tokyo University", and Michael Keen "Tokyo College, University of Tokyo, Tokyo, Japan".

None of those rows was already correct on the Directory copy.

**Printed text.** `raw_affiliation` on every touched row is the Directory printed text, byte-identical to before. No published panel cell or long-table part contains `Italian Cultural Institute`.

**Notes.** The Directory guardrail note `directory_guardrail_restore_20261101: …` stays in `ror_notes`, and the collector fix token (`tokyo_gatech_fix_20261110: REMATCH_TOKYO|REMATCH_GATECH: …`) is appended. The collector's own `ror_notes` text, which drops the guardrail note, was not copied.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,493,224 bytes; 63,400,174 bytes uncompressed, md5 `8ce651a307d63c4d914fc96fd95f59a7`). 181,443 rows, same 20-column schema, started from the published #47 long table; the 28 parts for the touched keys are updated and panel ↔ long sync is checked.

## Not fixed here

`ITALIAN_CULTURAL_INSTITUTE_other_rows_20261110.csv` (in the collector pack) lists 35 other seats (A* 1, A 7, B 13, C 14). The collector copies of those seats say `Italian Cultural Institute`. On the Directory copy they keep the printed text, for example Tokyo Institute of Technology, Tokyo University of Science, or Tokyo Metropolitan University, along with the guardrail note. Their `canonical_name` is the bare `Tokyo` and their ROR is blank, so the Directory lists them as `Tokyo` and Institutions shows one unmatched `Tokyo` (Japan) row with 35 appointments.

## Files

- `editor_affiliations.csv.gz` — long table
- `TOKYO_GATECH_changes_20261110.csv` — collector row-level change log (28 rows)
- `COLLECTOR_RELEASE_NOTES.md` — collector freeze notes
- `README.md` — this file
