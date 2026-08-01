# Design System: Energie Studio

Kompletter Neuentwurf, 27.07.2026. Ersetzt den Vorgänger vollständig — andere Struktur, andere Bildsprache, andere Farbstrategie.

---

## Stilvorgabe des Kunden (Stand 27.07., abends)

Auftraggeber hat zwei Screens geliefert (Projekte-Section dunkel, Team-Section hell). Sie sind **verbindlich** und gehen jeder Regel weiter unten vor. Die Merkmale, die auf die ganze Seite gespiegelt werden:

| Merkmal | Umsetzung |
|---|---|
| **Feste Seitenleiste links** | `--rail: 15rem`, Logo oben, nummerierte Kapitel 01–05, „Menü" unten. Aktives Kapitel in Teal mit einfahrendem Strich. Unter 960px klappt sie zur oberen Leiste um. |
| **Kapitel statt Sektionen** | Fünf Kapitel: 01 Leistungen · 02 Projekte · 03 Team · 04 Wissen · 05 Kontakt. Zähler `03 / 05` vertikal am rechten Rand. |
| **Teal-Punkt als Signatur** | Jede Sektions-Headline endet auf `<span class="dot">.</span>` in Teal. Nur der Punkt ist farbig, nie das Wort. |
| **Kicker mit Strich** | `— UNSERE PROJEKTE`: Mono-Versalien in Teal, davor ein 2.25rem-Strich. Das ist die **einzige** erlaubte Eyebrow-Form. |
| **Wechsel dunkel/hell** | Kapitel wechseln zwischen `--deep #080d0b` und `--off #f1f1ef`. Die Seitenleiste kippt beim Scrollen mit, ebenso `theme-color`. |
| **Blaupause im Hintergrund** | Technische Konstruktionszeichnung als Inline-SVG in dunklen Kapiteln. Links per Maske ausgeblendet, damit sie nicht durch den Text läuft. |
| **Karten mit Glow** | Radius `.625rem`, aktive/gehoverte Karte bekommt Teal-Rahmen plus doppelten Schein. Kreis-Pfeil unten rechts. |
| **Team als Schieber** | Vier Portraits randlos aneinander, Overlay unten mit Name (Teal-Mono) + Rolle + Plus. Darunter Fortschrittsbalken und zwei runde Pfeilknöpfe. |
| **Fettere Displays** | Gewicht **800** statt 600, Zeilenhöhe `.95`, Laufweite `-.025em`. |

Der frühere heller Grundton und die Regel „Radius 0" sind damit **überholt**. Was bleibt: Farben und Schriften des CD, die Kontrastgrenzen und das Verbot einer vierten Farbe.

---

## 0. Reference-Lock

Recherche in der Branche Technologie + Umwelt. Fünf Seiten technisch ausgelesen (Schriften, Motion-Bibliotheken, Farbwerte direkt aus dem Quelltext).

| Seite | Branche | Schriften | Motion | Ink | Fläche | Akzent |
|---|---|---|---|---|---|---|
| **passivelogic.com** | Gebäudeautomation | Inter + Fragment Mono | Lenis | `#1a1615` | `#f9f8f8` | `#168804` |
| basepowercompany.com | Energieversorgung | — | — | `#292826` | — | `#1e4d2b` |
| sensiq.co | Sensorik | — | — | `#5f5a50` | `#e7e6e4` | `#cfc500` |
| formenergy.com | Energiespeicher | Roboto + Roboto Mono | Swiper | — | — | `#faaf40` |
| zetta-joule.com | Kernenergie | Geist | GSAP | — | — | — |

**Das gemeinsame Muster:** warmes Fast-Schwarz statt reinem Schwarz · Off-White statt Weiss · Grotesk + Mono als Paar · genau **ein** gesättigter Akzent · Lenis/GSAP für den Scroll.

**Leitreferenz: PassiveLogic.** Nicht wegen der Optik, sondern weil es dieselbe Branche ist (Gebäudeautomation) und exakt dieselbe CD-Struktur fährt, die Energie Studio bereits besitzt: Grotesk + Mono, warmes Ink, ein grüner Akzent.

