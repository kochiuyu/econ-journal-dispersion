/* Journal editor directory.
   Project Pages base: /econ-journal-dispersion/
   Styles, this file, and data.js are loaded with relative URLs from index.html.
   Do not fetch them from the site root; that host path is the user Pages root,
   not this project site. */
(function () {
  "use strict";

  var PAGES_BASE = "/econ-journal-dispersion/";
  var DATA = window.EDITOR_DATA;
  var numberFormat = new Intl.NumberFormat("en-US");
  var collator = new Intl.Collator("en", { sensitivity: "base", numeric: true });

  var countEl = document.getElementById("count");
  var rowsEl = document.getElementById("rows");
  var pagerEl = document.getElementById("pager");

  if (!DATA || !DATA.rows) {
    countEl.textContent = "Directory data is not built yet. From the repository root, run python scripts/build_site.py.";
    return;
  }

  if (DATA.base && DATA.base !== PAGES_BASE) {
    console.warn("data.js base path does not match this page", DATA.base, PAGES_BASE);
  }

  var rows = DATA.rows;
  var roles = DATA.roles;
  var roleFamily = DATA.roleFamily;
  var families = DATA.families;
  var journals = DATA.journals;
  var fields = DATA.fields || [""];
  var journalField = DATA.journalField || [];
  var countries = DATA.countries;
  var continents = DATA.continents;
  var urls = DATA.urls;
  var profiles = DATA.profiles || [""];
  var universes = DATA.universes;
  var total = rows.length;
  var hay = new Array(total);
  var orderCache = new Map();

  var qEl = document.getElementById("q");
  var roleEl = document.getElementById("role");
  var continentEl = document.getElementById("continent");
  var countryEl = document.getElementById("country");
  var journalEl = document.getElementById("journal");
  var institutionEl = document.getElementById("institution");
  var fieldEl = document.getElementById("field");
  var pageSizeEl = document.getElementById("pagesize");
  var universeRow = document.getElementById("universe-row");
  var form = document.getElementById("filters");
  var clearBtn = document.getElementById("clear");

  var state = readUrl();
  var debounce = 0;

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

  function universeSelection(raw) {
    var selected = (raw || "").split(",").filter(Boolean);
    if (selected.indexOf("ajg") === -1) return selected;
    var next = [];
    selected.forEach(function (id) {
      if (id !== "ajg" && next.indexOf(id) === -1) next.push(id);
    });
    universes.forEach(function (universe) {
      if (universe.id.indexOf("ajg_") === 0 && next.indexOf(universe.id) === -1) next.push(universe.id);
    });
    return next;
  }

  function readUrl() {
    var params = new URLSearchParams(window.location.search);
    var size = Number(params.get("n"));
    var page = Number(params.get("page"));
    return {
      q: params.get("q") || "",
      universes: new Set(universeSelection(params.get("u"))),
      role: params.get("role") || "",
      continent: params.get("continent") || "",
      country: params.get("country") || "",
      journal: params.get("journal") || "",
      aff: params.get("aff") || "",
      field: params.get("field") || "",
      sort: params.get("sort") || "name",
      dir: params.get("dir") === "desc" ? "desc" : "asc",
      page: page > 0 ? page : 1,
      pageSize: size === 100 || size === 200 ? size : 50
    };
  }

  function writeUrl() {
    var params = new URLSearchParams();
    if (state.q) params.set("q", state.q);
    if (state.universes.size) params.set("u", Array.from(state.universes).join(","));
    if (state.role) params.set("role", state.role);
    if (state.continent) params.set("continent", state.continent);
    if (state.country) params.set("country", state.country);
    if (state.journal) params.set("journal", state.journal);
    if (state.aff) params.set("aff", state.aff);
    if (state.field) params.set("field", state.field);
    if (state.sort !== "name") params.set("sort", state.sort);
    if (state.dir === "desc") params.set("dir", "desc");
    if (state.page > 1) params.set("page", String(state.page));
    if (state.pageSize !== 50) params.set("n", String(state.pageSize));
    var query = params.toString();
    var next = window.location.pathname + (query ? "?" + query : "") + window.location.hash;
    var current = window.location.pathname + window.location.search + window.location.hash;
    if (next !== current) {
      window.history.replaceState(null, "", next);
    }
  }

  function haystack(index) {
    var cached = hay[index];
    if (cached) return cached;
    var row = rows[index];
    cached = [
      row[0],
      roles[row[1]],
      families[roleFamily[row[1]]],
      journals[row[2]],
      fieldText(journalField[row[2]]),
      fieldLabel(fieldText(journalField[row[2]])),
      row[4],
      countries[row[5]],
      continents[row[6]]
    ].join("\n").toLowerCase();
    hay[index] = cached;
    return cached;
  }

  function fieldText(index) {
    return fields[index] || "";
  }

  function fieldLabel(field) {
    var match = /^(\d+)\s+([\s\S]+)$/.exec(field || "");
    return match ? match[2] : (field || "");
  }

  function fieldOf(row) {
    return fieldText(journalField[row[2]]);
  }

  function universeText(mask) {
    var labels = [];
    for (var i = 0; i < universes.length; i++) {
      if (mask & universes[i].bit) labels.push(universes[i].label);
    }
    return labels.join(" ");
  }

  function nameSortKey(name) {
    return (name || "").replace(/^[^0-9A-Za-z\u00C0-\u024F\u0400-\u04FF\u4E00-\u9FFF]+/, "");
  }

  function sortValue(index, sort) {
    var row = rows[index];
    switch (sort) {
      case "role": return roles[row[1]] || "";
      case "journal": return journals[row[2]] || "";
      case "field": return fieldLabel(fieldOf(row));
      case "universe": return universeText(row[3]);
      case "affiliation": return row[4] || "";
      case "country": return countries[row[5]] || "";
      case "continent": return continents[row[6]] || "";
      default: return nameSortKey(row[0]);
    }
  }

  function getOrder() {
    var key = state.sort + ":" + state.dir;
    var cached = orderCache.get(key);
    if (cached) return cached;
    var order = new Array(total);
    for (var i = 0; i < total; i++) order[i] = i;
    if (!(state.sort === "name" && state.dir === "asc")) {
      var sign = state.dir === "desc" ? -1 : 1;
      var sort = state.sort;
      order.sort(function (a, b) {
        var compared = collator.compare(sortValue(a, sort), sortValue(b, sort));
        if (compared) return compared * sign;
        return a - b;
      });
    }
    orderCache.set(key, order);
    return order;
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

  function applyFilters() {
    var order = getOrder();
    var mask = selectedMask();
    var tokens = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    var role = state.role;
    var continent = state.continent;
    var country = state.country;
    var journal = state.journal;
    var aff = state.aff;
    var field = state.field;
    var matched = [];
    var uniCounts = {};
    for (var u = 0; u < universes.length; u++) uniCounts[universes[u].id] = 0;

    for (var n = 0; n < order.length; n++) {
      var index = order[n];
      var row = rows[index];
      if (mask && (row[3] & mask) === 0) continue;
      if (journal && journals[row[2]] !== journal) continue;
      if (!matchesChoice(row[4] || "", aff)) continue;
      if (!matchesChoice(fieldOf(row), field)) continue;
      if (!matchesChoice(continents[row[6]] || "", continent)) continue;
      if (!matchesChoice(countries[row[5]] || "", country)) continue;
      if (role && families[roleFamily[row[1]]] !== role) continue;
      if (tokens.length) {
        var text = haystack(index);
        var missed = false;
        for (var t = 0; t < tokens.length; t++) {
          if (text.indexOf(tokens[t]) === -1) {
            missed = true;
            break;
          }
        }
        if (missed) continue;
      }
      matched.push(index);
      for (var k = 0; k < universes.length; k++) {
        if (row[3] & universes[k].bit) uniCounts[universes[k].id] += 1;
      }
    }
    return { matched: matched, uniCounts: uniCounts };
  }

  function placeText(id, value) {
    var node = document.getElementById(id);
    if (node) node.textContent = value;
  }

  function fillHeader() {
    var counts = DATA.counts;
    placeText("n-appointments", formatNumber(counts.appointments));
    placeText("n-editors", formatNumber(counts.editors));
    placeText("n-journals", formatNumber(counts.journals));
    placeText("n-countries", formatNumber(counts.countries));
    var asOf = asOfText();
    placeText("asof", asOf);
    placeText("about-asof", asOf);
    placeText("footer-asof", asOf);
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

  var countryIndex = null;

  function buildCountryIndex() {
    var all = new Set();
    var byContinent = new Map();
    var blankAll = false;
    var blankByContinent = new Set();
    for (var i = 0; i < total; i++) {
      var country = countries[rows[i][5]] || "";
      var continent = continents[rows[i][6]] || "";
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
    if (!continent) {
      return { list: countryIndex.all, blank: countryIndex.blankAll };
    }
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
    for (var i = 0; i < found.list.length; i++) {
      addOption(countryEl, found.list[i], found.list[i]);
    }
    if (found.blank) addOption(countryEl, "__blank__", "Unknown");
    var stillThere = !previous || found.list.indexOf(previous) !== -1 || (previous === "__blank__" && found.blank);
    if (!stillThere) {
      state.country = "";
      state.page = 1;
    }
    countryEl.value = state.country;
  }

  function initControls() {
    families.forEach(function (family) {
      addOption(roleEl, family, family);
    });

    var continentNames = continents.filter(Boolean).slice().sort(function (a, b) {
      return collator.compare(a, b);
    });
    continentNames.forEach(function (name) { addOption(continentEl, name, name); });
    buildCountryIndex();
    if (countryIndex.lists.has("__blank__")) addOption(continentEl, "__blank__", "Unknown");

    var journalNames = journals.slice().sort(function (a, b) { return collator.compare(a, b); });
    journalNames.forEach(function (name) { addOption(journalEl, name, name); });

    var institutionNames = [];
    var seenInstitution = new Set();
    var blankInstitution = false;
    for (var i = 0; i < total; i++) {
      var institution = rows[i][4] || "";
      if (!institution) {
        blankInstitution = true;
        continue;
      }
      if (seenInstitution.has(institution)) continue;
      seenInstitution.add(institution);
      institutionNames.push(institution);
    }
    institutionNames.sort(function (a, b) { return collator.compare(a, b); });
    institutionNames.forEach(function (name) { addOption(institutionEl, name, name); });
    if (blankInstitution) addOption(institutionEl, "__blank__", "Unknown");
    if (state.aff && state.aff !== "__blank__" && !seenInstitution.has(state.aff)) {
      addOption(institutionEl, state.aff, state.aff);
    }

    var fieldNames = [];
    var seenField = new Set();
    var blankField = false;
    for (var j = 0; j < journals.length; j++) {
      var fieldName = fieldText(journalField[j]);
      if (!fieldName) {
        blankField = true;
        continue;
      }
      if (seenField.has(fieldName)) continue;
      seenField.add(fieldName);
      fieldNames.push(fieldName);
    }
    fieldNames.sort(function (a, b) { return collator.compare(fieldLabel(a), fieldLabel(b)); });
    fieldNames.forEach(function (name) {
      var option = document.createElement("option");
      option.value = name;
      option.textContent = fieldLabel(name);
      if (fieldLabel(name) !== name) option.title = name;
      fieldEl.appendChild(option);
    });
    if (blankField) addOption(fieldEl, "__blank__", "Unknown");
    if (state.field && state.field !== "__blank__" && !seenField.has(state.field)) {
      addOption(fieldEl, state.field, fieldLabel(state.field));
    }

    universes.forEach(function (universe) {
      var button = document.createElement("button");
      button.type = "button";
      button.className = "chip";
      button.dataset.universe = universe.id;
      button.setAttribute("aria-pressed", "false");
      var count = DATA.counts.byUniverse[universe.id];
      if (universe.title) button.title = universe.title;
      button.appendChild(document.createTextNode(universe.label + " "));
      var countNode = document.createElement("span");
      countNode.className = "c";
      countNode.textContent = formatNumber(count.appointments);
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

  function syncControls() {
    if (document.activeElement !== qEl) qEl.value = state.q;
    roleEl.value = state.role;
    journalEl.value = state.journal;
    institutionEl.value = state.aff;
    fieldEl.value = state.field;
    pageSizeEl.value = String(state.pageSize);
    continentEl.value = state.continent;
    refillCountries();
    var chips = universeRow.querySelectorAll(".chip");
    chips.forEach(function (chip) {
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

  function badge(universe) {
    var node = document.createElement("span");
    node.className = "badge u-" + universe.id;
    node.textContent = universe.label;
    if (universe.title) node.title = universe.title;
    return node;
  }

  function cell(text) {
    var td = document.createElement("td");
    td.textContent = text || "—";
    if (!text) td.className = "muted";
    return td;
  }

  function httpUrl(url) {
    return url.indexOf("http://") === 0 || url.indexOf("https://") === 0;
  }

  function nameCell(name, url) {
    var td = document.createElement("td");
    if (name && httpUrl(url)) {
      var link = document.createElement("a");
      link.className = "person";
      link.href = url;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.title = "Faculty profile";
      link.textContent = name;
      td.appendChild(link);
    } else {
      td.textContent = name || "—";
      if (!name) td.className = "muted";
    }
    return td;
  }

  function renderTable(matched) {
    var start = (state.page - 1) * state.pageSize;
    var slice = matched.slice(start, start + state.pageSize);
    var fragment = document.createDocumentFragment();
    if (!slice.length) {
      var tr = document.createElement("tr");
      var td = document.createElement("td");
      td.colSpan = 8;
      td.className = "empty";
      td.textContent = "No editors match these filters.";
      tr.appendChild(td);
      fragment.appendChild(tr);
    }
    slice.forEach(function (index) {
      var row = rows[index];
      var tr = document.createElement("tr");
      var profileUrl = row.length > 8 ? (profiles[row[8]] || "") : "";
      tr.appendChild(nameCell(row[0], profileUrl));
      tr.appendChild(cell(roles[row[1]]));

      var journalCell = document.createElement("td");
      journalCell.className = "journal";
      var url = urls[row[7]] || "";
      var journalName = journals[row[2]] || "—";
      if (httpUrl(url)) {
        var link = document.createElement("a");
        link.className = "journal";
        link.href = url;
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        link.textContent = journalName;
        journalCell.appendChild(link);
      } else {
        journalCell.textContent = journalName;
      }
      tr.appendChild(journalCell);

      var fieldName = fieldOf(row);
      var fieldCell = document.createElement("td");
      fieldCell.className = fieldName ? "field" : "muted";
      fieldCell.textContent = fieldName ? fieldLabel(fieldName) : "—";
      if (fieldName && fieldLabel(fieldName) !== fieldName) fieldCell.title = fieldName;
      tr.appendChild(fieldCell);

      var listCell = document.createElement("td");
      var any = false;
      universes.forEach(function (universe) {
        if (row[3] & universe.bit) {
          listCell.appendChild(badge(universe));
          any = true;
        }
      });
      if (!any) listCell.textContent = "—";
      tr.appendChild(listCell);

      var affiliation = cell(row[4]);
      affiliation.className = row[4] ? "affiliation" : "muted";
      tr.appendChild(affiliation);
      tr.appendChild(cell(countries[row[5]]));
      tr.appendChild(cell(continents[row[6]]));
      fragment.appendChild(tr);
    });
    rowsEl.replaceChildren(fragment);
  }

  function renderPager(matchedCount) {
    var pages = Math.max(1, Math.ceil(matchedCount / state.pageSize));
    if (state.page > pages) state.page = pages;
    pagerEl.replaceChildren();
    if (matchedCount <= state.pageSize) return;

    var prev = document.createElement("button");
    prev.type = "button";
    prev.className = "btn";
    prev.textContent = "Previous";
    prev.disabled = state.page <= 1;
    prev.addEventListener("click", function () {
      state.page -= 1;
      render();
      document.getElementById("directory").scrollIntoView({ block: "start" });
    });

    var pos = document.createElement("span");
    pos.className = "pos";
    pos.textContent = "Page " + formatNumber(state.page) + " of " + formatNumber(pages);

    var next = document.createElement("button");
    next.type = "button";
    next.className = "btn";
    next.textContent = "Next";
    next.disabled = state.page >= pages;
    next.addEventListener("click", function () {
      state.page += 1;
      render();
      document.getElementById("directory").scrollIntoView({ block: "start" });
    });

    pagerEl.appendChild(prev);
    pagerEl.appendChild(pos);
    pagerEl.appendChild(next);
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
      ? "Showing " + formatNumber(start) + "–" + formatNumber(end) + " of " + formatNumber(matched.length) + " appointments"
      : "No appointments match.";
    universeRow.querySelectorAll(".chip").forEach(function (chip) {
      var count = chip.querySelector(".c");
      if (count) count.textContent = formatNumber(result.uniCounts[chip.dataset.universe] || 0);
    });
    renderTable(matched);
    renderPager(matched.length);
    writeUrl();
  }

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

  roleEl.addEventListener("change", function () {
    state.role = roleEl.value;
    state.page = 1;
    render();
  });
  journalEl.addEventListener("change", function () {
    state.journal = journalEl.value;
    state.page = 1;
    render();
  });
  institutionEl.addEventListener("change", function () {
    state.aff = institutionEl.value;
    state.page = 1;
    render();
  });
  fieldEl.addEventListener("change", function () {
    state.field = fieldEl.value;
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
    state.role = "";
    state.continent = "";
    state.country = "";
    state.journal = "";
    state.aff = "";
    state.field = "";
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
        state.dir = "asc";
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
