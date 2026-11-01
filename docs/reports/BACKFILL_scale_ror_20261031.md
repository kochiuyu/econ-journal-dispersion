# BACKFILL scale — ROR harmonization (2026-10-31 data, input-fixed parse 2026-11-01; rebuilt 2026-11-01 Asia/Taipei, UTC+8)

**Status: HELD.** Nothing published, pushed, or handed to Web. Output: `releases/editors_backfill_scale_ror_20261031/`. Input: `releases/editors_backfill_scale_20261101/` (input-fixed parse release, 15,446 rows; unchanged; md5 baseline `reports/backfill_scale_work/ror2/baseline2_md5_releases.txt` — all 1,219 files of every other release — verified before and after). Code and intermediate pickles: `reports/backfill_scale_work/ror2/` (s0_donor → s5_build → s6_check → s7_write → s8_qa; overrides in `s5_splits.py`). Progress log: `reports/backfill_scale_work/PROGRESS.md`.

## 2026-11-01 rebuild: source change and user decisions
This pack was rebuilt in place (still HELD, never published) on the input-fixed parse release `releases/editors_backfill_scale_20261101` (report `reports/BACKFILL_scale_parse_20261101.md`) instead of `editors_backfill_scale_20261031`.

**Row-count change: 15,436 → 15,446 panel rows (+10).** The 10 added rows are inserted in journal/year order (new positions #6713–#8739), so **8,723 later rows shift position and get a new `editor_row_key`**; the crosswalk `editors_backfill_scale_row_key_crosswalk.csv` maps old → new `editor_row_key` (15,416 unchanged, 20 row_fixed, 10 row_added). Long table stays 11,661 parts (bleed text split off before is now fixed in the input; the added rows add parts). Rate: 96.94% (11,015/11,363) → **96.83% (11,013/11,373)**.

Rows changed versus the previous build (15,384 rows identical):

| change | rows | effect |
|---|---|---|
| System records with no campus printed blanked (University of Nebraska 0238rvs44 ×7, University of Alaska 01mtkd993 ×4, University of Hawaii 03tzaeb71 ×1) | 12 | matched → unmatched (`curated_block`, note names the old record) |
| Korea University (bare) kept blank; wrong Tokyo record 05m1gnk07 not applied | 20 | `ror_notes` wording only (already blank) |
| American, Western, ENS, Heidelberg (bare) — kept blank, proposed ids not applied | 0 | already blank; `BACKFILL_SCALE_ROR_unmatched_strings_*` text updated |
| 11 post15-blanked strings kept blank; 22 system_no_campus strings kept blank (no campus in print, city or profile domain) | 0 | already blank; category/proposed_handling text updated |
| ESSEC: France 02dga6j42 unless Singapore printed | 0 | all 21 rows already France (none print Singapore) |
| CEU stays 02zx40v98 | 0 | 5 rows, unchanged (1 prints Budapest, Hungary — country conflict kept by decision) |
| Parse fix: Michigan rows (text) | 6 | text only, ROR unchanged |
| Parse fix: de Mesquita rows | 4 | unmatched → University of Chicago 024mw5h28 |
| Parse fix: split-override rows lose bleed text (Iowa State 4, Oxford 2, Imperial 2, FRB St. Louis 2) | 10 | ROR unchanged; `affiliation_count` changes 222 → 212 |
| Parse fix: rows added | +10 | X L ×4 → Fudan 013q1eq08; R. Dieci ×2 → Bologna 01111rn36; R. Boucekkine ×4 → unmatched (Aix-Marseille, post15 blank kept) |

Matched arithmetic: 11,015 − 12 + 4 + 6 = 11,013.
Header changes versus the previous build: none in any existing file; one new file (the crosswalk).

## Method
1. **Donors (s0):** consistency2 (latest ROR pack panels) and the backfill pilot ROR pack, keyed by normalized string and by (name, string); plus the strings deliberately blanked in ror_fix_post15 (kept blank here). Donors are used for cross-checking and for the prior tie-break only; never applied blind.
2. **Parsing (multiaff convention):** each `raw_affiliation` split into printed parts in print order (semicolon, ' and '/'&' before a capital with protected phrases, comma-ror). 22 + 2 additional strings that print two institutions in one part were split by an explicit, asserted override (`and_split_override`); 10 rows where the PDF text layer merged the next editor's entry into the row (JEDC: J. Bhattacharya ×4, R. DiCecio ×2; JDE: C.M. Woodruff ×2, S. Zhang ×2) were split (`bleed_split_override`, 20 long rows; the bled text kept as part 2 with a blank ROR).
3. **Resolver:** strict pilot resolver against ROR v2.15 (active records only): exact name/label (high), exact alias / curated short form / campus text / research-institute record (medium), misprints with a `LOW:` note (low). Unique within the printed country; country must agree.
4. **Panel ror** = first matched non-former part (`ror_id_aff_rank`); other matched parts in `other_ror_ids`; all parts in `editor_affiliations.csv`.
5. **Staff** (role_class=staff, 222 rows): no ROR unless the row is clearly the editor's university (8 Data Editor rows); excluded from all metrics.
6. **Fixes from review (all systematic, all re-run end-to-end):**
   - input bleed: another editor's text (R Boucekkine/AMSE, R. Dieci/Bologna, X L/Fudan) sat inside 10 rows → split; the editor's own institution (Iowa State, St Louis Fed, Oxford, Imperial) is the panel ror, bled text blank.
   - unsplit two-institution parts (e.g. "Ohio State University and Tel Aviv University", "LUISS University, UPF, EIEF and Barcelona GSE") → split into parts; 24 strings.
   - segment step ignored the printed country: "University of the Andes, Colombia" had the Venezuelan record (WRONG) → Universidad de Los Andes 02mhbdp94; "NYU, Abu Dhabi, UAE/United Arab Emirates" had NYU (US) → NYU Abu Dhabi 00e5k0821 (campus printed); "CEPR, Montreal" → blank (country conflict).
   - consistency2 prior tie-breaks that picked a foreign namesake (earlier-pack errors): American University → Universidad Americana (Nicaragua), Western University → Cambodia, Ecole normale supérieure → ENS d'Abidjan, Heidelberg University → Heidelberg (Ohio), Korea University → Korea University (Tokyo). No country printed → **blank** (`ambiguous_name`) with the likely record proposed for approval. Northwestern / Georgia / Newcastle / Queen's tie-breaks were checked and kept (US/US/UK/Canada; pilot used the same rule).
   - "Faculty of Public Health & Policy … London School of Hygiene & Tropical Medicine" matched 01zqv1s26 "Faculty of Public Health" (the UK professional body; WRONG) → LSHTM 00a0jsq62.

## Rates
- **Overall (non-staff): 11,013 matched of 11,373 rows with an affiliation = 96.83%** (15,224 rows; 3,851 no affiliation; 360 unmatched). Previous build: 11,015/11,363 = 96.94%.
- **By confidence:** high 8,704 (79.0% of matched) · medium 2,244 · low 65.
- All rows: matched 11,021 · unmatched 360 · no_affiliation 4,017 · staff_excluded 48.
- Unmatched rows by reason (`ror_match_method`): curated_block 190 (system names, incl. the 12 blanked system-record rows) · no_exact_match 100 · post15_blank_kept 35 · ambiguous_name 20 · inactive_blank 10 · country_conflict 5.
- **Wayback-offset rows:** +0: 1,717 rows, 97.65% · +1: 432, 97.29% · −1: 489, 96.71% · all non-zero offsets 921 rows, 96.98% — no degradation from the offset captures.

### Per journal (non-staff)
| journal | rows (non-staff) | with affiliation | matched | high | medium | low | unmatched | no affiliation | match rate | staff rows |
|---|---|---|---|---|---|---|---|---|---|---|
| AEJ: Applied Economics | 256 | 45 | 45 | 36 | 9 | 0 | 0 | 211 | 100.0% | 19 |
| AEJ: Economic Policy | 310 | 49 | 49 | 31 | 18 | 0 | 0 | 261 | 100.0% | 19 |
| AEJ: Macroeconomics | 139 | 29 | 26 | 21 | 5 | 0 | 3 | 110 | 89.7% | 18 |
| AEJ: Microeconomics | 171 | 29 | 29 | 29 | 0 | 0 | 0 | 142 | 100.0% | 20 |
| AER | 609 | 0 | 0 | 0 | 0 | 0 | 0 | 609 | n/a (names only) | 19 |
| AER: Insights | 154 | 0 | 0 | 0 | 0 | 0 | 0 | 154 | n/a (names only) | 9 |
| American Journal of Agricultural Economics | 297 | 297 | 269 | 208 | 60 | 1 | 28 | 0 | 90.6% | 0 |
| Econometric Theory | 490 | 490 | 464 | 383 | 81 | 0 | 26 | 0 | 94.7% | 0 |
| The Economic Journal | 390 | 390 | 380 | 307 | 73 | 0 | 10 | 0 | 97.4% | 13 |
| Economic Theory | 692 | 684 | 679 | 595 | 80 | 4 | 5 | 8 | 99.3% | 0 |
| Energy Economics | 317 | 317 | 309 | 242 | 67 | 0 | 8 | 0 | 97.5% | 0 |
| European Economic Review | 648 | 648 | 631 | 508 | 118 | 5 | 17 | 0 | 97.4% | 0 |
| Experimental Economics | 470 | 470 | 466 | 340 | 123 | 3 | 4 | 0 | 99.2% | 1 |
| Games and Economic Behavior | 262 | 262 | 254 | 201 | 53 | 0 | 8 | 0 | 97.0% | 4 |
| Health Economics | 391 | 383 | 380 | 217 | 163 | 0 | 3 | 8 | 99.2% | 8 |
| Journal of Applied Econometrics | 550 | 550 | 535 | 372 | 160 | 3 | 15 | 0 | 97.3% | 19 |
| Journal of Business and Economic Statistics | 432 | 344 | 320 | 262 | 58 | 0 | 24 | 88 | 93.0% | 4 |
| Journal of Development Economics | 646 | 640 | 639 | 499 | 140 | 0 | 1 | 6 | 99.8% | 0 |
| Journal of Econometrics | 568 | 485 | 480 | 408 | 72 | 0 | 5 | 83 | 99.0% | 6 |
| Journal of Economic Behavior and Organization | 662 | 595 | 566 | 412 | 131 | 23 | 29 | 67 | 95.1% | 1 |
| Journal of Economic Dynamics and Control | 573 | 569 | 555 | 449 | 102 | 4 | 14 | 4 | 97.5% | 0 |
| Journal of Economic Growth | 281 | 281 | 273 | 217 | 56 | 0 | 8 | 0 | 97.2% | 0 |
| Journal of Economic Literature | 239 | 16 | 16 | 16 | 0 | 0 | 0 | 223 | 100.0% | 17 |
| Journal of Environmental Economics and Management | 564 | 564 | 494 | 441 | 52 | 1 | 70 | 0 | 87.6% | 0 |
| Journal of the European Economic Association | 589 | 60 | 60 | 34 | 26 | 0 | 0 | 529 | 100.0% | 2 |
| Journal of Financial Econometrics | 447 | 447 | 425 | 335 | 84 | 6 | 22 | 0 | 95.1% | 8 |
| Journal of Health Economics | 363 | 363 | 356 | 281 | 75 | 0 | 7 | 0 | 98.1% | 0 |
| Journal of International Economics | 540 | 540 | 538 | 416 | 120 | 2 | 2 | 0 | 99.6% | 0 |
| Journal of Labor Economics | 195 | 0 | 0 | 0 | 0 | 0 | 0 | 195 | n/a (names only) | 0 |
| Journal of Law and Economics | 55 | 0 | 0 | 0 | 0 | 0 | 0 | 55 | n/a (names only) | 0 |
| Journal of Monetary Economics | 451 | 424 | 414 | 370 | 44 | 0 | 10 | 27 | 97.6% | 0 |
| Journal of Money, Credit and Banking | 638 | 126 | 126 | 126 | 0 | 0 | 0 | 512 | 100.0% | 0 |
| Journal of Political Economy | 238 | 0 | 0 | 0 | 0 | 0 | 0 | 238 | n/a (names only) | 0 |
| Journal of Risk and Uncertainty | 271 | 271 | 260 | 192 | 68 | 0 | 11 | 0 | 95.9% | 7 |
| Journal of Urban Economics | 355 | 355 | 354 | 268 | 86 | 0 | 1 | 0 | 99.7% | 4 |
| Quarterly Journal of Economics | 275 | 0 | 0 | 0 | 0 | 0 | 0 | 275 | n/a (names only) | 8 |
| RAND Journal of Economics | 282 | 282 | 260 | 198 | 49 | 13 | 22 | 0 | 92.2% | 8 |
| Review of Economic Dynamics | 107 | 107 | 107 | 70 | 37 | 0 | 0 | 0 | 100.0% | 0 |
| Review of Economics and Statistics | 307 | 261 | 254 | 220 | 34 | 0 | 7 | 46 | 97.3% | 8 |
| **all (non-staff)** | 15224 | 11373 | 11013 | 8704 | 2244 | 65 | 360 | 3851 | **96.83%** | 222 |

Lowest rates: JEEM 87.6% (University of Maryland/California system strings; Nebraska system record now blank), AEJ: Macro 89.7% (3 rows), AJAE 90.6% (Nebraska/Alaska system records now blank), RAND 92.2%, JBES 93.0%.

## Unmatched strings (91 printed parts, 379 non-staff long rows; `BACKFILL_SCALE_ROR_unmatched_strings_20261031.csv`)
By category (strings / rows): system_no_campus 22/196 · post15_blanked_earlier 11/40 · place_only 25/32 · no_ror_record 7/28 · ambiguous_name 5/24 · inactive_record 3/15 · system_record_blanked 3/12 · country_conflict 5/11 · not_an_institution 1/7 · ambiguous 2/5 · joint_unit 1/2 · typo 1/2 · title_only 2/2 · ambiguous_campus 1/1 · building_name 1/1 · other 1/1.

| printed part | long rows | category | handling |
|---|---|---|---|
| University of Maryland | 47 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: University System of Maryland 01r0c1p88 / UMD College Park 047s2c258) |
| University of California | 37 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: UC system) |
| University of Wisconsin | 20 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: UW system / UW–Madison 01y2jtd41) |
| University of Illinois | 17 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: U of I system / UIUC 047426m28) |
| University of North Carolina | 14 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: UNC system / UNC Chapel Hill 0130frc33) |
| China Center for Health Economic Research (CCHER), Beijing, China | 8 | no_ror_record | keep blank: CCHER has no own ROR record (it is a Peking University centre, but PKU is not printed; rule 3) |
| Aix-Marseille Economic Sciences, Marseille, France | 8 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: 02ek9wp67 Aix-Marseille Sciences Economiques (blanked in ror_fix_post15) |
| University of Colorado | 8 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: CU system / CU Boulder 02ttsq026) |
| American University | 8 | ambiguous_name | USER DECISION 2026-11-01: keep blank; not applied: 052w4zt36 American University (United States) (namesakes in other countries; no country printed; earlier-pack tie-break was wrong, corrected in edito |
| University of Nebraska | 7 | system_record_blanked | USER DECISION 2026-11-01: keep blank (system record, no campus printed or evidenced) |
| Los Alamos, NM, USA | 7 | place_only | keep blank: place name only (Los Alamos National Laboratory 01e41cf67 is plausible but not printed) |
| University of Texas, USA | 7 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: UT system / UT Austin 00hj54h04) |
| Independent Researcher | 7 | not_an_institution | keep blank |
| Korea University | 6 | ambiguous_name | USER DECISION 2026-11-01: keep blank; not applied: 047dqcg40 Korea University (South Korea) (namesakes in other countries; no country printed; earlier-pack tie-break was wrong, corrected in editors_ro |
| University of Adelaide, Adelaide, SA, Australia | 6 | inactive_record | USER DECISION: ROR v2.15 marks 00892tw58 inactive, successor 028g18b61 (Adelaide University); apply successor or keep blank |
| University of Texas | 6 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: UT system / UT Austin 00hj54h04) |
| Toulouse 1 University Capitole, Toulouse, France | 6 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: 027ankh97 Université Toulouse Capitole (string was deliberately blanked in ror_fix_post15; kept blank) |
| University of Cergy-Pontoise, FRANCE | 5 | inactive_record | USER DECISION: 03vs46t66 Université de Cergy-Pontoise is inactive; successor CY Cergy Paris Université 043htjv09 |
| Microsoft Research, Herzelia, Israel | 5 | no_ror_record | keep blank: no Microsoft Research (Israel) record in ROR v2.15 (UK/India/Asia/US/Canada only) |
| Gerzensee, Switzerland | 5 | no_ror_record | keep blank: Study Center Gerzensee has no ROR record (place name only printed) |
| University of California, 1997–2000 | 5 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: UC system) |
| Yale School of Public Health, New Haven, Connecticut, USA | 5 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: 03v76x132 Yale University (school-level text; deliberately blanked in ror_fix_post15) |
| CEPR, Montreal, Quebec, Canada | 4 | country_conflict | USER DECISION: CEPR 04jzmdh37 (UK network record) vs printed Montreal, Canada; kept blank under rule 1 — approve 04jzmdh37 (CEPR is a network; fellows sit anywhere) or keep blank |
| Catholic University College Leuven, Leuven, Belgium | 4 | ambiguous | keep blank: not KU Leuven by name; only match candidate is the inactive Catholic University College of Bruges–Ostend; user may confirm KU Leuven 05f950310 |
| Western University | 4 | ambiguous_name | USER DECISION 2026-11-01: keep blank; not applied: 02grkyz14 Western University (Canada) (namesakes in other countries; no country printed; earlier-pack tie-break was wrong, corrected in editors_ror_c |
| Universita della Svizzera | 4 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: 03c4atk17 Università della Svizzera italiana (truncated print; blanked in ror_fix_post15) |
| European U. Institute | 4 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: 0031wrj91 European University Institute (blanked in ror_fix_post15) |
| Pontificia Universidade Catolica | 4 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: PUC-Rio / PUC-SP / PUC-RS etc.) |
| University of Adelaide, Adelaide, Australia | 4 | inactive_record | USER DECISION: as above (00892tw58 inactive -> successor 028g18b61) |
| University Paris | 4 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: several Paris universities) |
| University of Massachusetts | 4 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: UMass system 0260j1g46 / UMass Amherst 0072zz521) |
| University of Alaska | 4 | system_record_blanked | USER DECISION 2026-11-01: keep blank (system record, no campus printed or evidenced) |
| University of Toulouse, France | 4 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: Université Toulouse Capitole 027ankh97 / Toulouse School of Economics 00ff5f522 / former federal Universi |
| Christian-Albrechts-University of Kiel, Germany | 4 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: 04v76ef78 Kiel University (blanked in ror_fix_post15) |
| Ecole normale supérieure | 4 | ambiguous_name | USER DECISION 2026-11-01: keep blank; not applied: 05a0dhs15 École Normale Supérieure - PSL (France) (namesakes in other countries; no country printed; earlier-pack tie-break was wrong, corrected in e |
| University of Maryland, USA | 3 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: University System of Maryland 01r0c1p88 / UMD College Park 047s2c258) |
| George Mason University, UK | 3 | country_conflict | keep blank: printed country UK conflicts with George Mason University 02jqj7156 (US); likely print error — user may approve |
| Microsoft Research, Israel | 3 | no_ror_record | keep blank: no Microsoft Research (Israel) record in ROR v2.15 |
| Erasmus School of Economics | 3 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: 057w15z03 Erasmus University Rotterdam (school-level string blanked in ror_fix_post15; sub-part of a split two-institution string) |
| Department of Public Health, Danish Centre for Health Economics (DaCHE), Denmark | 3 | no_ror_record | keep blank: DaCHE has no own ROR record; parent (University of Southern Denmark) not printed (rule 3) |
| Gerzensee Switzerland | 3 | no_ror_record | keep blank: as above |
| University of Maryland, United States | 3 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: University System of Maryland 01r0c1p88 / UMD College Park 047s2c258) |
| Maryland | 3 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: state/system name) |
| University of Toulouse | 3 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: Université Toulouse Capitole 027ankh97 / Toulouse School of Economics 00ff5f522 / former federal Universi |
| INRA-AgroParisTech | 2 | joint_unit | USER DECISION: joint INRAE / AgroParisTech 02kbmgc12 unit; no record for the joint unit; could take AgroParisTech (medium) |
| WZB, Berlin, Germany | 2 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: 03k0z2z93 WZB Berlin Social Science Center (blanked in ror_fix_post15) |
| Thessaloniki, Greece | 2 | place_only | keep blank: place name only (sub-part of 'Thessaloniki, Greece & Erasmus University, Rotterdam, The Netherlands', split at '&'; the Erasmus sub-part is matched) |
| University of Notre Dame, Paris, France | 2 | country_conflict | keep blank: Notre Dame (US) Paris global centre; ROR has no French record; user may approve 00mkhxb43 |
| University of Wisconsin, 2012–2013 | 2 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: UW system / UW–Madison 01y2jtd41) |
| Heidelberg University | 2 | ambiguous_name | USER DECISION 2026-11-01: keep blank; not applied: 038t36y30 Heidelberg University (Germany) (namesakes in other countries; no country printed; earlier-pack tie-break was wrong, corrected in editors_r |
| (), Yale School of Public Health, New Haven, Connecticut, USA | 2 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: as above |
| Department of Economics, Virginia University, Charlottesville, VA 22904, USA | 2 | typo | PROPOSE low: University of Virginia 0153tk833 (Charlottesville 22904 printed; 'Virginia University' is a misprint) — user approval |
| Toulouse University | 2 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: same as 'University of Toulouse') |
| University of Arkansas | 1 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: UA system 05vvhh982 / flagship Fayetteville) |
| Imperial College London, USA | 1 | country_conflict | keep blank: printed USA conflicts with Imperial College London 041kmwe10 (UK); print error likely — user may approve |
| University of Colorado, USA | 1 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: CU system / CU Boulder 02ttsq026) |
| China University of Petroleum | 1 | ambiguous_campus | keep blank: Beijing vs East China (Qingdao) branch not printed; earlier-pack donor 02em1tr51 is WRONG (Univ. of Petroleum, Indonesia) |
| Max Plank Institute (MPI) of Economics, Jenna, Germany | 1 | no_ror_record | keep blank: Max Planck Institute of Economics (Jena, closed 2014) has no ROR record in v2.15 |
| ENSAI, France | 1 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: 00k206f19 ENSAI (blanked in ror_fix_post15) |
| Villa La Fonte, Italy | 1 | building_name | keep blank: EUI building (Villa La Fonte); user may approve European University Institute 0031wrj91 |
| University of Sydney, USA | 1 | country_conflict | keep blank: printed USA conflicts with University of Sydney 0384j8v12 (AU); user may approve |
| University of Maryland, Maryland, USA | 1 | other | keep blank |
| Madison | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Blacksburg | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Munich | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Koln | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Mason | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Aix-Marseille | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Haifa | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Graz | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Hamburg | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Hanover | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Senior Economist Department for Innovation and Competition, France | 1 | title_only | keep blank: job title + department, no institution |
| Dusseldorf | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Penn | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Tennessee | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Mainz | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Zurich | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| University Amsterdam | 1 | ambiguous | keep blank: University of Amsterdam vs Vrije Universiteit Amsterdam |
| Associate Professor of Economics | 1 | title_only | keep blank |
| Bielefeld | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Magdeburg | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Brasilia | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| University of Hawaii | 1 | system_record_blanked | USER DECISION 2026-11-01: keep blank (system record, no campus printed or evidenced) |
| Free University Amsterdam, Amsterdam, The Netherlands | 1 | post15_blanked_earlier | USER DECISION 2026-11-01: keep blank; not applied: 008xxew50 Vrije Universiteit Amsterdam (blanked in ror_fix_post15) |
| Arizona | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Minnesota | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Michigan | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Florida | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| British Columbia | 1 | place_only | keep blank: bare place/state name (often a list-style affiliation like 'Madison'); no inference from other years (rule 6) |
| Unviersity of Maryland | 1 | system_no_campus | USER DECISION 2026-11-01: keep blank (campus not printed or evidenced; candidates not applied: typo of 'University of Maryland' (system)) |

