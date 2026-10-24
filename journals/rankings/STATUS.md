# Rankings status

Updated: 2026-10-24

ABS/AJG is the Editor-Collector freeze `rankings_abs_ajg_20261024` under `journals/rankings/abs_ajg/releases/`. Other ranking systems are not in this layer yet. Directory chips are unchanged: FT50, ABDC A*/A/B/C, Top 5, and UTD24 stay on the editor directory. This layer does not add an ABS chip.

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

`site/rankings.html` filters by ranking system, edition year, and rating, and searches by journal title. `python scripts/build_site.py` writes `site/rankings-data.js` from this freeze.
