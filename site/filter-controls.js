/* Shared list grouping and removable filters; page controllers own URL state. */
(function () {
  "use strict";
  window.filterControls = {
    groupLists: function (container) {
      if (!container || container.dataset.grouped) return;
      container.dataset.grouped = "true";
      container.classList.add("list-families");
      var groups = new Map();
      [["ft50", "FT50 & tags"], ["abdc", "ABDC"], ["ajg", "AJG"]].forEach(function (item) {
        var fieldset = document.createElement("fieldset");
        fieldset.className = "list-family";
        var legend = document.createElement("legend");
        legend.textContent = item[1];
        fieldset.appendChild(legend);
        var choices = document.createElement("div");
        choices.className = "list-choices";
        fieldset.appendChild(choices);
        groups.set(item[0], { fieldset: fieldset, choices: choices });
      });
      container.querySelectorAll("button[data-universe]").forEach(function (button) {
        var id = button.dataset.universe;
        var key = id.indexOf("ajg") === 0 ? "ajg" : /^(a_star|a|b|c)$/.test(id) ? "abdc" : "ft50";
        groups.get(key).choices.appendChild(button);
      });
      groups.forEach(function (group) {
        if (group.choices.children.length) container.appendChild(group.fieldset);
      });
    },
    renderActive: function (container, filters, remove, focus) {
      if (!container) return;
      var signature = JSON.stringify(filters);
      if (container.dataset.signature === signature) return;
      container.dataset.signature = signature;
      container.hidden = !filters.length;
      container.replaceChildren();
      var caption = document.createElement("span");
      caption.className = "filter-caption";
      caption.textContent = "Active filters";
      container.appendChild(caption);
      filters.forEach(function (filter) {
        var button = document.createElement("button");
        button.type = "button";
        button.className = "chip filter-remove";
        var value = filter.value === "__blank__" ? "Unknown" : (filter.display || filter.value);
        button.textContent = filter.label + ": " + value + " \u00d7";
        button.setAttribute("aria-label", "Remove " + filter.label.toLowerCase() + " filter: " + value);
        button.dataset.filter = filter.key;
        button.addEventListener("click", function () {
          remove(filter);
          if (focus) focus.focus();
        });
        container.appendChild(button);
      });
    }
  };
})();
