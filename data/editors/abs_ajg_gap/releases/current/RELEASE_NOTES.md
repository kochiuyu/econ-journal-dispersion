# editors_abs_ajg_gap_ror_20261026_bracketfix

ROR ids on the ABS/AJG gap current boards. Bracket-only and address-only affiliations were blanked 2026-10-26 08:41 Asia/Hong_Kong. This supersedes freeze `editors_abs_ajg_gap_ror_20261026_countryfix`. The journal set and the row filter are still freeze `editors_abs_ajg_gap_20261025`. `editor_name` is still freeze `editors_display_names_20261025`, except seven ajg2 rows where the collector split a mashed person and institution from the same cell. There is still no `faculty_profile_url`. This freeze does not rematch ABDC C and does not edit Rankings.

`scripts/build_site.py` groups an Institutions row on `ror_id` when that cell is filled. The name and country it shows are `ror_name` and `ror_country` when those cells are filled. `raw_affiliation` is the masthead string and was not overwritten by the build. A row with an affiliation and no `ror_id` still groups on that affiliation text, unless the text is junk of one of these kinds:

- a country or territory after trimming and unwrapping `()` / `[]` (the countryfix detector: ROR country labels on these boards, plus `USA`, `US`, `U.S.`, `U.S.A.`, `UK`, `U.K.`, `Netherlands`, `Holland`, `Korea`, `Turkey`, `Czech Republic`)
- the whole string enclosed in `()` or `[]`
- a street, PO Box, or postal code with no organization token

A row with a `ror_id` is kept. An organization word (university, college, institute, school, and the same family) or an all-caps acronym of three or more letters keeps a street address, so `INFORMS` and `University of St. Gallen` stay. The build does not invent an institution name.

## Files in this repository

The collector wrote the bracket fix onto the live panels (11,288 / 5,032 / 3,490). Fourteen of those rows were already excluded from `editors_abs_ajg_gap_20261025` as drop-quality chrome (publisher navigation, a paper title, a metrics line, and similar). They stay out. None of the fourteen has a `ror_id`.

| File | Rows | Nonempty affiliation | `ror_id` filled | Fill of affiliation |
|---|---:|---:|---:|---:|
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,276 | 8,642 | 8,400 | 97.2% |
| `editors_abs_ajg_gap_ajg2_current.csv` | 5,030 | 4,671 | 4,484 | 96.0% |
| `editors_abs_ajg_gap_prio43_current.csv` | 3,490 | 2,616 | 2,500 | 95.6% |
| Total | 19,796 | 15,929 | 15,384 | 96.6% |

The collector’s live-panel total, including the fourteen chrome rows, is 15,384 / 15,930 nonempty affiliations (96.6%). One excluded ajg2 row still has a nonempty affiliation, so the published nonempty count is one smaller. Before this freeze the published panels had `ror_id` on 15,386 of 15,950 nonempty affiliations (96.5%).

`ror_id` is copied only where the collector recorded high or medium confidence. Low-confidence hits stay off `ror_id`: 241 ajg1, 177 ajg2, and 101 prio43 rows on these files. One ajg1 row, nine ajg2 rows, and thirteen prio43 rows are marked `unmatched` and have no `ror_id`.

On these published files the collector blanked `raw_affiliation` and `canonical_name` on 21 rows and cleared 2 bad ROR ids. Fully bracket-enclosed affiliations went from 17 to 0. The blanks are 17 bracket-only strings (`(Country)` or `(In Memoriam)`), 2 street addresses (`Manor Road, Oxford` and `130 Orange Valley Road, Kalamunda, WA, Australia`), and 2 zip or year strings (`NJ 08901` and `20011-2014`). The cleared ROR ids were Stockholm Environment Institute on the Manor Road row and Lebanon Valley College on the Orange Valley Road row. No organization name was invented. Two rows whose `editor_name` is itself an address fragment (`Manor Road Building`, `New Brunswick`) stay in the CSV with a blank affiliation.

Bare-country `raw_affiliation` rows left on these files, using the Institutions detector (exact country or territory after trim and unwrapping parentheses or brackets, no `ror_id`): ajg1 30, ajg2 42, prio43 25, total 97. The previous published panels had 112. Those 97 stay in the CSVs. The Institutions page does not list them.

## Rules

Nothing in this repository invents a ROR id, an editor name, or an institution name. `editor_name`, `editor_name_raw`, and `raw_affiliation` are the values already on these files. Distinct campuses were not merged unless they share a `ror_id`. A masthead that differs only by a country suffix collapses on the Institutions page when both rows carry the same `ror_id`. Rows that are still unmatched stay keyed on the affiliation string, except a bare country or territory, a fully bracketed fragment, or a street, PO Box, or postal code with no organization token.

Columns taken from this freeze, and only where the collector changed them: `raw_affiliation`, `canonical_name`, and the ROR cells on the 21 blanked rows (`ror_id`, `ror_name`, `ror_country`, `continent`, `lat`, `lon`, `ror_match_method`, `ror_match_score`, `ror_confidence`, `ror_notes`). Latitude and longitude are not written to the site.

The collector coverage note and `HANDOFF.md` are not used by the site. They are not in this repository.

## Public site

After this freeze the Institutions page has 10,099 rows (9,674 with a ROR id) and 147,195 appointments on an institution. The country-fix build had 10,104 rows, the same 9,674 with a ROR id, and 147,202 appointments. Five unmatched junk clusters are gone (`(In Memoriam)`, `(Morroco)`, `NJ 08901`, `(chair)`, and a bracketed credit line). The two cleared address-to-ROR matches are no longer appointments at Stockholm Environment Institute or Lebanon Valley College; both institutions remain because other rows still carry those ROR ids. Directory journals stay 2,853. Directory appointments stay 159,399. One hundred appointments are omitted because the affiliation is only a country or territory (was 115). Two are omitted because the affiliation is only a bracketed fragment. No remaining unmatched affiliation is only a street, PO Box, or postal code.

`scripts/build_site.py` reads these three CSVs. ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site. There is no `faculty_profile_url`, so person names stay plain text. A board link is `source_url` when that value is http(s).

Eight prio43 rows whose `editor_name` is `Email` (Nature Human Behaviour) stay in the CSV and are omitted from the directory by the existing non-person name filter. Those appointments have no `ror_id`.

Do not merge these boards into the ABDC files.

## Display names (`editors_display_names_20261025`)

Display names on these boards were cleaned 2026-10-25 20:20 Asia/Hong_Kong, before the ROR fill. The country-fix freeze then changed seven ajg2 names on Perspectives on Public Management & Governance, where the person and the institution had been stored in `editor_name` and the affiliation was only a country. This bracket fix did not change `editor_name`. The person is `editor_name`. The previous mashed string is `editor_name_raw`. Daniel Carpenter keeps Harvard University (`ror_id` `https://ror.org/03vek6s52`, high). Sandro Cabral, David Arellano Gault, Sharon Gilad, Sandra Groeneveld, Sounman Hong, and Yijia Jang stay unmatched. Grades and tenure columns were not edited.

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
