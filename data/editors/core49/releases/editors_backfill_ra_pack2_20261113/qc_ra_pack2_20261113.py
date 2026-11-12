"""QC for editors_backfill_ra_pack2_20261113 against live editors_backfill_red_jbes_20261113."""
import csv, json, re, hashlib, subprocess
from pathlib import Path
REL = Path('/workspace/econ-journal-editors/releases')
LIVE = REL / 'editors_backfill_red_jbes_20261113'; OUT = REL / 'editors_backfill_ra_pack2_20261113'
API = REL / 'RA_pack2_collector_work_20261113/evidence/ror_api_recheck_freeze'
RES = REL / 'RA_package_minimal_20261106_reserved_20261113'
P = 'editors_backfill_scale_panel#'
FILL = [999, 1055, 1089, 1205, 1260, 1630, 1662, 12660, 12694, 12737, 11338, 11356, 11368, 11452, 11461, 14135, 14157, 14206]
FK = [P + str(k) for k in FILL]; S20 = P + '2046'; KEYS = set(FK + [S20])
res = []
def ok(c, m): res.append(c); print(('PASS ' if c else 'FAIL ') + m)
def rows(p): return list(csv.DictReader(open(p, encoding='utf-8', newline='')))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
CHANGED = {'editors_backfill_scale_ror_panel.csv', 'editor_affiliations.csv', 'BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv'}
NEW = {'RA_pack2_changes_20261113.csv', 'RA_pack2_match_rate_changes_20261113.csv', 'build_ra_pack2_20261113.py', 'build_ra_pack2_20261113.log',
       'qc_ra_pack2_20261113.py', 'qc_ra_pack2_20261113.log', '_live_manifest_sha256.txt', 'README.md', 'HANDOFF.md', 'RELEASE_NOTES.md', '_build.json', 'SENDTO_BLURB.txt'}
DROPPED = {'README.md', 'HANDOFF.md', 'RELEASE_NOTES.md', '_build.json', 'SENDTO_BLURB.txt'}  # live docs replaced by this freeze's docs
live_files = {f.name for f in LIVE.iterdir()}; out_files = {f.name for f in OUT.iterdir()}
ok(out_files - live_files <= NEW, f'no unexpected new files {sorted(out_files - live_files - NEW)}')
ok(live_files - out_files <= set(), f'every live file present (docs rewritten) {sorted(live_files - out_files)}')
same = [f for f in sorted(live_files) if f not in CHANGED | DROPPED]
diff = [f for f in same if sha(LIVE / f) != sha(OUT / f)]
ok(not diff, f'{len(same)} other live files byte-identical (incl. gaps, inventory, spotcheck, matched/unmatched, crosswalk, PDFs) {diff}')
for f in ['editors_backfill_scale_gaps.csv', 'editors_backfill_scale_inventory.csv', 'editors_backfill_scale_spotcheck.csv', 'BACKFILL_SCALE_ROR_staff_rows_20261031.csv']:
    ok(sha(LIVE / f) == sha(OUT / f), f'{f} byte-identical to live')
for f in CHANGED | {'RA_pack2_changes_20261113.csv', 'RA_pack2_match_rate_changes_20261113.csv'}:
    b = (OUT / f).read_bytes(); ok(b.count(b'\n') == b.count(b'\r\n') and b.endswith(b'\r\n'), f'{f}: CRLF throughout')
for f in CHANGED:
    ok((OUT / f).read_bytes().split(b'\r\n')[0] == (LIVE / f).read_bytes().split(b'\r\n')[0], f'{f}: header unchanged')
