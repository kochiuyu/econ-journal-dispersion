# editors_name_swap_20261028

Name and institution fields on the ABDC A* and A current boards, frozen 2026-10-28 09:31 Asia/Hong_Kong. This supersedes the name fields of `editors_display_names_20261025` on those two files. ABDC B and C were not edited. They are still freeze `editors_display_names_20261025`. FT50 notes are in [`../../../ft50/releases/current/RELEASE_NOTES.md`](../../../ft50/releases/current/RELEASE_NOTES.md). AJG-gap notes are in [`../../../abs_ajg_gap/releases/current/RELEASE_NOTES.md`](../../../abs_ajg_gap/releases/current/RELEASE_NOTES.md).

`editor_name` is the name the directory shows. An empty `editor_name` is not a person. These two files have no blank name with a `ror_id`, so the empty rows are not institution appointments. The build does not invent a name or a ROR id.

## Files

| File | Rows | Empty `editor_name` | Notes |
|---|---:|---:|---|
| `editors_abdc_a_star_current.csv` | 25,188 | 3 | Was 25,190. Dropped the Review of Economic Studies rows named `CEMFI` and `Sciences Po`. Blanked `New York University, Abu Dhabi` and `Department of Geography, Loughborough University, UK`. `GREThA` was already empty. |
| `editors_abdc_a_current.csv` | 45,363 | 0 | Same row count. Four evidenced person-plus-institution splits, including Cony Ho and Suzanne Makarem. |
| `editors_abdc_b_current.csv` | 42,193 | 0 | Not in this freeze. |
| `editors_abdc_c_current.csv` | 26,915 | 0 | Not in this freeze. |

On A*, Kurt Mitman `raw_affiliation` is `CEMFI` with ROR `https://ror.org/035h6g182` (high), and the Sciences Po affiliations no longer start with a comma. Douglas Cumming on Journal of Business Venturing is the person, with Florida Atlantic University in the affiliation. `faculty_profile_url` is still filled on 8,467 of 25,188 A* rows and 5,202 of 45,363 A rows. Those columns were not the subject of this freeze.

`ror_id` is filled on 23,834 A* rows and 43,342 A rows. Counts include high, medium, and the low-confidence ids already on these files. This repository did not add a ROR id.

## Public site

The directory does not list `CEMFI`, `Sciences Po`, or a blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. There is no raw HTML in this release.

## Unchanged on B and C (`editors_display_names_20261025`)

`editor_name` on B and C is still the cleaned display name from 2026-10-25. `editor_name_raw` is the pre-clean value when the name changed. Faculty columns, tenure columns, and `ror_id` on B and C were not edited. The public directory does not display tenure.
