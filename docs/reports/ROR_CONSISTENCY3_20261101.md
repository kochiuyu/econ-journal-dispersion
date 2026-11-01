# ROR consistency 3 (2026-11-01) — report

Pack: `releases/editors_ror_consistency3_20261101/` (HELD).

Built 2026-11-01 (Asia/Taipei, UTC+8) from `releases/editors_ror_consistency2_20261031`. That pack and every other existing release are unchanged (md5 checked before and after the build). Nothing has been pushed or published.

## What changed
Foreign-namesake / wrong-organisation ROR ids, per the user decisions of 2026-11-01:
- the six ids named by the user (American University → Nicaragua record, Western University → Cambodia, ENS → Ivory Coast, Heidelberg → Tiffin Ohio, Korea University → Tokyo, China University of Petroleum → Indonesia);
- every other foreign-namesake or wrong-organisation id the cross-check (`reports/rorconsistency3_work/scan_candidates.csv`) found.

Rule: an id is **corrected** only when the right record is unambiguous from the printed text, city or country (active ror.org v2.15 records only, country-consistent). Otherwise it is **blanked** (a blank ROR is better than a wrong one). Where the printed text supports the current record (e.g. "Heidelberg University, Ohio", "Northeastern University, Shenyang", "University of the West Indies, Barbados", "Saint Louis University Madrid", "International Business School, Bulgaria"), the row is kept.

| level | corrected | blanked |
|---|---|---|
| panel `ror_id` (all 11 panels) | 111 | 429 |
| panel `other_ror_ids` tokens | 2 | 3 |
| `editor_affiliations.csv` parts | 113 | 432 |

Rows changed per file: `editor_affiliations.csv` 545; `editors_abdc_a_current.csv` 90; `editors_abdc_a_current_with_profile_pilot.csv` 83; `editors_abdc_a_star_current.csv` 62; `editors_abdc_b_current.csv` 78; `editors_abdc_b_current_with_profile_pilot.csv` 72; `editors_abdc_c_current.csv` 40; `editors_abs_ajg_gap_ajg1_current.csv` 7; `editors_abs_ajg_gap_ajg2_current.csv` 25; `editors_abs_ajg_gap_prio43_current.csv` 16; `editors_ft50_current.csv` 36; `editors_ft50_current_with_ror.csv` 36.
Every other row and every other cell is byte-identical to consistency2 (verified by a row-by-row diff; changed columns are only the ROR block columns listed below).

## Fields written
- Corrected panel row: `ror_id`, `ror_name`, `ror_country`, `continent`, `lat`, `lon` from the new record; `ror_match_method` = `ror_consistency3_20261101`; `ror_match_score` 1.0; `ror_confidence` high/medium (see the changes CSV); `ror_notes` appended with `ror_consistency3_20261101: <reason> (was <old id> <old name> (<old country>))`.
- Blanked panel row: ROR block emptied, `ror_id_aff_rank` emptied, `ror_match_method` = `ror_consistency3_20261101_blanked`, `ror_confidence` = `unmatched`, note appended as above. `canonical_name` (printed institution) is not touched.
- `editors_ft50_current.csv` has only `ror_id`, `ror_name`, `ror_country`, `continent` (+ `ror_id_aff_rank`); only those changed.
- `other_ror_ids`: wrong token replaced or removed (`;` separated, de-duplicated).
- `editor_affiliations.csv`: `ror_id`, `ror_name`, `ror_country`; `ror_match_kind` = `consistency3_fix` / `consistency3_blank` (new values); `ror_match_note`; `is_panel_ror` set to 0 on blanked parts. Panel `ror_id` and the long-table part with `is_panel_ror`=1 agree on every row (checked).
- **Header changes: none.** New `ror_match_method` values `ror_consistency3_20261101` / `ror_consistency3_20261101_blanked` and new `ror_match_kind` values `consistency3_fix` / `consistency3_blank` — flag for Web.

