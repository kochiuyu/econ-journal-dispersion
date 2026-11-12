"""Build editors_backfill_ra_pack2_20261113: live editors_backfill_red_jbes_20261113 + 19 RA pack 2 person-row edits.
18 names-only fills (panel fill + one appended long row each) and S20 Kuersteiner ET 2018 campus ROR (panel + existing long row).
Match-rate rows recomputed from the panel for the 7 journals touched. Every other file is byte-identical to live."""
import csv, io, json, sys
from pathlib import Path
REL = Path('/workspace/econ-journal-editors/releases')
LIVE = REL / 'editors_backfill_red_jbes_20261113'; OUT = REL / 'editors_backfill_ra_pack2_20261113'
API = REL / 'RA_pack2_collector_work_20261113/evidence/ror_api_recheck_freeze'
TAG = 'ra_pack2_20261113'; P = 'editors_backfill_scale_panel#'
WORK = 'releases/RA_pack2_collector_work_20261113 (evidence; DO NOT PUBLISH CVs)'
FILLS = [  # item, key, institution, raw, ror, method_basis, source, evidence
 ('S01', 999, 'Princeton University', 'Princeton University', '00hx57361', 'crosswalk', 'https://spia.princeton.edu/sites/default/files/person/cvfiles/CV073119.pdf', "Princeton CV (07/2019): Theodore A. Wells '29 Professor of Economics, Princeton 2014–present (covers 2018; 2018–19 Booth post is visiting)"),
 ('S02', 1055, 'University of California, Los Angeles', 'University of California, Los Angeles', '046rm7j60', 'crosswalk', 'http://www.econ.ucla.edu/mtv/cv-mtv.pdf', 'UCLA CV (May 2026): Associate Professor of Economics, UCLA 2015–2021; AER associate editor 2017–2023'),
 ('S03', 1089, 'University of California, Berkeley', 'University of California, Berkeley', '01an7q238', 'crosswalk', 'https://sites.google.com/view/pgourinchas/home/vita', 'Vita + full CV pogres_26a: UC Berkeley economics 2003–, on leave only from 04/2022 (IMF); AER co-editor 2019–22'),
 ('S04', 1205, 'University of Minnesota', 'University of Minnesota', '017zqws13', 'crosswalk', 'https://cla.umn.edu/about/directory/profile/loukas', 'UMN CLA profile: Professor, Department of Economics 2020–present (Associate Professor 2016–2020); Minneapolis address = Twin Cities campus'),
 ('S05', 1260, 'Pennsylvania State University', 'Pennsylvania State University', '04p491231', 'crosswalk', 'https://nageebali.com/NageebAliCV.pdf', 'CV: Professor of Economics, Pennsylvania State University 7/19–now; University Park'),
 ('S06', 1630, 'Princeton University', 'Princeton University', '00hx57361', 'crosswalk', 'https://markus.scholar.princeton.edu/sites/g/files/toruqf2651/files/documents/CV_markus.pdf', 'Princeton CV: Edwards S. Sanford Professor of Economics 2008–present'),
 ('S07', 1662, 'University of California, Berkeley', 'University of California, Berkeley', '01an7q238', 'crosswalk', 'https://andres.econ.berkeley.edu/papers/CV-June-2025.pdf', 'Berkeley CV (June 2025): Jordan Professor of Economics, UC Berkeley; previous post Penn State ended 2011'),
 ('S08', 12660, 'Norwegian School of Economics', 'Norwegian School of Economics', '04v53s997', 'crosswalk', 'https://sites.google.com/view/alexander-w-cappelen/more-info/academic-positions', 'Academic Positions page: Professor, Department of Economics, Norwegian School of Economics 2006–present'),
 ('S09', 12694, 'Federal Reserve Bank of New York', 'Federal Reserve Bank of New York', '05hwvzg47', 'crosswalk', 'https://www.newyorkfed.org/medialibrary/media/research/economists/vanderklaauw/vanderklaauw_cv.pdf', 'FRBNY CV (March 2026): Economic Research Advisor, FRBNY January 2022–present; Senior Vice President 2013–2022'),
 ('S10', 12737, 'University of Zurich', 'University of Zurich', '02crff812', 'crosswalk', 'https://yanagizawadrott.com/wp-content/uploads/2026/01/CV_Jan2026.pdf', 'CV (Jan 2026): Professor, Department of Economics, University of Zurich 2016–present; JPE associate editor since 2022'),
 ('S11', 11338, 'University of Chicago (Booth School of Business)', 'University of Chicago (Booth School of Business)', '024mw5h28', 'crosswalk', 'https://faculty.chicagobooth.edu/canice-prendergast/cv', 'Booth CV page: W. Allen Wallis Distinguished Service Professor, Chicago Booth 2017–present'),
 ('S12', 11356, 'Tel Aviv University', 'Tel Aviv University', '04mhzgx49', 'crosswalk', 'https://www.tau.ac.il/~itaysap/CV_itay.pdf', 'TAU CV: Senior Lecturer, Eitan Berglas School of Economics, Tel Aviv University 2019–2022; Associate Professor 2023–'),
 ('S13', 11368, 'University College London', 'University College London', '02jx3x895', 'crosswalk', 'https://www.christiandustmann.com/images/postpics/cvdustmann_9_26.pdf', 'CV: Professor of Economics, University College London since 2004'),
 ('S14', 11452, 'University of Chicago', 'University of Chicago', '024mw5h28', 'crosswalk', 'https://www.law.berkeley.edu/library/resources/cvs/Dharmapala.pdf', 'CV: Julius Kreeger Professor, University of Chicago Law School 2015–2020 (Berkeley Law only from 2023)'),
 ('S15', 11461, 'UNSW Sydney', 'UNSW Business School', '03r8z3t63', 'ror_name', 'http://yinglan.people.ust.hk/2020IOconference/Richard.pdf', 'CV (Oct 2019): Professor of Economics, UNSW Business School 2011–; continuity to 2021 from current UNSW Research profile (research.unsw.edu.au/people/scientia-professor-richard-timothy-holden)'),
 ('S16', 14135, 'Yale University', 'Yale University', '03v76x132', 'crosswalk', 'https://gerardpadro.com/_content/CV_Padro.pdf', 'CV: Professor of Economics and Political Science, Yale University 2018–2023 (LSE ended 2018)'),
 ('S17', 14157, 'Harvard University', 'Harvard University', '03vek6s52', 'crosswalk', 'https://stantcheva.scholars.harvard.edu/sites/g/files/omnuum7746/files/2025-12/CV_SStantcheva_Dec2025.pdf', 'Harvard CV (Dec 2025): Professor of Economics 05/2018–06/2021; Nathaniel Ropes Professor 07/2021–; QJE editor 01/2020–'),
 ('S18', 14206, 'University of Chicago (Booth School of Business)', 'University of Chicago (Booth School of Business)', '024mw5h28', 'crosswalk', 'https://compass-lexecon.files.svdcdn.com/production/files/cvs/Matthew-Notowidigdo-CV-October-2026.pdf', 'CV (Oct 2026): Professor of Economics, Chicago Booth 2020–2022'),
]
S20 = ('S20', 2046, '047s2c258', 'https://econweb.umd.edu/~kuersteiner/VITA2023-Mar-Kuersteiner_web.pdf')
TOUCHED_KEYS = [P + str(f[1]) for f in FILLS] + [P + str(S20[1])]

