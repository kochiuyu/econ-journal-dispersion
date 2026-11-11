# Nielsen / SEARCA Marks drops — editors_nielsen_searca_drop_20261111

Published 2026-11-11 (Asia/Taipei). The Collector freeze is applied on top of `editors_open_items_followup_20261111` (main `af8f5451`, PR #57).

## Why

PR #57 blanked the institution and ROR on Nielsen abdc_a#42676 and the SEARCA consultant abdc_c#15559, but left the printed raw text in place, so the Directory still listed those two rows under the printed-text labels. The user approved Marks-style DROPs of those two rows only.

## What changed

The Directory took `NIELSEN_SEARCA_DROP_directory_diff_20261111.csv`, keyed on `file` + `editor_row_key`: 2 cells (`raw_affiliation` blanked), 0 old-value mismatches, 0 missing keys. `ror_notes` comes from the freeze on those two rows. The long table blanks `raw_aff_part` on the same two parts and traces the printed text in `ror_match_note`.

| Row | Applied |
|---|---|
| abdc_a#42676 Nielsen (Pete Doe) | Marks-style DROP. Institution name, raw text and ROR blank; printed text `Consultant (former Chief Research Officer, Nielsen), USA` kept in `ror_notes` / `ror_match_note`; country United States and continent North America kept. |
| abdc_c#15559 SEARCA consultant (Maria Celeste H. Cadiz) | Same drop; printed text `Independent consultant (formerly SEARCA Knowledge Management Department Head)` kept in the notes; no country or continent. |
| Left untouched | abdc_c#15558 still carries SEARCA `04qf4zf50`. Diamond Leadership Institute (abdc_b#16107) is unchanged. The unpublished abdc_a pilot twin was skipped. |

Rows changed: A 1, C 1. All other panels are unchanged. Row counts are unchanged (ajg1 12,316, ajg2 5,462, FT50 10,047). The long table `data/editors/releases/editors_nielsen_searca_drop_20261111/editor_affiliations.csv.gz` keeps the published 181,449 parts, with 2 parts changed. Pilot files are not published. `CITATION.cff` is unchanged.

## Directory

| | PR #57 (live) | This freeze |
|---|---:|---:|
| Institutions | 11,186 | 11,184 |
| With ROR id | 6,696 | 6,696 |
| Countries | 169 | 169 |
| Shared display names | 43 | 43 |
| Appointments without institution | 13,413 | 13,415 |

The shared-name guard in `scripts/build_site.py` stays 43. The two printed-text Institutions labels are removed.

## Checks

- Protected names and near-miss pairs are unchanged.
- `site/data` and the pinned files contain 0 emails and no phone numbers.
