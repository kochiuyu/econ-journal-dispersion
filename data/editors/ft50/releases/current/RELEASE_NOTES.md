# editors_ft50_url_aff_20261028

University and ROR filled for FT50 editors who already had `faculty_profile_url` and a missing or unusable institution. Frozen 2026-10-28 11:51 Asia/Hong_Kong. Both files stay 10,046 rows. Empty `editor_name` is 0.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. It does not invent a name. An empty `editor_name` is not listed as a person. A bare country is not an institution.

## Rates

| Metric | Before this freeze | After |
|---|---:|---:|
| Rows | 10,046 | 10,046 |
| `faculty_profile_url` | 8,360 (83.2% in the previous publish) | 8,375 (83.4%) |
| `raw_affiliation` | 9,900 (98.5% on the ROR file) | 9,960 (99.1%) |
| Faculty URL, no university | 60 | 0 |
| Faculty URL, no `ror_id` | 63 | 3 |
| `ror_id` | 9,893 | 9,953 (99.1%) |
| Still blank URL | 1,686 | 1,671 |

The collector file had faculty-URL-and-no-ROR at 0 (9,956 `ror_id` values). Three medium hits are not in this publish because the ROR name is a different organization:

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland, USA.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School, Spain.
- Tom P. Moliterno, Academy of Management Review: `https://ror.org/02bygyh83` is The Citadel Foundation. Affiliation kept as The Citadel, USA.

No replacement ROR was added. Other new ROR ids are the collector’s high or medium matches, including University of Bolton recorded as University of Greater Manchester (the successor name). A non-empty ROR id that was already on the row was not replaced.

Jaap Paauwe’s display name is `Jaap Paauwe`. `editor_name_raw` is `Jaap Paauwe, Tilburg`, the spelling still on the ABDC copy of that Human Resource Management seat, so the directory keeps one row. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). No person is named `CEMFI` or `Sciences Po`.

No person name, ROR id, or URL was invented. Emails, phone numbers, and photos are not written to the site. ABDC and AJG-gap panels are unchanged.

## Public site

Directory appointments stay 158,716. FT50 seats stay 10,045 across 50 journals. Top 5 appointments stay 363. Faculty profile links on the directory are 21,666 (were 21,652). The FT50 chunk links 8,375 names. A bare country is still not an institution. Two Human Resource Management rows whose affiliation is only Netherlands, and who have no faculty URL, stay off that page.
