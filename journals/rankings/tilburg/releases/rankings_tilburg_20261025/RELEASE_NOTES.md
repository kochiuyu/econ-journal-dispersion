# Tilburg / TISEM top journal list freeze

- **Freeze id:** `rankings_tilburg_20261025`
- **Source:** TISEM top journal list, Tilburg University
  <https://www.tilburguniversity.edu/research/economics-and-management/publications/topjournals>
- **Retrieved:** 2026-10-25. The public page does not name a dated edition. `edition_year` is `Current`.
- **Ratings:** published tiers `Top-core`, `Top`, and `Very good`. `rating` = `rating_raw`.
- **Good tier:** the page intro mentions good journals. The page itself publishes no good-journal list, so none was added.
- **TiU Econtop database** (<https://rankings.tilburguniversity.edu/journal/list/>) was not joined. It is a separate economics ranking, not these tiers, and it does not add Econ-25 chips.
- **Raw HTML:** not in this repository.

## Edition

| Edition | Rows | Matched | Match % |
|---|---:|---:|---:|
| Current | 179 | 164 | 91.6% |

- **Top-core:** 42 (40 named top-core journals, plus Journal of Economic Literature and Journal of Economic Perspectives from the allocation supplement)
- **Top:** 41
- **Very good:** 96
- **Unmatched rows:** 15
- **Conflicts:** 0

## Mapping

- No ISSNs on the source page. Match is normalized title to FT50, core49, then ABDC A*/A/B/C.
- The same normalized title in more than one very-good group is one row. `field` joins the groups with `; `.
- The supply-chain heading spells European Journal of Operational Research as “Operations”. That duplicate was collapsed into the operations-research title. Field is `Operations Research; Supply Chain Management`.
- `OMEGA-International Journal of Management Science` is the catalog journal `omega` (Omega). That is the only manual title alias.
- Primary `journal_id` prefers FT50, then core49, then ABDC A*/A/B/C.
- No invented journal ids or tiers.

## Source note

`source_file` is `topjournals`. `source_note` is `TISEM top-core`, `TISEM top-core allocation supplement`, `TISEM top`, or `TISEM very good`.
