# Journal rankings

Rating catalogs. These files are not editorial boards and they are not appointments.

The editor directory chips (FT50, ABDC A*/A/B/C, Top 5, UTD24) stay on the directory. This folder is the rankings layer. The public page is `site/rankings.html`.

More ranking systems can be added later. ABS/AJG is the first one.

## Pinned release

`abs_ajg/releases/rankings_abs_ajg_20261024/`

CABS Academic Journal Guide grades via the Editor-Collector freeze `rankings_abs_ajg_20261024`. Raw portal extracts are not in this repository. Provenance, row counts, and the unmatched list are in that directory’s `RELEASE_NOTES.md`. A short public summary is `STATUS.md`.

| File | Role |
|------|------|
| `abs_ajg_{2010,2015,2018,2021,2024}.csv` | One edition each |
| `abs_ajg_long.csv` | The same rows stacked |
| `journal_id_crosswalk.csv` | Every catalog hit, including non-primary ids |
| `unmatched_journals.csv` | Rows with no `journal_id` |
| `conflicts.csv` | Empty in this freeze |
| `RELEASE_NOTES.md` | Freeze notes |

Grade columns:

`edition_year`, `rating`, `rating_raw`, `journal_title`, `print_issn`, `e_issn`, `field`, `publisher`, `journal_id`, `catalog`, `match_method`, `source_file`, `source_note`

`rating` is `4*`, `4`, `3`, `2`, or `1`. ABS 2010 has no `4*`. `journal_id` is empty when `match_method` is `unmatched`.

## Build

`python scripts/build_site.py` runs `scripts/build_rankings.py`, which reads this freeze and writes `site/rankings-data.js`. That file is generated and is not committed. The Pages workflow already runs `scripts/build_site.py`.
