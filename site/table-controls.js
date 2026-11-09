/* Sorting and pagination controls shared by the site's result tables. */
(function () {
  "use strict";

  var pager = document.getElementById("pager");
  var previous = document.getElementById("page-prev");
  var next = document.getElementById("page-next");
  var position = document.getElementById("page-position");
  var count = document.getElementById("count");
  var headers = document.querySelectorAll("th button[data-sort]");
  var numbers = new Intl.NumberFormat("en-US");

  window.tableControls = {
    sort: function (key, direction) {
      headers.forEach(function (button) {
        var header = button.closest("th");
        if (button.dataset.sort === key) {
          header.setAttribute("aria-sort", direction === "desc" ? "descending" : "ascending");
        } else {
          header.removeAttribute("aria-sort");
        }
      });
    },
    page: function (page, pages, changePage) {
      pager.hidden = false;
      position.textContent = "Page " + numbers.format(page) + " of " + numbers.format(pages);
      previous.disabled = page <= 1;
      next.disabled = page >= pages;
      previous.onclick = function () { go(page - 1); };
      next.onclick = function () { go(page + 1); };

      function go(target) {
        if (target < 1 || target > pages) return;
        changePage(target);
        count.focus({ preventScroll: true });
        count.scrollIntoView({ block: "start" });
      }
    }
  };
})();
