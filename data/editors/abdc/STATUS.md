# Editors — ABDC

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — current boards by ABDC rating:

| File | Rating | This freeze |
|------|--------|-------------|
| `editors_abdc_a_star_current.csv` | A* | `editors_name_swap_20261028` (25,188 rows) |
| `editors_abdc_a_current.csv` | A | `editors_name_swap_20261028` (45,363 rows) |
| `editors_abdc_b_current.csv` | B | unchanged, `editors_display_names_20261025` |
| `editors_abdc_c_current.csv` | C | unchanged, `editors_display_names_20261025` |

Excluded: `*.before_ror.csv`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Freeze `editors_name_swap_20261028` updates names and institutions on A* and A. It drops the Review of Economic Studies rows whose name was `CEMFI` or `Sciences Po`, sets Kurt Mitman to CEMFI with ROR `https://ror.org/035h6g182` (high), and blanks two A* org-as-name rows. A third A* row, Regional Studies `GREThA`, was already an empty `editor_name`. A has four evidenced person-plus-institution splits and no empty `editor_name`. The directory does not list an empty name. These empty A* rows have no `ror_id`, so they are not institution appointments. See `releases/current/RELEASE_NOTES.md`.

B and C keep `editor_name` from `editors_display_names_20261025`. Faculty columns, tenure columns, and `ror_id` on B and C were not edited.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
