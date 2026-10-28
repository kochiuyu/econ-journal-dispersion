# Editors — ABDC

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — current boards by ABDC rating. A* and C include freeze `editors_blank_rescrape_browser_20261028` (supersedes the Taylor & Francis-only browser pass). A and B are still freeze `editors_blank_rescrape_20261028`.

| File | Rating | Rows | Empty `editor_name` |
|------|--------|-----:|--------------------:|
| `editors_abdc_a_star_current.csv` | A* | 25,178 | 0 |
| `editors_abdc_a_current.csv` | A | 45,363 | 0 |
| `editors_abdc_b_current.csv` | B | 42,139 | 0 |
| `editors_abdc_c_current.csv` | C | 26,720 | 0 |

Excluded: `*.before_ror.csv`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Empty `editor_name` is 0. The browser pass replaced Business History (85) and Regional Studies (60) on A*, and on C: Climate Policy (56), Journal of Arts Management Law and Society (37), International Journal of Healthcare Management (35), Journal of Biopharmaceutical Statistics (87), International Journal of Financial Engineering (93), and Journal of Financial Management, Markets and Institutions (21). Junk and non-person rows were dropped. The directory does not list a blank name. A bare country is not an institution. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
