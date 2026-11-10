# Review-resolved fix — editors_review_resolved_fix_20261110

Published 2026-11-10 (Asia/Taipei). Supersedes `editors_weird_inst_fix_20261110` (stacked on PR #53).

## What changed

Keyed, user-approved fix from the Collector (every edit keyed on `editor_row_key`):

| Item | Institutions | Publish rows (Collector) |
|---|---:|---:|
| Row-level splits (Northeastern, American, Concordia, Los Andes, Trinity, HEC, IAE, York, ...) | 13 | 77 |
| REVIEW REMATCH / STRIP / DROP (Marks) / RENAME / SET_COUNTRY | 203 / 48 / 18 / 18 / 3 | 281 / 49 / 25 / 21 / 4 |
| Zhichen Chen → Hainan Vocational University of Science and Technology `05a8bts04` (new ROR, API-verified) | 1 | 1 |
| Over-stripped names restored (Sydney Law School, Tokyo Institute of Technology, T-Mobile, ...) + 1 degree-statement DROP | 26 + 1 | 65 + 1 |
| 'Tel' scrub damage restored in canonical names | 8 | 10 |
| Wrong ROR → right panel ROR / blanked (George Washington `00y4zzh67`, IfM Bonn `04c7t5k94`, ...) | 10 / 7 | 69 / 7 |
| E-mail addresses removed from text cells | 373 | 1,391 |

Applied here: 645 publish-panel rows differ from the previous Directory copy (A* 79, A 120, B 131, C 155, prio43 9, ajg2 23, ajg1 56, FT50 ROR file 37, FT50 slim 35) and 539 long rows. 2,022 logged cells (mostly e-mail removals in `source_note` and `raw_aff_part`) already equalled the freeze value in the Directory copy, which had removed those addresses earlier. Every other logged cell matched its `old` value (0 mismatches). Every changed panel row equals the Collector freeze row, except `ajg1 #4771`, where only the unlogged `ror_notes` history differs (the Directory copy keeps an older note prefix). Pilot panels are not published.

Web additions:

- **E-mail found and removed:** ABDC B `#13` (Sriparna Ghosh) carried a malformed e-mail address, written with a comma instead of a dot, in `raw_affiliation`, `canonical_name` and the long `raw_aff_part`. It was removed, with a trace kept in `ror_notes` / `ror_match_note`. The site never showed it, because the row displays its ROR name. It is still present in the older pinned long tables of earlier freezes, which were not rewritten.
- **`scripts/build_site.py`:**
  - Applied the Collector's `WEB_build_site_scrub_word_boundary.patch`: the phone and e-mail label regexes now need a word boundary.
  - Lowered the shared-name guard from 69 to 49.

## Directory

| | Before (#53 head 50d1f05) | After | Collector |
|---|---:|---:|---:|
| Institutions | 14,672 | 14,440 | 14,440 with the patch (14,439 without) |
| with ROR (= distinct ROR) | 6,387 | 6,379 | 6,379 |
| Countries | 162 | 162 | 162 |
| Appointments without an institution | 12,460 | 12,487 | |
| Shared display names | 69 | 49 | 49 |
| Appointments / editors / journals | 162,575 / 112,718 / 2,853 | 162,576 / 112,719 / 2,853 | |

## Checks

- **Spot checks:**
  - Zhichen Chen shows Hainan Vocational University of Science and Technology, `05a8bts04`, China.
  - Tokyo Institute of Technology (15 appointments, no ROR) is separate from Institute of Science Tokyo (8).
  - Sydney Law School (14) and T-Mobile are named in full.
  - Tel Aviv University (156) and Telkom University are intact. The Pegaso rows are all on `03cxwg632`, shown as Pegaso University, and the damaged "ematic" Institution is gone.
  - George Washington University has 318 rows on `00y4zzh67`; the George Institute UK ROR `04h0zjx60` has 0 rows.
  - IfM Bonn has 2 rows on `04c7t5k94`; IfM Mannheim `0010cp777` has 0.
  - York University has 503 rows on `05fq50484`; York College PA `022jz8688` has 0.
- **Scrub:**
  - Real e-mails and phones are still removed: labelled, international and NANP numbers, and addresses.
  - The site data has 0 e-mail addresses and 0 phone patterns.
  - No damaged name fragments remain ("Aviv University", "T", "ematic", "ecommunications").
- **Protected names and near-miss pairs:**
  - 11KBW, UNSW Sydney (665), INSEAD France / Singapore / UAE and 1 Decembrie 1918 University stay distinct.
  - Bolton/Boston, IIT/Indiana, Queen's Belfast/Canada, Tokyo Tech/Science Tokyo, Petru Maior/Palade and Aachen/RWTH are not merged.
- **Row counts:** unchanged (ajg1 12,316 and ajg2 5,462 published; FT50 10,047). The long table has 181,443 rows and 20 columns.
- **Contact data:** the pinned folder contains no e-mail addresses.
- **Untouched files:** CITATION.cff and core49 are untouched. `scripts/build_site.py` changed only as described above.
