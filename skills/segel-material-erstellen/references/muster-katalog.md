# Katalog: Anti-Patterns und Aktivierungsmuster

Grundlage für die Beratung in Phase 1 und für die Durchsicht von Entwürfen. In Gesprächen die ID nennen (z. B. „A1“), damit Entscheidungen in `STATUS.md` nachvollziehbar bleiben. Die Spalte „Standard“ verweist auf die Prinzipien und Grundsätze in `prinzipien.md`.

## Anti-Patterns

| ID | Name | Woran erkennbar | Stattdessen | Standard |
|---|---|---|---|---|
| A1 | Textwüste | Mehrere Bildschirmseiten Erklärtext ohne Aufgabe dazwischen | Text in kurze Häppchen teilen, nach jedem eine Aktivierung (M1, M7, M9) | P7 |
| A2 | Kochrezept | Schritt-für-Schritt-Anleitung, die man ohne Nachdenken abtippt | Ziel vorgeben, Weg offen lassen; gestufte Hilfen (M3) statt fertiger Schritte | P2 |
| A3 | Einheitsweg | Ein einziger Pfad für alle, kein Angebot für Schnelle oder Langsame | Basis- und Vertiefungspfad (M4), redundante Quellen (SeGeL) | P11 |
| A4 | Ratbare Fragen | Multiple Choice mit offensichtlicher Lösung, Ausschlussverfahren genügt | Begründung verlangen, plausible Distraktoren, Ausgabe interpretieren (M7) | G3 |
| A5 | Ungeprüfte Selbstüberprüfung | Aufgabe ohne Lösung, erwartetes Ergebnis oder Prüfbefehl | Selbstkontrolle immer mitliefern (SeGeL) | P11 |
| A6 | Guide als Lehrbuch | Guide erklärt Inhalte selbst | Guide kurz halten, nur Richtung und Verweise (SeGeL) | P11 |
| A7 | Sammel-Checkpunkt | Checklistenpunkt enthält mehrere Fähigkeiten oder ist nicht prüfbar | Ein „Ich kann …“ je Fähigkeit, beobachtbares Verb | P8 |
| A8 | Reine Wiedergabe | Fragen fragen nur Begriffe oder Definitionen ab | Anwendung, Fehlersuche, Transfer (M2, M5) | P8 |
| A9 | Doppelte Wahrheit | Simulation, Fragen und Lösungen werden getrennt gepflegt | Ein Szenario als Datenstruktur, alles daraus erzeugen | G6 |
| A10 | Feste Reihenfolge | Antworten oder Zuordnungen stehen bei jedem Aufruf gleich, z. B. richtige Zuordnung auf der Diagonale | Reihenfolge bei jedem Durchlauf neu mischen | G3 |
| A11 | Längste Antwort ist richtig | Die richtige Option ist als einzige lang, begründet oder differenziert | Alle Optionen gleich lang und gleich begründet formulieren | G3 |
| A12 | Ungeklärte Voraussetzung | Aufgabe verlangt einen Befehl, Begriff oder eine Option, die vorher nirgends eingeführt wurde | Vor der ersten Aufgabe einführen, z. B. mit Befehlskasten (M11) | G2 |
| A13 | Simulation aus dem Gedächtnis | Simulierte Ausgaben, Meldungen oder Oberflächen sind nachempfunden statt aus der echten Zielversion übernommen | Referenzinstallation, Rohausgaben unter `quellen/referenz/` ablegen | G6 |
| A14 | Lückenhafte Simulation | Eingebaute Hilfe (`--help`) fehlt, Shell-Verkettung führt zu unsinnigen Folgefehlern, typische Fehleingaben ohne hilfreiche Meldung, Konfigurationsdatei nicht bearbeitbar oder nur per Zeichenkettenvergleich geprüft | Hilfe originalgetreu, `&&`/`\|\|`/`;` nachbilden, Nicht-Nachgebildetes klar melden, Editor nachbilden und Datei wirklich parsen | G1, G4 |
| A15 | Sackgasse | Lernende können etwas irreversibel kaputtmachen (Datei verhunzt, Image gelöscht, Prozess hängt) und kommen nicht zurück | Knopf „Seite zurücksetzen“; im Durchlauftest je Seite einmal kaputtmachen und zurücksetzen | G5 |
| A16 | Verfallende Rückfrage | Bestätigung („Wirklich zurücksetzen?“) verfällt nach wenigen Sekunden, der Knopf wirkt kaputt | Rückfrage gilt bis zur nächsten Aktion bzw. bis zum Neuzeichnen | G5 |
| A17 | Rumprobieren ohne Auftrag | „Probiert einfach mal aus“ ohne Leitfrage und Rückmeldung | Auftrag, Leitfrage, Rückmeldung (M1) | P4 |
| A18 | Leeres Lob | „Super!“ oder nur ein Punktestand als Rückmeldung | Warum richtig/falsch, nächster Schritt | P6 |
| A19 | Harte Sperre | Im Entdecken und Üben geht es erst weiter, wenn alles richtig ist | Nächsten Schritt vorschlagen statt sperren; lenken ist erlaubt, wenn ein Ausweg wie „Schritt überspringen“ immer sichtbar bleibt | P11, G1 |
| A20 | Aufgezwungene Hilfe | Lange Erklärungen und Beispiele sind Pflicht, auch für Könner | Kurzfassung sichtbar, Ausführliches aufklappbar, Vorwissens-Check mit Überspring-Empfehlung (M14) | P3, G1 |
| A21 | Fertiger Spickzettel | Cheat Sheet zum Herunterladen statt eigener Sicherung, womöglich vor dem Abschlusscheck | Merkblatt zum Ergänzen nach dem Abschlusscheck (M16) | P13 |
| A22 | Rangliste | Vergleich mit Mitlernenden, Punkte als Selbstzweck | Fortschritt an Lernzielen oder eigener früherer Leistung | P12 |
| A23 | Lerntypen-Varianten | Eigene Fassungen für „visuelle“ oder „auditive“ Lerntypen | Nicht belegt – stattdessen Text und Bild zusammen für alle | P7 |

