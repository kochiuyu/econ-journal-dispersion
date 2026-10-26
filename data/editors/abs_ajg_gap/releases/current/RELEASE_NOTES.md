# editors_abs_ajg_gap_ror_20261026_countryfix

ROR ids on the ABS/AJG gap current boards, country-only affiliation fix applied 2026-10-26 07:44 Asia/Hong_Kong. This supersedes freeze `editors_abs_ajg_gap_ror_20261025`. The journal set and the row filter are still freeze `editors_abs_ajg_gap_20261025`. `editor_name` is still freeze `editors_display_names_20261025`, except seven ajg2 rows where the collector split a mashed person and institution from the same cell. There is still no `faculty_profile_url`. This freeze does not rematch ABDC C and does not edit Rankings.

`scripts/build_site.py` groups an Institutions row on `ror_id` when that cell is filled. The name and country it shows are `ror_name` and `ror_country` when those cells are filled. `raw_affiliation` is the masthead string and was not overwritten by the build. A row with an affiliation and no `ror_id` still groups on that affiliation text, unless the text is only a country or territory after trimming and removing wrapping parentheses. Those unmatched clusters are left off the Institutions page. The comparison uses the ROR country labels already on these boards, plus masthead aliases that are not the ROR label (`USA`, `US`, `U.S.`, `U.S.A.`, `UK`, `U.K.`, `Netherlands`, `Holland`, `Korea`, `Turkey`, `Czech Republic`). A row with a `ror_id` is kept. The build does not invent an institution name.

## Files in this repository

The collector wrote the country-fix onto the live panels (11,288 / 5,032 / 3,490). Fourteen of those rows were already excluded from `editors_abs_ajg_gap_20261025` as drop-quality chrome (publisher navigation, a paper title, a metrics line, and similar). They stay out. None of the fourteen has a `ror_id`. One excluded ajg2 row has a nonempty affiliation and a low-confidence note, so the affiliation and low-confidence counts below are one row smaller than the collector’s live-panel total.

| File | Rows | Nonempty affiliation | `ror_id` filled | Fill of affiliation |
|---|---:|---:|---:|---:|
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,276 | 8,645 | 8,400 | 97.2% |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,030 | 4,687 | 4,485 | 95.7% |
| `editors_abs_ajg_gap_prio43_current.csv` | 3,490 | 2,618 | 2,501 | 95.5% |
| Total | 19,796 | 15,950 | 15,386 | 96.5% |

The collector’s live-panel total, including those fourteen rows, is 15,386 / 15,951 nonempty affiliations (96.5%) across 19,810 rows. Before `editors_abs_ajg_gap_ror_20261025` the three published panels had `ror_id` on 0 rows. That freeze had `ror_id` on 15,390 of 15,974 nonempty affiliations (96.3%).

`ror_id` is copied only where the collector recorded high or medium confidence. Low-confidence hits stay off `ror_id`: 244 ajg1, 189 ajg2, and 102 prio43 rows on these files. The collector counted 190 low on the ajg2 live panel because of the excluded chrome row. One ajg1 row, ten ajg2 rows, and thirteen prio43 rows are marked `unmatched` and have no `ror_id`.

Country-only `raw_affiliation` rows left on these files, counted the way the collector counted them (exact country or territory after trim and parentheses): ajg1 31, ajg2 56, prio43 25, total 112. The previous live panels had 143. The collector cleared 7 bad medium ROR ids, blanked 24 UN-fragment or country-list junk affiliations, applied 7 evidenced person-plus-institution splits, and parked the remaining 112 for a later source pass. One split kept a new high-confidence ROR id (Harvard University). Those 112 rows stay in the CSVs. The Institutions page does not list them as institutions.

## Rules

Nothing in this repository invents a ROR id, an editor name, or an institution name. `editor_name`, `editor_name_raw`, and `raw_affiliation` are the values already on these files. Distinct campuses were not merged unless they share a `ror_id`. A masthead that differs only by a country suffix collapses on the Institutions page when both rows carry the same `ror_id`. Rows that are still unmatched stay keyed on the affiliation string, except a bare country or territory.

Columns copied from the freeze, and only those columns: `canonical_name`, `ror_id`, `ror_name`, `ror_country`, `continent`, `lat`, `lon`, `ror_match_method`, `ror_match_score`, `ror_confidence`, `ror_notes`, plus the seven split `editor_name` / `editor_name_raw` / `raw_affiliation` cells and the 24 blanked junk affiliations. Latitude and longitude are not written to the site.

The collector coverage note and `HANDOFF.md` are not used by the site. They are not in this repository.

## Public site

`scripts/build_site.py` reads these three CSVs. ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site. There is no `faculty_profile_url`, so person names stay plain text. A board link is `source_url` when that value is http(s).

Eight prio43 rows whose `editor_name` is `Email` (Nature Human Behaviour) stay in the CSV and are omitted from the directory by the existing non-person name filter. Those appointments have no `ror_id`.

Do not merge these boards into the ABDC files.

## Display names (`editors_display_names_20261025`)

Display names on these boards were cleaned 2026-10-25 20:20 Asia/Hong_Kong, before the ROR fill. This country-fix freeze then changed seven ajg2 names on Perspectives on Public Management & Governance, where the person and the institution had been stored in `editor_name` and the affiliation was only a country. The person is `editor_name`. The previous mashed string is `editor_name_raw`. The institution fragment is `raw_affiliation`. Daniel Carpenter keeps Harvard University (`ror_id` `https://ror.org/03vek6s52`, high). Sandro Cabral, David Arellano Gault, Sharon Gilad, Sandra Groeneveld, Sounman Hong, and Yijia Jang stay unmatched. No other `editor_name` was edited. Grades and tenure columns were not edited.

`editor_name` is the name the directory shows. `editor_name_raw` is the pre-clean value when the name changed, and blank when it did not. The build does not invent a name and does not display `editor_name_raw`.

`CHANGE_LOG.csv` from the collector freeze is about 6MB and is not used by the site. It is not in this repository.

The collector cleaned the live panels (11,288 / 5,032 / 3,490). Fourteen of those rows were already excluded from `editors_abs_ajg_gap_20261025` as drop-quality chrome. They stay out of these files. One of the fourteen was a case fix (`INFORMATION FOR` → `Information For`), so the committed ajg1 file has 602 changed names rather than 603. The seven splits above are not in that table.

| File | Rows | Changed | Degrees stripped | Case fixed | Initials expanded | Bare initials left |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,490 | 52 | 48 | 0 | 4 | 257 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,030 | 106 | 87 | 1 | 18 | 272 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,276 | 602 | 496 | 108 | 10 | 167 |

Degree, case, and initial columns for ajg1 are the collector's live-panel counts except the one excluded case fix. The other excluded rows were not name changes.

Collector totals across every live panel, including both FT50 files: 179,571 rows, 21,732 changed, 17,757 degrees stripped, 2,933 case fixes, 1,306 initials expanded, 2,928 bare initials left as printed. After the fourteen-row exclusion, the files committed here (all panels) are 179,557 rows and 21,731 changed names.

Strip trailing degrees and leading titles, turn ALL-CAPS person names into title case, and expand a bare given initial only from another row with the same initial, surname, and `ror_id`, normalized affiliation, or faculty URL. No invented givens. Bare initials with no such evidence stay as printed.