## Audit (`BACKFILL_SCALE_ROR_spotcheck_20261031.csv`, 370 matched non-staff rows, seed 20261031)
- Strata: every low row (65), per method (105), per journal (99), every split_override row (71), multi-affiliation (20), non-zero Wayback offset (10).
- Check: ROR name/alias (or parent name for a unit) found in the printed part and printed country = ror.org country; the rest read by hand.
- Result: ok 295 · ok_low 60 (misprint interpretations, kept low and flagged) · ok_manual 15 (hand-checked variants: UT Dallas/Austin with comma, Bocconi, City University London → City St George's, Carlos III Getafe campus, Ca' Foscari, "Timbergen", Tilburg School, Emory College, Paris 1, Waikato) · **ERROR 0** after fixes. The first audit run showed 4 "errors" that were a Netherlands/The Netherlands normalization bug in the check itself (fixed).
- Systematic errors found by the audit + sanity scans and fixed before release: see Method §6 (bleed, unsplit parts, country ignored in segment step, wrong prior tie-breaks, Faculty of Public Health).

## Sanity checks
- Inactive ROR records in output: **0** (Adelaide 00892tw58 ×2 strings and Cergy-Pontoise 03vs46t66 left blank with successor notes).
- Parent/campus: 7 long-table parts in a ROR parent/child relation to the panel ror (kept; both printed). No system → campus move without printed campus.
- System records in output: **0**. University of Nebraska System 0238rvs44 (7 rows), University of Alaska System 01mtkd993 (4), University of Hawaii System 03tzaeb71 (1) were blanked (user decision 2026-11-01: no campus printed or evidenced).
- Country: broad scan of every matched part for any printed country ≠ ror.org country → only CEU (approved exception) plus false positives (Georgia State, "New Mexico", "New South Wales").
- `source`, `source_note` and all other source columns: byte-identical (verified column by column; only `ror_match_status` and 212 `affiliation_count` values differ).

