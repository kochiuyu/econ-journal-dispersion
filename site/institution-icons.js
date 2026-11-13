/* Display a verified institution site icon beside its existing name. */
(function () {
  "use strict";

  var icons = window.INSTITUTION_ICONS || {};
  var failed = new Set();

  function forAffiliation(name, country) {
    if (Object.prototype.hasOwnProperty.call(icons, name)) return icons[name][country || ""];
    return "";
  }

  function prepend(container, url) {
    if (!url) return;

    var icon = document.createElement("img");
    icon.className = "institution-icon";
    icon.alt = "";
    icon.width = 18;
    icon.height = 18;
    icon.loading = "lazy";
    icon.decoding = "async";
    icon.fetchPriority = "low";
    icon.addEventListener("error", function () {
      failed.add(url);
      icon.style.visibility = "hidden";
    });
    // Keep the reserved 18px box after failures so adjacent text never jumps.
    if (failed.has(url)) icon.style.visibility = "hidden";
    else icon.src = url;
    container.prepend(icon);
  }

  window.institutionIcons = { forAffiliation: forAffiliation, prepend: prepend };
})();
