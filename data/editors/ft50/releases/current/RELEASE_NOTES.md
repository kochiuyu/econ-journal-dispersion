# editors_ft50_utd24_faculty_20261025

FT50 current boards after a UTD24 faculty-profile fill on 2026-10-25 (Asia/Hong_Kong, 21:32). This freeze includes the MIS Quarterly masthead links from `editors_ft50_faculty_masthead_20261025` and adds profile URLs on other boards. ABDC and AJG-gap panels are not part of this freeze.

`editor_name` and `editor_name_raw` are still freeze `editors_display_names_20261025`. This pass left both columns as they were. The directory shows `editor_name`. It does not display `editor_name_raw`, and it does not invent a name.

The collector gap note `UTD24_FACULTY_GAP_20261025.md` is summarized below. The fill log `UTD24_FACULTY_FILLS_20261025.csv` is not used by the site and is not in this repository.

## Files

`editors_ft50_current.csv` is the slim panel: 10,050 rows, with no ROR columns. Person profile columns are `faculty_profile_url`, `faculty_home_page`, `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key`. `faculty_profile_url` is filled on 8,360 rows (83.2%), up from 8,211 (81.7%) in `editors_ft50_faculty_masthead_20261025`, 8,199 (81.6%) in `editors_ft50_faculty_20261025`, and 4,724 (47.0%) in `editors_current_20261025`. 1,690 rows are still blank. `faculty_home_page` is still filled on 1,824 rows (18.1%).

`editors_ft50_current_with_ror.csv` is the file `scripts/build_site.py` reads when it is present (`FT50_CANDIDATES` prefers it over the slim CSV). It has the same 10,050 rows. `faculty_profile_url` is filled on 8,360 rows (83.2%), the same count as the slim file. Twelve URLs that the collector wrote only on the slim file were copied onto the matching blank ROR rows, along with `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key`. A non-empty ROR URL was not replaced. ROR, imputation, OpenAlex, and RePEc columns are otherwise unchanged. `ror_id` was not changed (9,895 rows still have one). `faculty_person_key` on the copied rows is the slim-file key. The five `faculty_*` columns now match the slim file on every row.

## Fill

| Milestone | Slim file | ROR file |
|---|---:|---:|
| `editors_current_20261025` | 4,724 (47.0%) | 4,724 (47.0%) |
| `editors_ft50_faculty_20261025` | 8,199 (81.6%) | 8,199 (81.6%) |
| `editors_ft50_faculty_masthead_20261025` | 8,211 (81.7%) | 8,211 (81.7%) |
| This freeze | 8,360 (83.2%) | 8,360 (83.2%) |

On the 4,906-row set in the collector gap note, both files are filled on 4,320 rows (88.1%), up from 4,171 (85.0%). Blanks went from 735 to 586. That set is 23 journals. It includes Journal of Applied Psychology, Journal of Political Economy, and Quarterly Journal of Economics. Manufacturing and Service Operations Management, Production and Operations Management, and Review of Financial Studies had no new URLs in this pass and are outside that count.

| Journal | Rows | Blank before | Blank after | Filled | Fill % |
|---|---:|---:|---:|---:|---:|
| Academy of Management Journal | 120 | 14 | 11 | 3 | 90.8% |
| Academy of Management Review | 109 | 19 | 17 | 2 | 84.4% |
| Administrative Science Quarterly | 138 | 14 | 10 | 4 | 92.8% |
| Information Systems Research | 166 | 24 | 12 | 12 | 92.8% |
| Journal of Accounting and Economics | 54 | 1 | 1 | 0 | 98.1% |
| Journal of Accounting Research | 22 | 2 | 2 | 0 | 90.9% |
| Journal of Applied Psychology | 675 | 181 | 152 | 29 | 77.5% |
| Journal of Consumer Research | 260 | 23 | 15 | 8 | 94.2% |
| Journal of Finance | 57 | 0 | 0 | 0 | 100.0% |
| Journal of Financial Economics | 65 | 12 | 8 | 4 | 87.7% |
| Journal of International Business Studies | 338 | 74 | 66 | 8 | 80.5% |
| Journal of Marketing | 261 | 20 | 15 | 5 | 94.3% |
| Journal of Marketing Research | 222 | 13 | 12 | 1 | 94.6% |
| Journal of Operations Management | 266 | 110 | 65 | 45 | 75.6% |
| Journal of Political Economy | 45 | 9 | 9 | 0 | 80.0% |
| Management Science | 571 | 47 | 41 | 6 | 92.8% |
| Marketing Science | 142 | 10 | 10 | 0 | 93.0% |
| MIS Quarterly | 81 | 3 | 3 | 0 | 96.3% |
| Operations Research | 245 | 32 | 29 | 3 | 88.2% |
| Organization Science | 425 | 51 | 44 | 7 | 89.6% |
| Quarterly Journal of Economics | 35 | 2 | 0 | 2 | 100.0% |
| Strategic Management Journal | 410 | 54 | 46 | 8 | 88.8% |
| The Accounting Review | 199 | 20 | 18 | 2 | 91.0% |

