# Editors — ABDC

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — current boards by ABDC rating. Freeze `editors_institution_paren_geo_20261028` (2026-10-28 16:39 Asia/Hong_Kong). It supersedes `editors_institution_nonsense_20261028`. Faculty URLs from `editors_nonft50_url_aff_20261028` stay.

| File | Rating | Rows | Empty `editor_name` | `faculty_profile_url` | `raw_affiliation` |
|------|--------|-----:|--------------------:|----------------------:|------------------:|
| `editors_abdc_a_star_current.csv` | A* | 25,178 | 0 | 12,523 (49.7%) | 23,864 (94.8%) |
| `editors_abdc_a_current.csv` | A | 45,363 | 0 | 6,237 (13.7%) | 43,059 (94.9%) |
| `editors_abdc_b_current.csv` | B | 42,139 | 0 | 3,509 (8.3%) | 39,914 (94.7%) |
| `editors_abdc_c_current.csv` | C | 26,720 | 0 | 1,379 (5.2%) | 24,102 (90.2%) |

Excluded: `*.before_ror.csv`, `*.before_url_aff_nonft50_20261028`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Freeze `editors_institution_paren_geo_20261028` clears residual bad ROR matches, blanks junk parenthetical affiliations, and backfills ROR country and continent. Faculty URL counts stay A* 12,523, A 6,237, B 3,509, and C 1,379. Empty `editor_name` is 0. A faculty URL with no university is 4 on A*, 1 on A, 1 on B, and 0 on C. A faculty URL with no `ror_id` is 74 on A*, 44 on A, 20 on B, and 5 on C. Those are cleared matches, not new URLs. No replacement ROR was invented. The three FT50 holds (University of Goma, EAE Business School, The Citadel Foundation) are held on the A* copy as well. `11KBW` stays on two Public Law rows. UNSW Sydney and INSEAD stay. The directory does not list a blank name. A bare country is not an institution. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