## Changes by wrong record (panel rows, all panels)
| current id (wrong record) | record name (country) | panel rows → new | 
|---|---|---|
| 03awzbc87 | Northeastern University (China) | 91 → blank; 5 → 04t5xt781 Northeastern University |
| 038e47q18 | Universidad Americana (Nicaragua) | 70 → blank; 9 → 052w4zt36 American University |
| 01qxhf360 | Concordia University (United States) | 43 → blank; 2 → 0420zvk78 Concordia University; 1 → 028177t76 Concordia University Texas |
| 05m1gnk07 | Korea University (Japan) | 28 → blank; 7 → 047dqcg40 Korea University |
| 02agqkc58 | Western University (Cambodia) | 34 → blank |
| 04pqpvr75 | Universidad de Los Andes (Bolivia) | 19 → blank; 2 → 02mhbdp94 Universidad de Los Andes |
| 04j757h98 | Victoria University (Australia) | 21 → 0040r6f76 Victoria University of Wellington |
| 04rcqnp59 | Heidelberg University (United States) | 12 → blank |
| 05p4f7w60 | University of the West Indies (Barbados) | 6 → 003kgv736 University of the West Indies; 6 → blank |
| 04wxqpw15 | Court of Appeal (Thailand) | 12 → blank |
| 04bgbsx11 | Jinan University (Lebanon) | 9 → blank; 1 → 02xe5ns62 Jinan University |
| 049rm1a24 | International Finance Corporation (Kazakhstan) | 9 → blank |
| 03z0f3m78 | Universidad del Pacífico (Paraguay) | 6 → blank |
| 04mwhg379 | Notre Dame University (Philippines) | 4 → blank; 2 → 030br0314 Notre Dame University – Louaize |
| 007fpb915 | Universidad Católica Andrés Bello (Venezuela) | 4 → 04teye511 Pontificia Universidad Católica de Chile; 1 → 00013q465 Pontificia Universidad Católica del Perú |
| 04abjgr86 | Sacred Heart University (Luxembourg) | 5 → blank |
| 04xtpyw05 | École Normale Supérieure d'Abidjan (Ivory Coast) | 4 → blank; 1 → 00hx6zz33 École Normale Supérieure Paris-Saclay |
| 04gpw1v92 | European University (North Macedonia) | 2 → 0031wrj91 European University Institute; 2 → 00m04y575 South East European University |
| 02em1tr51 | University of Petroleum (Indonesia) | 3 → blank; 1 → 041qf4r12 China University of Petroleum, Beijing |
| 05hvrsg85 | Food and Drug Administration (Thailand) | 4 → 034xvzb47 United States Food and Drug Administration |
| 034dn0836 | Institute of Psychology (Poland) | 2 → 01ynf4891 University of Milano-Bicocca; 2 → 015h0qg34 Maria Curie-Skłodowska University |
| 02hzmab58 | St. Mary's University (Ethiopia) | 4 → blank |
| 03jzczt57 | International Institute for Strategic Studies (United States) | 4 → blank |
| 02exxtn84 | Amity University (United Arab Emirates) | 4 → blank |
| 00wyq5s37 | St. John's University (Taiwan) | 4 → blank |
| 01e8b7f16 | La Salle University (Philippines) | 3 → blank |
| 01w50jw95 | New England Baptist Hospital (United States) | 3 → 0145fw131 Hong Kong Baptist University |
| 00cf0ab87 | Southeast University (Bangladesh) | 3 → blank |
| 045p44t13 | National Institutes of Health (Malaysia) | 2 → 01cwqze88 National Institutes of Health; 1 → 043z4tv69 National Institute of Allergy and Infectious Diseases |
| 0160prf97 | Edge Foundation (Egypt) | 3 → blank |
| 04jhxpq45 | Universidad Iberoamericana (Paraguay) | 3 → blank |
| 01dfpjy51 | Gulf University (Serbia) | 3 → blank |
| 02n9j6f76 | Universidad Del Pacifico (Colombia) | 3 → 05ma4gw77 University of the Pacific |
| 03dmtvy82 | Department of Commerce (Australia) | 3 → blank |
| 05patbw61 | Individual Differences (United States) | 2 → 02v51f717 Peking University |
| 047wxqh80 | International Christian University (Ukraine) | 2 → 01cg0k189 International Christian University |
| 03aztvx54 | International Organization for Migration (Poland) | 2 → blank |
| 000tee703 | Northeastern State University (Russia) | 2 → 01z7kzb45 Northeastern State University |
| 04smsfy22 | Saint Francis University (United States) | 2 → blank |
| 01my2ss20 | Hult International Business School (United States) | 2 → 01wttbg53 Hult International Business School |
| 02nqj0b62 | Economic Development Board (Singapore) | 2 → blank |
| 052ce7c92 | Population Council (India) | 2 → blank |
| 03j3dbz94 | Trinity College (United States) | 2 → blank |
| 02rv3w387 | Universidade Aberta (Portugal) | 2 → 05mzfcs16 The Open University |
| 00strmv13 | Queens University (Bangladesh) | 2 → blank |
| 01dhcyx48 | Cary Institute of Ecosystem Studies (United States) | 2 → 01gntjh03 Royal Netherlands Institute for Sea Research |
| 00qzjvm58 | Centers for Disease Control and Prevention (Uganda) | 1 → 042twtr12 Centers for Disease Control and Prevention; 1 → blank |
| 02wwrqj12 | Aga Khan University (Tanzania) | 2 → blank |
| 00ssdam06 | The Mount (United Kingdom) | 2 → blank |
| 02h8eme80 | Campbell Collaboration (India) | 2 → blank |
| 05fy98n62 | Columbia College (Canada) | 2 → 00es7k954 Columbia College - South Carolina |
| 019zv8f18 | National Institute of Occupational Safety and Health (Japan) | 2 → 0502a2655 National Institute for Occupational Safety and Health |
| 03bgwd624 | Ministry of Foreign Affairs (South Korea) | 2 → blank |
| 04yzbtf37 | Viện Công nghệ thông tin (Vietnam) | 2 → blank |
| 005jys510 | National Centre for Scientific Research (Angola) | 2 → 02feahw73 Centre National de la Recherche Scientifique |
| 03fkbz285 | Saint Louis University (Spain) | 2 → blank |
| 04yvncj21 | Bucharest University of Economic Studies (Romania) | 2 → 04d26v797 Academy of Economic Studies of Moldova |
| 05dbx6743 | Department of Veterans Affairs (Australia) | 2 → 05rsv9s98 United States Department of Veterans Affairs |
| 0517ce304 | Kingston University (United States) | 2 → blank |
| 00nb5xj61 | St. Andrews University (United States) | 1 → blank |
| 00hh6j532 | National Institute of Child Health (Hungary) | 1 → blank |
| 01913dg57 | École Supérieure Multinationale des Télécommunications (Senegal) | 1 → blank |
| 02bmams93 | St. Thomas University (United States) | 1 → blank |
| 02njbw696 | Universidad Simón Bolívar (Colombia) | 1 → blank |
| 00jkdhd30 | Saint Mary's University (Philippines) | 1 → blank |
| 00xcb0s16 | International Business School (Bulgaria) | 1 → blank |
| 057ewhh68 | Augsburg University (United States) | 1 → 03p14d497 University of Augsburg |
| 01svc3820 | Financial Services Commission (South Korea) | 1 → blank |
| 015bdn754 | Hanalei Watershed Hui (United States) | 1 → blank |
| 019mrv168 | New England Law (United States) | 1 → blank |
| 03qfy7r49 | Carol I National Defence University (Romania) | 1 → 01jepya76 United States Military Academy |
| 02jfryy43 | Ministry of Trade (Türkiye) | 1 → blank |
| 03e0h3d81 | Bansomdejchaopraya Rajabhat University (Thailand) | 1 → 0220mzb33 King's College London |
| 0350h3282 | Universidad del Norte (Mexico) | 1 → 031e6xm45 Universidad del Norte |
| 033pj6j32 | National Institute of Economic Research (Sweden) | 1 → 05rqjcx81 Institutul Național de Cercetări Economice |
| 00xh3h995 | Institute of Agricultural Economics (Bulgaria) | 1 → 00pnht824 Institute of Agricultural Economics Belgrade |
| 03m1s4j75 | Universidad de Oriente (Mexico) | 1 → blank |
| 040aqvh16 | United Nations University (Germany) | 1 → blank |
| 02b58zy88 | Department of Administration (Guam) | 1 → 03zga2b32 University of Bergen |
| 01cyq8n55 | Asia University (Japan) | 1 → blank |
| 001ke5c68 | Department of Agriculture (Belize) | 1 → 01na82s61 United States Department of Agriculture |

