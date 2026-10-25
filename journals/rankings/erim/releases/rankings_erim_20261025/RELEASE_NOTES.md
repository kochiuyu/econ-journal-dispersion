# ERIM Journals List Core 2024–2028 freeze

- **Freeze id:** `rankings_erim_20261025`
- **Source page:** <https://www.eur.nl/en/erim/erim/journal-list>
- **Core file:** EJL Core List 2024-2028
  <https://www.eur.nl/en/erim/media/2026-02-erim-journal-list-core-list-2024-2028>
- **Retrieved:** 2026-10-25. Core list only. The intranet full list is not in this freeze.
- **Columns used:** ISSN, eISSN, Journal, `EJL Class 2024 - 2028`, Track.
- **Ratings:** the Core class string, unchanged: STAR 44, M-STAR 3, P 69, EP* 3, PA 5, S 144, S (3=1) 7, M 8. `rating` = `rating_raw`.
- **Field:** the Core Track code (`LIS`, `F&A`, `ORG`, `GEN`, `MKT`, `S&E`, and the combined tracks as published).
- **Edition:** `2024–2028`.
- **Raw xlsx:** not in this repository.

## Edition

| Edition | Rows | Matched | Match % |
|---|---:|---:|---:|
| 2024–2028 | 283 | 257 | 90.8% |

- **Unmatched rows:** 26
- **Conflicts:** 1

## Mapping

- ISSN to FT50 / core49 / ABDC A*/A/B/C, then a unique normalized title.
- Primary `journal_id` prefers FT50, then core49, then ABDC A*/A/B/C.
- An empty eISSN stored as 0 in the workbook is blank.
- No invented journal ids or classes. STAR is not renamed to P*.

## Conflicts

- Business Ethics-A European Review: issn business_ethics_environment_responsibility vs title business_society (freeze-title)

The kept id is the ISSN hit. `Business Ethics-A European Review` (ISSN 0962-8770) is the journal continued as Business Ethics, the Environment & Responsibility. A title hit on Business & Society was not used.
