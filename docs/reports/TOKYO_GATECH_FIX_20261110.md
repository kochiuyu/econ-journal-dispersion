# editors_tokyo_gatech_fix_20261110

Published 2026-11-10 (Asia/Taipei) into the Directory current panels. It supersedes the `editors_inst_punct_split_20261110` current panels (PR #47). Collector freeze path: `editors_tokyo_gatech_fix_20261110`. No site filter. No invented ROR ids.

## Root cause (collector)

An early "Tokyo" ROR backfill matched Tokyo-printed seats to `015e2vx95` "Italian Cultural Institute, Tokyo". A later place-strip step (`residual_post35_strip_place_20261028`) wrote "Italian Cultural Institute" into `raw_affiliation` / `canonical_name` and cleared the ROR. The Directory guardrail (`directory_guardrail_restore_20261101`) reverted the printed text, but left the ROR blank and `canonical_name` as `University of Tokyo` or `Tokyo`. In the Directory that left a separate unmatched `University of Tokyo` Institutions row (20 appointments) next to The University of Tokyo `057zh3y96`. Georgia Tech was a similar rewrite to "Czech Academy of Sciences" that the guardrail had reverted with a blank ROR.

## Directory apply

Only the 28 keyed rows were written: 27 REMATCH_TOKYO to `057zh3y96` and 1 REMATCH_GATECH to `01zkghx44`. By panel: FT50 2 + 2, A* 5, A 5, B 5, C 3, prio43 1, ajg2 2, ajg1 3.

The 27 Tokyo rows break down as follows:
- The 22 blank-ROR `University of Tokyo` rows.
- The 2 matching slim FT50 rows.
- 3 rows whose printed text names the University of Tokyo but whose `canonical_name` was the bare `Tokyo`.

The printed `raw_affiliation` is unchanged. The Directory guardrail note is kept and the fix token is appended. Row counts, the held-out ajg1 / ajg2 navigation rows, the contact scrub, and the FT50 Top 5 alignment are unchanged.

The long table is the #47 long table with 28 parts updated, still 181,443 rows. gzip -9 -n: 7,493,224 bytes; uncompressed md5 `8ce651a307d63c4d914fc96fd95f59a7`.

## Directory totals

Appointments 162,575. Editors 112,718. Journals 2,853. Countries 159.
Institutions 15,432 (6,381 with a ROR id), were 15,434 / 6,381. Appointments without an institution stay 12,066. Shared display names stay 69.
The University of Tokyo `057zh3y96` is one row with 173 appointments (was 150, plus a separate unmatched `University of Tokyo` with 20). Georgia Institute of Technology has 286 appointments, and the unmatched `Georgia Inst of Technology` row is gone.

## Open item: the other 35 Italian Cultural Institute seats

The collector still has 35 publish-panel seats as `Italian Cultural Institute` (A* 1, A 7, B 13, C 14). On the Directory none of them shows that name. All 35 keep the correct printed text and the guardrail note, with `canonical_name` = `Tokyo` and a blank ROR. So the Directory table shows `Tokyo` for them, and Institutions groups them as one unmatched `Tokyo` (Japan) row with 35 appointments.

Their printed institutions include:
- Tokyo Institute of Technology (11)
- Tokyo University of Science (7)
- Tokyo Metropolitan University (3)
- Tokyo University of Agriculture and Technology (3)
- Tokyo International University (3)
- Tokyo Keizai University (2)
- Tokyo University of Marine Science and Technology (2)
- Tokyo Gakugei University (1)
- Tokyo Women's Medical University (1)
- Tokyo University of Foreign Studies (1)
- A bare "Tokyo" (Fuhito Kojima on Theoretical Economics)

A follow-up collector freeze should set `canonical_name` from the printed text and match ROR ids where there is a safe twin.
