# Open-items follow-up — editors_open_items_followup_20261111

Published 2026-11-11 (Asia/Taipei). The Collector freeze is applied on top of `editors_open_items_fix_20261111` (main `89aa2f09`, PR #56).

## Why

Four follow-ups to the open-items freeze were approved: revert Shenhar off Rutgers, set Bates to The University of Sydney (keeping UNSW as the second affiliation), clear the leftover faculty-match fields on FT50 #4634, and blank the former-employer institutions on Nielsen and SEARCA (GM already at the approved target).

## What changed

The Directory took `OPEN_ITEMS_FOLLOWUP_directory_diff_20261111.csv`, keyed on `file` + `editor_row_key`: 30 cells, 0 old-value mismatches, 0 missing keys. No `raw_affiliation` edits.

| Item | Applied |
|---|---|
| abdc_b#16107 Shenhar | Diamond Leadership Institute, Israel, no ROR (new institution). Rutgers `05vt9qd57` is a former employer. |
| abdc_b#39063 Bates | The University of Sydney `0384j8v12`, Australia. `affiliation_count` stays 2; UNSW `03r8z3t63` stays as the second affiliation (already on long-table aff_rank 2 and `other_ror_ids`). The UNSW master entry is unchanged. Not dropped. |
| FT50 #4634 (both rows) | `faculty_match_method` and `faculty_match_confidence` cleared. Institution remains Xi'an Jiaotong University `017zhmm22`. #4501 is untouched. |
| Nielsen abdc_a#42676 | Institution and ROR blanked; country United States kept. Printed text is unchanged, so the Directory may still list the printed-text label. |
| GM ajg1#4303 | Already on General Motors `05addee68`; left unchanged. |
| SEARCA abdc_c#15559 | Institution, ROR and country blanked. #15558 is unchanged and still carries `04qf4zf50`. Printed text is unchanged, so the Directory may still list the printed-text label. |

Rows changed: A 1, B 2, C 1, FT50 1 with_ror / 1 slim. AJG-gap panels are unchanged. Row counts are unchanged (ajg1 12,316, ajg2 5,462, FT50 10,047). The long table `data/editors/releases/editors_open_items_followup_20261111/editor_affiliations.csv.gz` keeps the published 181,449 parts, with 4 parts changed. Pilot files are not published. `CITATION.cff` is unchanged.

## Directory

| | PR #56 (live) | This freeze |
|---|---:|---:|
| Institutions | 11,185 | 11,186 |
| With ROR id | 6,697 | 6,696 |
| Countries | 169 | 169 |
| Shared display names | 43 | 43 |
| Appointments without institution | 13,413 | 13,413 |

The shared-name guard in `scripts/build_site.py` stays 43. Net +1 institution: Diamond Leadership Institute is new; the Bates "independent consultant…" label is gone (Sydney was already present). With-ROR −1: Nielsen's ROR was the only copy of `016x3qj75`.

## Checks

- Protected names (11KBW, UNSW, the INSEAD campuses, 1 Decembrie 1918, Bank of England) are unchanged. UNSW is still the second affiliation on Bates.
- No near-miss pair is merged.
- `site/data` and the pinned files contain 0 emails and no phone numbers.
