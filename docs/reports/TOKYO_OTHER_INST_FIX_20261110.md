# editors_tokyo_other_inst_fix_20261110

Published 2026-11-10 (Asia/Taipei) into the Directory current panels. It supersedes the `editors_tokyo_gatech_fix_20261110` current panels (PR #48). No site filter. `scripts/build_site.py` is unchanged.

## Scope

This fix covers the 35 remaining seats from the collector's "Italian Cultural Institute" place-strip rewrite (see `docs/reports/TOKYO_GATECH_FIX_20261110.md`). On the Directory those seats kept their printed text but had `canonical_name` = `Tokyo` and a blank ROR, so they showed as `Tokyo` and Institutions grouped them into one unmatched `Tokyo` (Japan) row with 35 appointments.

The rows are all on ABDC: A* 1, A 7, B 13, C 14.
- **Rematched (23):** to the printed institution's ROR id.
- **Tokyo Institute of Technology (11):** ROR left blank. They are not mapped to Institute of Science Tokyo `05dqf9946`, because on the panels that id is only used for seats printed as Institute of Science Tokyo.
- **Fuhito Kojima, Theoretical Economics (1):** printed `Tokyo` with blank canonical and ROR.

Six of the ROR ids were not on the published panels: `00ws30h19`, `048nxq511`, `03b0ym704`, `00khh5r84`, `03kjjhe36`, and `027tyzk91`. Four of those were only on unpublished profile-pilot files. All six were checked against the public ROR API and are active, Japan, with the exact display name. The three other ids (`05sj3n476`, `00qg0kr10`, `01g9ekh39`) were already on the published panels with the same name.

The printed `raw_affiliation` is unchanged, and the guardrail note is kept with the fix token appended. `ror_country` Japan is kept on the 12 blank-ROR seats, where the freeze would have cleared it.

## Directory totals

Appointments 162,575. Editors 112,718. Journals 2,853. Countries 159.
Institutions 15,438 (6,387 with a ROR id), were 15,432 / 6,381. Appointments without an institution stay 12,066. Shared display names stay 69.

The unmatched `Tokyo` (Japan) row now has 1 appointment (Kojima). Ten Tokyo institution rows are new or grown:
- Tokyo University of Science 14
- Tokyo International University 5
- Tokyo University of Agriculture and Technology 4
- Tokyo Metropolitan University 3
- Tokyo Keizai University 2
- Tokyo University of Marine Science and Technology 2
- Tokyo Gakugei University 1
- Tokyo Women's Medical University 1
- Tokyo University of Foreign Studies 1

Tokyo Institute of Technology is one unmatched row (Japan, 15 appointments: these 11 plus 4 already on the panels). There is no ROR row for Tokyo Institute of Technology; Institute of Science Tokyo `05dqf9946` (8 appointments) stays separate.

## Notes left as is

The existing `ror_notes` / `source_note` text on published panels mentions `Italian Cultural Institute` 34 times. These are history notes from #48 and earlier, such as "raw restored … (was 'Italian Cultural Institute')", and none is in an institution field. This freeze adds none.
