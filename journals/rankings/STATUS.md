# Rankings status

Updated: 2026-10-24

ABS/AJG is the Editor-Collector freeze `rankings_abs_ajg_20261024` under `journals/rankings/abs_ajg/releases/`. CNRS is `rankings_cnrs_20261024` (7,361 rows; ratings 1, 1e, 1g, 1eg, 2, 3, 4; years 2011–2015 and 2017–2020; domain in `field`). Handelsblatt/VWL is `rankings_handelsblatt_vwl_20261024` (42,478 rows; years 1998–2020; continuous `weight`; letter class when present). The Rankings page also reads the membership catalogs already in `journals/`: FT50 (50, April 2026 list), UTD24 (24), Top 5 (5), and ABDC A*/A/B/C (219 / 630 / 861 / 941, the 2025 list). Those four catalogs are not copied into this folder. FT50, UTD24, and Top 5 have no grades. The editor directory uses the 2024 `rating` from this freeze, including crosswalk ids, as AJG 4* / 4 / 3 / 2 / 1 chips on current FT50 and ABDC board rows. About 1,356 journals can show a chip. The 445 unmatched 2024 titles, and a small set of mapped titles that are not on those boards, do not. Many ABDC board journals have no AJG grade (about 2,400 board journal ids). Earlier editions are not directory chips. ABDC chip names are unchanged. Raw PDFs and xlsx are not committed.

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

`site/rankings.html` filters by ranking system, edition, rating, and field, and searches by journal title. ABDC uses one system and the rating filter A* / A / B / C. The field filter lists subjects on the selected edition (ABS/AJG `field`, CNRS domain, ABDC `field_for`). Handelsblatt/VWL adds a Weight column. FT50, UTD24, and Top 5 leave rating and field empty. The directory field filter uses the same ABDC `field_for` strings. `python scripts/build_site.py` writes `site/rankings-data.js` from these freezes and those catalogs, and tags the 2024 AJG grade on the directory from `abs_ajg_2024.csv` plus the 2024 crosswalk.

| System | Rows |
|--------|------|
| ABS/AJG | 7,245 |
| CNRS | 7,361 |
| Handelsblatt/VWL | 42,478 |
| FT50 | 50 |
| UTD24 | 24 |
| Top 5 | 5 |
| ABDC | 2,651 |
