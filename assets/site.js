/* ==========================================================================
   Energie Studio — Motion- und Interaktionsebene
   Grundsatz: Inhalte sind ohne JavaScript vollständig sichtbar.
   Dieses Skript verbessert nur, es schaltet nichts frei.
   ========================================================================== */
(function () {
  "use strict";

  var params  = new URLSearchParams(location.search);
  var CAPTURE = params.has("flat");
  var reduce  = window.matchMedia("(prefers-reduced-motion: reduce)").matches || CAPTURE;
  var root    = document.documentElement;

  if (CAPTURE) root.classList.add("capture");

  var hasGsap  = typeof gsap !== "undefined" && typeof ScrollTrigger !== "undefined";
  var hasSplit = typeof SplitText !== "undefined";
  if (hasGsap) gsap.registerPlugin(ScrollTrigger);

  var DESKTOP = window.matchMedia("(min-width: 961px)").matches;

  /* ── Lenis: weicher Scroll ───────────────────────────────────────────────
     Bewusst mit eigenem requestAnimationFrame statt über gsap.ticker: der
     Ticker schläft, wenn keine Animation läuft, und riss Lenis mit.      */
  var lenis = null;
  if (!reduce && typeof Lenis !== "undefined") {
    lenis = new Lenis({
      lerp: 0.075,
      wheelMultiplier: 0.7,
      smoothWheel: true,
      syncTouch: false,
      gestureOrientation: "vertical"
    });
    (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0);
    if (hasGsap) lenis.on("scroll", ScrollTrigger.update);
  }
  if (hasGsap) {
    gsap.ticker.lagSmoothing(0);
    /* Tastatur, Scrollbalken und Sprungmarken gehen an Lenis vorbei — ohne
       diesen Listener frieren die scrollgesteuerten Zustände dabei ein. */
    window.addEventListener("scroll", function () { ScrollTrigger.update(); }, { passive: true });
  }

  /* ── Barrierefreiheit: unversehrte Textkopie vor jedem Split ─────────── */
  function makeAccessible(el) {
    if (el.getAttribute("aria-hidden") === "true") return;
    var sr = document.createElement("span");
    sr.className = "sr-only";
    sr.textContent = el.textContent.trim();
    el.parentNode.insertBefore(sr, el);
    el.setAttribute("aria-hidden", "true");
  }
  function maskLines(lines) {
    lines.forEach(function (line) {
      var mask = document.createElement("span");
      mask.className = "line-mask";
      line.parentNode.insertBefore(mask, line);
      mask.appendChild(line);
    });
  }

  /* ── Hero-Eintritt ───────────────────────────────────────────────────── */
  function initHero() {
    if (reduce || !hasGsap) return;
    var title  = document.querySelector("[data-hero-title]");
    var visual = document.querySelector("[data-hero-visual]");
    var tl = gsap.timeline({ defaults: { ease: "expo.out" } });

    if (title) {
      var lines = Array.prototype.slice.call(title.querySelectorAll(".hero__line"));
      maskLines(lines);
      tl.fromTo(lines, { yPercent: 112 }, { yPercent: 0, duration: 1.25, stagger: 0.08 }, 0.15);
    }
    tl.fromTo(".hero__kicker", { autoAlpha: 0, y: 12 }, { autoAlpha: 1, y: 0, duration: .9 }, 0.05);
    tl.fromTo(".hero__lead, .hero__actions", { autoAlpha: 0, y: 18 }, { autoAlpha: 1, y: 0, duration: 1, stagger: .08 }, 0.55);
    if (visual) tl.fromTo(visual, { autoAlpha: 0, scale: 1.04, y: 22 }, { autoAlpha: 1, scale: 1, y: 0, duration: 1.5 }, 0.2);
    tl.fromTo(".fact", { autoAlpha: 0, x: 20 }, { autoAlpha: 1, x: 0, duration: .9, stagger: .09 }, 0.75);
  }

  /* ── Parallax im Hero ────────────────────────────────────────────────────
     Vier Ebenen laufen beim Scrollen unterschiedlich schnell nach unten.
     Je weiter hinten, desto stärker die Bewegung — daraus entsteht Tiefe. */
  function initParallax() {
    var hero = document.querySelector("[data-parallax]");
    if (!hero || reduce || !hasGsap || !DESKTOP) return;

    /* Der Vordergrund läuft bewusst nach OBEN, der Hintergrund nach unten.
       Diese Gegenbewegung macht den Effekt erst deutlich spürbar — laufen
       alle Ebenen in dieselbe Richtung, sieht man kaum einen Unterschied. */
    /* Ebene 1 und 2 sind 150 % hoch und um -50 % versetzt (siehe CSS). Ihr
       yPercent darf darum höchstens 33 betragen, sonst reissen sie oben ab. */
    var layers = [
      { n: "1", yPercent:  33 },   // Konstruktionsraster, ganz hinten
      { n: "2", yPercent:  24 },   // Blaupause
      { n: "3", yPercent:  34 },   // Gebäude
      { n: "4", yPercent: -14 }    // Text und Merkmale, ganz vorn
    ];

    var tl = gsap.timeline({
      scrollTrigger: {
        trigger: hero,
        start: "top top",
        end: "bottom top",
        scrub: 0.3
      }
    });

    layers.forEach(function (l, i) {
      var els = hero.querySelectorAll('[data-layer="' + l.n + '"]');
      if (!els.length) return;
      tl.to(els, { yPercent: l.yPercent, ease: "none" }, i === 0 ? 0 : "<");
    });

    // Das Gebäude kommt zusätzlich leicht auf den Betrachter zu
    var visual = hero.querySelector('[data-layer="3"] img');
    if (visual) tl.to(visual, { scale: 1.14, ease: "none" }, 0);
  }

  /* ── Philosophie-Text: Buchstaben werden beim Scrollen deckend ───────────
     Der Satz steht zunächst blass da und füllt sich beim Scrollen von links
     nach rechts auf. Ohne Skript bleibt er ganz normal lesbar.           */
  function initGradientText() {
    var el = document.querySelector("[data-gradient-text]");
    if (!el || reduce || !hasGsap || !hasSplit) return;

    makeAccessible(el);
    var split = new SplitText(el, { type: "words,chars", charsClass: "g-char" });

    /* 0.22 statt 0.1: auf hellem Grund wäre der Ausgangszustand sonst
       praktisch unsichtbar und der Satz erschiene aus dem Nichts. */
    gsap.fromTo(split.chars,
      { opacity: 0.22 },
      {
        opacity: 1,
        ease: "none",
        /* Lange Einzeldauer bei kleinem Versatz: dadurch sind immer rund
           ein Dutzend Zeichen gleichzeitig im Übergang und es entsteht ein
           weicher Verlauf statt eines harten Schalters. */
        duration: 4,
        stagger: { each: 0.3, from: "start" },
        /* scrub: true koppelt direkt an die Scrollposition. Mit einem
           Nachlaufwert bräuchte es den Animations-Ticker, der in manchen
           Umgebungen gedrosselt wird — dann bliebe der Text unverändert. */
        scrollTrigger: {
          trigger: el,
          start: "top 80%",
          end: "bottom 60%",
          scrub: true
        }
      });
  }

  /* ── Zeilen-Reveals ──────────────────────────────────────────────────── */
  function initReveals() {
    if (reduce || !hasGsap || !hasSplit) return;
    document.querySelectorAll("[data-reveal]").forEach(function (el) {
      makeAccessible(el);
      var split = new SplitText(el, { type: "lines", linesClass: "split-line" });
      maskLines(split.lines);
      gsap.fromTo(split.lines, { yPercent: 112 }, {
        yPercent: 0, duration: 1.05, ease: "expo.out", stagger: 0.07,
        scrollTrigger: { trigger: el, start: "top 88%", once: true }
      });
    });
    document.querySelectorAll(".v2 .kicker, .news .sec__head .kicker, .karte, .news__card, .person, .phase").forEach(function (el) {
      gsap.fromTo(el, { autoAlpha: 0, y: 22 }, {
        autoAlpha: 1, y: 0, duration: .8, ease: "expo.out",
        scrollTrigger: { trigger: el, start: "top 92%", once: true }
      });
    });
  }

  /* ── Navigation (horizontal, unverändert) ────────────────────────────── */
  function initNav() {
    var nav    = document.getElementById("nav");
    var burger = document.getElementById("burger");
    var menu   = document.getElementById("mobileMenu");
    var lastY  = 0;
    if (!nav) return;

    var sideBtn = document.getElementById("sidebarMenu");

    function toggleMenu() {
      var open = menu.classList.toggle("open");
      document.body.classList.toggle("menu-open", open);
      if (burger) {
        burger.setAttribute("aria-expanded", open ? "true" : "false");
        burger.setAttribute("aria-label", open ? "Menü schliessen" : "Menü öffnen");
      }
      if (sideBtn) sideBtn.setAttribute("aria-expanded", open ? "true" : "false");
    }
    if (sideBtn && menu) sideBtn.addEventListener("click", toggleMenu);

    if (burger && menu) {
      burger.addEventListener("click", toggleMenu);
      menu.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", function () {
          menu.classList.remove("open");
          document.body.classList.remove("menu-open");
          burger.setAttribute("aria-expanded", "false");
        });
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && menu.classList.contains("open")) burger.click();
      });
    }

    function update() {
      var y = window.scrollY;
      nav.classList.toggle("is--stuck", y > 24);
      if (document.body.classList.contains("menu-open")) { lastY = y; return; }
      if (y > 320 && y > lastY + 8)      nav.classList.add("is--hidden");
      else if (y < lastY - 8 || y < 320) nav.classList.remove("is--hidden");
      lastY = y;
    }
    if (hasGsap) ScrollTrigger.create({ onUpdate: update });
    else window.addEventListener("scroll", update, { passive: true });
    update();
  }

  /* ── Leistungen: das Haus fährt Gewerk für Gewerk ────────────────────────
     Die Section bleibt per CSS-sticky stehen; der Scrollweg darunter wird in
     vier gleiche Abschnitte geteilt. Bewusst ohne Animationsschleife: der
     Wechsel läuft über eine Klasse und CSS-Übergänge, damit er auch dort
     stimmt, wo requestAnimationFrame gedrosselt wird.                    */
  function initLeistungen() {
    var section = document.querySelector("[data-lst]");
    if (!section) return;
    var visual = section.querySelector("[data-lst-visual]");
    /* Absichtlich seitenweit: die Gewerke stehen auf grossen Bildschirmen
       in der Seitenleiste, auf kleinen im Balken der Section selbst. */
    var steps  = document.querySelectorAll("[data-lst-step]");
    var slides = section.querySelectorAll("[data-lst-slide]");
    var cards  = section.querySelectorAll("[data-lst-card]");
    var bar    = document.getElementById("sidebar");
    var count  = section.querySelector("[data-lst-count]");
    var label  = section.querySelector("[data-lst-mark-label]");
    var bilder = section.querySelectorAll("[data-lst-bild]");
    if (!visual || !steps.length) return;

    var MARKEN = [
      "Technikzentrale",
      "Luftverteilung",
      "Steigzonen",
      "Ganzes Gebäude"
    ];
    var N = 4;
    var now = -1;

    function setStep(i) {
      if (i === now) return;
      now = i;
      visual.setAttribute("data-step", String(i));
      /* Über das Attribut statt über den Index: es gibt zwei Sätze von
         Schaltflächen (Seitenleiste und Balken), ein Index träfe nur einen. */
      steps.forEach(function (b)  { b.classList.toggle("is-on", +b.getAttribute("data-lst-step") === i); });
      slides.forEach(function (s) { s.classList.toggle("is-on", +s.getAttribute("data-lst-slide") === i); });
      cards.forEach(function (c)  { c.classList.toggle("is-on", +c.getAttribute("data-lst-card") === i); });
      bilder.forEach(function (b) { b.classList.toggle("is-on", +b.getAttribute("data-lst-bild") === i); });
      if (count) count.textContent = "0" + (i + 1);
      if (label) label.textContent = MARKEN[i];
    }

    function travel() { return Math.max(1, section.offsetHeight - window.innerHeight); }
    /* Die letzte Bildschirmlänge gehört dem Vorhang: dort steht das vierte
       Gewerk schon fertig, während die dunkle Fläche hochkommt. */
    function stufenweg() { return Math.max(1, travel() - window.innerHeight); }

    var offenNow = null;
    function update() {
      var r = section.getBoundingClientRect();
      var p = -r.top / stufenweg();
      p = Math.max(0, Math.min(0.9999, p));
      setStep(Math.floor(p * N));

      /* Das Untermenü klappt nur auf, solange die Gewerke im Bild sind.
         Sobald der Vorhang hochkommt, ist Schluss — darum wird die letzte
         Bildschirmlänge (der Vorhang) nicht mitgerechnet. */
      var offen = r.top < window.innerHeight * 0.5
               && (r.bottom - window.innerHeight) > 0;
      if (offen !== offenNow) {
        offenNow = offen;
        if (bar) bar.classList.toggle("has-sub", offen);
      }
    }

    /* Klick auf den Balken führt in die Mitte des jeweiligen Abschnitts */
    steps.forEach(function (b) {
      b.addEventListener("click", function () {
        var i = parseInt(b.getAttribute("data-lst-step"), 10);
        var top = window.scrollY + section.getBoundingClientRect().top;
        scrollToY(Math.round(top + stufenweg() * (i + 0.5) / N));
      });
    });

    if (hasGsap) ScrollTrigger.create({ onUpdate: update, onRefresh: update });
    /* Zusätzlich am rohen Scroll-Ereignis: der Schrittwechsel soll nicht auf
       den nächsten Animationsschritt warten müssen. Mehrfaches Aufrufen
       kostet nichts, setStep steigt bei gleichem Stand sofort aus. */
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    setStep(0);
    update();

    var stand = function () { return -section.getBoundingClientRect().top / stufenweg(); };
    initLeistungenFahrt(section, setStep);
    initFilm(section, stand, N);
  }

  /* ── Bildfolge am Scrollrad ──────────────────────────────────────────────
     Das Video wird nicht abgespielt, sondern als Einzelbilder vorgeladen und
     je nach Scrollstand in eine Leinwand gezeichnet. Ein <video> per
     currentTime zu spulen ruckelt — besonders auf dem iPhone — weil der
     Decoder bei jedem Sprung neu ansetzt. Fertige Bilder hängen unmittelbar
     an der Scrollposition, brauchen keine Animationsschleife und laufen
     deshalb überall gleich weich, vorwärts wie rückwärts.

     Ein Abschnitt je Gewerk: wo eine Bildfolge liegt, führt sie die Bewegung
     und das Standbild tritt zurück; wo noch keine liegt, bleibt das Standbild
     mit der Kamerafahrt stehen. Kommt später ein Video dazu, genügt ein
     weiterer Eintrag in FILME.                                            */
  var FILME = {
    0: { ordner: "assets/film/heizung/",  anzahl: 80, endung: ".webp" },
    1: { ordner: "assets/film/lueftung/", anzahl: 80, endung: ".webp" },
    2: { ordner: "assets/film/sanitaer/", anzahl: 127, endung: ".webp" }
    /* Gebaeude-Automation kommt hierher, sobald das Endbild freigegeben und
       der Clip gebaut ist:
       3: { ordner: "assets/film/automation/", anzahl: N, endung: ".webp" }
       Er ist der einzige Clip, der die Tageszeit wechselt — er beginnt dort,
       wo Sanitaer aufhoert, faehrt in die Nacht und zuendet dann das Netz an.
       Die Sektion faehrt ueber --nacht farblich mit (siehe unten). */
  };

  /* Die Einzelbilder heissen bei jeder Neufassung gleich. Ohne diese Kennung
     bliebe der Browser beim alten Satz — die Seite sähe unverändert aus.
     Beim Neubauen der Bildfolgen mit hochzählen. */
  var FILM_STAND = "13";

  function initFilm(section, fortschritt, N) {
    var leinwand = section.querySelector("[data-lst-film]");
    var visual   = section.querySelector("[data-lst-visual]");
    if (!leinwand || !visual || reduce || !DESKTOP) return;

    var stift = leinwand.getContext("2d", { alpha: false });
    var GRUND = (getComputedStyle(root).getPropertyValue("--off") || "").trim() || "#f7f8f8";
    var teile = {}, letztesBild = null, filmAn = false, letzteNacht = -1;

    Object.keys(FILME).forEach(function (k) {
      teile[k] = { def: FILME[k], bilder: new Array(FILME[k].anzahl),
                   welle1: 0, bereit: false, geladen: false };
    });

    /* Die Leinwand bekommt genau so viele Bildpunkte, wie sie auf dem Schirm
       einnimmt. Sonst wird der feste Puffer auf die Fläche gestreckt und das
       Bild ist verzerrt. */
    function messe() {
      var r = leinwand.getBoundingClientRect();
      var d = Math.min(window.devicePixelRatio || 1, 2);
      var w = Math.round(r.width * d), h = Math.round(r.height * d);
      if (w && h && (leinwand.width !== w || leinwand.height !== h)) {
        leinwand.width = w; leinwand.height = h; letztesBild = null;
      }
    }

    /* wie object-fit: contain — dieselbe Geometrie wie beim Standbild,
       damit der Wechsel zwischen beiden nicht springt */
    function zeichne(t, i) {
      var b = t.bilder[i];
      if (!b) {                       /* Lücke: das nächstgelegene geladene Bild */
        for (var d = 1; d <= t.def.anzahl; d++) {
          if (t.bilder[i - d]) { b = t.bilder[i - d]; break; }
          if (t.bilder[i + d]) { b = t.bilder[i + d]; break; }
        }
      }
      if (!b || b === letztesBild) return;
      letztesBild = b;
      /* Das Bild fuellt die Flaeche randlos aus (wie object-fit: cover).
         Was ueber den Rahmen hinausragt, wird beschnitten — dafuer gibt es
         keine weiche Blende und keinen leeren Streifen mehr am Rand. */
      var kb = leinwand.width / leinwand.height, ki = b.width / b.height, w, h;
      if (ki > kb) { h = leinwand.height; w = h * ki; }
      else         { w = leinwand.width;  h = w / ki; }
      stift.drawImage(b, (leinwand.width - w) / 2, (leinwand.height - h) / 2, w, h);
    }

    function aktualisiere() {
      var p = Math.max(0, Math.min(0.9999, fortschritt()));
      var i = Math.floor(p * N);              /* welches Gewerk */
      var t = teile[i];
      var an = !!(t && t.bereit);
      if (an !== filmAn) { filmAn = an; visual.classList.toggle("hat-film", an); }
      if (!an) return;
      messe();
      /* Die Fahrt ist nach gut drei Vierteln des Abschnitts zu Ende; das
         letzte Viertel steht still. So bleibt am Schluss jedes Gewerks ein
         ruhiges Bild stehen, in dem man den Text lesen kann, statt dass die
         Kamera bis zum Umschalten durchläuft. */
      var lokal = Math.min(1, (p * N - i) / 0.76);
      zeichne(t, Math.min(t.def.anzahl - 1, Math.floor(lokal * t.def.anzahl)));
      /* Beim letzten Gewerk faehrt die ganze Sektion mit dem Bild in die
         Nacht. Der Wert steht etwas vor dem Bild, damit der Hintergrund
         schon dunkel ist, wenn die Lichter im Haus angehen. */
      var nacht = (i === N - 1) ? Math.max(0, Math.min(1, (lokal - 0.06) / 0.5)) : 0;
      if (nacht !== letzteNacht) {
        letzteNacht = nacht;
        section.style.setProperty("--nacht", nacht.toFixed(3));
      }
    }

    /* Geladen wird in drei Wellen: erst jedes vierte Bild, dann die Hälften,
       dann der Rest. Nach dem ersten Viertel der Daten ist die Fahrt schon
       bedienbar — fehlende Zwischenbilder werden so lange durch das
       nächstgelegene ersetzt — und wird danach von selbst feiner. */
    function laden(t) {
      var n = t.def.anzahl, gesehen = [], folge = [];
      [4, 2, 1].forEach(function (s) {
        for (var i = 0; i < n; i += s) if (!gesehen[i]) { gesehen[i] = 1; folge.push(i); }
      });
      var welle1 = Math.ceil(n / 4);
      folge.forEach(function (nr, rang) {
        var b = new Image();
        b.decoding = "async";
        b.onload = function () {
          t.bilder[nr] = b;
          if (rang < welle1 && ++t.welle1 === welle1) { t.bereit = true; }
          aktualisiere();
        };
        /* Ein fehlendes Bild ist kein Beinbruch: die Lückenfüllung greift,
           und fällt alles aus, bleibt das Standbild stehen. */
        b.src = t.def.ordner + ("00" + nr).slice(-3) + t.def.endung + "?v=" + FILM_STAND;
      });
    }

    /* Jede Bildfolge wird für sich geladen, und zwar erst kurz bevor sie an
       der Reihe ist. Sonst zieht der Besucher beim Betreten der Section alle
       Gewerke auf einmal herunter — auch die, die er nie zu sehen bekommt. */
    function pruefe() {
      var r = section.getBoundingClientRect();
      if (r.top > window.innerHeight * 1.5 || r.bottom < -window.innerHeight) return;
      var p = fortschritt() * N;
      var offen = 0;
      Object.keys(teile).forEach(function (k) {
        var t = teile[k];
        if (t.geladen) return;
        if (p > +k - 0.9) { t.geladen = true; laden(t); }
        else offen++;
      });
      if (!offen) window.removeEventListener("scroll", pruefe);
    }
    window.addEventListener("scroll", pruefe, { passive: true });
    pruefe();

    if (hasGsap) ScrollTrigger.create({ onUpdate: aktualisiere, onRefresh: aktualisiere });
    window.addEventListener("scroll", aktualisiere, { passive: true });
    window.addEventListener("resize", function () { letztesBild = null; aktualisiere(); });
  }

  /* ── Die Kamerafahrt am Scrollrad ────────────────────────────────────────
     Ohne GSAP springt der Ausschnitt von Stand zu Stand (CSS). Mit GSAP
     hängt er direkt am Scroll: zwischen den vier Ständen wird stufenlos
     überblendet, das Objekt zieht mit der Bewegung mit.

     scrub: true koppelt unmittelbar an die Scrollposition. Ein Nachlaufwert
     (scrub: 0.6) bräuchte den Animations-Ticker, der in gedrosselten
     Umgebungen steht — dann bliebe das Bild hängen. Das Weiche kommt hier
     ohnehin schon von Lenis.                                              */
  function initLeistungenFahrt(section, setStep) {
    if (!hasGsap) return;

    var haus = section.querySelector("[data-lst-haus]");
    var lead = section.querySelector("[data-lst-mark]");
    var vis  = section.querySelector("[data-lst-visual]");
    var copy = section.querySelector(".lst__copy");
    if (!haus || !lead || !vis) return;

    /* Vier Kamerastände: Versatz und Grösse des Objekts, dazu das Ziel der
       Leitlinie in Prozent des Bildbereichs. */
    var K = [
      { xp:  1.5, yp: -3, sc: 1.07, lx: 27, ly: 76 },
      { xp:  1,   yp:  4, sc: 1.06, lx: 34, ly: 30 },
      { xp: -1,   yp:  1, sc: 1.06, lx: 30, ly: 54 },
      { xp:  0,   yp: -1, sc: 0.94, lx: 52, ly: 44 }
    ];
    /* Als Funktion, damit die Werte bei Grössenänderung neu gerechnet
       werden (invalidateOnRefresh). */
    function zielX(i) { return function () { return vis.getBoundingClientRect().width  * K[i].lx / 100; }; }
    function zielY(i) { return function () { return vis.getBoundingClientRect().height * K[i].ly / 100; }; }

    var mm = gsap.matchMedia();
    mm.add({
      gross:  "(min-width: 1101px)",
      ruhig:  "(prefers-reduced-motion: reduce)"
    }, function (ctx) {
      if (!ctx.conditions.gross || ctx.conditions.ruhig) return;
      root.classList.add("gsap-lst");

      gsap.set(haus, { xPercent: K[0].xp, yPercent: K[0].yp, scale: K[0].sc, transformOrigin: "50% 50%" });
      gsap.set(lead, { x: zielX(0), y: zielY(0) });

      var tl = gsap.timeline({
        defaults: { ease: "power1.inOut" },
        scrollTrigger: {
          trigger: section,
          start: "top top",
          /* Genau der Weg der vier Schritte — die letzte Bildschirmlänge
             gehört dem Vorhang, dort steht die Fahrt schon still. */
          end: function () { return "+=" + Math.max(1, section.offsetHeight - 2 * window.innerHeight); },
          scrub: true,
          invalidateOnRefresh: true
        }
      });

      /* Der erste Stand hält bis zur Mitte des ersten Viertels, danach
         geht es Stand für Stand weiter — deckungsgleich mit den vier
         Abschnitten, die den Text schalten. */
      var t = 0.125, d = 0.25, i;
      for (i = 1; i < 4; i++) {
        tl.to(haus, { xPercent: K[i].xp, yPercent: K[i].yp, scale: K[i].sc, duration: d }, t)
          .to(lead, { x: zielX(i), y: zielY(i), duration: d }, t);
        t += d;
      }
      /* Die Textspalte läuft ein Stück gegen die Scrollrichtung. Das ist
         der Tiefeneindruck: vorne bewegt sich weniger als hinten. */
      if (copy) tl.fromTo(copy, { yPercent: 2.2 }, { yPercent: -2.2, ease: "none", duration: 1 }, 0);
      /* Platzhalter, damit die Zeitleiste genau eine Einheit lang ist */
      tl.to({ v: 0 }, { v: 1, duration: 1, ease: "none" }, 0);

      /* Welcher Text zu sehen ist, bleibt bewusst bei CSS. Das entscheidet
         über den Inhalt und darf nicht an der Animationsschleife hängen:
         steht die still (Hintergrund-Tab, Stromsparmodus), bliebe sonst
         ein leerer Block stehen. GSAP macht hier nur die Fahrt. */

      return function () {
        root.classList.remove("gsap-lst");
        gsap.set([haus, lead, copy], { clearProps: "all" });
      };
    });
  }

  /* ── Seitenleiste als Navigation ─────────────────────────────────────────
     Erscheint, sobald der helle Kopf verlassen ist, markiert das laufende
     Kapitel und kippt die Farbe mit. Der obere Balken tritt dann zurück. */
  function initSidebar() {
    var bar   = document.getElementById("sidebar");
    var nav   = document.getElementById("nav");
    var items = document.querySelectorAll(".sidebar__item");
    var secs  = document.querySelectorAll("[data-chapter]");
    if (!bar || !secs.length) return;

    var chapterNow = null, themeNow = null, shownNow = null;

    function update() {
      var focus = window.innerHeight * 0.4;
      var active = null;
      secs.forEach(function (s) {
        var r = s.getBoundingClientRect();
        if (r.top <= focus && r.bottom > focus) active = s;
      });

      // Sichtbar, sobald ein Kapitel den Fokuspunkt erreicht hat
      var shown = !!active;
      if (shown !== shownNow) {
        shownNow = shown;
        bar.classList.toggle("is-visible", shown);
        // Zwei Navigationen gleichzeitig wären doppelt: oben tritt zurück
        if (nav) nav.classList.toggle("is--replaced", shown);
      }
      if (!active) return;

      var theme = active.getAttribute("data-theme");
      if (theme !== themeNow) {
        themeNow = theme;
        bar.classList.toggle("is-light", theme === "light");
        var meta = document.querySelector('meta[name="theme-color"]');
        if (meta) meta.setAttribute("content", theme === "light" ? "#f7f8f8" : "#080d0b");
      }

      var chapter = active.getAttribute("data-chapter");
      if (chapter !== chapterNow) {
        chapterNow = chapter;
        items.forEach(function (a) {
          a.classList.toggle("is-active", a.getAttribute("data-rail") === chapter);
        });
      }
    }

    if (hasGsap) ScrollTrigger.create({ onUpdate: update, onRefresh: update });
    else window.addEventListener("scroll", update, { passive: true });
    update();
  }

  /* ── Überdeck-Scroll ─────────────────────────────────────────────────────
     Die Sektion darüber bleibt per CSS-sticky stehen; hier wird sie beim
     Überdecken sanft abgedunkelt, damit der Vorhang Tiefe bekommt.      */
  function initStack() {
    var stack = document.querySelector("[data-stack]");
    if (!stack || reduce || !hasGsap) return;
    var veil = stack.querySelector("[data-stack-veil]");
    var over = stack.querySelector(".stack__over");
    if (!veil || !over) return;

    gsap.fromTo(veil, { opacity: 0 }, {
      opacity: 0.55, ease: "none",
      scrollTrigger: {
        trigger: over,
        start: "top bottom",     // sobald der Vorhang unten auftaucht
        end: "top top",          // bis er oben angekommen ist
        scrub: true
      }
    });

  }

  /* ── Footer als Vorhang ──────────────────────────────────────────────────
     Der Footer wird unten festgesetzt und beim Scrollen hochgefahren. Der
     Platzhalter darüber liefert den Scrollweg und ersetzt die Höhe, die
     der Footer im Fluss verliert.                                       */
  function initFooterCurtain() {
    var footer = document.querySelector(".footer");
    var space  = document.querySelector("[data-footer-space]");
    var veil   = document.querySelector("[data-kontakt-veil]");
    if (!footer || !space || reduce || !hasGsap || !DESKTOP) return;

    /* Der Vorhang setzt den Footer unten fest. Ist er höher als der
       Bildschirm, bliebe sein oberer Teil — Foto und Überschrift —
       dauerhaft ausserhalb des Bildes. Dann läuft er lieber normal mit. */
    if (footer.offsetHeight > window.innerHeight) return;

    function size() {
      // Footerhöhe plus Scrollweg für die Fahrt nach oben
      space.style.height = (footer.offsetHeight + window.innerHeight * 0.65) + "px";
    }
    root.classList.add("curtain");
    size();
    window.addEventListener("resize", function () { size(); ScrollTrigger.refresh(); });

    gsap.fromTo(footer, { yPercent: 100 }, {
      yPercent: 0, ease: "none",
      scrollTrigger: { trigger: space, start: "top bottom", end: "bottom bottom", scrub: true }
    });

    if (veil) {
      gsap.fromTo(veil, { opacity: 0 }, {
        opacity: 0.45, ease: "none",
        scrollTrigger: { trigger: space, start: "top bottom", end: "bottom bottom", scrub: true }
      });
    }

    /* Kontakt sitzt jetzt im Footer. Sobald der Vorhang halb oben ist,
       springt der Kapitelmarker auf 05 — sonst bliebe er auf 04 hängen. */
    var items = document.querySelectorAll(".sidebar__item");
    ScrollTrigger.create({
      trigger: space, start: "center bottom", end: "bottom bottom",
      onToggle: function (self) {
        items.forEach(function (a) {
          var t = a.getAttribute("data-rail");
          if (t === "kontakt") a.classList.toggle("is-active", self.isActive);
          else if (self.isActive) a.classList.remove("is-active");
        });
      }
    });
  }

  /* ── Schieber ─────────────────────────────────────────────────────────
     Gilt für alle Bahnen mit [data-slider]: die Teamportraits und die
     Projektkarten. Ein Klick schiebt um genau eine Kachel weiter.      */
  function initSlider() {
    document.querySelectorAll("[data-slider]").forEach(function (wrap) {
      var track = wrap.querySelector("[data-slider-track]");
      if (!track || !track.children.length) return;
      var prev  = wrap.querySelector("[data-slider-prev]");
      var next  = wrap.querySelector("[data-slider-next]");
      var bar   = wrap.querySelector("[data-slider-progress]");
      var erste = track.children[0];

      /* Kachelbreite plus Lücke — sonst bleibt bei jedem Klick ein Rest. */
      function step() {
        var luecke = parseFloat(getComputedStyle(track).columnGap) || 0;
        return erste.getBoundingClientRect().width + luecke;
      }

      function sync() {
        var max = track.scrollWidth - track.clientWidth;
        var p = max > 2 ? track.scrollLeft / max : 1;
        /* Der Balken zeigt den sichtbaren Anteil plus Fortschritt —
           passt alles ins Bild, ist er voll. */
        var sichtbar = track.clientWidth / track.scrollWidth;
        if (bar) bar.style.transform = "scaleX(" + Math.min(1, sichtbar + p * (1 - sichtbar)) + ")";
        if (prev) prev.disabled = track.scrollLeft <= 2;
        if (next) next.disabled = track.scrollLeft >= max - 2;
      }

      function slide(dir) {
        track.scrollBy({ left: dir * step(), behavior: reduce ? "auto" : "smooth" });
      }
      if (prev) prev.addEventListener("click", function () { slide(-1); });
      if (next) next.addEventListener("click", function () { slide(1); });
      track.addEventListener("scroll", sync, { passive: true });
      window.addEventListener("resize", sync);
      sync();
    });
  }

  /* ── Kennzahlen ──────────────────────────────────────────────────────── */
  function initCounters() {
    if (reduce || !hasGsap) return;
    document.querySelectorAll("[data-count]").forEach(function (el) {
      var target = parseInt(el.getAttribute("data-count"), 10);
      var obj = { v: 0 };
      gsap.to(obj, {
        v: target, duration: 1.4, ease: "power2.out",
        onUpdate: function () { el.textContent = Math.round(obj.v); },
        scrollTrigger: { trigger: el, start: "top 88%", once: true }
      });
    });
  }

  /* ── Phasenlinie ─────────────────────────────────────────────────────── */
  function initPhasen() {
    var bar   = document.querySelector("[data-phase-bar]");
    var track = document.getElementById("ablauf");
    if (!bar || !track || reduce || !hasGsap || !DESKTOP) return;
    gsap.fromTo(bar, { scaleX: 0 }, {
      scaleX: 1, ease: "none",
      scrollTrigger: { trigger: track, start: "top 78%", end: "bottom 62%", scrub: 0.4 }
    });
  }

  /* ── Bilder ──────────────────────────────────────────────────────────── */
  function initMedia() {
    if (reduce || !hasGsap) return;
    document.querySelectorAll(".karte__media, .case__media").forEach(function (el) {
      var img = el.querySelector("img");
      if (!img) return;
      gsap.fromTo(img, { scale: 1.1 }, {
        scale: 1, duration: 1.3, ease: "expo.out",
        scrollTrigger: { trigger: el, start: "top 92%", once: true }
      });
    });
  }

  /* ── Sprungmarken ──────────────────────────────────────────────────────
     Zielposition als Zahl berechnen statt Lenis das Element auflösen zu
     lassen: sticky- und Transform-Kontexte auf der Seite machen die
     Element-Variante unzuverlässig. Mit Nachkontrolle und Notausgang.   */
  function scrollToTarget(el) {
    scrollToY(Math.round(window.scrollY + el.getBoundingClientRect().top - 8));
  }

  function scrollToY(y) {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    y = Math.max(0, Math.min(y, max));

    if (lenis) {
      var from = window.scrollY;
      lenis.scrollTo(y, { duration: 1.1 });
      /* Notausgang: Lenis fährt über requestAnimationFrame. Wird das
         gedrosselt (Hintergrund-Tab, stromsparender Modus), bewegt sich
         nichts — dann springt der Browser selbst ans Ziel. Ohne
         lenis.stop(), das würde den Scroll komplett sperren. */
      setTimeout(function () {
        if (Math.abs(window.scrollY - from) < 4 && Math.abs(y - from) > 20) {
          window.scrollTo(0, y);
          if (hasGsap) ScrollTrigger.update();
        }
      }, 260);
      return;
    }
    window.scrollTo({ top: y, behavior: reduce ? "auto" : "smooth" });
  }

  function initAnchors() {
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener("click", function (e) {
        var id = a.getAttribute("href");
        if (id.length < 2) return;
        var el = document.querySelector(id);
        if (!el) return;
        e.preventDefault();
        scrollToTarget(el);
      });
    });
  }

  /* ── Kontaktformular ─────────────────────────────────────────────────────
     Es gibt keinen Server, der die Anfrage entgegennimmt. Statt ein
     Formular vorzutäuschen, das ins Leere läuft, stellt das Skript die
     Nachricht zusammen und übergibt sie ans Mailprogramm. */
  function initKontaktForm() {
    var form = document.querySelector("[data-kontakt-form]");
    if (!form) return;
    var hinweis = form.querySelector("[data-kontakt-hinweis]");
    var ADRESSE = "info@energie-studio.ch";

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var name = (d.get("name") || "").trim();
      var mail = (d.get("mail") || "").trim();
      var tel  = (d.get("tel")  || "").trim();
      var text = (d.get("text") || "").trim();

      if (!name || !mail || !text) {
        hinweis.textContent = "Bitte Name, E-Mail und Ihr Vorhaben ausfüllen.";
        hinweis.setAttribute("data-fehler", "");
        return;
      }
      hinweis.removeAttribute("data-fehler");

      var betreff = "Anfrage von " + name;
      var koerper = [
        text, "",
        "— — —",
        "Name: " + name,
        "E-Mail: " + mail,
        tel ? "Telefon: " + tel : null
      ].filter(Boolean).join("\n");

      window.location.href = "mailto:" + ADRESSE +
        "?subject=" + encodeURIComponent(betreff) +
        "&body="    + encodeURIComponent(koerper);
      hinweis.textContent = "Ihr Mailprogramm öffnet sich mit der fertigen Anfrage.";
    });
  }

  /* ── Start, genau einmal ─────────────────────────────────────────────── */
  var booted = false;
  function boot() {
    if (booted) return;
    booted = true;
    initNav();
    initSidebar();
    initAnchors();
    initStack();
    initFooterCurtain();
    initHero();
    initParallax();
    initGradientText();
    initReveals();
    initLeistungen();
    initSlider();
    initCounters();
    initPhasen();
    initMedia();
    initKontaktForm();
    if (hasGsap) ScrollTrigger.refresh();
  }

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(boot);
    setTimeout(boot, 2000);
  } else {
    window.addEventListener("load", boot);
  }
})();
