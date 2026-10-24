# Affiliations — core49 TOC-first spine

Updated: 2026-10-24 (Asia/Hong_Kong)

## Release in this repo

`releases/canonical/`

| File | Role |
|------|------|
| `articles.csv` | Article spine from publisher TOCs |
| `affiliations.csv` | Author–affiliation rows |
| `issues.csv` | Issue index |
| `supplemental_openalex_panel.csv` | OpenAlex enrichment join |
| `openalex_institution_geo_cache.json` | Small geo cache (~53 KB) |

Print / official TOCs are ground truth for article lists; bibliographic APIs do not invent or drop articles. Join typically by `doi` + `journal_slug` / year.

## Windows (collector)

- **2018–2020**: complete (all 49 journals).
- **2021–2023**: in progress.
- Windowed release packages (`releases/2018-2020`, etc.) remain in the collector and can be mirrored here later.

## Excluded

Spine rebuild caches, publisher HTML, and any geo JSON larger than ~50 MB (none present at initial push).
