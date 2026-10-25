# Journal rankings

Rating catalogs. These files are not editorial boards and they are not appointments.

The editor directory is current FT50 and ABDC A*/A/B/C boards, plus AJG-gap boards in `data/editors/abs_ajg_gap/releases/current/`. Top 5 and UTD24 are tags on the FT50 and ABDC boards. AJG chips are the 2024 `rating` from this freeze, joined on catalog ids including non-primary crosswalk ids, where the journal is already on an FT50 or ABDC board. That join does not add a board. Gap rows take the same 2024 grade from the journal title, and only for journals that are not already in those editor files. The label does not include the year. Titles that still have no board, and the rest of the guide, stay on the Rankings page. This folder is still the ABS/AJG rankings layer. The public grades page is `site/rankings.html`.

That page also lists CNRS and Handelsblatt/VWL from the freezes below, and FT50, UTD24, Top 5, and ABDC from the catalogs in `journals/`. Those catalogs are not copied here. ABDC ratings are the catalog file (A*, A, B, C). FT50, UTD24, and Top 5 have no grade column and no field. The Field column is ABS/AJG `field`, the CNRS domain, or ABDC `field_for`. Handelsblatt/VWL shows the published weight.

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

## Other pinned releases

`cnrs/releases/rankings_cnrs_20261024/`

CNRS Section 37 categories for 2011–2015 and 2017–2020. Ratings are `1`, `1e`, `1g`, `1eg`, `2`, `3`, `4`. `field` is the domain code. Raw PDFs are not in this repository.

`handelsblatt_vwl/releases/rankings_handelsblatt_vwl_20261024/`

Forschungsmonitoring VWL weights for 1998–2020, plus the 2015 Handelsblatt journal list. `weight` is the published continuous value. `rating` is the letter class when the freeze has one, and blank on the 2015 PDF rows. Raw xlsx and PDFs are not in this repository.

`python scripts/build_site.py` runs `scripts/build_rankings.py`, which reads these freezes and `journals/catalog_ft50.csv`, `catalog_utd24.csv`, `catalog_top5.csv`, and `catalog_abdc_{a_star,a,b,c}.csv`, then writes `site/rankings-data.js`. That file is generated and is not committed. The Pages workflow already runs `scripts/build_site.py`.

| System | Rows |
|--------|------|
| ABS/AJG | 7,245 (five editions) |
| CNRS | 7,361 (nine editions) |
| Handelsblatt/VWL | 42,478 (1998–2020) |
| FT50 | 50 (April 2026 list, no grades) |
| UTD24 | 24 (no grades) |
| Top 5 | 5 (no grades) |
| ABDC | 2,651 (A* 219, A 630, B 861, C 941; 2025 list) |
