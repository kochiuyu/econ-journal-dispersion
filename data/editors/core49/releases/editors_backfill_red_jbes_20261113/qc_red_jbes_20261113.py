import csv, json, re, io
from pathlib import Path
OUT=Path('releases/editors_backfill_red_jbes_20261113'); MID=Path('releases/editors_backfill_red_2025_20261113')
LIVE=Path('/tmp/red25_live/data/editors/core49/releases/editors_backfill_red_gap_20261112')
ok=lambda c,m: print(('PASS ' if c else 'FAIL ')+m)
def rows(p): return list(csv.DictReader(open(p,encoding='utf-8',newline='')))
def lines(p): return p.read_bytes().split(b'\n')
# appended files: prefix byte-identity
for f,base_n in [('editors_backfill_scale_ror_panel.csv',15708),('editor_affiliations.csv',11940),('editors_backfill_scale_gaps.csv',None),('BACKFILL_SCALE_ROR_staff_rows_20261031.csv',None)]:
    m=MID/f; o=OUT/f
    ok(o.read_bytes().startswith(m.read_bytes()), f'{f}: intermediate bytes are an exact prefix (base + RED 2025 untouched)')
    ok(lines(o)[0]==lines(m)[0], f'{f}: header unchanged'); ok(o.read_bytes().count(b'\n')==o.read_bytes().count(b'\r\n'), f'{f}: CRLF throughout')
P=rows(OUT/'editors_backfill_scale_ror_panel.csv'); L=rows(OUT/'editor_affiliations.csv')
ok(len(P)==15708+165, f'panel {len(P)} = 15,708 + 165'); ok(len(L)==11940+162, f'long {len(L)} = 11,940 + 162')
# live base prefix
for f,n in [('editors_backfill_scale_ror_panel.csv',15664),('editor_affiliations.csv',11896)]:
    lp=rows(LIVE/f); ok(len(lp)==n and P[:n]==lp if f.startswith('editors') else L[:n]==lp, f'{f}: live base rows identical ({n})')
# RED 2025 identical to intermediate
mp=rows(MID/'editors_backfill_scale_ror_panel.csv'); ok(P[15664:15708]==mp[15664:15708] and all(r['journal']=='Review of Economic Dynamics' and r['board_year']=='2025' for r in mp[15664:15708]),'RED 2025 panel rows #15664-#15707 identical to intermediate')
ml=rows(MID/'editor_affiliations.csv'); ok(L[:11940]==ml,'long rows incl. RED 2025 identical to intermediate')
keys=[r['editor_row_key'] for r in P]; ok(len(set(keys))==len(keys),'panel keys unique')
new=P[15708:]; ok([int(k['editor_row_key'].split('#')[1]) for k in new]==list(range(15708,15873)),'new keys #15708-#15872 contiguous')
pk={r['editor_row_key']:r for r in P}; ok(all(l['editor_row_key'] in pk for l in L),'every long key exists in panel')
lk={}; [lk.setdefault(l['editor_row_key'],[]).append(l) for l in L[11940:]]
ok(all((r['editor_row_key'] in lk)==bool(r['raw_affiliation']) for r in new),'panel-long sync: long rows exactly for affiliated new rows')
ok(all(l['ror_id']==pk[k]['ror_id'] for k,v in lk.items() for l in v if l['aff_rank']=='1'),'long rank-1 ROR == panel ROR')
ok(sorted(r['editor_name'] for r in new if not r['raw_affiliation'])==sorted(['Jamie Hutchens','Margaret E. Martin','Arnold Zellner']*2),'panel-only rows = Hutchens/Martin/Zellner x2')
# ROR checks
api=lambda i: json.load(open(f'/tmp/jbesapi/{i}.json'))
ids=set()
for r in new:
    for x in [r['ror_id']]+r['other_ror_ids'].split('|'):
        if x: ids.add(x.rsplit('/',1)[1])
for l in L[11940:]:
    if l['ror_id']: ids.add(l['ror_id'].rsplit('/',1)[1])
