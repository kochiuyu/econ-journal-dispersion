# editors_institution_trailing_place_20261028

Trailing-place cleanup of institution strings on the current boards. Frozen 2026-10-28 21:14 Asia/Hong_Kong. This supersedes `editors_institution_empty_country_20261028` for Directory Institutions. Both FT50 files stay 10,046 rows. Empty `editor_name` is 1. No D4 or D5 pass is in this freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution.

## What the freeze changed

The collector freeze edits 2,044 editor rows across FT50, ABDC, and the AJG-gap files. Twelve ajg1 navigation rows and two ajg2 navigation rows in those files are not on the published boards, so they stay out. The pinned ROR-bearing files change 2,041 rows: FT50 ROR 78, ABDC A* 182, A 557, B 563, C 391, AJG-gap prio43 24, ajg2 73, ajg1 173. The slim FT50 file updates 8 `raw_affiliation` cells so the masthead matches the ROR file. Pattern classes, as unique displays then editor rows: mashup 2/2, role_title 44/57, trailing_place 1,077/1,985. Decided actions: blank 144, blank_bad_remainder 3, rematch_keep_org 2, strip_fallback_no_ror 182, strip_place 1,713. Nine flagged displays matched no panel row and were not forced.

On these two files the change is 8 `raw_affiliation` cells in the slim file and 78 rows in the ROR file. A trailing place or country is stripped from the organization. `Universidad de los Andes, Chile, Chile` becomes `Universidad de Los Andes`. `ESADE Business School, Spain` becomes `ESADE Business School`. `Rovira i Virgili University, Tarragona` becomes `Rovira i Virgili University`. `HEC Liège` becomes `HEC Liege`. `Concordia` and `Lisbon`, used with no organization, are blank. No new affiliation text was written. Three rows lost a ROR id that named a different organization: Francisco Morales (Universidad de Los Andes, Chile), and Tobias Hahn and Uri Simonsohn (EAE Business School). `ror_id` is on 9,882 rows, was 9,885.

The collector slim file again carried ROR columns. ROR stays on `editors_ft50_current_with_ror.csv`. The directory does not read the slim file while the ROR file is present.

| Metric | This publish |
|---|---:|
| Rows | 10,046 |
| Empty `editor_name` | 1 |
| `faculty_profile_url` | 8,375 (83.4%) |
| `raw_affiliation` on the ROR file | 9,946 (99.0%) |
| `ror_id` on the ROR file | 9,882 (98.4%) |
| Faculty URL, no `ror_id` | 42 |

The slim file has `raw_affiliation` on 9,942 rows and no ROR columns.

## Publish holds

Two medium hits that name a different organization stay unpublished. The collector file put University of Goma back on Rebecca Ratner. The ROR stays empty. The trailing place is stripped from the canonical name.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland. Canonical name is `University of Maryland` (was `University of Maryland, USA`).
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. That id stays off. The masthead is `ESADE Business School`. Country is Spain, taken from the place that was stripped.

Tom P. Moliterno, Academy of Management Review, stays on `https://ror.org/01vwr6t80`, the Citadel ROR already on these boards. Jaap Paauwe’s display name stays `Jaap Paauwe`. `editor_name_raw` stays `Jaap Paauwe, Tilburg`. The collector file had cleared that cell.

`canonical_name` values cleared in earlier institution freezes stay clear on rows this freeze did not edit. The collector file had restored them. Where this freeze blanked `raw_affiliation` and left no `ror_name`, `canonical_name` is clear. No new ROR id was added. Every `ror_id` in this publish was already on a prior panel.

Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). `11KBW`, UNSW Sydney, and INSEAD stay on the Institutions page. No person name or URL was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments stay 158,624. Editors stay 110,326. Journals stay 2,853. Countries are 175, were 176. The Scotland label was only on a blanked city string (`Edinburgh, Scotland`). FT50 seats stay 10,044 across 50 journals. Top 5 stays 362. UTD24 stays 5,178 across 24 journals. Faculty profile links stay 24,817. Institutions are 10,726 rows (9,266 with a ROR id), were 10,915 (9,282). 12,141 appointments have no institution, were 11,996. 627 appointments are omitted because the affiliation is only a country or territory. One is omitted because the affiliation is only a bracketed fragment. Eight are omitted because the affiliation is only a street, PO Box, or postal code. No institution row is a bare country.
