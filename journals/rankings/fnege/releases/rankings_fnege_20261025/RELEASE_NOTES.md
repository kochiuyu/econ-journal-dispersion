# FNEGE Journal Quality List freeze

- **Freeze id:** `rankings_fnege_20261025`
- **Source:** FNEGE Journal Quality List
  <https://fnege.org/en/fnege-journal-quality-list/>
- **Retrieved:** 2026-10-25. One public table carries FNEGE 2019, 2022, and 2025.
- **Preferred edition:** 2025 (891 journals). 2019 and 2022 are the same table, kept because the columns are already there. A blank cell is not a row.
- **Ratings:** published grades `1*`, `1`, `2`, `3`, `4`, plus `EM` and `NC` where the cell says so. `rating` = `rating_raw`. The page does not define EM or NC.
- **Field:** the published `DOMAINE / FIELD` code.
- **Raw HTML:** not in this repository.

## Editions

| Year | Rows | Matched | Match % |
|---|---:|---:|---:|
| 2019 | 484 | 410 | 84.7% |
| 2022 | 669 | 577 | 86.2% |
| 2025 | 891 | 733 | 82.3% |

- **Long panel rows:** 2044
- **Matched:** 1720 (84.1%)
- **Unmatched rows:** 324
- **2025 grades:** 1* 31, 1 59, 2 153, 3 251, 4 393, EM 4
- **Conflicts:** 3

## Mapping

- ISSN (print, else electronic) to FT50 / core49 / ABDC A*/A/B/C, then a unique normalized title.
- When print and electronic ISSN hit different catalog ids, the id whose catalog title matches the FNEGE title is kept. Otherwise the row is unmatched.
- Primary `journal_id` prefers FT50, then core49, then ABDC A*/A/B/C.
- ISSNs that are not 8 characters (`en cours`, a 7-digit value) are blank. Zero-width spaces are stripped. `17511577`-style values are hyphenated.
- No invented journal ids or grades.

## Conflicts

- 2025 APPETITE: print issn jams vs e-issn appetite; kept appetite
- 2025 DECISION SCIENCES JOURNAL OF INNOVATIVE EDUCATION: print issn decision_sciences_journal_innovative_education vs e-issn journal_travel_research; kept decision_sciences_journal_innovative_education
- 2025 SYSTEMS RESEARCH AND BEHAVIORAL SCIENCES: print issn technology_society vs e-issn systems_research_behavioral_science; kept systems_research_behavioral_science
