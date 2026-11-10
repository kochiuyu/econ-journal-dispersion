# editors_open_items_fix_20261111

Published 2026-11-11 (Asia/Taipei). This supersedes `editors_post_fullreview_fix_20261111` (PR #55) for the Directory current panels. It is a keyed, user-approved Collector freeze built from the open-items recommendations, taken through its `OPEN_ITEMS_directory_diff_20261111.csv` (keyed on `editor_row_key`; 306 cells, 0 missing keys, 0 old-value mismatches). It retargets bio and multi-organisation strings to the employer printed or looked up (e.g. Judge Business School & King's College to the University of Cambridge `013meh722`, Asia School of Management to Asia School of Business `037hqgd69`); applies the near-duplicate merges (RSM one way, FLACSO México `02wdjwg88`, HEC Liège, Assumption, CESS, Rutgers `05vt9qd57`, UW–Madison for one row); fixes country conflicts (Niagara `05309tf52` with country Canada, Emden/Leer, West Ukrainian NU, Southwestern UFE `04ewct822`); maps Creative New Zealand to Creative Capital Foundation `021e5n641`, St. Catharine's to Brock `056am2717`, and two undropped rows to Dalhousie and Nova Southeastern; and corrects the re-check finds (Guangxi University, QianFoShan Hospital, Lego (Denmark) `04vx9dd09`, CIMMYT Mexico `03gvhpa76`, Macao University of Tourism `00nx0vn86`, and the Indecon, Rutgers–New Brunswick and CINVESTAV countries). The CEIBS `faculty_profile_url` and `faculty_person_key` are cleared on FT50 #4634. 33 RORs were API-verified, 8 of them new to the panels. Holds (Pacífico, Naples, Concordia, UT System) and the 199 coin-flips stay as printed. No pilot files are published or changed. No raw edits. No emails or phones.

Rows changed: prio43 1, ajg2 3, ajg1 7. `ror_id` 2,627 / 4,936 / 9,206 (was 2,627 / 4,933 / 9,201). Row counts unchanged (ajg1 12,316, ajg2 5,462).

**Directory.** Institutions 11,185 (was 11,213), 6,697 with a ROR id (was 6,692; distinct 6,697). Countries 169 (unchanged). 13,413 appointments have no institution (unchanged). Shared display names 43 (was 44; CIMMYT Mexico joins the CIMMYT HQ ROR; the build guard is now 43). Appointments 162,575, editors 112,719, journals 2,853 (unchanged).

Long table and change logs: `data/editors/releases/editors_open_items_fix_20261111/` (`editor_affiliations.csv.gz`, 181,449 rows; 64 parts changed). Report: `docs/reports/OPEN_ITEMS_FIX_20261111.md`.

## Previous freeze: editors_post_fullreview_fix_20261111

Published 2026-11-11 (Asia/Taipei). This supersedes `editors_full_review_resolved_fix_20261111` (PR #54) for the Directory current panels. It is a keyed, user-approved Collector freeze, taken through its `POST_FULLREVIEW_directory_diff_20261111.csv` (keyed on `editor_row_key`; 4,593 cells, 0 missing keys, 0 old-value mismatches), plus `ror_notes` carried from the freeze on 9 rows. It applies the post-full-review residuals: WRONG_ROR 5/5 (inactive ROR records moved to their active successors: UniSA and Adelaide to Adelaide University `028g18b61`, TEI Piraeus to University of West Attica `00r2r5k05`, UPMC to Sorbonne Université `02en5vm52`, Rennes 1 to Université de Rennes `015m7wh34`), NEAR_DUPLICATE 101/138, MISSING_ROR 298/306 (269 new API-verified RORs), WRONG_COUNTRY 7 in full and 5 partly, NON_INSTITUTION 18/51 and MISSING_COUNTRY 11. It also applies the answers: 38 RENAMEs; Mercer, CTU Prague and CY Cergy; and FT50 slim #4634 set to its printed `Xi'an Jiaotong University, China` (`017zhmm22`). No pilot files are published or changed. No emails or phones.

Rows changed: prio43 22, ajg2 41, ajg1 114; `ror_id` 2,627 / 4,933 / 9,201 (was 2,610 / 4,898 / 9,113). Row counts unchanged (ajg1 12,316, ajg2 5,462).

**Directory.** Institutions 11,213 (was 11,330), 6,692 with a ROR id (was 6,396; distinct 6,692). Countries 169 (was 167; Guam and New Caledonia added). 13,413 appointments have no institution (was 13,404). Shared display names 44 (was 46; the build guard is now 44). Appointments 162,575, editors 112,719, journals 2,853 (unchanged).

Long table and change logs: `data/editors/releases/editors_post_fullreview_fix_20261111/` (`editor_affiliations.csv.gz`, 181,449 rows; 1,081 parts changed). Report: `docs/reports/POST_FULLREVIEW_FIX_20261111.md`.

## Previous freeze: editors_full_review_resolved_fix_20261111

Published 2026-11-11 (Asia/Taipei). This supersedes `editors_full_review_fix_20261111`, which supersedes `editors_raw_leak_fix_20261110`, for the Directory current panels. Both are keyed, user-approved Collector freezes taken through their directory diffs (keyed on `editor_row_key`; 21,335 + 5,085 cells, 0 old-value mismatches). `editors_full_review_fix_20261111` applies the full Institutions review send file (Institutions applied: MERGE 2,395, DROP 600, RENAME 231, SET_COUNTRY 214). DROP follows the Marks mechanism: name, raw and ROR blanked, printed text kept in `ror_notes`, country kept. It also fixes Jaap Paauwe (A* #2545 name `Jaap Paauwe`, raw `Tilburg, Netherlands`; FT50 #3821 `editor_name_raw` blank; both Tilburg University `04b8v1s79`, Netherlands). `editors_full_review_resolved_fix_20261111` applies 675 resolved held Institutions (SET_COUNTRY 559, MERGE 97, DROP 7, RENAME 5) and 213 row-level shared-name splits (e.g. University of Illinois → UIUC / UIC, Northeastern → Boston / Shenyang, University of Newcastle → UK / Australia), with 8 new ROR ids checked on the ROR API. Skipped by the Collector and still open: 77 MERGE rows already on a different campus ROR, 45 DROP rows that print a real organisation, 3 ROR ids that 404 (Mercer, CTU Prague, CY Cergy) and the Wisconsin Extended Campus system ROR.

Rows changed (both freezes): prio43 160, ajg2 407, ajg1 812; `ror_id` prio43 2,610 (was 2,553), ajg2 4,898 (was 4,777), ajg1 9,113 (was 8,750). Row counts unchanged (prio43 3,104, ajg2 5,462, ajg1 12,316).

**Directory.** Institutions 11,330 (was 14,192; 11,426 after the first freeze), 6,396 with a ROR id (was 6,386; distinct 6,396). Countries 167 (was 162). 13,404 appointments have no institution (was 12,658). Shared display names 46 (was 49; the build guard is now 46). Appointments 162,575 (was 162,576: the Paauwe A* seat now merges with its FT50 copy), editors 112,719, journals 2,853.

Long tables and change logs: `data/editors/releases/editors_full_review_fix_20261111/` and `data/editors/releases/editors_full_review_resolved_fix_20261111/`. Report: `docs/reports/FULL_REVIEW_FIX_20261111.md`.

## Previous freeze: editors_full_review_fix_20261111

Published 2026-11-11 (Asia/Taipei) in the same Directory PR, under `editors_full_review_resolved_fix_20261111`. Directory after it alone: Institutions 11,426, 6,387 with a ROR id, countries 161, shared display names 45.

## Previous freeze: editors_raw_leak_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_raw_drift_fix_20261110` for the Directory current panels (stacked on Directory PR #53). It is a keyed, user-approved fix on top of `editors_raw_drift_fix_20261110` (PR #53) for the Collector's leak scan: 161 rows where a 2026-10-28/29 `institution_*` script had written a canonical or ROR name into `raw_affiliation` get the original printed text back (341 cells from `RAW_LEAK_directory_diff_20261110.csv`). 117 are raw-only restores (111 same-organisation, e.g. `The University of Osaka` → printed `Osaka University`; 6 wrong-organisation rows whose institution was already right). 44 also fix the institution: the 17 Pakistan rows that showed `National Institute of Oceanography` (e.g. COMSATS University Islamabad `00nqqvk19`, IoBM Karachi `048w4c951`), the `AM Publications` rows (SAGE Publishing `05534qc24` / SAGE UK, or blanked where only a role was printed), the Japan rows that showed `Temple University` (Waseda `00ntfnx83`, Otaru, Hiroshima Shudo `05n757p35`), `Beijing University, China` → Peking University `02v51f717` on ajg2 #2222 (B #33518 stays Beihang, editor-confirmed), Galuh University → Universitas Galuh `03m7qjm52` (new ROR, ROR API-verified), 5 Nottingham Trent → University of Nottingham Ningbo China and prio43 #1334 → University of Newcastle Australia. 5 African Affairs prio43 rows are skipped. Qiang Meng (A* #18960, Transportation Science) stays NUS as the INFORMS board prints it, with a note that he moved to HKUST (Guangzhou) on 2026-08-28. The long table gets the matching `raw_aff_part` / ROR parts and the 6 long rows for the Top 5 seats FT50 #10046–#10048 (both FT50 files), so it has 181,449 rows. Institutions 14,192 (was 14,176), 6,386 with a ROR id (was 6,384; distinct 6,386). Countries 162 (unchanged). 12,658 appointments have no institution (unchanged). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Rows changed: prio43 3, ajg2 6, ajg1 13 rows; `ror_id` prio43 2,553, ajg2 4,777, ajg1 8,750 (all unchanged). Row counts unchanged (prio43 3,104, ajg2 5,462, ajg1 12,316).

**Directory.** Institutions 14,192 (was 14,176), 6,386 with a ROR id (was 6,384; distinct 6,386). Countries 162 (unchanged). 12,658 appointments have no institution (unchanged). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Long table and change log: `data/editors/releases/editors_raw_leak_fix_20261110/`. Report: `docs/reports/RAW_LEAK_FIX_20261110.md`.

## Previous freeze: editors_raw_drift_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_post_review_fix_20261110` for the Directory current panels (stacked on Directory PR #53). It is a keyed, user-approved fix on top of `editors_post_review_fix_20261110` (PR #53) that closes the raw-text drift between the Directory and the Collector source panels (comparison `raw_drift_20261110.csv`): the 21 rows whose printed text had been rewritten to `National Law University` keep their printed text and get the real ROR and country instead of the leftover India (e.g. University of Lyon → `01rk35k63`, The University of Law → `00bge3r76`, Plovdiv University → `0545p3742`, Politehnica București → `0558j5q12`); 11 HKUST (Guangzhou) rows are on `050h0vm43` / China (including C #27613, which was on the HKUST Hong Kong ROR); Kagoshima University `03ss88z23` replaces Nihon University; MIT replaces Ikon Science; Gradient (United States) `014qf4206` replaces Korea Telecom; ENSAI `00k206f19` and Springer Nature (Shanghai, China) `01f9pza55` are matched; FT50 #2955 (Tiffany Trzebiatowski) gets `Colorado State University` (`03k1gpj17`) in both FT50 files instead of a blank / bio; and AJG1 #10149 (Lawrence Sweet) takes the live-source text `IZZI Inc`. The three Top 5 seats (#10046–#10048) were already in the Directory copy and are not duplicated; the two Pompeu Fabra institution-as-name rows and the AJG1 navigation rows stay out. New ROR ids were checked on the ROR API; none is invented. Institutions 14,176 (was 14,195), 6,384 with a ROR id (was 6,379; distinct 6,384). Countries 162 (unchanged). 12,658 appointments have no institution (was 12,659). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Rows changed: prio43 2, ajg2 1, ajg1 1 rows; `ror_id` prio43 2,553 (was 2,551), ajg2 4,777 (was 4,776), ajg1 8,750 (unchanged). Row counts unchanged (prio43 3,104, ajg2 5,462, ajg1 12,316).

**Directory.** Institutions 14,176 (was 14,195), 6,384 with a ROR id (was 6,379; distinct 6,384). Countries 162 (unchanged). 12,658 appointments have no institution (was 12,659). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Long table and change log: `data/editors/releases/editors_raw_drift_fix_20261110/`. Report: `docs/reports/RAW_DRIFT_FIX_20261110.md`.

## Previous freeze: editors_post_review_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_review_resolved_fix_20261110` for the Directory current panels (stacked on Directory PR #53). It is a keyed, user-approved clean-up on top of `editors_review_resolved_fix_20261110` (PR #53), from the post-review Institution audit (399 names): trailing city / state / country cut or dropped (63 renamed, 74 dropped); role prefixes cut or dropped (22 / 49); department prefixes mapped to the parent organisation (30); near-duplicates merged (25 name merges, 10 ROR merges, 2 drops); fragments (punctuation, credential, address, place, contact) renamed or dropped (10 / 17); 3 long bios resolved; wrong RORs fixed (three STIE rows blanked off Universitas Patria Artha; CUNY rows → `00453a208`; Abt → `0502afh35`; IIESS → `033xgn512`, Argentina, the one new ROR, verified on ror.org; St Petersburg University → `023znxa73`; Inria → `02kvxyf05`); and contact text removed (e-mail addresses, including comma-malformed ones, and phone numbers; 2 ABDC B `editor_name` cells that held only a phone number are now blank). DROP follows the Marks mechanism (printed text kept in `ror_notes` / `ror_match_note`). The audit's 34 shared-name KEEP rows are untouched; no ROR id is invented. Institutions 14,195 (was 14,440), 6,379 with a ROR id (unchanged; distinct 6,379). Countries 162 (unchanged). 12,659 appointments have no institution (was 12,487). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Rows changed: prio43 1, ajg2 16, ajg1 17 rows; `ror_id` prio43 2,551 (was 2,550), ajg2 4,776 (was 4,770), ajg1 8,750 (was 8,745). Row counts unchanged (prio43 3,104, ajg2 5,462, ajg1 12,316).

**Directory.** Institutions 14,195 (was 14,440), 6,379 with a ROR id (unchanged; distinct 6,379). Countries 162 (unchanged). 12,659 appointments have no institution (was 12,487). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Long table and change log: `data/editors/releases/editors_post_review_fix_20261110/`. Report: `docs/reports/POST_REVIEW_FIX_20261110.md`.

## Previous freeze: editors_review_resolved_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_weird_inst_fix_20261110` for the Directory current panels (stacked on Directory PR #53). It is a keyed, user-approved fix on top of `editors_weird_inst_fix_20261110` (PR #53): the resolved REVIEW Institutions (REMATCH 203, STRIP 48, DROP 18 by the Marks mechanism, RENAME 18, SET_COUNTRY 3; the 49 KEEP names untouched) and 84 row-level splits (Northeastern, American, Concordia, Los Andes and Trinity College editor-confirmed rows; HEC split Paris / Montréal / Lausanne; IAE Aix / Poitiers; York University rows on York College PA `022jz8688` → Toronto `05fq50484`); Zhichen Chen (IJBPM) → Hainan Vocational University of Science and Technology `05a8bts04` (China; the one new ROR, verified on ror.org); 26 over-stripped names restored from the printed text (e.g. `Sydney Law School`, `Tokyo Institute of Technology` kept separate from Institute of Science Tokyo, `T-Mobile`); 'Tel' scrub damage restored in canonical names (Telematic, Tel-Hai, Telecom); wrong-ROR fixes (George Washington → `00y4zzh67`, off the George Institute UK ROR; IfM Bonn row → `04c7t5k94`; NC State, Georgia Tech Scheller, Catholic University Milan, Bologna, Lüneburg, Imperial, Pegaso, NKUST; a few contradicted RORs blanked); and e-mail addresses removed from text cells. Printed `raw_affiliation` changes only on DROP rows (traced) or e-mail removal. `scripts/build_site.py`: the phone/e-mail scrub labels now need a word boundary (Collector patch), so `Tel Aviv University`, `T-Mobile`, `Telkom University` and the Telematic names display in full, and the shared-name guard is 49. The long table, change log and skip list are in `data/editors/releases/editors_review_resolved_fix_20261110/`. Report: `docs/reports/REVIEW_RESOLVED_FIX_20261110.md`.

Rows changed: prio43 9, ajg2 23, ajg1 56 rows; `ror_id` 2,550 / 4,770 / 8,745 (was 2,547 / 4,750 / 8,708). Row counts unchanged (ajg1 12,316, ajg2 5,462, navigation rows out).

**Directory.** Institutions 14,440 (was 14,672), 6,379 with a ROR id (was 6,387; distinct 6,379). Countries 162 (unchanged). 12,487 appointments have no institution (was 12,460). Shared display names 49 (was 69). Appointments 162,576, editors 112,719, journals 2,853.

## Previous freeze: editors_weird_inst_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_country_misprint_fix_20261110` for the Directory current panels (stacked on Directory PR #53). It is a keyed, user-approved clean-up of weird Institution names on top of `editors_country_misprint_fix_20261110` (PR #53), from the non-REVIEW rows of the Institution audit: DROP 178 Institutions (391 publish rows; place-only, generic-role and credential names such as `Maryland`, `Independent Researcher, Vermont`, `Associate Professor`) plus 5 country-only fallbacks (`Greece and UK`, `Italy & UK`, `Finland and Tanzania`, `SE, UK`, the Solicitor string); STRIP 594 (632 rows; role prefixes, addresses, postcodes, URLs, punctuation and trailing state codes cut, e.g. `Harvard Business School, Cambridge, MA` → `Harvard Business School`); SET_COUNTRY 122 (137 rows, from a trailing state or code); REMATCH 186 (249 rows, to an existing panel twin ROR); and the University of Georgia fix (US rows on the Tbilisi ROR `02bjhwk41` → `00te3t702` / United States). DROP follows the Marks mechanism: `canonical_name`, `raw_affiliation` and `ror_id` are blanked, the printed text is kept in `ror_notes` (long table: `raw_aff_part` blanked, trace in `ror_match_note`); country stays. 120 rows whose printed raw still names an organisation (e.g. `Sydney Law School`, `Tokyo Institute of Technology`) are not dropped and are listed for a later restore. The audit's REVIEW names are untouched; no ROR id is invented. The long table, change log and skip list are in `data/editors/releases/editors_weird_inst_fix_20261110/`. Report: `docs/reports/WEIRD_INST_FIX_20261110.md`.

Rows changed: prio43 22, ajg2 54, ajg1 81 rows; `ror_id` 2,547 / 4,750 / 8,708 (was 2,546 / 4,746 / 8,700). Row counts unchanged (ajg1 12,316, ajg2 5,462, navigation rows out).

**Directory.** Institutions 14,672 (was 15,160), 6,387 with a ROR id (unchanged). Countries 162 (unchanged). 12,460 appointments have no institution (was 12,068). Shared display names stay 69. Appointments 162,575, editors 112,718, journals 2,853.

## Previous freeze: editors_country_misprint_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_trailing_country_fix_20261110` (Directory PR #53) for the Directory current panels. It is a keyed, user-approved fix on top of `editors_trailing_country_fix_20261110` (PR #53): 30 publish rows get the real country for 27 Institutions whose printed country was wrong (e.g. ESADE Business School → Spain, TU Berlin → Germany, Queens University Belfast → United Kingdom); Imperial College of London (C #17649) is rematched to the existing panel ROR `041kmwe10` Imperial College London. 11 fragment rows (the 11 held back in PR #53) get a clean `canonical_name` or a blank one: the Court of Appeal / Supreme Court rows become `Court of Appeal of England and Wales` / `Supreme Court of the United Kingdom` (UK), the two Independent Scholar rows become `Independent Scholar`, and `Greece and`, `Italy &`, `Finland and`, `SE` and the Solicitor row are blanked, so the Directory falls back to the printed text (e.g. `Greece and UK`). `University of the North, Barranquilla, .` loses its trailing `, .` and merges with its twin. The printed `raw_affiliation` is unchanged; no ROR id is invented. The long table, change log and skip list are in `data/editors/releases/editors_country_misprint_fix_20261110/`. Report: `docs/reports/COUNTRY_MISPRINT_FIX_20261110.md`.

Rows changed: prio43 1, ajg1 2 rows; ajg2 unchanged; `ror_id` unchanged.

**Directory.** Institutions 15,160 (was 15,166), 6,387 with a ROR id (unchanged). Countries 162 (unchanged). 12,068 appointments have no institution (unchanged). Appointments 162,575, editors 112,718, journals 2,853. Shared display names stay 69.

## Previous freeze: editors_trailing_country_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_raw_aff_part_no_fix_20261110` (Directory PR #52) for the Directory current panels. It is a keyed, user-approved fix for Institution names that ended in a printed country. 6,036 publish-panel rows get the country stripped from `canonical_name` and `ror_country` / `continent` set from it (137 Institutions are rematched to an existing panel twin, reusing that twin's ROR id where it has one; no ROR id is invented). The printed `raw_affiliation` is unchanged. The audit's REVIEW and KEEP names are untouched, and 11 rows whose stripped name would end in a dangling `and` / `&` (e.g. `Court of Appeal of England and`) are held back. No site filter. The long table, change log and skip list are in `data/editors/releases/editors_trailing_country_fix_20261110/`. Report: `docs/reports/TRAILING_COUNTRY_FIX_20261110.md`.

Rows changed: prio43 52, ajg2 198, ajg1 842. The navigation rows stay out.

**Directory.** Institutions 15,166 (was 15,434), 6,387 with a ROR id (unchanged). Countries 162 (was 159: Guinea, Haiti, Timor-Leste). 12,068 appointments have no institution (was 12,067: a printed `…, Haiti` row now falls to the country-only filter). Appointments 162,575, editors 112,718, journals 2,853. Shared display names stay 69.

## Previous freeze: editors_raw_aff_part_no_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_edpacs_marks_country_fix_20261110` (Directory PR #51) for the Directory current panels. It is a long-table-only fix: `raw_aff_part` `no` → blank on 9,695 parts of `data/editors/releases/editors_raw_aff_part_no_fix_20261110/editor_affiliations.csv.gz`. The panel CSVs are unchanged. Report: `docs/reports/RAW_AFF_PART_NO_FIX_20261110.md`.

AJG-gap long parts blanked: prio43 358 / ajg2 236 / ajg1 2,317.

**Directory.** Unchanged: appointments 162,575, editors 112,718, journals 2,853, Institutions 15,434 (6,387 with a ROR id), countries 159, 12,067 appointments without an institution, shared display names 69.

## Previous freeze: editors_edpacs_marks_country_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_paren_num_leftover_fix_20261110` (Directory PR #50) for the Directory current panels. It is a keyed, user-approved follow-up on three ABDC C EDPACS seats. No ROR ids change and there is no site filter. The long table and change log are in `data/editors/releases/editors_edpacs_marks_country_fix_20261110/`. Report: `docs/reports/EDPACS_MARKS_COUNTRY_FIX_20261110.md`.

The three AJG-gap files are unchanged.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,434 (6,387 with a ROR id), were 15,435 / 6,387. Countries stay 159. 12,067 appointments have no institution (was 12,066: Marks' seat no longer falls back to his printed bio). Shared display names stay 69. The only parenthesis- and number-start Institutions left are the 14 kept numbered organisations.

## Previous freeze: editors_paren_num_leftover_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_tokyo_other_inst_fix_20261110` (Directory PR #49) for the Directory current panels. It is a keyed, user-approved fix for the parenthesis- and number-start Institutions left as REVIEW. Only institution fields are changed, the printed `raw_affiliation` is kept, and the guardrail and history notes stay in `ror_notes` with a `paren_num_leftover_fix_20261110:` token appended. No new ROR ids and no site filter. The long table and change log are in `data/editors/releases/editors_paren_num_leftover_fix_20261110/`. Report: `docs/reports/PAREN_NUM_LEFTOVER_FIX_20261110.md`.

`editors_abs_ajg_gap_ajg1_current#7504` (Neha Gangwar, `(GGSIPU) Periyar Management and Computer College, India`) is rematched to Guru Gobind Singh Indraprastha University `https://ror.org/034q1za58`, which was already on 3 panel rows. ajg1 `ror_id` 8,698 (was 8,697). ajg1 stays 12,316 rows: the collector file's ten extra navigation keys stay out. prio43 and ajg2 are unchanged.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,435 (6,387 with a ROR id), were 15,438 / 6,387. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The remaining parenthesis- and number-start Institutions are the 14 kept numbered organisations, plus Norman Marks' printed bio, which still shows through the printed-text fallback.

## Previous freeze: editors_tokyo_other_inst_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_tokyo_gatech_fix_20261110` (Directory PR #48) for the Directory current panels. It is a keyed ABDC-only fix for the 35 seats whose `canonical_name` was the bare `Tokyo` with a blank ROR. The collector's copies of those seats had the place-strip rewrite `Italian Cultural Institute`, and the Directory guardrail had already restored the printed text. The three AJG-gap files are unchanged. There is no site filter. The long table and change log are in `data/editors/releases/editors_tokyo_other_inst_fix_20261110/`. Report: `docs/reports/TOKYO_OTHER_INST_FIX_20261110.md`.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,438 (6,387 with a ROR id), were 15,432 / 6,381. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The unmatched `Tokyo` (Japan) Institutions row falls from 35 appointments to 1.

## Previous freeze: editors_tokyo_gatech_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_inst_punct_split_20261110` (Directory PR #47) for the Directory current panels. It is a keyed panel-only fix on the AJG-gap files. It rematches University of Tokyo seats whose ROR the Directory guardrail (`directory_guardrail_restore_20261101`) had left blank to The University of Tokyo `https://ror.org/057zh3y96`, and rematches the Decision Sciences `Georgia Inst of Technology` seat to `https://ror.org/01zkghx44`. The printed `raw_affiliation` is kept, and the Directory guardrail note stays in `ror_notes` with the fix token appended. There is no site filter. The long table and change log are in `data/editors/releases/editors_tokyo_gatech_fix_20261110/`. Report: `docs/reports/TOKYO_GATECH_FIX_20261110.md`.

| File | Rows | Rows patched | `ror_id` (was) |
|---|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 1 | 2,546 (2,545) |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,462 | 2 | 4,746 (4,744) |
| `editors_abs_ajg_gap_ajg1_current.csv` | 12,316 | 3 | 8,697 (8,694) |

The ajg1 / ajg2 navigation rows stay out. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,432 (6,381 with a ROR id), were 15,434 / 6,381. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The University of Tokyo is one Institutions row (`057zh3y96`, 173 appointments); `Georgia Inst of Technology` is no longer a separate unmatched row.

## Previous freeze: editors_inst_punct_split_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_inst_drop_rematch_20261110` (Directory PR #46) for the Directory current panels. It is a panel-only Institutions cleanup on the AJG-gap files: leftover punctuation-start junk is blanked (DROP), high-confidence name splits are rematched onto existing panel ROR twins (REMATCH; printed `raw_affiliation` kept; `canonical_name` set to the twin `ror_name`), and three name-only variants are unified with a blank ROR (UNIFY). REVIEW and KEEP flags were excluded. There is no site filter in `scripts/build_site.py`. The long table and change log are in `data/editors/releases/editors_inst_punct_split_20261110/`. Report: `docs/reports/INST_PUNCT_SPLIT_20261110.md`.

**What changed.** All three AJG-gap current panels are patched by the collector delta applied onto the published Directory copy of `editors_inst_drop_rematch_20261110` (prio43 9, ajg2 14, ajg1 51 REMATCH rows; no DROP or UNIFY). The twelve ajg1 navigation rows (including Vincent Pan) and the two ajg2 Policy Design and Practice navigation rows stay out; the collector ajg1 file still has ten of those extra keys, which were not added. Published ajg1 remains 12,316 and ajg2 remains 5,462.

| File | Rows | `ror_id` (was) | Nonempty `raw_affiliation` | Empty `editor_name` |
|---|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 2,545 (2,536) | 2,723 | 3 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,462 | 4,744 (4,730) | 5,224 | 0 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 12,316 | 8,694 (8,643) | 9,997 | 15 |

`faculty_profile_url` stays prio43 82, ajg2 386, ajg1 615. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,434 (6,381 with a ROR id), were 15,612 / 6,381. Countries stay 159. 12,066 appointments have no institution (were 12,052). Shared display names 69 (were 125).

## Previous freeze: editors_inst_drop_rematch_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_nonlatin_inst_20261110` (Directory PR #45) for the Directory current panels. It is a panel-only Institutions cleanup on the AJG-gap files (DROP junk bios and address lines; REMATCH singleton variants onto existing panel ROR twins; printed `raw_affiliation` kept). REVIEW and KEEP flags were excluded. There is no site filter in `scripts/build_site.py`. The long table and change log are in `data/editors/releases/editors_inst_drop_rematch_20261110/`. Report: `docs/reports/INST_DROP_REMATCH_20261110.md`.

**What changed.** All three AJG-gap current panels are patched by the collector delta applied onto the published Directory copy of `editors_nonlatin_inst_20261110`. The twelve ajg1 navigation rows (including Vincent Pan) and the two ajg2 Policy Design and Practice navigation rows stay out; the collector ajg1 file still has ten of those extra keys, which were not added. Directory guardrail restores and contact scrub stay. Published ajg1 remains 12,316 and ajg2 remains 5,462. One GAP row, `The Universidad Nacional Experimental Politécnica`, keeps its printed name and a blank ROR.

| File | Rows | `ror_id` (was) | Nonempty `raw_affiliation` (was) | Empty `editor_name` |
|---|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 2,536 (2,534) | 2,723 (2,723) | 3 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,462 | 4,730 (4,686) | 5,224 (5,224) | 0 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 12,316 | 8,643 (8,454) | 9,997 (9,998) | 15 |

`faculty_profile_url` stays prio43 82, ajg2 386, ajg1 615. `11KBW`, UNSW Sydney, and INSEAD stay. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,612 (6,381 with a ROR id), were 16,234 / 6,381. Countries stay 159. 12,052 appointments have no institution (were 11,991).

## Previous freeze: editors_nonlatin_inst_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_ror_consistency3b_20261101` (Directory PR #41) for the Directory current panels. The files in this folder are unchanged. The only panel edit is on ABDC C (19 bio/CV blurbs blanked, 60 rematches onto existing Latin ROR twins, printed non-Latin names kept). Long table: `data/editors/releases/editors_nonlatin_inst_20261110/editor_affiliations.csv.gz`. Report: `docs/reports/NONLATIN_INST_20261110.md`.

## Previous freeze: editors_ror_consistency3b_20261101

Published 2026-11-01 (Asia/Hong_Kong) with user approval. This supersedes `editors_browser_single_20261029` (Directory PR #40). The collector packs between the two (`editors_ror_consistency2`, `editors_ror_consistency`, `editors_ror_multiaff`, `editors_ror_campus2`, `editors_ror_campus`, `post15`, the profile `pilot`, the scale-parse packs, and the t39 / institution-fix freezes) were never published and are retired. The long table and audit logs are in `data/editors/releases/editors_ror_consistency3b_20261101/`; reports in `docs/reports/` (`PREPUBLISH_CHECK_20261101.md`, `ROR_PREPUBLISH_FIX_20261101.md`, `ROR_CONSISTENCY3_20261101.md`). The core49 backfill `editors_backfill_scale_ror_20261031` is pinned at the same time under `data/editors/core49/releases/`.

**Columns.** After `board_urls` and `board_url_count` every panel adds `board_status`, `tenure_start_year`, `tenure_end_year`, `snapshot_date`, `snapshot_source`, `board_year`, `editor_row_key`, `affiliation_count`, `ror_id_aff_rank`, `primary_aff_basis`, `former_flag`, and `other_ror_ids`. The slim `editors_ft50_current.csv` also gains `ror_id`, `ror_name`, `ror_country`, and `continent`. The board columns are no longer the last two. A single `board_urls` entry may now appear on any journal.

**ROR.** The collector blanks a ROR id when the masthead text cannot be matched to one organization without guessing (strict matching, multi-affiliation parsing, campus splits). So `ror_id` coverage is lower than in `editors_browser_single_20261029` on every panel except ajg2, and a few correct ids were blanked as ambiguous. Nothing was invented. Display affiliation is still `ror_name`, then `canonical_name`, then `raw_affiliation`; country is `ror_country`.

**Directory guardrails kept.** The twelve ajg1 navigation rows (including Vincent Pan on Advances in Decision Sciences) and the two ajg2 Policy Design and Practice navigation rows stay out. Collector institution-string rewrites that were wrong (for example Tokyo mastheads rewritten to `Italian Cultural Institute`, and HKUST (Guangzhou) collapsed onto HKUST) are reverted to the published text: 95 rows plus two `editor_name_raw` restores, listed in `DIRECTORY_GUARDRAILS_restored_rows_20261101.csv`. `11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate; ESSEC is France `02dga6j42`. A blank or country-only affiliation is not an institution. Emails and phone or fax numbers that the collector left in text cells (mostly `source_note`) were removed.

**Directory.** Appointments 162,575 (were 160,104). Editors 112,718 (were 111,229). Journals 2,853. Institutions 16,283 rows, 6,381 with a ROR id (were 11,344 / 8,665). 11,972 appointments have no institution; 650 country-only, 12 bracket-only, and 7 address-only appointments stay off Institutions. Countries 159 (were 175).

| File | Rows (was) | `ror_id` (was) | Empty `editor_name` |
|---|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 (3,104) | 2,534 (2,651) | 3 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,462 (4,982) | 4,686 (4,574) | 0 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 12,316 (11,544) | 8,454 (8,625) | 15 |

Ten ajg1 rows in the collector file are removed here (the navigation keys plus a blank Journal of Information Technology Management row); the build name filter drops the rest. Contact text removed from ajg1 30 and ajg2 6 cells.

## Previous freeze: editors_browser_single_20261029

Frozen 2026-10-30 07:09 Asia/Taipei. This supersedes `editors_single_editor_20261029` (Directory PR #39). The collector added browser-captured boards on three ABDC journals: Journal of Derivatives (A, 1 to 18), Journal of Portfolio Management (A, 1 to 73), and Arts and the Market (C, 1 to 55). The three AJG-gap files are unchanged in this publish. The collector copies are byte-identical to `editors_single_editor_20261029`. See `data/editors/abdc/releases/current/RELEASE_NOTES.md`.

Directory appointments are 160,104, were 159,961. Editors are 111,229, were 111,154. Journals stay 2,853. Institutions are 11,344 rows (8,665 with a ROR id), were 11,276 (8,663). 12,307 appointments have no institution. 642 country-only, 3 bracket-only, and 5 street, PO Box, or postal-code appointments stay off that page. `11KBW`, UNSW Sydney, and INSEAD stay. Twelve ajg1 navigation rows stay out, including Vincent Pan on Advances in Decision Sciences.

## Previous freeze: editors_single_editor_20261029

Fuller boards for four AJG 1 journals that had one editor row, plus two browser-board replacements carried in this freeze. Frozen 2026-10-29 23:18 Asia/Taipei. This supersedes `editors_browser_boards_20261029`. prio43 and ajg2 row counts are unchanged. African Affairs stays the 40-row Wayback board. Rankings were not edited. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. Empty `editor_name` is 3 on prio43, 0 on ajg2, and 16 on ajg1. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

Every current editor CSV ends with `board_urls` and `board_url_count`. `board_urls` is a pipe-separated list of public board-page URLs, filled only when that board spans more than one page. On these files that is PASOS Journal of Tourism and Cultural Heritage. `board_url_count` is the number of those URLs. Both cells are blank on every other row. `source_url` stays the primary board link. The build selects columns by name and does not write `board_urls` to the site.

The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. Live OUP for African Affairs is still Cloudflare-blocked. See `african_affairs_needs_browser.md`.

This publish replaces the rows of six ajg1 journals. Other rows stay as published in `editors_apjiht_board_fix_20261029`, including the three-journal board fix and the place-suffix and country corrections from earlier freezes. Small Business International Review stays parked (6 rows). The collector ajg1 file again included 12 navigation or citation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them. His collector row carries `Architecture Business School` and `https://ror.org/04facnr46`. No replacement ROR was added. The collector file counted ajg1 as 11,295 to 11,556 because those 12 rows were still in it. The published file is 11,244 to 11,544.

## Boards

| Journal | Was | Now |
|---|---:|---:|
| International Journal of Innovation and Technology Management | 1 | 96 |
| PASOS Journal of Tourism and Cultural Heritage | 1 | 87 |
| Pacific Journal of Optimization | 1 | 54 |
| Quantitative Finance and Economics | 11 | 43 |
| Strategic Behavior and the Environment | 1 | 28 |
| Foundations and Trends® in Information Systems | 6 | 13 |

International Journal of Innovation and Technology Management is 96 people, from the 2022-08-14 Wayback snapshot. The live World Scientific page returned 403. Source `https://web.archive.org/web/20220814200834/https://www.worldscientific.com/page/ijitm/editorial-board`. ROR ids already on these boards are attached on 65 of 96 (63 high, 2 medium).

PASOS Journal of Tourism and Cultural Heritage is 87 people. `board_urls` lists the editorial team, the scientific council, and the about page (`board_url_count` 3), all Wayback copies. ROR ids already on these boards are attached on 4 of 87, all high.

Pacific Journal of Optimization is 54 people. The old row was `Order Form`. Source `https://web.archive.org/web/20251117200040/http://manu71.magtech.com.cn/Jwk3_pjo/EN/column/column2.shtml`. ROR ids already on these boards are attached on 33 of 54, all high.

Quantitative Finance and Economics is 43 people. The old rows were navigation labels. Source `https://www.aimspress.com/qfe/news/solo-detail/editorialboard`. One ROR id already on these boards is attached (Jinyu Chen, Central South University, high).

Strategic Behavior and the Environment is 28 people. Source `https://web.archive.org/web/20260321070732id_/https://www.emerald.com/sbe/pages/editorial-board`. The publisher line is not on this board. ROR ids already on these boards are attached on 21 of 28, all high.

Foundations and Trends® in Information Systems is 13 people. The old rows were navigation labels and two blank names. Source `https://www.emerald.com/ftisy/pages/editorial-board`. ROR ids already on these boards are attached on all 13, all high.

Small Business International Review stays the 6 parked rows. The site was unreachable.

The new rows contain no email address, phone number, or photo.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2. The collector CSV again included 12 ajg1 navigation or citation rows and 2 ajg2 navigation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, blank affiliation | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 3 | 82 | 2,723 | 2,651 | 1 | 2 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,982 | 0 | 386 | 4,727 | 4,574 | 0 | 7 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,544 | 16 | 616 | 9,159 | 8,625 | 2 | 7 |
| Total | 19,630 | 19 | 1,084 | 16,609 | 15,850 | 3 | 16 |

`ror_id` on a nonempty affiliation is 15,850 / 16,609 (95.4%): ajg1 8,625 / 9,159 (94.2%), ajg2 4,574 / 4,727 (96.8%), prio43 2,651 / 2,723 (97.4%). Gap `ror_id` was 15,715. The added ids were already on these boards. Gap `ror_id` values are high or medium confidence only. A faculty URL with a blank affiliation is 3. Sixteen faculty URLs have no `ror_id`. No name, ROR id, affiliation, or URL was invented.

## Public site

Directory journals stay 2,853. Directory appointments are 159,961, were 158,747. Editors are 111,154, were 110,424. Countries stay 175. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796). Faculty profile links stay 24,817. The Institutions page has 11,276 rows (8,663 with a ROR id), were 10,824 (8,662), and 12,309 appointments with no institution. 641 appointments are omitted because the affiliation is only a country or territory, were 633. Three are omitted because the affiliation is only a bracketed fragment. Ten are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country. `11KBW`, UNSW Sydney, and INSEAD stay.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
