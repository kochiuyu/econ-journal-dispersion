# editors_institution_dept_country_20261028

Department and country-in-name cleanup of institution strings on the ABDC A*, A, B, and C current boards. Frozen 2026-10-28 22:41 Asia/Hong_Kong. This supersedes `editors_institution_trailing_place_20261028` for Directory Institutions. Row counts are unchanged. Empty `editor_name` is 2 on A*, 2 on A, 0 on B, and 11 on C. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution. Faculty URL counts are unchanged.

The collector freeze edits 1,168 editor rows across FT50, ABDC, and the AJG-gap files. Twelve ajg1 navigation rows and two ajg2 navigation rows are not on the published boards and stay out. On these files the collector count is A* 48, A 246, B 393, and C 302. The pinned files change A* 55, A 250, B 397, and C 308 rows against `editors_institution_trailing_place_20261028`. A country string inside the institution display name is stripped. A department or faculty suffix is stripped. A rematch uses only a ROR id already on these boards. Where the ROR name was the parenthesis-laden string and the masthead names a different organization, that id is cleared and the masthead stays. The country already on the row stays. No new ROR id was added.

The directory reads `canonical_name` when `ror_name` is empty. Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` is clear, so the row does not keep the old display. `canonical_name` values cleared in the previous institution freezes stay clear on rows this freeze did not edit. The collector file had restored them.

## Files

| File | Rows | Empty `editor_name` | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 2 | 23,806 (94.6%) | 23,599 | 12,523 (49.7%) | 67 |
| `editors_abdc_a_current.csv` | 45,363 | 2 | 42,776 (94.3%) | 41,937 | 6,237 (13.7%) | 50 |
| `editors_abdc_b_current.csv` | 42,139 | 0 | 39,777 (94.4%) | 38,724 | 3,509 (8.3%) | 21 |
| `editors_abdc_c_current.csv` | 26,720 | 11 | 23,846 (89.2%) | 23,008 | 1,379 (5.2%) | 4 |

## Named cases

Luisa Andreu and Joaquín Aldas-Manzano are Universitat de València, `https://ror.org/043nxc105`, an id already on these boards. Keren Kaplan Mintz is Tel-Hai College, country Israel. Decio Coviello is `HEC`. No new ROR was attached. Simona Sacone is University of Genoa, `https://ror.org/0107c5v14`, an id already on these boards. Taşkın Yıldız is `Adana Alparslan Türkeş Science and Technology University`. The mining department is gone. Jordi Ripollés is Universitat Jaume I, `https://ror.org/02ws1xc11`.

Martine Cools, Journal of Management Accounting Research, is KU Leuven, `https://ror.org/05f950310`. The masthead had typed `KU Leueven`. That id was already on these boards.

Soumen Ghosh, Decision Sciences, keeps the masthead `Georgia Inst of Technology`. The flagged display was the ROR name `Czech Academy of Sciences, Institute of Ethnology`. That display is now Czech Academy of Sciences, `https://ror.org/053avzc18`, an id already on these boards. The masthead was not overwritten.

吉田　拓真 keeps the Kagoshima masthead. The flagged display was `Research Institute of Science and Technology, College of Science and Technology, Nihon University`. That display is now Nihon University, `https://ror.org/05jk51a88`, an id already on these boards.

A stripped wrong ROR name is not copied onto a different affiliation. Bradley Taylor stays `GITR Limited, UK`, not Thales. Philip Marcovici stays `The Offices of Philip Marcovici Limited`. Rahul Garella stays `Strides, Europe`. Bram Ramjiawan stays the St Boniface research centre. Louise Trevaskis stays `FAAA`. Pablo Cardona stays `IESE, Spain`. Andrew Ward and Alexander Lipton keep their mastheads. Suneet Trivedy’s canonical name stays `PwC`.

`Aberdeen University` stays on University of Aberdeen, `https://ror.org/016476m91`, United Kingdom. Hengeler Mueller stays as the firm name. Dunarea de Jos and Tribhuvan Sahkari stay without decorative quotes. `[C]Worthy` stays off David McCarthy.

The same two medium hits withheld on the FT50 file are withheld on the ABDC copy of that seat.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School. Country is Spain.

Tom P. Moliterno on the A* copy of Academy of Management Review uses the same Citadel ROR as the FT50 row, `https://ror.org/01vwr6t80`.

Kai Hockerts stays INSEAD, `https://ror.org/05ynf4333`. Sam Kirshner stays UNSW Sydney, `https://ror.org/03r8z3t63`. `11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments stay 158,624. ABDC chips stay A* 25,172 (219 journals), A 45,350 (626), B 42,124 (836), and C 26,708 (732). Countries stay 175. Institutions are 10,888 rows (8,669 with a ROR id), were 10,726 (9,266). 12,161 appointments have no institution, were 12,141. 628 country-only appointments, 3 bracket-only appointments, and 10 street, PO Box, or postal-code appointments stay off that page.
