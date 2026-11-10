# editors_full_review_fix_20261111
Base: releases/editors_raw_leak_fix_20261110. Input: /workspace/institutions_full_review_send_20261111.csv (3,517 Institutions; MERGE 2,437 / DROP 627 / RENAME 233 / SET_COUNTRY 220). Hold file not applied. Keyed on editor_row_key.

Applied (Institutions with >=1 row changed): MERGE 2,395; DROP 600; RENAME 231; SET_COUNTRY 214. Publish rows: MERGE 3,924, DROP 751, RENAME 238, SET_COUNTRY 3,518 (+322 ft50_current mirror rows).
Not applied (172 skip lines, FULL_REVIEW_skipped_20261111.csv):
- 77 MERGE rows already on a different campus ROR (ESCP Berlin vs Paris; UWI St Augustine vs Mona; Palermo Argentina vs Italy; Amity Dubai vs India; CEIBS FT50 with_ror twin prints Xi'an Jiaotong) - kept
- 45 DROP rows whose printed raw names a real organisation (e.g. 'Kiel Institute ...; Kiel University; Sciences Po') - not blanked; candidates for RENAME
- 4 Cyrillic names kept as printed (no translation); 4 protected UNSW rows; Concordia U., CA and Universidad del Pacifico, Engineering (targets are hold-file coin-flips)
- 44 no-op Institutions (already at target)
Rules: DROP = Marks style (canonical/raw/ROR blanked, printed text kept in ror_notes / long ror_match_note, country kept). MERGE/RENAME/SET_COUNTRY never edit raw. SET_COUNTRY: for non-academic multi-office firms the office country in the printed text wins over HQ.
Paauwe: A* #2545 'Jaap Paauwe, Tilburg' / canonical 'Netherlands' -> 'Jaap Paauwe', raw 'Tilburg, Netherlands' (user-approved, Wayback board), Tilburg University 04b8v1s79, Netherlands; FT50 #3821 (both files) name kept 'Jaap Paauwe', editor_name_raw blank, 04b8v1s79, country 'The Netherlands' -> 'Netherlands'.
No new RORs (all send RORs already in panels). Pilots byte-identical; the au.dk e-mail still in editors_abdc_a_current_with_profile_pilot#15779 (Helena Skyt Nielsen) faculty_profile_url is left as-is (pilot untouched) - not a change.
Directory (Web build on copy): 14,192 / 6,386 / 6,386 / 162 / 49 -> 11,426 / 6,387 / 6,387 / 161 / 45. Countries -1 = spelling variants (Brasil, US, SWITZERLAND, INDIA) folded; +Turks and Caicos Islands.
