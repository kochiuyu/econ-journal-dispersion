/* Journal rankings.
   Project Pages base: /econ-journal-dispersion/
   Styles, this file, and rankings-data.js are loaded with relative URLs.
   Do not fetch them from the site root; that host path is the user Pages root,
   not this project site. */
(function () {
  "use strict";

  var PAGES_BASE = "/econ-journal-dispersion/";
  var DATA = window.RANKINGS_DATA;
  var numberFormat = new Intl.NumberFormat("en-US");
  var collator = new Intl.Collator("en", { sensitivity: "base", numeric: true });
  var RATING_RANK = { "4*": 5, "4": 4, "3": 3, "2": 2, "1": 1 };

  var countEl = document.getElementById("count");
  var rowsEl = document.getElementById("rows");
  var pagerEl = document.getElementById("pager");

  if (!DATA || !DATA.rows) {
    countEl.textContent = "Rankings data is not built yet. From the repository root, run python scripts/build_site.py.";
    return;
  }

  if (DATA.base && DATA.base !== PAGES_BASE) {
    console.warn("rankings-data.js base path does not match this page", DATA.base, PAGES_BASE);
  }

  var rows = DATA.rows;
  var labels = DATA.subjectLabels || {};
  var total = rows.length;
  var hay = new Array(total);

  var qEl = document.getElementById("q");
  var systemEl = document.getElementById("system");
  var yearEl = document.getElementById("year");
  var ratingEl = document.getElementById("rating");
  var pageSizeEl = document.getElementById("pagesize");
  var form = document.getElementById("filters");
  var clearBtn = document.getElementById("clear");
  var nJournals = document.getElementById("n-journals");
  var nTop = document.getElementById("n-top");
  var nMapped = document.getElementById("n-mapped");
  var nEditions = document.getElementById("n-editions");
  var lTop = document.getElementById("l-top");
  var sTop = document.getElementById("s-top");
  var sJournals = document.getElementById("s-journals");

  var state = readUrl();
  var debounce = 0;

  function formatNumber(value) {
    return numberFormat.format(value);
  }

  function subjectLabel(code) {
    return labels[code] || code || "";
  }

  function systemLabel(id) {
    var systems = DATA.systems || [];
    for (var i = 0; i < systems.length; i++) {
      if (systems[i].id === id) return systems[i].label;
    }
    return id;
  }

  function ratingsFor(system, year) {
    var all = (DATA.ratings && DATA.ratings[system]) || ["4*", "4", "3", "2", "1"];
    if (String(year) === "2010") {
      return all.filter(function (grade) { return grade !== "4*"; });
    }
    return all.slice();
  }

  function defaultSystem() {
    return (DATA.systems && DATA.systems[0] && DATA.systems[0].id) || "abs_ajg";
  }

  function defaultYear(system) {
    var years = (DATA.editions && DATA.editions[system]) || [];
    if (!years.length) return "";
    return String(Math.max.apply(null, years));
  }

  function readUrl() {
    var params = new URLSearchParams(window.location.search);
    var size = Number(params.get("n"));
    var page = Number(params.get("page"));
    var system = params.get("system") || defaultSystem();
    var year = params.get("year") || defaultYear(system);
    var sort = params.get("sort") || "name";
    var dir = params.get("dir") === "desc" ? "desc" : "asc";
    if (["name", "rating", "subject", "year", "id"].indexOf(sort) === -1) sort = "name";
    return {
      q: params.get("q") || "",
      system: system,
      year: year,
      rating: params.get("rating") || "",
      sort: sort,
      dir: dir,
      page: page > 0 ? page : 1,
      pageSize: size === 100 || size === 200 ? size : 50
    };
  }

  function writeUrl() {
    var params = new URLSearchParams();
    if (state.q) params.set("q", state.q);
    if (state.system) params.set("system", state.system);
    if (state.year) params.set("year", state.year);
    if (state.rating) params.set("rating", state.rating);
    if (state.sort !== "name") params.set("sort", state.sort);
    if (state.dir !== "asc") params.set("dir", state.dir);
    if (state.page > 1) params.set("page", String(state.page));
    if (state.pageSize !== 50) params.set("n", String(state.pageSize));
    var query = params.toString();
    var next = window.location.pathname + (query ? "?" + query : "") + window.location.hash;
    var current = window.location.pathname + window.location.search + window.location.hash;
    if (next !== current) history.replaceState(null, "", next);
  }

  function fillHay() {
    for (var i = 0; i < total; i++) {
      var row = rows[i];
      var code = row[5] || "";
      hay[i] = [
        row[3] || "",
        row[2] || "",
        code,
        subjectLabel(code),
        row[6] || "",
        row[7] || ""
      ].join(" ").toLowerCase();
    }
  }

  function addOption(select, value, label) {
    var option = document.createElement("option");
    option.value = value;
    option.textContent = label;
    select.appendChild(option);
  }

  function fillSystems() {
    systemEl.replaceChildren();
    (DATA.systems || []).forEach(function (system) {
      addOption(systemEl, system.id, system.label);
    });
  }

  function fillYears() {
    var years = ((DATA.editions && DATA.editions[state.system]) || []).slice();
    years.sort(function (a, b) { return b - a; });
    var current = state.year;
    yearEl.replaceChildren();
    years.forEach(function (year) {
      addOption(yearEl, String(year), String(year));
    });
    if (years.map(String).indexOf(current) === -1) {
      state.year = years.length ? String(years[0]) : "";
    }
  }

  function fillRatings() {
    var grades = ratingsFor(state.system, state.year);
    var current = state.rating;
    ratingEl.replaceChildren();
    addOption(ratingEl, "", "All ratings");
    grades.forEach(function (grade) {
      addOption(ratingEl, grade, grade);
    });
    if (current && grades.indexOf(current) === -1) state.rating = "";
  }

  function syncControls() {
    qEl.value = state.q;
    systemEl.value = state.system;
    yearEl.value = state.year;
    ratingEl.value = state.rating;
    pageSizeEl.value = String(state.pageSize);
    document.querySelectorAll("th button").forEach(function (button) {
      if (button.dataset.sort === state.sort) {
        button.setAttribute("aria-sort", state.dir === "asc" ? "ascending" : "descending");
      } else {
        button.removeAttribute("aria-sort");
      }
    });
  }

  function editionRows() {
    var year = Number(state.year);
    var matched = [];
    for (var i = 0; i < total; i++) {
      var row = rows[i];
      if (row[0] !== state.system) continue;
      if (row[1] !== year) continue;
      matched.push(i);
    }
    return matched;
  }

  function applyFilters(indexes) {
    var query = state.q.trim().toLowerCase();
    var rating = state.rating;
    var matched = [];
    indexes.forEach(function (index) {
      var row = rows[index];
      if (rating && row[4] !== rating) return;
      if (query && hay[index].indexOf(query) === -1) return;
      matched.push(index);
    });
    var dir = state.dir === "desc" ? -1 : 1;
    matched.sort(function (a, b) {
      var ra = rows[a];
      var rb = rows[b];
      var cmp = 0;
      if (state.sort === "rating") cmp = (RATING_RANK[ra[4]] || 0) - (RATING_RANK[rb[4]] || 0);
      else if (state.sort === "subject") cmp = collator.compare(subjectLabel(ra[5]), subjectLabel(rb[5]));
      else if (state.sort === "year") cmp = ra[1] - rb[1];
      else if (state.sort === "id") cmp = collator.compare(ra[2] || "", rb[2] || "");
      else cmp = collator.compare(ra[3] || "", rb[3] || "");
      if (cmp === 0) cmp = collator.compare(ra[3] || "", rb[3] || "");
      return cmp * dir;
    });
    return matched;
  }

  function cell(text, className) {
    var td = document.createElement("td");
    if (className) td.className = className;
    td.textContent = text || "";
    return td;
  }

  function renderStats(indexes) {
    var topGrade = String(state.year) === "2010" ? "4" : "4*";
    var topCount = 0;
    var mapped = 0;
    indexes.forEach(function (index) {
      var row = rows[index];
      if (row[4] === topGrade) topCount += 1;
      if (row[2]) mapped += 1;
    });
    nJournals.textContent = formatNumber(indexes.length);
    sJournals.textContent = systemLabel(state.system) + " " + state.year;
    nTop.textContent = formatNumber(topCount);
    lTop.textContent = topGrade;
    sTop.textContent = topGrade === "4*" ? "Journals of Distinction" : "Highest grade that year";
    nMapped.textContent = formatNumber(mapped);
    var sMapped = document.getElementById("s-mapped");
    if (sMapped) {
      var rate = indexes.length ? (100 * mapped / indexes.length) : 0;
      sMapped.textContent = rate.toFixed(1) + "% of this edition";
    }
    var years = (DATA.editions && DATA.editions[state.system]) || [];
    nEditions.textContent = formatNumber(years.length);
  }

  function renderTable(matched) {
    var fragment = document.createDocumentFragment();
    var start = (state.page - 1) * state.pageSize;
    var slice = matched.slice(start, start + state.pageSize);
    if (!slice.length) {
      var tr = document.createElement("tr");
      var td = document.createElement("td");
      td.colSpan = 5;
      td.className = "empty";
      td.textContent = "No journals match these filters.";
      tr.appendChild(td);
      fragment.appendChild(tr);
    }
    slice.forEach(function (index) {
      var row = rows[index];
      var tr = document.createElement("tr");
      var name = cell(row[3], "journal");
      tr.appendChild(name);
      tr.appendChild(cell(row[4], "rating"));
      var subject = cell(subjectLabel(row[5]));
      if (row[5] && subjectLabel(row[5]) !== row[5]) subject.title = row[5];
      tr.appendChild(subject);
      tr.appendChild(cell(String(row[1])));
      tr.appendChild(cell(row[2] || "—", row[2] ? "idcode" : "muted"));
      fragment.appendChild(tr);
    });
    rowsEl.replaceChildren(fragment);
  }

  function renderPager(matchedCount) {
    var pages = Math.max(1, Math.ceil(matchedCount / state.pageSize));
    if (state.page > pages) state.page = pages;
    pagerEl.replaceChildren();
    if (matchedCount <= state.pageSize) return;

    function button(label, disabled, delta) {
      var el = document.createElement("button");
      el.type = "button";
      el.className = "btn";
      el.textContent = label;
      el.disabled = disabled;
      el.addEventListener("click", function () {
        state.page += delta;
        render();
        document.getElementById("rankings").scrollIntoView({ block: "start" });
      });
      return el;
    }

    var pos = document.createElement("span");
    pos.className = "pos";
    pos.textContent = "Page " + formatNumber(state.page) + " of " + formatNumber(pages);
    pagerEl.appendChild(button("Previous", state.page <= 1, -1));
    pagerEl.appendChild(pos);
    pagerEl.appendChild(button("Next", state.page >= pages, 1));
  }

  function render() {
    fillYears();
    fillRatings();
    syncControls();
    var edition = editionRows();
    renderStats(edition);
    var matched = applyFilters(edition);
    var pages = Math.max(1, Math.ceil(matched.length / state.pageSize) || 1);
    if (state.page > pages) state.page = pages;
    var start = matched.length ? (state.page - 1) * state.pageSize + 1 : 0;
    var end = Math.min(state.page * state.pageSize, matched.length);
    countEl.textContent = matched.length
      ? "Showing " + formatNumber(start) + "–" + formatNumber(end) + " of " + formatNumber(matched.length) + " journals"
      : "No journals match.";
    renderTable(matched);
    renderPager(matched.length);
    writeUrl();
  }

  fillHay();
  fillSystems();

  qEl.addEventListener("input", function () {
    window.clearTimeout(debounce);
    debounce = window.setTimeout(function () {
      state.q = qEl.value.trim();
      state.page = 1;
      render();
    }, 180);
  });

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    window.clearTimeout(debounce);
    state.q = qEl.value.trim();
    state.page = 1;
    render();
  });

  systemEl.addEventListener("change", function () {
    state.system = systemEl.value;
    state.year = defaultYear(state.system);
    state.rating = "";
    state.page = 1;
    render();
  });
  yearEl.addEventListener("change", function () {
    state.year = yearEl.value;
    state.page = 1;
    render();
  });
  ratingEl.addEventListener("change", function () {
    state.rating = ratingEl.value;
    state.page = 1;
    render();
  });
  pageSizeEl.addEventListener("change", function () {
    state.pageSize = Number(pageSizeEl.value) || 50;
    state.page = 1;
    render();
  });

  clearBtn.addEventListener("click", function () {
    state.q = "";
    state.system = defaultSystem();
    state.year = defaultYear(state.system);
    state.rating = "";
    state.sort = "name";
    state.dir = "asc";
    state.page = 1;
    state.pageSize = 50;
    render();
  });

  document.querySelectorAll("th button").forEach(function (button) {
    button.addEventListener("click", function () {
      var sort = button.dataset.sort;
      if (state.sort === sort) state.dir = state.dir === "asc" ? "desc" : "asc";
      else {
        state.sort = sort;
        state.dir = sort === "rating" || sort === "year" ? "desc" : "asc";
      }
      state.page = 1;
      render();
    });
  });

  window.addEventListener("popstate", function () {
    state = readUrl();
    render();
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "/" && document.activeElement !== qEl && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "SELECT") {
      event.preventDefault();
      qEl.focus();
    }
  });

  render();
})();
