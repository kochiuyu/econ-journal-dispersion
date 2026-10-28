# Editors — ABDC

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — current boards by ABDC rating. Freeze `editors_institution_residual_junk_20261028` (2026-10-28 19:29 Asia/Hong_Kong). It supersedes `editors_institution_problem_list_20261028` for Directory Institutions. Faculty URLs from `editors_nonft50_url_aff_20261028` stay.

| File | Rating | Rows | Empty `editor_name` | `faculty_profile_url` | `raw_affiliation` |
|------|--------|-----:|--------------------:|----------------------:|------------------:|
| `editors_abdc_a_star_current.csv` | A* | 25,178 | 0 | 12,523 (49.7%) | 23,847 (94.7%) |
| `editors_abdc_a_current.csv` | A | 45,363 | 0 | 6,237 (13.7%) | 43,013 (94.8%) |
| `editors_abdc_b_current.csv` | B | 42,139 | 0 | 3,509 (8.3%) | 39,866 (94.6%) |
| `editors_abdc_c_current.csv` | C | 26,720 | 0 | 1,379 (5.2%) | 23,969 (89.7%) |

Excluded: `*.before_ror.csv`, `*.before_url_aff_nonft50_20261028`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Freeze `editors_institution_residual_junk_20261028` strips a leading role or credential, blanks a title or credential used as an institution name, strips decorative double quotes, strips a trailing country from an unmatched masthead string, and clears the `[C]Worthy` ROR on David McCarthy. Faculty URL counts stay A* 12,523, A 6,237, B 3,509, and C 1,379. Empty `editor_name` is 0. A faculty URL with no affiliation string is 3 on A*, 4 on A, 0 on B, and 0 on C. A faculty URL with no `ror_id` is 60 on A*, 40 on A, 19 on B, and 4 on C. No replacement ROR was invented. University of Goma and EAE Business School stay held on the A* copy of the Journal of Marketing Research seats. Tom P. Moliterno uses the Citadel ROR already on these boards. Where this freeze blanked or shortened `raw_affiliation` and left no `ror_name`, `canonical_name` still held the old string, and the directory reads `canonical_name` before `raw_affiliation`, so that copy was cleared (A* 1, A 6, B 11, C 32). Hengeler Mueller stays as the firm name. Dunarea de Jos and Tribhuvan Sahkari lose decorative quotes. `11KBW` stays on two Public Law rows. UNSW Sydney and INSEAD stay. The directory does not list a blank name. A bare country is not an institution. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
