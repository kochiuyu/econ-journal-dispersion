# editors_nonlatin_inst_20261110

Published 2026-11-10 (Asia/Taipei) into the Directory current panels. Base: the published Directory copy of `editors_ror_consistency3b_20261101` (PR #41). Collector freeze path: `editors_nonlatin_inst_20261110`. No site filter in `scripts/build_site.py`. No invented ROR ids. `11KBW`, UNSW Sydney, and INSEAD stay.

## Collector actions

| Action | Count |
|---|---:|
| DROP bio/CV blurbs | 19 |
| REMATCH to an existing Latin ROR twin (printed non-Latin names kept) | 60 |
| GAP, no twin, ROR left blank | 8 |
| Stale flag not on the panel | 1 |
| Appointments touched | 87 |

The 60 rematches use 19 ROR ids already on the consistency3b panels (HSE, MSU, CEMI, Academia Sinica Institute of Economics, NTU, and others listed in the freeze RELEASE_NOTES). After the build, nine unmatched Institutions still start with a non-Latin character: the eight GAP names (six Russian institutes or groups, plus ノルウェー王立海洋学研究所 and 大阪医科薬科大学 医学研究支援センター) and 鹿児島大学 理工学域理学系理工学研究科 (the stale flag, already not on the patched row). Those nine stay; no ROR id was invented for them.

Boards: Journal of the New Economic Association, Applied Econometrics, Academia Economic Papers, Journal of the Japan Statistical Society.

## Directory apply

The collector pack's other panels are byte copies of collector consistency3b, not of the published Directory copy, so they were not overlaid. Only the 79 ABDC C appointments that actually change a panel field (60 rematch + 19 drop) were written onto `data/editors/abdc/releases/current/editors_abdc_c_current.csv`. Those 79 keys did not overlap the Directory guardrail or contact-scrub rows. The 8 GAP rows and the stale flag were not panel edits. AJG1 navigation rows stay out. Prior contact scrub stays.

The published long table (181,443 rows) is the consistency3b Directory long table with the same 79 parts updated. gzip -9 -n: 7,461,347 bytes; uncompressed 63,236,288 bytes; md5 `e829cd1ccd0187d7800fb0770e362ae0`.

ABDC C: 27,719 rows, `ror_id` 21,297 (was 21,237), `raw_affiliation` 24,887 (was 24,906).

## Directory totals

Appointments 162,575. Editors 112,718. Journals 2,853.
Institutions 16,234 (6,381 with a ROR id), were 16,283 / 6,381.
Countries stay 159. Appointments without an institution: 11,991 (were 11,972). Shared display names stay 125.