bad=[i for i in ids if api(i)['status']!='active']; ok(not bad,f'{len(ids)} distinct RORs on new rows all API-active {bad}')
disp=lambda i: next(n['value'] for n in api(i)['names'] if 'ror_display' in n['types'])
ok(all(disp(r['ror_id'][-9:])==r['ror_name'] and api(r['ror_id'][-9:])['locations'][0]['geonames_details']['country_name']==r['ror_country'] for r in new if r['ror_id']),'ror_name/country = API display/country')
used=set(x['ror_id'] for x in P[:15708] if x['ror_id'])
fresh={r['ror_id'] for r in new if r['ror_id']}-used; print('   RORs new to the backfill:',fresh)
ok(not any('0031wrj91' in r['ror_id'] or '03ydkyb10' in r['ror_id'] for r in new),'no EUI 0031wrj91 / no UW system 03ydkyb10')
# email/phone scan on all non-PDF files
E=re.compile(rb'[\w.+-]+@[\w-]+\.[a-z]{2,}',re.I); hits=[f.name for f in OUT.iterdir() if f.suffix!='.pdf' and E.search(f.read_bytes())]
ok(not hits,f'no email addresses in any non-PDF file {hits}')
ok(not any(b'jbes.asa' in f.read_bytes() for f in OUT.iterdir() if f.suffix not in {'.pdf','.py','.log'}), 'jbes.asa contact not present in data files')
# whole-file comparisons
changed={'editors_backfill_scale_ror_panel.csv','editor_affiliations.csv','editors_backfill_scale_gaps.csv','BACKFILL_SCALE_ROR_staff_rows_20261031.csv','editors_backfill_scale_inventory.csv','BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv'}
for f in sorted(MID.glob('*.csv')):
    if f.name not in changed: ok((OUT/f.name).read_bytes()==f.read_bytes(), f'{f.name} byte-identical to intermediate')
ok((OUT/'editors_backfill_scale_spotcheck.csv').read_bytes()==(LIVE/'editors_backfill_scale_spotcheck.csv').read_bytes(),'spotcheck = live scrubbed copy')
def diffrows(f,keyf):
    a=rows(MID/f); b=rows(OUT/f); return [(keyf(x),{k:(x[k],y[k]) for k in x if x[k]!=y[k]}) for x,y in zip(a,b) if x!=y], len(a)==len(b)
d,same=diffrows('editors_backfill_scale_inventory.csv',lambda r:(r['journal'][:10],r['board_year'])); ok(same and [k for k,_ in d]==[('Journal of',  '2019'),('Journal of','2020')],f'inventory: only JBES 2019/2020 changed {[k for k,_ in d]}')
for k,v in d: print('  ',k,{x:y[1] for x,y in v.items() if x not in('note',)})
d,same=diffrows('BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv',lambda r:r['journal']); ok(same and [k for k,_ in d]==[ 'Journal of Business and Economic Statistics'],'match_rates: only JBES row changed'); print('  ',d)
inv=rows(OUT/'editors_backfill_scale_inventory.csv')
for y in ('2019','2020'):
    i=[r for r in inv if r['journal_id']=='S18095783' and r['board_year']==y][0]; n=[r for r in new if r['board_year']==y]
    ok(i['rows_parsed']==str(len(n)) and i['rows_with_affiliation']==str(sum(1 for r in n if r['raw_affiliation'])),f'inventory {y} counts {i["rows_parsed"]}/{i["rows_with_affiliation"]}')
G=rows(OUT/'editors_backfill_scale_gaps.csv'); g=[r for r in G if r['journal_id']=='S18095783' and r['board_year'] in('2019','2020')]
from collections import Counter; print('   JBES 2019/2020 gaps:',Counter((r['board_year'],r['gap_type']) for r in g))
print('   2025 JBES inventory:',[ (r['status'],r['rows_parsed']) for r in inv if r['journal_id']=='S18095783' and r['board_year']=='2025'])
