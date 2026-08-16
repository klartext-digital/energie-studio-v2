# -*- coding: utf-8 -*-
"""Referenzliste — die einzige Quelle für Projekte auf beiden Seiten.

Stand: Referenzliste vom 14.08.2026. Alle früheren Einträge sind ersetzt.
Es stehen ausschliesslich die gelieferten Angaben darin: keine erfundenen
Beschreibungen, keine geschätzten Zahlen, keine ausgeschriebenen Kürzel.
Wer eine Referenz ergänzt, trägt sie hier ein und lässt die Seiten neu bauen.
"""

# name, kategorie, fachgebiete, leistungen, bauherr, auftraggeber, zeit
REFERENZEN = [
    ("PUK LEN — Wärmeerzeugung EWS",
     "Spitalbauten", "HK", "Planung Phase 21–41", "PUK", "PUK", "2026–2027"),

    ("BAZ Duttweilerstrasse — Erneuerung Heizzentrale",
     "Bundesbauten", "HK", "Planung Phase 21–53", "AHB", "Bund", "2025–2026"),

    ("TE Connectivity Ltd. Schaffhausen — Büroerweiterung 2. OG",
     "Büro", "HLKS", "Planung Phase 21–53", "TE Connectivity Ltd.", "SAD Architekten", "2024–2025"),

    ("Stiftung Schürmatt — Ersatz Heizungsanlage",
     "Arealplanung", "HK", "Planung Phase 21–53", "Stiftung Schürmatt", "Stiftung Schürmatt", "2025–2027"),

    ("ON Zürich — Büroausbau 5. OG",
     "Büro", "HLKS", "Planung Phase 21–53", "ON Zürich", "SAD Architekten", "2024"),

    ("PUK Rheinau — dezentrale Warmwasserbereitung",
     "Arealplanung", "HLKS", "Planung Phase 21–53", "PUK", "PUK", "2022–2025"),

    ("DHL Erlensee",
     "Logistik", "HLKS", "Planung Phase 21–53", "DHL", "DHL", "2022"),

    ("PUK LEN — Sanierung Trakt A/B und MB",
     "Spitalbauten", "HK", "Planung Phase 21–53", "PUK", "PUK", "2026–2027"),

    ("PUK Männedorf — Ersatz Heizungsanlage",
     "Arealplanung", "HLKS", "Planung Phase 21–53", "PUK", "PUK", "2024–2026"),

    ("Rheinmetall — Stickstoffanlage",
     "Industrie", "Gase", "Planung Phase 21–41", "RAD", "RAD", "2026"),

    ("Flughafen Frankfurt",
     "Flughafen", "HLK", "Energetische Inspektion, §12 EnEV",
     "Flughafen Frankfurt", "Flughafen Frankfurt", "2022"),
]

# Kleinere Mandate: nur Name und Fachbereich.
WEITERE = [
    "PUK Medikamentenkühlungen — Rheinau, Zürich, Männedorf",
    "Neugutstrasse Adliswil",
    "PUK Neumünsterallee — Ersatz Heizungsanlage",
    "PUK Heliosstrasse — Ersatz Heizungsanlage",
    "Römerweg Embrach — Pilotplanung HLK und Umplanung",
    "PUK Lengg — Dezentralisierung Warmwasserbereitung",
    "Hofackerstrasse Zürich — Ersatz Heizungsanlage",
    "LFS Lebach",
    "Nettomarkt Fechingen",
    "Rewe Markt Wiesloch",
    "Rewe Markt Worms",
    "EFH Reisenhofer",
    "Meiser Solar",
    "Rewe Markt Schmelz",
    "Wohnhaus Wald",
]

# Diese sechs stehen als Auswahl auf der Startseite (Reihenfolge = Anzeige).
STARTSEITE = [0, 1, 2, 6, 10, 5]

# Bilder sind allgemeine Aufnahmen aus der Gebaeudetechnik, keine
# Projektfotos — deshalb beschreiben die Alternativtexte nur, was zu sehen
# ist, und behaupten keinen Projektbezug.
BILDER = [
    ("assets/img/technik-1.webp", "Technikzentrale mit Verteilern und Rohrleitungen"),
    ("assets/img/bau-3.webp",     "Montagearbeiten an einer haustechnischen Anlage"),
    ("assets/img/technik-3.webp", "Lüftungsgerät in einer Technikzentrale"),
    ("assets/img/bau-1.webp",     "Rohrleitungen im Rohbau"),
    ("assets/img/technik-5.webp", "Schaltschrank einer Gebäudeautomation"),
    ("assets/img/technik-2.webp", "Pumpengruppe mit Absperrarmaturen"),
]


def _feld(bez, wert):
    return ('<li><span class="kenn k">%s</span><span class="v">%s</span></li>' % (bez, wert))


def referenzliste(einzug="    "):
    """Alle elf Referenzen für die Projektseite."""
    aus = []
    for i, (name, kat, fach, leist, bauherr, auftrag, zeit) in enumerate(REFERENZEN):
        bild, alt = BILDER[i % len(BILDER)]
        felder = "\n".join(einzug + "          " + _feld(b, w) for b, w in [
            ("Fachgebiete", fach),
            ("Leistungen", leist),
            ("Bauherr", bauherr),
            ("Auftraggeber", auftrag),
            ("Realisierung", zeit),
        ])
        aus.append(
'''%(e)s<article class="case">
%(e)s  <div class="case__media"><img src="%(bild)s" alt="%(alt)s" loading="lazy" decoding="async"></div>
%(e)s  <div>
%(e)s    <span class="kenn" style="color:var(--teal-ink);display:block;margin-bottom:.7rem">%(kat)s</span>
%(e)s    <h2>%(name)s</h2>
%(e)s    <ul class="specs">
%(felder)s
%(e)s    </ul>
%(e)s  </div>
%(e)s</article>''' % {"e": einzug, "bild": bild, "alt": alt, "kat": kat,
                      "name": name, "felder": felder})
    return "\n\n".join(aus)


def weitere_liste(einzug="      "):
    return "\n".join(
        '%s<li><span class="nm">%s</span><span class="kenn tg">Gebäudetechnik</span></li>'
        % (einzug, n) for n in WEITERE)


def startkarten(einzug="      "):
    """Sechs Karten für den Schieber auf der Startseite."""
    pfeil = ('<span class="karte__go" aria-hidden="true"><svg width="18" height="12" '
             'viewBox="0 0 18 12" fill="none"><path d="M0 6h16M11 1l5 5-5 5" '
             'stroke="currentColor" stroke-width="1.4"/></svg></span>')
    aus = []
    for platz, i in enumerate(STARTSEITE):
        name, kat, fach, leist, bauherr, auftrag, zeit = REFERENZEN[i]
        bild, alt = BILDER[platz % len(BILDER)]
        aus.append(
'''%(e)s<a class="karte" href="projekte.html">
%(e)s  <div class="karte__media"><img src="%(bild)s" alt="%(alt)s" loading="lazy" decoding="async"></div>
%(e)s  <div class="karte__body">
%(e)s    <span class="kenn karte__cat">%(kat)s</span>
%(e)s    <h3>%(name)s</h3>
%(e)s    <span class="kenn karte__meta">%(fach)s · %(zeit)s</span>
%(e)s    %(pfeil)s
%(e)s  </div>
%(e)s</a>''' % {"e": einzug, "bild": bild, "alt": alt, "kat": kat,
                "name": name, "fach": fach, "zeit": zeit, "pfeil": pfeil})
    return "\n".join(aus)
