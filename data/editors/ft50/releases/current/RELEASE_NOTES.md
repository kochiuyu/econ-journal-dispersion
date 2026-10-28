# editors_institution_nonsense_20261028

Institution cleanup on the FT50 current board, frozen 2026-10-28 15:34 Asia/Hong_Kong. Both files stay 10,046 rows. Empty `editor_name` is 0.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. It does not invent a name, a ROR id, or a URL. An empty `editor_name` is not listed as a person. A bare country is not an institution. A blank affiliation is not an institution.

## What this freeze changed

Class A blanked 1 affiliation and dropped 18 navigation or citation rows on the wider publish (the FT50 files stay the same length). Class B cleared univish bad ROR matches and rematched only on a strict high or medium overlap. Class C blanked email and URL affiliations. Country-only affiliations were blanked. The FT50 ROR file is where those clears show up.

| Metric | Before this freeze | After |
|---|---:|---:|
| Rows | 10,046 | 10,046 |
| `faculty_profile_url` | 8,375 (83.4%) | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,960 (99.1%) | 9,957 (99.1%) |
| `ror_id` on the ROR file | 9,953 | 9,948 (99.0%) |
| Faculty URL, no university | 0 | 0 |
| Faculty URL, no `ror_id` | 3 | 7 |

The slim file has `raw_affiliation` on 9,958 rows. The directory does not read it while the ROR file is present.

Three medium hits stay unpublished because the ROR name is a different organization. The affiliation text stays. No replacement ROR was added.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland, USA.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.
- Tom P. Moliterno, Academy of Management Review: `https://ror.org/02bygyh83` is The Citadel Foundation. Affiliation kept as The Citadel, USA.

Four more faculty URLs have no `ror_id` because the freeze rejected the previous company ROR and did not record a strict high or medium replacement: Jack Fraser and Chengwei Liu (Imperial College), Ute Stephan (King's College), and Marco van Gelderen (VU University). The affiliation text stays.

Jaap Paauwe’s display name is `Jaap Paauwe`. `editor_name_raw` is `Jaap Paauwe, Tilburg`, the spelling still on the ABDC copy of that Human Resource Management seat, so the directory keeps one row. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). No person is named `CEMFI` or `Sciences Po`. Kevin Dunn is not on this board.

No person name, ROR id, or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments are 158,664 (were 158,716). Editors are 110,345. Journals stay 2,853. Countries stay 173. FT50 seats stay 10,045 across 50 journals. Top 5 appointments stay 363. UTD24 stays 5,178 across 24 journals. Faculty profile links on the directory are 24,817 (were 24,837). The FT50 chunk links 8,375 names. Institutions are 10,069 rows (9,614 with a ROR id). 11,234 appointments have no institution. 627 appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. `11KBW` stays an institution row. No institution row is a bare country.