def api(i):
    d = json.load(open(API / f'{i}.json')); g = d['locations'][0]['geonames_details']
    return dict(status=d['status'], name=next(n['value'] for n in d['names'] if 'ror_display' in n['types']),
                country=g['country_name'], continent=g.get('continent_name', ''), lat=float(g['lat']), lon=float(g['lng']))
def ser(row):
    s = io.StringIO(); csv.writer(s, lineterminator='').writerow(row); return s.getvalue().encode('utf-8')
def parse(line): return next(csv.reader([line.decode('utf-8')]))

def main():
    log = []
    # ---- panel ----
    pb = (LIVE / 'editors_backfill_scale_ror_panel.csv').read_bytes(); PL = pb.split(b'\r\n'); assert PL[-1] == b''
    H = parse(PL[0]); ix = {h: i for i, h in enumerate(H)}
    rows = [parse(l) for l in PL[1:-1]]; bykey = {r[ix['editor_row_key']]: n for n, r in enumerate(rows)}
    def ref(ror):  # existing panel row carrying this ROR -> geo fields (consistency with the backfill)
        for r in rows:
            if r[ix['ror_id']] == 'https://ror.org/' + ror: return r
        raise SystemExit('no existing panel row for ' + ror)
    def strmatch(inst, ror):
        c = [r for r in rows if r[ix['institution']] == inst]
        return len(c), all(r[ix['ror_id']] == 'https://ror.org/' + ror for r in c)
    changes = []; long_new = []
    LH = parse((LIVE / 'editor_affiliations.csv').read_bytes().split(b'\r\n')[0]); lix = {h: i for i, h in enumerate(LH)}
    for item, k, inst, raw, ror, basis, src, ev in FILLS:
        n = bykey[P + str(k)]; r = rows[n]; old = list(r)
        assert r[ix['ror_match_status']] == 'no_affiliation' and not r[ix['raw_affiliation']] and not r[ix['institution']] and not r[ix['ror_id']], item
        a = api(ror); assert a['status'] == 'active', item
        g = ref(ror); assert g[ix['ror_name']] == a['name'] and g[ix['ror_country']] == a['country'], item
        assert abs(float(g[ix['lat']]) - a['lat']) < 1e-4 and abs(float(g[ix['lon']]) - a['lon']) < 1e-4, item
        if basis == 'crosswalk':
            cnt, uni = strmatch(inst, ror); assert cnt > 0 and uni, (item, cnt, uni)
            how = f"ROR from unambiguous existing scale-panel crosswalk for {inst} ({cnt} rows)"; meth = f'{TAG}+panel_crosswalk'
        else:
            assert inst == a['name']; how = f"ROR from exact ror.org display name '{a['name']}' (API-active, {a['country']}); raw '{raw}' as in CV"; meth = f'{TAG}+ror_api_exact_name'
        notes = f"{TAG}: {how}; institution='{inst}'; source={src}; {ev}; API re-checked 2026-11-13 active"
        pf = [x for x in r[ix['parse_flags']].split(';') if x and x != 'no_affiliation_printed'] + ['ra_pack2_filled_20261113']
        upd = dict(raw_affiliation=raw, affiliation_imputed='yes', institution=inst, canonical_name=inst,
                   source_note=r[ix['source_note']] + f" | {TAG}: institution from Collector CV/faculty check (RA pack 2 {item}, in-house); source={src}; evidence={ev}",
                   parse_flags=';'.join(pf), ror_id='https://ror.org/' + ror, ror_name=a['name'], ror_country=a['country'],
                   continent=g[ix['continent']], lat=g[ix['lat']], lon=g[ix['lon']], ror_match_method=meth, ror_match_score='1.0',
                   ror_confidence='high', ror_notes=notes, ror_match_status='matched', affiliation_count='1', ror_id_aff_rank='1', primary_aff_basis='single')
        for f, v in upd.items(): r[ix[f]] = v
        lr = [''] * len(LH)
        for f, v in dict(editor_row_key=P + str(k), panel_file='editors_backfill_scale_ror_panel.csv', row_index=str(k), journal=r[ix['journal']],
                         year=r[ix['year']], editor_name=r[ix['editor_name']], aff_text_source='raw_affiliation', aff_rank='1', raw_aff_part=raw,
                         split_basis='single', ror_id='https://ror.org/' + ror, ror_name=a['name'], ror_country=a['country'], ror_match_kind=meth,
                         ror_match_note=notes, aff_role='sole', role_basis='single', is_panel_ror='1').items(): lr[lix[f]] = v
        long_new.append(lr)
        changes.append(dict(ra_id=item, editor_row_key=P + str(k), journal=r[ix['journal']], year=r[ix['year']], editor_name=r[ix['editor_name']],
            old_raw_affiliation='', old_institution='', old_ror_id='', old_ror_match_status='no_affiliation', new_institution=inst, new_raw_affiliation=raw,
            new_ror_id='https://ror.org/' + ror, new_ror_name=a['name'], new_ror_match_status='matched', evidence_source_link=src, evidence_notes=ev,
            board_urls_kept=r[ix['board_urls']], long_action='insert', ror_action='set_from_crosswalk' if basis == 'crosswalk' else 'set_from_ror_api_exact_name', method=TAG))
    # S20 campus ROR
    item, k, ror, src = S20; n = bykey[P + str(k)]; r = rows[n]
    assert r[ix['raw_affiliation']] == 'University of Maryland' and r[ix['institution']] == 'University of Maryland' and not r[ix['ror_id']]
    a = api(ror); assert a['status'] == 'active' and a['name'] == 'University of Maryland, College Park' and a['country'] == 'United States'
    g = ref(ror)
    notes20 = (f"{TAG}: campus ROR from CV evidence under the university-system rule (assign a campus only when evidenced by text, city, CV or faculty page; never a system ROR). "
               f"Printed 'University of Maryland' kept; Kuersteiner vita March 2023 ({src}): Professor, University of Maryland since 2013, address College Park, MD 20742 "
               f"-> University of Maryland, College Park ({ror}); API re-checked 2026-11-13 active, United States. Prior note: system name only; campus not printed")
    old_status = r[ix['ror_match_status']]
    for f, v in dict(canonical_name=a['name'], ror_id='https://ror.org/' + ror, ror_name=a['name'], ror_country=a['country'], continent=g[ix['continent']],
                     lat=g[ix['lat']], lon=g[ix['lon']], ror_match_method=f'campus_cv_evidence+{TAG}', ror_match_score='1.0', ror_confidence='medium',
                     ror_notes=notes20, ror_match_status='matched', ror_id_aff_rank='1').items(): r[ix[f]] = v
    changes.append(dict(ra_id=item, editor_row_key=P + str(k), journal=r[ix['journal']], year=r[ix['year']], editor_name=r[ix['editor_name']],
        old_raw_affiliation='University of Maryland', old_institution='University of Maryland', old_ror_id='', old_ror_match_status=old_status,
        new_institution='University of Maryland', new_raw_affiliation='University of Maryland', new_ror_id='https://ror.org/' + ror, new_ror_name=a['name'],
        new_ror_match_status='matched', evidence_source_link=src, evidence_notes='Vita March 2023: Professor, University of Maryland since 2013; College Park address',
        board_urls_kept=r[ix['board_urls']], long_action='update_existing_long_row', ror_action='set_campus_ror_from_cv', method=TAG))
    out = [PL[0]] + [ser(x) if x != parse(PL[i + 1]) else PL[i + 1] for i, x in enumerate(rows)] + [b'']
    (OUT / 'editors_backfill_scale_ror_panel.csv').write_bytes(b'\r\n'.join(out))
    # ---- long ----
    lb = (LIVE / 'editor_affiliations.csv').read_bytes(); LL = lb.split(b'\r\n'); assert LL[-1] == b''
    hit = 0
    for i in range(1, len(LL) - 1):
        x = parse(LL[i])
        if x[lix['editor_row_key']] == P + '2046':
            assert x[lix['aff_rank']] == '1' and not x[lix['ror_id']]
            x[lix['ror_id']] = 'https://ror.org/' + ror; x[lix['ror_name']] = a['name']; x[lix['ror_country']] = a['country']
            x[lix['ror_match_kind']] = f'campus_cv_evidence+{TAG}'; x[lix['ror_match_note']] = notes20; x[lix['is_panel_ror']] = '1'
            LL[i] = ser(x); hit += 1
    assert hit == 1
    LL = LL[:-1] + [ser(x) for x in long_new] + [b'']
    (OUT / 'editor_affiliations.csv').write_bytes(b'\r\n'.join(LL))
    # ---- match rates (touched journals only) ----
    mb = (LIVE / 'BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv').read_bytes(); ML = mb.split(b'\r\n'); MH = parse(ML[0]); mix = {h: i for i, h in enumerate(MH)}
    jids = sorted({rows[bykey[k]][ix['journal_id']] for k in TOUCHED_KEYS}); mr = []
    for i in range(1, len(ML) - 1):
        x = parse(ML[i])
        if x[mix['journal_id']] not in jids: continue
        allj = [r for r in rows if r[ix['journal_id']] == x[mix['journal_id']]]; ns = [r for r in allj if r[ix['role_class']] != 'staff']
        wa = [r for r in ns if r[ix['ror_match_status']] in ('matched', 'unmatched')]; m = [r for r in ns if r[ix['ror_match_status']] == 'matched']
        old = dict(zip(MH, x))
        new = dict(rows_non_staff=str(len(ns)), no_affiliation=str(sum(1 for r in ns if r[ix['ror_match_status']] == 'no_affiliation')), with_affiliation=str(len(wa)),
                   matched=str(len(m)), unmatched=str(len(wa) - len(m)), match_rate=f'{len(m)/len(wa):.4f}' if wa else '',
                   high=str(sum(1 for r in m if r[ix['ror_confidence']] == 'high')), medium=str(sum(1 for r in m if r[ix['ror_confidence']] == 'medium')),
                   low=str(sum(1 for r in m if r[ix['ror_confidence']] == 'low')), staff_rows_excluded=str(len(allj) - len(ns)))
        for f, v in new.items(): x[mix[f]] = v
        ML[i] = ser(x); mr.append(dict(journal=old['journal'], **{f'{f}_before': old[f] for f in new}, **{f'{f}_after': new[f] for f in new}))
    (OUT / 'BACKFILL_SCALE_ROR_match_rates_by_journal_20261031.csv').write_bytes(b'\r\n'.join(ML))
    # ---- change logs ----
    ch = list(changes[0].keys())
    with open(OUT / 'RA_pack2_changes_20261113.csv', 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, ch, lineterminator='\r\n'); w.writeheader(); w.writerows(changes)
    with open(OUT / 'RA_pack2_match_rate_changes_20261113.csv', 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, list(mr[0].keys()), lineterminator='\r\n'); w.writeheader(); w.writerows(mr)
    for x in mr: log.append(f"match_rates {x['journal']}: with_aff {x['with_affiliation_before']}->{x['with_affiliation_after']}, matched {x['matched_before']}->{x['matched_after']}, unmatched {x['unmatched_before']}->{x['unmatched_after']}, rate {x['match_rate_before'] or 'n/a'}->{x['match_rate_after']}")
    log.append(f'panel rows {len(rows)}; long rows {len(LL) - 2}; panel keys changed {len(changes)}; long rows appended {len(long_new)}; long rows updated 1')
    (OUT / 'build_ra_pack2_20261113.log').write_text('\n'.join(log) + '\n'); print('\n'.join(log))
if __name__ == '__main__': main()
