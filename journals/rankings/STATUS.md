# Rankings status

Updated: 2026-10-25

ABS/AJG is the Editor-Collector freeze `rankings_abs_ajg_20261024` under `journals/rankings/abs_ajg/releases/`. CNRS is `rankings_cnrs_20261024` (7,361 rows; ratings 1, 1e, 1g, 1eg, 2, 3, 4; years 2011–2015 and 2017–2020; domain in `field`). Handelsblatt/VWL is `rankings_handelsblatt_vwl_20261024` (42,478 rows; years 1998–2020; continuous `weight`; letter class when present). The Rankings page also reads the membership catalogs already in `journals/`: FT50 (50, April 2026 list), UTD24 (24), Top 5 (5), and ABDC A*/A/B/C (219 / 630 / 861 / 941, the 2025 list). Those four catalogs are not copied into this folder. FT50, UTD24, and Top 5 have no grades. FT50 `field` is the subject area printed on the McMaster LibGuide at https://libguides.mcmaster.ca/ft-top50 (the April 2026 list on that page). A cell that prints two subjects keeps both, comma-separated, in one field. UTD24 and Top 5 still have no field. The editor directory uses the 2024 `rating` from this freeze, including crosswalk ids, as AJG 4* / 4 / 3 / 2 / 1 chips. About 1,356 of the 1,378 mapped titles sit on an FT50 or ABDC board and show a chip from that id join. The 445 unmatched 2024 titles have no catalog id, so the join does not tag them. Many ABDC board journals have no AJG grade (about 2,400 board journal ids). AJG-gap boards (`data/editors/abs_ajg_gap/releases/current/`, freeze `editors_abs_ajg_gap_20261025`) add journals that are not already in those editor files and take the same 2024 grade from the title. The directory then shows a chip on 1,796 journals. 27 titles in the 2024 guide still have no board. Earlier editions are not directory chips. This folder is still the full guide. ABDC chip names are unchanged. Raw PDFs and xlsx are not committed.

These files are journal grades. They are not mastheads. Raw CABS portal extracts (`/workspace/abs-ajg/`) are not committed.

## Editions

Grades and ids are the freeze’s. Nothing here was re-rated. `conflicts.csv` has no data rows.

| Edition | Journals | With `journal_id` | Match | Unmatched |
|---------|----------|-------------------|-------|-----------|
| 2010 | 794 | 721 | 90.8% | 73 (9.2%) |
| 2015 | 1,377 | 1,120 | 81.3% | 257 (18.7%) |
| 2018 | 1,545 | 1,231 | 79.7% | 314 (20.3%) |
| 2021 | 1,706 | 1,317 | 77.2% | 389 (22.8%) |
| 2024 | 1,823 | 1,378 | 75.6% | 445 (24.4%) |

Long panel: 7,245 rows. Unmatched row-years: 1,478 (20.4%). Match methods on the long panel: `issn` 5,736, `title` 31, `unmatched` 1,478.

2010 is the ABS guide (`source_note` `ABS2010`, grades 1–4). 2015–2024 are AJG and include `4*`.

## Page

Tilburg/TISEM is `rankings_tilburg_20261025` (179 journals; tiers Top-core 42, Top 41, Very good 96; 164 matched, 91.6%). The public page does not publish a good tier, and the TiU Econtop database is not joined. FNEGE is `rankings_fnege_20261025` (2,044 rows; 2019, 2022, and 2025; grades 1*, 1, 2, 3, 4, plus EM and NC when printed). 2025 has 891 journals, 733 matched (82.3%). ERIM Core is `rankings_erim_20261025` (283 journals; edition 2024–2028; classes STAR, M-STAR, P, EP*, PA, S, S (3=1), and M; 257 matched, 90.8%). NYU Stern Economics is `rankings_stern_20261025` (49 journals; edition 2020; tiers Top 5, Really excellent, Field, and Review; 47 matched, 95.9%). ShanghaiRanking is `rankings_shanghai_20261025` (76 rows; 2024 and 2026; rating Top; subjects Economics, Business Administration, Finance, and Management). 2026 has 19 journals, all matched. These lists are Rankings rows only. They do not add directory chips. Raw HTML, xlsx, and PDFs are not committed.

`site/rankings.html` filters by ranking system, edition, rating, and field, and searches by journal title. ABDC uses one system and the rating filter A* / A / B / C. The field filter lists subjects on the selected edition (ABS/AJG `field`, CNRS domain, ABDC `field_for`, FNEGE domain, ERIM track, the TISEM very-good group, the Stern field heading, the Shanghai subject, or the FT50 McMaster subject area). Handelsblatt/VWL adds a Weight column. FT50, UTD24, and Top 5 leave rating empty. FT50 fills field from that LibGuide. UTD24 and Top 5 leave field empty. The directory field filter uses the same ABDC `field_for` strings. `python scripts/build_site.py` writes `site/rankings-data.js` from these freezes and those catalogs, and tags the 2024 AJG grade on the directory from `abs_ajg_2024.csv` plus the 2024 crosswalk.

| System | Rows |
|--------|------|
| ABS/AJG | 7,245 |
| CNRS | 7,361 |
| Handelsblatt/VWL | 42,478 |
| FT50 | 50 |
| UTD24 | 24 |
| Top 5 | 5 |
| ABDC | 2,651 |
| Tilburg | 179 |
| FNEGE | 2,044 |
| ERIM | 283 |
| Stern | 49 |
| Shanghai | 76 |
