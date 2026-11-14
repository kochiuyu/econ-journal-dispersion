"""QC for editors_backfill_red2024_20261114 against live editors_backfill_ra_pack2_20261113 (PR #72)."""
import csv, json, re, hashlib, subprocess
from pathlib import Path
from collections import Counter
REL = Path('/workspace/econ-journal-editors/releases')
LIVE = REL / 'editors_backfill_ra_pack2_20261113'; OUT = REL / 'editors_backfill_red2024_20261114'
PDF = Path('/workspace/econ-journal-editors/abs_ajg/reports/RED_2024_editorial_board.pdf')
API = Path('/tmp/red24api'); RES = REL / 'RA_package_minimal_20261106_reserved_20261113'
P = 'editors_backfill_scale_panel#'; JID = 'S163499366'
URL = 'https://www.sciencedirect.com/science/article/pii/S1094202524000061'; DOI = '10.1016/S1094-2025(24)00006-1'
NEWKEYS = [P + str(k) for k in range(15873, 15917)]
res = []
def ok(c, m): res.append(bool(c)); print(('PASS ' if c else 'FAIL ') + m)
def rows(p): return list(csv.DictReader(open(p, encoding='utf-8', newline='')))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
CHANGED = {'editors_backfill_scale_ror_panel.csv', 'editor_affiliations.csv', 'editors_backfill_scale_inventory.csv', 'editors_backfill_scale_gaps.csv',
           'BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv'}
NEWCSV = {'RED_2024_board_changes_20261114.csv', 'RED_2024_match_rate_changes_20261114.csv', 'red_2024_board_extracted.csv'}
NEW = NEWCSV | {'RED_2024_board_source_20261114.md', 'backfill_red2024_20261114.py', 'backfill_red2024_20261114.log', 'qc_red2024_20261114.py',
                'qc_red2024_20261114.log', '_summary_20261114.json', '_live_manifest_sha256.txt', 'README.md', 'HANDOFF.md', 'HANDOFF_NOTE.md',
                'RELEASE_NOTES.md', 'CHANGES.md', 'QC_REPORT.md', '_build.json'}
DROPPED = {'README.md', 'HANDOFF.md', 'RELEASE_NOTES.md', '_build.json', 'SENDTO_BLURB.txt', '_summary_20261113.json', '_live_manifest_sha256.txt'}
live_files = {f.name for f in LIVE.iterdir()}; out_files = {f.name for f in OUT.iterdir()}
ok(out_files - live_files <= NEW, f'no unexpected new files {sorted(out_files - live_files - NEW)}')
ok(live_files - out_files <= DROPPED, f'every live data file present (only live docs replaced) {sorted(live_files - out_files)}')
ok(not (OUT / PDF.name).exists() and not any(f.suffix == '.pdf' and f.name not in live_files for f in OUT.iterdir()), 'RED 2024 PDF not in release folder; no new PDF')
same = [f for f in sorted(live_files & out_files) if f not in CHANGED | DROPPED]
diff = [f for f in same if sha(LIVE / f) != sha(OUT / f)]
ok(not diff, f'{len(same)} other live files byte-identical (spotcheck, staff rows, matched/unmatched, crosswalk, change CSVs, PDFs) {diff}')
for f in sorted(CHANGED | NEWCSV - {'red_2024_board_extracted.csv'}):
    b = (OUT / f).read_bytes(); ok(b.count(b'\n') == b.count(b'\r\n') and b.endswith(b'\r\n'), f'{f}: CRLF throughout')
b = (OUT / 'red_2024_board_extracted.csv').read_bytes(); ok(b'\r' not in b, 'red_2024_board_extracted.csv: LF, as red_2025_board_extracted.csv')
for f in sorted(CHANGED):
    ok((OUT / f).read_bytes().split(b'\r\n')[0] == (LIVE / f).read_bytes().split(b'\r\n')[0], f'{f}: header unchanged')
