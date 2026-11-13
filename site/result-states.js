/* Visitor-facing loading, empty, and recovery states shared by result pages. */
(function () {
  "use strict";
  var count = document.getElementById("count");
  var table = document.querySelector(".tbl-wrap");
  if (!count || !table) return;
  var stage = table.closest(".results-stage");
  var page = document.getElementById("system") ? "rankings" : document.getElementById("institution") ? "directory" : document.getElementById("continent") ? "institutions" : "journals";
  var entity = page === "directory" ? "editors" : page === "institutions" ? "institutions" : "journals";
  var form = document.getElementById("filters");
  var panel = document.createElement("section");
  panel.id = "result-state";
  panel.className = "result-state";
  panel.setAttribute("aria-labelledby", "result-state-title");
  var title = document.createElement("h2");
  title.id = "result-state-title";
  var description = document.createElement("p");
  description.id = "result-state-description";
  var actions = document.createElement("div");
  actions.className = "result-state-actions";
  panel.append(title, description, actions);
  (document.querySelector(".directory-mobile-sort") || table).before(panel);

  function show(kind, heading, message, showTable) {
    if (stage) stage.dataset.resultsState = kind;
    panel.hidden = false;
    panel.dataset.kind = kind;
    title.textContent = heading;
    description.textContent = message;
    actions.replaceChildren();
    table.hidden = !showTable;
    var loading = kind === "loading";
    table.setAttribute("aria-busy", String(loading));
    if (form) form.setAttribute("aria-busy", String(loading));
    document.querySelectorAll(".directory-mobile-sort, .results-mobile-sort").forEach(function (bar) { bar.hidden = loading; });
  }
  function action(label, run) {
    var button = document.createElement("button");
    button.type = "button";
    button.className = "btn";
    button.textContent = label;
    button.addEventListener("click", run);
    actions.appendChild(button);
  }
  function changeScope() {
    var lists = document.getElementById("universe-row");
    var disclosure = lists && lists.closest("details");
    if (disclosure) disclosure.open = true;
    var target = lists ? lists.querySelector("button") : document.getElementById("system");
    if (target) {
      target.focus({ preventScroll: true });
      target.scrollIntoView({ block: "center" });
    }
  }

  window.resultStates = {
    ready: function () {
      if (stage) stage.dataset.resultsState = "ready";
      panel.hidden = true;
      panel.dataset.kind = "ready";
      table.hidden = false;
      table.setAttribute("aria-busy", "false");
      if (form) form.setAttribute("aria-busy", "false");
      document.querySelectorAll(".directory-mobile-sort, .results-mobile-sort").forEach(function (bar) { bar.hidden = false; });
    },
    loading: function (text, message) {
      count.textContent = text;
      show("loading", text.replace(/…$/, ""), message || "Fetching editorial-board records. Your search and selected lists will be kept.", false);
      var pager = document.getElementById("pager");
      if (pager) pager.hidden = true;
    },
    empty: function (chooseLists) {
      var message = page === "rankings"
        ? "Try a different search, rating, or field. Clear filters keeps your selected ranking and edition."
        : "Try a different search or remove a filter. Clear filters keeps your selected journal lists.";
      show("empty", chooseLists ? "Choose a journal list" : "No " + entity + " found", chooseLists ? "Open Journal lists and choose a list to load its editorial boards." : message, false);
      if (!chooseLists) action("Clear filters", function () { document.getElementById("clear").click(); });
      action(page === "rankings" ? "Change ranking or edition" : "Choose journal lists", changeScope);
    },
    error: function (options) {
      options = options || {};
      var partial = !!options.partial;
      show("error", partial ? "Some lists couldn’t load" : "Couldn’t load " + entity,
        options.message || "Check your connection and try again. Your filters and shared link will be kept.", partial);
      count.textContent = partial ? count.textContent + " Results may be incomplete." : "Could not load " + entity + ".";
      if (!partial) document.getElementById("pager").hidden = true;
      action("Try again", function () {
        count.focus({ preventScroll: true });
        (options.retry || function () { window.location.reload(); })();
      });
      if (options.fatal) {
        document.querySelectorAll("#stats .n").forEach(function (number) { number.textContent = "—"; });
        form.querySelectorAll("input, select, button").forEach(function (input) { input.disabled = true; });
        var copy = document.getElementById("copy-link");
        if (copy) copy.disabled = true;
      } else if (!partial) {
        action(page === "rankings" ? "Change ranking or edition" : "Choose journal lists", changeScope);
      }
    }
  };

  // A missing data bundle or controller must not leave a permanent loading message.
  window.addEventListener("error", function (event) {
    var script = event.target;
    if (!script || script.tagName !== "SCRIPT") return;
    var path = new URL(script.src, window.location.href).pathname;
    if (/(?:data\/shell|journals-data|institutions-data|rankings-data|app|journals|institutions|rankings)\.js$/.test(path)) {
      window.resultStates.error({ fatal: true });
    }
  }, true);
  // Deferred fetch failures can precede our error listener. Controllers always
  // initialize aria-sort before starting asynchronous data requests.
  document.addEventListener("DOMContentLoaded", function () {
    if (!document.querySelector("th[aria-sort]") && panel.dataset.kind !== "error") {
      window.resultStates.error({ fatal: true });
    }
  }, { once: true });
  window.resultStates.loading("Loading " + entity + "…", page === "rankings" ? "Fetching journal rankings and editions. Your selected ranking and filters will be kept." : undefined);
})();
