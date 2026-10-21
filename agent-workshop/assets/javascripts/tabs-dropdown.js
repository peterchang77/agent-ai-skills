// Group header tabs named "Group · Variant" into one dropdown per group (e.g. "Demo ▾" with Tabular / Imaging).
// Plain DOM only. If this script fails, the ungrouped tabs still work. Below the wide-screen breakpoint Material hides the tabs and uses the drawer.
document.addEventListener("DOMContentLoaded", function () {
  var list = document.querySelector(".md-tabs__list");
  if (!list) return;
  var groups = {};
  Array.prototype.slice.call(list.children).forEach(function (li) {
    var a = li.querySelector("a.md-tabs__link");
    var m = a && a.textContent.trim().match(/^(.+?)\s·\s(.+)$/);
    if (m) (groups[m[1]] = groups[m[1]] || []).push({ li: li, a: a, variant: m[2] });
  });
  Object.keys(groups).forEach(function (name) {
    var items = groups[name];
    var host = items[0].li;
    var active = items.some(function (i) { return i.li.classList.contains("md-tabs__item--active"); });
    var menu = document.createElement("ul");
    menu.className = "wk-dd-menu"; menu.setAttribute("role", "menu");
    items.forEach(function (i) {
      var li = document.createElement("li"); li.setAttribute("role", "none");
      var a = i.a.cloneNode(false);
      a.textContent = i.variant; a.className = "wk-dd-link"; a.setAttribute("role", "menuitem");
      if (i.li.classList.contains("md-tabs__item--active")) a.setAttribute("aria-current", "page");
      li.appendChild(a); menu.appendChild(li);
    });
    var btn = document.createElement("a");
    btn.className = "md-tabs__link wk-dd-btn"; btn.href = items[0].a.getAttribute("href");
    btn.setAttribute("aria-haspopup", "true"); btn.setAttribute("aria-expanded", "false");
    btn.textContent = name;
    host.className = "md-tabs__item wk-dd" + (active ? " md-tabs__item--active" : "");
    host.textContent = ""; host.appendChild(btn); host.appendChild(menu);
    items.slice(1).forEach(function (i) { i.li.remove(); });
    // A first tap or click opens the menu (needed on touch screens); a second click on the button follows its link.
    btn.addEventListener("click", function (e) {
      if (!host.classList.contains("wk-open")) { e.preventDefault(); host.classList.add("wk-open"); btn.setAttribute("aria-expanded", "true"); }
    });
    document.addEventListener("click", function (e) {
      if (!host.contains(e.target)) { host.classList.remove("wk-open"); btn.setAttribute("aria-expanded", "false"); }
    });
    host.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { host.classList.remove("wk-open"); btn.setAttribute("aria-expanded", "false"); btn.focus(); }
    });
  });
});