**Bewahren:** Ink/Off-White/ein Akzent · Grotesk + Mono mit klar getrennten Rollen · Lenis-Scroll · Kennzahlen als Beweis statt als Deko.
**Nur übernommen:** von *Base Power* die Farbstrategie „Committed" — der Akzent trägt ganze Sektionsflächen, statt nur Striche zu setzen. Von *Form Energy* die grossformatige Industriefotografie als eigene Sektion.
**Verworfen:** sensiqs Akzent-Dominanz (Teal ist gedeckter als Acid-Gelb) · zetta-joules dünne, gemischt geschriebene Riesen-Headlines — die widersprechen der Header-Vorlage des Kunden.

---

## 1. Verbindliche Kundenvorgabe

Nicht verhandelbar, geht jeder Design-Regel vor.

**Header** nach `Screen Design/header1.png`: Versalien-Headline über drei Zeilen, dritte Zeile in Teal · Gebäude gross rechts · drei Merkmale als schmale Spalte rechts aussen · zwei Buttons (gefüllt + Outline) · Navigation in Versalien mit Outline-CTA.

**Farben** — ausschliesslich aus den Logo-SVGs:

| Wert | Rolle |
|---|---|
| `#1A1A1A` | Ink. Text, dunkle Sektionsflächen |
| `#50BAA0` | Teal. Der einzige Akzent — CTA, Kennzahlen, Systemlinien, Zahlen-Sektion als Fläche |
| `#FFFFFF` | Weiss. Grundfläche |

Abgeleitet werden nur Helligkeitsstufen derselben drei Werte (Off-White `#F7F8F8`, Nebel `#EDF0EF`, Linie `#DDE3E1`, Fliesstext `#5A6764`, Teal dunkel `#2B8067` für Text auf Weiss). **Keine vierte Farbe.**

**Schriften** — aus der Firmenpräsentation ausgelesen (eingebettete Fonts):

| Schrift | Schnitte | Rolle |
|---|---|---|
| **Inter** | 300 / 400 / 500 / 600 | Alles Sichtbare: Displays, Titel, Fliesstext, Navigation |
| **Overpass Mono** | 400 / 500 | Ausschliesslich Messgrössen und Kennwerte: `18 MW`, `90'000 m²`, `CHF 2 Mio.`, Zonenmarker am Gebäudeschnitt |

Overpass Mono ist **nicht** dekorativ und steht **nie** als Eyebrow über einer Sektion. Es markiert technische Grössen — das ist seine einzige Rolle.

---

## 2. Atmosphäre

Nüchtern, technisch, hell. Ein Planungsbüro, kein Lifestyle-Anbieter. Die Seite wirkt wie ein sauber gezeichneter Gebäudeschnitt: viel Weissraum, harte Kanten, dünne Linien, keine weichen Schatten. Wärme entsteht durch das Teal und durch echte Baustellenfotografie, nicht durch runde Ecken.

Radius durchgehend **0**. Eine einzige Ausnahme: der Icon-Kreis in den Hero-Merkmalen (`50%`), weil er ein Symbolträger ist.

---

## 3. Typografie

| Stufe | Grösse (fluid) | Schnitt | Zeilenhöhe | Laufweite | Schreibweise |
|---|---|---|---|---|---|
| Display | `clamp(2.8rem, 6vw, 5.5rem)` | 600 | 1.02 | −0.02em | VERSALIEN |
| Sektionstitel | `clamp(2rem, 3.6vw, 3.4rem)` | 600 | 1.06 | −0.015em | VERSALIEN |
| Untertitel | `clamp(1.25rem, 1.8vw, 1.7rem)` | 500 | 1.2 | −0.01em | Gemischt |
| Lead | `clamp(1.05rem, 1.2vw, 1.2rem)` | 400 | 1.6 | 0 | Gemischt |
| Fliesstext | `1rem` | 400 | 1.65 | 0 | Gemischt |
| Kennwert | `0.8rem` | Mono 500 | 1 | 0.06em | VERSALIEN |
| Navigation | `0.82rem` | 500 | 1 | 0.09em | VERSALIEN |

Display-Ceiling 5.5rem (88px) — unter der 6rem-Grenze. Fliesstext maximal 68ch. `text-wrap: balance` auf allen Titeln, `pretty` auf Lead-Absätzen.

---

## 4. Farbstrategie: Committed

Der Akzent trägt Fläche, nicht nur Striche. Sektionsrhythmus hell → dunkel → Teal → hell:

