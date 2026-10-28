# editors_institution_residual_junk_20261028

Residual cleanup of institution strings on the ABDC A*, A, B, and C current boards. Frozen 2026-10-28 19:29 Asia/Hong_Kong. This supersedes `editors_institution_problem_list_20261028` for Directory Institutions. Row counts are unchanged. Empty `editor_name` is 0. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution. Faculty URL counts are unchanged.

203 editor rows changed across FT50, ABDC, and the AJG-gap files. On these files the change is A* 3, A 32, B 58, and C 74. A leading role or credential is stripped or blanked. A title or credential used as the institution name is blanked. Decorative double quotes are stripped from `ror_name` and `raw_affiliation`, and the same `ror_id` is kept. A trailing country is stripped from an unmatched masthead string when the country is already filled. No new ROR id was added.

The directory reads `canonical_name` when `ror_name` is empty. Where this freeze blanked or shortened `raw_affiliation` and left no `ror_name`, `canonical_name` still held the old string. That copy was cleared so the row shows the cleaned text, or a blank, on the site: A* 1, A 6, B 11, C 32. `canonical_name` values cleared in `editors_institution_problem_list_20261028` stay clear. The collector file had restored them. No new affiliation text was written.

## Files

| File | Rows | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no affiliation | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 23,847 (94.7%) | 23,644 | 12,523 (49.7%) | 3 | 60 |
| `editors_abdc_a_current.csv` | 45,363 | 43,013 (94.8%) | 42,292 | 6,237 (13.7%) | 4 | 40 |
| `editors_abdc_b_current.csv` | 42,139 | 39,866 (94.6%) | 39,109 | 3,509 (8.3%) | 0 | 19 |
| `editors_abdc_c_current.csv` | 26,720 | 23,969 (89.7%) | 23,317 | 1,379 (5.2%) | 0 | 4 |

## Named cases

Hengeler Mueller, Capital Markets Law Journal (Hendrik Haag): `(Partner, retired), Hengeler Mueller` is `Hengeler Mueller`. Country stays Germany. No ROR id.

`[C]Worthy` on The Journal of Alternative Investments (David McCarthy) was `https://ror.org/0147z1m82`. That id is cleared. The masthead stays `D.F. McCarthy, LLC`, with no ROR id.

Dunarea de Jos and Tribhuvan Sahkari lose decorative quotes on `ror_name`. The ROR ids stay `https://ror.org/052sta926` and `https://ror.org/026tkwd63`.

auditline on EDPACS (Ulrich Hahn) is blank. The credential line is not an institution.

The same two medium hits withheld on the FT50 file are withheld on the ABDC A* copy of that seat. The collector file had put the ROR ids back. Affiliation text stays.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.

Tom P. Moliterno on the A* copy of Academy of Management Review uses the same Citadel ROR as the FT50 row, `https://ror.org/01vwr6t80`.

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. UNSW Sydney and INSEAD stay institution rows.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments stay 158,664. ABDC chips stay A* 25,174 (219 journals), A 45,352 (626), B 42,124 (836), and C 26,719 (732). Countries stay 176. Institutions are 11,268 rows (9,286 with a ROR id), were 11,304 (9,287). 11,539 appointments have no institution, were 11,499. 627 country-only appointments, 1 bracket-only appointment, and 8 street, PO Box, or postal-code appointments stay off that page.
