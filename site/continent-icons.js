/* Simplified continent silhouettes at a common icon size. */
(function () {
  "use strict";

  var svgNS = "http://www.w3.org/2000/svg";
  var silhouettes = new Map([
    ["Africa", "M3 6 7 3 14 3 16 6 19 9 22 9 19 13 17 15 16 20 13 23 11 21 10 16 8 13 4 13 2 10Z M20 17 22 15 21 20 19 22Z"],
    ["Antarctica", "M1 14 4 12 7 13 8 10 6 7 7 5 10 10 13 11 15 8 19 7 22 9 24 13 22 16 18 17 16 20 12 19 9 20 5 18 2 18Z"],
    ["Asia", "M2 7 4 4 8 4 11 2 16 3 19 2 23 4 23 7 20 8 19 11 17 12 18 15 16 18 14 15 13 11 11 13 10 18 8 16 7 12 5 13 3 11 1 11Z M17 19 20 19 23 21 20 22 17 21Z M21 11 22 9 23 10 22 13 20 14Z"],
    ["Europe", "M2 16 6 14 6 11 10 10 11 8 11 5 14 2 16 3 15 7 13 9 15 11 17 8 21 7 23 10 21 14 17 14 16 17 13 15 11 15 14 20 12 21 9 17 7 17 6 20 2 20Z M3 9 5 8 6 11 4 13 2 12Z"],
    ["North America", "M1 5 5 3 8 4 10 2 15 2 18 4 16 6 18 8 16 11 12 13 10 16 11 18 14 20 12 21 9 19 7 16 6 13 4 11 5 8 1 8Z M19 2 23 2 24 4 22 7 19 7 20 5Z"],
    ["South America", "M6 2 10 1 13 4 17 5 21 8 19 12 16 14 15 18 12 21 11 24 9 22 9 18 8 15 8 12 5 9 4 5Z"],
    ["Oceania", "M2 12 6 9 8 6 11 6 12 10 14 9 17 14 16 18 13 20 10 17 7 17 4 19 2 17Z M13 4 16 4 19 7 16 8 14 6Z M20 18 22 15 24 16 22 20 19 23 18 22Z"]
  ]);

  window.updateContinentIcon = function (container, continent) {
    if (!container) return;
    var name = continent === "Australia" || continent === "Australasia" ? "Oceania" : continent;
    var existing = container.querySelector(".continent-icon");
    if (existing && existing.dataset.continent === name) return;
    if (existing) existing.remove();
    var silhouette = silhouettes.get(name);
    if (!silhouette) return;

    var icon = document.createElementNS(svgNS, "svg");
    icon.setAttribute("class", "continent-icon");
    icon.setAttribute("viewBox", "0 0 24 24");
    icon.setAttribute("width", "16");
    icon.setAttribute("height", "16");
    icon.setAttribute("aria-hidden", "true");
    icon.setAttribute("focusable", "false");
    icon.dataset.continent = name;
    var path = document.createElementNS(svgNS, "path");
    path.setAttribute("d", silhouette);
    path.setAttribute("fill", "currentColor");
    icon.appendChild(path);
    container.prepend(icon);
  };
})();
