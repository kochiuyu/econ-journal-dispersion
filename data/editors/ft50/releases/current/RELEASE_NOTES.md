# editors_current_20261025

This FT50 current release is the same freeze as the ABDC current boards (2026-10-25).

Full notes: [`../../../abdc/releases/current/RELEASE_NOTES.md`](../../../abdc/releases/current/RELEASE_NOTES.md).

## Files

`editors_ft50_current.csv` is the slim freeze: 10,050 rows, with no ROR columns. Person profile columns are `faculty_profile_url`, `faculty_home_page`, `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key`. `faculty_profile_url` is filled on 4,724 rows (47.0%). `faculty_home_page` is filled on 1,824 rows (18.1%).

`editors_ft50_current_with_ror.csv` is the file `scripts/build_site.py` reads when it is present (`FT50_CANDIDATES` prefers it over the slim CSV). The freeze did not ship ROR columns, and this repository has no script that rebuilds them. The existing imputation, OpenAlex, RePEc, and ROR columns were left in place (9,895 rows still have `ror_id`). The five `faculty_*` columns were copied from the slim freeze on the same row order. Journal, role, and year match on every row. Shared board fields were not overwritten, so person-only `editor_name` values and filled affiliations already on this file stay as they were. `ror_id` was not changed.

The public directory links a name to `faculty_profile_url` when that value is a non-empty http(s) URL. It does not link `faculty_home_page`, and it does not invent OpenAlex or ORCID person links.
