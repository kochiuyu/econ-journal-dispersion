# editors_weird_inst_fix_20261110

Base: releases/editors_country_misprint_fix_20261110. Built from /workspace/institutions_weird_send_20261110.csv (non-REVIEW rows only); every REVIEW row of institutions_weird_post53_20261110.csv untouched.
Script: abs_ajg/scripts/weird_inst_fix_20261110.py (+ weird_inst_strip_rules_20261110.py, data/weird_strip_overrides_20261110.tsv, data/weird_rematch_skips_20261110.json).

## Changes
| Action | Institutions changed | Publish rows | ft50_current mirror | Pilot rows | Long rows |
|---|---|---|---|---|---|
| DROP | 178/187 | 391 | 0 | 180 | 505 |
| country_only_fallback | 5 | 5 | 0 | 3 | 8 |
| STRIP | 594/715 | 632 | 0 | 313 | 55 |
| SET_COUNTRY | 122/124 | 137 | 0 | 85 | 222 |
| uga_fix | 1 | 7 | 2 | 2 | 11 |
| REMATCH | 186/214 | 249 | 6 | 98 | 124 |

- DROP = Marks mechanism (edpacs_marks_country_fix): canonical, raw_affiliation and ROR blanked, printed text traced in ror_notes; long raw_aff_part blanked with trace in ror_match_note; geo kept (country describes the editor). Country-only fallbacks 'Greece and UK', 'Italy & UK', 'Finland and Tanzania', 'SE, UK' and the Solicitor string dropped the same way.
- DROP guard: 120 rows (publish+pilot) whose printed raw still names an organisation (canonical over-stripped by an earlier pass, e.g. 'Tokyo' for 'Tokyo Institute of Technology', 'Sydney' for 'Sydney Law School', 'Nottingham' for 'Nottingham University Business School China', 'T' for 'T-Mobile') were NOT dropped; logged with a suggested canonical. DROP Institutions with all rows skipped: Adelaide, Director, Edinburgh, Gothenburg, Lausanne, Newcastle, Nottingham, Southampton, T.
- STRIP: role prefix cut to the organisation; addresses/postcodes, URLs, punctuation, trailing state/country codes removed; 11 results equal an existing Directory ROR name and take that ROR.
- SET_COUNTRY from trailing state/code (US states, UK, NZ, NSW, HK); DE/IN/CA/AB treated as ambiguous.
- UGA fix: US University of Georgia rows carried Tbilisi ROR 02bjhwk41 + country Georgia -> 00te3t702 / United States / North America. Georgian (Tbilisi) rows untouched.
- REMATCH via twin_name/twin_ror, only RORs already in panels; near-miss pairs (Bolton/Boston, IIT/Indiana, Queen's Belfast/Canada, Tokyo Tech/Science Tokyo, Petru Maior/Palade, Aachen/RWTH) never merged.

## Directory (edj-web working copy, build_site.py)
Base requested 15,159 / 6,387 / 6,387 / 162; the working copy at HEAD 283a746 + Web's misprint edits builds 15,160.
- Before: 15,160 Institutions, 6,387 with ROR, 6,387 distinct ROR, 162 countries
- After:  14,672 Institutions, 6,387 with ROR, 6,387 distinct ROR, 162 countries; shared names 69 (guard ok)
- Aggregates: 2,853 journals (2,426 with a field, 2,835 with a board link), 14,672 institutions (6,387 with ROR, 69 shared names), 12,460 appointments without an institution

## QC
verify ok=True: row counts unchanged (AJG1 12,326 incl. 10 nav untouched, AJG2 5,462, long 269,539); no header/EOL changes; no invented ROR; no ROR changes outside UGA; raw_affiliation changed only on DROP rows, all traced (513); raw_aff_part blanked only on DROP (513); panel<->long desync 0; 11KBW, UNSW, INSEAD FR 00ghzk478 / SG 05ynf4333 intact; non-Latin canonicals kept; protected rows 0.

## Files
WEIRD_INST_changes_20261110.csv (change log), WEIRD_INST_skipped_20261110.csv (160 Institution skips + 120 row skips, with reasons), _summary_20261110.json.
Pilots changed consistently but are not in the publish set.
