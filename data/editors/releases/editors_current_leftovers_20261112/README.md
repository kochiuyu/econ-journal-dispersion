# editors_current_leftovers_20261112 — current-board leftovers (UNPUBLISHED)

Built on `editors_leftover_fixes_20261112`, the live Directory (PR #69, 59652942). It contains only Collector-doable, evidenced fixes from the 2026-11-12 open-item list, under the user's "Yes, unless you think only RA can fix, you can fix those?".

| Item | Panel rows | What |
|---|---:|---|
| D_ET ATTACH / DROP | 2 / 2 | The European Transport official board (https://istiee.unict.it/content/editorial-advisory-board, fetched 2026-11-12) prints the affiliations that had been scraped into the next row's name. |
| D_JMID ATTACH / DROP | 5 / 17 | JMID official board (https://www.mechanism-design.org/, fetched 2026-11-12): 5 attach + phantom DROP pairs, and 12 non-person rows. |
| E_school_unit REMATCH | 27 | AMSE 02ek9wp67, EDHEC 05q7a8a02, IESEG 04jqeag92, Sant'Anna 025602r80, Budapest Business School 00r3jwh90 (own RORs); GWU 00y4zzh67, Nord 030mwrt98, Queen's (Canada) 02y72wh86, Temple 00kx1jb78, UCSD 0168r3w48, Edinburgh 01nrxwf90, Utrecht 04pp8hn57 (parent named in the printed school). |
| F_country FILL | 68 | ror_country/continent from the final country token of the printed raw; single-country strings only; no ROR. |

The long table carries the same changes on 117 keys. The 4 European Transport keys are panel-only, so no long rows were invented.

**Rules held.** Every ROR is API-active and already in the catalog; none were invented.
- raw_affiliation is changed only on DROP rows.
- On DROPs, country and continent are kept and the printed text goes to ror_notes / ror_match_note.
- There are no header, line-ending or row-count changes, and the pilots are byte-identical.
- The protected, held, near-miss, 11KBW, UNSW and INSEAD checks pass. Panel–long desync is 0, with 0 contacts.

**Left alone on purpose:** see `CURRENT_LEFTOVERS_skipped_20261112.csv` and the held lists in RELEASE_NOTES.md.

Files: `CURRENT_LEFTOVERS_changes_20261112.csv` (every field change), `CURRENT_LEFTOVERS_directory_diff_20261112.csv`, `CURRENT_LEFTOVERS_skipped_20261112.csv`, `_summary_20261112.json`, `_build.json`, and the script `current_leftovers_20261112.py` (also in `abs_ajg/scripts/`). Log: `abs_ajg/logs/current_leftovers_20261112.log`.
