# -*- coding: utf-8 -*-
"""Inhalte fuer die Wissens-Unterseite.

Bloecke: ("h2", …) ("p", …) ("ul", [...]) ("merk", …)
Ziel je Beitrag: 1100 bis 1400 Woerter, also 6 bis 7 Minuten Lesezeit.

Bewusst OHNE Veroeffentlichungsdatum: die Beitraege sind neu, ein
erfundenes Datum waere eine Falschangabe.
"""

BEITRAEGE = [

{
 "slug": "hydraulischer-abgleich",
 "kategorie": "Heizung",
 "bild": "assets/img/technik-1.jpg",
 "alt": "Verteiler mit Strangregulierventilen in einer Technikzentrale",
 "titel": "Hydraulischer Abgleich: der kleinste Eingriff mit der grössten Wirkung",
 "teaser": "Warum halbe Häuser zu warm und halbe zu kalt sind, was ein Abgleich wirklich kostet und woran Sie erkennen, ob er je gemacht wurde.",
 "lead": "Kein anderer Eingriff in eine Heizung verändert Verbrauch und Behaglichkeit mit so wenig Aufwand. Und kein anderer wird so oft weggelassen.",
 "inhalt": [
  ("p", "Wasser nimmt den Weg des geringsten Widerstands. In einem Heizsystem heisst das: Die Heizkörper nahe der Pumpe bekommen zu viel Wasser, die am Ende des Strangs zu wenig. Die Bewohner in den entfernten Räumen drehen auf, die Betreiber erhöhen die Vorlauftemperatur, und ab diesem Moment läuft die gesamte Anlage dauerhaft zu heiss, damit der letzte Raum warm wird."),
  ("p", "Genau in diesem Zustand treffen wir sehr viele Bestandsanlagen an. Nicht defekt, nicht falsch dimensioniert, nicht schlecht gebaut — nur nie eingeregelt. Der Unterschied zwischen einer eingeregelten und einer nicht eingeregelten Anlage ist keine Frage der Qualität der Komponenten. Es ist eine Frage von zwei Arbeitstagen Rechnen und einem Tag Einstellen, die irgendwann in der Bauphase nicht bezahlt wurden."),

  ("h2", "Was beim Abgleich tatsächlich passiert"),
  ("p", "Der hydraulische Abgleich verteilt den Volumenstrom so, dass jeder Verbraucher genau die Wassermenge erhält, die er für seine Heizlast braucht. Dafür wird zuerst gerechnet, nicht geschraubt. Der Ablauf ist immer derselbe:"),
  ("ul", [
    "Heizlast je Raum nach Norm ermitteln — nicht nach Augenmass und nicht nach der Grösse des vorhandenen Heizkörpers.",
    "Aus der Heizlast und der gewünschten Spreizung den nötigen Volumenstrom je Heizkörper berechnen.",
    "Die Auslegungs-Vorlauftemperatur auf den ungünstigsten Raum festlegen — der bestimmt das ganze System.",
    "Für jedes Thermostat- oder Strangregulierventil den Voreinstellwert bestimmen.",
    "Die Pumpe auf den tatsächlichen Betriebspunkt einstellen, nicht auf die Werkseinstellung.",
    "Alles in einem Protokoll mit Soll- und Ist-Werten festhalten.",
  ]),
  ("p", "Der letzte Punkt ist der wichtigste und wird am häufigsten übersprungen. Ohne Protokoll gibt es keinen Nachweis, dass abgeglichen wurde, keine Grundlage für spätere Anpassungen und keine Möglichkeit zu prüfen, ob die Einstellungen im Betrieb noch stehen. Ein Abgleich ohne Dokumentation ist im Betrieb nicht reproduzierbar — und damit nach der ersten Störung faktisch verloren."),

  ("h2", "Warum die Spreizung so viel verrät"),
  ("p", "Die Differenz zwischen Vorlauf- und Rücklauftemperatur ist die einfachste Diagnose, die Sie ohne Werkzeug stellen können. Ist sie klein — etwa fünf Kelvin, wo zwanzig ausgelegt wären — fliesst zu viel Wasser zu schnell durch die Heizkörper. Das Wasser hat keine Zeit, seine Wärme abzugeben, und kommt fast so heiss zurück, wie es losgefahren ist."),
  ("p", "Die Folgen ziehen sich durch die ganze Anlage. Die Pumpe fördert unnötig viel und verbraucht Strom im Quadrat zur Fördermenge. Der Rücklauf ist zu heiss, was jeder Brennwertkessel mit schlechterer Ausnutzung quittiert und jede Wärmepumpe mit einer tieferen Arbeitszahl. Und die Regelung wird träge, weil die Heizkörper kaum noch auf Ventilbewegungen reagieren."),
  ("merk", "Eine zu kleine Spreizung ist kein Schönheitsfehler. Sie kostet gleichzeitig Pumpenstrom, Erzeugerwirkungsgrad und Regelgüte."),

  ("h2", "Was der Abgleich bringt"),
  ("p", "Die Wirkung hängt stark vom Ausgangszustand ab, und wer hier mit festen Prozentzahlen wirbt, kennt das Gebäude nicht. Bei einer Anlage, die nie eingeregelt wurde und mit deutlich überhöhter Vorlauftemperatur gefahren wird, sind zweistellige Einsparungen beim Wärmebedarf realistisch. Dazu kommt der Pumpenstrom, der oft um mehr als die Hälfte sinkt, weil die Pumpe nach dem Abgleich auf einem viel tieferen Betriebspunkt arbeiten kann."),
  ("p", "Bei einer Anlage, die bereits sauber läuft, bringt der Abgleich wenig. Dann ist er trotzdem sinnvoll — aber als Vorbereitung, nicht als Sparmassnahme. Und das ist der eigentliche Punkt."),
  ("p", "Eine Wärmepumpe arbeitet umso effizienter, je tiefer die Vorlauftemperatur ist. Solange die Anlage sechzig Grad braucht, weil ein einzelner Raum sonst kalt bleibt, verschenken Sie einen erheblichen Teil des Vorteils der neuen Erzeugung. Der Abgleich senkt die nötige Vorlauftemperatur — und erst dadurch rechnet sich der Erzeugerwechsel so, wie er auf dem Papier gerechnet wurde. Wer die Wärmepumpe auf eine nicht abgeglichene Anlage setzt, kauft die Effizienz und bekommt sie nicht."),

  ("h2", "Woran Sie erkennen, ob abgeglichen wurde"),
  ("ul", [
    "Es existiert ein Abgleichprotokoll mit Voreinstellwerten je Ventil. Ohne dieses Dokument ist die Anlage im Zweifel nicht abgeglichen.",
    "Die Thermostatventile haben sichtbar unterschiedliche Voreinstellungen. Wenn alle gleich stehen, wurde nicht gerechnet.",
    "Die Pumpe läuft nicht auf der höchsten Stufe und nicht auf konstanter Kennlinie.",
    "Die Rücklauftemperatur liegt im Winterbetrieb deutlich unter der Vorlauftemperatur.",
    "Es gibt keine Räume, in denen im Winter dauerhaft das Fenster gekippt ist.",
    "Niemand im Haus beschreibt einzelne Räume als «wird nie richtig warm».",
  ]),
  ("p", "Mündliche Auskünfte helfen an dieser Stelle nicht weiter. «Das wurde damals gemacht» heisst in der Praxis fast immer, dass die Ventile beim Einbau irgendwie eingestellt und danach nie überprüft wurden."),

  ("h2", "Wann sich der Aufwand lohnt"),
  ("p", "Immer dann, wenn ohnehin etwas an der Anlage geschieht: Erzeugerwechsel, Pumpentausch, Ventilerneuerung, Fassaden- oder Fenstersanierung. Nach einer Dämmung ändert sich die Heizlast jedes einzelnen Raums, damit stimmen sämtliche alten Einstellungen nicht mehr. Ein Abgleich ist dann keine Zusatzleistung, sondern ein notwendiger Teil der Sanierung — sonst heizen Sie ein gedämmtes Gebäude mit den Einstellungen des ungedämmten."),
  ("p", "Mehrere Kantone verlangen den hydraulischen Abgleich inzwischen bei bestimmten Eingriffen in die Heizungsanlage. Die Regelungen unterscheiden sich, deshalb gehört die Prüfung der kantonalen Vorgaben früh in die Planung und nicht erst zur Baueingabe."),

  ("h2", "Die häufigsten Fehler"),
  ("ul", [
    "Voreinstellung nach Gefühl statt nach Rechnung. Wer die Ventile «ungefähr» einstellt, verschiebt das Problem nur an eine andere Stelle im Netz.",
    "Abgleich ohne Anpassung der Heizkurve. Die tiefere mögliche Vorlauftemperatur muss auch geregelt werden, sonst bleibt der ganze Effekt aus.",
    "Die Pumpe unverändert lassen. Nach dem Abgleich passt der alte Betriebspunkt nicht mehr, und der grösste Stromspareffekt bleibt liegen.",
    "Einzelne Stränge auslassen, weil sie schwer zugänglich sind. Erfahrungsgemäss sitzen genau dort die Probleme.",
    "Den Abgleich vor der Dämmung machen. Die Reihenfolge ist immer: bauliche Massnahmen, dann Heizlast neu rechnen, dann abgleichen.",
  ]),

  ("h2", "Was wir Bauherren empfehlen"),
  ("p", "Behandeln Sie den Abgleich nicht als Nachtrag, sondern als eigene Position mit eigenem, prüfbarem Ergebnis. Verlangen Sie das Protokoll als Bestandteil der Abnahme, nicht als Nachreichung. Und legen Sie fest, wer nach einer vollen Heizperiode nachschaut, ob die Einstellungen noch stehen."),
  ("p", "Anlagen werden im Betrieb verstellt — von Hauswarten, von Nutzern, bei Reparaturen. Das ist normal und lässt sich nicht verhindern, nur abfangen. Eine kurze Kontrolle nach dem ersten Winter kostet einen halben Tag und sichert das Ergebnis für die nächsten Jahre."),
 ],
},

{
 "slug": "waermepumpe-im-bestand",
 "kategorie": "Sanierung",
 "bild": "assets/img/bau-4.jpg",
 "alt": "Wärmepumpe in einem bestehenden Technikraum",
 "titel": "Wärmepumpe im Bestand: wann sie funktioniert und wann nicht",
 "teaser": "Vorlauftemperatur, Heizflächen und Schallschutz entscheiden — nicht das Baujahr. Eine Einordnung ohne Versprechen.",
 "lead": "Die Frage ist selten, ob eine Wärmepumpe technisch möglich ist. Sie ist fast immer möglich. Die Frage ist, zu welcher Effizienz und zu welchem Preis.",
 "inhalt": [
  ("p", "Über den Erfolg einer Wärmepumpe im Bestand entscheidet im Wesentlichen eine einzige Grösse: die Vorlauftemperatur, die das Gebäude am kältesten Auslegungstag braucht. Jedes Grad weniger verbessert die Jahresarbeitszahl spürbar. Alles andere — Fabrikat, Regelung, Speichergrösse, Steuerungskomfort — ist demgegenüber nachrangig."),

  ("h2", "Die Rechnung hinter der Vorlauftemperatur"),
  ("p", "Eine Wärmepumpe hebt Wärme von einem tiefen auf ein höheres Temperaturniveau. Je grösser dieser Hub, desto mehr Strom kostet er — das ist keine Frage der Bauart, sondern der Thermodynamik. Zwischen einer Anlage, die mit fünfunddreissig Grad Vorlauf auskommt, und einer, die fünfundfünfzig braucht, liegt im Jahresmittel grob ein Drittel Stromverbrauch. Bei identischem Gebäude und identischem Gerät."),
  ("merk", "Nicht das Baujahr entscheidet, sondern die Auslegungstemperatur des Verteilsystems."),
  ("p", "Deshalb ist die erste Massnahme im Bestand nie der Gerätekauf, sondern die Frage: Wie tief kommen wir mit der Vorlauftemperatur tatsächlich? Das lässt sich messen, und zwar ohne Investition."),
  ("p", "Im Winterbetrieb wird die Heizkurve schrittweise abgesenkt, jeweils um ein bis zwei Grad, und dann beobachtet, ab wann der ungünstigste Raum nicht mehr warm wird. Das kostet nichts ausser Geduld und ein paar Wochen, und es liefert die belastbarste Grundlage, die es für diese Entscheidung gibt. Eine Rechnung auf dem Papier kann diese Messung ergänzen, aber nicht ersetzen — zu viele Bestandsgebäude weichen von ihren Plänen ab."),

  ("h2", "Heizflächen: mehr Fläche statt mehr Temperatur"),
  ("p", "Wo die Absenkung an ihre Grenze stösst, hilft Fläche. Ein grösserer Heizkörper gibt bei tieferer Systemtemperatur dieselbe Leistung ab. Der Austausch einzelner kritischer Heizkörper ist fast immer günstiger als eine dauerhaft höhere Systemtemperatur — und er stört den Betrieb weit weniger, als nachträglich eine Fussbodenheizung einzubauen."),
  ("ul", [
    "Fussbodenheizung: dreissig bis fünfunddreissig Grad, ideale Voraussetzung.",
    "Grossflächige Heizkörper oder Niedertemperatur-Konvektoren: vierzig bis fünfundvierzig Grad, gut geeignet.",
    "Klassische Radiatoren im wenig gedämmten Bau: fünfundfünfzig bis siebzig Grad, kritisch.",
    "Einzelne Problemräume: gezielter Tausch statt Anhebung der ganzen Systemtemperatur.",
  ]),
  ("p", "Es lohnt sich, die Problemräume namentlich zu erfassen. In den meisten Gebäuden sind es drei bis fünf von hundert — Eckzimmer, Räume über Durchfahrten, Bäder mit grossen Aussenflächen. Diese wenigen Räume bestimmen die Auslegung des gesamten Systems. Sie einzeln zu ertüchtigen ist meist die günstigste Massnahme im ganzen Projekt."),

  ("h2", "Wann die Gebäudehülle zuerst dran ist"),
  ("p", "Wenn das Gebäude so viel Wärme verliert, dass auch grosse Heizflächen die nötige Temperatur nicht drücken, hilft nur die Hülle. Fenster und Dach bringen dabei in der Regel mehr pro investiertem Franken als die Fassade, und sie sind meist einfacher umzusetzen."),
  ("p", "Wichtig ist die Reihenfolge: erst dämmen, dann die Heizlast neu rechnen, dann die Wärmepumpe dimensionieren. Umgekehrt kaufen Sie eine Maschine, die nach der Sanierung deutlich zu gross ist. Zu grosse Wärmepumpen takten — sie schalten häufig ein und aus, was den Verdichter belastet, die Effizienz senkt und die Lebensdauer verkürzt. Eine zu grosse Wärmepumpe ist ein teurerer Fehler als eine knapp bemessene mit elektrischer Nachheizung für wenige Stunden im Jahr."),

  ("h2", "Schall: der unterschätzte Projektkiller"),
  ("p", "Bei Aussenluft-Wärmepumpen ist der Schall regelmässig das grössere Hindernis als die Technik. Massgebend sind die Immissionsgrenzwerte an der Grundstücksgrenze und beim nächsten Nachbarn, und die Nacht ist der kritische Fall. Ein Standort, der tagsüber unauffällig ist, kann nachts unzulässig sein."),
  ("ul", [
    "Standortwahl früh klären, nicht erst in der Ausführungsplanung.",
    "Schallnachweis vor der Baueingabe rechnen lassen, nicht danach.",
    "Reflektierende Flächen und Innenecken meiden — sie verstärken den Pegel messbar.",
    "Nachtabsenkung der Verdichterleistung als Reserve einplanen.",
    "Körperschall über die Aufstellung entkoppeln, nicht nur den Luftschall betrachten.",
  ]),
  ("p", "Der letzte Punkt wird oft vergessen und ist im Nachhinein besonders unangenehm zu korrigieren: Ein Gerät, dessen Vibrationen über die Befestigung in die Gebäudestruktur wandern, ist in Räumen hörbar, die vom Aufstellort weit entfernt sind."),

  ("h2", "Sole oder Luft"),
  ("p", "Erdsonden liefern das stabilere Temperaturniveau und die höhere Jahresarbeitszahl, brauchen aber eine Bewilligung, Platz für die Bohrung und deutlich mehr Kapital. Ob überhaupt gebohrt werden darf, hängt vom Gewässerschutzbereich ab. Das ist eine kantonale Karte und in wenigen Minuten geklärt."),
  ("p", "Diese Abklärung gehört an den Anfang, nicht ans Ende. Sie entscheidet darüber, ob die Variantenrechnung überhaupt zwei Varianten hat — und wenn die Bohrung nicht zulässig ist, spart man sich den gesamten Vergleich."),

  ("h2", "Was in eine belastbare Entscheidungsgrundlage gehört"),
  ("ul", [
    "Gemessene, nicht geschätzte Vorlauftemperatur aus dem Winterbetrieb.",
    "Heizlast nach Norm, raumweise gerechnet.",
    "Liste der kritischen Räume mit Massnahme und Kosten je Raum.",
    "Schallnachweis für den vorgesehenen Standort, inklusive Nachtwerten.",
    "Abklärung der Zulässigkeit von Erdsonden am Standort.",
    "Variantenvergleich über die Lebensdauer, nicht über den Anschaffungspreis.",
    "Zustand und Auslegung der Trinkwarmwasserbereitung — sie verlangt oft die höchste Temperatur im ganzen System.",
  ]),
  ("p", "Der letzte Punkt wird häufig übersehen. Wenn das Trinkwarmwasser über dieselbe Wärmepumpe läuft, bestimmt die Hygieneanforderung die Maximaltemperatur — und damit möglicherweise die Auslegung der ganzen Anlage. Eine getrennte Betrachtung von Heizung und Warmwasser, gegebenenfalls mit eigener Erzeugung, ist oft die effizientere Lösung."),
  ("p", "Wer diese sieben Punkte hat, kann entscheiden. Wer sie nicht hat, kauft ein Gerät und hofft."),
 ],
},

{
 "slug": "lueftung-sia-382",
 "kategorie": "Lüftung",
 "bild": "assets/img/technik-2.jpg",
 "alt": "Lüftungskanäle in einer Technikzentrale",
 "titel": "Lüftung nach SIA 382/1: was bei der Abnahme wirklich geprüft wird",
 "teaser": "Aussenluftraten, Messprotokolle und die Punkte, an denen Anlagen bei der Abnahme regelmässig durchfallen.",
 "lead": "Eine Lüftungsanlage wird nicht danach beurteilt, wie sie geplant war, sondern danach, was am Auslass ankommt. Zwischen beidem liegen erfahrungsgemäss zehn bis dreissig Prozent.",
 "inhalt": [
  ("p", "Die SIA 382/1 regelt die Grundlagen und Anforderungen an Lüftungs- und Klimaanlagen. Für die Praxis heisst das vor allem zweierlei: Es gibt definierte Aussenluftvolumenströme je Nutzung und Person, und es gibt einen Nachweis, dass sie eingehalten werden. Der Nachweis ist der Teil, der regelmässig schiefgeht."),

  ("h2", "Die Auslegung ist der einfache Teil"),
  ("p", "Die nötigen Luftmengen ergeben sich aus Nutzung, Belegungsdichte und angestrebter Raumluftqualität. Die Raumnutzungsdaten der SIA 2024 liefern dafür die Standardwerte — für Belegung, Betriebszeiten, innere Lasten. Sie sind der Ausgangspunkt einer Auslegung, nicht deren Ergebnis."),
  ("merk", "Standardwerte sind eine Annahme. Wer sie nicht mit der realen Nutzung abgleicht, plant an der Wirklichkeit vorbei."),
  ("p", "Der klassische Fall ist das Sitzungszimmer, das nach Standardbelegung gerechnet wird und im Betrieb regelmässig doppelt besetzt ist. Die Anlage ist normkonform ausgelegt und trotzdem zu klein. Der zweite klassische Fall ist umgekehrt: Ein Grossraumbüro wird nach Vollbelegung gerechnet, ist aber im Schnitt zu sechzig Prozent besetzt — die Anlage läuft dauerhaft über Bedarf und verbraucht entsprechend."),
  ("p", "Beide Fälle löst man nicht mit einer anderen Auslegung, sondern mit einem Gespräch: Wer nutzt diese Räume, wie oft, mit wie vielen Personen? Diese Information hat der künftige Betreiber, nicht die Norm."),

  ("h2", "Was die Abnahme verlangt"),
  ("ul", [
    "Messprotokoll der Volumenströme an jedem Auslass — nicht nur eine Summenmessung am Gerät.",
    "Nachweis der Luftdichtheit des Kanalnetzes in der geforderten Klasse.",
    "Filterklassen und Einbauzustand dokumentiert, mit Datum des Ersteinbaus.",
    "Schallpegel im Raum unter tatsächlichen Betriebsbedingungen.",
    "Funktionsnachweis der Regelung über alle vorgesehenen Betriebsarten.",
    "Hygienedokumentation und nachgewiesene Zugänglichkeit aller Reinigungsöffnungen.",
  ]),
  ("p", "Der zweite Punkt ist der teuerste, wenn er fehlt. Undichte Kanäle verlieren Luft im Schacht, wo sie niemandem nützt. Die Ventilatoren gleichen das mit mehr Leistung aus, der Strombedarf steigt dauerhaft — und der Fehler wird erst sichtbar, wenn jemand am Auslass misst statt am Gerät. Eine Dichtheitsprüfung während der Bauzeit, solange die Kanäle noch zugänglich sind, kostet einen Bruchteil der späteren Korrektur."),

  ("h2", "Die drei häufigsten Mängel"),
  ("p", "Erstens: nicht eingeregelt. Die Anlage läuft, die Verteilung stimmt nicht. Es ist dasselbe Muster wie bei der Heizung — die nahen Auslässe bekommen zu viel, die entfernten zu wenig. Der Unterschied ist nur, dass man Luft nicht sieht und die Beschwerden deshalb später kommen."),
  ("p", "Zweitens: nicht zugänglich. Reinigungsöffnungen hinter abgehängten Decken ohne Revisionsklappe, Filterwechsel nur mit Gerüst oder Hubsteiger, Brandschutzklappen, die zur Prüfung nicht erreichbar sind. Das ist kein Schönheitsfehler. Es führt dazu, dass die Wartung faktisch nicht stattfindet — und eine Lüftungsanlage, die nicht gereinigt wird, verliert Leistung und wird über die Jahre zum Hygieneproblem."),
  ("p", "Drittens: Regelung ohne Konzept. Konstanter Volumenstrom in Räumen mit stark schwankender Belegung verbraucht dauerhaft zu viel Energie. Bedarfsgeführte Regelung ohne saubere Sensorik liefert Zufallswerte und wird von den Nutzern früher oder später überstimmt. Beides ist häufig, und beides lässt sich in der Planung vermeiden."),

  ("h2", "Bedarfsführung: sinnvoll, aber nicht überall"),
  ("p", "Die Regelung nach CO₂-Gehalt der Raumluft lohnt sich dort, wo die Belegung stark und unregelmässig schwankt: Sitzungszimmer, Schulungsräume, Aulen, Kantinen. In Räumen mit gleichmässiger Belegung bringt sie wenig und kostet Sensorik, Verkabelung und Aufwand in der Inbetriebnahme."),
  ("p", "Die Entscheidung gehört raumweise getroffen, nicht pauschal für das ganze Gebäude. Und sie braucht eine bewusste Wahl des Messorts: Ein Sensor in der Abluft mittelt über den ganzen Raum und reagiert träge, ein Sensor im Aufenthaltsbereich reagiert schnell und lässt sich durch eine einzelne Person direkt daneben verfälschen. Beides ist vertretbar, aber es muss entschieden und dokumentiert sein."),

  ("h2", "Wärmerückgewinnung ehrlich rechnen"),
  ("p", "Die Rückwärmzahl auf dem Datenblatt gilt für den Auslegungspunkt. Im Jahresmittel liegt der reale Wert tiefer, und die zusätzliche Ventilatorleistung für den Druckverlust des Wärmetauschers gehört gegengerechnet. Eine Wärmerückgewinnung, die im Datenblatt glänzt und im Betrieb den Strombedarf hochtreibt, ist kein Gewinn, sondern eine Verschiebung von Wärme zu Strom."),
  ("p", "Bei Rotationswärmetauschern kommt die Frage der Leckage dazu, bei Plattentauschern die der Vereisung und der dafür nötigen Vorwärmung. Beides gehört in die Betrachtung, wenn man die Systeme ehrlich vergleichen will."),

  ("h2", "Was Bauherren verlangen sollten"),
  ("ul", [
    "Einregulierprotokoll als Voraussetzung für die Abnahme, nicht als Nachreichung.",
    "Messung am Auslass, stichprobenweise im Beisein der Bauleitung.",
    "Revisionsplan mit allen Zugängen, freigegeben bevor die Decken geschlossen werden.",
    "Übergabe der Regelparameter in lesbarer Form, nicht nur im Gerät gespeichert.",
    "Eine Nachmessung nach dem ersten Betriebsjahr, vertraglich vereinbart.",
  ]),
  ("p", "Diese fünf Punkte kosten in der Ausschreibung fast nichts und entscheiden über den Betrieb der nächsten zwanzig Jahre. Der letzte ist der wirksamste: Er sorgt dafür, dass die Anlage nicht nur am Abnahmetag funktioniert."),
 ],
},

{
 "slug": "trinkwasser-legionellen",
 "kategorie": "Sanitär",
 "bild": "assets/img/technik-5.jpg",
 "alt": "Trinkwasserverteilung mit Speicher und Zirkulationsleitungen",
 "titel": "Trinkwasser und Legionellen: was die Planung leisten muss",
 "teaser": "Temperaturhaltung, Stagnation und Totleitungen. Warum das Problem fast immer in der Planung entsteht und nicht im Betrieb.",
 "lead": "Legionellen sind kein Hygieneproblem des Betreibers. Sie sind in den allermeisten Fällen ein Planungsergebnis, das erst Jahre später sichtbar wird.",
 "inhalt": [
  ("p", "Legionellen vermehren sich in stehendem, lauwarmem Wasser. Alles, was Wasser stehen lässt oder in den kritischen Temperaturbereich bringt, ist ein Risiko — und beides wird auf dem Plan entschieden, lange bevor jemand die Anlage betreibt. Der Betreiber kann ein Planungsproblem später nur noch verwalten, nicht mehr beheben."),

  ("h2", "Die drei Grundsätze"),
  ("ul", [
    "Kalt bleibt kalt. Kaltwasserleitungen dürfen sich nicht erwärmen — also nicht ungetrennt neben Warmleitungen im selben Schacht, nicht in warmen Deckenhohlräumen ohne Dämmung.",
    "Warm bleibt warm. Im gesamten Warmwasserkreis darf die Temperatur nicht in den kritischen Bereich absacken. Das betrifft besonders die entferntesten Punkte der Zirkulation und die Stichleitungen zu den Entnahmestellen.",
    "Nichts steht still. Jede Leitung braucht regelmässigen Durchfluss — auch die, an die niemand denkt.",
  ]),
  ("merk", "Die gefährlichste Leitung ist die, an die niemand mehr denkt."),

  ("h2", "Totleitungen: das häufigste Erbe"),
  ("p", "Bei jedem Umbau entstehen sie: Ein Waschbecken wird versetzt, die alte Stichleitung bleibt in der Wand. Ein Stockwerk wird umgenutzt, ein ganzer Strang wird nicht mehr gebraucht. Ein Gebäudeteil steht temporär leer. Das Wasser darin steht, erwärmt sich auf Raumtemperatur und bildet ein Reservoir, das den Rest der Anlage immer wieder neu belastet."),
  ("p", "Deshalb gehört zu jedem Sanitärumbau eine Bestandsaufnahme der stillgelegten Leitungen — und ihr Rückbau bis zur durchflossenen Leitung. Nicht das Verschliessen mit einer Kappe: Eine abgekappte Leitung von zwei Metern Länge ist genau das Problem, das man beseitigen wollte. Der Rückbau muss bis zum durchströmten Strang gehen, sonst bleibt ein Sackgassen-Volumen zurück."),
  ("p", "Diese Bestandsaufnahme ist Aufwand, und sie wird regelmässig aus dem Angebot gestrichen. Sie ist trotzdem die wirksamste Einzelmassnahme in jeder Bestandssanierung."),

  ("h2", "Zirkulation richtig auslegen"),
  ("p", "Der klassische Fehler ist die hydraulisch nicht abgeglichene Zirkulation. Der kurze Strang zirkuliert kräftig, der lange kaum — und genau dort, am entferntesten Punkt, fällt die Temperatur unter den kritischen Wert. Auch hier braucht es Regulierventile mit gerechneten Voreinstellungen und ein Protokoll, genau wie bei der Heizung."),
  ("p", "Thermische Regulierventile, die nach Temperatur statt nach Volumenstrom regeln, nehmen einen Teil der Arbeit ab, ersetzen die Auslegung aber nicht. Und sie brauchen eine Kontrolle: Ein verklemmtes Ventil fällt im Betrieb nicht auf, weil das Warmwasser an der Entnahmestelle trotzdem warm ankommt — nur eben nicht über die Zirkulation, sondern nach längerem Laufenlassen."),
  ("p", "Zeitschaltungen, welche die Zirkulationspumpe nachts abstellen, sparen etwas Strom und schaffen ein Risiko. Wenn abgeschaltet wird, dann kontrolliert und mit definierter Wiederaufheizung — nicht als beiläufige Sparmassnahme in der Regelung, die niemand dokumentiert hat."),

  ("h2", "Speicher, Erzeugung und der Zielkonflikt mit der Wärmepumpe"),
  ("p", "Die Kombination aus Wärmepumpe und Trinkwarmwasser verlangt besondere Sorgfalt, weil zwei Anforderungen gegeneinander stehen: Die Wärmepumpe arbeitet effizient bei tiefen Temperaturen, die Hygiene verlangt hohe."),
  ("p", "Auflösen lässt sich das über Frischwasserstationen, die das Trinkwarmwasser im Durchfluss erzeugen und damit das stehende Volumen minimieren, über Schichtspeicher mit gezielter Nachheizung im oberen Bereich, oder über eine getrennte Erzeugung für das Warmwasser. Alle drei Wege sind gangbar. Was nicht geht, ist die Speichertemperatur stillschweigend abzusenken, um die Jahresarbeitszahl im Bericht schöner aussehen zu lassen — das verschiebt ein Effizienzproblem in die Hygiene."),

  ("h2", "Was der Betrieb übernehmen muss"),
  ("ul", [
    "Temperaturkontrolle an definierten Messpunkten, dokumentiert und mit Grenzwerten.",
    "Spülplan für selten genutzte Entnahmestellen, mit benannter Zuständigkeit.",
    "Regelung für Nutzungsänderungen — leerstehende Bereiche brauchen einen Plan, keine Improvisation.",
    "Zuständigkeit schriftlich geregelt, nicht mündlich vereinbart.",
    "Nachführung des Konzepts bei jedem Umbau.",
  ]),
  ("p", "Ohne benannte Zuständigkeit passiert nichts. Das ist keine juristische Feinheit, sondern der Unterschied zwischen einem Konzept und einem Papier in einem Ordner."),

  ("h2", "Was wir Bauherren raten"),
  ("p", "Verlangen Sie ein Hygienekonzept als eigenständiges Dokument, nicht als Absatz im Anlagenbeschrieb. Darin gehören: Temperaturkonzept mit Sollwerten, Zirkulationsschema mit Abgleichwerten, Liste der kritischen Entnahmestellen, Spülplan und Zuständigkeiten."),
  ("p", "Und legen Sie fest, dass dieses Dokument bei jeder Nutzungsänderung nachgeführt wird. Genau dann entstehen die Probleme — nicht beim Neubau, sondern beim dritten Umbau, wenn niemand mehr weiss, welche Leitung wohin führt."),
 ],
},

{
 "slug": "gebaeudeautomation-nachruesten",
 "kategorie": "Automation",
 "bild": "assets/img/technik-3.jpg",
 "alt": "Schaltschrank der Gebäudeleittechnik",
 "titel": "Gebäudeautomation im laufenden Betrieb erweitern",
 "teaser": "Offene Schnittstellen, Datenpunktlisten und Migrationspfade — wie man eine Leittechnik erneuert, ohne das Gebäude anzuhalten.",
 "lead": "Die Steuerung eines Gebäudes zu erneuern ist heikler, als die Erzeugung zu tauschen. Man ersetzt nicht ein Gerät, sondern das Nervensystem.",
 "inhalt": [
  ("p", "Bei einer Erzeugersanierung gibt es einen Umschaltpunkt: alte Anlage aus, neue Anlage ein. Bei der Gebäudeautomation gibt es Hunderte — jeder Fühler, jeder Antrieb, jede Verriegelung. Deshalb ist bei diesen Projekten die Reihenfolge wichtiger als die Technik."),

  ("h2", "Zuerst die Datenpunktliste, dann alles andere"),
  ("p", "Die Datenpunktliste ist das eigentliche Bauwerk einer Gebäudeautomation. Sie hält fest, welcher Wert wo gemessen wird, welcher Antrieb wie angesteuert wird und welche Verriegelung zwingend eingehalten werden muss. Ohne sie ist jede Migration ein Blindflug — und in Bestandsanlagen ist sie fast nie aktuell."),
  ("merk", "Der erste Schritt jeder GA-Sanierung ist eine Bestandsaufnahme, kein Angebot."),
  ("ul", [
    "Welche Datenpunkte existieren physisch, und welche stehen nur im alten Schema?",
    "Welche sind aufgeschaltet, welche nur verdrahtet und nie in Betrieb genommen?",
    "Welche Verriegelungen sind sicherheitsrelevant — Brandschutz, Frostschutz, Not-Aus?",
    "Welche Regelstrategien laufen tatsächlich, und welche stehen nur in der Dokumentation?",
    "Welche Handeingriffe hat der Betrieb über die Jahre eingebaut, und warum?",
  ]),
  ("p", "Der letzte Punkt liefert oft die wichtigsten Erkenntnisse. Jeder überbrückte Fühler und jeder auf Hand gestellte Antrieb ist die Antwort auf ein Problem, das jemand hatte. Wer diese Eingriffe bei der Migration einfach wegräumt, holt sich das ursprüngliche Problem zurück."),

  ("h2", "Offene Schnittstellen sind kein Luxus"),
  ("p", "Eine Leittechnik lebt fünfzehn bis zwanzig Jahre, die Geräte darunter oft nur zehn. Wer sich auf ein geschlossenes System festlegt, bindet sich für die gesamte Restlaufzeit an einen Anbieter — bei jeder Erweiterung, jedem Ersatzteil und jeder Programmänderung."),
  ("p", "Offene Protokolle kosten in der Beschaffung wenig und halten die Tür für den nächsten Schritt offen. Auf der Automationsebene hat sich BACnet etabliert, auf der Feldebene KNX oder Modbus. Entscheidend ist dabei weniger das Protokoll selbst als die Frage, wem die Datenpunkte gehören und wer sie exportieren darf. Das gehört in den Vertrag, nicht ins Datenblatt."),
  ("ul", [
    "Wem gehören die Programmquellen der Automationsstationen?",
    "Darf ein Dritter Änderungen vornehmen, ohne Gewährleistung zu verlieren?",
    "Sind die Datenpunkte ohne Zusatzlizenz auslesbar?",
    "Was kostet eine Erweiterung um zehn Prozent der Datenpunkte?",
  ]),
  ("p", "Diese vier Fragen in der Ausschreibung ersparen später viel Geld. Sie werden selten gestellt."),

  ("h2", "Migration in Abschnitten"),
  ("p", "Im laufenden Betrieb wird nie das ganze Gebäude auf einmal umgeschaltet. Bewährt hat sich der Weg über Zonen: Ein Bereich bekommt die neue Automationsstation, läuft parallel, wird beobachtet und erst dann übernommen. Die alte und die neue Ebene sprechen währenddessen über eine Übergangs-Schnittstelle miteinander."),
  ("ul", [
    "Pilotzone wählen, die unkritisch ist — das Lager, nicht der Operationssaal.",
    "Parallelbetrieb mit Vergleichsmessung über mindestens zwei Wochen.",
    "Rückfallebene definieren und testen, bevor umgeschaltet wird.",
    "Umschaltung in der Schwachlastzeit, nicht am Montagmorgen.",
    "Nach jeder Zone eine kurze Auswertung, bevor die nächste beginnt.",
  ]),
  ("p", "Der letzte Punkt verhindert, dass sich ein Fehler durch alle Zonen zieht. Wer alle Zonen nach demselben Muster baut, bevor die erste überprüft ist, vervielfacht jeden Denkfehler."),

  ("h2", "Was in kritischen Bauten zusätzlich gilt"),
  ("p", "In Kliniken, Rechenzentren und der Produktion entscheidet nicht die Automation über den Zeitplan, sondern der Betrieb. Jede Umschaltung braucht ein abgestimmtes Zeitfenster, eine schriftliche Rückfallanweisung und eine Person auf Seite des Betreibers, die im Moment der Umschaltung entscheiden darf. Ohne diese Person steht die Baustelle — nicht wegen der Technik, sondern weil niemand die Freigabe erteilen kann."),
  ("p", "Diese Person muss vor Projektbeginn benannt sein, nicht während der ersten Umschaltung gesucht werden."),

  ("h2", "Der häufigste Fehler nach der Inbetriebnahme"),
  ("p", "Die Anlage läuft, die Abnahme ist unterschrieben, und niemand schaut wieder hin. Regelparameter, die für den Sommerbetrieb gesetzt wurden, bleiben im Winter stehen. Sollwerte werden von Nutzern verstellt und nie zurückgesetzt. Störmeldungen werden quittiert statt bearbeitet. Nach zwei Jahren läuft die neue Automation schlechter als die alte, die man ersetzt hat."),
  ("p", "Deshalb gehört zu jeder GA-Sanierung eine vereinbarte Nachschau nach einer vollen Heiz- und einer vollen Kühlperiode. Das ist keine Garantieleistung und keine Kulanz, sondern der letzte Teil der Inbetriebnahme — und er gehört von Anfang an in den Vertrag und ins Budget."),
 ],
},

{
 "slug": "betriebsoptimierung",
 "kategorie": "Betrieb",
 "bild": "assets/img/bau-2.jpg",
 "alt": "Techniker bei der Kontrolle einer Anlage",
 "titel": "Betriebsoptimierung: die ersten zwei Jahre entscheiden",
 "teaser": "Warum neue Anlagen im zweiten Winter oft mehr verbrauchen als im ersten — und was dagegen hilft.",
 "lead": "Eine Anlage wird nicht bei der Abnahme gut. Sie wird es im ersten Betriebsjahr, oder sie wird es nie.",
 "inhalt": [
  ("p", "Bei der Abnahme läuft eine Anlage unter Idealbedingungen: leeres oder wenig belegtes Gebäude, definierte Aussentemperatur, alle Sollwerte frisch gesetzt, der Fachmann steht daneben. Der echte Betrieb sieht anders aus — und genau in dieser Differenz entsteht der Verbrauch, über den man später spricht."),

  ("h2", "Warum Gebäude driften"),
  ("ul", [
    "Sollwerte werden im Betrieb verstellt und nie zurückgesetzt.",
    "Zeitprogramme passen nicht zur tatsächlichen Nutzung — sie stammen aus der Planung, nicht aus der Beobachtung.",
    "Betriebsarten, die für die Inbetriebnahme gesetzt wurden, bleiben dauerhaft aktiv.",
    "Nutzungen ändern sich, die Regelung wird nicht nachgeführt.",
    "Störungen werden quittiert statt behoben, weil die Anlage trotzdem läuft.",
    "Personal wechselt, und das Wissen über die Anlage geht mit.",
  ]),
  ("merk", "Der grösste Einzelposten ist fast immer eine Anlage, die läuft, wenn niemand da ist."),
  ("p", "Das klingt banal und ist es nicht. Eine Lüftung, die statt zwölf Stunden sechzehn läuft, verbraucht ein Drittel mehr — ohne dass es jemandem auffällt, weil nichts kaputt ist und sich niemand beschwert."),

  ("h2", "Was eine Betriebsoptimierung konkret tut"),
  ("p", "Sie vergleicht das, was die Anlage tun soll, mit dem, was sie tatsächlich tut. Dafür braucht es Daten über eine volle Periode, nicht eine Momentaufnahme. Aus dem Vergleich entstehen Massnahmen — meist ohne Investition, oft mit sofortiger Wirkung."),
  ("ul", [
    "Zeitprogramme an die reale Belegung anpassen, inklusive Feiertagen und Ferien.",
    "Heiz- und Kühlkurven nachziehen, nachdem das Gebäude ein Jahr im Betrieb war.",
    "Gleichzeitiges Heizen und Kühlen aufspüren und abstellen.",
    "Ventilatoren und Pumpen auf den tatsächlichen Betriebspunkt bringen.",
    "Sollwertbänder erweitern, wo es die Nutzung erlaubt.",
    "Nachtabsenkung und Wochenendbetrieb überprüfen — oft sind sie nicht aktiv.",
  ]),
  ("p", "Der dritte Punkt lohnt die gesonderte Suche. Gleichzeitiges Heizen und Kühlen im selben Raum ist häufiger, als man denkt, und praktisch nie beabsichtigt. Es entsteht durch überlappende Sollwertbänder, durch Nachheizregister, die gegen eine zu tief eingestellte Zulufttemperatur arbeiten, oder durch Einzelraumregler, die gegen die zentrale Regelung laufen. Sichtbar wird es nur in den Daten, spürbar nur an der Rechnung."),

  ("h2", "Ohne Messung keine Optimierung"),
  ("p", "Wer nicht misst, diskutiert. Ein brauchbares Messkonzept braucht keine hundert Zähler, aber die richtigen: Wärme nach Erzeuger und nach Verbrauchergruppe, Strom für Wärmepumpe, Kälte und Lüftung getrennt, Wasser gesamt. Damit lassen sich Kennzahlen bilden, die etwas aussagen — und Veränderungen zuordnen, statt sie zu vermuten."),
  ("p", "Wichtiger als die Anzahl der Messstellen ist ihre Zuordnung. Ein Zähler, von dem niemand genau weiss, welchen Bereich er erfasst, ist im Streitfall wertlos."),

  ("h2", "Der Ablauf, der sich bewährt hat"),
  ("ul", [
    "Erste Nachschau nach der ersten vollen Heizperiode.",
    "Zweite nach der ersten vollen Kühlperiode.",
    "Dritte nach dem zweiten Betriebsjahr, wenn sich die Nutzung eingespielt hat.",
    "Danach in längeren Abständen, und immer bei wesentlichen Nutzungsänderungen.",
  ]),
  ("p", "Diese Termine gehören in den Vertrag, sonst finden sie nicht statt. Nicht aus Nachlässigkeit — sondern weil im Betrieb immer etwas Dringenderes ansteht als eine Anlage, die läuft."),

  ("h2", "Was sie bringt"),
  ("p", "Bei Anlagen, die nie systematisch nachgeführt wurden, sind zweistellige Einsparungen üblich, ohne dass ein einziges Gerät ersetzt wird. Der Aufwand liegt im Bereich weniger Tage Ingenieurleistung und amortisiert sich in solchen Fällen meist innerhalb einer Heizperiode."),
  ("p", "Bei bereits optimierten Anlagen bleibt der Effekt klein. Dann wird die Optimierung zur Bestandssicherung: Sie verhindert, dass das Erreichte über die Jahre wieder verloren geht. Beides ist ein gutes Ergebnis — es sollte nur vorher klar sein, welches der beiden man erwartet. Wer bei einer sauber laufenden Anlage zweistellige Einsparungen verspricht, hat sie nicht angeschaut."),
 ],
},

{
 "slug": "free-cooling",
 "kategorie": "Kälte",
 "bild": "assets/img/technik-4.jpg",
 "alt": "Rückkühler auf einem Flachdach",
 "titel": "Free Cooling: wann sich freie Kühlung wirklich rechnet",
 "teaser": "Die Grenztemperatur entscheidet, nicht die Technik. Wo freie Kühlung viel bringt und wo sie nur Anlagentechnik hinzufügt.",
 "lead": "Freie Kühlung ist keine Sparmassnahme, die man einer bestehenden Kälteanlage hinzufügt. Sie ist eine Auslegungsentscheidung, die man früh trifft oder gar nicht.",
 "inhalt": [
  ("p", "Der Gedanke ist einfach: Solange es draussen kälter ist als das Kühlwasser sein muss, braucht es keinen Kältekompressor. Man kühlt über den Rückkühler direkt und spart den energieintensivsten Teil der Anlage. Ob das viele Stunden im Jahr betrifft oder wenige, hängt an einer einzigen Zahl — der geforderten Kaltwassertemperatur."),

  ("h2", "Die Grenztemperatur ist die ganze Rechnung"),
  ("p", "Eine Anlage, die mit sechzehn Grad Kaltwasser auskommt, kann in unseren Breiten während eines erheblichen Teils des Jahres frei gekühlt werden. Eine Anlage, die sechs Grad braucht, praktisch nie. Zwischen diesen beiden Auslegungen liegt der Unterschied zwischen einer sinnvollen Investition und totem Kapital auf dem Dach."),
  ("merk", "Nicht «können wir frei kühlen?» ist die Frage, sondern «wie hoch dürfen wir die Kaltwassertemperatur legen?»"),
  ("p", "Hohe Kaltwassertemperaturen verlangen grosse Übergabeflächen: Kühldecken statt Umluftkühlern, grosse Register statt kleiner, Bauteilaktivierung statt Nachrüstlösungen. Das kostet in der Investition und zahlt sich über den Betrieb zurück — aber nur, wenn es von Anfang an so geplant wird. Nachträglich lässt sich die Kaltwassertemperatur nicht anheben, ohne die Übergabe umzubauen."),

  ("h2", "Der Taupunkt als zweite Grenze"),
  ("p", "Bei Kühldecken und Bauteilaktivierung kommt eine zusätzliche Bedingung dazu: Die Oberflächentemperatur darf den Taupunkt der Raumluft nicht unterschreiten, sonst schlägt sich Feuchtigkeit nieder. Das begrenzt die Kaltwassertemperatur nach unten und passt damit gut zur freien Kühlung — beide verlangen dasselbe."),
  ("p", "Es verlangt aber auch eine Taupunktüberwachung und eine Regelstrategie, die bei feuchter Witterung die Vorlauftemperatur anhebt. Wer das weglässt, bekommt im ersten schwülen Sommer nasse Decken."),

  ("h2", "Wo es sich fast immer lohnt"),
  ("ul", [
    "Rechenzentren und Serverräume mit ganzjährigem, gleichmässigem Kühlbedarf.",
    "Prozesskühlung in der Industrie mit konstanter Last.",
    "Bauten mit Kühldecken oder thermischer Bauteilaktivierung.",
    "Anlagen, die auch in der kalten Jahreszeit Kälte brauchen.",
  ]),
  ("p", "Der letzte Punkt ist der entscheidende und wird oft übersehen. Freie Kühlung nützt dann, wenn es draussen kalt ist. Wenn zu dieser Zeit kein Kühlbedarf besteht, gibt es nichts einzusparen. Ein reines Bürogebäude, das nur im Hochsommer kühlt, profitiert wenig — genau dann, wenn es kühlen muss, ist draussen zu warm."),

  ("h2", "Nachtauskühlung: der günstigere Verwandte"),
  ("p", "Wo Speichermasse vorhanden ist, ist die nächtliche Auskühlung über die Lüftung oft die wirtschaftlichere Massnahme. Sie braucht keine zusätzliche Hydraulik und keinen zweiten Wärmetauscher, nur eine Regelstrategie und ausreichende Öffnungs- oder Kanalquerschnitte."),
  ("p", "Voraussetzung sind Bauteile, die Wärme aufnehmen können. Abgehängte Decken und Doppelböden schneiden die Speichermasse ab und machen den Effekt weitgehend zunichte — eine Entscheidung, die im Ausbau fällt und die Haustechnik trifft. Auch das ist ein Fall für die integrale Planung: Wer die Decke abhängt, entscheidet über die Kühlstrategie mit."),

  ("h2", "Was in der Auslegung geprüft gehört"),
  ("ul", [
    "Jahresdauerlinie der Kühllast, nicht nur die Spitzenlast.",
    "Aussentemperaturverteilung am Standort über das ganze Jahr.",
    "Geforderte Kaltwassertemperatur je Verbraucher, einzeln aufgeführt.",
    "Zusätzlicher Strombedarf für Rückkühler und Pumpen im Freikühlbetrieb.",
    "Platzbedarf, Gewicht und Schall des Rückkühlers.",
    "Umschaltstrategie zwischen freier und maschineller Kühlung, inklusive Mischbetrieb.",
  ]),
  ("p", "Der vierte Punkt wird gern übersehen. Freie Kühlung spart Verdichterstrom und kostet Ventilator- und Pumpenstrom. Bei schlecht ausgelegter Hydraulik — zu hohe Druckverluste, zu kleine Temperaturspreizung — bleibt unter dem Strich wenig übrig. Der Vergleich muss die gesamte Anlage umfassen, nicht nur den Verdichter."),
  ("p", "Der sechste Punkt entscheidet über den Alltag. Eine Anlage, die zu spät auf freie Kühlung umschaltet oder zwischen den Betriebsarten pendelt, verschenkt genau die Stunden, für die sie gebaut wurde."),

  ("h2", "Die ehrliche Einordnung"),
  ("p", "Freie Kühlung ist dort ausgezeichnet, wo ganzjähriger Kühlbedarf auf hohe Kaltwassertemperaturen trifft. Sie ist dort ein teures Anhängsel, wo man sie nachträglich an eine auf tiefe Temperaturen ausgelegte Anlage schraubt."),
  ("p", "Die Entscheidung fällt in der Vorstudie, zusammen mit der Wahl des Übergabesystems. Später ist sie nur noch teuer korrigierbar — und dann meist als Kompromiss, der weniger bringt, als er kostet."),
 ],
},

{
 "slug": "foerdergelder-reihenfolge",
 "kategorie": "Förderung",
 "bild": "assets/img/bau-1.jpg",
 "alt": "Baustelle mit Installationsarbeiten an der Gebäudetechnik",
 "titel": "Fördergelder in der Schweiz: die Reihenfolge entscheidet",
 "teaser": "Der häufigste Grund für abgelehnte Gesuche ist kein formaler Fehler, sondern ein zu früher Baustart.",
 "lead": "Fördergelder sind kein Rabatt, den man nachträglich einlöst. Sie sind ein Verfahren mit einer festen Reihenfolge — und wer sie umstellt, verliert den Anspruch vollständig.",
 "inhalt": [
  ("p", "Die Förderlandschaft in der Schweiz ist zweistufig aufgebaut: Der Bund stellt über das Gebäudeprogramm Mittel bereit, die Kantone setzen sie um und ergänzen sie mit eigenen Programmen. Für Sie als Bauherrschaft heisst das: Die Grundsätze gleichen sich, aber Beträge, Bedingungen und Fristen unterscheiden sich von Kanton zu Kanton, teilweise erheblich."),
  ("p", "Es gibt deshalb keine allgemeingültige Antwort auf die Frage «Wie viel bekomme ich?». Es gibt nur die Antwort für Ihren Kanton, für Ihr Vorhaben, zum heutigen Stand."),

  ("h2", "Der eine Fehler, der alles kostet"),
  ("merk", "Das Gesuch muss vor Baubeginn eingereicht und in der Regel bewilligt sein. Wer vorher startet, verliert den Anspruch — rückwirkend gibt es nichts."),
  ("p", "Als Baubeginn gilt je nach Programm bereits die verbindliche Bestellung oder der Vertragsabschluss, nicht erst der Spatenstich oder die erste Montage. Das ist der Punkt, an dem die meisten Gesuche scheitern: Die Bauherrschaft hat in guter Absicht früh bestellt, um Liefertermine zu sichern, und damit den Anspruch verwirkt."),
  ("p", "Besonders bitter ist das bei Wärmeerzeugern mit langen Lieferfristen. Der Reflex, früh zu bestellen, ist betriebswirtschaftlich verständlich und förderrechtlich fatal. Wer beides braucht, muss die Bewilligungsdauer in den Terminplan aufnehmen — und nicht darauf hoffen, dass es niemand prüft."),

  ("h2", "Die Reihenfolge, die funktioniert"),
  ("ul", [
    "Kantonales Programm und aktuelle Bedingungen prüfen — die Beträge ändern sich regelmässig.",
    "Nötige Vorleistungen klären; in mehreren Kantonen ist ein GEAK Plus Voraussetzung.",
    "Gesuch mit den geforderten Unterlagen einreichen.",
    "Zusicherung abwarten.",
    "Erst dann bestellen und bauen.",
    "Nach Abschluss die Auszahlung mit den geforderten Nachweisen beantragen.",
  ]),
  ("p", "Zwischen Schritt drei und vier liegt Zeit — je nach Kanton und Auslastung mehrere Wochen. Diese Zeit gehört in den Terminplan, sonst gerät sie unter Druck, und dann entstehen genau die vorzeitigen Bestellungen, die den Anspruch kosten."),
  ("p", "Der sechste Schritt wird unterschätzt. Die Auszahlung erfolgt nicht automatisch, sondern auf Antrag und gegen Nachweis der ausgeführten Massnahme. Wer die nötigen Belege — Rechnungen, Fotos, Messprotokolle, Konformitätsnachweise — nicht während der Bauzeit sammelt, sucht sie ein Jahr später zusammen."),

  ("h2", "Was typischerweise gefördert wird"),
  ("ul", [
    "Ersatz fossiler Heizungen durch erneuerbare Systeme.",
    "Anschluss an einen Wärmeverbund.",
    "Wärmedämmung von Fassade, Dach, Boden und Fenstern.",
    "Gesamtsanierungen mit definiertem Zielwert, oft mit einem Bonus gegenüber Einzelmassnahmen.",
    "Beratungsleistungen, Energienachweise und Machbarkeitsstudien.",
  ]),
  ("p", "Der vierte Punkt lohnt die genaue Prüfung. Mehrere Kantone fördern eine zusammenhängende Sanierung deutlich stärker als dieselben Massnahmen einzeln über mehrere Jahre verteilt. Wer ohnehin etappieren muss — aus Kosten- oder Betriebsgründen — sollte die Etappierung nach den Förderbedingungen zuschneiden und nicht umgekehrt. Der Unterschied kann mehrere Zehntausend Franken betragen."),

  ("h2", "Was Sie zusätzlich prüfen sollten"),
  ("p", "Neben den kantonalen Programmen gibt es kommunale Beiträge, Förderungen von Energieversorgern und je nach Kanton steuerliche Abzüge für energetische Sanierungen. Diese Töpfe schliessen sich nicht immer gegenseitig aus — manchmal aber doch, und dann entscheidet die Kombination über den Gesamtbetrag."),
  ("p", "Bei den Steuern lohnt zudem der Blick auf die zeitliche Verteilung: In mehreren Kantonen lassen sich Sanierungskosten über mehrere Steuerperioden verteilen. Bei grösseren Vorhaben kann die Etappierung deshalb auch steuerlich relevant sein — das gehört mit dem Treuhänder besprochen, bevor die Etappen festgelegt sind."),

  ("h2", "Was das für die Planung heisst"),
  ("p", "Die Förderprüfung gehört in die Vorstudie, nicht in die Ausführungsplanung. Sie beeinflusst die Variantenwahl, den Terminplan und manchmal den Zuschnitt der Etappen. Als nachträgliche Ergänzung bringt sie meist nur noch einen Bruchteil dessen, was möglich gewesen wäre."),
  ("p", "Und ein praktischer Hinweis zum Schluss: Prüfen Sie die Bedingungen immer direkt beim Kanton und tagesaktuell. Beträge und Voraussetzungen werden regelmässig angepasst, Programme werden ausgesetzt, wenn die Mittel ausgeschöpft sind. Jede Zusammenfassung — auch diese — ist eine Momentaufnahme und ersetzt die Abklärung im Einzelfall nicht."),
 ],
},

{
 "slug": "geak-minergie-snbs",
 "kategorie": "Label",
 "bild": "assets/img/haus.jpg",
 "alt": "Modernes Wohn- und Geschäftsgebäude",
 "titel": "GEAK, Minergie, SNBS: welches Label wofür",
 "teaser": "Drei Instrumente mit drei verschiedenen Zwecken. Was jedes verlangt, was es kostet und wann es sich lohnt.",
 "lead": "Labels werden oft verwechselt, weil sie alle irgendwie mit Energie zu tun haben. Sie beantworten aber drei völlig verschiedene Fragen.",
 "inhalt": [
  ("p", "Der GEAK sagt, wie gut ein Gebäude heute ist. Minergie sagt, wie gut ein Gebäude gebaut oder saniert wird. Der SNBS sagt, wie nachhaltig ein Bauwerk insgesamt ist — Energie ist dort nur einer von vielen Aspekten. Wer diese drei Fragen auseinanderhält, kommt schneller zu einer Entscheidung."),

  ("h2", "GEAK: die Bestandsaufnahme"),
  ("p", "Der Gebäudeenergieausweis der Kantone bewertet die Gebäudehülle und die Gesamtenergieeffizienz auf einer Skala von A bis G. Er beschreibt den Ist-Zustand und verlangt keinerlei Massnahme. Für Verkauf, Vermietung und die eigene Standortbestimmung ist er das schnellste verfügbare Instrument."),
  ("p", "Der GEAK Plus ergänzt den Ausweis um einen Beratungsbericht mit mehreren Sanierungsvarianten, deren energetischer Wirkung und groben Kosten. Genau diese Variante verlangen mehrere Kantone als Voraussetzung für Fördergelder — und deshalb steht sie oft ganz am Anfang eines Projekts, noch vor der eigentlichen Planung."),
  ("merk", "Der GEAK Plus ist selten ein Selbstzweck. Er ist meist die Eintrittskarte zur Förderung."),
  ("p", "Wichtig zu wissen: Der GEAK bewertet mit standardisierten Annahmen zu Nutzung und Klima, nicht mit Ihrem tatsächlichen Verbrauch. Ein Gebäude mit schlechter Klasse und sparsamen Nutzern kann real weniger verbrauchen als eines mit besserer Klasse und intensiver Nutzung. Der GEAK vergleicht Gebäude, nicht Haushalte."),

  ("h2", "Minergie: der Baustandard"),
  ("p", "Minergie stellt Anforderungen an das fertige Gebäude: Energiekennzahl, Luftdichtheit der Hülle, kontrollierte Lüftung, thermischer Komfort im Sommer. Es ist ein Standard für Neubau und Sanierung, kein Bewertungsinstrument für den Bestand."),
  ("ul", [
    "Minergie — der Grundstandard mit Anforderungen an Energie und Komfort.",
    "Minergie-P — deutlich strengerer Energiebedarf, entsprechend höhere Anforderungen an die Hülle.",
    "Minergie-A — die Eigenversorgung über das Jahr steht im Mittelpunkt.",
    "Zusatz ECO — ergänzt die Themen Gesundheit und Bauökologie.",
  ]),
  ("p", "Der Aufwand liegt weniger in der Technik als in der Disziplin. Luftdichtheit muss gebaut und gemessen werden, nicht nur ausgeschrieben. Die Lüftung muss geplant statt nachgerüstet werden. Der sommerliche Wärmeschutz braucht einen Nachweis, der die Verschattung einschliesst — und Verschattung wird in Kostenrunden gern gestrichen."),
  ("p", "Wer diese Punkte früh einplant, hat kaum bauliche Mehrkosten. Wer sie nachträglich erfüllen muss, zahlt deutlich. Das ist der wesentliche Unterschied zwischen einem Projekt, das Minergie von Anfang an anstrebt, und einem, das es nachträglich «auch noch» erreichen will."),

  ("h2", "SNBS: das ganze Bauwerk"),
  ("p", "Der Standard Nachhaltiges Bauen Schweiz betrachtet Gesellschaft, Wirtschaft und Umwelt gemeinsam — von der Standortqualität über die Nutzungsflexibilität und die Lebenszykluskosten bis zum Rückbau. Energie ist ein Kriterium unter vielen."),
  ("p", "Er ist entsprechend umfassender und aufwendiger und lohnt sich vor allem bei grösseren Vorhaben und bei öffentlichen Bauherrschaften, die Nachhaltigkeit gegenüber Dritten belegen müssen. Für ein einzelnes Mehrfamilienhaus ist der Aufwand meist unverhältnismässig."),

  ("h2", "Was das in der Praxis kostet"),
  ("p", "Der GEAK ist die günstigste Massnahme und amortisiert sich häufig allein über die Fördergelder, zu denen er den Zugang öffnet. Er ist damit fast immer eine sinnvolle erste Investition, auch wenn noch nicht feststeht, ob und wann saniert wird."),
  ("p", "Minergie kostet Planungsaufwand, Zertifizierungsgebühren und Messungen. Bei früher Berücksichtigung bleiben die baulichen Mehrkosten überschaubar; der grösste Posten ist oft die kontrollierte Lüftung, die in vielen Fällen ohnehin sinnvoll wäre."),
  ("p", "Der SNBS verlangt zusätzlich Nachweise über den gesamten Lebenszyklus und damit eine eigene Projektorganisation. Diese Kosten sind planbar, aber sie sind nicht klein — sie gehören von Beginn an ins Budget und nicht als Nachtrag."),

  ("h2", "Eine einfache Entscheidungshilfe"),
  ("ul", [
    "Sie wollen wissen, wo Ihr Gebäude steht, und Fördergelder holen: GEAK Plus.",
    "Sie bauen oder sanieren und wollen einen belegbaren Qualitätsstandard: Minergie.",
    "Sie müssen Nachhaltigkeit gegenüber Dritten ausweisen: SNBS.",
    "Sie wollen ausschliesslich tiefere Betriebskosten: kein Label, sondern eine Betriebsoptimierung.",
  ]),
  ("p", "Der letzte Punkt ist ernst gemeint. Ein Label verbessert kein Gebäude — es beschreibt es und verpflichtet zu Anforderungen. Die Einsparung kommt aus den Massnahmen und aus dem Betrieb, nicht aus dem Zertifikat. Wer nur die Kosten senken will, investiert das Geld für die Zertifizierung besser in eine saubere Einregulierung."),
 ],
},

{
 "slug": "integrale-planung",
 "kategorie": "Planung",
 "bild": "assets/img/bau-3.jpg",
 "alt": "Planungsbesprechung auf der Baustelle",
 "titel": "Integrale Planung: warum Einzeloptimierung scheitert",
 "teaser": "Jedes Gewerk für sich optimiert ergibt kein optimales Gebäude. Wo die Schnittstellen liegen und wann sie geklärt sein müssen.",
 "lead": "Ein Gebäude, in dem jedes Gewerk für sich das Beste herausgeholt hat, ist selten ein gutes Gebäude. Meistens ist es ein teures.",
 "inhalt": [
  ("p", "Die Fassade wird auf minimalen Wärmeverlust optimiert. Die Lüftung auf minimalen Druckverlust. Die Heizung auf tiefe Investitionskosten. Jedes Gewerk hat seine Sache gut gemacht — und zusammen ergibt sich eine Anlage, die im Sommer überhitzt, im Winter zu trocken ist und deren Regelung nach zwei Jahren niemand mehr versteht."),
  ("p", "Das ist kein Vorwurf an die Beteiligten. Es ist die zwangsläufige Folge einer Planung, in der die Optimierungsziele nie miteinander abgeglichen wurden."),

  ("h2", "Die drei teuersten Schnittstellen"),
  ("p", "Erstens: Hülle und Kühlung. Der Glasanteil und die Verschattung entscheiden über die Kühllast — und damit über Kälteerzeugung, Kanalquerschnitte, Steigzonen und Technikflächen. Wird die aussenliegende Verschattung aus Kostengründen gestrichen, wächst die Haustechnik um ein Vielfaches der eingesparten Summe. Diese Rechnung wird selten aufgemacht, weil die beiden Positionen in verschiedenen Budgets stehen."),
  ("p", "Zweitens: Statik und Verteilung. Deckendurchbrüche, Schachtlagen und lichte Höhen bestimmen, ob die Verteilung sauber geführt werden kann. Wer das spät klärt, baut Umwege — und jeder Umweg kostet Druckverlust, also dauerhaft Strom für Pumpen und Ventilatoren, über die gesamte Lebensdauer."),
  ("p", "Drittens: Nutzung und Regelung. Wenn die tatsächliche Nutzung erst in der Ausführungsplanung feststeht, ist die Regelstrategie bereits gebaut. Sie wird dann angepasst statt entworfen — der häufigste Grund für Anlagen, die «irgendwie laufen», aber niemand mehr durchschaut."),
  ("merk", "Die teuersten Entscheidungen fallen in den Phasen, in denen am wenigsten Geld ausgegeben wird."),

  ("h2", "Die Kostenkurve über die Projektphasen"),
  ("p", "In der Vorstudie kostet eine Änderung fast nichts und wirkt maximal — man verschiebt eine Linie im Schema. In der Bauprojektphase kostet dieselbe Änderung spürbar mehr und wirkt begrenzt. In der Ausführungsplanung kostet sie ein Vielfaches. Auf der Baustelle ist sie kaum noch bezahlbar und meist nur als Kompromiss umsetzbar."),
  ("p", "Trotzdem wird der Haustechnikplaner traditionell spät beigezogen — oft erst, wenn Geometrie, Fassade und Grundrisse feststehen. Genau dann sind die Freiheitsgrade weg, die über die Effizienz entschieden hätten. Was danach kommt, ist Schadensbegrenzung mit technischen Mitteln."),

  ("h2", "Was integrale Planung praktisch bedeutet"),
  ("ul", [
    "Haustechnik ab der Vorstudie am Tisch, nicht ab dem Bauprojekt.",
    "Ein gemeinsames Energie- und Raumklimakonzept, bevor die Fassade fixiert wird.",
    "Schacht- und Technikflächen als frühe Setzung, nicht als Restfläche nach dem Ausbau.",
    "Nutzungsprofile schriftlich, mit dem künftigen Betreiber abgestimmt.",
    "Ein Verantwortlicher für die Schnittstellen, benannt und mit Entscheidungsbefugnis ausgestattet.",
    "Eine gemeinsame Variantenbetrachtung statt paralleler Einzeloptimierungen.",
  ]),
  ("p", "Der fünfte Punkt ist der wirksamste und der am seltensten umgesetzte. Schnittstellen gehören niemandem — deshalb bleiben sie liegen, bis sie zum Problem werden. Eine benannte Person mit dem Auftrag, genau diese Nahtstellen zu bewirtschaften, verhindert mehr Kosten als jede technische Massnahme."),

  ("h2", "Der Betreiber gehört an den Tisch"),
  ("p", "Wer das Gebäude später betreibt, weiss Dinge, die in keinem Raumbuch stehen: wann die Räume wirklich genutzt werden, wo im letzten Bau die Störungen aufgelaufen sind, welche Bedienung im Alltag funktioniert und welche nach drei Monaten überbrückt wird."),
  ("p", "Diese Erfahrung kostet nichts und ersetzt viele Annahmen — aber nur, wenn man sie einholt, bevor entschieden ist. Ein Betreiber, der das fertige Konzept vorgelegt bekommt, kann nur noch Bedenken anmelden. Einer, der in der Vorstudie gefragt wird, liefert Grundlagen."),

  ("h2", "Woran man erkennt, dass es funktioniert hat"),
  ("p", "An der Regelung. Ein Gebäude, dessen Gewerke aufeinander abgestimmt sind, braucht eine einfache Regelstrategie: wenige Betriebsarten, klare Sollwerte, nachvollziehbare Abhängigkeiten. Wo die Regelung kompliziert wird, gleicht sie in aller Regel etwas aus, das baulich hätte gelöst werden können."),
  ("p", "Komplexität in der Gebäudeautomation ist häufig die Rechnung für eine Entscheidung, die zwei Planungsphasen früher gefallen ist. Man bezahlt sie nicht einmal, sondern jedes Jahr — in Betriebsaufwand, in Störungen und in Energie."),
 ],
},

{
 "slug": "messkonzept-monitoring",
 "kategorie": "Betrieb",
 "bild": "assets/img/technik-1.jpg",
 "alt": "Zählerinstallation mit Wärmezählern",
 "titel": "Messkonzept: ohne Zähler keine Steuerung",
 "teaser": "Welche Messpunkte man wirklich braucht, welche Kennzahlen etwas aussagen und warum ein Zähler zu wenig schlimmer ist als zehn zu viel.",
 "lead": "Fast jedes Gebäude hat Zähler. Fast keines hat ein Messkonzept. Der Unterschied zeigt sich in dem Moment, in dem jemand fragt, warum der Verbrauch gestiegen ist.",
 "inhalt": [
  ("p", "Ein Hauptzähler sagt Ihnen, dass Sie mehr verbrauchen. Er sagt Ihnen nicht, wo. Damit ist er für die Rechnung geeignet und für die Steuerung wertlos. Ein Messkonzept unterscheidet sich davon in genau einem Punkt: Es ist so aufgebaut, dass jede Abweichung einer Ursache zugeordnet werden kann."),

  ("h2", "Die Grundregel"),
  ("merk", "Messen Sie dort, wo Sie später eine Entscheidung treffen wollen — nicht dort, wo der Zähler am einfachsten zu montieren ist."),
  ("p", "Daraus folgt die Struktur fast von selbst: getrennt nach Erzeugung, nach Verbrauchergruppe und nach Mietbereich oder Nutzungseinheit. Wer diese drei Ebenen hat, kann jede Auffälligkeit eingrenzen — zuerst auf die Ebene, dann auf den Bereich, dann auf die Anlage."),
  ("p", "Ohne diese Struktur bleibt jede Diskussion über den Verbrauch eine Meinungsdiskussion. Mit ihr wird sie zu einer Frage von zwanzig Minuten am Bildschirm."),

  ("h2", "Was mindestens gemessen gehört"),
  ("ul", [
    "Wärme je Erzeuger — bei Wärmepumpen zwingend zusammen mit dem zugehörigen Strom, sonst gibt es keine Jahresarbeitszahl.",
    "Wärme je Verbrauchergruppe: Heizung, Trinkwarmwasser, Lüftungserwärmung.",
    "Kälte je Erzeuger und je Verbrauchergruppe.",
    "Strom getrennt nach Wärmepumpe, Kälteerzeugung, Lüftung und Allgemeinstrom.",
    "Wasser gesamt, bei grösseren Bauten zusätzlich das Warmwasser separat.",
    "Bei Photovoltaik: Erzeugung, Eigenverbrauch und Einspeisung getrennt.",
  ]),
  ("p", "Der erste Punkt ist der wichtigste und wird am häufigsten vergessen. Ohne den zugeordneten Stromzähler lässt sich die Effizienz einer Wärmepumpe nicht bestimmen — und damit auch nicht belegen, ob sie hält, was die Auslegung versprochen hat. Bei einer Investition dieser Grössenordnung ist das ein erstaunlicher blinder Fleck."),
  ("p", "Der zweite Punkt macht die grösste Einzelposition sichtbar. In gut gedämmten Gebäuden übersteigt der Wärmebedarf für Trinkwarmwasser den für die Heizung — ohne getrennte Messung merkt das niemand, und alle Optimierungsbemühungen richten sich auf den kleineren Posten."),

  ("h2", "Kennzahlen, die etwas aussagen"),
  ("ul", [
    "Jahresarbeitszahl der Wärmeerzeugung, gerechnet über ein volles Jahr.",
    "Wärmebedarf je Quadratmeter Energiebezugsfläche und Jahr, witterungsbereinigt.",
    "Stromverbrauch der Lüftung je gefördertem Kubikmeter Luft.",
    "Anteil Trinkwarmwasser am gesamten Wärmebedarf.",
    "Verhältnis von Grundlast zu Spitzenlast.",
  ]),
  ("p", "Die letzte Kennzahl ist die unterschätzteste. Eine hohe Grundlast in einem Gebäude, das nachts und am Wochenende leer steht, ist der zuverlässigste Hinweis auf ein Zeitprogramm, das nicht stimmt — und damit auf die günstigste Einsparung, die es gibt."),
  ("p", "Die Witterungsbereinigung beim zweiten Punkt ist kein Detail. Ohne sie vergleichen Sie einen milden mit einem kalten Winter und ziehen daraus Schlüsse über Ihre Anlage."),

  ("h2", "Datenpunkte sind kein Monitoring"),
  ("p", "Eine moderne Gebäudeautomation liefert Tausende von Werten. Ohne Aufbereitung sind sie ein Archiv, kein Werkzeug. Nützlich wird es erst mit drei Dingen: einer sauberen Zuordnung der Zähler zu Bereichen, einer Ablage über mehrere Jahre und wenigen Auswertungen, die regelmässig tatsächlich jemand anschaut."),
  ("p", "Wenige Auswertungen, die angeschaut werden, sind mehr wert als viele, die niemand öffnet. Ein monatlicher Blick auf fünf Kennzahlen findet mehr als ein Dashboard mit zweihundert Kacheln, das nach vier Wochen niemand mehr aufruft."),
  ("p", "Dazu gehört auch eine banale organisatorische Frage: Wer schaut hin, wie oft, und wen informiert diese Person, wenn etwas auffällt? Ohne diese Antwort bleibt das beste Monitoring folgenlos."),

  ("h2", "Wann das Konzept entstehen muss"),
  ("p", "In der Projektierung. Zähler nachzurüsten bedeutet, Leitungen aufzutrennen — im laufenden Betrieb aufwendig, teuer und oft nur in Betriebsferien möglich. Die Mehrkosten für einen zusätzlichen Zähler im Neubau sind dagegen gering, gemessen an dem, was er über zwanzig Jahre an Klärung erspart."),
  ("p", "Ein Zähler zu wenig kostet Sie später Diskussionen ohne Grundlage, Gutachten und im schlechtesten Fall eine Fehlinvestition. Zehn zu viel kosten Sie einmalig etwas Geld und ein wenig Platz im Schacht. Die Asymmetrie ist eindeutig — und trotzdem wird beim Messkonzept regelmässig zuerst gespart."),
 ],
},

]
