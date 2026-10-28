# editors_institution_residual_post35_20261028

Residual place-in-name, country, and variant cleanup of institution strings on the AJG-gap boards. Frozen 2026-10-28 23:40 Asia/Hong_Kong. This supersedes `editors_institution_dept_country_20261028` for Directory Institutions. African Affairs stays the 40-row Wayback board. Rankings were not edited. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads these three CSVs. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. Empty `editor_name` is 3 on prio43, 0 on ajg2, and 19 on ajg1. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

The journal set is still `editors_abs_ajg_gap_20261025` (289 / 105 / 46 journals). Faculty URLs from `editors_ajg_gap_url_aff_20261028` stay. Live OUP for African Affairs is still Cloudflare-blocked. See `african_affairs_needs_browser.md`.

The collector freeze touches 711 editor rows across FT50, ABDC, and these files. On the collector ajg1 file that count sits next to 12 navigation or citation rows, and the ajg2 file has 2 navigation rows. Those 14 rows are not on the published boards and stay out, including Vincent Pan on Advances in Decision Sciences. This publish pins prio43 18, ajg2 19, and ajg1 51 rows. A residual place inside the institution name is stripped. A country mismatch is corrected when the affiliation text names that country. A rematch uses only a ROR id already on these boards. One hundred seventy-two collector rows across the whole freeze stay as published in the previous freeze, including Akiko Takeda, Takeo Igarashi, Kenjiro Taura, Hikaru Ogawa, Miho Takahashi, and Satoshi Usami (the collector would have replaced the Tokyo masthead with `Italian Cultural Institute`) and Matthew T. Witt (the collector would have replaced the masthead with `National Law University`). Xiao Wang, Nature Human Behaviour, keeps country China and the masthead `Springer Nature (Shanghai, China), Shanghai, China`. No new ROR id was added.

## Files in this repository

Fourteen drop-quality chrome rows stay out of ajg1 and ajg2. The collector CSV again included 12 ajg1 navigation or citation rows and 2 ajg2 navigation rows. They are not published. Vincent Pan on Advances in Decision Sciences stays out with them. His collector row carries `Architecture Business School` and `https://ror.org/04facnr46`. No replacement ROR was added.

`canonical_name` values cleared in `editors_institution_problem_list_20261028`, `editors_institution_residual_junk_20261028`, and `editors_institution_post31_touchup_20261028` stay clear on rows this publish did not edit. Adelaide University variants on these boards stay on `https://ror.org/028g18b61`, Adelaide University, Australia, an id already on these boards.

| File | Rows | Empty `editor_name` | `faculty_profile_url` | Nonempty `raw_affiliation` | `ror_id` | URL, blank affiliation | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `editors_abs_ajg_gap_prio43_current.csv` | 3,104 | 3 | 82 | 2,723 | 2,652 | 1 | 2 |
| `editors_abs_ajg_gap_ajg2_current.csv` | 4,982 | 0 | 386 | 4,727 | 4,574 | 0 | 7 |
| `editors_abs_ajg_gap_ajg1_current.csv` | 11,217 | 19 | 616 | 8,809 | 8,478 | 2 | 7 |
| Total | 19,303 | 22 | 1,084 | 16,259 | 15,704 | 3 | 16 |

`ror_id` on a nonempty affiliation is 15,704 / 16,259 (96.6%): ajg1 8,478 / 8,809 (96.3%), ajg2 4,574 / 4,727 (96.8%), prio43 2,652 / 2,723 (97.4%). Gap `ror_id` was 15,705. Gap `ror_id` values are high or medium confidence only. A faculty URL with a blank affiliation is 3. Sixteen faculty URLs have no `ror_id`. No name, ROR id, affiliation, or URL was invented.

## Named case

Weiru Chen, ajg2, is `Alibaba Group`, country China. The masthead had `Alibaba Group (China), Hangzhou, China`.

Mahmoud Rajablu, International Journal of Project Organisation and Management, is `Canadian Business Success Centre (CBSC)`, country Canada. The previous freeze had left `General Electric` in `raw_affiliation`. The place `Canada` is stripped from the organization string. No ROR was attached.

Bas van Aarle is KU Leuven, `https://ror.org/05f950310`, country Belgium. The masthead had typed `K.U. Leuven`. That id was already on these boards.

Rhomberg, Lorenz, Risk Analysis, keeps the masthead `Gradient Corporation`. The collector had written `Korea Telecom` into `raw_affiliation`.

Ian Martin Johnson, Journal of Humanities and Applied Social Sciences, stays Robert Gordon University (`https://ror.org/04f0qj703`, United Kingdom). Shi, Peng and Bing Yan on the prio43 board stay Adelaide University (`https://ror.org/028g18b61`, Australia). That id was already on these boards.

## Public site

Directory journals stay 2,853. Directory appointments stay 158,624. Editors stay 110,326. Countries stay 175. AJG journal chips stay 47 / 98 / 324 / 564 / 763 (1,796). Faculty profile links stay 24,817. The Institutions page has 10,835 rows (8,663 with a ROR id), were 10,888 (8,669), and 12,164 appointments with no institution, were 12,161. 628 appointments are omitted because the affiliation is only a country or territory. Three are omitted because the affiliation is only a bracketed fragment. Ten are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country. `11KBW`, UNSW Sydney, and INSEAD stay. Robert Gordon University stays. Adelaide University stays, including the variant mastheads rematched to the existing id. Hengeler Mueller stays. Dunarea de Jos University of Galati and Tribhuvan Sahkari University stay, without decorative quotes. `[C]Worthy` and A. Berland Inc. are not institution rows.

ORCID, OpenAlex, and RePEc ids stay off the site. Emails, phone numbers, and photos are not written to the site.

Do not merge these boards into the ABDC files.
