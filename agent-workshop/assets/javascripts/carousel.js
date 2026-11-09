// Turn <div class="wk-carousel"> (a list of images) into a slider with left/right arrows, dots, and keyboard support.
// Without JavaScript the images simply stack, so the content stays readable.
(function () {
  function init() {
    Array.prototype.slice.call(document.querySelectorAll(".wk-carousel")).forEach(function (root) {
      if (root.dataset.ready) return;
      var imgs = Array.prototype.slice.call(root.querySelectorAll("img"));
      if (imgs.length < 2) return;
      root.dataset.ready = "1";
      var n = imgs.length, cur = 0;
      var track = document.createElement("div"); track.className = "wk-car-track";
      var slides = imgs.map(function (img, i) {
        var s = document.createElement("figure"); s.className = "wk-car-slide";
        s.setAttribute("role", "group"); s.setAttribute("aria-roledescription", "slide");
        s.setAttribute("aria-label", (i + 1) + " of " + n);
        img.removeAttribute("width"); img.removeAttribute("height"); img.loading = "eager";
        s.appendChild(img); track.appendChild(s); return s;
      });
      root.textContent = "";
      root.classList.add("wk-car-on");
      root.setAttribute("role", "region"); root.setAttribute("aria-roledescription", "carousel");
      root.setAttribute("aria-label", root.dataset.label || "Figure");
      root.tabIndex = 0;
      var prev = btn("wk-car-prev", "Previous", "\u2039"), next = btn("wk-car-next", "Next", "\u203A");
      var dots = document.createElement("div"); dots.className = "wk-car-dots";
      var dotEls = slides.map(function (_, i) {
        var d = btn("wk-car-dot", "Show " + (i + 1) + " of " + n, ""); d.onclick = function () { go(i); }; dots.appendChild(d); return d;
      });
      var stage = document.createElement("div"); stage.className = "wk-car-stage";
      stage.appendChild(prev); stage.appendChild(track); stage.appendChild(next);
      root.appendChild(stage); root.appendChild(dots);
      function btn(cls, label, text) {
        var b = document.createElement("button"); b.type = "button"; b.className = cls;
        b.setAttribute("aria-label", label); b.textContent = text; return b;
      }
      function go(i) {
        cur = Math.max(0, Math.min(n - 1, i));
        track.style.transform = "translateX(" + (-100 * cur) + "%)";
        slides.forEach(function (s, k) { s.setAttribute("aria-hidden", k === cur ? "false" : "true"); });
        dotEls.forEach(function (d, k) { if (k === cur) d.setAttribute("aria-current", "true"); else d.removeAttribute("aria-current"); });
        prev.disabled = cur === 0; next.disabled = cur === n - 1;
      }
      prev.onclick = function () { go(cur - 1); };
      next.onclick = function () { go(cur + 1); };
      root.addEventListener("keydown", function (e) {
        if (e.key === "ArrowLeft") { go(cur - 1); e.preventDefault(); }
        else if (e.key === "ArrowRight") { go(cur + 1); e.preventDefault(); }
      });
      var x0 = null;   // swipe on touch screens
      track.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
      track.addEventListener("touchend", function (e) {
        if (x0 === null) return;
        var dx = e.changedTouches[0].clientX - x0; x0 = null;
        if (Math.abs(dx) > 40) go(cur + (dx < 0 ? 1 : -1));
      });
      go(0);
    });
  }
  // Material's instant navigation swaps page content without a reload, so re-run on each page change.
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(init);
  else document.addEventListener("DOMContentLoaded", init);
})();
