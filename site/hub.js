/* Hub counts. Project Pages base: /econ-journal-dispersion/
   meta.json is a relative URL so this page works on project Pages and under
   python -m http.server -d site. Do not fetch it from the site root. */
(function () {
  "use strict";

  var PAGES_BASE = "/econ-journal-dispersion/";
  var numberFormat = new Intl.NumberFormat("en-US");

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

  function asOf(meta) {
    var year = meta.year ? "Board year " + meta.year : "Current boards";
    if (meta.collectedMin && meta.collectedMax) {
      var range = meta.collectedMin === meta.collectedMax
        ? formatDate(meta.collectedMin)
        : formatDate(meta.collectedMin) + " – " + formatDate(meta.collectedMax);
      return year + ", collected " + range + ".";
    }
    return year + ".";
  }

  function place(id, value) {
    var node = document.getElementById(id);
    if (node) node.textContent = value;
  }

  fetch("meta.json").then(function (response) {
    if (!response.ok) throw new Error(String(response.status));
    return response.json();
  }).then(function (meta) {
    if (!meta || !meta.counts) throw new Error("meta");
    if (meta.base && meta.base !== PAGES_BASE) {
      console.warn("meta.json base path does not match this page", meta.base, PAGES_BASE);
    }
    place("n-appointments", formatNumber(meta.counts.appointments));
    place("n-editors", formatNumber(meta.counts.editors));
    place("n-journals", formatNumber(meta.counts.journals));
    place("n-countries", formatNumber(meta.counts.countries));
    var text = asOf(meta);
    place("asof", text);
    place("about-asof", text);
    place("footer-asof", text);
    var byId = {};
    (meta.universes || []).forEach(function (item) { byId[item.id] = item; });
    document.querySelectorAll("[data-universe]").forEach(function (card) {
      var item = byId[card.getAttribute("data-universe")];
      if (!item) return;
      var count = card.querySelector("[data-universe-count]");
      var journals = card.querySelector("[data-universe-journals]");
      if (count) count.textContent = formatNumber(item.appointments);
      if (journals) journals.textContent = formatNumber(item.journals);
      if (item.title) card.title = item.title;
    });
  }).catch(function () {
    var status = document.getElementById("meta-status");
    if (status) {
      status.textContent = "Counts are not built yet. From the repository root, run python scripts/build_site.py.";
    }
  });
})();