# ---- panel ----
LP = rows(LIVE / 'editors_backfill_scale_ror_panel.csv'); NP = rows(OUT / 'editors_backfill_scale_ror_panel.csv')
ok(len(LP) == 15873 and len(NP) == 15917, f'panel rows {len(NP)} = {len(LP)} + 44')
lb = (LIVE / 'editors_backfill_scale_ror_panel.csv').read_bytes(); nb = (OUT / 'editors_backfill_scale_ror_panel.csv').read_bytes()
ok(nb.startswith(lb), 'panel: live file is a byte prefix of the new file (no existing row changed)')
new = NP[15873:]
ok([r['editor_row_key'] for r in new] == NEWKEYS, 'new keys #15873-#15916, contiguous, in board order')
ok(len({r['editor_row_key'] for r in NP}) == len(NP), 'panel keys unique')
ok(all(r['journal_id'] == JID and r['journal'] == 'Review of Economic Dynamics' and r['year'] == r['board_year'] == '2024' for r in new), 'all new rows RED 2024')
ok(not any(r['journal_id'] == JID and r['board_year'] == '2024' for r in LP), 'live had no RED 2024 rows')
ok(all(r['source_url'] == r['board_urls'] == URL and r['board_url_count'] == '1' and DOI in r['source_note'] and r['issue'] == 'Vol 52 (2024-04)'
       and r['source_type'] == 'official_issue' and r['board_status'] == 'issue_front_matter' and not r['archive_url'] for r in new),
   'source_url/board_urls = ScienceDirect article URL, board_url_count 1, DOI in source_note, issue Vol 52 (2024-04), no archive_url')
rc = Counter(r['role'] for r in new)
ok(rc == Counter({'CO-ORDINATING EDITOR': 1, 'EDITORS': 9, 'ASSOCIATE EDITORS': 30, 'EDITORIAL ADVISORY BOARD': 4}), f'roles as printed {dict(rc)}')
ok(Counter(r['role_class'] for r in new) == Counter({'editor': 10, 'board': 30, 'advisory': 4}), 'role_class editor 10 / board 30 / advisory 4 (as RED 2025)')
# conventions vs RED 2025 twin rows
T = [r for r in LP if r['journal_id'] == JID and r['board_year'] == '2025']
PROV = {'year', 'source_url', 'board_urls', 'source_note', 'capture_timestamp', 'collection_date', 'data_source', 'snapshot_date', 'snapshot_source',
        'board_year', 'capture_date', 'parse_flags', 'ror_match_method', 'ror_notes', 'issue', 'editor_row_key'}
ok(len(T) == 44 and all({c for c in a if a[c] != b[c]} <= PROV for a, b in zip(T, new)),
   'every new row equals its RED 2025 twin on all non-provenance fields (names, roles, raw, institution, ROR, geo, flags)')
# independent text check against pdftotext -raw
txt = re.sub(r'\s+', ' ', subprocess.run(['pdftotext', '-raw', str(PDF), '-'], capture_output=True, text=True).stdout)
lay = subprocess.run(['pdftotext', '-layout', str(PDF), '-'], capture_output=True, text=True).stdout
EXP = {'Thomas F. Cooley': 'T.F. Cooley', 'Boyan Jovanovic': 'B. Jovanovic', 'Edward C. Prescott': 'E.C. Prescott', 'Thomas J. Sargent': 'T.J. Sargent'}
ok(all((r['editor_name_raw'].replace("'", '\u2019') if 'La' in r['editor_name_raw'] else r['editor_name_raw']) in lay for r in new), 'every editor_name_raw printed on the PDF (initials as printed; La\u2019O apostrophe normalised as on RED 2021/2025)')
ok(all(EXP.get(r['editor_name'], r['editor_name_raw']) == r['editor_name_raw'] for r in new) and sum(r['editor_name'] != r['editor_name_raw'] for r in new) == 4,
   'editor_name = printed except the 4 advisory expansions (as RED 2021/2025)')
ok(all(r['raw_affiliation'] in txt for r in new), 'every raw_affiliation occurs verbatim (whitespace-joined) in the pdftotext -raw text')
ok(all(r['affiliation_count'] == '1' and r['ror_id_aff_rank'] == '1' and r['primary_aff_basis'] == 'single' and not r['other_affiliations'] and not r['other_ror_ids']
       for r in new), 'one printed affiliation per person; single/primary columns as RED 2025')
tr = (OUT / 'RED_2024_board_source_20261114.md').read_text()
ok(all(r['editor_name_raw'].replace("'", '\u2019') in tr or r['editor_name_raw'] in tr for r in new), 'every printed name in the transcript')
# ---- ROR ----
def api(i):
    d = json.load(open(API / f'{i}.json')); g = d['locations'][0]['geonames_details']
    return d['status'], next(n['value'] for n in d['names'] if 'ror_display' in n['types']), g['country_name']
