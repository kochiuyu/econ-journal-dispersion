# Editors — ABS/AJG gap

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — name and ROR fields from freeze `editors_name_swap_20261028`. This supersedes `editors_abs_ajg_gap_ror_20261026_bracketfix` for the cells that freeze changed. The journal set and the row filter are still `editors_abs_ajg_gap_20261025`. Fourteen drop-quality chrome rows in the collector live panels stay out.

Current boards for AJG journals that are not already in the FT50 or ABDC editor freezes:

| File | Panel | Rows | Empty `editor_name` | Journals in this freeze |
|------|--------|-----:|--------------------:|------------------------:|
| `editors_abs_ajg_gap_prio43_current.csv` | AJG 4*, 4, and 3 | 3,490 | 22 | 46 (9 grade 4, 37 grade 3; no 4* left outside FT50/ABDC) |
| `editors_abs_ajg_gap_ajg2_current.csv` | AJG 2 | 5,030 | 41 | 105 |
| `editors_abs_ajg_gap_ajg1_current.csv` | AJG 1 | 11,276 | 24 | 289 |

Notes: `releases/current/RELEASE_NOTES.md`.

Excluded: collector `raw/`, QC logs, `HANDOFF_WEB.md`, and the `NAME_SWAP_*` / `NAME_ORG_SWAP_*` audit CSVs.

## Scope

One current snapshot, not a multi-year panel. Grades on the public directory come from the journal’s 2024 title in `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`, and they must sit in the panel above. These files do not add FT50 or ABDC badges.

`editor_name` is the name the directory shows. An empty `editor_name` is not listed as a person (87 rows on these files). Sixty of those have a `ror_id` and are counted on Institutions without counting as editors. `ror_id` is filled on 15,438 of 15,959 nonempty affiliations (96.7%): ajg1 8,426/8,654 (97.4%), ajg2 4,488/4,671 (96.1%), prio43 2,524/2,634 (95.8%). High or medium confidence only. `faculty_profile_url` is not on these files. The public directory does not display tenure, and it does not publish ORCID, OpenAlex, or RePEc ids. Eight prio43 rows whose name is `Email` stay out of the directory.

The full Academic Journal Guide is still larger than the boards in the directory. Rankings keeps every AJG title.
