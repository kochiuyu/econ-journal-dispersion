# editors_institution_paren_geo_20261028

Residual ROR cleanup, junk-parenthesis blanking, and ROR country backfill on the FT50 current board. Frozen 2026-10-28 16:39 Asia/Hong_Kong. This supersedes `editors_institution_nonsense_20261028`. Both files stay 10,046 rows. Empty `editor_name` is 0. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. It does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution.

## What this freeze changed

D1 cleared bad reattached and famous ROR matches, then rematched only on a strict high or medium overlap that ignores country tokens and rejects known-bad ids. D2 blanked junk parenthetical affiliations. D3 filled missing ROR country and continent. Famous leftovers are none.

| Metric | Before this freeze | After |
|---|---:|---:|
| Rows | 10,046 | 10,046 |
| `faculty_profile_url` | 8,375 (83.4%) | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,957 (99.1%) | 9,956 (99.1%) |
| `ror_id` on the ROR file | 9,948 | 9,867 (98.2%) |
| Faculty URL, no `ror_id` | 7 | 57 |

The slim file has `raw_affiliation` on 9,957 rows. The directory does not read it while the ROR file is present. Cleared ROR ids were not replaced when the strict rematch missed.

Three medium hits stay unpublished because the ROR name is a different organization. The affiliation text stays.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland, USA.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.
- Tom P. Moliterno, Academy of Management Review: `https://ror.org/02bygyh83` is The Citadel Foundation. Affiliation kept as The Citadel, USA.

Jaap Paauwe’s display name is `Jaap Paauwe`. `editor_name_raw` is `Jaap Paauwe, Tilburg`, so the ABDC copy of that Human Resource Management seat stays one row. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page.

No person name, ROR id, or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments stay 158,664. Editors stay 110,345. Journals stay 2,853. Countries are 172. FT50 seats stay 10,045 across 50 journals. Top 5 stays 363. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 11,482 rows (9,312 with a ROR id), were 10,069 (9,614). 11,255 appointments have no institution. 628 appointments are omitted because the affiliation is only a country or territory. Three are omitted because the affiliation is only a bracketed fragment. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
