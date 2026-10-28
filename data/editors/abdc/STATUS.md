# Editors — ABDC

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — current boards by ABDC rating. Freeze `editors_nonft50_url_aff_20261028` (2026-10-28 13:07 Asia/Hong_Kong).

| File | Rating | Rows | Empty `editor_name` | `faculty_profile_url` | `raw_affiliation` |
|------|--------|-----:|--------------------:|----------------------:|------------------:|
| `editors_abdc_a_star_current.csv` | A* | 25,178 | 0 | 12,523 (49.7%) | 23,881 (94.8%) |
| `editors_abdc_a_current.csv` | A | 45,363 | 0 | 6,237 (13.7%) | 43,401 (95.7%) |
| `editors_abdc_b_current.csv` | B | 42,139 | 0 | 3,509 (8.3%) | 40,020 (95.0%) |
| `editors_abdc_c_current.csv` | C | 26,720 | 0 | 1,379 (5.2%) | 24,306 (91.0%) |

Excluded: `*.before_ror.csv`, `*.before_url_aff_nonft50_20261028`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Freeze `editors_nonft50_url_aff_20261028` fills `raw_affiliation` and ROR where a faculty profile URL already identified the institution, clears junk non-person URLs, and applies unused high/medium faculty-cache URLs keyed by name and ROR. Empty `editor_name` is 0. A faculty URL with no university is 0 (was 47). A faculty URL with no `ror_id` is 0 (was 50). Faculty URL rows are A* 8,467→12,523, A 5,202→6,237, B 3,123→3,509, and C 1,228→1,379. The directory does not list a blank name. A bare country is not an institution. No name, ROR id, affiliation, or faculty URL was invented. FT50 and AJG-gap panels are not part of this freeze. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
