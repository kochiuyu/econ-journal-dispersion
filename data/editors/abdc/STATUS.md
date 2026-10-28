# Editors — ABDC

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — current boards by ABDC rating. Freeze `editors_institution_post31_touchup_20261028` (2026-10-28 20:04 Asia/Hong_Kong). It supersedes `editors_institution_residual_junk_20261028` for Directory Institutions. Faculty URLs from `editors_nonft50_url_aff_20261028` stay.

| File | Rating | Rows | Empty `editor_name` | `faculty_profile_url` | `raw_affiliation` |
|------|--------|-----:|--------------------:|----------------------:|------------------:|
| `editors_abdc_a_star_current.csv` | A* | 25,178 | 2 | 12,523 (49.7%) | 23,847 (94.7%) |
| `editors_abdc_a_current.csv` | A | 45,363 | 1 | 6,237 (13.7%) | 42,907 (94.6%) |
| `editors_abdc_b_current.csv` | B | 42,139 | 0 | 3,509 (8.3%) | 39,866 (94.6%) |
| `editors_abdc_c_current.csv` | C | 26,720 | 11 | 1,379 (5.2%) | 23,968 (89.7%) |

Excluded: `*.before_ror.csv`, `*.before_url_aff_nonft50_20261028`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Freeze `editors_institution_post31_touchup_20261028` blanks navigation chrome, blanks `View full biography` used as an institution, clears the Aberdeen Regional Hospital ROR, and rematches Binam Ghimire to Robert Gordon University (`https://ror.org/04f0qj703`, United Kingdom) because the masthead already names that university. Faculty URL counts stay A* 12,523, A 6,237, B 3,509, and C 1,379. Empty `editor_name` is 2 on A*, 1 on A, 0 on B, and 11 on C. A faculty URL with no `ror_id` is 60 on A*, 40 on A, 19 on B, and 4 on C. No replacement ROR was invented. University of Goma and EAE Business School stay held on the A* copy of the Journal of Marketing Research seats. Tom P. Moliterno uses the Citadel ROR already on these boards. Where this freeze blanked the institution and left no `ror_name`, `canonical_name` was cleared (A* 2, A 119, C 1). Hengeler Mueller stays as the firm name. Dunarea de Jos and Tribhuvan Sahkari stay without decorative quotes. `11KBW` stays on two Public Law rows. UNSW Sydney and INSEAD stay. The directory does not list a blank name. A bare country is not an institution. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
