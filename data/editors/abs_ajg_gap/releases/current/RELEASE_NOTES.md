# editors_institution_nonsense_20261028

Institution cleanup on the AJG-gap boards, frozen 2026-10-28 15:34 Asia/Hong_Kong. African Affairs is re-parsed from the Wayback snapshot `20240427143040` because the live OUP board is Cloudflare-blocked. See `african_affairs_needs_browser.md`. Rankings were not edited.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Empty `editor_name` is 0. The build does not invent a name, a ROR id, or a URL. A bare country is not an institution. A blank affiliation is not an institution.

The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay on rows this freeze did not replace.

## African Affairs

The previous board was 86 rows, including citation titles, publisher parentheses, street addresses, and `Kevin Dunn` clusters. The published board is 40 people. Tim Kelsall is kept with a blank affiliation. The other 39 rows have an affiliation. The directory links the journal to `https://academic.oup.com/afraf/pages/Editorial_Board`. That live page was blocked on 2026-10-28, so the rows are the Wayback parse, not a live scrape. No raw HTML is in this repository.

Nature Human Behaviour no longer has the eight `Email` rows or the eight `Biography` rows. Those 16 rows are out of the file, not merely hidden at build time.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2. This freeze’s CSV also contained 12 ajg1 navigation or citation rows and 2 ajg2 navigation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them. His collector row paired a UNSW profile URL with ROR `EU Business School, Geneva`. That ROR is not published, and no replacement was added.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, no university | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 0 | 82 | 2,746 | 2,700 | 0 | 0 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,982 | 0 | 386 | 4,788 | 4,650 | 0 | 0 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,217 | 0 | 616 | 8,895 | 8,692 | 0 | 0 |
| Total | 19,303 | 0 | 1,084 | 16,429 | 16,042 | 0 | 0 |

`ror_id` on a nonempty affiliation is 16,042 / 16,429 (97.6%): ajg1 8,692 / 8,895 (97.7%), ajg2 4,650 / 4,788 (97.1%), prio43 2,700 / 2,746 (98.3%). Gap `ror_id` values are high or medium confidence only. A faculty URL with no university is 0. A faculty URL with no `ror_id` is 0.

## Public site

Directory journals stay 2,853. Directory appointments are 158,664, down 52 from 158,716. Editors are 110,345. Countries stay 173. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796). Faculty profile links on the directory are 24,817 (were 24,837). The Institutions page has 10,069 rows (9,614 with a ROR id) and 11,234 appointments with no institution. 627 appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. No institution row is a bare country. `11KBW` stays.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
