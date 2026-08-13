# -*- coding: utf-8 -*-
"""Baut die Wissens-Unterseite und die Einzelbeitraege.

Alles wird erzeugt, nichts von Hand gepflegt: Kopf, Navigation, Fuss und
Lesezeit sind fuer jeden Beitrag identisch. Neue Beitraege kommen in
beitraege.py dazu, dann dieses Skript nochmal laufen lassen.
"""
import os, re, math, html
from beitraege import BEITRAEGE
from ergaenzungen import ERGAENZUNG
from formular import formular

# Zusatzabschnitte anhaengen
for _b in BEITRAEGE:
    _b["inhalt"] = _b["inhalt"] + ERGAENZUNG.get(_b["slug"], [])

ZIEL = "/Users/klartext/Desktop/energie-studio-v2"
STAND = os.environ.get("STAND", "1")

# Woerter pro Minute beim stillen Lesen deutscher Sachtexte.
WPM = 200


def woerter(b):
    t = b["lead"]
    for art, wert in b["inhalt"]:
        t += " " + (" ".join(wert) if isinstance(wert, list) else wert)
    return len(re.findall(r"[\wäöüÄÖÜß-]+", t))


def lesezeit(b):
    m = max(1, int(math.ceil(woerter(b) / WPM)))
    return m


def kopf(titel, beschreibung, tiefe, aktiv=""):
    p = "../" if tiefe else ""
    def a(ziel, name, kennung=""):
        cur = ' aria-current="page"' if kennung and kennung == aktiv else ""
        return '<li><a href="%s%s"%s>%s</a></li>' % (p, ziel, cur, name)
    return '''<!DOCTYPE html>
<html lang="de-CH">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#ffffff">
<title>%s</title>
<meta name="description" content="%s">
<link rel="icon" type="image/svg+xml" href="%sassets/logo/icon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Overpass+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.css">
<link rel="stylesheet" href="%sassets/style.css?v=%s">
</head>
<body>

<a class="sr-only" href="#main">Zum Inhalt springen</a>

<header class="nav is--stuck" id="nav">
  <div class="nav__inner">
    <a class="nav__logo" href="%sindex.html" aria-label="Energie Studio, zur Startseite">
      <img src="%sassets/logo/logo-h.svg" alt="Energie Studio">
    </a>
    <nav aria-label="Hauptnavigation">
      <ul class="nav__links">
        %s
      </ul>
    </nav>
    <a class="btn btn--primary nav__cta" href="%sindex.html#kontakt">Beratung anfragen
      <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5" stroke="currentColor" stroke-width="1.6"/></svg>
    </a>
    <button class="burger" id="burger" aria-label="Menü öffnen" aria-expanded="false" aria-controls="mobileMenu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="mobile-menu" id="mobileMenu">
  <a href="%sindex.html#leistungen">Leistungen</a>
  <a href="%sprojekte.html">Projekte</a>
  <a href="%sindex.html#team">Über uns</a>
  <a href="%swissen.html">Wissen</a>
  <a href="%sindex.html#kontakt">Kontakt</a>
</div>

<main id="main">
''' % (html.escape(titel), html.escape(beschreibung), p, p, STAND, p, p,
       "\n        ".join([
           a("index.html#leistungen", "Leistungen"),
           a("projekte.html", "Projekte", "projekte"),
           a("index.html#team", "Über uns"),
           a("wissen.html", "Wissen", "wissen"),
           a("index.html#kontakt", "Kontakt"),
       ]), p, p, p, p, p, p)


def fuss(tiefe):
    p = "../" if tiefe else ""
    return '''
</main>

<footer class="footer">
  <div class="wrap footer__in">
    <ul class="footer__links">
      <li><a href="%sindex.html#leistungen">Leistungen</a></li>
      <li><a href="%sprojekte.html">Projekte</a></li>
      <li><a href="%sindex.html#team">Team</a></li>
      <li><a href="%swissen.html">Wissen</a></li>
      <li><a href="%sindex.html#kontakt">Kontakt</a></li>
      <li><a href="../impressum.html">Impressum &amp; Datenschutz</a></li>
    </ul>
    <a class="nach-oben" href="#main" data-nach-oben>
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
        <path d="M8 13.5V2.5M3.5 7 8 2.5 12.5 7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      Nach oben
    </a>
    <span class="footer__base">© 2026 Energie Studio AG · Windisch, Kanton Aargau</span>
  </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/SplitText.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js"></script>
<script src="%sassets/site.js?v=%s"></script>
</body>
</html>
''' % (p, p, p, p, p, p, STAND)


def kontaktblock(tiefe):
    return ("""
<section class="sec" style="background:var(--nebel)">
  <div class="wrap">
    <div class="kontakt">
      <div>
        <p class="kicker" style="color:var(--teal-ink);margin-bottom:1.1rem">Kontakt</p>
        <h2 class="h2" data-reveal>Eine Frage zu Ihrem<br>Geb\u00e4ude?</h2>
        <p class="lead" style="margin-top:1.5rem">Schildern Sie uns kurz die Ausgangslage. Wir melden uns innerhalb von zwei Arbeitstagen.</p>
        <dl class="kontakt__list">
          <div class="kontakt__row"><dt class="kenn">E-Mail</dt><dd><a href="mailto:hello@energie-studio.ch">hello@energie-studio.ch</a></dd></div>
          <div class="kontakt__row" style="border:0"><dt class="kenn">Standort</dt><dd>Windisch, Kanton Aargau</dd></div>
        </dl>
      </div>
""" + formular("      ") + """
    </div>
  </div>
</section>
""")