ids = {r['ror_id'].rsplit('/', 1)[1] for r in new if r['ror_id']}
ok(all(api(i)[0] == 'active' for i in ids), f'{len(ids)} distinct RORs API-active (ROR v2 API re-checked 2026-11-14)')
ok(all((r['ror_name'], r['ror_country']) == api(r['ror_id'][-9:])[1:] and r['canonical_name'] == r['ror_name'] for r in new), 'ror_name/ror_country/canonical = API display name/country')
used = {r['ror_id'] for r in LP if r['ror_id']}
ok(all(r['ror_id'] in used for r in new if r['ror_id']), 'no ROR new to the backfill')
ok(sum(1 for r in new if r['ror_id']) == 44 and all(r['ror_match_status'] == 'matched' for r in new), '44/44 ROR matched, 0 blank')
BAD = ('0031wrj91', '03ydkyb10', '04jzmdh37', '05ynf4333', '00ghzk478')
ok(not any(x in r['ror_id'] for r in new for x in BAD), 'no EUI / UW-system / CEPR-UK / INSEAD ids on new rows')
ok(all(r['ror_id'].endswith('017zqws13') for r in new if r['raw_affiliation'].startswith('University of Minnesota')), 'U Minnesota rows -> Twin Cities campus 017zqws13 (as RED 2021/2025)')
ok(all(r['ror_id'].endswith(i) for r in new for s, i in (('Centre for Research in International Economics', '0241avf06'), ('Einaudi Institute', '04e874t64')) if r['raw_affiliation'].startswith(s)), 'research institutes keep own ROR (CREI, EIEF)')
lat = {}
for r in LP:
    if r['ror_id']: lat.setdefault(r['ror_id'], set()).add((r['lat'], r['lon']))
ok(all((r['lat'], r['lon']) in lat[r['ror_id']] for r in new), 'geo fields equal those on existing rows with the same ROR')
# ---- long ----
LL = rows(LIVE / 'editor_affiliations.csv'); NL = rows(OUT / 'editor_affiliations.csv')
ok(len(LL) == 12120 and len(NL) == 12164, f'long rows {len(NL)} = {len(LL)} + 44')
ok((OUT / 'editor_affiliations.csv').read_bytes().startswith((LIVE / 'editor_affiliations.csv').read_bytes()), 'long: live file is a byte prefix (no existing long row changed)')
app = NL[12120:]; N = {r['editor_row_key']: r for r in NP}
ok([r['editor_row_key'] for r in app] == NEWKEYS, 'long: 44 rows appended, one per new key, same order')
ok(all(r['aff_rank'] == '1' and r['aff_role'] == 'sole' and r['split_basis'] == 'single' and r['is_panel_ror'] == '1' and r['row_index'] == r['editor_row_key'].split('#')[1]
       and r['year'] == '2024' and r['raw_aff_part'] == N[r['editor_row_key']]['raw_affiliation'] and r['editor_name'] == N[r['editor_row_key']]['editor_name']
       and r['ror_id'] == N[r['editor_row_key']]['ror_id'] and r['ror_name'] == N[r['editor_row_key']]['ror_name'] for r in app),
   'appended long rows: rank 1, sole, single, is_panel_ror=1, row_index=key, raw/name/ROR = panel')
TL = {r['editor_row_key']: r for r in LL}
LPROV = {'editor_row_key', 'row_index', 'year', 'ror_match_kind', 'ror_match_note'}
ok(all({c for c in a if a[c] != TL[t['editor_row_key']][c]} <= LPROV for a, t in zip(app, T)), 'each long row equals the RED 2025 twin long row on non-provenance fields')
pk = set(N); ok(all(r['editor_row_key'] in pk for r in NL), 'every long key exists in panel')
lk = Counter(r['editor_row_key'] for r in NL)
ok({r['editor_row_key'] for r in NP if r['raw_affiliation']} <= set(lk), 'every panel row with raw affiliation has a long row')
mis = sorted({r['editor_row_key'] for r in NL if r['aff_rank'] == '1' and r['ror_id'] != N[r['editor_row_key']]['ror_id']})
ok(mis == ['editors_backfill_scale_panel#5078', 'editors_backfill_scale_panel#5126'], f'global rank-1 long ROR vs panel: only the 2 pre-existing live exceptions {mis}')
# ---- inventory / gaps / match rates ----
def rowdiff(f):
    a = rows(LIVE / f); b = rows(OUT / f); return a, b, [(x, y) for x, y in zip(a, b) if x != y]
a, b, d = rowdiff('editors_backfill_scale_inventory.csv')
ok(len(a) == len(b) and len(d) == 1 and d[0][1]['journal_id'] == JID and d[0][1]['board_year'] == '2024', 'inventory: only the RED 2024 row changed')
i = d[0][1]; ok(i['status'] == 'ok_issue_front_matter' and i['rows_parsed'] == '44' and i['rows_with_affiliation'] == '44' and i['source_url'] == URL and not i['archive_url'],
               f'inventory RED 2024: {i["status"]} {i["rows_parsed"]}/{i["rows_with_affiliation"]}, source_url kept')
