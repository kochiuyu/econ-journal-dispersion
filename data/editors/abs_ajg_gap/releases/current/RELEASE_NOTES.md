# editors_institution_paren_geo_20261028

Residual ROR cleanup, junk-parenthesis blanking, and ROR country backfill on the AJG-gap boards. Frozen 2026-10-28 16:39 Asia/Hong_Kong. This supersedes `editors_institution_nonsense_20261028`. African Affairs stays the 40-row Wayback board. Rankings were not edited. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Empty `editor_name` is 0. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution.

The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay on rows this freeze did not replace. Live OUP for African Affairs is still Cloudflare-blocked. See `african_affairs_needs_browser.md`.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2. The collector CSV again included 12 ajg1 navigation or citation rows and 2 ajg2 navigation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them. No replacement ROR was added for that row.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, no university | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 0 | 82 | 2,746 | 2,667 | 0 | 2 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,982 | 0 | 386 | 4,784 | 4,571 | 0 | 6 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,217 | 0 | 616 | 8,881 | 8,513 | 0 | 8 |
| Total | 19,303 | 0 | 1,084 | 16,411 | 15,751 | 0 | 16 |

`ror_id` on a nonempty affiliation is 15,751 / 16,411 (96.0%): ajg1 8,513 / 8,881 (95.9%), ajg2 4,571 / 4,784 (95.5%), prio43 2,667 / 2,746 (97.1%). Gap `ror_id` values are high or medium confidence only. A faculty URL with no university is 0. Sixteen faculty URLs have no `ror_id` because the strict rematch missed. No replacement id was added.

## Public site

Directory journals stay 2,853. Directory appointments stay 158,664. Editors stay 110,345. Countries are 172. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796). Faculty profile links stay 24,817. The Institutions page has 11,482 rows (9,312 with a ROR id) and 11,255 appointments with no institution. 628 appointments are omitted because the affiliation is only a country or territory. Three are omitted because the affiliation is only a bracketed fragment. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country. `11KBW`, UNSW Sydney, and INSEAD stay.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
