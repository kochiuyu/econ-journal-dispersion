# Editors — ABDC

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — current boards by ABDC rating. Freeze `editors_institution_junk_cleanup_20261028` (2026-10-28 17:48 Asia/Hong_Kong). It supersedes `editors_institution_paren_geo_20261028`. Faculty URLs from `editors_nonft50_url_aff_20261028` stay.

| File | Rating | Rows | Empty `editor_name` | `faculty_profile_url` | `raw_affiliation` |
|------|--------|-----:|--------------------:|----------------------:|------------------:|
| `editors_abdc_a_star_current.csv` | A* | 25,178 | 0 | 12,523 (49.7%) | 23,861 (94.8%) |
| `editors_abdc_a_current.csv` | A | 45,363 | 0 | 6,237 (13.7%) | 43,057 (94.9%) |
| `editors_abdc_b_current.csv` | B | 42,139 | 0 | 3,509 (8.3%) | 39,903 (94.7%) |
| `editors_abdc_c_current.csv` | C | 26,720 | 0 | 1,379 (5.2%) | 24,085 (90.1%) |

Excluded: `*.before_ror.csv`, `*.before_url_aff_nonft50_20261028`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Freeze `editors_institution_junk_cleanup_20261028` blanks evidenced junk in the institution field and clears digit-leading ROR ids that name a different organization. 33 rows lose `raw_affiliation`. 11 rows lose a digit-leading `ror_id` (10 keep the affiliation text, and Lee H. Rosenthal on the University of Chicago Law Review was already blank). Faculty URL counts stay A* 12,523, A 6,237, B 3,509, and C 1,379. Empty `editor_name` is 0. A faculty URL with no university is 4 on A*, 1 on A, 1 on B, and 0 on C. A faculty URL with no `ror_id` is 74 on A*, 44 on A, 20 on B, and 5 on C. No replacement ROR was invented. The three FT50 holds (University of Goma, EAE Business School, The Citadel Foundation) stay held on the A* copy. Where this freeze blanked `raw_affiliation`, `canonical_name` was the same string, and the directory reads `canonical_name` when `ror_name` is empty, so that copy was cleared too. `11KBW` stays on two Public Law rows. UNSW Sydney and INSEAD stay. The directory does not list a blank name. A bare country is not an institution. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