# ---- panel ----
LP = rows(LIVE / 'editors_backfill_scale_ror_panel.csv'); NP = rows(OUT / 'editors_backfill_scale_ror_panel.csv')
ok(len(NP) == len(LP) == 15873, f'panel rows {len(NP)} (live {len(LP)})')
ok([r['editor_row_key'] for r in NP] == [r['editor_row_key'] for r in LP], 'panel key order identical to live (no new keys)')
ok(len({r['editor_row_key'] for r in NP}) == len(NP), 'panel keys unique')
dk = {b['editor_row_key'] for a, b in zip(LP, NP) if a != b}
ok(dk == KEYS, f'exactly the 19 intended panel keys differ ({len(dk)})')
lb = (LIVE / 'editors_backfill_scale_ror_panel.csv').read_bytes().split(b'\r\n'); nb = (OUT / 'editors_backfill_scale_ror_panel.csv').read_bytes().split(b'\r\n')
ok(sum(1 for a, b in zip(lb, nb) if a != b) == 19 and len(lb) == len(nb), 'panel: 19 lines differ at byte level, all others byte-identical')
L = {r['editor_row_key']: r for r in LP}; N = {r['editor_row_key']: r for r in NP}
FROZEN = ['editor_name', 'editor_name_raw', 'role', 'source_url', 'board_urls', 'board_url_count', 'board_status', 'snapshot_date', 'board_year',
          'journal', 'journal_id', 'year', 'issue', 'source_type', 'source_file', 'role_class', 'former_flag', 'is_former', 'other_affiliations', 'other_ror_ids']
ok(all(L[k][f] == N[k][f] for k in KEYS for f in FROZEN), 'names, roles, board source_url/board_urls and provenance unchanged on the 19 keys')
FILLF = {'raw_affiliation', 'affiliation_imputed', 'institution', 'canonical_name', 'source_note', 'parse_flags', 'ror_id', 'ror_name', 'ror_country', 'continent',
         'lat', 'lon', 'ror_match_method', 'ror_match_score', 'ror_confidence', 'ror_notes', 'ror_match_status', 'affiliation_count', 'ror_id_aff_rank', 'primary_aff_basis'}
ok(all({f for f in N[k] if N[k][f] != L[k][f]} <= FILLF for k in FK), 'names-only fills: only affiliation/ROR fields changed')
ok(all(L[k]['ror_match_status'] == 'no_affiliation' and not L[k]['raw_affiliation'] for k in FK), 'all 18 were names-only (no_affiliation, empty raw) on live')
ok(all(N[k]['ror_match_status'] == 'matched' and N[k]['raw_affiliation'] and N[k]['affiliation_imputed'] == 'yes' and 'no_affiliation_printed' not in N[k]['parse_flags']
       and 'ra_pack2_filled_20261113' in N[k]['parse_flags'] and N[k]['source_note'].startswith(L[k]['source_note'] + ' | ra_pack2_20261113:') for k in FK),
   'fills: matched, imputed=yes, flag ra_pack2_filled_20261113, live source_note kept as prefix')
ok({f for f in N[S20] if N[S20][f] != L[S20][f]} <= {'canonical_name', 'ror_id', 'ror_name', 'ror_country', 'continent', 'lat', 'lon', 'ror_match_method', 'ror_match_score',
   'ror_confidence', 'ror_notes', 'ror_match_status', 'ror_id_aff_rank'} and N[S20]['raw_affiliation'] == 'University of Maryland' == N[S20]['institution'],
   'S20 #2046: printed raw and institution "University of Maryland" kept; only ROR fields changed')
ok(N[S20]['ror_id'] == 'https://ror.org/047s2c258' and 'College Park' in N[S20]['ror_notes'] and 'since 2013' in N[S20]['ror_notes'], 'S20 ROR 047s2c258 with College Park CV evidence in ror_notes')
EXP = {999: '00hx57361', 1055: '046rm7j60', 1089: '01an7q238', 1205: '017zqws13', 1260: '04p491231', 1630: '00hx57361', 1662: '01an7q238', 12660: '04v53s997',
       12694: '05hwvzg47', 12737: '02crff812', 11338: '024mw5h28', 11356: '04mhzgx49', 11368: '02jx3x895', 11452: '024mw5h28', 11461: '03r8z3t63', 14135: '03v76x132',
       14157: '03vek6s52', 14206: '024mw5h28'}
ok(all(N[P + str(k)]['ror_id'] == 'https://ror.org/' + v for k, v in EXP.items()), 'each fill carries the reviewed ROR id')
ok(N[P + '11461']['raw_affiliation'] == 'UNSW Business School' and N[P + '11461']['institution'] == 'UNSW Sydney', 'S15 raw UNSW Business School / institution UNSW Sydney')
for k in [3864, 5947, 11665, 14899, 6483, 433, 14257, 15446]:
    ok(L[P + str(k)] == N[P + str(k)], f'#{k} unchanged (do-not-change / non-substitute)')
