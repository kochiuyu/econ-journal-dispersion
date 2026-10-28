# Editors — ABDC

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — current boards by ABDC rating. Freeze `editors_institution_dept_country_20261028` (2026-10-28 22:41 Asia/Hong_Kong). It supersedes `editors_institution_trailing_place_20261028` for Directory Institutions. Faculty URLs from `editors_nonft50_url_aff_20261028` stay.

| File | Rating | Rows | Empty `editor_name` | `faculty_profile_url` | `raw_affiliation` |
|------|--------|-----:|--------------------:|----------------------:|------------------:|
| `editors_abdc_a_star_current.csv` | A* | 25,178 | 2 | 12,523 (49.7%) | 23,806 (94.6%) |
| `editors_abdc_a_current.csv` | A | 45,363 | 2 | 6,237 (13.7%) | 42,776 (94.3%) |
| `editors_abdc_b_current.csv` | B | 42,139 | 0 | 3,509 (8.3%) | 39,777 (94.4%) |
| `editors_abdc_c_current.csv` | C | 26,720 | 11 | 1,379 (5.2%) | 23,846 (89.2%) |

Excluded: `*.before_ror.csv`, `*.before_url_aff_nonft50_20261028`, `abdc/raw/`, scrape queues, `journals_abdc_b_product03.csv`, and the collector audit CSVs.

## Catalogs

`journals/catalog_abdc_{a_star,a,b,c}.csv` from the locked **2025 ABDC Journal Quality List**.

## Notes

Coverage still varies by rating (live scrape / overlap seeding). Treat these as **current-board snapshots**, not a balanced historical panel.

Freeze `editors_institution_dept_country_20261028` strips a department suffix or a country string inside the institution name, and rematches only to a ROR id already on these boards. Sam Kirshner stays UNSW Sydney (`https://ror.org/03r8z3t63`) and Kai Hockerts stays INSEAD (`https://ror.org/05ynf4333`). `Aberdeen University` stays on University of Aberdeen (`https://ror.org/016476m91`, United Kingdom). Faculty URL counts stay A* 12,523, A 6,237, B 3,509, and C 1,379. Empty `editor_name` is 2 on A*, 2 on A, 0 on B, and 11 on C. A faculty URL with no `ror_id` is 67 on A*, 50 on A, 21 on B, and 4 on C. No replacement ROR was invented. University of Goma and EAE Business School stay held on the Journal of Marketing Research seats. Tom P. Moliterno uses the Citadel ROR already on these boards. Where this freeze blanked the institution and left no `ror_name`, `canonical_name` is clear. Hengeler Mueller stays as the firm name. Dunarea de Jos and Tribhuvan Sahkari stay without decorative quotes. `11KBW` stays on two Public Law rows. UNSW Sydney and INSEAD stay. The directory does not list a blank name. A bare country is not an institution. See `releases/current/RELEASE_NOTES.md`.

UTD24’s INFORMS Journal on Computing (`informs_journal_computing`; UTD label “Journal on Computing”) is multi-tagged from the A panel. See `journals/catalog_utd24.csv`. There is no separate UTD24 release.
