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

  var mobileTable = document.querySelector("[data-mobile-table]");
  var mobileSort, mobileDirection;
  var currentKey, currentDirection;
  var detailSequence = 0;

  function mobileSetup() {
    if (!mobileTable || mobileSort) return;
    headers.forEach(function (button) {
      button.dataset.label = button.textContent;
      if (button.dataset.sort !== "appointments") return;
      button.setAttribute("aria-label", "Appointments");
      var full = document.createElement("span");
      full.className = "column-full-label";
      full.textContent = "Appointments";
      var short = document.createElement("abbr");
      short.className = "column-mobile-label";
      short.title = "Appointments";
      short.textContent = "Appts";
      button.replaceChildren(full, short);
    });
    var toolbar = document.createElement("div");
    toolbar.className = "results-mobile-sort";
    toolbar.setAttribute("role", "group");
    toolbar.setAttribute("aria-label", "Sort results");
    var label = document.createElement("label");
    label.htmlFor = "results-mobile-sort";
    label.className = "lbl";
    label.textContent = "Sort by";
    mobileSort = document.createElement("select");
    mobileSort.id = label.htmlFor;
    mobileDirection = document.createElement("button");
    mobileDirection.type = "button";
    mobileDirection.className = "btn";
    mobileSort.addEventListener("change", function () {
      var button = Array.from(headers).find(function (item) { return item.dataset.sort === mobileSort.value; });
      if (button) button.click();
    });
    mobileDirection.addEventListener("click", function () {
      var button = Array.from(headers).find(function (item) { return item.dataset.sort === currentKey; });
      if (button) button.click();
    });
    toolbar.append(label, mobileSort, mobileDirection);
    mobileTable.closest(".tbl-wrap").before(toolbar);
  }

  function mobileSortState() {
    mobileSetup();
    if (!mobileSort) return;
    mobileSort.replaceChildren();
    headers.forEach(function (button) {
      if (button.closest("th").hidden) return;
      var option = document.createElement("option");
      option.value = button.dataset.sort;
      option.textContent = button.dataset.label || button.textContent;
      mobileSort.appendChild(option);
    });
    mobileSort.value = currentKey;
    mobileDirection.textContent = currentDirection === "desc" ? "Descending ↓" : "Ascending ↑";
    mobileDirection.setAttribute("aria-label", currentDirection === "desc" ? "Descending sort; change to ascending" : "Ascending sort; change to descending");
  }

  function mobileRows() {
    if (!mobileTable) return;
    var kind = mobileTable.dataset.mobileTable;
    var visible = kind === "rankings" ? [0, 1] : [0, 3, 4];
    var columns = Array.from(mobileTable.tHead.rows[0].cells).filter(function (cell) { return !cell.hidden; });
    // The optional Rankings weight column changes the position of the journal id.
    Array.from(mobileTable.tHead.rows[0].cells).forEach(function (cell, index) {
      cell.classList.toggle("mobile-secondary", visible.indexOf(index) === -1);
    });
    Array.from(mobileTable.tBodies[0].rows).forEach(function (row) {
      if (row.querySelector(".empty")) return;
      var cells = Array.from(row.cells);
      cells.forEach(function (cell, index) { cell.classList.toggle("mobile-secondary", visible.indexOf(index) === -1); });
      var detailRow = document.createElement("tr");
      detailRow.className = "results-detail-row";
      detailRow.id = "results-details-" + (++detailSequence);
      detailRow.hidden = true;
      var detailCell = document.createElement("td");
      detailCell.colSpan = visible.length;
      detailRow.appendChild(detailCell);
      var toggle = document.createElement("button");
      toggle.type = "button";
      toggle.className = "btn results-detail-toggle";
      toggle.textContent = "Details";
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-controls", detailRow.id);
      toggle.setAttribute("aria-label", "Details for " + cells[0].textContent.trim());
      toggle.addEventListener("click", function () {
        if (!detailCell.firstChild) {
          var list = document.createElement("dl");
          cells.forEach(function (cell, index) {
            if (visible.indexOf(index) !== -1) return;
            var term = document.createElement("dt");
            term.textContent = columns[index].textContent.trim();
            var value = document.createElement("dd");
            Array.from(cell.childNodes).forEach(function (node) { value.appendChild(node.cloneNode(true)); });
            list.append(term, value);
          });
          detailCell.appendChild(list);
        }
        detailRow.hidden = !detailRow.hidden;
        toggle.setAttribute("aria-expanded", String(!detailRow.hidden));
      });
      cells[0].appendChild(toggle);
      row.after(detailRow);
    });
    mobileSortState();
  }

  window.tableControls = {
    mobileRows: mobileRows,
    sort: function (key, direction) {
      currentKey = key;
      currentDirection = direction;
      mobileSortState();
      headers.forEach(function (button) {
        var header = button.closest("th");
        var label = button.dataset.label || button.textContent;
        if (button.dataset.sort === "appointments" && mobileTable && window.matchMedia("(max-width: 640px)").matches) label = "Appts (appointments)";
        button.setAttribute("aria-label", button.dataset.sort === key ? label + ", sorted " + (direction === "desc" ? "descending; sort ascending" : "ascending; sort descending") : "Sort by " + label);
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
  window.matchMedia("(max-width: 640px)").addEventListener("change", function () {
    if (currentKey) window.tableControls.sort(currentKey, currentDirection);
  });
})();

