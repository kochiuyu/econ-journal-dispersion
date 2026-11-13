/* Copy the controllers' current, canonical URL; keep manual sharing available. */
(function () {
  "use strict";
  var button = document.getElementById("copy-link");
  if (!button) return;
  var panel = button.closest(".share-results");
  var status = document.getElementById("copy-link-status");
  var manual = document.getElementById("copy-link-manual");
  var input = document.getElementById("copy-link-url");
  var busy = false;
  var revision = 0;

  function reset() {
    revision++;
    status.textContent = "";
    manual.hidden = true;
    input.value = "";
  }
  document.addEventListener("input", function (event) {
    if (!panel.contains(event.target)) reset();
  });
  document.addEventListener("change", function (event) {
    if (!panel.contains(event.target)) reset();
  });
  document.addEventListener("click", function (event) {
    if (!panel.contains(event.target) && event.target.closest("button")) reset();
  }, true);
  window.addEventListener("popstate", reset);
  input.addEventListener("focus", function () { input.select(); });
  input.addEventListener("click", function () { input.select(); });

  button.addEventListener("click", async function () {
    if (busy) return;
    reset();
    document.dispatchEvent(new CustomEvent("prepare-share"));
    var url = window.location.href;
    var ticket = revision;
    busy = true;
    button.setAttribute("aria-busy", "true");
    try {
      if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error("Clipboard unavailable");
      await navigator.clipboard.writeText(url);
      if (ticket === revision) status.textContent = "Link copied.";
    } catch (_) {
      if (ticket === revision) {
        status.textContent = "Copy the selected link to share these results.";
        input.value = url;
        manual.hidden = false;
        input.focus();
        input.select();
      }
    } finally {
      busy = false;
      button.removeAttribute("aria-busy");
    }
  });
})();
