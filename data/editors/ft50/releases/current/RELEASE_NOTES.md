# editors_blank_rescrape_20261028

Blank `editor_name` rows left by `editors_name_swap_abdc_ajg_20261028` are cleared, frozen 2026-10-28 Asia/Hong_Kong. FT50 itself had no empty names. These two files stay 10,046 rows.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. It does not invent a name. An empty `editor_name` is not listed as a person. These files have none.

`ror_id` is filled on 9,893 rows. `faculty_profile_url` is filled on 8,360 of 10,046 rows (83.2%) in both files. 1,686 rows are still blank. Twelve URLs that this freeze wrote only on the slim file were copied onto the matching blank ROR rows, with `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key`. A non-empty ROR URL was not replaced. Kurt Mitman stays at CEMFI with ROR `https://ror.org/035h6g182` (high). No person is named `CEMFI` or `Sciences Po`.

No person name was invented. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments are 158,716 (were 159,093 before `editors_blank_rescrape_browser_20261028`). FT50 seats stay 10,045 across 50 journals. Top 5 appointments stay 363. Faculty profile links on the directory are 21,652.
