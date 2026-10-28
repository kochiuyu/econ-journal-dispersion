# editors_institution_trailing_place_20261028

Trailing-place cleanup of institution strings on the ABDC A*, A, B, and C current boards. Frozen 2026-10-28 21:14 Asia/Hong_Kong. This supersedes `editors_institution_empty_country_20261028` for Directory Institutions. Row counts are unchanged. Empty `editor_name` is 2 on A*, 2 on A, 0 on B, and 11 on C. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution. Faculty URL counts are unchanged.

The collector freeze edits 2,044 editor rows across FT50, ABDC, and the AJG-gap files. Twelve ajg1 navigation rows and two ajg2 navigation rows are not on the published boards and stay out. On these files the change is A* 182, A 557, B 563, and C 391. A trailing place or country is stripped from the organization. A role title or a mashup used as the institution is blank. A keep-org masthead is rematched only to a ROR id already on these boards. Where the ROR name was the place-laden string rather than the organization left after the strip, that id is cleared. No new ROR id was added.

The directory reads `canonical_name` when `ror_name` is empty. Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` is clear, so the row does not keep the old display. `canonical_name` values cleared in the previous institution freezes stay clear on rows this freeze did not edit. The collector file had restored them.

## Files

| File | Rows | Empty `editor_name` | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 2 | 23,806 (94.6%) | 23,641 | 12,523 (49.7%) | 63 |
| `editors_abdc_a_current.csv` | 45,363 | 2 | 42,779 (94.3%) | 42,168 | 6,237 (13.7%) | 44 |
| `editors_abdc_b_current.csv` | 42,139 | 0 | 39,781 (94.4%) | 39,088 | 3,509 (8.3%) | 21 |
| `editors_abdc_c_current.csv` | 26,720 | 11 | 23,852 (89.3%) | 23,293 | 1,379 (5.2%) | 4 |

## Named cases

Sam Kirshner, Journal of Supply Chain Management, was `Regional Editor (Southeast Asia & Pacific), UNSW, Australia`. The row is UNSW Sydney, `https://ror.org/03r8z3t63`, Australia. That id was already on these boards.

Ute-Christine Klehe, Journal of Business and Psychology, is `Abt.Arbeits- und Organisationspsychologie Otto`. The trailing `Marburg, Germany` is gone. Andrew Lloyd, Quality of Life Research, is `Acaster Lloyd Consulting Ltd`. The trailing `London, United Kingdom` is gone. Taşkın Yıldız, Resources Policy, is `Adana Alparslan Türkeş Science and Technology University, Department of Mining Engineering`, country Türkiye. The trailing place is gone.

Vitaliy Pogoretskyy, World Trade Review, was a mashup of the Advisory Centre on WTO Law and IKEA Supply AG. The institution is blank.

`Aberdeen University` and `ABERDEEN UNIVERSITY` stay on University of Aberdeen, `https://ror.org/016476m91`, United Kingdom, the rematch from `editors_institution_empty_country_20261028`. That id was already on these boards.

- Agnieszka Konopka, Journal of Experimental Psychology: general: raw stays `Aberdeen University, United Kingdom`. ROR is University of Aberdeen.
- Ritu Vij, Third World Quarterly: the row whose raw is `Aberdeen University, UK` is University of Aberdeen.
- Scott Styles, Juridical Review: raw stays `ABERDEEN UNIVERSITY`. ROR is University of Aberdeen.

Hengeler Mueller stays as the firm name. Dunarea de Jos and Tribhuvan Sahkari stay without decorative quotes. `[C]Worthy` stays off David McCarthy.

The same two medium hits withheld on the FT50 file are withheld on the ABDC copy of that seat.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland. Canonical name is `University of Maryland`.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School. Country is Spain.

Tom P. Moliterno on the A* copy of Academy of Management Review uses the same Citadel ROR as the FT50 row, `https://ror.org/01vwr6t80`.

Kai Hockerts, Journal of Asia Entrepreneurship and Sustainability, was `Adjunct Professor, INSEAD, France`. The row is INSEAD, `https://ror.org/05ynf4333`. That id was already on these boards. The ROR country is Singapore.

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. UNSW Sydney and INSEAD stay institution rows.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments stay 158,624. ABDC chips stay A* 25,172 (219 journals), A 45,350 (626), B 42,124 (836), and C 26,708 (732). Countries are 175, were 176. Institutions are 10,726 rows (9,266 with a ROR id), were 10,915 (9,282). 12,141 appointments have no institution, were 11,996. 627 country-only appointments, 1 bracket-only appointment, and 8 street, PO Box, or postal-code appointments stay off that page.