# ── Uebersichtsseite ─────────────────────────────────────────────────────
karten = []
for b in BEITRAEGE:
    karten.append('''      <a class="news__card" href="wissen/%s.html">
        <div class="news__media"><img src="%s" alt="%s" loading="lazy"></div>
        <div class="news__body">
          <span class="kenn news__date">%s · %d Min.</span>
          <h3>%s</h3>
          <p>%s</p>
          <span class="news__go" aria-hidden="true">
            <svg width="18" height="12" viewBox="0 0 18 12" fill="none"><path d="M0 6h16M11 1l5 5-5 5" stroke="currentColor" stroke-width="1.5"/></svg>
          </span>
        </div>
      </a>''' % (b["slug"], b["bild"], html.escape(b["alt"]),
                 html.escape(b["kategorie"]), lesezeit(b),
                 html.escape(b["titel"]), html.escape(b["teaser"])))

uebersicht = kopf(
    "Wissen — Energie Studio",
    "Fachbeiträge zu Heizung, Lüftung, Sanitär und Gebäudeautomation: Normen, "
    "Förderung, Betrieb und Sanierung im Bestand.",
    0, "wissen")
uebersicht += '''
<section class="page-head">
  <div class="wrap">
    <p class="kenn" style="color:var(--teal-ink);margin-bottom:1.2rem">Wissen</p>
    <h1 class="display" data-reveal>News &amp;<br>Einblicke</h1>
    <p class="lead" style="margin-top:1.4rem;max-width:60ch">
      Fachbeiträge aus der Planungspraxis — zu Normen, Förderung, Sanierung im Bestand
      und dem, was im Betrieb tatsächlich über den Verbrauch entscheidet.
      Jeder Beitrag ist in sechs bis sieben Minuten gelesen.
    </p>
  </div>
</section>

<section class="sec news" style="min-height:0">
  <div class="wrap">
    <div class="news__cards news__cards--alle">
''' + "\n\n".join(karten) + '''
    </div>
  </div>
</section>
''' + kontaktblock(0) + fuss(0)

open(os.path.join(ZIEL, "wissen.html"), "w").write(uebersicht)
print("wissen.html  %d Beitraege" % len(BEITRAEGE))


# ── Einzelseiten ─────────────────────────────────────────────────────────
os.makedirs(os.path.join(ZIEL, "wissen"), exist_ok=True)

for i, b in enumerate(BEITRAEGE):
    koerper = []
    for art, wert in b["inhalt"]:
        if art == "h2":
            koerper.append("      <h2>%s</h2>" % html.escape(wert))
        elif art == "p":
            koerper.append("      <p>%s</p>" % html.escape(wert))
        elif art == "ul":
            li = "\n".join("        <li>%s</li>" % html.escape(x) for x in wert)
            koerper.append("      <ul>\n%s\n      </ul>" % li)
        elif art == "merk":
            koerper.append('      <p class="beitrag__merk">%s</p>' % html.escape(wert))

    # Zwei weitere Beitraege als Hinweis am Schluss
    andere = [x for x in BEITRAEGE if x["slug"] != b["slug"]]
    weiter = andere[(i) % len(andere):(i) % len(andere) + 2]
    if len(weiter) < 2:
        weiter = andere[:2]
    weiter_html = "\n\n".join('''        <a class="news__card" href="%s.html">
          <div class="news__media"><img src="../%s" alt="%s" loading="lazy"></div>
          <div class="news__body">
            <span class="kenn news__date">%s · %d Min.</span>
            <h3>%s</h3>
            <p>%s</p>
            <span class="news__go" aria-hidden="true">
              <svg width="18" height="12" viewBox="0 0 18 12" fill="none"><path d="M0 6h16M11 1l5 5-5 5" stroke="currentColor" stroke-width="1.5"/></svg>
            </span>
          </div>
        </a>''' % (w["slug"], w["bild"], html.escape(w["alt"]),
                   html.escape(w["kategorie"]), lesezeit(w),
                   html.escape(w["titel"]), html.escape(w["teaser"])) for w in weiter)

    seite = kopf("%s — Energie Studio" % b["titel"], b["teaser"], 1, "wissen")
    seite += '''
<article class="beitrag">

  <header class="page-head beitrag__kopf">
    <div class="wrap">
      <p class="kenn beitrag__meta">
        <a href="../wissen.html">Wissen</a>
        <span aria-hidden="true">·</span> %s
        <span aria-hidden="true">·</span> %d Min. Lesezeit
      </p>
      <h1 class="h2 beitrag__titel" data-reveal>%s</h1>
      <p class="lead beitrag__lead">%s</p>
    </div>
  </header>

  <figure class="beitrag__bild">
    <img src="../%s" alt="%s" fetchpriority="high">
  </figure>

  <div class="wrap">
    <div class="beitrag__text">
%s
    </div>

    <p class="beitrag__hinweis">
      Dieser Beitrag ordnet ein und ersetzt keine Planung am konkreten Objekt.
      Normen, Förderbedingungen und kantonale Vorgaben ändern sich — prüfen Sie
      den aktuellen Stand bei der zuständigen Stelle.
    </p>

    <div class="beitrag__weiter">
      <p class="kicker" style="color:var(--teal-ink)">Weiterlesen</p>
      <div class="news__cards news__cards--zwei">
%s
      </div>
    </div>
  </div>
</article>
''' % (html.escape(b["kategorie"]), lesezeit(b), html.escape(b["titel"]),
       html.escape(b["lead"]), b["bild"], html.escape(b["alt"]),
       "\n".join(koerper), weiter_html)
    seite += kontaktblock(1) + fuss(1)

    open(os.path.join(ZIEL, "wissen", b["slug"] + ".html"), "w").write(seite)
    print("  %-32s %4d Woerter  %d Min." % (b["slug"], woerter(b), lesezeit(b)))
