# editors_institution_country_place_20261029

Place-suffix and country cleanup of institution strings on the ABDC A*, A, B, and C current boards. Frozen 2026-10-29 00:37 Asia/Hong_Kong. This supersedes `editors_institution_residual_post35_20261028` for Directory Institutions. Row counts are unchanged. Empty `editor_name` is 2 on A*, 2 on A, 0 on B, and 11 on C. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution. Faculty URL counts are unchanged.

The collector freeze touches 161 editor rows across FT50, ABDC, and the AJG-gap files. This publish pins 159. On these files that is A* 5, A 36, B 60, and C 46. A place suffix is stripped. A country mismatch is corrected when the affiliation text names that country. Nine rows clear a wrong Office of Science & Technology Austria ROR and keep the masthead. A rematch uses only a ROR id already on these boards. The FT50 files are unchanged. A stripped ROR name is not copied onto a different masthead. HKUST (Guangzhou) stays distinct from The Hong Kong University of Science and Technology. Universidade de Santiago de Compostela stays Spain. Oxford colleges stay the United Kingdom. No new ROR id was added.

The directory reads `canonical_name` when `ror_name` is empty. `canonical_name` values cleared in the previous institution freezes stay clear on rows this publish did not edit.

## Files

| File | Rows | Empty `editor_name` | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 2 | 23,806 (94.6%) | 23,600 | 12,523 (49.7%) | 67 |
| `editors_abdc_a_current.csv` | 45,363 | 2 | 42,776 (94.3%) | 41,935 | 6,237 (13.7%) | 50 |
| `editors_abdc_b_current.csv` | 42,139 | 0 | 39,775 (94.4%) | 38,720 | 3,509 (8.3%) | 21 |
| `editors_abdc_c_current.csv` | 26,720 | 11 | 23,845 (89.2%) | 23,001 | 1,379 (5.2%) | 4 |

`ror_id` was 23,599 / 41,935 / 38,722 / 23,005. The added id is Federation University, `https://ror.org/05qbzwv83`, already on these boards. The cleared ids were the Office of Science & Technology Austria ROR on mastheads that name a different organization.

## Named cases

Alexis Goncalves is `Pfizer Inc.`, country United States. The masthead had `Pfizer Inc. - USA`.

Andrew Stewart is `Morgan Stanley`, country United States. The masthead had `Morgan Stanley - USA`. Eric Lufkin’s `Morgan Stanley` seat stays the United Kingdom.

Matt Symonds is `Bain and Company, Inc.`, country United Kingdom. Darrell Rigby is `Bain & Company`, country United States. Robert J. Thomas is `Accenture Institute for High Performance Business`, country United States. Sean Rafter is `HELP Logistics`, country Switzerland. Michael Keenan is `OECD`. The masthead had `OECD - France`. Country stays France.

John DeMarco is `IBM Corporation`, country United States. John Black stays `IBM - UK`, country United Kingdom, so that seat does not collapse into the United States `IBM` row.

Daniel Halbheer stays `HEC France`. Country is France.

Nine mastheads that had been matched to Office of Science & Technology Austria keep the organization string and lose that ROR. Leon B. Greenfield stays WilmerHale. David Katz stays Pactech Law. Michael Maccoby stays The Macoby Group. No replacement ROR was attached.

Federation University seats that named that organization use `https://ror.org/05qbzwv83`, an id already on these boards. `canonical_name` values cleared in earlier freezes stay clear.

`Aberdeen University` stays on University of Aberdeen, `https://ror.org/016476m91`, United Kingdom. Hengeler Mueller stays as the firm name. Dunarea de Jos and Tribhuvan Sahkari stay without decorative quotes. HKUST (Guangzhou) stays a separate affiliation from The Hong Kong University of Science and Technology. China University of Geosciences (Beijing) keeps `https://ror.org/04q6c7p66`.

The same two medium hits withheld on the FT50 file are withheld on the ABDC copy of that seat.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School. Country is Spain.

Tom P. Moliterno on the A* copy of Academy of Management Review uses the same Citadel ROR as the FT50 row, `https://ror.org/01vwr6t80`.

Kai Hockerts stays INSEAD, `https://ror.org/05ynf4333`. Sam Kirshner stays UNSW Sydney, `https://ror.org/03r8z3t63`. `11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id.

Philip Marcovici, Suneet Trivedy, Rahul Garella, Louise Trevaskis, Andrew Ward, and Alexander Lipton keep the mastheads and canonical names from the previous publish. Soumen Ghosh keeps `Georgia Inst of Technology`.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments stay 158,624. ABDC chips stay A* 25,172 (219 journals), A 45,350 (626), B 42,124 (836), and C 26,708 (732). Countries stay 175. Institutions are 10,782 rows (8,662 with a ROR id), were 10,835 (8,663). 12,164 appointments have no institution. 628 country-only appointments, 3 bracket-only appointments, and 10 street, PO Box, or postal-code appointments stay off that page.