ok(not N[P + '3864']['ror_id'] and not N[P + '5947']['ror_id'], 'S19 CEPR Montreal and S21 EUI stay ROR-blank')
ok(not any(x in N[k]['ror_id'] for k in KEYS for x in ('0031wrj91', '03ydkyb10', '04jzmdh37')), 'no EUI / UW-system / CEPR-UK id on changed rows')
# ---- ROR API ----
def api(i):
    d = json.load(open(API / f'{i}.json')); g = d['locations'][0]['geonames_details']
    return d['status'], next(n['value'] for n in d['names'] if 'ror_display' in n['types']), g['country_name']
ids = {N[k]['ror_id'].rsplit('/', 1)[1] for k in KEYS}
ok(all(api(i)[0] == 'active' for i in ids), f'{len(ids)} distinct RORs API-active (re-checked 2026-11-13)')
ok(all((N[k]['ror_name'], N[k]['ror_country']) == api(N[k]['ror_id'][-9:])[1:] for k in KEYS), 'ror_name/ror_country = API display name/country')
used = {r['ror_id'] for r in LP if r['ror_id']}
ok(all(N[k]['ror_id'] in used for k in KEYS), 'no ROR new to the backfill (all ids already used on live rows)')
ok(all(N[k]['lat'] == next(r['lat'] for r in LP if r['ror_id'] == N[k]['ror_id']) for k in KEYS), 'geo fields copied from existing rows with the same ROR')
# ---- long ----
LL = rows(LIVE / 'editor_affiliations.csv'); NL = rows(OUT / 'editor_affiliations.csv')
ok(len(NL) == len(LL) + 18 == 12120, f'long rows {len(NL)} = {len(LL)} + 18')
llb = (LIVE / 'editor_affiliations.csv').read_bytes().split(b'\r\n'); nlb = (OUT / 'editor_affiliations.csv').read_bytes().split(b'\r\n')
dl = [i for i, (a, b) in enumerate(zip(llb[:-1], nlb)) if a != b]
ok(len(dl) == 1 and NL[dl[0] - 1]['editor_row_key'] == S20, f'long: live rows byte-identical except the one #2046 row ({dl})')
app = NL[len(LL):]
ok([r['editor_row_key'] for r in app] == FK, 'long: 18 rows appended, one per names-only fill, in item order')
ok(all(r['aff_rank'] == '1' and r['aff_role'] == 'sole' and r['split_basis'] == 'single' and r['is_panel_ror'] == '1' and r['row_index'] == r['editor_row_key'].split('#')[1]
       and r['raw_aff_part'] == N[r['editor_row_key']]['raw_affiliation'] for r in app), 'appended long rows follow the RA-fix pattern (rank 1, sole, single, is_panel_ror=1, row_index=key)')
ok(not any(r['editor_row_key'] in set(FK) for r in LL), 'none of the 18 had a long row on live')
pk = {r['editor_row_key'] for r in NP}; ok(all(r['editor_row_key'] in pk for r in NL), 'every long key exists in panel')
lk = {}
for r in NL: lk.setdefault(r['editor_row_key'], []).append(r)
ok(all(len(lk.get(k, [])) == 1 for k in KEYS), 'each of the 19 keys has exactly one long row')
ok(all(v[0]['ror_id'] == N[k]['ror_id'] and v[0]['ror_name'] == N[k]['ror_name'] and v[0]['ror_match_note'] == N[k]['ror_notes'] for k in KEYS for v in [lk[k]]),
   'panel/long agree on ROR id, name and note for all 19 keys')
