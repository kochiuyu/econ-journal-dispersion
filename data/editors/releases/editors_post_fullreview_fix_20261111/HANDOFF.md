# Handoff: editors_post_fullreview_fix_20261111
Status: built, QC ok, UNPUBLISHED. Web build needs the shared-name guard set to 44.
Directory: 11,330/6,396/6,396/167/46 -> 11,213/6,692/6,692/169/44.
Still needs a decision:
1. BIO_OR_MULTI_ORG 24: no targets were given, so all were left as printed.
2. NEAR_DUPLICATE: the 37 not merged (see the skipped log). These include the 12 low-confidence generic names, Max Planck/CNRS collapses, 4 Russian names, two-organisation strings, Linklaters London and FLACSO.
3. Low-confidence MISSING_ROR not applied: SRH Berlin->Heidelberg, Nutraceutical->Better Being, Bank of the West->BMO, University of Africa->Obong.
4. MISSING_ROR rows where the printed country disagrees with the ROR country: Niagara (Canada), Emden/Leer (Poland), West Ukrainian NU (Poland), Univ. of Finance and Economics (China/Mongolia).
5. Creative New Zealand: the raw is "Creative Capital, New York", so the row needs a rename. St. Catharine's is a coin-flip between the UK and Canada.
6. NON_INSTITUTION DROPs not made because the printed raw names an organisation: abdc_b#39063, abdc_c#18771, abdc_c#18673, abdc_b#9281 (KU Leuven is printed).
7. ft50_current_with_ror#4634's profile URL is a CEIBS page, which probably belongs to the other X. Zhao (#4501).
8. Pilot rows keep the inactive UniSA/Adelaide/UPMC RORs because pilots are frozen.
9. 199 HELD_COIN_FLIP rows stay as printed. 276 rows have no country evidence.
