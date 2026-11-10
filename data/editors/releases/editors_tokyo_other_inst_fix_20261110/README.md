# editors_tokyo_other_inst_fix_20261110 — published (Directory copy, 2026-11-10)

**Publish note (2026-11-10, Asia/Taipei).** Keyed panel-only fix on the published Directory copy of `editors_tokyo_gatech_fix_20261110` (PR #48). It supersedes those current panels. The collector pack is at `/workspace/econ-journal-editors/releases/editors_tokyo_other_inst_fix_20261110`. There is no site filter and `*_with_profile_pilot.csv` is not published. Only ABDC panels change; FT50 and AJG-gap files are unchanged.

## What changes

These are the 35 seats whose Directory `canonical_name` was the bare `Tokyo` with a blank ROR (A* 1, A 7, B 13, C 14). The collector's copies of them had been rewritten to `Italian Cultural Institute`, and the Directory guardrail had restored the printed text. Only the 35 changelog keys were written, and only institution fields. Row counts are unchanged.

| Printed institution | ROR | On published panels before? | Rows |
|---|---|---|---:|
| Tokyo Institute of Technology | blank (not mapped to Institute of Science Tokyo `05dqf9946`) | — | 11 |
| Tokyo University of Science | `05sj3n476` | yes (7 rows, same name) | 7 |
| Tokyo Metropolitan University | `00ws30h19` | no (pilot only); ROR API verified | 3 |
| Tokyo University of Agriculture and Technology | `00qg0kr10` | yes (1 row, same name) | 3 |
| Tokyo International University | `01g9ekh39` | yes (2 rows, same name) | 3 |
| Tokyo University of Marine Science and Technology | `048nxq511` | no (pilot only); ROR API verified | 2 |
| Tokyo Keizai University | `03b0ym704` | no (pilot only); ROR API verified | 2 |
| Tokyo Gakugei University | `00khh5r84` | no (pilot only); ROR API verified | 1 |
| Tokyo Women's Medical University | `03kjjhe36` | no; ROR API verified | 1 |
| Tokyo University of Foreign Studies | `027tyzk91` | no; ROR API verified | 1 |
| Fuhito Kojima, Theoretical Economics, printed `Tokyo` | blank; `canonical_name` blank | — | 1 |

ROR API check (api.ror.org v2, 2026-11-10): all six ids not previously on the published panels resolve, are `active`, have exactly the stated `ror_display` name, and are located in Japan.

The changes kept the Directory's existing values in three places:
- **Printed text.** `raw_affiliation` is byte-identical to the Directory printed text on all 35 rows.
- **Notes.** The Directory guardrail note stays in `ror_notes`, with the `tokyo_other_inst_fix_20261110:` token appended.
- **Country.** On the 12 blank-ROR seats, the collector freeze clears `ror_country` / `continent`. The Directory keeps `Japan` / `Asia` there (the printed text is in Tokyo), as it does on other blank-ROR seats.

No institution field in the published panels or long table contains `Italian Cultural Institute`.

## Long table

`editor_affiliations.csv.gz` (gzip -9 -n, 7,493,938 bytes; 63,402,388 bytes uncompressed, md5 `34a817edc388e206f44d51510ff1c983`). 181,443 rows, same 20-column schema, started from the published #48 long table; the 35 parts for the touched keys are updated and panel ↔ long ROR sync is checked.

## Files

- `editor_affiliations.csv.gz` — long table
- `TOKYO_OTHER_INST_changes_20261110.csv` — collector row-level change log (35 rows: 21 REMATCH_BASE, 2 REMATCH_NEW_TO_PANELS, 12 RESTORE_RAW_ROR_BLANK; `old_*` columns are the collector's pre-fix values, not the Directory's)
- `COLLECTOR_RELEASE_NOTES.md` — collector freeze notes
- `README.md` — this file
