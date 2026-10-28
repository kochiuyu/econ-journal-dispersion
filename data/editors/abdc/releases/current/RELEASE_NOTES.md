# editors_name_swap_abdc_ajg_20261028

Name and institution fields on the ABDC A*, A, B, and C current boards, frozen 2026-10-28 09:48 Asia/Hong_Kong. This supersedes `editors_name_swap_20261028` and extends it to B and C. FT50 notes are in [`../../../ft50/releases/current/RELEASE_NOTES.md`](../../../ft50/releases/current/RELEASE_NOTES.md). AJG-gap notes are in [`../../../abs_ajg_gap/releases/current/RELEASE_NOTES.md`](../../../abs_ajg_gap/releases/current/RELEASE_NOTES.md).

`editor_name` is the name the directory shows. An empty `editor_name` is not a person. When that row has a `ror_id`, Institutions still counts the appointment and does not count an editor. The build does not invent a name or a ROR id.

Pure institution-as-name is 0 on these four files. Unrecovered org-as-name rows are parked with a blank `editor_name`.

## Files

| File | Rows | Empty `editor_name` | Of which have `ror_id` | `ror_id` filled | `faculty_profile_url` |
|---|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,185 | 3 | 1 | 23,835 | 8,467 |
| `editors_abdc_a_current.csv` | 45,363 | 0 | 0 | 43,343 | 5,202 |
| `editors_abdc_b_current.csv` | 42,145 | 5 | 4 | 40,000 | 3,129 |
| `editors_abdc_c_current.csv` | 26,875 | 37 | 33 | 24,107 | 1,228 |

A* dropped the two Review of Economic Studies LMU orphan rows with FT50. Its three empty names are Business History, and two Regional Studies rows (`GREThA`, and the Loughborough geography department). B’s five empty names are Labour (2), Negotiation Journal (2), and International Journal of Urban and Regional Research (1). C’s 37 empty names are mostly Global Business and Organizational Excellence (23), an institutions-only masthead, plus Journal of Arts Management Law and Society (6) and eight single rows.

`ror_id` counts include high, medium, and low-confidence ids already on these files. This repository did not add a ROR id.

## Public site

The directory does not list a blank name, `CEMFI`, or `Sciences Po`. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. There is no raw HTML in this release.
