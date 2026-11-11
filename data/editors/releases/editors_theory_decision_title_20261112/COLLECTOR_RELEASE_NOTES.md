# editors_theory_decision_title_20261112 (built 2026-11-12 00:39, Asia/Taipei; UNPUBLISHED)

Base: `releases/editors_campus_conflict_fix_20261111` (live via Directory PR #64, 004c6cfe).
Input: `/workspace/collector_journal_title_20261112/theory_decision_rename_20261112.csv` (72 rows, all `editors_abdc_a_current`, `abdc_journal_id` `theory_decision_international_journal`) and README.md.
User-approved, this journal only, relayed by Journal-Editor-Web (formerly Econ-Journal-Web; same agent). Keyed on editor_row_key. No affiliation or raw-text edits. Pilots byte-identical.
Script: `theory_decision_title_20261112.py`.

On each matching appointment, the display field `journal` was changed from

> Theory and Decision: an international journal for multidisciplinary advances in decision sciences

to

> Theory and Decision

`journal_name_abdc` was left as the long ABDC listed string (same long form as above). `abdc_journal_id` stays `theory_decision_international_journal`. No affiliations, ROR, names, roles, or other fields were changed. Other subtitled ABDC titles were not in the file and were not renamed. `journals/catalog_abdc_a.csv` was not edited.

## Applied 72 / 72 (0 skips)

Every file key was confirmed on `editors_abdc_a_current` with `abdc_journal_id` `theory_decision_international_journal` and with the long title in `journal` before the change.

The long table has a `journal` display column. It was updated to "Theory and Decision" on 77 long-table rows for these 72 keys (5 keys have a second affiliation row). Every other long-table field was left unchanged.

The 72 Theory and Decision rows on `editors_abdc_a_current_with_profile_pilot` use different keys and were not in the file; both pilot files are byte-identical to the base.

## Directory (Web build on a copy)
- before: 11,077 / 6,698 / 6,698 / 169 / 43 (reproduces the live counts)
- after:  11,077 / 6,698 / 6,698 / 169 / 43
- Shared-name guard stays 43; no change needed.
- Appointments without an institution stayed at 13,415.
- Institution counts are unchanged, as expected for a display-title-only edit.

## QC: ok
- Row counts, headers and line endings unchanged. Long table 269,545 rows. AJG1 12,326 (nav 10 untouched), AJG2 5,462, FT50 10,049/10,049. Pilots byte-identical.
- Only `journal` changed, on the 72 panel keys and their 77 long-table rows. `journal_name_abdc` unchanged on every row. No raw edits. 0 invented RORs. Protected names intact. 0 emails or phones.
- Panel–long mismatches: 0 on changed rows; 874 on the full table (874 in the base). Mismatch accounting is ROR/country, not journal title.
- Held campus and two-place rows, Diamond Leadership Institute, and the Nielsen/SEARCA rows were not in the file and were left as printed.
