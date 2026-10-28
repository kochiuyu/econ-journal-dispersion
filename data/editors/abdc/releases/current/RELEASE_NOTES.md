# editors_institution_post31_touchup_20261028

Post-#31 touchup of institution strings on the ABDC A*, A, B, and C current boards. Frozen 2026-10-28 20:04 Asia/Hong_Kong. This supersedes `editors_institution_residual_junk_20261028` for Directory Institutions. Row counts are unchanged. Empty `editor_name` is 2 on A*, 1 on A, 0 on B, and 11 on C. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution. Faculty URL counts are unchanged.

The collector freeze edits 167 editor rows across FT50, ABDC, and the AJG-gap files. Two ajg1 navigation rows in that count are not on the published boards and stay out. On these files the change is A* 4, A 123, B 1, and C 12. Navigation chrome is blanked. `View full biography` and role lines used as the institution are blanked. The Aberdeen Regional Hospital ROR is cleared where the masthead does not name that hospital. Binam Ghimire is rematched to Robert Gordon University, an id already on these boards. No new ROR id was added.

The directory reads `canonical_name` when `ror_name` is empty. Where this freeze blanked the institution and left no `ror_name`, `canonical_name` was cleared so the row does not keep the old display: A* 2, A 119, C 1. B had none. `canonical_name` values cleared in the two previous institution freezes stay clear. The collector file had restored them. Canonical text written here is already on the masthead: `Aberdeen University` where the hospital ROR was cleared, and `Robert Gordon University` on Binam Ghimire.

## Files

| File | Rows | Empty `editor_name` | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 2 | 23,847 (94.7%) | 23,643 | 12,523 (49.7%) | 60 |
| `editors_abdc_a_current.csv` | 45,363 | 1 | 42,907 (94.6%) | 42,185 | 6,237 (13.7%) | 40 |
| `editors_abdc_b_current.csv` | 42,139 | 0 | 39,866 (94.6%) | 39,108 | 3,509 (8.3%) | 19 |
| `editors_abdc_c_current.csv` | 26,720 | 11 | 23,968 (89.7%) | 23,316 | 1,379 (5.2%) | 4 |

## Named cases

Aberdeen Regional Hospital (`https://ror.org/052nzzz22`) is cleared. The masthead does not name that hospital.

- Agnieszka Konopka, Journal of Experimental Psychology: general: raw stays `Aberdeen University, United Kingdom`. No ROR id. Display canonical is `Aberdeen University`.
- Ritu Vij, Third World Quarterly: the row whose raw is `Aberdeen University, UK` loses the hospital ROR. Her other seats stay University of Aberdeen (`https://ror.org/016476m91`) where the masthead says that name.
- Scott Styles, Juridical Review: raw stays `ABERDEEN UNIVERSITY`. No ROR id.

Binam Ghimire, Economics and Business Review: raw is `Aberdeen Business School, Robert Gordon University, UK`. ROR is `https://ror.org/04f0qj703`, Robert Gordon University, United Kingdom. That id was already on these boards.

`Read more about editorial board roles.` and `View full biography` are not institution names. Abstracting and indexing chrome is not an editor and not an institution.

Hengeler Mueller stays as the firm name. Dunarea de Jos and Tribhuvan Sahkari stay without decorative quotes. `[C]Worthy` stays off David McCarthy. auditline stays blank. The same two medium hits withheld on the FT50 file are withheld on the ABDC A* copy of that seat.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.

Tom P. Moliterno on the A* copy of Academy of Management Review uses the same Citadel ROR as the FT50 row, `https://ror.org/01vwr6t80`.

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. UNSW Sydney and INSEAD stay institution rows.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments are 158,628, were 158,664. ABDC chips are A* 25,172 (219 journals), were 25,174; A 45,351 (626), were 45,352; B 42,124 (836), unchanged; C 26,708 (732), were 26,719. Countries stay 176. Institutions are 11,261 rows (9,282 with a ROR id), were 11,268 (9,286). 11,625 appointments have no institution, were 11,539. 627 country-only appointments, 1 bracket-only appointment, and 8 street, PO Box, or postal-code appointments stay off that page.