## Rule-8 cross-check vs consistency2 + pilot (`BACKFILL_SCALE_ROR_crosscheck_20261031.csv`)
Panel rows whose string is in a donor: agree 7,901 · ours blank, donor has id 213 · both blank 56 · hierarchy 15 · distinct 30. 49 non-agreeing strings, each noted; none overridden silently:
- ours blank by rule (system names, post15 blanks, inactive, ambiguous): Maryland/California/Wisconsin/Illinois/North Carolina/Colorado/Texas/Massachusetts/Toulouse — the donors pick a campus or the system without printed evidence.
- **Donor wrong (earlier-pack errors; consistency2 itself is not modified — fixed in the new HELD pack `editors_ror_consistency3_20261101`):** China University of Petroleum → 02em1tr51 University of Petroleum (Indonesia) in consistency2 (abdc_a_current, abs_ajg_gap_prio43_current); Korea University → Tokyo; American University → Nicaragua; Western University → Cambodia; Heidelberg University → Ohio.
- distinct: 4 multi-affiliation strings where the donor took another printed part (both kept here); **ESSEC Business School** (12 rows): ours = main record 02dga6j42 (France, alias), donor = 04be2h179 ESSEC Asia-Pacific (Singapore, display name) — campus not printed (user decision).
- hierarchy: Queen Mary (ours QMUL, donor University of London), NYU Abu Dhabi string variant, University of Hawaii (ours now blank — system record blanked; donor Mānoa).

