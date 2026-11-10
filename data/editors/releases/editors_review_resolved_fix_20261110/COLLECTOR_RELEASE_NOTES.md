# editors_review_resolved_fix_20261110

Base: releases/editors_weird_inst_fix_20261110 (= PR #53 Directory, 14,672 Institutions). User-approved via Econ-Journal-Web. Not published.
Script: abs_ajg/scripts/review_resolved_fix_20261110.py (+ data/review_item3_names_20261110.json). Every edit is keyed on editor_row_key (never on notes text).

## Changes
| Item | Institutions (publish) | Publish rows | ft50_current mirror | Pilot rows | Long rows |
|---|---|---|---|---|---|
| 1 row-level splits | 13 | 77 | 17 | 21 | 98 |
| 1 REMATCH | 203 | 281 | 9 | 98 | 376 |
| 1 STRIP | 48 | 49 | 0 | 7 | 15 |
| 1 DROP (Marks) | 18 | 25 | 0 | 11 | 36 |
| 1 RENAME | 18 | 21 | 0 | 5 | 13 |
| 1 SET_COUNTRY | 3 | 4 | 0 | 2 | 6 |
| 2 Zhichen Chen -> Hainan VUST | 1 | 1 | 0 | 0 | 1 |
| 3 rename over-stripped rows | 26 | 65 | 1 | 50 | 100 |
| 3 DROP (degree statement) | 1 | 1 | 0 | 0 | 1 |
| 4 'Tel' scrub damage restored | 8 | 10 | 0 | 6 | 0 |
| 5 wrong ROR -> right panel ROR | 10 | 69 | 8 | 30 | 99 |
| 5 wrong ROR blanked | 7 | 7 | 0 | 2 | 9 |
| e-mail scrub | 373 | 1391 | 624 | 217 | 17 |

Items:
1. Resolved REVIEW decisions (/workspace/institutions_review_resolved_20261110.csv; 49 KEEP untouched) and 84 row-level splits (/workspace/institutions_review_rowlevel_20261110.csv). All target RORs already exist on panel rows. Name-level decisions only touch rows with that Directory display and no other ROR, and never when the row's printed country contradicts the decision. Explicit editor rows: Hyun-Jae Lee US NAS -> Korea NAS 0030qkm60; Daniel D'Angelo NZ ARA ROR -> blank (US name-only twin). York University rows 022jz8688 (York College PA) -> 05fq50484 Toronto. HEC split Paris/Montréal/Lausanne. Seven UGA rows were already on 00te3t702 (weird freeze).
2. Zhichen Chen (IJBPM, ajg1 #1271): canonical 'Hainan Vocational University of Science and Technology', ROR https://ror.org/05a8bts04 (ROR API v2: active, education, Haikou, China; exact display name; aliases 海南科技职业大学/海南科技职业学院), China / Asia.
3. Over-stripped weird DROP rows renamed to the printed organisation (Tokyo Institute of Technology kept separate from Science Tokyo, no ROR). Existing panel ROR reused only for the clearly same org: Lausanne Hotel School -> EHL 02kqs4h17, Lyon 3 -> 05b5c0584, Montreal Polytechnic -> 05f8d4e86, Maastricht -> 02jz4aj89, Newcastle Unversity -> Newcastle University 01kj2bm70, Edinburgh Nappier -> Edinburgh Napier 03zjvnn91, Nottingham University Ningbo -> UNNC 03y4dt428. Newcastle Business School split by printed country (Northumbria UK / University of Newcastle AU). 'PhD in Business Administration from Nanjing University' dropped (degree, not affiliation). Raw never edited.
4. Phone-scrub damage: canonical names restored from raw (Telematic, Tel-Hai, Telecom, Telangana, Telehealth). Root cause is Web's build_site.py LEFTOVER_LABEL_RE/LABELED_PHONE_RE lacking a trailing word boundary; patch attached (WEB_build_site_scrub_word_boundary.patch). It also fixes about 40 Directory display names that only Web can fix (Tel Aviv University shown as 'Aviv University', T-Mobile shown as 'T', Telecom/Telkom/Telfer/Tellus/Di Tella). Collector fixes: scripts/gapfill_wayback.py label rule is now word-bounded; trailing_country_fix_20261110.py gains safe_scrub() for any canonical derived from text.
5. Wrong-ROR audit: George Institute UK 04h0zjx60 (George Washington -> GWU 00y4zzh67; George Bacovia, Fund for American Studies, bare 'George' -> blank ROR), IfM Mannheim 0010cp777 Bonn row -> IfM Bonn 04c7t5k94, and clear contradictions found by a raw-vs-ROR-name scan: NC State on North Central State College -> 04tj63d06; Georgia Tech Scheller on Brook Byers Institute -> 01zkghx44; Catholic University Milan on PUC-SP -> 03h7r5v07; Bologna on Bergamo -> 01111rn36; Lüneburg on Luxembourg -> 02w2y2t16; Imperial on Bonn -> 041kmwe10; Pegaso on Italian University Line -> 03cxwg632; NKUAS on Quemoy -> NKUST 00hfj7g70; College Prep U, University of Africa, Pfizer (x2), Nine Martingale -> blank ROR.
E-mail: addresses removed from raw_affiliation (17), canonical_name (19), source_note (2,206 incl. ft50_current), long raw_aff_part (17); the Directory copy's cleaned value is reused where it exists. The change log never contains an address (logged as '[email removed]'). Three faculty_profile_url values (au.dk person URLs) embed an address and were not touched (URL, not affiliation/notes text). The Dan Swanson address was redacted in WEIRD_INST_changes_20261110.csv (freeze + abs_ajg/reports). It is still present in older frozen release panels/long tables from today (inst_drop_rematch ... weird_inst_fix); those were not rewritten.

## Directory (Web build_site.py on a copy)
- Before: 14,672 Institutions, 6,387 with ROR, 6,387 distinct ROR, 162 countries, 69 shared names
- After:  14,439 Institutions, 6,379 with ROR, 6,379 distinct ROR, 162 countries, 49 shared names
- After + Web scrub patch: 14,440 Institutions, 6,379 with ROR, 162 countries, 49 shared names
- Web guard 'expected 69' must become 49 (the resolved splits collapse shared names). Build run with the guard set to that value on the copy.
- RORs leaving the Directory: Brook Byers Institute 04t9vjc16, York College PA 022jz8688, George Institute UK 04h0zjx60, IfM Mannheim 0010cp777, Applied Research Associates NZ 04gmfhf08, US NAS 038mfx688, Italian University Line 02wgnr390, Seton Hall Prep 04f00y561, Obong University 02crmer26. New: Hainan VUST 05a8bts04.

## Skips (57)
- 12 x item1 REMATCH: row already has a decision from item1-rowlevel (REMATCH); not applied twice
- 7 x item1-rowlevel REMATCH: already on https://ror.org/00te3t702 (applied by editors_weird_inst_fix UGA fix); no change
- 3 x item1 DROP: protected organisation on row (11KBW/UNSW/INSEAD)
- 3 x item1 REMATCH: no row with this display in base freeze
- 2 x item1 REMATCH: target ROR country Switzerland != decision country Singapore
- 2 x item1 REMATCH: target 'Applied Research Associates': exact ROR twin https://ror.org/04gmfhf08 is in New Zealand, row in Unite
- 2 x item1 REMATCH: row country United Kingdom != decision country Argentina
- 2 x item1 -: 1 row(s): row carries a different ROR; not moved
- 2 x item1 -: 2 row(s): row carries a different ROR; not moved
- 2 x item3 RENAME: printed 'Birmingham City University, USA' contradicts the UK university; not renamed
- 2 x item4 RESTORE_TEL: superseded by item1 REMATCH ('Pegaso University')
- 1 x item1 STRIP: no row with this display in base freeze
- 1 x item1 REMATCH: row country Germany != decision country Italy
- 1 x item1 COINFLIP: COINFLIP decision handled by item 2 (Zhichen Chen)
- 1 x item1 REMATCH: no row changed (rows already on target or carry another ROR)
- 1 x item1 REMATCH: row country France != decision country Russia
- 1 x item1 STRIP: row country Germany != decision country France
- 1 x item1 STRIP: row country Portugal != decision country Switzerland
- 1 x item1 -: 4 row(s): row carries a different ROR; not moved
- 1 x item1 -: 19 row(s): row carries a different ROR; not moved
- 1 x item1 -: 12 row(s): row carries a different ROR; not moved
- 1 x item1 -: 5 row(s): row carries a different ROR; not moved
- 1 x item1 -: 262 row(s): row carries a different ROR; not moved
- 1 x item1 -: 7 row(s): row carries a different ROR; not moved
- 1 x item1 -: 20 row(s): row carries a different ROR; not moved
- 1 x item3 RENAME: printed country Germany != ROR country The Netherlands
- 1 x item3 RENAME: canonical is already 'T-Mobile'; the Directory shows 'T' only because Web's phone scrub eats 'Mobile' (item 4 
- 1 x item4 RESTORE_TEL: superseded by item1 RENAME ('University of Ain Témouchent')
- 1 x item4 RESTORE_TEL: superseded by item1 RENAME ('IUL Telematic University')

## QC
verify ok=True: row counts unchanged (AJG1 12,326 incl. 10 nav untouched, AJG2 5,462, long 269,539); no header/EOL changes; no invented ROR (one new real ROR 05a8bts04, API-verified); raw_affiliation changed only by Marks DROP (traced) or e-mail removal; no new panel<->long desync (full-table desync 2085 -> 2019, all pre-existing); no e-mail left in panel affiliation/notes fields or long table; no near-miss merges; non-Latin names kept; 11KBW, UNSW, INSEAD FR 00ghzk478 / SG 05ynf4333 intact; working panels identical. Pilots changed consistently but are not in the publish set.
