# Editors — ABDC

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — current boards by ABDC rating, freeze `editors_name_swap_abdc_ajg_20261028` (supersedes `editors_name_swap_20261028`):

| File | Rating | Rows | Empty `editor_name` |
|------|--------|-----:|--------------------:|
| `editors_abdc_a_star_current.csv` | A* | 25,185 | 3 |
| `editors_abdc_a_current.csv` | A | 45,363 | 0 |
| `editors_abdc_b_current.csv` | B | 42,145 | 5 |
| `editors_abdc_c_current.csv` | C | 26,875 | 37 |

Excluded: `*.before_ror.csv`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector `NAME_SWAP_*` audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Pure institution-as-name is 0 on all four files. Forty-five rows still have an empty `editor_name` (A* 3, B 5, C 37). The directory does not list them. Thirty-eight of those have a `ror_id` and count on Institutions without counting as an editor. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
