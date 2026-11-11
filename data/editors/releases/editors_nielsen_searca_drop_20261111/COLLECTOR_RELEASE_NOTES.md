# editors_nielsen_searca_drop_20261111 (built 2026-11-11 08:09, Asia/Taipei; UNPUBLISHED)

Base: `releases/editors_open_items_followup_20261111` (live via PR #57, af8f5451). User-approved Marks-style DROP of exactly two rows, relayed by Econ-Journal-Web. Keyed on editor_row_key. Script: `nielsen_searca_drop_20261111.py`.

## Drops

### editors_abdc_a_current#42676 (Pete Doe)
Printed text (now only in notes): `Consultant (former Chief Research Officer, Nielsen), USA`
- Panel before: canonical already blank, raw as above, no ROR, country United States, continent North America.
- Panel after: raw also blank; still no institution name or ROR; country United States and continent North America kept. The printed text is appended to ror_notes as `nielsen_searca_drop_20261111: user-approved DROP (Marks); printed text: …`.
- Long table: raw_aff_part blanked; same printed text appended to ror_match_note; ror_id/ror_name remain blank; ror_country United States kept; is_panel_ror=0.

### editors_abdc_c_current#15559 (Maria Celeste H. Cadiz)
Printed text (now only in notes): `Independent consultant (formerly SEARCA Knowledge Management Department Head)`
- Panel before: canonical already blank, raw as above, no ROR, no country, no continent.
- Panel after: raw also blank; institution, ROR, country and continent remain blank. Printed text appended to ror_notes in the same Marks form.
- Long table: raw_aff_part blanked; printed text appended to ror_match_note; ROR and country remain blank; is_panel_ror=0.

## Left untouched
- abdc_c#15558 still carries SEARCA 04qf4zf50, Philippines (byte-identical to base).
- Diamond Leadership Institute (abdc_b#16107) is byte-identical to base.
- Only these two publish-panel rows differ from the base.
- The abdc_a pilot twin `editors_abdc_a_current_with_profile_pilot#42152` (same Pete Doe / Nielsen text) was skipped and left byte-identical. Logged.

## Directory (Web build on a copy)
- before: 11,186 / 6,696 / 6,696 / 169 / 43 (reproduces the live counts)
- after:  11,184 / 6,696 / 6,696 / 169 / 43
- Shared-name guard stays 43; no change needed.
- Appointments without an institution: 13,413 -> 13,415 (the two dropped rows).

## QC: ok
- Row counts, headers and line endings unchanged. Long table 269,545 rows. AJG1 12,326 (nav 10 untouched), AJG2 5,462, FT50 10,049/10,049. Pilots byte-identical.
- The only raw edits are these two approved Marks DROPs. 0 invented RORs. Protected names intact. 0 emails or phones.
- Panel–long mismatches: 0 on changed rows; 884 on the full table (same as base).
