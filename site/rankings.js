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
  // Higher number is the better grade. The default order is this rank,
  // best first, then the journal name A–Z. CNRS 1 / 1e / 1g / 1eg share the
  // top category. FNEGE EM and NC follow 1* > 1 > 2 > 3 > 4. A blank
  // Handelsblatt letter sits below F; the same letter then uses weight,
  // higher first. Shanghai is one Top grade, so that list stays A–Z.
  // FT50, UTD24, and Top 5 are absent and stay A–Z.
  // Stern mixes six department vocabularies. Top 5 outranks Really excellent,
  // which outranks Top-tier. Field and Specialized high-impact are the
  // specialized tier under that. Other notable, Notable review, and Review
  // share the bottom tier. Economics keeps its printed order. A department's
  // top-tier list outranks its notable or specialized list.
  // SHUFE is Top Tier, then First Tier, then Second Tier, then Third Tier.
  var RATING_RANK = {
    abs_ajg: { "4*": 5, "4": 4, "3": 3, "2": 2, "1": 1 },
    abdc: { "A*": 4, "A": 3, "B": 2, "C": 1 },
    cnrs: { "1": 5, "1e": 5, "1g": 5, "1eg": 5, "2": 4, "3": 3, "4": 2 },
    handelsblatt_vwl: { "A+": 7, "A": 6, "B": 5, "C": 4, "D": 3, "E": 2, "F": 1 },
    tilburg: { "Top-core": 3, "Top": 2, "Very good": 1 },
    fnege: { "1*": 7, "1": 6, "2": 5, "3": 4, "4": 3, "EM": 2, "NC": 1 },
    erim: { "STAR": 8, "M-STAR": 7, "P": 6, "EP*": 5, "PA": 4, "S": 3, "S (3=1)": 2, "M": 1 },
    stern: {
      "Top 5": 5,
      "Really excellent": 4,
      "Top-tier": 3,
      "Field": 2,
      "Specialized high-impact": 2,
      "Other notable": 1,
      "Notable review": 1,
      "Review": 1
    },
    shanghai: { "Top": 1 },
    shufe: { "Top Tier": 4, "First Tier": 3, "Second Tier": 2, "Third Tier": 1 }
  };
  // build_rankings.py joins a Stern department code and memo heading with this.
  var STERN_FIELD_SEP = "\u001f";
  var TOP_SUB = {
    abs_ajg: "Highest grade that year",
    cnrs: "Highest category",
    handelsblatt_vwl: "Highest class",
    tilburg: "Highest tier",
    fnege: "Highest grade",
    erim: "Highest class",
    stern: "Highest tier",
    shanghai: "Top journals",
    shufe: "Highest tier"
  };

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
  var fieldEl = document.getElementById("field");
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

  function sternParts(code) {
    var text = code || "";
    var sep = text.indexOf(STERN_FIELD_SEP);
    if (sep === -1) return { dept: text, sub: "" };
    return { dept: text.slice(0, sep), sub: text.slice(sep + 1) };
  }

  function subjectLabel(system, code) {
    if (system === "stern") {
      var parts = sternParts(code);
      var sternLabels = (DATA.fieldLabels && DATA.fieldLabels.stern) || {};
      var dept = sternLabels[parts.dept] || parts.dept || "";
      if (!dept) return "";
      return parts.sub ? dept + " — " + parts.sub : dept;
    }
    var bySystem = (DATA.fieldLabels && DATA.fieldLabels[system]) || {};
    if (code && Object.prototype.hasOwnProperty.call(bySystem, code)) return bySystem[code];
    return labels[code] || code || "";
  }

  function systemMeta(id) {
    var systems = DATA.systems || [];
    for (var i = 0; i < systems.length; i++) {
      if (systems[i].id === id) return systems[i];
    }
    return null;
  }

  function systemLabel(id) {
    var meta = systemMeta(id);
    return meta ? meta.label : id;
  }

  function showsWeight(system) {
    var meta = systemMeta(system);
    return !!(meta && meta.showWeight);
  }

  function ratingRank(system, rating) {
    var table = RATING_RANK[system] || {};
    return table[rating] || 0;
  }

  function hasGradeTiers(system) {
    return Object.keys(RATING_RANK[system] || {}).length > 1;
  }

  function defaultSort(system) {
    return hasGradeTiers(system) ? "rating" : "name";
  }

  function defaultDir(sort) {
    return sort === "rating" || sort === "year" || sort === "weight" ? "desc" : "asc";
  }

  function compareName(left, right) {
    return collator.compare(left[3] || "", right[3] || "");
  }

  function compareWeight(left, right) {
    var wa = parseFloat(left[8]);
    var wb = parseFloat(right[8]);
    var aok = isFinite(wa);
    var bok = isFinite(wb);
    if (aok && bok) return wa - wb;
    if (aok) return 1;
    if (bok) return -1;
    return 0;
  }

  function knownSystem(id) {
    var systems = DATA.systems || [];
    for (var i = 0; i < systems.length; i++) {
      if (systems[i].id === id) return true;
    }
    return false;
  }

  function ratingsFor(system, year) {
    var table = DATA.ratings || {};
    var all = Object.prototype.hasOwnProperty.call(table, system)
      ? table[system].slice()
      : ["4*", "4", "3", "2", "1"];
    if (system === "abs_ajg" && String(year) === "2010") {
      return all.filter(function (grade) { return grade !== "4*"; });
    }
    if (system === "stern") {
      var seen = {};
      var yearKey = String(year);
      for (var i = 0; i < total; i++) {
        var row = rows[i];
        if (row[0] !== "stern" || String(row[1]) !== yearKey || !row[4]) continue;
        seen[row[4]] = true;
      }
      return all.filter(function (grade) { return seen[grade]; });
    }
    return all;
  }

  function defaultSystem() {
    return (DATA.systems && DATA.systems[0] && DATA.systems[0].id) || "abs_ajg";
  }

  function defaultYear(system) {
    var years = (DATA.editions && DATA.editions[system]) || [];
    if (!years.length) return "";
    return String(years[years.length - 1]);
  }

  function readUrl() {
    var params = new URLSearchParams(window.location.search);
    var size = Number(params.get("n"));
    var page = Number(params.get("page"));
    var system = params.get("system") || defaultSystem();
    if (!knownSystem(system)) system = defaultSystem();
    var year = params.get("year") || defaultYear(system);
    var sort = params.get("sort") || defaultSort(system);
    if (sort === "subject") sort = "field";
    if (["name", "rating", "field", "year", "id", "weight"].indexOf(sort) === -1) sort = defaultSort(system);
    var dirParam = params.get("dir");
    var dir = dirParam === "asc" || dirParam === "desc" ? dirParam : defaultDir(sort);
    return {
      q: params.get("q") || "",
      system: system,
      year: year,
      rating: params.get("rating") || "",
      field: params.get("field") || "",
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
    if (state.field) params.set("field", state.field);
    var sortIsDefault = state.sort === defaultSort(state.system) && state.dir === defaultDir(state.sort);
    if (!sortIsDefault) {
      params.set("sort", state.sort);
      if (state.dir !== defaultDir(state.sort)) params.set("dir", state.dir);
    }
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
        subjectLabel(row[0], code),
        row[6] || "",
        row[7] || "",
        row[8] || ""
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
    years.sort(function (a, b) {
      var na = Number(a);
      var nb = Number(b);
      if (isFinite(na) && isFinite(nb)) return nb - na;
      return collator.compare(String(b), String(a));
    });
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
    addOption(ratingEl, "", grades.length ? "All ratings" : "No grades");
    grades.forEach(function (grade) {
      addOption(ratingEl, grade, grade);
    });
    ratingEl.disabled = grades.length === 0;
    ratingEl.title = grades.length ? "" : "This list has no grade tiers";
    if (current && grades.indexOf(current) === -1) state.rating = "";
  }

  function fieldsForEdition() {
    var seen = {};
    var list = [];
    editionRows().forEach(function (index) {
      var code = rows[index][5] || "";
      if (state.system === "stern") code = sternParts(code).dept;
      if (!code || seen[code]) return;
      seen[code] = true;
      list.push(code);
    });
    list.sort(function (a, b) {
      return collator.compare(subjectLabel(state.system, a), subjectLabel(state.system, b));
    });
    return list;
  }

  function fillFields() {
    var fields = fieldsForEdition();
    var current = state.field;
    fieldEl.replaceChildren();
    var fieldBlank = state.system === "stern" ? "All departments" : "All fields";
    addOption(fieldEl, "", fields.length ? fieldBlank : "No fields");
    fields.forEach(function (code) {
      addOption(fieldEl, code, subjectLabel(state.system, code));
    });
    fieldEl.disabled = fields.length === 0;
    if (state.system === "stern" && fields.length) {
      fieldEl.title = "Department on this edition. The table adds the memo heading when the row has one.";
    } else {
      fieldEl.title = fields.length ? "" : "This list has no field";
    }
    if (current && fields.indexOf(current) === -1) state.field = "";
  }

  function syncControls() {
    qEl.value = state.q;
    systemEl.value = state.system;
    yearEl.value = state.year;
    ratingEl.value = state.rating;
    fieldEl.value = state.field;
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
    var year = String(state.year);
    var matched = [];
    for (var i = 0; i < total; i++) {
      var row = rows[i];
      if (row[0] !== state.system) continue;
      if (String(row[1]) !== year) continue;
      matched.push(i);
    }
    return matched;
  }

  function applyFilters(indexes) {
    var query = state.q.trim().toLowerCase();
    var rating = state.rating;
    var field = state.field;
    var matched = [];
    indexes.forEach(function (index) {
      var row = rows[index];
      if (rating && row[4] !== rating) return;
      if (field) {
        var rowField = row[5] || "";
        if (state.system === "stern") {
          if (sternParts(rowField).dept !== field) return;
        } else if (rowField !== field) return;
      }
      if (query && hay[index].indexOf(query) === -1) return;
      matched.push(index);
    });
    var dir = state.dir === "desc" ? -1 : 1;
    matched.sort(function (a, b) {
      var ra = rows[a];
      var rb = rows[b];
      var cmp = 0;
      if (state.sort === "rating") {
        cmp = ratingRank(state.system, ra[4]) - ratingRank(state.system, rb[4]);
        if (cmp !== 0) return cmp * dir;
        if (showsWeight(state.system)) {
          cmp = compareWeight(ra, rb);
          if (cmp !== 0) return -cmp;
        }
        return compareName(ra, rb);
      }
      if (state.sort === "weight") cmp = compareWeight(ra, rb);
      else if (state.sort === "field") cmp = collator.compare(subjectLabel(state.system, ra[5]), subjectLabel(state.system, rb[5]));
      else if (state.sort === "year") {
        var ya = Number(ra[1]);
        var yb = Number(rb[1]);
        cmp = isFinite(ya) && isFinite(yb) ? ya - yb : collator.compare(String(ra[1]), String(rb[1]));
      }
      else if (state.sort === "id") cmp = collator.compare(ra[2] || "", rb[2] || "");
      else cmp = compareName(ra, rb);
      if (cmp === 0) cmp = compareName(ra, rb);
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
    var grades = ratingsFor(state.system, state.year);
    var topGrade = grades.length ? grades[0] : "";
    var topCount = 0;
    var mapped = 0;
    indexes.forEach(function (index) {
      var row = rows[index];
      if (topGrade && row[4] === topGrade) topCount += 1;
      if (row[2]) mapped += 1;
    });
    nJournals.textContent = formatNumber(indexes.length);
    sJournals.textContent = systemLabel(state.system) + " " + state.year;
    if (topGrade) {
      nTop.textContent = formatNumber(topCount);
      lTop.textContent = topGrade;
      sTop.textContent = topGrade === "4*"
        ? "Journals of Distinction"
        : (TOP_SUB[state.system] || "Highest rating");
    } else {
      nTop.textContent = "—";
      lTop.textContent = "Rating";
      sTop.textContent = "No grade tiers";
    }
    nMapped.textContent = formatNumber(mapped);
    var sMapped = document.getElementById("s-mapped");
    if (sMapped) {
      var rate = indexes.length ? (100 * mapped / indexes.length) : 0;
      sMapped.textContent = rate.toFixed(1) + "% of this edition";
    }
    var years = (DATA.editions && DATA.editions[state.system]) || [];
    nEditions.textContent = formatNumber(years.length);
    var sEditions = document.getElementById("s-editions");
    if (sEditions) sEditions.textContent = years.length > 1 ? "Editions on file" : "List on file";
  }

  function renderTable(matched) {
    var fragment = document.createDocumentFragment();
    var start = (state.page - 1) * state.pageSize;
    var slice = matched.slice(start, start + state.pageSize);
    if (!slice.length) {
      var tr = document.createElement("tr");
      var td = document.createElement("td");
      td.colSpan = showsWeight(state.system) ? 6 : 5;
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
      var ratingCell = cell(row[4] || "—", row[4] ? "rating" : "muted");
      if (row[4] && state.system === "tilburg") ratingCell.title = "TISEM top journal list";
      if (row[4] && state.system === "fnege") ratingCell.title = "FNEGE " + row[1];
      if (row[4] && state.system === "erim") ratingCell.title = "ERIM Journals List Core 2024–2028";
      if (row[4] && state.system === "stern") {
        ratingCell.title = "NYU Stern " + subjectLabel("stern", sternParts(row[5] || "").dept) + " top journals, " + row[1];
      }
      if (row[4] && state.system === "shanghai") ratingCell.title = "ShanghaiRanking top journals " + row[1];
      if (row[4] && state.system === "shufe") ratingCell.title = "SHUFE Tenure-Track Journal List";
      tr.appendChild(ratingCell);
      var fieldText = row[5] ? subjectLabel(state.system, row[5]) : "";
      var fieldCell = cell(fieldText || "—", row[5] ? "field" : "muted");
      if (state.system === "stern" && row[5]) {
        var sternField = sternParts(row[5]);
        fieldCell.title = sternField.sub ? sternField.dept + " · " + sternField.sub : sternField.dept;
      } else if (row[5] && fieldText !== row[5]) fieldCell.title = row[5];
      tr.appendChild(fieldCell);
      tr.appendChild(cell(String(row[1])));
      if (showsWeight(state.system)) tr.appendChild(cell(row[8] || "—", row[8] ? "weight" : "muted"));
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
    fillFields();
    var weightCol = document.getElementById("col-weight");
    if (weightCol) weightCol.hidden = !showsWeight(state.system);
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
    var previous = state.system;
    var wasDefault = state.sort === defaultSort(previous) && state.dir === defaultDir(state.sort);
    state.system = systemEl.value;
    state.year = defaultYear(state.system);
    state.rating = "";
    state.field = "";
    if (!showsWeight(state.system) && state.sort === "weight") wasDefault = true;
    if (wasDefault) {
      state.sort = defaultSort(state.system);
      state.dir = defaultDir(state.sort);
    }
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
  fieldEl.addEventListener("change", function () {
    state.field = fieldEl.value;
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
    state.field = "";
    state.sort = defaultSort(state.system);
    state.dir = defaultDir(state.sort);
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
        state.dir = sort === "rating" || sort === "year" || sort === "weight" ? "desc" : "asc";
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
