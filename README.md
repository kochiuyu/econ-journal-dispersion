# econ-journal-dispersion

Public research data for **Geographic Dispersion** work on economics (and related) journals.

**Repository:** https://github.com/kochiuyu/econ-journal-dispersion

**Editor directory:** https://kochiuyu.github.io/econ-journal-dispersion/

## What this repo is

Analysis-friendly **catalogs + release panels** only. Use the files under `data/*/releases/` for papers and coauthor analysis. Scrapes, HTML caches, RePEc dumps, and collector scripts stay in separate workspaces and are **not** versioned here.

## Journal universes

| Catalog | Path | Role |
|---------|------|------|
| **core49** | `journals/catalog_core49.csv` | Geographic Dispersion core economics journals |
| **FT50** | `journals/catalog_ft50.csv` | Financial Times Research rank journals |
| **ABDC** | `journals/catalog_abdc_{a_star,a,b,c}.csv` | 2025 ABDC Journal Quality List by rating |
| **Top 5** | `journals/catalog_top5.csv` | AER, Econometrica, JPE, QJE, and ReStud. Subset tag on the FT50 current release |
| **UTD24** | `journals/catalog_utd24.csv` | UT Dallas Naveen Jindal Top 24. Twenty-three journals tagged from the FT50 freeze; INFORMS Journal on Computing tagged from the ABDC A freeze |
| **ABS/AJG** | `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/` | CABS Academic Journal Guide grades for 2010, 2015, 2018, 2021, and 2024, via the Editor-Collector freeze. Ratings, not editor boards. See `journals/rankings/STATUS.md` |

Prefer joining on stable keys (`journal_slug` / `journal_id`, `year`, `doi`) — see `docs/README.md`.

## Data layout

```
data/
  editors/
    core49/          # STATUS only for now (wayback / multi-year panels still in collector)
    ft50/releases/current/
    abdc/releases/current/
  authors/           # STATUS only — stream still in progress (no 1GB caches here)
  affiliations/
    releases/canonical/   # TOC-first articles / affiliations / issues
```

**Rule:** analyze from `releases/` only. Do not treat collector folders or `STATUS.md` progress notes as frozen paper inputs until a release is pinned.

## Stream status (summary)

| Stream | State in this repo |
|--------|--------------------|
| Editors — FT50 | Current-board panels in `releases/current/` — freeze `editors_current_20261024` |
| Editors — ABDC A*/A/B/C | Current-board panels in `releases/current/` — same freeze (ROR-enriched where available) |
| Editors — core49 | Documented in `STATUS.md`; multi-year panels not yet copied into a pinned release |
| Affiliations (core49 TOC spine) | Canonical articles / affiliations / issues under `releases/canonical/` |
| Authors (core49) | **In progress** — see `data/authors/STATUS.md`; no analysis dump yet |

## Website

Searchable directory of **current journal editors** on the FT50 list and the ABDC A*, A, B, and C lists. Top 5 and UTD24 are extra multi-select filters on those same boards:

**https://kochiuyu.github.io/econ-journal-dispersion/**

core49 is not included (it is an older ABDC A* subset, not a separate universe in this directory). Authors are out of scope.

`scripts/build_site.py` reads the current editor releases and writes `site/data.js`. The page is static HTML, CSS, and JS: a filterable table (name, role, journal, list, affiliation, country, continent), header counts, and a short note on the release. Emails, phone numbers, and photos are not published.

One row is one person in one role on one journal. The same person on two journals is two rows. Where that same appointment is in both the FT50 release and an ABDC rating, the build keeps a single row and tags it with both lists (for example FT50 and ABDC A*). A Top 5 or UTD24 journal keeps those badges on that same row. Wording comes from `editors_ft50_current_with_ror.csv`; a blank affiliation or country is filled from the ABDC row. The same name and role with two different affiliations stays two rows. The full rule is at the top of `scripts/build_site.py`.

Top 5 is American Economic Review, Econometrica, Journal of Political Economy, Quarterly Journal of Economics, and Review of Economic Studies (`journals/catalog_top5.csv`). UTD24 is the official UT Dallas list (`journals/catalog_utd24.csv`): 23 journals already in the FT50 freeze, plus INFORMS Journal on Computing from `editors_abdc_a_current.csv`. Journal of Applied Psychology stays on FT50 only.

The same boards are also grouped by journal and by institution:

**https://kochiuyu.github.io/econ-journal-dispersion/journals.html**

**https://kochiuyu.github.io/econ-journal-dispersion/institutions.html**

`scripts/build_site.py` writes `site/journals-data.js` (one row per journal: list badges, appointments, distinct editors, countries, ABDC field, board link) and `site/institutions-data.js` (one row per ROR id, or per affiliation name when ROR is missing). A journal name opens the directory with `?journal=`. An institution name opens it with `?aff=` set to that affiliation and `?country=` when the row has a country. Those files are generated and are not committed.

Journal grades are a separate page, not extra directory chips:

**https://kochiuyu.github.io/econ-journal-dispersion/rankings.html**

`scripts/build_site.py` also runs `scripts/build_rankings.py`, which reads the Editor-Collector freeze `journals/rankings/abs_ajg/releases/rankings_abs_ajg_20261024/` and writes `site/rankings-data.js`. The Rankings page filters by ranking system, edition year, and rating, and searches by journal title. ABS/AJG is the first system (2010, 2015, 2018, 2021, 2024). Directory chips stay as they are.

### Local build

```bash
python scripts/build_site.py
python -m http.server 8000 -d site
```

Open http://127.0.0.1:8000/ . Styles and scripts use relative URLs, so this is the same tree GitHub Pages serves under `/econ-journal-dispersion/` rather than at the user-site root. Journals are at http://127.0.0.1:8000/journals.html , institutions at http://127.0.0.1:8000/institutions.html , and rankings at http://127.0.0.1:8000/rankings.html . `site/data.js`, `site/journals-data.js`, `site/institutions-data.js`, and `site/rankings-data.js` are generated and are not committed.

### Enable GitHub Pages

`.github/workflows/pages.yml` builds the site on every push to `main` and deploys it with GitHub Actions. Once, in the repository settings:

1. **Settings → Pages**
2. **Build and deployment → Source: GitHub Actions**

If Pages is still set to “Deploy from a branch”, switch it to GitHub Actions. Until that source is selected, the workflow can succeed without the site updating. No custom domain is required. The live URL is https://kochiuyu.github.io/econ-journal-dispersion/ .

## License / citation

Dataset intended as **CC-BY-4.0**. See `CITATION.cff`.

Underlying board lists and TOCs are public journal mastheads / publisher pages; enrichment (ROR, OpenAlex) follows each provider’s terms.
