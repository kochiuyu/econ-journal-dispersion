# editors_name_swap_abdc_ajg_20261028

Name and institution fields on the FT50 current boards, frozen 2026-10-28 09:48 Asia/Hong_Kong. This supersedes `editors_name_swap_20261028`. ABDC A*, A, B, and C, and the AJG-gap panels, are in the same freeze.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. It does not display `editor_name_raw`, and it does not invent a name. A row with an empty `editor_name` is not listed as a person. These two files have none.

## What changed

Both files are 10,046 rows (were 10,048 in `editors_name_swap_20261028`). The collector dropped two Review of Economic Studies rows whose affiliation was only LMU after Davide Cantoni and Claudia Steinwender were filled from that masthead. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (`Centro de Estudios Monetarios y Financieros`, high). No person is named `CEMFI` or `Sciences Po`.

`editors_ft50_current_with_ror.csv` has `ror_id` on 9,893 rows. `faculty_profile_url` is filled on 8,360 of 10,046 rows (83.2%) in both files. 1,686 rows are still blank. Twelve URLs that this freeze wrote only on the slim file were copied onto the matching blank ROR rows, with `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key`. A non-empty ROR URL was not replaced. Those twelve are the same seats as in `editors_ft50_utd24_faculty_20261025`. The directory name for the Liu seat stays `X. Liu`.

No person name was invented. ROR ids were not invented in this repository. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments are 159,104. FT50 seats are 10,045 across 50 journals. Top 5 appointments are 363. Faculty profile links on the directory are 21,658.