## Open issues
1. ECARES → ULB and CORE → UCLouvain stay **low** (no own records). Cowles Foundation has its own record here (rule 3) while the pilot donor uses Yale.
2. Bleed text is removed in the input-fixed source; the 10 former bleed rows now carry only the editor's own institution.
3. Input fixes: done in the new parse release `editors_backfill_scale_20261101` (rows added for R. Boucekkine, R. Dieci, X. L.; de Mesquita leak removed); this pack is now built from it.
4. "University Paris Sud - ADIS, Institut Universitaire de France [and CEPII]" (8 rows) → Institut Universitaire de France 055khg266 via the segment step (IUF is printed; Paris-Sud is inactive → Paris-Saclay). Kept; flagged.
5. `former_flag` = 0 on all rows: no printed part carries a former/retired word; past editors remain labelled by `is_former`/`role_class=past` (383 rows).
6. `editor_row_key` prefix `editors_backfill_scale_panel#…` kept as in the source.

## User decisions (2026-11-01) — applied
1. System records Nebraska/Alaska/Hawaii: **blanked** (12 rows).
2. System strings without campus (22 strings): **kept blank**; proposed campuses not applied (no campus in print, city or profile domain).
3. post15-blanked strings (11) and the 5 ambiguous bare names (American, Western, ENS, Heidelberg, Korea): **kept blank**; proposed ids not applied.
4. ESSEC: France 02dga6j42 unless Singapore printed (no row prints Singapore). CEU stays 02zx40v98 (confirmed).

## Still open (left as built)
- "Virginia University, Charlottesville" → UVA 0153tk833 (blank now).
- INRA-AgroParisTech → AgroParisTech 02kbmgc12 or blank (blank now).
- Inactive Adelaide 00892tw58 → successor 028g18b61; Cergy-Pontoise 03vs46t66 → 043htjv09 (blank now).
- Country conflicts (blank now): CEPR Montreal, George Mason "UK", Imperial "USA", Sydney "USA", Notre Dame Paris; CEU Budapest kept on 02zx40v98.
- ECARES/CORE low; Cowles own record vs Yale; IUF/Paris-Sud; NORC centre; Northwestern tie-break.
