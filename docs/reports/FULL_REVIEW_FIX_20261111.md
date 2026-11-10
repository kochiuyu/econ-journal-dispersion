# Full Institutions review — editors_full_review_fix_20261111 + editors_full_review_resolved_fix_20261111

Published 2026-11-11 (Asia/Taipei). The two Collector freezes are applied in order on top of `editors_raw_leak_fix_20261110` (main `c57a7a6`, PR #53).

## Why

A full review of the built Institutions list (14,192 names) found spelling variants of the same organisation, strings that are not an institution (roles, bios, topics, places), names with the wrong country, and shared names that mean more than one campus. The user approved the send file, the resolved hold file and the row-level coin-flip splits.

## What changed

The Directory took each freeze's directory diff, keyed on `file` + `editor_row_key`, with 0 old-value mismatches and 0 missing keys. `ror_notes` carries the Collector's trace (758 rows; for DROP rows it keeps the printed text).

| Freeze | Cells | Applied |
|---|---:|---|
| `editors_full_review_fix_20261111` | 21,335 | MERGE 2,395, DROP 600, RENAME 231, SET_COUNTRY 214 Institutions; Paauwe fix |
| `editors_full_review_resolved_fix_20261111` | 5,085 | resolved holds: SET_COUNTRY 559, MERGE 97, DROP 7, RENAME 5; 213 row-level splits |

Rules:
- **DROP** follows the Marks mechanism. `canonical_name`, `raw_affiliation` and `ror_id` are blanked, the printed text is kept in `ror_notes`, and the country stays.
- **MERGE, RENAME and SET_COUNTRY** never edit the printed raw.
- **Splits** give each editor of a shared name (e.g. University of Illinois, Northeastern, University of Newcastle, UNC, University of Texas, IIM, UMass, Rome, Concordia, Los Andes, VNU, Maryland, China University of Petroleum, Max Planck Institute) their own campus ROR. Editors who could not be placed keep the printed name.
- **New ROR ids:** 8, all checked on the ROR API v2. Examples: `010zh7098` Saint Mary's University (Halifax), `023ahcz89` MPI for Comparative and International Private Law, `04k83g518` Concordia University Wisconsin. No ROR id is invented.
- **Jaap Paauwe:** A* #2545 has name `Jaap Paauwe` and raw `Tilburg, Netherlands`. On FT50 #3821 (both files), `editor_name_raw` is blank. All three rows are Tilburg University `04b8v1s79`, Netherlands. The A* seat now merges with its FT50 copy, so appointments go from 162,576 to 162,575.

Rows changed:
- **ABDC:** A* 1,081, A 2,554, B 2,331, C 1,938.
- **AJG gap:** prio43 160, ajg2 407, ajg1 812.
- **FT50:** ROR file 382, slim file 345.

The long table keeps its 181,449 rows. It is the Collector's table restricted to the published keys, with the earlier web e-mail-scrub note kept on B #13. Each freeze folder gets its own `editor_affiliations.csv.gz` (gzip -9 -n).

## Directory

| | Live (main) | After freeze 1 | After freeze 2 (this PR) | Collector |
|---|---:|---:|---:|---:|
| Institutions | 14,192 | 11,426 | 11,330 | 11,330 |
| with ROR (= distinct ROR) | 6,386 | 6,387 | 6,396 | 6,396 |
| Countries | 162 | 161 | 167 | 167 |
| Shared display names | 49 | 45 | 46 | 46 |
| Appointments without an institution | 12,658 | | 13,404 | |

`scripts/build_site.py`: the shared-name guard is now 46 (was 49).

## Checks

- **Scrub:** the site data has 0 e-mail addresses and 0 phone patterns. Changed cells and pinned files have none either.
- **Protected names:** 11KBW, UNSW Sydney, INSEAD (France / Singapore / UAE), 1 Decembrie 1918 University and Bank of England are intact.
- **Near-miss pairs:** Bolton/Boston, IIT/Indiana, Queen's Belfast/Canada, Tokyo Tech/Science Tokyo, Petru Maior/Palade and Aachen clinic/RWTH stay separate.
- **Row counts:** ajg1 12,316, ajg2 5,462, FT50 10,047; no pilots published; CITATION.cff untouched.

## Still open (Collector decisions)

- 77 MERGE rows already on a different campus ROR: ESCP Berlin/Paris, UWI, Palermo, Amity, CEIBS / Xi'an Jiaotong.
- 45 DROP rows whose printed raw names a real organisation; candidates for RENAME.
- 3 ROR ids that 404 (Mercer `028zh6278`, CTU Prague `03jbxjb94`, CY Cergy `047t3d518`) are left blank. The Wisconsin Extended Campus system ROR was refused.
- 4 Cyrillic names are kept as printed.
- 245 coin-flip Institutions are still on hold; the 207 two-place rows and the ambiguous acronyms stay as printed.
