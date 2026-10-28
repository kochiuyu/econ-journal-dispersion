# editors_institution_paren_geo_20261028

Residual ROR cleanup, junk-parenthesis blanking, and ROR country backfill on the ABDC A*, A, B, and C current boards. Frozen 2026-10-28 16:39 Asia/Hong_Kong. This supersedes `editors_institution_nonsense_20261028`. Row counts are unchanged. Empty `editor_name` is 0. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. Faculty URL counts are unchanged. Cleared ROR ids were not replaced when the strict rematch missed.

## Files

| File | Rows | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no university | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 23,864 (94.8%) | 23,629 | 12,523 (49.7%) | 4 | 74 |
| `editors_abdc_a_current.csv` | 45,363 | 43,059 (94.9%) | 42,271 | 6,237 (13.7%) | 1 | 44 |
| `editors_abdc_b_current.csv` | 42,139 | 39,914 (94.7%) | 39,087 | 3,509 (8.3%) | 1 | 20 |
| `editors_abdc_c_current.csv` | 26,720 | 24,102 (90.2%) | 23,296 | 1,379 (5.2%) | 0 | 5 |

The same three medium hits withheld on the FT50 file are withheld on the ABDC A* copy of that seat. Affiliation text stays.

- Rebecca Ratner, Journal of Marketing Research: not University of Goma. Affiliation kept as University of Maryland, USA.
- Ioannis Evangelidis, Journal of Marketing Research: not EAE Business School. Affiliation kept as ESADE Business School, Spain.
- Tom P. Moliterno, Academy of Management Review: not The Citadel Foundation. Affiliation kept as The Citadel, USA.

`11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id. UNSW Sydney and INSEAD stay institution rows.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments stay 158,664. ABDC chips stay A* 25,174 (219 journals), A 45,352 (626), B 42,124 (836), and C 26,719 (732).
