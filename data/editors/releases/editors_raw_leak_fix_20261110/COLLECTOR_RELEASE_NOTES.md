# editors_raw_leak_fix_20261110
Base: releases/editors_raw_drift_fix_20261110. Keyed on editor_row_key.

## Leak scan (166 rows from RAW_DRIFT_leak_scan_20261110.csv)
- 161 rows: raw_affiliation (+ the matching long raw_aff_part) set back to the original printed text.
  - 117 are raw-only restores: 111 same-organisation rows plus 6 wrong-organisation rows whose institution was already correct.
  - 44 are raw restores plus an institution fix: 38 wrong-organisation rows plus 6 reclassified (5 Nottingham Trent→University of Nottingham Ningbo China 03y4dt428; prio43#1334 →University of Newcastle Australia 00eae9z71).
- 5 rows skipped: African Affairs prio43 #3079/#3084/#3085/#3086/#3092. Their pre-rewrite value came from a faculty search, not the printed board.
- New ROR: Universitas Galuh 03m7qjm52 (verified via ROR API). Every other ROR was already in the panel.
- Source verification is in RAW_LEAK_source_verification_20261110.csv: 47 verified live, 33 verified on Wayback, 10 name found but the text differs, 76 unverified online.
- One email scrubbed on restore (abdc_a#16537). It is logged as '[email removed]'.

## Steering
- S1, Qiang Meng A*#18960: the live INFORMS board still prints NUS. Only a ror_notes line was added.
- S2: email-bearing faculty_profile_url blanked on abdc_a#15895 and abdc_a_star#13053. The long table has no such column.
  - The pilot abdc_a_with_profile_pilot#15779 still has the same URL. Pilots are kept byte-identical, so this needs a decision.
- S3, FT50 #3821 Paauwe: no change. The page prints 'Jaap Paauwe' with ', Tilburg, Netherlands' as the affiliation.

## Directory (Web build on a copy)
- Before: 14,176 / 6,384 / 6,384 / 162 / 49.
- After: 14,192 / 6,386 / 6,386 / 162 / 49.
- Directory diff: RAW_LEAK_directory_diff_20261110.csv (341 field rows).
