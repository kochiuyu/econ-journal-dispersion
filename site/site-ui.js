/* A progressively enhanced mobile menu; navigation stays visible without JS. */
(function () {
  "use strict";
  var nav = document.querySelector(".topbar .nav");
  if (!nav) return;
  var bar = nav.parentElement;
  var small = window.matchMedia("(max-width: 640px)");
  var button = document.createElement("button");
  button.type = "button";
  button.className = "site-menu-toggle";
  button.textContent = "Menu";
  nav.id = "site-navigation";
  button.setAttribute("aria-controls", nav.id);
  var current = nav.querySelector('[aria-current="page"]');
  var page = document.createElement("span");
  page.className = "mobile-page";
  page.textContent = current ? current.textContent : "Icon credits";
  bar.querySelector(".t1").after(page);
  nav.before(button);
  function setOpen(open) {
    nav.hidden = small.matches && !open;
    button.setAttribute("aria-expanded", String(!nav.hidden));
    button.setAttribute("aria-label", nav.hidden ? "Open site menu" : "Close site menu");
    bar.classList.toggle("menu-open", !nav.hidden && small.matches);
  }
  button.addEventListener("click", function () { setOpen(nav.hidden); });
  bar.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && small.matches && !nav.hidden) {
      event.preventDefault();
      setOpen(false);
      button.focus();
    }
  });
  small.addEventListener("change", function () {
    // Keep focused links visible when crossing into the mobile layout.
    var buttonFocused = document.activeElement === button;
    setOpen(nav.contains(document.activeElement));
    if (!small.matches && buttonFocused) (current || nav.querySelector("a")).focus();
  });
  setOpen(false);
})();
