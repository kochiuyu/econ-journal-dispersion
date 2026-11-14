/* Journal images are matched by complete title, never by publisher alone. */
(function () {
  "use strict";
  var images = {"accountingorganizationsandsociety":"aos.webp","americaneconomicreview":"aer.webp","harvardbusinessreview":"hbr.webp","journalofaccountingandeconomics":"jae.webp","journalofbusinessventuring":"jbv.webp","journaloffinancialandquantitativeanalysis":"jfqa.webp","journaloffinancialeconomics":"jfe.webp","journalofinternationalbusinessstudies":"jibs.webp","journaloftheacademyofmarketingscience":"jams.webp","organizationalbehaviorandhumandecisionprocesses":"obhdp.webp","researchpolicy":"rp.webp","reviewofaccountingstudies":"rast.webp","reviewofeconomicstudies":"restud.svg"};
  var failed = new Set();

  function key(name) {
    return String(name || "").normalize("NFKC").toLowerCase()
      .replace(/^the\s+/, "").replace(/&/g, "and")
      .replace(/[^\p{L}\p{N}]+/gu, "");
  }
  function initials(name) {
    var words = String(name || "").match(/[\p{L}\p{N}]+/gu) || [];
    words = words.filter(function (word) { return !/^(the|a|an|and|of|for|in|on|at|to)$/i.test(word); });
    return words.slice(0, 3).map(function (word) { return Array.from(word)[0]; }).join("").toUpperCase() || "J";
  }
  function prepend(cell, name) {
    if (!name || cell.querySelector(".journal-identity")) return;
    var identity = document.createElement("span");
    identity.className = "journal-identity";
    var label = document.createElement("span");
    label.className = "journal-label";
    while (cell.firstChild) label.appendChild(cell.firstChild);
    var mark = document.createElement("span");
    mark.className = "journal-mark";
    mark.setAttribute("aria-hidden", "true");
    mark.textContent = initials(name);
    var asset = images[key(name)];
    if (asset && !failed.has(asset)) {
      var img = document.createElement("img");
      img.src = "assets/journals/" + asset;
      img.alt = "";
      img.width = 24;
      img.height = 30;
      img.loading = "lazy";
      img.decoding = "async";
      img.setAttribute("fetchpriority", "low");
      img.addEventListener("error", function () { failed.add(asset); img.remove(); });
      mark.appendChild(img);
    }
    identity.append(mark, label);
    cell.appendChild(identity);
  }
  window.journalIcons = { prepend: prepend };
})();
