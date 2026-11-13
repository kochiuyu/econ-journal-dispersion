/* Keep the result controls compact on phones without changing filter state. */
(function () {
  "use strict";
  var form = document.getElementById("filters");
  if (!form) return;
  var small = window.matchMedia("(max-width: 640px)");
  var groups = [];

  function disclosure(title, className) {
    var details = document.createElement("details");
    details.className = className;
    details.open = true;
    var summary = document.createElement("summary");
    summary.textContent = title;
    details.appendChild(summary);
    groups.push(details);
    return details;
  }
  function note(summary) {
    var span = document.createElement("span");
    span.className = "compact-selection";
    summary.append(" ", span);
    return span;
  }

  var lists = document.getElementById("universe-row");
  var listNote;
  if (lists) {
    var listGroup = disclosure("Journal lists", "compact-filter compact-lists");
    lists.before(listGroup);
    listGroup.appendChild(lists);
    listNote = note(listGroup.firstElementChild);
  }

  var existing = form.querySelector(".directory-more");
  var extraGroup, extraNote;
  if (existing) {
    // Preserve the Directory's existing disclosure and its desktop behavior.
    existing.classList.add("compact-directory-more");
    extraGroup = existing;
    extraNote = note(existing.querySelector("summary"));
  } else {
    var ids = document.getElementById("system") ? ["rating", "field"] : lists && document.getElementById("continent") ? ["continent", "country"] : ["field"];
    var first = document.getElementById(ids[0]);
    var row = first.closest(".row");
    extraGroup = disclosure("More filters", "compact-filter compact-extra");
    extraNote = note(extraGroup.firstElementChild);
    if (document.getElementById("system")) {
      // Ranking and Edition stay in the same row on desktop and remain visible on phones.
      row.appendChild(extraGroup);
      extraGroup.classList.add("compact-inline");
      var fields = document.createElement("div");
      fields.className = "row compact-extra-fields";
      ids.forEach(function (id) {
        fields.append(form.querySelector('label[for="' + id + '"]'), document.getElementById(id));
      });
      extraGroup.appendChild(fields);
    } else {
      row.before(extraGroup);
      extraGroup.appendChild(row);
    }
  }

  var hint = form.parentElement.querySelector(":scope > .hint");
  if (hint) (lists ? listGroup : extraGroup).appendChild(hint);

  function pairControl(label, className) {
    var input = document.getElementById(label.htmlFor);
    var control = input.closest(".combo") || input;
    var pair = document.createElement("div");
    pair.className = className;
    label.before(pair);
    pair.append(label, control);
  }
  extraGroup.querySelectorAll(".row > label[for]").forEach(function (label) {
    pairControl(label, "compact-field-control");
  });
  if (document.getElementById("system")) {
    ["system", "year"].forEach(function (id) {
      pairControl(form.querySelector('label[for="' + id + '"]'), "compact-scope-control");
    });
  }

  var stats = document.getElementById("stats");
  if (stats) {
    var title = document.getElementById("system") ? "Coverage · selected edition" : "Coverage · all lists";
    var coverage = disclosure(title, "compact-coverage");
    stats.before(coverage);
    coverage.appendChild(stats);
  }

  function updateNotes() {
    if (lists) {
      var selected = Array.from(lists.querySelectorAll('[aria-pressed="true"]'));
      var label = selected.length === 0 ? "All lists" : selected.length === 1 ? selected[0].firstChild.textContent.trim() : selected.length + " selected";
      if (listNote.textContent !== label) listNote.textContent = label;
    }
    var active = Array.from(extraGroup.querySelectorAll("input, select")).filter(function (input) { return input.value !== ""; }).length;
    var text = active ? active + " active" : "";
    if (extraNote.textContent !== text) extraNote.textContent = text;
  }
  function layout() {
    groups.forEach(function (group) {
      // Never hide a control that currently has keyboard focus during a resize.
      group.open = !small.matches || group.contains(document.activeElement);
    });
  }
  form.addEventListener("change", updateNotes);
  form.addEventListener("input", updateNotes);
  // Controllers also change controls when chips are removed, URLs restore, or lists load.
  var observer = new MutationObserver(updateNotes);
  observer.observe(form, { subtree: true, childList: true, attributes: true, attributeFilter: ["aria-pressed", "selected"] });
  form.parentElement.addEventListener("click", function () { window.queueMicrotask(updateNotes); });
  window.addEventListener("popstate", function () { window.queueMicrotask(updateNotes); });
  small.addEventListener("change", layout);
  layout();
  updateNotes();
})();
