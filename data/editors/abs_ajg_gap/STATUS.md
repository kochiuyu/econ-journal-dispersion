# Editors — ABS/AJG gap

Updated: 2026-10-26 (Asia/Hong_Kong)

## Release in this repo

`releases/current/` — ROR from freeze `editors_abs_ajg_gap_ror_20261026_bracketfix`. Display names are still freeze `editors_display_names_20261025`, except seven evidenced person-plus-institution splits on the ajg2 board. The journal set and the row filter are still `editors_abs_ajg_gap_20261025`. This supersedes `editors_abs_ajg_gap_ror_20261026_countryfix`.

Current boards for AJG journals that are not already in the FT50 or ABDC editor freezes:

| File | Panel | Rows | Journals in this freeze |
|------|--------|-----:|------------------------:|
| `editors_abs_ajg_gap_prio43_current.csv` | AJG 4*, 4, and 3 | 3,490 | 46 (9 grade 4, 37 grade 3; no 4* left outside FT50/ABDC) |
| `editors_abs_ajg_gap_ajg2_current.csv` | AJG 2 | 5,030 | 105 |
| `editors_abs_ajg_gap_ajg1_current.csv` | AJG 1 | 11,276 | 289 |

Notes: `releases/current/RELEASE_NOTES.md`.

Excluded: collector `raw/`, QC logs, and `HANDOFF_WEB.md`.

## Scope

One current snapshot, not a multi-year panel. Grades on the public directory come from the journal’s 2024 title in `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/abs_ajg_2024.csv`, and they must sit in the panel above. These files do not add FT50 or ABDC badges.

`editor_name` is the cleaned display name. When the name changed, the previous value is `editor_name_raw`. Fourteen live-panel rows that this public freeze already excluded as drop-quality chrome stay out, so the row counts above are unchanged. `faculty_profile_url` is not on these files. Tenure columns are present. `ror_id` is filled on 15,384 of 15,929 nonempty affiliations (96.6%): ajg1 8,400/8,642 (97.2%), ajg2 4,484/4,671 (96.0%), prio43 2,500/2,616 (95.6%). The previous country-fix freeze had 15,386 of 15,950 (96.5%). `raw_affiliation` was not overwritten by the build. The collector blanked 21 bracket, street, and zip affiliations and cleared 2 bad address-to-ROR matches. Bare-country affiliations that remain (ajg1 30, ajg2 42, prio43 25, total 97) stay in the CSV and are omitted from the Institutions page, along with any unmatched cluster that is fully bracketed or only a street, PO Box, or postal code. The public directory does not display tenure, and it does not publish ORCID, OpenAlex, or RePEc ids.

The full Academic Journal Guide is still larger than the boards in the directory. Rankings keeps every AJG title.
