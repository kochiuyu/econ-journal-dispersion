# Editors — ABDC

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — current boards by ABDC rating, freeze `editors_blank_rescrape_20261028` (supersedes the blank names in `editors_name_swap_abdc_ajg_20261028`):

| File | Rating | Rows | Empty `editor_name` |
|------|--------|-----:|--------------------:|
| `editors_abdc_a_star_current.csv` | A* | 25,182 | 0 |
| `editors_abdc_a_current.csv` | A | 45,363 | 0 |
| `editors_abdc_b_current.csv` | B | 42,139 | 0 |
| `editors_abdc_c_current.csv` | C | 26,858 | 0 |

Excluded: `*.before_ror.csv`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Empty `editor_name` is 0. Negotiation Journal (52), Labour (20), International Journal of Urban and Regional Research (78), Global Business and Organizational Excellence (33), Higher Education Quarterly (46), and South African Journal of Economic and Management Sciences (27) were restored from cached or live HTTP. Residual Taylor & Francis and World Scientific orphans were dropped, not named. The directory does not list a blank name. A bare country is not an institution. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
