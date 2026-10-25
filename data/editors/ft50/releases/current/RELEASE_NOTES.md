# editors_display_names_20261025

Display names on the FT50 current boards, cleaned 2026-10-25 20:20 Asia/Hong_Kong. Source script: `scripts/clean_display_names.py` in the Editor-Collector. This folder still has the faculty-profile columns from `editors_ft50_faculty_20261025`. Those columns were not edited.

`editor_name` is the name the directory shows. `editor_name_raw` is the pre-clean value when the name changed, and blank when it did not. The build does not invent a name and does not display `editor_name_raw`.

`CHANGE_LOG.csv` from the collector freeze is about 6MB and is not used by the site. It is not in this repository.

## Rules

1. Strip trailing degrees and credentials (PhD, Ph.D., MD, MBA, MSc, and the same class of tokens) and leading titles (Dr., Prof., Professor).
2. Turn ALL-CAPS person names into title case. Particles such as `van` and `de` stay lowercase in the middle of a name.
3. Expand a bare given initial only when another row has a fuller given with the same initial and surname, and the same `ror_id`, the same normalized `raw_affiliation`, or the same `faculty_profile_url` / `faculty_home_page`. Conflicts stay as printed. No web lookup and no invented given name.

Order: degree strip, then case, then initial expansion.

## Files

| File | Rows | `editor_name` changed |
|---|---:|---:|
| `editors_ft50_current.csv` | 10,050 | 1,368 |
| `editors_ft50_current_with_ror.csv` | 10,050 | 1,397 |

The slim file expanded 87 initials. The ROR file expanded 117, because some identity evidence sits on columns the slim file does not use the same way. `scripts/build_site.py` reads the ROR file when it is present.

Collector totals across FT50, ABDC, and the AJG-gap live panels: 179,571 rows, 21,732 changed, 17,757 degrees stripped, 2,933 case fixes, 1,306 initials expanded, 2,928 bare initials left as printed. This repository omits 14 AJG-gap rows that the public gap freeze had already excluded, so the committed panels are 179,557 rows and 21,731 changed names. See the ABDC and AJG-gap notes.

## Examples

| Change | Before | After |
|---|---|---|
| Degree | `Dimitris Papanikolaou, PhD` | `Dimitris Papanikolaou` |
| Degree | `Philipp Schnabl, PhD` | `Philipp Schnabl` |
| Case | `PAUL HRIBAR` | `Paul Hribar` |
| Case | `LISA DE SIMONE` | `Lisa de Simone` |
| Initial | `M. Akturk` | `M. Serkan Akturk` |
| Initial | `P. Arora` | `Priyank Arora` |

Left as printed: `R. Preston McAfee` and `B. Douglas Bernheim` (a full given already follows the initial), and bare initials with no cross-panel identity evidence, such as `P. Ahlstrom` and `C. Carter` on the Journal of Operations Management.

Journal of Operations Management associate editor `S. Dhanorkar` is `Suvrat Dhanorkar` on both FT50 files (`editor_name_raw` is `S. Dhanorkar`). The ABDC A* copy of that seat is still `S. Dhanorkar`: that row has no faculty URL, and the cleaner did not treat its ROR and affiliation text as the same identity as the fuller form. The directory reattaches that ABDC row and shows the FT50 name. It does not write a new name into the ABDC file.

One Journal of Business Venturing review-board line was stored twice, once as `Trish Ruebottom, PhD` and once as `Trish Ruebottom`. After the degree strip the directory keeps one appointment.

## Unchanged from editors_ft50_faculty_20261025

`faculty_profile_url` is still filled on 8,199 of 10,050 rows (81.6%). `faculty_home_page` is still filled on 1,824 rows. ROR ids were not edited (9,895 rows on the ROR file still have one). A non-empty profile URL was not replaced. The directory links `faculty_profile_url` when it is http(s) and does not contain an email. It does not link `faculty_home_page`, and it does not invent an OpenAlex or ORCID person link. Where an FT50 appointment is also on an ABDC board, display fields, including the profile URL, come from the FT50 ROR file. A blank FT50 profile URL may be filled from the ABDC partner.

Emails, phone numbers, and photos are not written to the site. This release has no raw HTML and no search cache.
