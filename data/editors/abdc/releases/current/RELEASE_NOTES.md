# editors_institution_nonsense_20261028

Institution cleanup on the ABDC A*, A, B, and C current boards, frozen 2026-10-28 15:34 Asia/Hong_Kong. Row counts are unchanged. Empty `editor_name` is 0.

`editor_name` is the name the directory shows. The build does not invent a name, a ROR id, or a URL. A bare country is not an institution. A blank affiliation is not an institution. Faculty URLs from `editors_nonft50_url_aff_20261028` stay. This freeze clears bad ROR matches and country-only or contact affiliations. It does not add faculty URLs.

## Files

| File | Rows | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no university | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 23,871 (94.8%) | 23,860 | 12,523 (49.7%) | 1 | 6 |
| `editors_abdc_a_current.csv` | 45,363 | 43,085 (95.0%) | 43,046 | 6,237 (13.7%) | 1 | 3 |
| `editors_abdc_b_current.csv` | 42,139 | 39,923 (94.7%) | 39,865 | 3,509 (8.3%) | 1 | 1 |
| `editors_abdc_c_current.csv` | 26,720 | 24,105 (90.2%) | 24,005 | 1,379 (5.2%) | 0 | 0 |

Before this freeze, a faculty URL with no university was 0 and a faculty URL with no `ror_id` was 0. The rows that are now URL-without-ROR are clears, not new URLs. No replacement ROR was invented for them.

The same three medium hits withheld on the FT50 file are withheld here, on the ABDC A* copy of that seat. Affiliation text stays.

- Rebecca Ratner, Journal of Marketing Research: not University of Goma. Affiliation kept as University of Maryland, USA.
- Ioannis Evangelidis, Journal of Marketing Research: not EAE Business School. Affiliation kept as ESADE Business School, Spain.
- Tom P. Moliterno, Academy of Management Review: not The Citadel Foundation. Affiliation kept as The Citadel, USA.

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. That is the chambers name, not a country.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments are 158,664. ABDC chips stay A* 25,174 (219 journals), A 45,352 (626), B 42,124 (836), and C 26,719 (732).