1. Hero — Weiss mit zartem Teal-Verlauf
2. Positionierung — Off-White
3. **Gebäudeschnitt — Ink `#1A1A1A`**, Systemlinien in Teal
4. **Kennzahlen — Teal `#50BAA0` als Vollfläche**, Text in Ink
5. Projekte — Weiss, grosse Fotos
6. Ablauf — Off-White
7. Team & Standorte — Weiss
8. Wissen — Off-White
9. **Kontakt — Ink**

Kontrast nachgerechnet: Ink auf Teal 7.35:1 · Fliesstext `#5A6764` auf Weiss 5.90:1 · Teal-dunkel `#2B8067` auf Weiss 4.79:1 · Label auf Teal-Fläche 4.79:1. Alle über WCAG AA (4.5:1). Weisser Text auf Teal wäre 2.2:1 und ist **verboten** — auf Teal-Flächen steht immer Ink.

---

## 5. Der zentrale Move

**Der Gebäudeschnitt.** Eine gezeichnete Schnittansicht durch ein Gebäude, als SVG in Code gezeichnet — keine Bilddatei. Vier Zonen von oben nach unten, die genau dort sitzen, wo die Technik im echten Gebäude liegt:

| Zone | Höhe | Gewerk |
|---|---|---|
| Dach | oben | Photovoltaik, Lüftungszentrale |
| Geschosse | Mitte oben | Lüftung & Klima |
| Steigzonen | Mitte unten | Sanitär |
| Technikzentrale & Untergrund | unten | Heizung, Kälte, Erdsonden |

Beim Scrollen wandert die aktive Zone von oben nach unten durch das Gebäude — genau die ursprüngliche Idee (Solar oben, Leitungen unten), nur ohne Video gelöst. Gebäudeautomation liegt als Systemebene darüber und verbindet alle vier.

Das ist der eine Moment, den man sich merkt. Alles andere ordnet sich unter.

---

## 6. Komponenten

* **Buttons** — Rechteckig, kein Radius. Primär: Teal-Fläche, Ink-Text, Hover dunkler. Sekundär: 1px Ink-Rahmen, transparent, Hover Ink-Fläche mit weissem Text. Aktiv `scale(.98)`, 90ms.
* **Container** — Keine Karten. Gruppiert wird über Linien (`1px #DDE3E1`), Weissraum und Rasterspalten. Karten nur, wo geklickt wird (Projekt-Kacheln, Wissens-Beiträge).
* **Bilder** — Randlos, kein Radius, `object-fit: cover`, fixes Seitenverhältnis. Hover: `scale(1.03)` über 600ms.
* **Linien** — 1px, `#DDE3E1` auf hell, `rgba(255,255,255,.14)` auf dunkel. Systemlinien im Gebäudeschnitt in Teal.

## 7. Layout

Container 1320px, Seitenrand `clamp(1.25rem, 4vw, 3.5rem)`. Sektionsabstand `clamp(5rem, 9vw, 9rem)`, variiert bewusst — Kennzahlen und Gebäudeschnitt sitzen enger, Projekte und Kontakt weiter.
12-Spalten-Raster auf Desktop, asymmetrisch genutzt (7/5, 8/4), nicht 6/6. Ab 900px einspaltig.

## 8. Motion

Ein Token `--motion` (1 oder 0), unter `prefers-reduced-motion` auf 0 — jede Dauer wird damit multipliziert.

| Vorgang | Dauer | Kurve |
|---|---|---|
| Hover, Fokus | 140ms | `cubic-bezier(.2,0,0,1)` |
| Zustandswechsel | 260ms | `cubic-bezier(.4,0,.2,1)` |
| Eintritt, Reveal | 700ms | `cubic-bezier(.16,1,.3,1)` |
| Gebäudeschnitt-Zone | 500ms | `cubic-bezier(.16,1,.3,1)` |

Lenis für den Scroll (`lerp .1`, `wheelMultiplier .8`), GSAP ScrollTrigger für Reveals und die Zonensteuerung. Inhalte sind ohne JavaScript sichtbar — Reveals verbessern nur, sie schalten nichts frei.

## 9. Verbote

Keine Eyebrow-Labels über Sektionen · keine Nummerierung ausser bei der echten SIA-Phasenfolge · keine Karten als Standard-Container · keine Farbverläufe im Text · kein Glas-Effekt · keine Seitenstreifen an Elementen · kein reines Schwarz oder reines Weiss als Textfarbe · keine vierte Farbe · Mono niemals als Fliesstext oder Sektionslabel.
