# Editors — ABDC

Updated: 2026-10-25 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — ROR-enriched current boards by ABDC rating:

| File | Rating |
|------|--------|
| `editors_abdc_a_star_current.csv` | A* |
| `editors_abdc_a_current.csv` | A |
| `editors_abdc_b_current.csv` | B |
| `editors_abdc_c_current.csv` | C |

Excluded: `*.before_ror.csv`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Freeze `editors_display_names_20261025`: `editor_name` is the cleaned display name. When the name changed, the previous value is `editor_name_raw`. Faculty columns (`faculty_profile_url`, `faculty_home_page`, `faculty_match_method`, `faculty_match_confidence`, `faculty_person_key`), tenure columns, and `ror_id` are still the `editors_current_20261025` values. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
