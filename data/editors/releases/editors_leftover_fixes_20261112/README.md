# editors_leftover_fixes_20261112 (UNPUBLISHED freeze)

Base: editors_school_unit_leftover_20261112, which the web repo published at 4e00305 (2026-11-12 07:34 Asia/Taipei). The user approved this freeze in Collector chat on 2026-11-12 ("yes fix them").

## A. Three UK Henley rows → University of Reading (3 applied, 3 expected, 0 skipped)
- **Rows:** AJG1 #1185 and #2555 (Abby Ghobadian) and #2583 (Marc Day).
- **Printed raw:** "Henley Management College, UK", left unchanged. No mention of Africa.
- **Change:** Henley Business School / blank ROR → University of Reading / 05v62cm79 / United Kingdom.
- Henley Africa #18374 is untouched.

## B. Name-field phantoms (6 applied, 6 expected, 0 skipped)
- **REStud phantom rows** (editor_name "Universitat Pompeu Fabra"): ft50 #577, ft50 #578, with_ror #577, with_ror #578, dropped Marks-style.
  - Blanked: editor_name, raw_affiliation, canonical_name, ROR, country and continent. Rows #577 (both files) and slim #578 had carried raw "Barcelona School of Economics" with ROR 02k09n368, Spain.
  - The printed text is kept in ror_notes on the with_ror twins and in ror_match_note on the long table. The slim ft50 file has no ror_notes column.
  - Real editors #640 Enikolopov, #608 Penta and #627 Vanasco are untouched.
  - The live Directory already left these 4 rows out (its FT50 files have 10,047 rows), so the drop only cleans the source.
- **JLAS move:** AJG2 #5449, Sônia Miriam Draibe.
  - Set to Universidade Estadual de Campinas (UNICAMP) / 04wffgt70 / Brazil / South America.
  - affiliation_count 0 → 1. Raw left blank (not invented); the source string is in ror_notes.
- **JLAS phantom:** AJG2 #5450, dropped Marks-style. Name "Universidade Estadual de Campinas, Brazil" blanked and kept in ror_notes.
- #5449 and #5450 have no long-table rows, so they stay panel-only; no long rows were invented.

## C. Long-table country sync (874 applied, 874 expected, 0 skipped)
- Every mismatch matched the pattern "panel has a country, long-table primary row is blank". All were synced from the panel.
- No pilot rows were involved, and no panel values changed.
- Panel–long mismatches: 874 → **0**.
- 2,879 panel keys still have no long-table row. They are left unmapped and none were invented.

## ROR API (fetched 2026-11-12, Asia/Taipei)
| ROR | Status | API name | API country |
|---|---|---|---|
| 05v62cm79 | active | University of Reading | United Kingdom |
| 04wffgt70 | active | Universidade Estadual de Campinas (UNICAMP) | Brazil |

Aliases for 04wffgt70 include "Universidade Estadual de Campinas". Both RORs are already on the panels; no new RORs were added.

## Directory
| | Institutions | With ROR | Distinct ROR | Countries | Shared names |
|---|---|---|---|---|---|
| Before | 11,075 | 6,698 | 6,698 | 169 | 43 |
| After | 11,074 | 6,698 | 6,698 | 169 | 43 |

- Appointments go 162,575 → 162,574, editors 112,719 → 112,718, and appointments without an institution 13,415 → 13,413.
- The shared-name guard stays at 43.
- **Web build change needed:** in `scripts/build_site.py`, change the AJG_GAP_FILES `ajg2` expected_dropped from **0 to 1**. Phantom #5450 now has a blank editor_name, and the builder drops blank-name rows with no ROR. Without this change the build stops with "dropped 1 names, expected 0". The after counts above were built with that one-line change.

## QC: verify ok=True
- Row counts, headers and EOL are unchanged; the long table has 269,545 rows. Pilots are byte-identical.
- Raw text changed only on the B drops.
- Nothing unexpected changed on panels or the long table. No invented RORs, no contacts.
- None of the 40 held rows changed.
- Untouched rows are unchanged: #640, #608, #627, #18374, the Nielsen/SEARCA/Diamond keys, and the JLAS neighbours #5448 and #5451.
