# ShanghaiRanking top journals freeze

- **Freeze id:** `rankings_shanghai_20261025`
- **Survey page:** <https://www.shanghairanking.com/activities/aes>
- **2026 list:** <https://wjgs-rk.oss-cn-hangzhou.aliyuncs.com/univCn/gras/2026/Top_Journal_list_2026.pdf>
- **2024 list:** <https://www.shanghairanking.com/_pub/com/gras/2024/Top%20Journal%20list.pdf>
- **Retrieved:** 2026-10-25.
- **Subjects:** Economics, Business Administration, Finance, and Management. Other subjects in the PDFs, including Public Administration and Hospitality & Tourism Management, are not in this freeze.
- **Union:** a journal in more than one of those subjects is one row. `field` joins the subjects with `; `, in that subject order.
- **Rating:** `Top` on every row. Membership is binary. `rating` = `rating_raw`.
- **2026** rows are the Academic Excellence Survey.
- **2024** Economics, Finance, and Management rows are the Academic Excellence Survey. 2024 Business Administration rows are the Journal Citation Report block in that PDF.
- **Raw PDFs:** not in this repository.

## Editions

| Edition | Rows | Matched | Match % |
|---|---:|---:|---:|
| 2024 | 57 | 55 | 96.5% |
| 2026 | 19 | 19 | 100.0% |

Long panel: 76 rows, 74 matched (97.4%). Unmatched rows: 2. Conflicts: 0.

### 2026 subjects

Economics 5, Business Administration 6, Finance 3, Management 8. Academy of Management Journal, Administrative Science Quarterly, and Strategic Management Journal are in both Business Administration and Management, so the union is 19.

### 2024 subjects

Economics 5, Business Administration 41, Finance 3, Management 8. No title is in two subjects. The union is 57.

## Mapping

- No ISSNs in the PDFs. Match is a unique normalized title to FT50, then core49, then ABDC A*/A/B/C.
- Primary `journal_id` prefers FT50, then core49, then ABDC A*/A/B/C.
- `CORPORATE GOVERNANCE-THE INTERNATIONAL JOURNAL OF BUSINESS IN SOCIETY` is the catalog journal `Corporate Governance` (Emerald). That is the only manual title alias.
- Three 2024 titles lost a space at a line break in the PDF (`OF BUSINESS`, `BUSINESS MANAGEMENT`, `COMMERCE RESEARCH`). The stored title has the space.
- No invented journal ids. Economics is the classic top five and stays a subject, not a separate rating.

## Unmatched

- INTERNATIONAL JOURNAL OF ENGINEERING BUSINESS MANAGEMENT (2024)
- JOURNAL OF THEORETICAL AND APPLIED ELECTRONIC COMMERCE RESEARCH (2024)

## Source note

`source_file` is `shanghai-top-journals`. `source_note` is `ShanghaiRanking AES 2026`, `ShanghaiRanking AES 2024`, or `ShanghaiRanking JCR 2024`.
