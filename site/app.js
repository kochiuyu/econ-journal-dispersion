/* Journal editor directory.
   Project Pages base: /econ-journal-dispersion/
   directory.html loads data/shell.js, then this file. List rows are data/<id>.js,
   fetched when that chip is selected or a journal/institution link needs them.
   The page opens on FT50. Do not fetch these files from the site root. */
(function () {
  "use strict";

  var PAGES_BASE = "/econ-journal-dispersion/";
  var SHELL = window.EDITOR_SHELL;
  var numberFormat = new Intl.NumberFormat("en-US");
  var collator = new Intl.Collator("en", { sensitivity: "base", numeric: true });

  var countEl = document.getElementById("count");
  var rowsEl = document.getElementById("rows");
  var pagerEl = document.getElementById("pager");
  var directoryEl = document.getElementById("directory");

  if (!SHELL || !SHELL.universes || !SHELL.counts || !SHELL.journals) {
    if (countEl) {
      countEl.textContent = "Directory data is not built yet. From the repository root, run python scripts/build_site.py.";
    }
    return;
  }

  if (SHELL.base && SHELL.base !== PAGES_BASE) {
    console.warn("shell.js base path does not match this page", SHELL.base, PAGES_BASE);
  }

  var universes = SHELL.universes;
  var families = SHELL.families;
  var rows = [];
  var roleNames = [];
  var roleFamily = [];
  var roleLookup = new Map();
  var journalNames = [];
  var journalFields = [];
  var journalLookup = new Map();
  var countries = new StringTable(true);
  var continents = new StringTable(true);
  var urls = new StringTable(true);
  var profiles = new StringTable(true);
  var seenRows = new Set();
  var hay = [];
  var orderCache = new Map();
  var rowsNameSorted = true;
  var loadedOnce = false;
  var loadedChunks = new Set();
  var inflight = new Map();
  var institutionIndex = null;
  var institutionIndexPromise = null;
  var institutionPack = null;
  var countryIndex = null;
  var appliedContinent = null;
  var generation = 0;

  var journalInfo = new Map();
  SHELL.journals.forEach(function (name, index) {
    journalInfo.set(name, {
      mask: SHELL.journalMask[index] || 0,
      cover: SHELL.journalCover[index] || 0
    });
  });

  var qEl = document.getElementById("q");
  var roleEl = document.getElementById("role");
  var continentEl = document.getElementById("continent");
  var countryEl = document.getElementById("country");
  var journalEl = document.getElementById("journal");
  var institutionEl = document.getElementById("institution");
  var suggestEl = document.getElementById("institution-list");
  var fieldEl = document.getElementById("field");
  var pageSizeEl = document.getElementById("pagesize");
  var universeRow = document.getElementById("universe-row");
  var form = document.getElementById("filters");
  var clearBtn = document.getElementById("clear");

  var state = readUrl();
  var debounce = 0;
  var suggestItems = [];
  var suggestIndex = -1;

  function StringTable(emptyFirst) {
    this.values = [];
    this.lookup = new Map();
    if (emptyFirst) {
      this.values.push("");
      this.lookup.set("", 0);
    }
  }

  StringTable.prototype.add = function (value) {
    var found = this.lookup.get(value);
    if (found !== undefined) return found;
    var index = this.values.length;
    this.values.push(value);
    this.lookup.set(value, index);
    return index;
  };

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
    var year = SHELL.year ? "Board year " + SHELL.year : "Current boards";
    if (SHELL.collectedMin && SHELL.collectedMax) {
      var range = SHELL.collectedMin === SHELL.collectedMax
        ? formatDate(SHELL.collectedMin)
        : formatDate(SHELL.collectedMin) + " – " + formatDate(SHELL.collectedMax);
      return year + ", collected " + range + ".";
    }
    return year + ".";
  }

  function universeById(id) {
    for (var i = 0; i < universes.length; i++) {
      if (universes[i].id === id) return universes[i];
    }
    return null;
  }

  function universeLabel(id) {
    var universe = universeById(id);
    return universe ? universe.label : id;
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

  function sameSet(a, b) {
    if (a.size !== b.size) return false;
    var ok = true;
    a.forEach(function (id) {
      if (!b.has(id)) ok = false;
    });
    return ok;
  }

  function syncUniverseMode() {
    var defaults = new Set(SHELL.defaultUniverses || ["ft50"]);
    if (!state.universes.size) state.universeMode = "none";
    else if (sameSet(state.universes, defaults)) state.universeMode = "default";
    else state.universeMode = "explicit";
  }

  function readUrl() {
    var params = new URLSearchParams(window.location.search);
    var size = Number(params.get("n"));
    var page = Number(params.get("page"));
    var rawU = params.get("u");
    var journal = params.get("journal") || "";
    var aff = params.get("aff") || "";
    var universesSelected;
    var universeMode;
    var noUniverse = SHELL.noUniverse || "-";
    if (rawU === null) {
      if (journal || aff) {
        universesSelected = new Set();
        universeMode = "none";
      } else {
        universesSelected = new Set(SHELL.defaultUniverses || ["ft50"]);
        universeMode = "default";
      }
    } else if (rawU === noUniverse) {
      universesSelected = new Set();
      universeMode = "none";
    } else {
      universesSelected = new Set(universeSelection(rawU));
      universeMode = universesSelected.size ? "explicit" : "none";
    }
    return {
      q: params.get("q") || "",
      universes: universesSelected,
      universeMode: universeMode,
      role: params.get("role") || "",
      continent: params.get("continent") || "",
      country: params.get("country") || "",
      journal: journal,
      aff: aff,
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
    if (state.universeMode === "none") params.set("u", SHELL.noUniverse || "-");
    else if (state.universeMode === "explicit" && state.universes.size) {
      params.set("u", Array.from(state.universes).join(","));
    }
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
    if (next !== current) history.replaceState(null, "", next);
  }

  function isCovered(id) {
    var options = (SHELL.covers && SHELL.covers[id]) || [id];
    for (var i = 0; i < options.length; i++) {
      if (loadedChunks.has(options[i])) return true;
    }
    return false;
  }

  function chunksFromMask(mask) {
    var ids = [];
    if (!mask) return ids;
    for (var i = 0; i < universes.length; i++) {
      if (mask & universes[i].bit) ids.push(universes[i].id);
    }
    return ids;
  }

  function needsInstitutionIndex() {
    return !!(state.aff && state.aff !== "__blank__" && state.universeMode === "none");
  }

  function chunksToFetch() {
    var ids = [];
    function add(id) {
      if (!id || ids.indexOf(id) !== -1 || isCovered(id)) return;
      ids.push(id);
    }
    if (state.universeMode !== "none") state.universes.forEach(add);
    if (state.journal) {
      var info = journalInfo.get(state.journal);
      if (info) chunksFromMask(info.cover).forEach(add);
    }
    if (needsInstitutionIndex() && institutionIndex) {
      chunksFromMask(institutionIndex[state.aff]).forEach(add);
    }
    return ids.filter(function (id) {
      var options = (SHELL.covers && SHELL.covers[id]) || [id];
      for (var i = 0; i < options.length; i++) {
        var other = options[i];
        if (other !== id && ids.indexOf(other) !== -1) return false;
      }
      return true;
    });
  }

  function addRole(name, family) {
    var existing = roleLookup.get(name);
    if (existing !== undefined) return existing;
    var index = roleNames.length;
    roleNames.push(name);
    roleFamily.push(family);
    roleLookup.set(name, index);
    return index;
  }

  function addJournal(name, field) {
    var existing = journalLookup.get(name);
    if (existing !== undefined) {
      if (!journalFields[existing] && field) journalFields[existing] = field;
      return existing;
    }
    var index = journalNames.length;
    journalNames.push(name);
    journalFields.push(field || "");
    journalLookup.set(name, index);
    return index;
  }

  function rowKey(mapped) {
    return mapped.join("\u0001");
  }

  function ingest(chunk) {
    var mapRole = [];
    var mapJournal = [];
    var mapCountry = [];
    var mapContinent = [];
    var mapUrl = [];
    var mapProfile = [];
    var i;
    for (i = 0; i < chunk.roles.length; i++) mapRole[i] = addRole(chunk.roles[i], chunk.roleFamily[i]);
    for (i = 0; i < chunk.journals.length; i++) {
      var field = chunk.fields[chunk.journalField[i]] || "";
      mapJournal[i] = addJournal(chunk.journals[i], field);
    }
    for (i = 0; i < chunk.countries.length; i++) mapCountry[i] = countries.add(chunk.countries[i]);
    for (i = 0; i < chunk.continents.length; i++) mapContinent[i] = continents.add(chunk.continents[i]);
    for (i = 0; i < chunk.urls.length; i++) mapUrl[i] = urls.add(chunk.urls[i]);
    for (i = 0; i < chunk.profiles.length; i++) mapProfile[i] = profiles.add(chunk.profiles[i]);
    var added = 0;
    for (i = 0; i < chunk.rows.length; i++) {
      var row = chunk.rows[i];
      var mapped = [
        row[0],
        mapRole[row[1]],
        mapJournal[row[2]],
        row[3],
        row[4],
        mapCountry[row[5]],
        mapContinent[row[6]],
        mapUrl[row[7]],
        mapProfile[row[8]]
      ];
      var key = rowKey(mapped);
      if (seenRows.has(key)) continue;
      seenRows.add(key);
      rows.push(mapped);
      added += 1;
    }
    if (added && rows.length !== added) rowsNameSorted = false;
    loadedOnce = true;
    countryIndex = null;
    institutionPack = null;
    orderCache.clear();
  }

  function loadChunk(id) {
    if (!/^[a-z0-9_]+$/.test(id)) return Promise.reject(new Error(id));
    if (loadedChunks.has(id)) return Promise.resolve();
    if (inflight.has(id)) return inflight.get(id);
    var promise = new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = "data/" + id + ".js";
      script.onload = function () {
        var chunk = window.EDITOR_CHUNKS && window.EDITOR_CHUNKS[id];
        if (!chunk || !chunk.rows) {
          inflight.delete(id);
          reject(new Error(universeLabel(id)));
          return;
        }
        ingest(chunk);
        loadedChunks.add(id);
        inflight.delete(id);
        resolve();
      };
      script.onerror = function () {
        inflight.delete(id);
        reject(new Error(universeLabel(id)));
      };
      document.head.appendChild(script);
    });
    inflight.set(id, promise);
    return promise;
  }

  function ensureInstitutionIndex() {
    if (institutionIndex) return Promise.resolve(institutionIndex);
    if (institutionIndexPromise) return institutionIndexPromise;
    institutionIndexPromise = new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = "data/institution-index.js";
      script.onload = function () {
        institutionIndex = window.EDITOR_INSTITUTION_INDEX || {};
        resolve(institutionIndex);
      };
      script.onerror = function () {
        institutionIndexPromise = null;
        reject(new Error("institution index"));
      };
      document.head.appendChild(script);
    });
    return institutionIndexPromise;
  }

  function markBusy(ids) {
    var pending = {};
    ids.forEach(function (id) { pending[id] = true; });
    universeRow.querySelectorAll(".chip").forEach(function (chip) {
      if (pending[chip.dataset.universe]) chip.setAttribute("aria-busy", "true");
      else chip.removeAttribute("aria-busy");
    });
    var busy = ids.length ? "true" : "false";
    if (directoryEl) directoryEl.setAttribute("aria-busy", busy);
    countEl.setAttribute("aria-busy", busy);
  }

  function showPending(text) {
    countEl.textContent = text;
    if (rows.length) return;
    var tr = document.createElement("tr");
    var td = document.createElement("td");
    td.colSpan = 8;
    td.className = "empty";
    td.textContent = text;
    tr.appendChild(td);
    rowsEl.replaceChildren(tr);
    pagerEl.replaceChildren();
  }

  function schedule() {
    var gen = ++generation;
    syncControls();
    writeUrl();
    var chain = needsInstitutionIndex() && !institutionIndex ? ensureInstitutionIndex() : Promise.resolve();
    if (needsInstitutionIndex() && !institutionIndex) showPending("Loading institutions…");
    chain.then(function () {
      if (gen !== generation) return null;
      var ids = chunksToFetch();
      if (!ids.length) {
        markBusy([]);
        render();
        return null;
      }
      markBusy(ids);
      showPending("Loading " + ids.map(universeLabel).join(", ") + "…");
      return Promise.allSettled(ids.map(loadChunk)).then(function (results) {
        var failed = [];
        results.forEach(function (result) {
          if (result.status === "rejected") {
            failed.push(result.reason && result.reason.message ? result.reason.message : "a list");
          }
        });
        return failed;
      });
    }).then(function (failed) {
      if (gen !== generation || failed === null) return;
      markBusy([]);
      render();
      if (failed.length) {
        countEl.textContent = "Could not load " + failed.join(", ") + ". Showing appointments already loaded.";
      }
    }).catch(function (error) {
      if (gen !== generation) return;
      markBusy([]);
      render();
      countEl.textContent = "Could not load " + (error && error.message ? error.message : "directory data") + ". From the repository root, run python scripts/build_site.py.";
    });
  }

  function haystack(index) {
    var cached = hay[index];
    if (cached) return cached;
    var row = rows[index];
    cached = [
      row[0],
      roleNames[row[1]],
      families[roleFamily[row[1]]],
      journalNames[row[2]],
      fieldText(journalFields[row[2]]),
      fieldLabel(fieldText(journalFields[row[2]])),
      row[4],
      countries.values[row[5]],
      continents.values[row[6]]
    ].join("\n").toLowerCase();
    hay[index] = cached;
    return cached;
  }

  function fieldText(value) {
    return value || "";
  }

  function fieldLabel(field) {
    var match = /^(\d+)\s+([\s\S]+)$/.exec(field || "");
    return match ? match[2] : (field || "");
  }

  function fieldOf(row) {
    return fieldText(journalFields[row[2]]);
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
      case "role": return roleNames[row[1]] || "";
      case "journal": return journalNames[row[2]] || "";
      case "field": return fieldLabel(fieldOf(row));
      case "universe": return universeText(row[3]);
      case "affiliation": return row[4] || "";
      case "country": return countries.values[row[5]] || "";
      case "continent": return continents.values[row[6]] || "";
      default: return nameSortKey(row[0]);
    }
  }

  function getOrder() {
    var key = state.sort + ":" + state.dir + ":" + rows.length + ":" + (rowsNameSorted ? "1" : "0");
    var cached = orderCache.get(key);
    if (cached) return cached;
    var order = new Array(rows.length);
    for (var i = 0; i < rows.length; i++) order[i] = i;
    if (!(rowsNameSorted && state.sort === "name" && state.dir === "asc")) {
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
      var universe = universeById(id);
      if (universe) mask |= universe.bit;
    });
    return mask;
  }

  function journalMatchesSelection(name) {
    if (!state.universes.size) return true;
    var info = journalInfo.get(name);
    if (!info || !info.mask) return true;
    return (info.mask & selectedMask()) !== 0;
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
      if (journal && journalNames[row[2]] !== journal) continue;
      if (!matchesChoice(row[4] || "", aff)) continue;
      if (!matchesChoice(fieldOf(row), field)) continue;
      if (!matchesChoice(continents.values[row[6]] || "", continent)) continue;
      if (!matchesChoice(countries.values[row[5]] || "", country)) continue;
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
    var counts = SHELL.counts;
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

  function buildCountryIndex() {
    if (countryIndex && countryIndex.rows === rows.length) return;
    var all = new Set();
    var byContinent = new Map();
    var blankAll = false;
    var blankByContinent = new Set();
    for (var i = 0; i < rows.length; i++) {
      var country = countries.values[rows[i][5]] || "";
      var continent = continents.values[rows[i][6]] || "";
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
      rows: rows.length,
      all: sorted(all),
      lists: lists,
      blankAll: blankAll,
      blankByContinent: blankByContinent
    };
  }

  function countriesForContinent(continent) {
    buildCountryIndex();
    if (!continent) return { list: countryIndex.all, blank: countryIndex.blankAll };
    var key = continent === "__blank__" ? "__blank__" : continent;
    return {
      list: countryIndex.lists.get(key) || [],
      blank: countryIndex.blankByContinent.has(key)
    };
  }

  function keepExtra(select, previous) {
    if (!previous) return;
    addOption(select, previous, previous === "__blank__" ? "Unknown" : previous);
  }

  function refillContinents() {
    var names = [];
    var seen = new Set();
    var blank = false;
    for (var i = 0; i < rows.length; i++) {
      var name = continents.values[rows[i][6]] || "";
      if (!name) {
        blank = true;
        continue;
      }
      if (seen.has(name)) continue;
      seen.add(name);
      names.push(name);
    }
    names.sort(function (a, b) { return collator.compare(a, b); });
    var signature = rows.length + "\n" + names.join("\n") + "\n" + (blank ? "1" : "0");
    if (continentEl.dataset.signature !== signature) {
      continentEl.dataset.signature = signature;
      var previous = state.continent;
      continentEl.replaceChildren();
      addOption(continentEl, "", "All continents");
      names.forEach(function (item) { addOption(continentEl, item, item); });
      if (blank) addOption(continentEl, "__blank__", "Unknown");
      var present = !previous || names.indexOf(previous) !== -1 || (previous === "__blank__" && blank);
      if (!present) keepExtra(continentEl, previous);
    }
    continentEl.value = state.continent;
  }

  function refillCountries() {
    var previous = state.country;
    var found = countriesForContinent(state.continent);
    var signature = rows.length + "\n" + state.continent + "\n" + found.list.join("\n") + "\n" + (found.blank ? "1" : "0");
    if (countryEl.dataset.signature !== signature) {
      countryEl.dataset.signature = signature;
      countryEl.replaceChildren();
      addOption(countryEl, "", "All countries");
      for (var i = 0; i < found.list.length; i++) addOption(countryEl, found.list[i], found.list[i]);
      if (found.blank) addOption(countryEl, "__blank__", "Unknown");
      var stillThere = !previous || found.list.indexOf(previous) !== -1 || (previous === "__blank__" && found.blank);
      var continentChanged = appliedContinent !== null && appliedContinent !== state.continent;
      if (!stillThere) {
        if (continentChanged && loadedOnce) {
          state.country = "";
          state.page = 1;
        } else {
          keepExtra(countryEl, previous);
        }
      }
    }
    appliedContinent = state.continent;
    countryEl.value = state.country;
  }

  function refillFields() {
    var names = [];
    var seen = new Set();
    var blank = false;
    for (var i = 0; i < journalFields.length; i++) {
      var name = journalFields[i] || "";
      if (!name) {
        blank = true;
        continue;
      }
      if (seen.has(name)) continue;
      seen.add(name);
      names.push(name);
    }
    names.sort(function (a, b) { return collator.compare(fieldLabel(a), fieldLabel(b)); });
    var signature = rows.length + "\n" + names.join("\n") + "\n" + (blank ? "1" : "0");
    if (fieldEl.dataset.signature !== signature) {
      fieldEl.dataset.signature = signature;
      var previous = state.field;
      fieldEl.replaceChildren();
      addOption(fieldEl, "", "All fields");
      names.forEach(function (item) {
        var option = document.createElement("option");
        option.value = item;
        option.textContent = fieldLabel(item);
        if (fieldLabel(item) !== item) option.title = item;
        fieldEl.appendChild(option);
      });
      if (blank) addOption(fieldEl, "__blank__", "Unknown");
      var present = !previous || seen.has(previous) || (previous === "__blank__" && blank);
      if (!present) {
        if (previous === "__blank__") addOption(fieldEl, "__blank__", "Unknown");
        else {
          var extra = document.createElement("option");
          extra.value = previous;
          extra.textContent = fieldLabel(previous);
          fieldEl.appendChild(extra);
        }
      }
    }
    fieldEl.value = state.field;
  }

  function institutionChoices() {
    if (institutionPack && institutionPack.rows === rows.length) return institutionPack;
    var seen = new Set();
    var names = [];
    var blank = false;
    for (var i = 0; i < rows.length; i++) {
      var name = rows[i][4] || "";
      if (!name) {
        blank = true;
        continue;
      }
      if (seen.has(name)) continue;
      seen.add(name);
      names.push(name);
    }
    names.sort(function (a, b) { return collator.compare(a, b); });
    institutionPack = { rows: rows.length, names: names, blank: blank };
    return institutionPack;
  }

  function closeSuggest() {
    suggestItems = [];
    suggestIndex = -1;
    suggestEl.replaceChildren();
    suggestEl.hidden = true;
    institutionEl.setAttribute("aria-expanded", "false");
    institutionEl.removeAttribute("aria-activedescendant");
  }

  function paintSuggest() {
    suggestEl.replaceChildren();
    if (!suggestItems.length) {
      var empty = document.createElement("li");
      empty.className = "empty";
      empty.textContent = "No loaded institutions match.";
      suggestEl.appendChild(empty);
    }
    suggestItems.forEach(function (item, index) {
      var li = document.createElement("li");
      li.role = "presentation";
      var button = document.createElement("button");
      button.type = "button";
      button.id = "institution-opt-" + index;
      button.setAttribute("role", "option");
      button.setAttribute("aria-selected", index === suggestIndex ? "true" : "false");
      button.textContent = item.label;
      button.addEventListener("mousedown", function (event) {
        event.preventDefault();
        chooseSuggest(index);
      });
      li.appendChild(button);
      suggestEl.appendChild(li);
    });
    suggestEl.hidden = false;
    institutionEl.setAttribute("aria-expanded", "true");
    if (suggestIndex >= 0) institutionEl.setAttribute("aria-activedescendant", "institution-opt-" + suggestIndex);
    else institutionEl.removeAttribute("aria-activedescendant");
  }

  function openSuggest(query) {
    var pack = institutionChoices();
    var q = query.trim().toLowerCase();
    suggestItems = [];
    if (!q) {
      closeSuggest();
      return;
    }
    if (pack.blank && "unknown".indexOf(q) !== -1) {
      suggestItems.push({ value: "__blank__", label: "Unknown" });
    }
    for (var i = 0; i < pack.names.length && suggestItems.length < 12; i++) {
      if (pack.names[i].toLowerCase().indexOf(q) !== -1) {
        suggestItems.push({ value: pack.names[i], label: pack.names[i] });
      }
    }
    suggestIndex = suggestItems.length ? 0 : -1;
    paintSuggest();
  }

  function moveSuggest(delta) {
    if (suggestEl.hidden || !suggestItems.length) {
      openSuggest(institutionEl.value);
      return;
    }
    suggestIndex = (suggestIndex + delta + suggestItems.length) % suggestItems.length;
    paintSuggest();
  }

  function chooseSuggest(index) {
    var item = suggestItems[index];
    if (!item) return;
    state.aff = item.value;
    state.page = 1;
    institutionEl.value = item.label;
    closeSuggest();
    schedule();
  }

  function displayedAffiliation() {
    if (state.aff === "__blank__") return "Unknown";
    return state.aff || "";
  }

  function applyInstitutionText() {
    var text = institutionEl.value.trim();
    if (!text) {
      state.aff = "";
      return;
    }
    if (text.toLowerCase() === "unknown") {
      state.aff = "__blank__";
      return;
    }
    var pack = institutionChoices();
    for (var i = 0; i < pack.names.length; i++) {
      if (pack.names[i] === text) {
        state.aff = pack.names[i];
        return;
      }
    }
    if (state.aff && text === displayedAffiliation()) return;
    institutionEl.value = displayedAffiliation();
  }

  function globalAppointments(id) {
    var counts = SHELL.counts.byUniverse && SHELL.counts.byUniverse[id];
    return counts ? counts.appointments : 0;
  }

  function initControls() {
    families.forEach(function (family) { addOption(roleEl, family, family); });
    var journalOptions = SHELL.journals.slice().sort(function (a, b) { return collator.compare(a, b); });
    journalOptions.forEach(function (name) { addOption(journalEl, name, name); });
    if (state.journal && journalOptions.indexOf(state.journal) === -1) {
      addOption(journalEl, state.journal, state.journal);
    }
    universes.forEach(function (universe) {
      var button = document.createElement("button");
      button.type = "button";
      button.className = "chip";
      button.dataset.universe = universe.id;
      button.dataset.loaded = "false";
      button.setAttribute("aria-pressed", state.universes.has(universe.id) ? "true" : "false");
      if (universe.title) button.title = universe.title;
      button.appendChild(document.createTextNode(universe.label + " "));
      var countNode = document.createElement("span");
      countNode.className = "c";
      countNode.textContent = formatNumber(globalAppointments(universe.id));
      button.appendChild(countNode);
      button.addEventListener("click", function () {
        if (state.universes.has(universe.id)) state.universes.delete(universe.id);
        else state.universes.add(universe.id);
        syncUniverseMode();
        state.page = 1;
        schedule();
      });
      universeRow.appendChild(button);
    });
  }

  function syncControls() {
    if (document.activeElement !== qEl) qEl.value = state.q;
    roleEl.value = state.role;
    journalEl.value = state.journal;
    if (document.activeElement !== institutionEl) institutionEl.value = displayedAffiliation();
    pageSizeEl.value = String(state.pageSize);
    refillContinents();
    refillCountries();
    refillFields();
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

  function emptyMessage() {
    if (!rows.length && state.universeMode === "none" && !state.journal && !state.aff) {
      return "Select a list to load appointments.";
    }
    return "No editors match these filters.";
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
      td.textContent = emptyMessage();
      tr.appendChild(td);
      fragment.appendChild(tr);
    }
    slice.forEach(function (index) {
      var row = rows[index];
      var tr = document.createElement("tr");
      var profileUrl = row.length > 8 ? (profiles.values[row[8]] || "") : "";
      tr.appendChild(nameCell(row[0], profileUrl));
      tr.appendChild(cell(roleNames[row[1]]));

      var journalCell = document.createElement("td");
      journalCell.className = "journal";
      var url = urls.values[row[7]] || "";
      var journalName = journalNames[row[2]] || "—";
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
      tr.appendChild(cell(countries.values[row[5]]));
      tr.appendChild(cell(continents.values[row[6]]));
      fragment.appendChild(tr);
    });
    rowsEl.replaceChildren(fragment);
  }

  function renderPager(matchedCount) {
    var pages = Math.max(1, Math.ceil(matchedCount / state.pageSize));
    if (state.page > pages) state.page = pages;
    pagerEl.replaceChildren();
    if (matchedCount <= state.pageSize) return;

    function go(delta) {
      state.page += delta;
      render();
      directoryEl.scrollIntoView({ block: "start" });
    }

    var prev = document.createElement("button");
    prev.type = "button";
    prev.className = "btn";
    prev.textContent = "Previous";
    prev.disabled = state.page <= 1;
    prev.addEventListener("click", function () { go(-1); });

    var pos = document.createElement("span");
    pos.className = "pos";
    pos.textContent = "Page " + formatNumber(state.page) + " of " + formatNumber(pages);

    var next = document.createElement("button");
    next.type = "button";
    next.className = "btn";
    next.textContent = "Next";
    next.disabled = state.page >= pages;
    next.addEventListener("click", function () { go(1); });

    pagerEl.appendChild(prev);
    pagerEl.appendChild(pos);
    pagerEl.appendChild(next);
  }

  function loadedScopeNote() {
    if (state.universeMode !== "none" || state.journal || state.aff) return "";
    for (var i = 0; i < universes.length; i++) {
      if (!isCovered(universes[i].id)) return " Loaded lists only.";
    }
    return "";
  }

  function render() {
    var suggestOpen = !suggestEl.hidden;
    syncControls();
    var result = applyFilters();
    var matched = result.matched;
    var pages = Math.max(1, Math.ceil(matched.length / state.pageSize) || 1);
    if (state.page > pages) state.page = pages;
    var start = matched.length ? (state.page - 1) * state.pageSize + 1 : 0;
    var end = Math.min(state.page * state.pageSize, matched.length);
    if (!matched.length) {
      countEl.textContent = rows.length ? "No appointments match." : emptyMessage();
    } else {
      countEl.textContent = "Showing " + formatNumber(start) + "–" + formatNumber(end) + " of " + formatNumber(matched.length) + " appointments" + loadedScopeNote();
    }
    universeRow.querySelectorAll(".chip").forEach(function (chip) {
      var id = chip.dataset.universe;
      var count = chip.querySelector(".c");
      var ready = isCovered(id);
      chip.dataset.loaded = ready ? "true" : "false";
      if (count) {
        count.textContent = formatNumber(ready ? (result.uniCounts[id] || 0) : globalAppointments(id));
      }
    });
    renderTable(matched);
    renderPager(matched.length);
    writeUrl();
    if (suggestOpen && document.activeElement === institutionEl) openSuggest(institutionEl.value);
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
    var before = state.aff;
    applyInstitutionText();
    closeSuggest();
    state.page = 1;
    if (state.aff !== before || needsInstitutionIndex()) schedule();
    else render();
  });

  roleEl.addEventListener("change", function () {
    state.role = roleEl.value;
    state.page = 1;
    render();
  });
  journalEl.addEventListener("change", function () {
    state.journal = journalEl.value;
    state.page = 1;
    if (state.journal && !journalMatchesSelection(state.journal)) {
      state.universes = new Set();
      state.universeMode = "none";
    }
    schedule();
  });
  institutionEl.addEventListener("input", function () {
    openSuggest(institutionEl.value);
  });
  institutionEl.addEventListener("keydown", function (event) {
    if (event.key === "ArrowDown") {
      event.preventDefault();
      moveSuggest(1);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      moveSuggest(-1);
    } else if (event.key === "Escape") {
      closeSuggest();
      institutionEl.value = displayedAffiliation();
    } else if (event.key === "Enter" && !suggestEl.hidden && suggestIndex >= 0) {
      event.preventDefault();
      chooseSuggest(suggestIndex);
    }
  });
  institutionEl.addEventListener("blur", function () {
    window.setTimeout(function () {
      if (document.activeElement === institutionEl) return;
      var before = state.aff;
      applyInstitutionText();
      closeSuggest();
      if (state.aff !== before) {
        state.page = 1;
        schedule();
      }
    }, 150);
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
    state.universes = new Set(SHELL.defaultUniverses || ["ft50"]);
    state.universeMode = "default";
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
    closeSuggest();
    schedule();
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
    appliedContinent = null;
    closeSuggest();
    schedule();
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "/" && document.activeElement !== qEl && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "SELECT" && document.activeElement.tagName !== "TEXTAREA") {
      event.preventDefault();
      qEl.focus();
    }
  });

  schedule();
})();
