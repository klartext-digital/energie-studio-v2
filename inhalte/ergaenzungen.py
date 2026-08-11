# -*- coding: utf-8 -*-
"""Zusaetzliche Abschnitte je Beitrag.

Getrennt gehalten, damit beitraege.py lesbar bleibt. Der Generator haengt
diese Bloecke an den jeweiligen Beitrag an.
"""

ERGAENZUNG = {

"hydraulischer-abgleich": [
  ("h2", "Was ein Abgleich kostet und wann er sich rechnet"),
  ("p", "Der Aufwand besteht aus zwei Teilen: der Berechnung und der Umsetzung. Die Berechnung braucht eine Bestandsaufnahme — Raumgeometrie, Heizkörpertypen und -grössen, Rohrnetz. Bei vorhandenen Plänen geht das schnell, bei einem Bau ohne brauchbare Unterlagen ist die Aufnahme der grössere Posten."),
  ("p", "Die Umsetzung hängt daran, ob die vorhandenen Ventile überhaupt voreinstellbar sind. Ältere Thermostatventile sind es oft nicht — dann kommt der Ventiltausch dazu. Das ist der Punkt, an dem aus einer kleinen eine mittlere Massnahme wird, und er sollte vor der Offerte geklärt sein, nicht danach."),
  ("p", "Gerechnet über die Lebensdauer ist der Abgleich in fast allen Fällen die Massnahme mit der kürzesten Amortisationszeit im ganzen Gebäude. Das gilt besonders dort, wo die Vorlauftemperatur anschliessend dauerhaft gesenkt werden kann."),

  ("h2", "Der Sonderfall Fussbodenheizung"),
  ("p", "Bei Flächenheizungen ist der Abgleich technisch einfacher und wirtschaftlich oft noch lohnender. Die Kreise haben sehr unterschiedliche Längen, und ohne Abgleich bekommt der kurze Kreis den grössten Teil des Wassers. Die Folge sind Räume mit spürbar unterschiedlicher Temperatur bei identischer Einstellung."),
  ("p", "Moderne Verteiler haben Durchflussmesser, an denen sich der Sollwert direkt einstellen lässt. Der Abgleich ist dann eine Sache von Stunden — vorausgesetzt, jemand hat vorher die nötigen Durchflüsse gerechnet. Ohne diese Rechnung werden die Messer nur auf identische Werte gestellt, was das Problem nicht löst, sondern zementiert."),

  ("h2", "Zusammengefasst"),
  ("ul", [
    "Der Abgleich ist die Voraussetzung dafür, dass eine tiefe Vorlauftemperatur überhaupt möglich wird.",
    "Ohne Protokoll gilt eine Anlage als nicht abgeglichen.",
    "Nach jeder baulichen Verbesserung der Hülle muss neu gerechnet werden.",
    "Pumpe und Heizkurve gehören zwingend dazu, sonst bleibt der halbe Effekt liegen.",
    "Eine Kontrolle nach der ersten Heizperiode sichert das Ergebnis.",
  ]),
],

"waermepumpe-im-bestand": [
  ("h2", "Die Rolle des Speichers"),
  ("p", "Ein Pufferspeicher entkoppelt Erzeugung und Verteilung und verhindert, dass die Wärmepumpe bei kleiner Last ständig ein- und ausschaltet. Zu gross darf er trotzdem nicht sein: Jeder Liter Speicher hat Verluste, und ein überdimensionierter Puffer senkt die Systemtemperatur langsamer, als die Regelung es gern hätte."),
  ("p", "Ob überhaupt ein Puffer nötig ist, hängt vom Verteilsystem ab. Eine Fussbodenheizung mit viel Estrichmasse bringt ihre eigene Trägheit mit und braucht oft keinen zusätzlichen Speicher. Ein Radiatorennetz mit vielen Thermostatventilen, die gleichzeitig schliessen, braucht ihn dagegen fast immer — sonst fehlt der Wärmepumpe die Abnahme."),

  ("h2", "Was der Stromtarif ändert"),
  ("p", "Wärmepumpen werden von vielen Energieversorgern über einen eigenen Tarif abgerechnet, teilweise verbunden mit Sperrzeiten, in denen der Verdichter nicht laufen darf. Diese Sperrzeiten müssen bei der Auslegung berücksichtigt sein — sie erhöhen die nötige Leistung und den Speicherbedarf."),
  ("p", "Es lohnt sich, die tatsächlichen Tarifbedingungen des örtlichen Versorgers vor der Dimensionierung zu klären. Sie unterscheiden sich stark und beeinflussen sowohl die Gerätegrösse als auch die Betriebskosten spürbar."),

  ("h2", "Der Übergang: Sanierung in Etappen"),
  ("p", "Nicht jedes Gebäude lässt sich in einem Zug ertüchtigen. Wer in Etappen vorgeht, sollte die Wärmepumpe auf den Zustand nach der Sanierung auslegen und für die Übergangszeit eine Zusatzheizung vorsehen — nicht umgekehrt. Eine grosse Wärmepumpe, die nach der Dämmung dauerhaft im Teillastbetrieb läuft, ist der teurere Fehler."),
  ("ul", [
    "Zielzustand definieren, danach dimensionieren.",
    "Übergangslösung für die Spitzenlast einplanen, zeitlich befristet.",
    "Heizflächen bereits im ersten Schritt auf die Zieltemperatur auslegen.",
    "Hydraulischen Abgleich nach jeder Etappe wiederholen.",
  ]),
],

"lueftung-sia-382": [
  ("h2", "Feuchte: die vergessene Grösse"),
  ("p", "Im Winter ist die Aussenluft trocken. Wird sie erwärmt, sinkt die relative Feuchte weiter — in gut gelüfteten Gebäuden regelmässig unter zwanzig Prozent. Das ist der häufigste Beschwerdegrund in Bürobauten mit mechanischer Lüftung, und er lässt sich nicht wegregeln, sondern nur durch die Auslegung vermeiden."),
  ("p", "Die wirksamste Massnahme ist die bedarfsgeführte Regelung: Wer nur so viel Aussenluft einbringt, wie tatsächlich nötig ist, trocknet die Räume weniger aus. Eine aktive Befeuchtung ist die aufwendigere Lösung — sie kostet Energie, Wasseraufbereitung und Hygieneaufwand und sollte erst geprüft werden, wenn die Luftmengen bereits bedarfsgerecht sind."),

  ("h2", "Schall aus der Lüftung"),
  ("p", "Lüftungsgeräusche werden selten in der Planung, aber regelmässig im Betrieb zum Thema. Die Ursachen sind fast immer dieselben: zu hohe Luftgeschwindigkeiten in den Kanälen, fehlende Schalldämpfer in Nebenwegen, oder Übersprechen zwischen Räumen über gemeinsame Kanäle."),
  ("p", "Der dritte Punkt ist in Bürobauten der unangenehmste, weil er die Vertraulichkeit betrifft. Telefonkabinen und Besprechungsräume brauchen deshalb eigene Anschlüsse oder Schalldämpfer im Abzweig — eine Massnahme, die in der Planung wenig kostet und nachträglich kaum umsetzbar ist."),

  ("h2", "Zusammengefasst"),
  ("ul", [
    "Die Auslegung folgt der realen Nutzung, nicht dem Standardwert.",
    "Die Dichtheitsprüfung gehört in die Bauzeit, nicht in die Abnahme.",
    "Zugänglichkeit entscheidet darüber, ob die Anlage je gewartet wird.",
    "Bedarfsführung raumweise entscheiden, nicht pauschal.",
    "Eine Nachmessung nach einem Jahr deckt auf, was die Abnahme nicht zeigt.",
  ]),
],

"trinkwasser-legionellen": [
  ("h2", "Dämmung ist Hygiene"),
  ("p", "Die Dämmung der Trinkwasserleitungen wird gern als Energiethema behandelt. Sie ist vor allem ein Hygienethema. Ungedämmte Kaltwasserleitungen in warmen Schächten erreichen im Sommer Temperaturen, die im kritischen Bereich liegen — und zwar über Stunden, jeden Tag."),
  ("p", "Die Trennung von warm- und kaltführenden Leitungen im Schacht ist deshalb keine Detailfrage, sondern eine Grundsatzentscheidung der Planung. Wo sie räumlich nicht möglich ist, braucht es eine erhöhte Dämmstärke auf der Kaltseite und den Nachweis, dass die Temperatur eingehalten wird."),

  ("h2", "Was bei Leerstand passiert"),
  ("p", "Leerstehende Wohnungen, geschlossene Gebäudeteile, saisonal genutzte Bauten: In all diesen Fällen steht Wasser über Wochen. Ein Spülplan allein reicht dann oft nicht, weil er in der Praxis nicht eingehalten wird. Wirksamer sind automatische Spüleinrichtungen an den kritischen Endsträngen — sie kosten wenig und arbeiten unabhängig von der Organisation."),
  ("p", "Wichtig ist, den Leerstand als Planungsfall zu behandeln und nicht als Ausnahme. In Wohnbauten mit Mieterwechsel ist er der Normalfall."),

  ("h2", "Wenn doch etwas gefunden wird"),
  ("p", "Ein positiver Befund ist kein Grund für Aktionismus. Sinnvoll ist ein strukturiertes Vorgehen: erst die Verteilung der Befunde im Netz erfassen, dann die Ursache eingrenzen — Temperatur, Stagnation oder Ablagerung — und erst dann Massnahmen ergreifen."),
  ("p", "Thermische Desinfektionen sind wirksam gegen die Symptome, aber wirkungslos gegen die Ursache. Wo die Ursache eine Totleitung oder ein kalter Zirkulationsstrang ist, kommt der Befund nach jeder Desinfektion zuverlässig zurück. Die Suche nach der Ursache ist deshalb die günstigere Investition — auch wenn sie mehr Aufwand macht als eine Aufheizung."),
],

"gebaeudeautomation-nachruesten": [
  ("h2", "Störmeldungen, die niemand mehr liest"),
  ("p", "In vielen Bestandsanlagen laufen dauerhaft Dutzende Störmeldungen auf. Sie werden quittiert, weil die Anlage trotzdem funktioniert, und irgendwann schaut niemand mehr hin. Eine echte Störung geht in diesem Rauschen unter."),
  ("p", "Die Bereinigung der Meldungen gehört deshalb zu jeder GA-Sanierung: Jede Meldung braucht eine Priorität, einen Empfänger und eine definierte Reaktion. Meldungen ohne diese drei Angaben gehören abgeschaltet — eine Meldung, auf die niemand reagiert, ist schlimmer als keine."),

  ("h2", "Fernzugriff und Sicherheit"),
  ("p", "Fernzugriff spart Wege und verkürzt Reaktionszeiten. Er öffnet aber auch einen Weg ins Gebäude. Eine Automationsanlage, die ohne Absicherung am Internet hängt, ist ein reales Risiko — und zwar nicht nur für die Anlage, sondern über das Netzwerk auch für alles andere im Haus."),
  ("ul", [
    "Getrenntes Netz für die Gebäudeautomation, nicht dasselbe wie für die Büro-IT.",
    "Zugriff nur über gesicherte Verbindung, mit persönlichen Konten statt Sammelpasswort.",
    "Dokumentierte Liste aller Zugänge, inklusive der Fernwartung von Lieferanten.",
    "Regelung, was beim Ausscheiden eines Dienstleisters mit dessen Zugang geschieht.",
  ]),
  ("p", "Der letzte Punkt wird fast immer vergessen. In vielen Gebäuden haben ehemalige Lieferanten noch Jahre nach Vertragsende funktionierende Zugänge."),

  ("h2", "Zusammengefasst"),
  ("ul", [
    "Die Bestandsaufnahme der Datenpunkte steht vor jedem Angebot.",
    "Offene Protokolle und der Zugriff auf die eigenen Daten gehören in den Vertrag.",
    "Migration zonenweise, mit getesteter Rückfallebene.",
    "Störmeldungen bereinigen, sonst bleibt das System blind.",
    "Nachschau nach der ersten Heiz- und Kühlperiode vertraglich sichern.",
  ]),
],

"betriebsoptimierung": [
  ("h2", "Wer sie durchführt"),
  ("p", "Eine Betriebsoptimierung ist keine Wartung und keine Störungsbehebung. Sie braucht jemanden, der die Anlage als System versteht und die Daten lesen kann — und der nicht identisch ist mit demjenigen, der die Anlage gebaut hat. Diese Unabhängigkeit ist kein Misstrauen, sondern methodisch sinnvoll: Wer eine Regelstrategie entworfen hat, prüft sie schwerer ergebnisoffen."),
  ("p", "Der Aufwand liegt typischerweise bei wenigen Tagen je Durchgang, verteilt auf Datenauswertung, Begehung und Umsetzung. Er sollte als eigene Position im Budget stehen, nicht im Wartungsvertrag verschwinden."),

  ("h2", "Typische Funde"),
  ("ul", [
    "Lüftungsanlagen, die an Wochenenden und Feiertagen weiterlaufen.",
    "Heizkurven, die nie an die tatsächliche Gebäudereaktion angepasst wurden.",
    "Nachheizregister, die gegen eine zu tief geregelte Zulufttemperatur arbeiten.",
    "Pumpen auf konstanter Kennlinie statt geregelt.",
    "Frostschutzschaltungen, die dauerhaft aktiv sind.",
    "Einzelraumregler, die von Nutzern übersteuert und nie zurückgesetzt wurden.",
    "Sommer- und Winterbetrieb, die manuell umgeschaltet werden müssten und es nicht werden.",
  ]),
  ("p", "Auffällig ist, wie wenige dieser Funde eine Investition erfordern. Die meisten sind Einstellungen — und genau deshalb ist die Betriebsoptimierung wirtschaftlich so attraktiv."),

  ("h2", "Der Unterschied zur Wartung"),
  ("p", "Wartung hält den Zustand. Optimierung verbessert ihn. Ein Wartungsvertrag sorgt dafür, dass Filter gewechselt und Verschleissteile ersetzt werden; er sorgt nicht dafür, dass die Regelung zur Nutzung passt. Beide Leistungen sind nötig, und sie sollten getrennt beauftragt und getrennt beurteilt werden."),
  ("p", "Wo beides im selben Vertrag steckt, verschwindet die Optimierung erfahrungsgemäss zugunsten der Wartung — sie ist weniger dringend und schwerer zu belegen."),
],

"free-cooling": [
  ("h2", "Der Rückkühler bestimmt den Standort"),
  ("p", "Freie Kühlung braucht Fläche im Freien, und diese Fläche ist auf Dächern regelmässig knapp — zumal sie mit Photovoltaik konkurriert. Die Entscheidung, wie viel Dachfläche wofür reserviert wird, fällt früh und ist später kaum revidierbar."),
  ("p", "Dazu kommen Gewicht, Schall und die Zugänglichkeit für die Reinigung. Verschmutzte Rückkühler verlieren spürbar an Leistung, und ein Gerät, das nur mit Hubsteiger erreichbar ist, wird selten gereinigt."),

  ("h2", "Hybride Rückkühler und der Wasserverbrauch"),
  ("p", "Adiabate oder hybride Rückkühler verbessern die Leistung bei hohen Aussentemperaturen durch Verdunstung. Sie erweitern damit das Fenster für freie Kühlung und senken die Spitzenlast der Kältemaschine — kosten aber Wasser und bringen zusätzliche Hygieneanforderungen mit sich."),
  ("p", "Ob das sinnvoll ist, hängt vom Standort und von der Lastkurve ab. Wo Kühlung vor allem an wenigen heissen Tagen gebraucht wird, kann die Verdunstungskühlung die Auslegung der Kältemaschine deutlich entlasten. Wo ganzjährig gekühlt wird, spielt sie eine kleinere Rolle."),

  ("h2", "Zusammengefasst"),
  ("ul", [
    "Die zulässige Kaltwassertemperatur entscheidet über das gesamte Konzept.",
    "Freie Kühlung braucht Kühlbedarf in der kalten Jahreszeit, sonst läuft sie ins Leere.",
    "Übergabeflächen und Kaltwassertemperatur gehören zusammen geplant.",
    "Der Zusatzstrom für Rückkühler und Pumpen gehört in die Rechnung.",
    "Nachtauskühlung ist oft die günstigere Alternative — wenn Speichermasse vorhanden ist.",
  ]),
],

"foerdergelder-reihenfolge": [
  ("h2", "Was in ein vollständiges Gesuch gehört"),
  ("p", "Die Anforderungen unterscheiden sich je Kanton und Massnahme, aber der Kern ist meist derselbe. Wer diese Unterlagen früh zusammenstellt, verliert keine Zeit in der Bearbeitung:"),
  ("ul", [
    "Angaben zum Gebäude: Adresse, Baujahr, Energiebezugsfläche, bisheriges Heizsystem.",
    "Beschreibung der geplanten Massnahme mit technischen Daten.",
    "Offerte oder Kostenschätzung.",
    "Je nach Programm ein GEAK oder GEAK Plus.",
    "Nachweis der Eigentümerschaft und Zustimmung bei Stockwerkeigentum.",
    "Bestätigung, dass mit den Arbeiten noch nicht begonnen wurde.",
  ]),
  ("p", "Bei Stockwerkeigentum ist der fünfte Punkt der zeitkritische. Ein Beschluss der Eigentümerversammlung braucht Vorlauf, und ohne ihn steht das Gesuch still. Diese Frist gehört als Erstes in den Terminplan."),

  ("h2", "Der Unterschied zwischen Zusicherung und Auszahlung"),
  ("p", "Die Zusicherung ist eine Reservation, keine Zahlung. Sie ist befristet — wer die Massnahme nicht innerhalb der gesetzten Frist ausführt und abrechnet, verliert sie. Diese Frist ist grosszügig bemessen, aber sie ist real, und bei Projekten mit Verzögerungen wird sie gelegentlich knapp."),
  ("p", "Für die Liquiditätsplanung heisst das: Die Massnahme muss vollständig vorfinanziert werden. Die Auszahlung erfolgt erst nach Abschluss und Prüfung — je nach Kanton und Auslastung mit spürbarem zeitlichem Abstand."),

  ("h2", "Zusammengefasst"),
  ("ul", [
    "Gesuch vor der Bestellung, nicht vor dem Spatenstich.",
    "Kantonale Bedingungen tagesaktuell prüfen, nicht aus zweiter Hand.",
    "Vorleistungen wie den GEAK Plus früh anstossen.",
    "Bei Stockwerkeigentum den Beschluss als Erstes terminieren.",
    "Belege während der Bauzeit sammeln, nicht danach suchen.",
    "Förderprüfung in die Vorstudie legen — sie beeinflusst die Variantenwahl.",
  ]),
],

"geak-minergie-snbs": [
  ("h2", "Was Labels für die Finanzierung bedeuten"),
  ("p", "Über den energetischen Nutzen hinaus haben Labels eine wirtschaftliche Seite. Mehrere Banken bieten für zertifizierte Bauten günstigere Hypothekarkonditionen an, und institutionelle Investoren verlangen bei Ankäufen zunehmend einen Nachweis der energetischen Qualität."),
  ("p", "Für Eigentümer, die mittelfristig verkaufen oder refinanzieren wollen, ist das ein Argument, das über die Betriebskosten hinausgeht. Es lohnt sich, die Konditionen vor der Entscheidung abzuklären — die Unterschiede sind je nach Anbieter erheblich."),

  ("h2", "Zertifizierung ist ein Prozess, kein Dokument"),
  ("p", "Bei Minergie und SNBS begleitet die Zertifizierung das Projekt von der Eingabe bis zur Bestätigung nach Fertigstellung. Zwischenprüfungen, Messungen und Nachweise fallen zu definierten Zeitpunkten an. Wer das erst in der Ausführung bemerkt, hat ein Terminproblem."),
  ("ul", [
    "Provisorische Zertifizierung auf Basis der Projektunterlagen.",
    "Nachweise während der Ausführung, etwa die Luftdichtheitsmessung.",
    "Definitive Zertifizierung nach Fertigstellung.",
  ]),
  ("p", "Die Luftdichtheitsmessung ist der kritische Termin. Sie muss stattfinden, solange Nachbesserungen noch möglich sind — also bevor die Hülle verkleidet ist. Wer sie ans Ende schiebt, kann ein negatives Ergebnis nur noch mit grossem Aufwand korrigieren."),

  ("h2", "Zusammengefasst"),
  ("ul", [
    "GEAK beschreibt den Bestand und öffnet die Tür zur Förderung.",
    "Minergie ist ein Baustandard mit Anforderungen an Energie und Komfort.",
    "SNBS bewertet Nachhaltigkeit über den ganzen Lebenszyklus.",
    "Früh eingeplant kosten Labels wenig, nachträglich viel.",
    "Ein Label ersetzt keine Betriebsoptimierung.",
  ]),
],

"integrale-planung": [
  ("h2", "Wie sich das organisatorisch abbilden lässt"),
  ("p", "Integrale Planung ist keine Frage des guten Willens, sondern der Organisation. Sie braucht drei Dinge: einen frühen Zeitpunkt, ein gemeinsames Ziel und jemanden, der die Schnittstellen führt."),
  ("ul", [
    "Ein Zielwertblatt zu Beginn: Energiekennzahl, Raumklima, Betriebskosten, Flexibilität — mit Zahlen, nicht mit Adjektiven.",
    "Regelmässige Abstimmungen zwischen Architektur, Tragwerk und Haustechnik in den frühen Phasen, nicht erst bei der Koordination der Pläne.",
    "Ein gemeinsames digitales Modell, wo es der Projektgrösse angemessen ist.",
    "Eine dokumentierte Schnittstellenliste, die geführt und nicht einmalig erstellt wird.",
  ]),
  ("p", "Das Zielwertblatt ist dabei das wirksamste Instrument. Solange die Ziele qualitativ formuliert sind — «energieeffizient», «komfortabel» — kann jedes Gewerk sie für sich auslegen. Mit Zahlen wird sichtbar, wo sie sich widersprechen."),

  ("h2", "Der Preis der späten Entscheidung"),
  ("p", "Ein Beispiel aus der Praxis, das sich in ähnlicher Form immer wiederholt: Der Glasanteil einer Südfassade wird aus gestalterischen Gründen erhöht, die aussenliegende Verschattung fällt später dem Kostendruck zum Opfer. Die Kühllast steigt, die Kälteanlage wird grösser, die Kanäle werden grösser, die abgehängte Decke wird tiefer, ein Geschoss verliert Raumhöhe."),
  ("p", "Am Ende hat das Projekt bei der Verschattung gespart und ein Vielfaches davon in Technik und Geschosshöhe ausgegeben. Keiner der Beteiligten hat einen Fehler gemacht — jeder hat in seinem Budget optimiert."),

  ("h2", "Zusammengefasst"),
  ("ul", [
    "Die Haustechnik gehört ab der Vorstudie an den Tisch.",
    "Zielwerte mit Zahlen verhindern widersprüchliche Optimierungen.",
    "Schnittstellen brauchen einen benannten Verantwortlichen.",
    "Der künftige Betreiber liefert Grundlagen, die keine Norm enthält.",
    "Komplizierte Regelungen sind meist die Rechnung für frühe Versäumnisse.",
  ]),
],

"messkonzept-monitoring": [
  ("h2", "Abrechnung und Steuerung sind zwei verschiedene Zwecke"),
  ("p", "Zähler für die verbrauchsabhängige Heizkostenabrechnung unterliegen eichrechtlichen Anforderungen und sind entsprechend teurer. Zähler für die Betriebsführung müssen nicht geeicht sein — sie müssen reproduzierbar messen und richtig zugeordnet sein."),
  ("p", "Diese Unterscheidung spart Geld. Wer jeden Messpunkt in Abrechnungsqualität ausführt, gibt für die Betriebsführung deutlich mehr aus als nötig. Umgekehrt lässt sich mit einfachen Zählern nicht abrechnen. Beide Zwecke gehören deshalb im Konzept getrennt aufgeführt."),

  ("h2", "Datenhaltung: der unterschätzte Teil"),
  ("p", "Ein Monitoring ist nur so gut wie seine Historie. Vergleiche über Jahre sind der eigentliche Wert — sie zeigen den langsamen Anstieg, den niemand bemerkt, und belegen die Wirkung einer Massnahme."),
  ("ul", [
    "Speicherdauer von mindestens fünf Jahren festlegen.",
    "Datenexport in einem offenen Format sicherstellen, unabhängig vom Systemanbieter.",
    "Zuordnung der Zähler dokumentieren und bei jedem Umbau nachführen.",
    "Verantwortlichkeit für die Datenpflege benennen.",
  ]),
  ("p", "Der zweite Punkt entscheidet darüber, ob die Daten Ihnen gehören oder Ihrem Systemlieferanten. Beim Systemwechsel zeigt sich, ob das geregelt wurde."),

  ("h2", "Zusammengefasst"),
  ("ul", [
    "Messen, wo entschieden wird — nicht, wo es einfach ist.",
    "Wärmepumpen brauchen zwingend einen zugeordneten Stromzähler.",
    "Wenige Kennzahlen, die jemand regelmässig anschaut, schlagen jedes grosse Dashboard.",
    "Witterungsbereinigung, sonst vergleichen Sie Winter statt Anlagen.",
    "Das Konzept entsteht in der Projektierung, nicht im Betrieb.",
  ]),
],

}
