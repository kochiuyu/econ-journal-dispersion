# editors_post_fullreview_fix_20261111

Published 2026-11-11 (Asia/Taipei). This supersedes `editors_full_review_resolved_fix_20261111` (PR #54) for the Directory current panels. It is a keyed, user-approved Collector freeze, taken through its `POST_FULLREVIEW_directory_diff_20261111.csv` (keyed on `editor_row_key`; 4,593 cells, 0 missing keys, 0 old-value mismatches), plus `ror_notes` carried from the freeze on 9 rows. It applies the post-full-review residuals: WRONG_ROR 5/5 (inactive ROR records moved to their active successors: UniSA and Adelaide to Adelaide University `028g18b61`, TEI Piraeus to University of West Attica `00r2r5k05`, UPMC to Sorbonne Université `02en5vm52`, Rennes 1 to Université de Rennes `015m7wh34`), NEAR_DUPLICATE 101/138, MISSING_ROR 298/306 (269 new API-verified RORs), WRONG_COUNTRY 7 in full and 5 partly, NON_INSTITUTION 18/51 and MISSING_COUNTRY 11. It also applies the answers: 38 RENAMEs; Mercer, CTU Prague and CY Cergy; and FT50 slim #4634 set to its printed `Xi'an Jiaotong University, China` (`017zhmm22`). No pilot files are published or changed. No emails or phones.

Rows changed: 19 `editors_ft50_current_with_ror.csv` rows, 12 slim rows; `ror_id` 9,819 / 9,740 (was 9,808 / 9,729). Row counts unchanged (10,047).

**Directory.** Institutions 11,213 (was 11,330), 6,692 with a ROR id (was 6,396; distinct 6,692). Countries 169 (was 167; Guam and New Caledonia added). 13,413 appointments have no institution (was 13,404). Shared display names 44 (was 46; the build guard is now 44). Appointments 162,575, editors 112,719, journals 2,853 (unchanged).

Long table and change logs: `data/editors/releases/editors_post_fullreview_fix_20261111/` (`editor_affiliations.csv.gz`, 181,449 rows; 1,081 parts changed). Report: `docs/reports/POST_FULLREVIEW_FIX_20261111.md`.

## Previous freeze: editors_full_review_resolved_fix_20261111

Published 2026-11-11 (Asia/Taipei). This supersedes `editors_full_review_fix_20261111`, which supersedes `editors_raw_leak_fix_20261110`, for the Directory current panels. Both are keyed, user-approved Collector freezes taken through their directory diffs (keyed on `editor_row_key`; 21,335 + 5,085 cells, 0 old-value mismatches). `editors_full_review_fix_20261111` applies the full Institutions review send file (Institutions applied: MERGE 2,395, DROP 600, RENAME 231, SET_COUNTRY 214). DROP follows the Marks mechanism: name, raw and ROR blanked, printed text kept in `ror_notes`, country kept. It also fixes Jaap Paauwe (A* #2545 name `Jaap Paauwe`, raw `Tilburg, Netherlands`; FT50 #3821 `editor_name_raw` blank; both Tilburg University `04b8v1s79`, Netherlands). `editors_full_review_resolved_fix_20261111` applies 675 resolved held Institutions (SET_COUNTRY 559, MERGE 97, DROP 7, RENAME 5) and 213 row-level shared-name splits (e.g. University of Illinois → UIUC / UIC, Northeastern → Boston / Shenyang, University of Newcastle → UK / Australia), with 8 new ROR ids checked on the ROR API. Skipped by the Collector and still open: 77 MERGE rows already on a different campus ROR, 45 DROP rows that print a real organisation, 3 ROR ids that 404 (Mercer, CTU Prague, CY Cergy) and the Wisconsin Extended Campus system ROR.

Rows changed (both freezes): 382 `editors_ft50_current_with_ror.csv` rows, 345 slim rows; `ror_id` 9,808 / 9,729 (was 9,732 / 9,652). Row count unchanged (10,047). #3821 Jaap Paauwe: `editor_name_raw` is now blank, because A* #2545 has the clean name.

**Directory.** Institutions 11,330 (was 14,192; 11,426 after the first freeze), 6,396 with a ROR id (was 6,386; distinct 6,396). Countries 167 (was 162). 13,404 appointments have no institution (was 12,658). Shared display names 46 (was 49; the build guard is now 46). Appointments 162,575 (was 162,576: the Paauwe A* seat now merges with its FT50 copy), editors 112,719, journals 2,853.

Long tables and change logs: `data/editors/releases/editors_full_review_fix_20261111/` and `data/editors/releases/editors_full_review_resolved_fix_20261111/`. Report: `docs/reports/FULL_REVIEW_FIX_20261111.md`.

## Previous freeze: editors_full_review_fix_20261111

Published 2026-11-11 (Asia/Taipei) in the same Directory PR, under `editors_full_review_resolved_fix_20261111`. Directory after it alone: Institutions 11,426, 6,387 with a ROR id, countries 161, shared display names 45.

## Previous freeze: editors_raw_leak_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_raw_drift_fix_20261110` for the Directory current panels (stacked on Directory PR #53). It is a keyed, user-approved fix on top of `editors_raw_drift_fix_20261110` (PR #53) for the Collector's leak scan: 161 rows where a 2026-10-28/29 `institution_*` script had written a canonical or ROR name into `raw_affiliation` get the original printed text back (341 cells from `RAW_LEAK_directory_diff_20261110.csv`). 117 are raw-only restores (111 same-organisation, e.g. `The University of Osaka` → printed `Osaka University`; 6 wrong-organisation rows whose institution was already right). 44 also fix the institution: the 17 Pakistan rows that showed `National Institute of Oceanography` (e.g. COMSATS University Islamabad `00nqqvk19`, IoBM Karachi `048w4c951`), the `AM Publications` rows (SAGE Publishing `05534qc24` / SAGE UK, or blanked where only a role was printed), the Japan rows that showed `Temple University` (Waseda `00ntfnx83`, Otaru, Hiroshima Shudo `05n757p35`), `Beijing University, China` → Peking University `02v51f717` on ajg2 #2222 (B #33518 stays Beihang, editor-confirmed), Galuh University → Universitas Galuh `03m7qjm52` (new ROR, ROR API-verified), 5 Nottingham Trent → University of Nottingham Ningbo China and prio43 #1334 → University of Newcastle Australia. 5 African Affairs prio43 rows are skipped. Qiang Meng (A* #18960, Transportation Science) stays NUS as the INFORMS board prints it, with a note that he moved to HKUST (Guangzhou) on 2026-08-28. The long table gets the matching `raw_aff_part` / ROR parts and the 6 long rows for the Top 5 seats FT50 #10046–#10048 (both FT50 files), so it has 181,449 rows. Institutions 14,192 (was 14,176), 6,386 with a ROR id (was 6,384; distinct 6,386). Countries 162 (unchanged). 12,658 appointments have no institution (unchanged). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Rows changed: 3 `editors_ft50_current_with_ror.csv` rows, 2 slim rows; `ror_id` 9,732 / 9,652 (unchanged). Row count unchanged (10,047). The long table gains the 6 parts for the Top 5 seats #10046–#10048 (181,449 rows). #3821 Jaap Paauwe keeps `editor_name_raw` `Jaap Paauwe, Tilburg`: the ABDC A* HRM copy of the seat still uses that spelling, and the build uses it to merge the two rows.

**Directory.** Institutions 14,192 (was 14,176), 6,386 with a ROR id (was 6,384; distinct 6,386). Countries 162 (unchanged). 12,658 appointments have no institution (unchanged). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Long table and change log: `data/editors/releases/editors_raw_leak_fix_20261110/`. Report: `docs/reports/RAW_LEAK_FIX_20261110.md`.

## Previous freeze: editors_raw_drift_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_post_review_fix_20261110` for the Directory current panels (stacked on Directory PR #53). It is a keyed, user-approved fix on top of `editors_post_review_fix_20261110` (PR #53) that closes the raw-text drift between the Directory and the Collector source panels (comparison `raw_drift_20261110.csv`): the 21 rows whose printed text had been rewritten to `National Law University` keep their printed text and get the real ROR and country instead of the leftover India (e.g. University of Lyon → `01rk35k63`, The University of Law → `00bge3r76`, Plovdiv University → `0545p3742`, Politehnica București → `0558j5q12`); 11 HKUST (Guangzhou) rows are on `050h0vm43` / China (including C #27613, which was on the HKUST Hong Kong ROR); Kagoshima University `03ss88z23` replaces Nihon University; MIT replaces Ikon Science; Gradient (United States) `014qf4206` replaces Korea Telecom; ENSAI `00k206f19` and Springer Nature (Shanghai, China) `01f9pza55` are matched; FT50 #2955 (Tiffany Trzebiatowski) gets `Colorado State University` (`03k1gpj17`) in both FT50 files instead of a blank / bio; and AJG1 #10149 (Lawrence Sweet) takes the live-source text `IZZI Inc`. The three Top 5 seats (#10046–#10048) were already in the Directory copy and are not duplicated; the two Pompeu Fabra institution-as-name rows and the AJG1 navigation rows stay out. New ROR ids were checked on the ROR API; none is invented. Institutions 14,176 (was 14,195), 6,384 with a ROR id (was 6,379; distinct 6,384). Countries 162 (unchanged). 12,658 appointments have no institution (was 12,659). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Rows changed: 1 `editors_ft50_current_with_ror.csv` row, 1 slim row; `ror_id` 9,732 (was 9,731) / 9,652 (was 9,651). Row count unchanged (10,047); the Collector's three added Top 5 seats were already here.

**Directory.** Institutions 14,176 (was 14,195), 6,384 with a ROR id (was 6,379; distinct 6,384). Countries 162 (unchanged). 12,658 appointments have no institution (was 12,659). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Long table and change log: `data/editors/releases/editors_raw_drift_fix_20261110/`. Report: `docs/reports/RAW_DRIFT_FIX_20261110.md`.

## Previous freeze: editors_post_review_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_review_resolved_fix_20261110` for the Directory current panels (stacked on Directory PR #53). It is a keyed, user-approved clean-up on top of `editors_review_resolved_fix_20261110` (PR #53), from the post-review Institution audit (399 names): trailing city / state / country cut or dropped (63 renamed, 74 dropped); role prefixes cut or dropped (22 / 49); department prefixes mapped to the parent organisation (30); near-duplicates merged (25 name merges, 10 ROR merges, 2 drops); fragments (punctuation, credential, address, place, contact) renamed or dropped (10 / 17); 3 long bios resolved; wrong RORs fixed (three STIE rows blanked off Universitas Patria Artha; CUNY rows → `00453a208`; Abt → `0502afh35`; IIESS → `033xgn512`, Argentina, the one new ROR, verified on ror.org; St Petersburg University → `023znxa73`; Inria → `02kvxyf05`); and contact text removed (e-mail addresses, including comma-malformed ones, and phone numbers; 2 ABDC B `editor_name` cells that held only a phone number are now blank). DROP follows the Marks mechanism (printed text kept in `ror_notes` / `ror_match_note`). The audit's 34 shared-name KEEP rows are untouched; no ROR id is invented. Institutions 14,195 (was 14,440), 6,379 with a ROR id (unchanged; distinct 6,379). Countries 162 (unchanged). 12,659 appointments have no institution (was 12,487). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Rows changed: 4 `editors_ft50_current_with_ror.csv` rows, 2 slim rows; `ror_id` 9,731 (was 9,730) / 9,651 (was 9,650). Row count unchanged (10,047).

**Directory.** Institutions 14,195 (was 14,440), 6,379 with a ROR id (unchanged; distinct 6,379). Countries 162 (unchanged). 12,659 appointments have no institution (was 12,487). Shared display names 49 (unchanged). Appointments 162,576, editors 112,719, journals 2,853.

Long table and change log: `data/editors/releases/editors_post_review_fix_20261110/`. Report: `docs/reports/POST_REVIEW_FIX_20261110.md`.

## Previous freeze: editors_review_resolved_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_weird_inst_fix_20261110` for the Directory current panels (stacked on Directory PR #53). It is a keyed, user-approved fix on top of `editors_weird_inst_fix_20261110` (PR #53): the resolved REVIEW Institutions (REMATCH 203, STRIP 48, DROP 18 by the Marks mechanism, RENAME 18, SET_COUNTRY 3; the 49 KEEP names untouched) and 84 row-level splits (Northeastern, American, Concordia, Los Andes and Trinity College editor-confirmed rows; HEC split Paris / Montréal / Lausanne; IAE Aix / Poitiers; York University rows on York College PA `022jz8688` → Toronto `05fq50484`); Zhichen Chen (IJBPM) → Hainan Vocational University of Science and Technology `05a8bts04` (China; the one new ROR, verified on ror.org); 26 over-stripped names restored from the printed text (e.g. `Sydney Law School`, `Tokyo Institute of Technology` kept separate from Institute of Science Tokyo, `T-Mobile`); 'Tel' scrub damage restored in canonical names (Telematic, Tel-Hai, Telecom); wrong-ROR fixes (George Washington → `00y4zzh67`, off the George Institute UK ROR; IfM Bonn row → `04c7t5k94`; NC State, Georgia Tech Scheller, Catholic University Milan, Bologna, Lüneburg, Imperial, Pegaso, NKUST; a few contradicted RORs blanked); and e-mail addresses removed from text cells. Printed `raw_affiliation` changes only on DROP rows (traced) or e-mail removal. `scripts/build_site.py`: the phone/e-mail scrub labels now need a word boundary (Collector patch), so `Tel Aviv University`, `T-Mobile`, `Telkom University` and the Telematic names display in full, and the shared-name guard is 49. The long table, change log and skip list are in `data/editors/releases/editors_review_resolved_fix_20261110/`. Report: `docs/reports/REVIEW_RESOLVED_FIX_20261110.md`.

Rows changed: `editors_ft50_current_with_ror.csv` 37 rows, `editors_ft50_current.csv` 35 rows; `ror_id` 9,730 / 9,650 (was 9,703 / 9,624). Both files stay 10,047 rows.

**Directory.** Institutions 14,440 (was 14,672), 6,379 with a ROR id (was 6,387; distinct 6,379). Countries 162 (unchanged). 12,487 appointments have no institution (was 12,460). Shared display names 49 (was 69). Appointments 162,576, editors 112,719, journals 2,853.

## Previous freeze: editors_weird_inst_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_country_misprint_fix_20261110` for the Directory current panels (stacked on Directory PR #53). It is a keyed, user-approved clean-up of weird Institution names on top of `editors_country_misprint_fix_20261110` (PR #53), from the non-REVIEW rows of the Institution audit: DROP 178 Institutions (391 publish rows; place-only, generic-role and credential names such as `Maryland`, `Independent Researcher, Vermont`, `Associate Professor`) plus 5 country-only fallbacks (`Greece and UK`, `Italy & UK`, `Finland and Tanzania`, `SE, UK`, the Solicitor string); STRIP 594 (632 rows; role prefixes, addresses, postcodes, URLs, punctuation and trailing state codes cut, e.g. `Harvard Business School, Cambridge, MA` → `Harvard Business School`); SET_COUNTRY 122 (137 rows, from a trailing state or code); REMATCH 186 (249 rows, to an existing panel twin ROR); and the University of Georgia fix (US rows on the Tbilisi ROR `02bjhwk41` → `00te3t702` / United States). DROP follows the Marks mechanism: `canonical_name`, `raw_affiliation` and `ror_id` are blanked, the printed text is kept in `ror_notes` (long table: `raw_aff_part` blanked, trace in `ror_match_note`); country stays. 120 rows whose printed raw still names an organisation (e.g. `Sydney Law School`, `Tokyo Institute of Technology`) are not dropped and are listed for a later restore. The audit's REVIEW names are untouched; no ROR id is invented. The long table, change log and skip list are in `data/editors/releases/editors_weird_inst_fix_20261110/`. Report: `docs/reports/WEIRD_INST_FIX_20261110.md`.

Rows changed: `editors_ft50_current_with_ror.csv` 18 rows, `editors_ft50_current.csv` 8 rows; `ror_id` 9,703 / 9,624 (was 9,701 / 9,622). Both files stay 10,047 rows.

**Directory.** Institutions 14,672 (was 15,160), 6,387 with a ROR id (unchanged). Countries 162 (unchanged). 12,460 appointments have no institution (was 12,068). Shared display names stay 69. Appointments 162,575, editors 112,718, journals 2,853.

## Previous freeze: editors_country_misprint_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_trailing_country_fix_20261110` (Directory PR #53) for the Directory current panels. It is a keyed, user-approved fix on top of `editors_trailing_country_fix_20261110` (PR #53): 30 publish rows get the real country for 27 Institutions whose printed country was wrong (e.g. ESADE Business School → Spain, TU Berlin → Germany, Queens University Belfast → United Kingdom); Imperial College of London (C #17649) is rematched to the existing panel ROR `041kmwe10` Imperial College London. 11 fragment rows (the 11 held back in PR #53) get a clean `canonical_name` or a blank one: the Court of Appeal / Supreme Court rows become `Court of Appeal of England and Wales` / `Supreme Court of the United Kingdom` (UK), the two Independent Scholar rows become `Independent Scholar`, and `Greece and`, `Italy &`, `Finland and`, `SE` and the Solicitor row are blanked, so the Directory falls back to the printed text (e.g. `Greece and UK`). `University of the North, Barranquilla, .` loses its trailing `, .` and merges with its twin. The printed `raw_affiliation` is unchanged; no ROR id is invented. The long table, change log and skip list are in `data/editors/releases/editors_country_misprint_fix_20261110/`. Report: `docs/reports/COUNTRY_MISPRINT_FIX_20261110.md`.

Rows changed: Both FT50 files are unchanged.

**Directory.** Institutions 15,160 (was 15,166), 6,387 with a ROR id (unchanged). Countries 162 (unchanged). 12,068 appointments have no institution (unchanged). Appointments 162,575, editors 112,718, journals 2,853. Shared display names stay 69.

## Previous freeze: editors_trailing_country_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_raw_aff_part_no_fix_20261110` (Directory PR #52) for the Directory current panels. It is a keyed, user-approved fix for Institution names that ended in a printed country. 6,036 publish-panel rows get the country stripped from `canonical_name` and `ror_country` / `continent` set from it (137 Institutions are rematched to an existing panel twin, reusing that twin's ROR id where it has one; no ROR id is invented). The printed `raw_affiliation` is unchanged. The audit's REVIEW and KEEP names are untouched, and 11 rows whose stripped name would end in a dangling `and` / `&` (e.g. `Court of Appeal of England and`) are held back. No site filter. The long table, change log and skip list are in `data/editors/releases/editors_trailing_country_fix_20261110/`. Report: `docs/reports/TRAILING_COUNTRY_FIX_20261110.md`.

Rows changed: with_ror 84 (name + country), slim 81 (country only).

**Directory.** Institutions 15,166 (was 15,434), 6,387 with a ROR id (unchanged). Countries 162 (was 159: Guinea, Haiti, Timor-Leste). 12,068 appointments have no institution (was 12,067: a printed `…, Haiti` row now falls to the country-only filter). Appointments 162,575, editors 112,718, journals 2,853. Shared display names stay 69.

## Previous freeze: editors_raw_aff_part_no_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_edpacs_marks_country_fix_20261110` (Directory PR #51) for the Directory current panels. It is a long-table-only fix: `raw_aff_part` `no` → blank on 9,695 parts of `data/editors/releases/editors_raw_aff_part_no_fix_20261110/editor_affiliations.csv.gz`. The panel CSVs are unchanged. Report: `docs/reports/RAW_AFF_PART_NO_FIX_20261110.md`.

FT50 long parts blanked: 104 (slim) / 99 (with_ror).

**Directory.** Unchanged: appointments 162,575, editors 112,718, journals 2,853, Institutions 15,434 (6,387 with a ROR id), countries 159, 12,067 appointments without an institution, shared display names 69.

## Previous freeze: editors_edpacs_marks_country_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_paren_num_leftover_fix_20261110` (Directory PR #50) for the Directory current panels. It is a keyed, user-approved follow-up on three ABDC C EDPACS seats. No ROR ids change and there is no site filter. The long table and change log are in `data/editors/releases/editors_edpacs_marks_country_fix_20261110/`. Report: `docs/reports/EDPACS_MARKS_COUNTRY_FIX_20261110.md`.

Both FT50 files are unchanged.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,434 (6,387 with a ROR id), were 15,435 / 6,387. Countries stay 159. 12,067 appointments have no institution (was 12,066: Marks' seat no longer falls back to his printed bio). Shared display names stay 69. The only parenthesis- and number-start Institutions left are the 14 kept numbered organisations.

## Previous freeze: editors_paren_num_leftover_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_tokyo_other_inst_fix_20261110` (Directory PR #49) for the Directory current panels. It is a keyed, user-approved fix for the parenthesis- and number-start Institutions left as REVIEW. Only institution fields are changed, the printed `raw_affiliation` is kept, and the guardrail and history notes stay in `ror_notes` with a `paren_num_leftover_fix_20261110:` token appended. No new ROR ids and no site filter. Both FT50 files are unchanged. The long table and change log are in `data/editors/releases/editors_paren_num_leftover_fix_20261110/`. Report: `docs/reports/PAREN_NUM_LEFTOVER_FIX_20261110.md`.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,435 (6,387 with a ROR id), were 15,438 / 6,387. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The remaining parenthesis- and number-start Institutions are the 14 kept numbered organisations, plus Norman Marks' printed bio, which still shows through the printed-text fallback.

## Previous freeze: editors_tokyo_other_inst_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_tokyo_gatech_fix_20261110` (Directory PR #48) for the Directory current panels. It is a keyed ABDC-only fix for the 35 seats whose `canonical_name` was the bare `Tokyo` with a blank ROR. The collector's copies of those seats had the place-strip rewrite `Italian Cultural Institute`, and the Directory guardrail had already restored the printed text. Both FT50 files are unchanged. There is no site filter. The long table and change log are in `data/editors/releases/editors_tokyo_other_inst_fix_20261110/`. Report: `docs/reports/TOKYO_OTHER_INST_FIX_20261110.md`.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,438 (6,387 with a ROR id), were 15,432 / 6,381. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The unmatched `Tokyo` (Japan) Institutions row falls from 35 appointments to 1.

## Previous freeze: editors_tokyo_gatech_fix_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_inst_punct_split_20261110` (Directory PR #47) for the Directory current panels. It is a keyed panel-only fix on FT50. It rematches University of Tokyo seats whose ROR the Directory guardrail (`directory_guardrail_restore_20261101`) had left blank to The University of Tokyo `https://ror.org/057zh3y96`, and rematches the Decision Sciences `Georgia Inst of Technology` seat to `https://ror.org/01zkghx44`. The printed `raw_affiliation` is kept, and the Directory guardrail note stays in `ror_notes` with the fix token appended. There is no site filter. The long table and change log are in `data/editors/releases/editors_tokyo_gatech_fix_20261110/`. Report: `docs/reports/TOKYO_GATECH_FIX_20261110.md`.

| File | Rows | `ror_id` (was) | `raw_affiliation` |
|---|---:|---:|---:|
| `editors_ft50_current.csv` | 10,047 | 9,622 (9,620) | 9,936 |
| `editors_ft50_current_with_ror.csv` | 10,047 | 9,701 (9,699) | 9,941 |

Two rows per file: Eric Weese (Econometrica) and Fuhito Kojima (Journal of Political Economy). Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,432 (6,381 with a ROR id), were 15,434 / 6,381. Countries stay 159. 12,066 appointments have no institution (unchanged). Shared display names stay 69. The University of Tokyo is one Institutions row (`057zh3y96`, 173 appointments); `Georgia Inst of Technology` is no longer a separate unmatched row.

## Previous freeze: editors_inst_punct_split_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_inst_drop_rematch_20261110` (Directory PR #46) for the Directory current panels. It is a panel-only Institutions cleanup on FT50: leftover punctuation-start junk is blanked (DROP), high-confidence name splits are rematched onto existing panel ROR twins (REMATCH; printed `raw_affiliation` kept; `canonical_name` set to the twin `ror_name`), and three name-only variants are unified with a blank ROR (UNIFY). REVIEW and KEEP flags were excluded. There is no site filter in `scripts/build_site.py`. The long table and change log are in `data/editors/releases/editors_inst_punct_split_20261110/`. Report: `docs/reports/INST_PUNCT_SPLIT_20261110.md`.

**What changed.** Both FT50 files are patched by the collector delta applied onto the published Directory copy of `editors_inst_drop_rematch_20261110` (13 slim + 20 with_ror REMATCH rows; no DROP or UNIFY). The collector copies were not overlaid. Directory guardrail restores, contact scrub, and the FT50 Top 5 alignment stay. `*_with_profile_pilot.csv` is not published.

| File | Rows | `ror_id` (was) | `raw_affiliation` |
|---|---:|---:|---:|
| `editors_ft50_current.csv` | 10,047 | 9,620 (9,607) | 9,936 |
| `editors_ft50_current_with_ror.csv` | 10,047 | 9,699 (9,679) | 9,941 |

`11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,434 (6,381 with a ROR id), were 15,612 / 6,381. Countries stay 159. 12,066 appointments have no institution (were 12,052). Shared display names 69 (were 125).

## Previous freeze: editors_inst_drop_rematch_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_nonlatin_inst_20261110` (Directory PR #45) for the Directory current panels. It is a panel-only Institutions cleanup (DROP junk bios and address lines; REMATCH singleton variants onto existing panel ROR twins; printed `raw_affiliation` kept). REVIEW and KEEP flags were excluded. There is no site filter in `scripts/build_site.py`. Long table: `data/editors/releases/editors_inst_drop_rematch_20261110/editor_affiliations.csv.gz`. Report: `docs/reports/INST_DROP_REMATCH_20261110.md`.

**What changed.** Both FT50 files are patched by the collector delta applied onto the published Directory copy of `editors_nonlatin_inst_20261110`. Directory guardrail restores, contact scrub, held-out AJG1 navigation rows, and the FT50 Top 5 alignment stay. The collector copies were not overlaid, because they predate those Directory-only edits. Slim `editors_ft50_current.csv` also blanks Tiffany Trzebiatowski's Journal of Management Studies CV (the collector only patched the with_ror copy of that row). Elizabeth M. Lee's slim rematch to Saint Joseph's University is not copied onto with_ror (that file already blanks the id as PA vs NY ambiguous).

| File | Rows | `ror_id` (was) | `raw_affiliation` (was) |
|---|---:|---:|---:|
| `editors_ft50_current.csv` | 10,047 | 9,607 (9,600) | 9,936 (9,941) |
| `editors_ft50_current_with_ror.csv` | 10,047 | 9,679 (9,673) | 9,941 (9,946) |

`11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate. Invented ROR ids: 0.

**Directory.** Appointments 162,575. Editors 112,718. Journals 2,853. Institutions 15,612 (6,381 with a ROR id), were 16,234 / 6,381. Countries stay 159. 12,052 appointments have no institution (were 11,991).

## Previous freeze: editors_nonlatin_inst_20261110

Published 2026-11-10 (Asia/Taipei). This supersedes `editors_ror_consistency3b_20261101` (Directory PR #41) for the Directory current panels. The files in this folder are unchanged. The only panel edit is on ABDC C (19 bio/CV blurbs blanked, 60 rematches onto existing Latin ROR twins, printed non-Latin names kept). Long table: `data/editors/releases/editors_nonlatin_inst_20261110/editor_affiliations.csv.gz`. Report: `docs/reports/NONLATIN_INST_20261110.md`.

## Previous freeze: editors_ror_consistency3b_20261101

Published 2026-11-01 (Asia/Hong_Kong) with user approval. This supersedes `editors_browser_single_20261029` (Directory PR #40). The collector packs between the two (`editors_ror_consistency2`, `editors_ror_consistency`, `editors_ror_multiaff`, `editors_ror_campus2`, `editors_ror_campus`, `post15`, the profile `pilot`, the scale-parse packs, and the t39 / institution-fix freezes) were never published and are retired. The long table and audit logs are in `data/editors/releases/editors_ror_consistency3b_20261101/`; reports in `docs/reports/` (`PREPUBLISH_CHECK_20261101.md`, `ROR_PREPUBLISH_FIX_20261101.md`, `ROR_CONSISTENCY3_20261101.md`). The core49 backfill `editors_backfill_scale_ror_20261031` is pinned at the same time under `data/editors/core49/releases/`.

**Columns.** After `board_urls` and `board_url_count` every panel adds `board_status`, `tenure_start_year`, `tenure_end_year`, `snapshot_date`, `snapshot_source`, `board_year`, `editor_row_key`, `affiliation_count`, `ror_id_aff_rank`, `primary_aff_basis`, `former_flag`, and `other_ror_ids`. The slim `editors_ft50_current.csv` also gains `ror_id`, `ror_name`, `ror_country`, and `continent`. The board columns are no longer the last two. A single `board_urls` entry may now appear on any journal.

**ROR.** The collector blanks a ROR id when the masthead text cannot be matched to one organization without guessing (strict matching, multi-affiliation parsing, campus splits). So `ror_id` coverage is lower than in `editors_browser_single_20261029` on every panel except ajg2, and a few correct ids were blanked as ambiguous. Nothing was invented. Display affiliation is still `ror_name`, then `canonical_name`, then `raw_affiliation`; country is `ror_country`.

**Directory guardrails kept.** The twelve ajg1 navigation rows (including Vincent Pan on Advances in Decision Sciences) and the two ajg2 Policy Design and Practice navigation rows stay out. Collector institution-string rewrites that were wrong (for example Tokyo mastheads rewritten to `Italian Cultural Institute`, and HKUST (Guangzhou) collapsed onto HKUST) are reverted to the published text: 95 rows plus two `editor_name_raw` restores, listed in `DIRECTORY_GUARDRAILS_restored_rows_20261101.csv`. `11KBW`, UNSW Sydney, and INSEAD stay, with INSEAD France `00ghzk478` and Singapore `05ynf4333` separate; ESSEC is France `02dga6j42`. A blank or country-only affiliation is not an institution. Emails and phone or fax numbers that the collector left in text cells (mostly `source_note`) were removed.

**Directory.** Appointments 162,575 (were 160,104). Editors 112,718 (were 111,229). Journals 2,853. Institutions 16,283 rows, 6,381 with a ROR id (were 11,344 / 8,665). 11,972 appointments have no institution; 650 country-only, 12 bracket-only, and 7 address-only appointments stay off Institutions. Countries 159 (were 175).

| File | Rows (was) | `ror_id` (was) |
|---|---:|---:|
| `editors_ft50_current.csv` | 10,047 (10,046) | 9,600 (no column) |
| `editors_ft50_current_with_ror.csv` | 10,047 (10,046) | 9,673 (9,864) |

Two Review of Economic Studies rows whose `editor_name` was `Universitat Pompeu Fabra` are dropped (the collector removed them from ABDC A* only). Three Top 5 seats the collector added only to ABDC A* (`t39_final15_fix_20261030`: American Economic Review Erik Snowberg and Juan Carlos Suárez Serrato; Review of Economic Studies Mikkel Plagborg-Moller) are copied into both FT50 files, tagged `top5_ft50_align_20261101` in `ror_notes`, so every Top 5 seat is an FT50 seat. Their long-table rows are the A* ones. Empty `editor_name` is 1. `faculty_profile_url` stays 8,375. Contact text removed from 625 / 626 cells.

## Previous freeze: editors_browser_single_20261029

Frozen 2026-10-30 07:09 Asia/Taipei. This supersedes `editors_single_editor_20261029` (Directory PR #39). The collector added browser-captured boards on three ABDC journals: Journal of Derivatives (A, 1 to 18), Journal of Portfolio Management (A, 1 to 73), and Arts and the Market (C, 1 to 55). Both FT50 files are unchanged in this publish. The collector copies are byte-identical to `editors_single_editor_20261029`. See `data/editors/abdc/releases/current/RELEASE_NOTES.md`.

Directory appointments are 160,104, were 159,961. Editors are 111,229, were 111,154. Journals stay 2,853. Institutions are 11,344 rows (8,665 with a ROR id), were 11,276 (8,663). 12,307 appointments have no institution. 642 country-only, 3 bracket-only, and 5 street, PO Box, or postal-code appointments stay off that page. `11KBW`, UNSW Sydney, and INSEAD stay. Twelve ajg1 navigation rows stay out, including Vincent Pan on Advances in Decision Sciences.

## Previous freeze: editors_single_editor_20261029

Fuller boards on ABDC A, ABDC B, ABDC C, and AJG 1, including the five browser-board replacements carried in this freeze. Frozen 2026-10-29 23:18 Asia/Taipei. This supersedes `editors_browser_boards_20261029`. Both FT50 files stay 10,046 rows. The only change on these two files is two trailing columns, `board_urls` and `board_url_count`, and both are blank on every FT50 row. Empty `editor_name` is 1. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

`board_urls` is a pipe-separated list of public board-page URLs, filled only on multi-page boards in the ABDC and AJG-gap files. `board_url_count` is the number of those URLs. The build selects columns by name and does not write `board_urls` to the site. `source_url` stays the primary board link.

## What this publish changed

The collector freeze replaces heading and navigation rows on five journals and expands fifteen journals that had a single editor row. This publish pins those journals on the ABDC A, ABDC B, ABDC C, and AJG 1 files. By panel that is A 2 rows to 411, B 13 rows to 219, C 12 rows to 309, and ajg1 21 rows to 321. The FT50 files, ABDC A*, prio43, and ajg2 are unchanged apart from the two blank columns. A rematch on a new row uses a ROR id already on these boards, or one exact crosswalk hit (`https://ror.org/04a85ht85`, Galgotias College of Engineering & Technology). No ROR id was invented.

Other rows stay as published in `editors_apjiht_board_fix_20261029`. The collector CSV also rewrote institution strings outside those journals. Those rows stay as published, including Tokyo mastheads that the collector would have replaced with `Italian Cultural Institute`. Twelve ajg1 navigation rows stay out, including Vincent Pan on Advances in Decision Sciences. Small Business International Review stays parked. `11KBW`, UNSW Sydney, and INSEAD stay.

The slim file still has no ROR columns.

| Metric | This publish |
|---|---:|
| Rows | 10,046 |
| Empty `editor_name` | 1 |
| `faculty_profile_url` | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,946 (99.0%) |
| `ror_id` on the ROR file | 9,864 (98.2%) |
| Faculty URL, no `ror_id` | 48 |

The slim file has `raw_affiliation` on 9,942 rows and no ROR columns.

## Publish holds

Two medium hits that name a different organization stay unpublished.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. That id stays off. The masthead is `ESADE Business School`. Country stays Spain.

Jaap Paauwe’s display name stays `Jaap Paauwe`. `editor_name_raw` stays `Jaap Paauwe, Tilburg`.

`canonical_name` values cleared in earlier institution freezes stay clear on rows this publish did not edit. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page. No person name or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments are 159,961, were 158,747. Editors are 111,154, were 110,424. Journals stay 2,853. Countries stay 175. FT50 seats stay 10,044 across 50 journals. Top 5 stays 362. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 11,276 rows (8,663 with a ROR id), were 10,824 (8,662). 12,309 appointments have no institution. 641 appointments are omitted because the affiliation is only a country or territory, were 633. Three are omitted because the affiliation is only a bracketed fragment. Ten are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
