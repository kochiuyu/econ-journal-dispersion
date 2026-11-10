# editors_post_fullreview_fix_20261111 (built 2026-11-11, Asia/Taipei; UNPUBLISHED)

Base: `releases/editors_full_review_resolved_fix_20261111` (live via PR #54). Keyed on editor_row_key; FT50 twins edited only when both print the same raw.
Script: `abs_ajg/scripts/post_fullreview_fix_20261111.py` (copy here).

## Answers (/workspace/collector_answers_20261111)
- (a) a_campus_merge_77: 76 rows kept as is. FT50 #4634 rechecked on the live board page
  https://www.jom-hub.com/team (fetched 2026-11-11). It prints two X. Zhaos:
  Associate Editors "X. Zhao, China Europe Intl. Bus. School (CEIBS), China" (= #4501) and
  Editorial Review Board "X. Zhao, Xi'an Jiaotong University, China" (= #4634).
  ft50_current_with_ror#4634 already matched (Xi'an Jiaotong 017zhmm22), so it was left unchanged. ft50_current#4634 was set to the printed text:
  raw "Xi'an Jiaotong University, China", ROR 017zhmm22, China (approved raw correction from the board page; long table synced).
  Note: with_ror#4634 faculty_profile_url points to a CEIBS page, which probably belongs to the other X. Zhao. Not changed.
- (b) 38 RENAMEs applied (34 rows plus 4 FT50 mirrors). RORs come from the API, or name and country only for Brescia University College, Leicester Vaughan College,
  First Liberty Institute and Mississippi Christian University x2. Country fixes: Turku -> Finland, Tel Aviv-Yafo -> Israel, Guam, Perugia -> Italy, MIT x3 -> United States.
  6 KEEP_AS_IS rows untouched, including the 3 UNSW degree strings.
- (c) Mercer School of Law -> 04bk7v425; ajg2#5061 -> CTU Prague 03kqpb082; abdc_b#34077 -> CY Cergy 043htjv09 (not ILEPS #37176). All are active in the API.
- (d) APPROVED PILOT SCRUB: faculty_profile_url blanked on `editors_abdc_a_current_with_profile_pilot#15779` (Helena Skyt Nielsen; the cell held an email).
  This is the only pilot cell changed. The abdc_b pilot is byte-identical. The pilot stays unpublished.

## Residuals (/workspace/institutions_post_fullreview_residual_20261111.csv, 982 rows)
Counts confirmed: BIO_OR_MULTI_ORG 24, HELD_COIN_FLIP 199, MISSING_COUNTRY 244, MISSING_ROR 306, NEAR_DUPLICATE 138, NON_INSTITUTION 51, NON_LATIN 1, WRONG_COUNTRY 14, WRONG_ROR 5.
Institutions applied / expected:
- WRONG_ROR 5/5 (386 rows). Each old record is inactive and names the successor; each successor is active.
  UniSA and Adelaide -> Adelaide University 028g18b61; TEI Piraeus -> University of West Attica 00r2r5k05;
  UPMC -> Sorbonne Université 02en5vm52; Rennes 1 -> Université de Rennes 015m7wh34.
  Pilot rows keep the old IDs because pilots are untouched.
- NEAR_DUPLICATE 101/138 (215 rows). 37 not applied:
  - 12 low-confidence;
  - Max Planck x3 and the CNRS multi-org strings x2;
  - 4 non-Latin;
  - 4 two-organisation strings;
  - IIIT Raichur, Monash China, Concordia U. CA, Pacifico, Naples, UT system, Linklaters London, FLACSO x2;
  - the Rotterdam cycle (applied one way only);
  - 3 rows already fixed by (c).
- MISSING_ROR 298/306 (421 rows incl. FT50 mirrors). Each one is active in the API, matches by name or alias, and agrees on country.
  - Low-confidence: Telethon Kids -> The Kids Research Institute Australia and Mercy College -> Mercy University applied (API alias matches). SRH Berlin, Nutraceutical, Bank of the West and University of Africa were not applied.
  - Printed country disagreed with the ROR country: Niagara (Canada), Emden/Leer (Poland), West Ukrainian NU (Poland), Univ. of Finance and Economics (China vs Mongolia), plus single rows of Korn Ferry, P&G, AstraZeneca and CIMMYT.
- WRONG_COUNTRY 7/14 applied in full, 5 partly (11 rows).
  - Multi-office organisations keep the office country printed in the text: Emerald x8 rows, IFPRI Egypt, Putnam France, IMD Singapore.
  - Not applied: Creative New Zealand (the raw reads "Creative Capital, New York", so the name is wrong) and St. Catharine's (coin-flip).
- NON_INSTITUTION 18/51 (9 Marks DROPs, 14 RENAME rows; Reed College gets 00a6ram87).
  - 25 rows already fixed by answer (b).
  - 2 protected UNSW credential strings.
  - 4 rows whose printed raw names an organisation are not dropped: #39063, #18771, #18673, and #9281 (printed "Ph.D. Nova Southeastern University ... KU Leuven, Leuven, Belgium").
- MISSING_COUNTRY 11/244 (12 rows). A country was set only where the printed text or the row's ROR record gives one. 276 rows have no such evidence and were left blank.
- BIO_OR_MULTI_ORG 0/24: the file gives no targets, so these were left as printed. HELD_COIN_FLIP 199 and NON_LATIN 1 were untouched.

New RORs (all API-verified): 269. See POST_FULLREVIEW_new_rors_20261111.csv.
New country values: Guam, New Caledonia.

## Directory (Web build on a copy)
before 11,330 institutions / 6,396 with ROR / 6,396 distinct / 167 countries / 46 shared names (reproduced)
after  11,213 / 6,692 / 6,692 / 169 / 44. Appointments without an institution: 13,404 -> 13,413.
Web's shared-name guard constant must change from 46 to 44.

## QC: ok
- Row counts, headers and line endings unchanged. Long table 269,545 rows. AJG1 12,326 rows, with the 10 nav rows untouched. AJG2 5,462 rows; FT50 10,049/10,049.
- No unexpected panel or long diffs. The only raw edits are Marks DROPs and #4634.
- 0 invented RORs. Protected rows unchanged (11KBW, UNSW, INSEAD FR/SG). No non-Latin names lost; no near-miss pairs merged. Working panels identical.
- Changed rows are all in sync between panels and the long table. Full-table desyncs fell from 1,038 to 885.
- 0 emails or phones. Pilot: one cell changed (#15779 faculty_profile_url), and no emails remain in the pilot.