## Kept on purpose (not changed here)
- ESSEC → France 02dga6j42 when no campus is printed; Singapore 04be2h179 only where Singapore is printed. CEU stays Austria 02zx40v98 (user decision).
- Category B (ambiguous bare name, current record plausible/dominant), e.g. bare "Victoria University" (Melbourne), "Trinity College, USA" (Hartford), "St. Thomas University, USA".
- Print-error country conflicts of the same organisation (e.g. "University of Alberta, USA") and overseas-campus prints mapped to the home record (Curtin/Swinburne/Monash Malaysia, SKEMA, Georgetown/CMU Qatar …) — open item.
- "Korea University, Tokyo, Japan" (1 long-table part, editors_abs_ajg_gap_ajg2_current) kept on 05m1gnk07 because the printed city matches that record — flagged.

## Files
- the 11 panels and `editor_affiliations.csv` (same names, same headers, LF line endings as consistency2);
- `ROR_CONSISTENCY3_changes_20261101.csv` — one row per change: level, file, row_index, editor_row_key, printed_part, old ror (id/name/country), new ror (id/name/country), action, reason;
- `_build.json` — source and output md5s.

Report: `reports/ROR_CONSISTENCY3_20261101.md`. Rules: `reports/rorconsistency3_work/rules.py`; build: `reports/rorconsistency3_work/apply.py`.

## Method
1. `scan.py` / `scan_run.py`: for every distinct ROR id in consistency2, compared the record's country/city/name to the printed affiliation parts; listed foreign-namesake candidates (`scan_candidates.csv`).
2. Each candidate id was reviewed by hand against ror.org v2.15 (local dump) and given ordered rules (`rules.py`): printed-evidence regex → new id (or blank). First match wins; no match keeps the id. Rules are applied to the long-table printed part (`raw_aff_part`); the panel primary follows its long-table part (`is_panel_ror`=1); full panel text is used only for two ids whose part is a fragment (02b58zy88, 033pj6j32).
3. Every target id was asserted active in the dump. No records were invented.
4. Verification: same headers and row counts as consistency2; only the 1,090 logged rows differ, and only in ROR block columns; panel/long table in sync; all existing releases md5-identical before and after.

## Open items (not changed)
- HQ-type bare names blanked rather than mapped to headquarters (IISS, Population Council, Campbell Collaboration, IOM, IFC, Aga Khan University) — could be mapped to the HQ record if the user prefers.
- Profile-domain evidence was not available for these rows, so campus/country could only come from printed text.
- Country-conflict prints of the same organisation and overseas-campus prints left as built.
