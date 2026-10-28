# editors_blank_rescrape_browser_20261028

Browser restore for Taylor & Francis, World Scientific, and Wiley boards, frozen 2026-10-28 10:17 Asia/Hong_Kong. This supersedes the Taylor & Francis-only browser pass and replaces the boards that `editors_blank_rescrape_20261028` had left for a later scrape. ABDC A and B are unchanged from that earlier freeze.

`editor_name` is the name the directory shows. Empty `editor_name` is 0. The build does not invent a name or a ROR id. A bare country is not an institution. Junk and non-person rows from the scrapes were dropped.

## Files

| File | Rows | What changed |
|---|---:|---|
| `editors_abdc_a_star_current.csv` | 25,178 | Business History 86→85. Regional Studies 63→60. `ror_id` on 23,822 rows. `faculty_profile_url` on 8,467. |
| `editors_abdc_a_current.csv` | 45,363 | Unchanged. Empty `editor_name` is 0. |
| `editors_abdc_b_current.csv` | 42,139 | Unchanged. Empty `editor_name` is 0. |
| `editors_abdc_c_current.csv` | 26,720 | Climate Policy 58→56. Journal of Arts Management Law and Society 63→37. International Journal of Healthcare Management 30→35. Journal of Biopharmaceutical Statistics 96→87. International Journal of Financial Engineering 174→93. Journal of Financial Management, Markets and Institutions 46→21. `ror_id` on 24,213 rows. `faculty_profile_url` on 1,228. |

Tong Fu is one row, role `Managing Editor; Associate Editors`, with the longer Guizhou affiliation. Newcastle upon Tyne rows match Newcastle University (United Kingdom). Tim Huijts keeps the ROA affiliation; the false ELTE Hungary ROR was cleared and no Maastricht id was invented.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site.