a, b, d = rowdiff('editors_backfill_scale_gaps.csv')
ok(len(b) == len(a) + 3 and len(d) == 1 and d[0][0]['gap_type'] == 'queued' and d[0][1]['gap_type'] == 'resolved' and d[0][1]['board_year'] == '2024' and d[0][1]['journal_id'] == JID,
   'gaps: RED 2024 queued -> resolved (only changed line); 3 lines appended')
off = [r['text_as_printed'] for r in b[len(a):]]
ok(off == ['Ellen McGrattan, President', 'Erwan Quintin, Treasurer', 'Marina Azzimonti, Secretary'] and all(r['gap_type'] == 'excluded_sed_society_officer_line_excluded' and r['board_year'] == '2024' for r in b[len(a):]),
   f'SED officers excluded and logged as gaps (same gap_type as 2025): {off}')
ok(not any(n in r['editor_name'] for r in new for n in ('McGrattan', 'Quintin')) and not any(r['editor_name'] == 'Marina Azzimonti' for r in new), 'no society officer on panel rows (M. Azzimonti Renzo is the printed AE)')
a, b, d = rowdiff('BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv')
ok(len(a) == len(b) and len(d) == 1 and d[0][1]['journal_id'] == JID, 'match_rates: only the RED row changed')
J = [x for x in NP if x['journal_id'] == JID]; ns = [x for x in J if x['role_class'] != 'staff']
m = sum(1 for x in ns if x['ror_match_status'] == 'matched'); wa = sum(1 for x in ns if x['ror_match_status'] in ('matched', 'unmatched'))
r = d[0][1]; print('   RED match rate', d[0][0]['matched'], '/', d[0][0]['with_affiliation'], d[0][0]['match_rate'], '->', r['matched'], '/', r['with_affiliation'], r['match_rate'])
ok(r['matched'] == str(m) and r['with_affiliation'] == str(wa) and r['rows_non_staff'] == str(len(ns)) and r['staff_rows_excluded'] == str(len(J) - len(ns))
   and r['match_rate'] == f'{m / wa:.4f}', 'RED match_rates row equals a recount of the panel')
print('   RED rows by board_year:', dict(sorted(Counter(x['board_year'] for x in J).items())))
# ---- contacts / proxy ----
EM = re.compile(rb'[\w.+-]+@[\w-]+(\.[\w-]+)*\.[a-z]{2,}', re.I); PHN = re.compile(rb'(\+\d{1,3}[ (]\d|\(?\b\d{3}\)?[ .-]\d{3}[ .-]\d{4}\b)')
hits = [f.name for f in OUT.iterdir() if f.suffix != '.pdf' and EM.search(f.read_bytes())]
ok(not hits, f'no email addresses in non-PDF files {hits}')
ph = [f for f in sorted(NEW) if (OUT / f).exists() and PHN.search((OUT / f).read_bytes())]
ok(not ph, f'no phone numbers in files written by this freeze {ph}')
ok(not any(PHN.search(v.encode()) for r in new for v in r.values()) and not any(PHN.search(v.encode()) for r in app for v in r.values()), 'no phone numbers in new panel/long rows')
px = [f.name for f in OUT.iterdir() if f.suffix == '.csv' and b'easyaccess' in f.read_bytes() and f.name in CHANGED | NEWCSV]
ok(not px and not any('easyaccess' in v for r in new for v in r.values()), 'no CUHK proxy URL in changed/new data files')
# ---- protected folders ----
r = subprocess.run(['sha256sum', '-c', 'SHA256SUMS'], cwd=RES, capture_output=True, text=True); ok(r.returncode == 0, 'reserved pack 2 SHA256SUMS all OK')
ok(sha(REL / 'RA_package_minimal_20261106.zip') == 'd51803344ce8eadcc68efedba01f4c6815e15412360855ca436a81f6c7fccefd', 'shipped RA pack zip checksum unchanged')
cur = {f.name: sha(f) for f in LIVE.iterdir() if f.is_file()}; old = dict(l.split('  ')[::-1] for l in (OUT / '_live_manifest_sha256.txt').read_text().splitlines())
ok(cur == old, 'live freeze folder checksums unchanged vs manifest taken before the build')
print(f'\n{sum(res)} PASS / {len(res) - sum(res)} FAIL')
