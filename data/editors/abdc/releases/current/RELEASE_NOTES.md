# editors_blank_rescrape_20261028

Blank `editor_name` rows on the ABDC boards, frozen 2026-10-28 Asia/Hong_Kong. This supersedes the parked blanks in `editors_name_swap_abdc_ajg_20261028`. FT50 notes are in [`../../../ft50/releases/current/RELEASE_NOTES.md`](../../../ft50/releases/current/RELEASE_NOTES.md). AJG-gap notes are in [`../../../abs_ajg_gap/releases/current/RELEASE_NOTES.md`](../../../abs_ajg_gap/releases/current/RELEASE_NOTES.md).

`editor_name` is the name the directory shows. Empty `editor_name` is 0 on all four files. The standing rule still drops an empty name from the person directory. The build does not invent a name or a ROR id. A bare country is not an institution.

## Files

| File | Rows | Empty `editor_name` | `ror_id` filled | `faculty_profile_url` |
|---|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,182 | 0 | 23,834 | 8,467 |
| `editors_abdc_a_current.csv` | 45,363 | 0 | 43,343 | 5,202 |
| `editors_abdc_b_current.csv` | 42,139 | 0 | 39,993 | 3,123 |
| `editors_abdc_c_current.csv` | 26,858 | 0 | 24,106 | 1,228 |

Restored from cached or live HTTP, replacing the old board: Negotiation Journal 52, Labour 20, International Journal of Urban and Regional Research 78, Global Business and Organizational Excellence 33, Higher Education Quarterly 46, South African Journal of Economic and Management Sciences 27. Business and Society Review kept its named rows and dropped the empty one (79 rows).

Residual Taylor & Francis and World Scientific orphans with no recoverable person were dropped, not given a name: Business History and Regional Studies on A*, and on C the empty rows at Climate Policy, Journal of Arts Management Law and Society, International Journal of Healthcare Management, Journal of Biopharmaceutical Statistics, International Journal of Financial Engineering, and Journal of Financial Management, Markets and Institutions. Those titles are on a needs-browser queue outside this repository.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site.
