# editors_name_swap_20261028

Name and institution fields on the FT50 current boards, frozen 2026-10-28 09:31 Asia/Hong_Kong. This supersedes the name fields of `editors_display_names_20261025` and `editors_ft50_utd24_faculty_20261025` on these two files. ABDC A* and A, and the AJG-gap panels, are in the same freeze. ABDC B and C were not edited.

`scripts/build_site.py` reads `editors_ft50_current_with_ror.csv` when it is present. The directory shows `editor_name`. It does not display `editor_name_raw`, and it does not invent a name. A row with an empty `editor_name` is not listed as a person.

## What changed

The collector change log has 174 actions. On these two files the actions are: drop the two Review of Economic Studies orphan rows whose `editor_name` was `CEMFI` or `Sciences Po` (the people were already on the board); sync 57 Journal of Finance names on the slim file from the ROR file, where the person and the institution had been stored in one cell; split Douglas Cumming from Florida Atlantic University on Journal of Business Venturing; set Kurt Mitman `raw_affiliation` to `CEMFI` with ROR `https://ror.org/035h6g182` (`Centro de Estudios Monetarios y Financieros`, high); and clean leading commas on Sciences Po affiliations.

Both files are 10,048 rows (were 10,050). `editors_ft50_current_with_ror.csv` has `ror_id` on 9,893 rows. `faculty_profile_url` is filled on 8,360 of 10,048 rows (83.2%) in both files. 1,688 rows are still blank. Twelve URLs that this freeze wrote only on the slim file were copied onto the matching blank ROR rows, with `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key`. A non-empty ROR URL was not replaced. Those twelve are the same seats copied in `editors_ft50_utd24_faculty_20261025`: Christof Brandtner, Sule Alan, Todd Schoellman, and the Journal of Operations Management rows Vivek Astvansh, Maria Besiou, Mahyar Eftekhar, Larry Fredendall, Mark Johnson, X. Liu, Richard Metters, Jeff Shockley, and Sean Wan. The directory name for the Liu seat stays `X. Liu`.

No person name was invented. ROR ids were not invented in this repository. Emails, phone numbers, and photos are not written to the site.

## Public site

Directory appointments are 159,308 (were 159,399). FT50 seats are 10,047 across 50 journals. Top 5 appointments are 365. Review of Economic Studies no longer has a person named `CEMFI` or `Sciences Po`. Kurt Mitman is one directory row at Centro de Estudios Monetarios y Financieros. Journal of Finance shows `Antoinette Schoar`, not the mashed institution string. Faculty profile links on the directory are 21,658.