## Aktivierungsmuster

| ID | Name | Kurzbeschreibung | Passt besonders bei | Standard |
|---|---|---|---|---|
| M1 | Vorhersage | „Was passiert, wenn …?“ – erst vermuten, dann ausprobieren, dann erklären | Befehle, Konfigurationen, Abläufe | P4 |
| M2 | Fehlersuche | Fehlerhafte Konfiguration, Code oder Ausgabe; Fehler finden und begründen | Technik-Themen, Vertiefung | P2 |
| M3 | Gestufte Hilfen | Immer drei Stufen, einzeln anzufordern: Denkanstoß, Teillösung bzw. Verweis, Lösung mit Begründung; zählen im Üben nicht, im Abschlusscheck gibt es keine | Aufgaben mit Hängergefahr | P2 |
| M4 | Wahlpfade | Basis- und Expertenpfad, Wahlaufgaben | Heterogene Klassen | P11 |
| M5 | Transfer | Gelerntes auf einen neuen, eigenen Fall anwenden | Abschluss eines Abschnitts | P2 |
| M6 | Zuordnen mit Begründung | Sortieren oder Zuordnen, mindestens ein Fall mit Begründung | Begriffe, Kategorien | P5 |
| M7 | Ausgabe deuten | Echte Logs, Befehlsausgaben oder Screenshots interpretieren | Diagnose, Systemverständnis | P4 |
| M8 | Challenge mit Prüfbefehl | Kleines Ziel, dessen Erreichen ein Befehl oder Test belegt | Praktische Übungen, Selbstüberprüfung | P11 |
| M9 | Selbsterklärung | „Erkläre in zwei Sätzen …“, danach Musterlösung zum Vergleich | Nach Texten und Videos | P11 |
| M10 | Peer-Check | Ergebnis mit Mitlernenden vergleichen oder gegenseitig erklären | Pull-Prinzip, Präsenzphasen | P11 |
| M11 | Befehlskasten | Kasten „Befehle dieser Seite“ an fester Stelle vor der ersten Aufgabe: Syntax mit Platzhaltern, kein fertiger Aufgabenbefehl; Hilfe-Knopf nur für Hänger | Konsolen-Simulationen, gegen A12 | G2 |
| M12 | Lösungsbeispiel zuerst | Vollständig gelöstes Beispiel mit Begründung je Schritt vor dem ersten eigenen Versuch, überspringbar | Neue Aufgabentypen, Einsteiger | P3 |
| M13 | Kurz-Check | 3–5 unbewertete Fragen am Abschnittsende, als „zählt nicht“ markiert, ab Abschnitt 3 mit Wiederholungsfrage | Jedes Material mit Abschnitten | P5, P10 |
| M14 | Vorwissens-Check | Je Lernziel eine Frage am Anfang, daraus Empfehlung, was übersprungen werden kann | Heterogene Klassen | P3, P11 |
| M15 | Selbsteinschätzung vorher/nachher | Je Lernziel „Das kann ich schon / noch nicht“ zu Beginn und nach dem Abschlusscheck | SeGeL, Selbststeuerung | P11 |
| M16 | Merkblatt zum Ergänzen | Halb vorgefülltes Merkblatt je Lernziel nach dem Abschlusscheck, aus dem Gedächtnis ergänzen, mit Muster vergleichen, Selbsttest zum späteren Wiederholen | Abschluss, Lernportfolio | P13, P10 |
