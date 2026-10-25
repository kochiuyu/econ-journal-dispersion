/* Journal list.
   Project Pages base: /econ-journal-dispersion/
   Styles, this file, and journals-data.js are loaded with relative URLs.
   Do not fetch them from the site root; that host path is the user Pages root,
   not this project site.
   Row: [journal, mask, appointments, editors, countries, fieldIndex, urlIndex] */
(function () {
  "use strict";

  var PAGES_BASE = "/econ-journal-dispersion/";
  var DATA = window.JOURNALS_DATA;
  var numberFormat = new Intl.NumberFormat("en-US");
  var collator = new Intl.Collator("en", { sensitivity: "base", numeric: true });
  var COUNT_SORTS = { appointments: true, editors: true, countries: true };

  var countEl = document.getElementById("count");
  var rowsEl = document.getElementById("rows");
  var pagerEl = document.getElementById("pager");

  if (!DATA || !DATA.rows) {
    countEl.textContent = "Journal data is not built yet. From the repository root, run python scripts/build_site.py.";
    return;
  }

  if (DATA.base && DATA.base !== PAGES_BASE) {
    console.warn("journals-data.js base path does not match this page", DATA.base, PAGES_BASE);
  }

  var rows = DATA.rows;
  var fields = DATA.fields || [""];
  var urls = DATA.urls || [""];
  var universes = DATA.universes || [];
  var total = rows.length;
  var hay = new Array(total);

  var qEl = document.getElementById("q");
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

  function fieldText(index) {
    return fields[index] || "";
  }

  function fieldLabel(field) {
    var match = /^(\d+)\s+([\s\S]+)$/.exec(field || "");
    return match ? match[2] : (field || "");
  }

  function universeText(mask) {
    var labels = [];
    for (var i = 0; i < universes.length; i++) {
      if (mask & universes[i].bit) labels.push(universes[i].label);
    }
    return labels.join(" ");
  }

  function readUrl() {
    var params = new URLSearchParams(window.location.search);
    var size = Number(params.get("n"));
    var page = Number(params.get("page"));
    var sort = params.get("sort") || "name";
    if (["name", "lists", "field", "appointments", "editors", "countries"].indexOf(sort) === -1) sort = "name";
    return {
      q: params.get("q") || "",
      universes: new Set((params.get("u") || "").split(",").filter(Boolean)),
      field: params.get("field") || "",
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
    if (state.field) params.set("field", state.field);
    if (state.sort !== "name") params.set("sort", state.sort);
    if (state.dir === "desc") params.set("dir", "desc");
    if (state.page > 1) params.set("page", String(state.page));
    if (state.pageSize !== 50) params.set("n", String(state.pageSize));
    var query = params.toString();
    var next = window.location.pathname + (query ? "?" + query : "") + window.location.hash;
    var current = window.location.pathname + window.location.search + window.location.hash;
    if (next !== current) history.replaceState(null, "", next);
  }

  function directoryUrl(name) {
    var params = new URLSearchParams();
    params.set("journal", name);
    return "index.html?" + params.toString();
  }

  function fillHay() {
    for (var i = 0; i < total; i++) {
      var field = fieldText(rows[i][5]);
      hay[i] = [rows[i][0] || "", field, fieldLabel(field)].join("\n").toLowerCase();
    }
  }

  function placeText(id, value) {
    var node = document.getElementById(id);
    if (node) node.textContent = value;
  }

  function fillHeader() {
    var counts = DATA.counts;
    placeText("n-journals", formatNumber(counts.journals));
    placeText("n-appointments", formatNumber(counts.appointments));
    placeText("n-editors", formatNumber(counts.editors));
    placeText("n-countries", formatNumber(counts.countries));
    var asOf = asOfText();
    placeText("asof", asOf);
    placeText("about-asof", asOf);
    placeText("footer-asof", asOf);
    var missing = counts.missingField || 0;
    placeText(
      "about-field",
      missing
        ? formatNumber(missing) + (missing === 1 ? " journal has" : " journals have") + " no ABDC field and stay in the table."
        : "Every journal in this table has an ABDC field."
    );
  }

  function addOption(select, value, label) {
    var option = document.createElement("option");
    option.value = value;
    option.textContent = label;
    select.appendChild(option);
  }

  function initControls() {
    var seen = [];
    var blank = false;
    for (var i = 0; i < total; i++) {
      var field = fieldText(rows[i][5]);
      if (!field) blank = true;
      else if (seen.indexOf(field) === -1) seen.push(field);
    }
    seen.sort(function (a, b) { return collator.compare(fieldLabel(a), fieldLabel(b)); });
    seen.forEach(function (field) {
      var option = document.createElement("option");
      option.value = field;
      option.textContent = fieldLabel(field);
      if (fieldLabel(field) !== field) option.title = field;
      fieldEl.appendChild(option);
    });
    if (blank) addOption(fieldEl, "__blank__", "Unknown");

    universes.forEach(function (universe) {
      var button = document.createElement("button");
      button.type = "button";
      button.className = "chip";
      button.dataset.universe = universe.id;
      button.setAttribute("aria-pressed", "false");
      if (universe.title) button.title = universe.title;
      var count = DATA.counts.byUniverse[universe.id];
      button.appendChild(document.createTextNode(universe.label + " "));
      var countNode = document.createElement("span");
      countNode.className = "c";
      countNode.textContent = formatNumber(count.journals);
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
      case "lists": return universeText(row[1]);
      case "field": return fieldLabel(fieldText(row[5]));
      case "appointments": return row[2];
      case "editors": return row[3];
      case "countries": return row[4];
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
    var field = state.field;
    var matched = [];
    var uniCounts = {};
    for (var u = 0; u < universes.length; u++) uniCounts[universes[u].id] = 0;

    for (var i = 0; i < total; i++) {
      var row = rows[i];
      if (mask && (row[1] & mask) === 0) continue;
      var fieldValue = fieldText(row[5]);
      if (field === "__blank__") {
        if (fieldValue) continue;
      } else if (field && fieldValue !== field) {
        continue;
      }
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
        if (row[1] & universes[k].bit) uniCounts[universes[k].id] += 1;
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
    fieldEl.value = state.field;
    pageSizeEl.value = String(state.pageSize);
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

  function badge(universe) {
    var node = document.createElement("span");
    node.className = "badge u-" + universe.id;
    node.textContent = universe.label;
    if (universe.title) node.title = universe.title;
    return node;
  }

  function numCell(value) {
    var td = document.createElement("td");
    td.className = "num";
    td.textContent = formatNumber(value);
    return td;
  }

  function renderTable(matched) {
    var start = (state.page - 1) * state.pageSize;
    var slice = matched.slice(start, start + state.pageSize);
    var fragment = document.createDocumentFragment();
    if (!slice.length) {
      var emptyRow = document.createElement("tr");
      var emptyCell = document.createElement("td");
      emptyCell.colSpan = 7;
      emptyCell.className = "empty";
      emptyCell.textContent = "No journals match these filters.";
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
      link.href = directoryUrl(row[0]);
      link.textContent = row[0];
      nameCell.appendChild(link);
      tr.appendChild(nameCell);

      var listCell = document.createElement("td");
      var any = false;
      universes.forEach(function (universe) {
        if (row[1] & universe.bit) {
          listCell.appendChild(badge(universe));
          any = true;
        }
      });
      if (!any) listCell.textContent = "—";
      tr.appendChild(listCell);

      var field = fieldText(row[5]);
      var fieldCell = document.createElement("td");
      fieldCell.className = field ? "field" : "muted";
      fieldCell.textContent = field ? fieldLabel(field) : "—";
      if (field && fieldLabel(field) !== field) fieldCell.title = field;
      tr.appendChild(fieldCell);

      tr.appendChild(numCell(row[2]));
      tr.appendChild(numCell(row[3]));
      tr.appendChild(numCell(row[4]));

      var board = document.createElement("td");
      var url = urls[row[6]] || "";
      if (url.indexOf("http://") === 0 || url.indexOf("https://") === 0) {
        var boardLink = document.createElement("a");
        boardLink.href = url;
        boardLink.target = "_blank";
        boardLink.rel = "noopener noreferrer";
        boardLink.textContent = "Board";
        board.appendChild(boardLink);
      } else {
        board.className = "muted";
        board.textContent = "—";
      }
      tr.appendChild(board);
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
        document.getElementById("journals").scrollIntoView({ block: "start" });
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
      ? "Showing " + formatNumber(start) + "–" + formatNumber(end) + " of " + formatNumber(matched.length) + " journals"
      : "No journals match.";
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
    state.universes = new Set();
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
