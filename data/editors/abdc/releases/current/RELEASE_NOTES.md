# editors_institution_residual_post35_20261028

Residual place-in-name, country, and variant cleanup of institution strings on the ABDC A*, A, B, and C current boards. Frozen 2026-10-28 23:40 Asia/Hong_Kong. This supersedes `editors_institution_dept_country_20261028` for Directory Institutions. Row counts are unchanged. Empty `editor_name` is 2 on A*, 2 on A, 0 on B, and 11 on C. No D4 or D5 pass is in this freeze.

`editor_name` is the name the directory shows. Display affiliation is `ror_name`, then `canonical_name`, then `raw_affiliation`. Country is `ror_country`. The build does not invent a name, a ROR id, or a URL. A blank affiliation is not an institution. A bare country is not an institution. A string fully enclosed in brackets is not an institution. A street, PO Box, or postal code with no organization name is not an institution. Faculty URL counts are unchanged.

The collector freeze touches 711 editor rows across FT50, ABDC, and the AJG-gap files. This publish pins 539. On these files that is A* 13, A 130, B 147, and C 161. A residual place inside the institution name is stripped. A country mismatch is corrected when the affiliation text names that country. Amazon-like variants merge to `Amazon`. Three address-junk rows are blanked. A rematch uses only a ROR id already on these boards. One hundred seventy-two collector rows stay as published in the previous freeze. A stripped ROR name is not copied onto a different masthead. HKUST (Guangzhou) stays distinct from The Hong Kong University of Science and Technology. Universidade de Santiago de Compostela stays Spain. Oxford colleges stay the United Kingdom. No new ROR id was added.

The directory reads `canonical_name` when `ror_name` is empty. Where this publish blanked `raw_affiliation` and left no `ror_name`, `canonical_name` is clear. `canonical_name` values cleared in the previous institution freezes stay clear on rows this publish did not edit.

## Files

| File | Rows | Empty `editor_name` | `raw_affiliation` | `ror_id` | `faculty_profile_url` | URL, no `ror_id` |
|---|---:|---:|---:|---:|---:|---:|
| `editors_abdc_a_star_current.csv` | 25,178 | 2 | 23,806 (94.6%) | 23,599 | 12,523 (49.7%) | 67 |
| `editors_abdc_a_current.csv` | 45,363 | 2 | 42,776 (94.3%) | 41,935 | 6,237 (13.7%) | 50 |
| `editors_abdc_b_current.csv` | 42,139 | 0 | 39,775 (94.4%) | 38,722 | 3,509 (8.3%) | 21 |
| `editors_abdc_c_current.csv` | 26,720 | 11 | 23,845 (89.2%) | 23,005 | 1,379 (5.2%) | 4 |

`ror_id` was 23,599 / 41,937 / 38,724 / 23,008. The cleared ids were place-qualified ROR names whose display string no longer carried that place. Two `K.U.Leuven` rows gained KU Leuven, `https://ror.org/05f950310`, an id already on these boards.

## Named cases

Simon Washington, Advanced Mobility Analytics Group Pty Ltd, is country Australia. The masthead had `Brisbane, Australia` and the country cell was United States. The place is stripped. No ROR was invented.

Amazon spellings that named the United States (`Amazon, USA`, `Amazon, United States`, `Amazon (United States), Seattle, United States`) are `Amazon`. Country on those seats stays United States. Bare `Amazon` seats that already had Germany stay Germany. No Australia ROR was added.

Manfred Kircher is `KADIB Kircher Advice in Bioeconomy`, country Germany. The Frankfurt postal code is gone.

Three address-junk affiliations are blank. Theodor-W.-Adorno Platz 3 was `60323 Frankfurt am Main, Germany`. Via Garibaldi was `4 (III piano) - 16124 Genova (Italy)`. Marcel Boumans was the date string `(The Netherlands), 2008-2013`, which the previous freeze had replaced with `Thales`.

Bradley Taylor is `GITR Limited`, country United Kingdom. Bram Ramjiawan is `St Boniface General Hospital Research Centre`, country Canada. Pablo Cardona is `IESE`, country Spain. Those three mastheads had been the wrong ROR name (`Thales` or `General Electric`) after `editors_institution_dept_country_20261028`. The organization string already on `canonical_name` is restored, with the place stripped. No new ROR id was attached.

Licia Calvi is KU Leuven, `https://ror.org/05f950310`. The masthead had typed `K.U.Leuven`. That id was already on these boards.

Soumen Ghosh, Decision Sciences, keeps the masthead `Georgia Inst of Technology`. The display stays Czech Academy of Sciences. 吉田　拓真 keeps the Kagoshima masthead. The display stays Nihon University. Andrew Ward, Alexander Lipton, Philip Marcovici, Rahul Garella, Suneet Trivedy, and Louise Trevaskis keep the mastheads and canonical names from the previous publish.

`Aberdeen University` stays on University of Aberdeen, `https://ror.org/016476m91`, United Kingdom. Hengeler Mueller stays as the firm name. Dunarea de Jos and Tribhuvan Sahkari stay without decorative quotes. `[C]Worthy` stays off David McCarthy. HKUST (Guangzhou) stays a separate affiliation from The Hong Kong University of Science and Technology.

The same two medium hits withheld on the FT50 file are withheld on the ABDC copy of that seat.

- Rebecca Ratner, Journal of Marketing Research: `https://ror.org/03a6cpb51` is University of Goma. Affiliation kept as University of Maryland.
- Ioannis Evangelidis, Journal of Marketing Research: `https://ror.org/03qzktr95` is EAE Business School. Affiliation kept as ESADE Business School. Country is Spain.

Tom P. Moliterno on the A* copy of Academy of Management Review uses the same Citadel ROR as the FT50 row, `https://ror.org/01vwr6t80`.

Kai Hockerts stays INSEAD, `https://ror.org/05ynf4333`. Sam Kirshner stays UNSW Sydney, `https://ror.org/03r8z3t63`. `11KBW` stays on two Public Law rows (Aileen McColgan KC, Chris Knight KC), with no ROR id.

One A* row whose name is `___` stays off the person directory. The A panel’s Helena Skyt Nielsen URL still contains an email and is not published.

## Public site

The directory lists no blank name. Where an FT50 appointment is also on an ABDC board, display fields come from `editors_ft50_current_with_ror.csv`. Emails, phone numbers, and photos are not written to the site. Directory appointments stay 158,624. ABDC chips stay A* 25,172 (219 journals), A 45,350 (626), B 42,124 (836), and C 26,708 (732). Countries stay 175. Institutions are 10,835 rows (8,663 with a ROR id), were 10,888 (8,669). 12,164 appointments have no institution, were 12,161. 628 country-only appointments, 3 bracket-only appointments, and 10 street, PO Box, or postal-code appointments stay off that page.
