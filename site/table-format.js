/* Display conventions only: source values, filtering, sorting and URLs stay intact. */
(function () {
  "use strict";
  var numbers = new Intl.NumberFormat("en-US", { maximumFractionDigits: 20 });
  function isMissing(value) {
    return value === null || value === undefined || (typeof value === "string" && value.trim() === "");
  }
  function missing(container, label) {
    container.replaceChildren();
    container.classList.add("muted");
    var marker = document.createElement("span");
    marker.className = "missing-value";
    marker.title = label || "Not reported";
    var dash = document.createElement("span");
    dash.setAttribute("aria-hidden", "true");
    dash.textContent = "—";
    var description = document.createElement("span");
    description.className = "sr-only";
    description.textContent = label || "Not reported";
    marker.append(dash, description);
    container.appendChild(marker);
  }
  function text(container, value, label) {
    if (isMissing(value)) missing(container, label);
    else container.textContent = String(value);
  }
  window.tableFormat = {
    isMissing: isMissing,
    missing: missing,
    text: text,
    number: function (container, value) {
      if (isMissing(value) || !Number.isFinite(Number(value))) missing(container);
      else container.textContent = numbers.format(Number(value));
    },
    decimal: function (container, value) {
      if (isMissing(value) || (typeof value === "number" && !Number.isFinite(value))) {
        missing(container);
        return;
      }
      // Group the integer part without rounding or dropping published decimal digits.
      var source = String(value).trim();
      var parts = /^([+-]?)(\d+)(\.\d+)?$/.exec(source);
      container.textContent = parts ? parts[1] + parts[2].replace(/\B(?=(\d{3})+(?!\d))/g, ",") + (parts[3] || "") : source;
    }
  };
})();
