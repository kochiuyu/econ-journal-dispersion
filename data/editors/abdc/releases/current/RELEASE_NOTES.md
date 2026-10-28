# editors_institution_junk_cleanup_20261028

Evidenced junk in the institution field was blanked or cleared on the ABDC A*, A, B, and C current boards. Frozen 2026-10-28 17:48 Asia/Hong_Kong. This supersedes `editors_institution_paren_geo_20261028`. Row counts are unchanged. Empty `editor_name` is 0. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. Faculty URL counts are unchanged.

The directory displays `ror_name`, then `canonical_name`, then `raw_affiliation`. On the 33 rows whose `raw_affiliation` this freeze blanked, `canonical_name` was that same string. That copy was cleared so the row is blank on the site. No new affiliation text was written.

## What changed

44 ABDC rows. 33 blanked `raw_affiliation` (and the matching `canonical_name`). 11 cleared a digit-leading junk `ror_id`: 10 keep the affiliation text, and Lee H. Rosenthal on the University of Chicago Law Review was already blank (`77 Elektronika (Hungary)` cleared).

| Class | Rows |
|---|---:|
| Date range / role tenure | 17 |
| Credential / title, uncorroborated | 10 |
| Street / postal code | 4 |
| Digit-leading junk ROR | 11 |
| Biography chrome | 2 |

| Panel | Date range | Credential | Street | Digit ROR | Biography chrome |
|---|---:|---:|---:|---:|---:|
| A* | 3 | 0 | 0 | 3 | 0 |
| A | 0 | 0 | 0 | 0 | 2 |
| B | 8 | 0 | 3 | 6 | 0 |
| C | 6 | 10 | 1 | 2 | 0 |

Kept affiliation text after the digit-leading clear includes `BI Oslo`, `Ined, France`, `VUB Research Group Work and Organizational Psychology, Brussels, Belgium`, `Arntzen de Besche Advokatfirma AS, Oslo`, and `ADVOKATFIRMAET SCHJODT AS, OSLO`. `3B's Research Group`, `657 Oslo`, `77 Elektronika (Hungary)`, `5T Torino (Italy)`, `6WIND (France)`, `Nestec (Switzerland)`, and `Izmir University` are off the Institutions page.

## Files

| File | Rows | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no university | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 23,861 (94.8%) | 23,626 | 12,523 (49.7%) | 4 | 74 |
| `editors_abdc_a_current.csv` | 45,363 | 43,057 (94.9%) | 42,271 | 6,237 (13.7%) | 1 | 44 |
| `editors_abdc_b_current.csv` | 42,139 | 39,903 (94.7%) | 39,081 | 3,509 (8.3%) | 1 | 20 |
| `editors_abdc_c_current.csv` | 26,720 | 24,085 (90.1%) | 23,290 | 1,379 (5.2%) | 0 | 5 |

The same three medium hits withheld on the FT50 file are withheld on the ABDC A* copy of that seat. Affiliation text stays.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland, USA.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.
- Tom P. Moliterno, Academy of Management Review: `https://ror.org/02bygyh83` is The Citadel Foundation. Affiliation kept as The Citadel, USA.

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. UNSW Sydney and INSEAD stay institution rows.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments stay 158,664. ABDC chips stay A* 25,174 (219 journals), A 45,352 (626), B 42,124 (836), and C 26,719 (732). Institutions are 11,454 rows (9,304 with a ROR id), were 11,482 (9,312). 11,289 appointments have no institution. 628 country-only appointments, 3 bracket-only appointments, and 8 street, PO Box, or postal-code appointments stay off that page.