mis = [k for k, v in lk.items() for r in v if r['aff_rank'] == '1' and r['ror_id'] != N[k]['ror_id']]
mis_live = [r['editor_row_key'] for r in LL if r['aff_rank'] == '1' and r['ror_id'] != L[r['editor_row_key']]['ror_id']]
ok(mis == mis_live and not set(mis) & KEYS, f'global rank-1 long ROR vs panel ROR: same {len(mis)} pre-existing live exceptions only ({sorted(set(mis))}; is_panel_ror=0), none on changed keys')
withaff = {r['editor_row_key'] for r in NP if r['raw_affiliation']}; ok(withaff <= set(lk), 'every panel row with raw affiliation has a long row')
# ---- match rates ----
LM = rows(LIVE / 'BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv'); NM = rows(OUT / 'BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv')
TJ = {'AER', 'AER: Insights', 'Journal of Political Economy', 'Journal of Labor Economics', 'Journal of Law and Economics', 'Quarterly Journal of Economics', 'Econometric Theory'}
ok(len(LM) == len(NM) and {b['journal'] for a, b in zip(LM, NM) if a != b} == TJ, 'match_rates: only the 7 touched journals changed')
good = True
for r in NM:
    if r['journal'] not in TJ: continue
    J = [x for x in NP if x['journal_id'] == r['journal_id']]; ns = [x for x in J if x['role_class'] != 'staff']
    m = sum(1 for x in ns if x['ror_match_status'] == 'matched'); wa = sum(1 for x in ns if x['ror_match_status'] in ('matched', 'unmatched'))
    good &= r['matched'] == str(m) and r['with_affiliation'] == str(wa) and r['rows_non_staff'] == str(len(ns)) and r['staff_rows_excluded'] == str(len(J) - len(ns))
ok(good, 'touched match_rates rows equal a recount of the panel')
# ---- inventory / gaps for the three whole-board gaps ----
inv = rows(OUT / 'editors_backfill_scale_inventory.csv')
st = {(r['journal'], r['board_year']): r['status'] for r in inv}
print('   inventory:', {k: v for k, v in st.items() if (k[0].startswith('Journal of Risk') and k[1] == '2023') or (k[0] == 'Review of Economic Dynamics' and k[1] == '2024') or (k[0].startswith('Journal of Business') and k[1] == '2025')})
ok(sum(1 for r in NP if r['journal'] == 'Journal of Risk and Uncertainty' and r['board_year'] == '2023') == 0 and sum(1 for r in NP if r['journal'] == 'Review of Economic Dynamics' and r['board_year'] == '2024') == 0
   and sum(1 for r in NP if r['journal_id'] == 'S18095783' and r['board_year'] == '2025') == 0, 'no JRU 2023 / RED 2024 / JBES 2025 board rows added')
# ---- contacts scan (non-PDF) ----
EM = re.compile(rb'[\w.+-]+@[\w-]+(\.[\w-]+)*\.[a-z]{2,}', re.I); PH = re.compile(rb'(\+\d{1,3}[ (]\d|\(?\b\d{3}\)?[ .-]\d{3}[ .-]\d{4}\b)')
hits = [f.name for f in OUT.iterdir() if f.suffix != '.pdf' and EM.search(f.read_bytes())]
ok(not hits, f'no email addresses in non-PDF files {hits}')
newtxt = [OUT / f for f in NEW if (OUT / f).exists()]
ph = [f.name for f in newtxt if PH.search(f.read_bytes())]
ok(not ph, f'no phone numbers in files written by this freeze {ph}')
ok(not any(PH.search(N[k][f].encode()) for k in KEYS for f in N[k]), 'no phone numbers in changed panel rows')
# ---- checksums of protected folders ----
r = subprocess.run(['sha256sum', '-c', 'SHA256SUMS'], cwd=RES, capture_output=True, text=True); ok(r.returncode == 0, 'reserved pack 2 SHA256SUMS all OK (original/ untouched)')
ok(sha(REL / 'RA_package_minimal_20261106.zip') == 'd51803344ce8eadcc68efedba01f4c6815e15412360855ca436a81f6c7fccefd', 'shipped RA pack zip checksum unchanged')
man = OUT / '_live_manifest_sha256.txt'
if man.exists():
    cur = {f.name: sha(f) for f in LIVE.iterdir()}; old = dict(l.split('  ')[::-1] for l in man.read_text().splitlines())
    ok(cur == old, 'live freeze folder checksums unchanged vs manifest taken before the build')
print(f'\n{sum(res)} PASS / {len(res) - sum(res)} FAIL')
