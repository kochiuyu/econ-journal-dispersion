# Docs / codebook (placeholder)

Stable join keys used across universes and streams:

| Key | Meaning |
|-----|---------|
| `journal_slug` | Canonical journal id (core49 catalog); FT50/ABDC use `journal_id` in those catalogs — map via overlap columns where present |
| `journal_id` | Top 5 (`journals/catalog_top5.csv`) joins to `catalog_ft50.csv`. UTD24 (`journals/catalog_utd24.csv`) joins to the FT50 catalog, except `informs_journal_computing`, which joins to ABDC A. ABS/AJG rows in freeze `rankings_abs_ajg_20261024` carry the freeze’s primary catalog id (FT50, core49, or ABDC); empty means unmatched. AJG-gap editor rows (`data/editors/abs_ajg_gap/releases/current/`) use the collector slug in `journal_id`; that slug matches an ABDC catalog id only for a handful of titles |
| `year` | Calendar / cover year of the board or article window |
| `doi` | Article DOI when available (affiliations / author panels) |

Full variable dictionary will land here as releases freeze. Until then, see column headers in each `releases/` CSV and the stream `STATUS.md` files.
