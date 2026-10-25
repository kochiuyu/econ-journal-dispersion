# editors_ft50_faculty_masthead_20261025

FT50 current boards after filling blank `faculty_profile_url` cells from journal masthead website anchors on 2026-10-25 (Asia/Hong_Kong). The new links are the "website" anchors already on the MIS Quarterly editorial board. ABDC and AJG-gap panels are not part of this freeze.

`editor_name` and `editor_name_raw` are still freeze `editors_display_names_20261025`. This pass left both columns as they were. The directory shows `editor_name`. It does not display `editor_name_raw`, and it does not invent a name.

## Files

`editors_ft50_current.csv` is the slim panel: 10,050 rows, with no ROR columns. Person profile columns are `faculty_profile_url`, `faculty_home_page`, `faculty_match_method`, `faculty_match_confidence`, and `faculty_person_key`. `faculty_profile_url` is filled on 8,211 rows (81.7%), up from 8,199 rows (81.6%) in `editors_ft50_faculty_20261025` and from 4,724 rows (47.0%) in `editors_current_20261025`. 1,839 rows are still blank. `faculty_home_page` is still filled on 1,824 rows (18.1%).

`editors_ft50_current_with_ror.csv` is the file `scripts/build_site.py` reads when it is present (`FT50_CANDIDATES` prefers it over the slim CSV). It has the same 10,050 rows and the same `faculty_*` values, including `faculty_profile_url` on 8,211 rows (81.7%). ROR, imputation, OpenAlex, and RePEc columns match the previous file in this folder. `ror_id` was not changed (9,895 rows still have one). The five `faculty_*` columns changed only where `faculty_profile_url` had been blank: 12 new URLs, all `masthead_website` at high confidence. A non-empty `faculty_profile_url` was not replaced, and no filled URL was cleared.

## Fill

| Milestone | Filled / 10,050 | Fill % |
|---|---:|---:|
| `editors_current_20261025` | 4,724 | 47.0% |
| `editors_ft50_faculty_20261025` | 8,199 | 81.6% |
| This freeze | 8,211 | 81.7% |

| Scope | Before | After |
|---|---:|---:|
| FT50 overall | 8,199 / 10,050 (81.6%) | 8,211 / 10,050 (81.7%) |
| MIS Quarterly | 66 / 81 (81.5%) | 78 / 81 (96.3%) |

Blank cells were not filled with invented OpenAlex, ORCID, or Google Scholar links. Each new URL is an http(s) page the journal already listed.

## MIS Quarterly

Twelve senior and associate editors whose `faculty_profile_url` was blank now use the masthead website anchor. `faculty_match_method` is `masthead_website` and `faculty_match_confidence` is `high`.

| Editor | Role | `faculty_profile_url` |
|---|---|---|
| Miguel Godinho de Matos | Senior Editors | https://www.clsbe.lisboa.ucp.pt/pt-pt/pessoa/miguel-godinho-matos |
| Matti Rossi | Senior Editors | https://research.aalto.fi/en/persons/matti-rossi/ |
| Mari-Klara Stein | Senior Editors | https://www.etis.ee/CV/Mari-Klara_Stein/eng/ |
| Abayomi Baiyere | Associate Editors | https://smith.queensu.ca/faculty_and_research/faculty_list/abayomi-baiyere.php |
| Leona Chandra Kruse | Associate Editors | https://www.uia.no/english/about-uia/employees/leonac/ |
| Seung Hyun Kim | Associate Editors | https://ysb.yonsei.ac.kr/faculty.asp?mid=n02&uid=107 |
| Zhepeng (Lionel) Li | Associate Editors | https://www.hkubs.hku.hk/people/zhepeng-li/ |
| Alexander Maedche | Associate Editors | https://h-lab.win.kit.edu/team_maedche.php |
| Sabine Matook | Associate Editors | https://about.uq.edu.au/experts/1654 |
| Mareike Möhlmann | Associate Editors | https://www.mareikemohlmann.com/ |
| Rene Riedl | Associate Editors | https://fh-ooe.at/studienangebot/digital-business-management-master/personen-kontakt |
| Xiao Xiao | Associate Editors | https://www.cbs.dk/en/research/departments-and-centres/department-of-digitalization/staff/xxdigi |

Example: Abayomi Baiyere (Associate Editors, Queen's University) is https://smith.queensu.ca/faculty_and_research/faculty_list/abayomi-baiyere.php. That cell was blank before this freeze.

Three MIS Quarterly rows stay blank. They are staff roles with no masthead website anchor: Kaylee Brosius, Todd Balazovic, and Monica Birth.

Two masthead website anchors have no panel row (Eric Zheng; Yingjie Zhang). This freeze does not add rows for them.

Only MIS Quarterly had a per-editor website anchor on the FT50 board HTML. Other journals were left unchanged.

## Rules

1. Fill only where `faculty_profile_url` was blank.
2. Leave a non-empty URL as it was.
3. Reject `mailto:` links and links on `misq.umn.edu`.
4. Keep the http(s) page the journal listed.
5. Match on the normalized `editor_name`.
6. Set `faculty_match_method` to `masthead_website` and `faculty_match_confidence` to `high`.
7. Leave an unmatched masthead name unmatched. No new web search.

## Display names

Unchanged from `editors_display_names_20261025`. `editor_name` is the cleaned display name (degrees and leading titles removed, ALL-CAPS names in title case, a bare initial expanded only from another row with the same identity evidence). `editor_name_raw` is the pre-clean value when the name changed, and blank when it did not. The slim file has 1,368 non-empty `editor_name_raw` cells. The ROR file has 1,397. This freeze did not edit either column.

## Public site

The public directory links a name to `faculty_profile_url` when that value is a non-empty http(s) URL. It prefers that column over `faculty_home_page`. It does not link `faculty_home_page`, and it does not invent an OpenAlex or ORCID person link. Where an FT50 appointment is also on an ABDC board, display fields, including `faculty_profile_url`, come from this FT50 file. A blank FT50 profile URL may be filled from the ABDC partner. A non-empty FT50 URL is not replaced.

Emails, phone numbers, and photos are not written to the site. ORCID, OpenAlex, and RePEc ids stay on the ROR CSV and are not published as person links. This release has no raw HTML and no search cache.
