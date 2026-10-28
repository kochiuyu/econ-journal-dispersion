# Editors — ABS/AJG gap

Updated: 2026-10-28 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — name and ROR fields from freeze `editors_name_swap_abdc_ajg_20261028`. This supersedes `editors_name_swap_20261028`. The journal set is still `editors_abs_ajg_gap_20261025`. Fourteen drop-quality chrome rows in the collector live panels stay out.

Current boards for AJG journals that are not already in the FT50 or ABDC editor freezes:

| File | Panel | Rows | Empty `editor_name` | Journals |
|------|--------|-----:|--------------------:|---------:|
| `editors_abs_ajg_gap_prio43_current.csv` | AJG 4*, 4, and 3 | 3,445 | 16 | 46 (9 grade 4, 37 grade 3; no 4* left outside FT50/ABDC) |
| `editors_abs_ajg_gap_ajg2_current.csv` | AJG 2 | 4,984 | 1 | 105 |
| `editors_abs_ajg_gap_ajg1_current.csv` | AJG 1 | 11,226 | 1 | 289 |

Notes: `releases/current/RELEASE_NOTES.md`.

Excluded: collector `raw/`, QC logs, `HANDOFF_WEB.md`, and the `NAME_SWAP_*` / `NAME_ORG_SWAP_*` audit CSVs.

## Scope

One current snapshot, not a multi-year panel. Grades on the public directory come from the journal’s 2024 title in `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`, and they must sit in the panel above. These files do not add FT50 or ABDC badges.

`editor_name` is the name the directory shows. An empty `editor_name` is not listed as a person (18 rows on these files). Seventeen of those have a `ror_id` and are counted on Institutions without counting as editors. Pure institution-as-name is 0. `ror_id` is filled on 15,531 of 15,993 nonempty affiliations (97.1%): ajg1 8,457/8,666 (97.6%), ajg2 4,513/4,670 (96.6%), prio43 2,561/2,657 (96.4%). High or medium confidence only. `faculty_profile_url` is not on these files. The public directory does not display tenure, and it does not publish ORCID, OpenAlex, or RePEc ids. Eight prio43 rows whose name is `Email` stay out of the directory.

The full Academic Journal Guide is still larger than the boards in the directory. Rankings keeps every AJG title.
