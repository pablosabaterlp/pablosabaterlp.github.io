(function () {
  "use strict";

  var config = window.SITE_CONFIG;
  var dict = window.I18N;
  var header = document.querySelector(".site-header");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Links from config.js ---------- */
  var links = {
    email: "mailto:" + config.EMAIL,
    site: config.SITE_URL,
    linkedin: config.LINKEDIN,
    github: config.GITHUB,
    resume: config.RESUME
  };
  var shown = {
    email: config.EMAIL,
    site: config.SITE_URL.replace(/^https?:\/\//, "").replace(/\/$/, ""),
    linkedin: config.LINKEDIN.replace(/^https?:\/\/(www\.)?/, "").replace(/\/$/, "")
  };
  document.querySelectorAll("[data-link]").forEach(function (el) {
    el.href = links[el.dataset.link];
  });
  document.querySelectorAll("[data-show]").forEach(function (el) {
    el.textContent = shown[el.dataset.show];
  });

  /* ---------- Language ---------- */
  var LANG_KEY = "lang";
  var lang = "en";

  function storedLang() {
    try { return localStorage.getItem(LANG_KEY); } catch (e) { return null; }
  }

  function setLang(next) {
    lang = dict[next] ? next : "en";
    var strings = dict[lang];
    document.documentElement.lang = lang;
    document.title = strings["meta.title"];
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var value = strings[el.dataset.i18n];
      if (value !== undefined) el.innerHTML = value;
    });
    document.querySelectorAll("[data-i18n-label]").forEach(function (el) {
      var value = strings[el.dataset.i18nLabel];
      if (value !== undefined) el.setAttribute("aria-label", value);
    });
    document.querySelectorAll(".lang button").forEach(function (btn) {
      btn.setAttribute("aria-pressed", String(btn.dataset.lang === lang));
    });
    document.querySelectorAll(".prj-toggle").forEach(updateToggleLabel);
    updateMobileCurrent();
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* storage unavailable */ }
  }

  document.querySelectorAll(".lang button").forEach(function (btn) {
    btn.addEventListener("click", function () { setLang(btn.dataset.lang); });
  });

  /* ---------- Progress bar ---------- */
  var fill = document.querySelector(".progress-fill");
  var ticking = false;
  function updateProgress() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var pct = max > 0 ? Math.min(100, (window.scrollY / max) * 100) : 0;
    fill.style.width = pct + "%";
    ticking = false;
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; requestAnimationFrame(updateProgress); }
  }, { passive: true });
  window.addEventListener("resize", updateProgress);
  updateProgress();

  /* ---------- Active section ---------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".nav-links a"));
  var currentId = null;

  function updateMobileCurrent() {
    var link = navLinks.filter(function (a) { return a.hash === "#" + currentId; })[0];
    var box = document.querySelector(".mobile-current");
    header.classList.toggle("has-current", !!link);
    if (!link) return;
    box.querySelector(".num").textContent = link.querySelector(".num").textContent;
    box.querySelector(".label").textContent = link.querySelector("[data-i18n]").textContent;
  }

  function setActive(id) {
    currentId = id;
    navLinks.forEach(function (a) {
      var on = a.hash === "#" + id;
      a.classList.toggle("is-active", on);
      if (on) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
    });
    updateMobileCurrent();
  }

  var sections = document.querySelectorAll("main > section");
  var visible = {};
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { visible[e.target.id] = e.isIntersecting; });
    // The topmost section crossing the middle band of the viewport wins.
    var active = null;
    sections.forEach(function (s) { if (!active && visible[s.id]) active = s.id; });
    if (active) setActive(active === "top" ? null : active);
  }, { rootMargin: "-40% 0px -55% 0px" });
  sections.forEach(function (s) { observer.observe(s); });

  /* ---------- Mobile menu ---------- */
  var menuBtn = document.querySelector(".menu-toggle");
  var nav = document.querySelector(".nav");
  function closeMenu() {
    menuBtn.setAttribute("aria-expanded", "false");
    nav.classList.remove("is-open");
  }
  menuBtn.addEventListener("click", function () {
    var open = menuBtn.getAttribute("aria-expanded") !== "true";
    menuBtn.setAttribute("aria-expanded", String(open));
    nav.classList.toggle("is-open", open);
  });
  navLinks.forEach(function (a) { a.addEventListener("click", closeMenu); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMenu(); });

  /* ---------- Project cards ---------- */
  function updateToggleLabel(btn) {
    var open = btn.getAttribute("aria-expanded") === "true";
    btn.querySelector("[data-i18n]").textContent = dict[lang][open ? "prj.less" : "prj.more"];
  }
  document.querySelectorAll(".prj-toggle").forEach(function (btn) {
    var panel = document.getElementById(btn.getAttribute("aria-controls"));
    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") !== "true";
      btn.setAttribute("aria-expanded", String(open));
      panel.classList.toggle("is-open", open);
      panel.inert = !open;
      updateToggleLabel(btn);
    });
  });

  /* ---------- QR switcher (mobile: segmented control + swipe) ---------- */
  var track = document.querySelector(".qr-track");
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".qr-seg button"));
  var dots = document.querySelectorAll(".qr-dots span");

  function markQr(i) {
    tabs.forEach(function (t, j) { t.setAttribute("aria-selected", String(i === j)); });
    dots.forEach(function (d, j) { d.classList.toggle("is-active", i === j); });
  }
  tabs.forEach(function (tab, i) {
    tab.addEventListener("click", function () {
      markQr(i);
      track.scrollTo({ left: i * track.clientWidth, behavior: reduceMotion ? "auto" : "smooth" });
    });
  });
  track.addEventListener("scroll", function () {
    if (!track.clientWidth) return;
    markQr(Math.round(track.scrollLeft / track.clientWidth));
  }, { passive: true });

  /* ---------- Init ---------- */
  setLang(storedLang() || "en");
})();
