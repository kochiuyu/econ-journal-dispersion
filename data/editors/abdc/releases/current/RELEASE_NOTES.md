# editors_institution_empty_country_20261028

Empty-country cleanup of institution strings on the ABDC A*, A, B, and C current boards. Frozen 2026-10-28 20:41 Asia/Hong_Kong. This supersedes `editors_institution_post31_touchup_20261028` for Directory Institutions. Row counts are unchanged. Empty `editor_name` is 2 on A*, 2 on A, 0 on B, and 11 on C. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution. Faculty URL counts are unchanged.

The collector freeze edits 506 editor rows across FT50, ABDC, and the AJG-gap files. Twelve ajg1 navigation rows and two ajg2 navigation rows are not on the published boards and stay out. On these files the change is A* 41, A 81, B 68, and C 99. A street, postal address, city fragment, credential, or navigation string used as the institution is blank. A masthead that names a university already on these boards is rematched to that existing ROR id. No new ROR id was added.

The directory reads `canonical_name` when `ror_name` is empty. Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` is clear, so the row does not keep the old display. `canonical_name` values cleared in the previous institution freezes stay clear. The collector file had restored them.

## Files

| File | Rows | Empty `editor_name` | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 2 | 23,811 (94.6%) | 23,646 | 12,523 (49.7%) | 60 |
| `editors_abdc_a_current.csv` | 45,363 | 2 | 42,842 (94.4%) | 42,189 | 6,237 (13.7%) | 40 |
| `editors_abdc_b_current.csv` | 42,139 | 0 | 39,809 (94.5%) | 39,115 | 3,509 (8.3%) | 19 |
| `editors_abdc_c_current.csv` | 26,720 | 11 | 23,882 (89.4%) | 23,322 | 1,379 (5.2%) | 4 |

## Named cases

`Aberdeen University` and `ABERDEEN UNIVERSITY` are rematched to University of Aberdeen, `https://ror.org/016476m91`, United Kingdom. That id was already on these boards. The masthead text stays.

- Agnieszka Konopka, Journal of Experimental Psychology: general: raw stays `Aberdeen University, United Kingdom`. ROR is University of Aberdeen.
- Ritu Vij, Third World Quarterly: the row whose raw is `Aberdeen University, UK` is University of Aberdeen. Her seats whose raw already says University of Aberdeen stay on `https://ror.org/016476m91`.
- Scott Styles, Juridical Review: raw stays `ABERDEEN UNIVERSITY`. ROR is University of Aberdeen.

One A-panel title used as an editor name is blank (`Dynamic and longitudinal development of anthropomorphic perceptions and human` on AIS Transactions on Human-Computer Interaction). The row is not a person. The paper-title affiliation on the `Psychological` row of that board is blank. Rajasegaran Krishnasamy’s Accounting Research Institute street address on the C panel is blank.

Hengeler Mueller stays as the firm name. Dunarea de Jos and Tribhuvan Sahkari stay without decorative quotes. `[C]Worthy` stays off David McCarthy. The same two medium hits withheld on the FT50 file are withheld on the ABDC A* copy of that seat.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.

Tom P. Moliterno on the A* copy of Academy of Management Review uses the same Citadel ROR as the FT50 row, `https://ror.org/01vwr6t80`.

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. UNSW Sydney and INSEAD stay institution rows.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments are 158,624, were 158,628. ABDC chips are A* 25,172 (219 journals), unchanged; A 45,350 (626), were 45,351; B 42,124 (836), unchanged; C 26,708 (732), unchanged. Countries stay 176. Institutions are 10,915 rows (9,282 with a ROR id), were 11,261 (9,282). 11,996 appointments have no institution, were 11,625. 627 country-only appointments, 1 bracket-only appointment, and 8 street, PO Box, or postal-code appointments stay off that page.
