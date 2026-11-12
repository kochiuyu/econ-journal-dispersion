# RELEASE NOTES — editors_current_leftovers_20261112

Status: **HELD / unpublished.** Base: editors_leftover_fixes_20261112.

## Applied (121 panel rows, 117 long keys)
- D: 7 attaches + 19 Marks-style DROPs (European Transport and JMID). See README.
- E: 27 school-unit rematches.
- F: 68 printed-country fills.

## Directory (build of a web copy with these panels)
Before: 11,074 institutions / 6,698 with ROR / 6,698 distinct / 169 countries / 43 shared names.
After: 11,065 / 6,698 / 6,698 / 169 / 43. Appointments without an institution: 13,413 → 13,387.
Required: `build_site.py` AJG_GAP_FILES ajg1 expected_dropped 15 → 32.

## Held (not changed)
- **JMID rest of board.** It needs a whole-board re-harvest (user decision):
  - "Former Editorial Members" (#11150–#11166) are listed as current Associate Editors.
  - Article authors (#11171–#11206, minus the titles dropped here) were scraped in as editors.
  - Many affiliations disagree with the site (e.g. Zaifu Yang, Kim-Sau Chung, John Hatfield, Herings, Pycia, Yamashita).
  - Kotowski #11113 (raw "Pennsylvania School of Arts" vs site "Notre Dame, USA", phantom #11114), Schwarz #11132 (raw Northwestern vs site Google Research, phantom #11133) and Kesten #11106 ("The University of Sydney Skip" vs site Carnegie Mellon) all need raw edits.
  - #11210 is an AJG1 nav row.
- **European Transport.** Di Matteo #15763 (site: ACI, Italy) and Bonera #15767 (site: Brescia Mobilità) have blank affiliations but no phantom row. That is a blank-affiliation fill, not a name-field fix.
- **E skips:**
  - EDHEC UK/Singapore campus rows (#40833, #33794, #35895), because distinct campuses stay distinct.
  - "Edinburgh Business School, UK" #29393, which may be Heriot-Watt.
  - "University of New York School of Law" #35355 (NYU or CUNY?).
  - "NWU Business School" #8580 (ambiguous, no country).
  - INCAE (Costa Rica ROR on Nicaragua rows), One School of Business (country conflict), PKU HSBC (held), all two-place strings, and IFoA (country conflict).
  - Schools that need outside knowledge to place: Kellogg, Rotman, Belk, Harbert, Arison, Osgoode, Schulich Law, Miami Herbert, USC Marshall and the like.
- **F skips:** rows whose display is a bare country (non-institution rows), "University of Illinois, UK" #34176 (conflict), "UNSW / Enterprise Analysts" #1943 (two-place, protected), and multi-country strings.
- **G:** All 6,698 live RORs are active in the ROR v2.15 dump (2026-10-20), so there are no successor swaps. The slim `editors_ft50_current.csv` differs from its with_ror twin on 82 ror_id / 81 country / 45 raw values. It is not read by the Directory, so this is held for a decision on which side wins. "The Netherlands" spelling remains on 2 rows (build_site normalises it).
