/* Institution list.
   Project Pages base: /econ-journal-dispersion/
   Styles, this file, and institutions-data.js are loaded with relative URLs.
   Do not fetch them from the site root; that host path is the user Pages root,
   not this project site.
   Row: [institution, countryIndex, continentIndex, editors, appointments, journals, mask] */
(function () {
  "use strict";

  var PAGES_BASE = "/econ-journal-dispersion/";
  var DATA = window.INSTITUTIONS_DATA;
  var numberFormat = new Intl.NumberFormat("en-US");
  var collator = new Intl.Collator("en", { sensitivity: "base", numeric: true });
  var COUNT_SORTS = { editors: true, appointments: true, journals: true };

  var countEl = document.getElementById("count");
  var rowsEl = document.getElementById("rows");
  var pagerEl = document.getElementById("pager");

  if (!DATA || !DATA.rows) {
    countEl.textContent = "Institution data is not built yet. From the repository root, run python scripts/build_site.py.";
    return;
  }

  if (DATA.base && DATA.base !== PAGES_BASE) {
    console.warn("institutions-data.js base path does not match this page", DATA.base, PAGES_BASE);
  }

  var rows = DATA.rows;
  var countries = DATA.countries || [""];
  var continents = DATA.continents || [""];
  var universes = DATA.universes || [];
  var total = rows.length;
  var hay = new Array(total);

  var qEl = document.getElementById("q");
  var continentEl = document.getElementById("continent");
  var countryEl = document.getElementById("country");
  var pageSizeEl = document.getElementById("pagesize");
  var universeRow = document.getElementById("universe-row");
  var form = document.getElementById("filters");
  var clearBtn = document.getElementById("clear");

  var state = readUrl();
  var debounce = 0;
  var countryIndex = null;

  function formatNumber(value) {
    return numberFormat.format(value);
  }

  function formatDate(iso) {
    if (!iso) return "";
    var parts = iso.split("-");
    if (parts.length !== 3) return iso;
    var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    var month = months[Number(parts[1]) - 1] || parts[1];
    return Number(parts[2]) + " " + month + " " + parts[0];
  }

  function asOfText() {
    var year = DATA.year ? "Board year " + DATA.year : "Current boards";
    if (DATA.collectedMin && DATA.collectedMax) {
      var range = DATA.collectedMin === DATA.collectedMax
        ? formatDate(DATA.collectedMin)
        : formatDate(DATA.collectedMin) + " – " + formatDate(DATA.collectedMax);
      return year + ", collected " + range + ".";
    }
    return year + ".";
  }

  function countryName(row) {
    return countries[row[1]] || "";
  }

  function continentName(row) {
    return continents[row[2]] || "";
  }

  function readUrl() {
    var params = new URLSearchParams(window.location.search);
    var size = Number(params.get("n"));
    var page = Number(params.get("page"));
    var sort = params.get("sort") || "name";
    if (["name", "country", "continent", "editors", "appointments", "journals"].indexOf(sort) === -1) sort = "name";
    return {
      q: params.get("q") || "",
      universes: new Set((params.get("u") || "").split(",").filter(Boolean)),
      continent: params.get("continent") || "",
      country: params.get("country") || "",
      sort: sort,
      dir: params.get("dir") === "desc" ? "desc" : "asc",
      page: page > 0 ? page : 1,
      pageSize: size === 100 || size === 200 ? size : 50
    };
  }

  function writeUrl() {
    var params = new URLSearchParams();
    if (state.q) params.set("q", state.q);
    if (state.universes.size) params.set("u", Array.from(state.universes).join(","));
    if (state.continent) params.set("continent", state.continent);
    if (state.country) params.set("country", state.country);
    if (state.sort !== "name") params.set("sort", state.sort);
    if (state.dir === "desc") params.set("dir", "desc");
    if (state.page > 1) params.set("page", String(state.page));
    if (state.pageSize !== 50) params.set("n", String(state.pageSize));
    var query = params.toString();
    var next = window.location.pathname + (query ? "?" + query : "") + window.location.hash;
    var current = window.location.pathname + window.location.search + window.location.hash;
    if (next !== current) history.replaceState(null, "", next);
  }

  function directoryUrl(name, country) {
    var params = new URLSearchParams();
    params.set("aff", name);
    if (country) params.set("country", country);
    return "index.html?" + params.toString();
  }

  function fillHay() {
    for (var i = 0; i < total; i++) {
      var row = rows[i];
      hay[i] = [row[0] || "", countryName(row), continentName(row)].join("\n").toLowerCase();
    }
  }

  function placeText(id, value) {
    var node = document.getElementById(id);
    if (node) node.textContent = value;
  }

  function fillHeader() {
    var counts = DATA.counts;
    placeText("n-institutions", formatNumber(counts.institutions));
    placeText("n-appointments", formatNumber(counts.appointments));
    placeText("n-editors", formatNumber(counts.editors));
    placeText("n-countries", formatNumber(counts.countries));
    var asOf = asOfText();
    placeText("asof", asOf);
    placeText("about-asof", asOf);
    placeText("footer-asof", asOf);
    var unmatched = counts.unmatchedAppointments || 0;
    placeText(
      "about-unmatched",
      formatNumber(unmatched) + (unmatched === 1 ? " appointment is" : " appointments are") +
        " omitted because they have no named institution."
    );
    placeText(
      "about-ror",
      formatNumber(counts.withRor) + " of " + formatNumber(counts.institutions) + " rows are a ROR id."
    );
  }

  function addOption(select, value, label) {
    var option = document.createElement("option");
    option.value = value;
    option.textContent = label;
    select.appendChild(option);
  }

  function matchesChoice(value, selected) {
    if (!selected) return true;
    if (selected === "__blank__") return !value;
    return value === selected;
  }

  function buildCountryIndex() {
    var all = new Set();
    var byContinent = new Map();
    var blankAll = false;
    var blankByContinent = new Set();
    for (var i = 0; i < total; i++) {
      var country = countryName(rows[i]);
      var continent = continentName(rows[i]);
      var key = continent || "__blank__";
      if (!byContinent.has(key)) byContinent.set(key, new Set());
      if (!country) {
        blankAll = true;
        blankByContinent.add(key);
        continue;
      }
      all.add(country);
      byContinent.get(key).add(country);
    }
    function sorted(set) {
      return Array.from(set).sort(function (a, b) { return collator.compare(a, b); });
    }
    var lists = new Map();
    byContinent.forEach(function (set, key) { lists.set(key, sorted(set)); });
    countryIndex = {
      all: sorted(all),
      lists: lists,
      blankAll: blankAll,
      blankByContinent: blankByContinent
    };
  }

  function countriesForContinent(continent) {
    if (!continent) return { list: countryIndex.all, blank: countryIndex.blankAll };
    var key = continent === "__blank__" ? "__blank__" : continent;
    return {
      list: countryIndex.lists.get(key) || [],
      blank: countryIndex.blankByContinent.has(key)
    };
  }

  function refillCountries() {
    var previous = state.country;
    var found = countriesForContinent(state.continent);
    var signature = state.continent + "\n" + found.list.join("\n") + "\n" + found.blank;
    if (countryEl.dataset.signature === signature) {
      countryEl.value = state.country;
      return;
    }
    countryEl.dataset.signature = signature;
    countryEl.replaceChildren();
    addOption(countryEl, "", "All countries");
    for (var i = 0; i < found.list.length; i++) addOption(countryEl, found.list[i], found.list[i]);
    if (found.blank) addOption(countryEl, "__blank__", "Unknown");
    var stillThere = !previous || found.list.indexOf(previous) !== -1 || (previous === "__blank__" && found.blank);
    if (!stillThere) {
      state.country = "";
      state.page = 1;
    }
    countryEl.value = state.country;
  }

  function initControls() {
    var continentNames = continents.filter(Boolean).slice().sort(function (a, b) {
      return collator.compare(a, b);
    });
    continentNames.forEach(function (name) { addOption(continentEl, name, name); });
    buildCountryIndex();
    if (countryIndex.lists.has("__blank__")) addOption(continentEl, "__blank__", "Unknown");

    universes.forEach(function (universe) {
      var button = document.createElement("button");
      button.type = "button";
      button.className = "chip";
      button.dataset.universe = universe.id;
      button.setAttribute("aria-pressed", "false");
      var count = DATA.counts.byUniverse[universe.id];
      button.appendChild(document.createTextNode(universe.label + " "));
      var countNode = document.createElement("span");
      countNode.className = "c";
      countNode.textContent = formatNumber(count.institutions);
      button.appendChild(countNode);
      button.addEventListener("click", function () {
        if (state.universes.has(universe.id)) state.universes.delete(universe.id);
        else state.universes.add(universe.id);
        state.page = 1;
        render();
      });
      universeRow.appendChild(button);
    });
  }

  function selectedMask() {
    var mask = 0;
    state.universes.forEach(function (id) {
      for (var i = 0; i < universes.length; i++) {
        if (universes[i].id === id) mask |= universes[i].bit;
      }
    });
    return mask;
  }

  function sortValue(index) {
    var row = rows[index];
    switch (state.sort) {
      case "country": return countryName(row);
      case "continent": return continentName(row);
      case "editors": return row[3];
      case "appointments": return row[4];
      case "journals": return row[5];
      default: return row[0] || "";
    }
  }

  function compareSort(a, b) {
    var va = sortValue(a);
    var vb = sortValue(b);
    if (typeof va === "number") return va - vb;
    return collator.compare(va, vb);
  }

  function applyFilters() {
    var mask = selectedMask();
    var tokens = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    var continent = state.continent;
    var country = state.country;
    var matched = [];
    var uniCounts = {};
    for (var u = 0; u < universes.length; u++) uniCounts[universes[u].id] = 0;

    for (var i = 0; i < total; i++) {
      var row = rows[i];
      if (mask && (row[6] & mask) === 0) continue;
      if (!matchesChoice(continentName(row), continent)) continue;
      if (!matchesChoice(countryName(row), country)) continue;
      if (tokens.length) {
        var text = hay[i];
        var missed = false;
        for (var t = 0; t < tokens.length; t++) {
          if (text.indexOf(tokens[t]) === -1) {
            missed = true;
            break;
          }
        }
        if (missed) continue;
      }
      matched.push(i);
      for (var k = 0; k < universes.length; k++) {
        if (row[6] & universes[k].bit) uniCounts[universes[k].id] += 1;
      }
    }

    var sign = state.dir === "desc" ? -1 : 1;
    matched.sort(function (a, b) {
      var compared = compareSort(a, b);
      if (compared) return compared * sign;
      return collator.compare(rows[a][0], rows[b][0]);
    });
    return { matched: matched, uniCounts: uniCounts };
  }

  function syncControls() {
    if (document.activeElement !== qEl) qEl.value = state.q;
    continentEl.value = state.continent;
    pageSizeEl.value = String(state.pageSize);
    refillCountries();
    universeRow.querySelectorAll(".chip").forEach(function (chip) {
      chip.setAttribute("aria-pressed", state.universes.has(chip.dataset.universe) ? "true" : "false");
    });
    document.querySelectorAll("th button").forEach(function (button) {
      if (button.dataset.sort === state.sort) {
        button.setAttribute("aria-sort", state.dir === "desc" ? "descending" : "ascending");
      } else {
        button.removeAttribute("aria-sort");
      }
    });
  }

  function numCell(value) {
    var td = document.createElement("td");
    td.className = "num";
    td.textContent = formatNumber(value);
    return td;
  }

  function textCell(text) {
    var td = document.createElement("td");
    td.textContent = text || "—";
    if (!text) td.className = "muted";
    return td;
  }

  function renderTable(matched) {
    var start = (state.page - 1) * state.pageSize;
    var slice = matched.slice(start, start + state.pageSize);
    var fragment = document.createDocumentFragment();
    if (!slice.length) {
      var emptyRow = document.createElement("tr");
      var emptyCell = document.createElement("td");
      emptyCell.colSpan = 6;
      emptyCell.className = "empty";
      emptyCell.textContent = "No institutions match these filters.";
      emptyRow.appendChild(emptyCell);
      fragment.appendChild(emptyRow);
    }
    slice.forEach(function (index) {
      var row = rows[index];
      var tr = document.createElement("tr");
      var nameCell = document.createElement("td");
      nameCell.className = "journal";
      var link = document.createElement("a");
      link.className = "journal";
      link.href = directoryUrl(row[0], countryName(row));
      link.textContent = row[0];
      nameCell.appendChild(link);
      tr.appendChild(nameCell);
      tr.appendChild(textCell(countryName(row)));
      tr.appendChild(textCell(continentName(row)));
      tr.appendChild(numCell(row[3]));
      tr.appendChild(numCell(row[4]));
      tr.appendChild(numCell(row[5]));
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
        document.getElementById("institutions").scrollIntoView({ block: "start" });
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
    syncControls();
    var result = applyFilters();
    var matched = result.matched;
    var pages = Math.max(1, Math.ceil(matched.length / state.pageSize) || 1);
    if (state.page > pages) state.page = pages;
    var start = matched.length ? (state.page - 1) * state.pageSize + 1 : 0;
    var end = Math.min(state.page * state.pageSize, matched.length);
    countEl.textContent = matched.length
      ? "Showing " + formatNumber(start) + "–" + formatNumber(end) + " of " + formatNumber(matched.length) + " institutions"
      : "No institutions match.";
    universeRow.querySelectorAll(".chip").forEach(function (chip) {
      var count = chip.querySelector(".c");
      if (count) count.textContent = formatNumber(result.uniCounts[chip.dataset.universe] || 0);
    });
    renderTable(matched);
    renderPager(matched.length);
    writeUrl();
  }

  fillHay();
  fillHeader();
  initControls();

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

  continentEl.addEventListener("change", function () {
    state.continent = continentEl.value;
    state.page = 1;
    render();
  });
  countryEl.addEventListener("change", function () {
    state.country = countryEl.value;
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
    state.universes = new Set();
    state.continent = "";
    state.country = "";
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
        state.dir = COUNT_SORTS[sort] ? "desc" : "asc";
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