MIS Quarterly stays at 78/81. The twelve masthead links from the previous pass are still here, including Abayomi Baiyere at https://smith.queensu.ca/faculty_and_research/faculty_list/abayomi-baiyere.php (`masthead_website`, high). Kaylee Brosius, Todd Balazovic, and Monica Birth stay blank.

## What was added

Blank cells only. New slim-file URLs, by method:

| Method | Rows | Confidence |
|---|---:|---|
| `masthead_href` | 40 | high |
| `masthead_website` | 10 | high |
| `web_search_near_miss` | 98 | 88 medium, 10 high |
| `web_search` | 1 | high |

Phase A is the 50 masthead links (`masthead_website` and `masthead_href`): ISR personal sites, JCR name links, JOOM sites, and AMR faculty pages. Phase B is the 98 near-miss and cached hits (`web_search_near_miss`). One further URL is `web_search` at high confidence: Annapoornima Subramanian, https://cde.nus.edu.sg/isem/staff/m-subramanian-annapoornima/. Eleven bad near-miss candidates were not kept (journal author pages, a salary site, a blog, an alumni page, and wrong-person pages).

Examples:

| Editor | Journal | URL | Method |
|---|---|---|---|
| Jane Feng | Information Systems Research | https://www.sem.tsinghua.edu.cn/en/info/1219/7156.htm | `masthead_website` |
| Jay Handelman | Journal of Consumer Research | https://smith.queensu.ca/faculty_and_research/faculty_list/handelman-jay.php | `masthead_href` |
| Benn Lawson | Journal of Operations Management | https://www.sbs.ox.ac.uk/about-us/people/benn-lawson | `web_search_near_miss` |

The largest remaining blanks on this 4,906-row set are Journal of Applied Psychology (152), Journal of International Business Studies (66), Journal of Operations Management (65), Strategic Management Journal (46), and Organization Science (44). This freeze does not add another search pass for them.

## Slim URLs copied onto the ROR file

These twelve `faculty_profile_url` values were on the slim file only. Each ROR cell was blank. The row match is `journal` + `year` + `editor_name` + `role` when that key is unique in both files. Where the ROR file keeps a fuller or shorter display name, the match is `journal` + `year` + `role` + `raw_affiliation`, plus a shared `editor_name` or `editor_name_raw`. `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key` were copied with the URL. `faculty_home_page` was already empty on both sides and was left as it was. No non-empty ROR URL was overwritten. Display names were not edited. The directory name for the Journal of Operations Management row is still `X. Liu` (the ROR `editor_name`); the URL is the one stored under `Xiaojin Liu` on the slim file.

| Editor on the slim file | Journal | URL |
|---|---|---|
| Christof Brandtner | Academy of Management Journal | https://sociology.stanford.edu/people/christof-brandtner |
| Sule Alan | Quarterly Journal of Economics | https://publicpolicy.cornell.edu/people/sule-alan/ |
| Todd Schoellman | Quarterly Journal of Economics | https://economics.stanford.edu/people/todd-schoellman |
| V. Astvansh | Journal of Operations Management | https://www.binghamton.edu/apps/directory/person/profile/vastvansh |
| M. Besiou | Journal of Operations Management | https://www.klu.org/faculty-research/faculty/resident-faculty/maria-besiou |
| M. Eftekhar | Journal of Operations Management | https://search.asu.edu/profile/2183845 |
| L. Fredendall | Journal of Operations Management | https://www.clemson.edu/business/about/profiles/FLAWREN |
| M. Johnson | Journal of Operations Management | https://www.wbs.ac.uk/about/person/mark-johnson/ |
| Xiaojin Liu | Journal of Operations Management | https://directory.business.vcu.edu/profile.php?urn=xliu22 |
| R. Metters | Journal of Operations Management | https://mays.tamu.edu/directory/rich-metters/ |
| J. Shockley | Journal of Operations Management | https://directory.business.vcu.edu/profile.php?urn=tjshockley |
| S. Wan | Journal of Operations Management | https://fisher.osu.edu/people/wan.207 |

## Display names

Unchanged from `editors_display_names_20261025`. `editor_name` is the cleaned display name. `editor_name_raw` is the pre-clean value when the name changed, and blank when it did not. The slim file has 1,368 non-empty `editor_name_raw` cells. The ROR file has 1,397. This freeze did not edit either column.

## Public site

The public directory links a name to `faculty_profile_url` when that value is a non-empty http(s) URL. It prefers that column over `faculty_home_page`. It does not link `faculty_home_page`, and it does not invent an OpenAlex or ORCID person link. Where an FT50 appointment is also on an ABDC board, display fields come from the FT50 ROR file. A blank FT50 profile URL may be filled from the ABDC partner. A non-empty FT50 URL is not replaced.

Emails, phone numbers, and photos are not written to the site. ORCID, OpenAlex, and RePEc ids stay on the ROR CSV and are not published as person links. This release has no raw HTML and no search cache.
