# editors_school_unit_leftover_20261112 (UNPUBLISHED freeze)

Base: editors_theory_decision_title_20261112 (live via Directory PR #67, 27e1a716).
Approval: user, 2026-11-12 ("Yes, freeze the 13 rematches"). The 6 name-field DROPs were NOT approved and are untouched.

## Applied: 13 of 13, 0 skips
Only canonical_name, ror_id, ror_name, ror_country and lat/lon changed. raw_affiliation stayed as printed on all 13 rows.
- NUBS China, 2 rows (abdc_a #4924 Patrick Chau, #5221 Y. Ye): set to University of Nottingham Ningbo China, 03y4dt428, China. Mastheads show China/Ningbo. UK Nottingham (01ee9ar58) was not used.
- UK Henley Management School/College, 3 rows (abdc_b #30182, #30664 Yipeng Liu; #31832 Abby Ghobadian): set to University of Reading, 05v62cm79, United Kingdom. Mastheads show "- UK". Henley Africa #18374 is untouched.
- RSM Erasmus, 8 rows (a_star #14113, #24564; a #40739; b #18143, #32487, #39125; c #20763, #22989): set to Erasmus University Rotterdam, 057w15z03, Netherlands.

## ROR API check (re-fetched 2026-11-12 07:26 Asia/Taipei)
| ROR | Status | API name | API country |
|---|---|---|---|
| 03y4dt428 | active | University of Nottingham Ningbo China | China |
| 05v62cm79 | active | University of Reading | United Kingdom |
| 057w15z03 | active | Erasmus University Rotterdam | The Netherlands |

No new ROR ids were added; all three were already on the published panels.

## Directory
| | Institutions | With ROR | Distinct ROR | Countries | Shared names |
|---|---|---|---|---|---|
| Before | 11,077 | 6,698 | 6,698 | 169 | 43 |
| After | 11,075 | 6,698 | 6,698 | 169 | 43 |

- Two blank-ROR names folded into existing ROR entries: "Nottingham University Business School China" and the blank-ROR "Rotterdam School of Management, Erasmus University". The two other RSM rows that already had ROR 057w15z03 are unchanged.
- The shared-name guard stays at 43.

## QC: verify ok=True
- Row counts, headers and EOL are unchanged. AJG1 is 12,326 rows with 10 nav rows untouched; AJG2 is 5,462; both FT50 files are 10,049.
- Pilots are byte-identical.
- Nothing unexpected changed on panels or the long table. No invented RORs, no near-miss merges, and no non-Latin names lost.
- 11KBW, UNSW, INSEAD FR/SG and 1 Decembrie 1918 are intact.
- No contacts (emails or phones) found.
- Long table: 269,545 rows, synced. Panel–long desync is 0 on changed rows and 874 on the full table (same as the base; all ror_country debt).
- None of the 40 held rows changed.
- Not-approved rows are unchanged: REStud #577/#578 (ft50 and with_ror), ajg2 #5449/#5450, and Henley Africa #18374.

## Follow-up, not applied
Three more UK Henley Management College rows are still blank. They were not in the RA inventory or the approval:
- ajg1 #1185 and #2555 (Abby Ghobadian)
- ajg1 #2583 (Marc Day)

Printed raw on all three is "Henley Management College, UK". They are candidates for the same Reading rematch if the user approves.
