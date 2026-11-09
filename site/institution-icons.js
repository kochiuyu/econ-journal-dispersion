/* Display a verified institution site icon beside its existing name. */
(function () {
  "use strict";

  var icons = window.INSTITUTION_ICONS || {};

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
    icon.addEventListener("error", function () { icon.remove(); });
    icon.src = url;
    container.prepend(icon);
  }

  window.institutionIcons = { forAffiliation: forAffiliation, prepend: prepend };
})();
