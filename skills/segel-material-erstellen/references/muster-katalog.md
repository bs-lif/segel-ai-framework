# Katalog: Anti-Patterns und Aktivierungsmuster

Grundlage für die Beratung in Phase 1 und für die Durchsicht von Entwürfen. In Gesprächen die ID nennen (z. B. „A1“), damit Entscheidungen in `STATUS.md` nachvollziehbar bleiben.

## Anti-Patterns

| ID | Name | Woran erkennbar | Stattdessen |
|---|---|---|---|
| A1 | Textwüste | Mehrere Bildschirmseiten Erklärtext ohne Aufgabe dazwischen | Text in kurze Häppchen teilen, nach jedem eine Aktivierung (M1, M7, M9) |
| A2 | Kochrezept | Schritt-für-Schritt-Anleitung, die man ohne Nachdenken abtippt | Ziel vorgeben, Weg offen lassen; gestufte Hilfen (M3) statt fertiger Schritte |
| A3 | Einheitsweg | Ein einziger Pfad für alle, kein Angebot für Schnelle oder Langsame | Basis- und Vertiefungspfad (M4), redundante Quellen (SeGeL) |
| A4 | Ratbare Fragen | Multiple Choice mit offensichtlicher Lösung, Ausschlussverfahren genügt | Begründung verlangen, plausible Distraktoren, Ausgabe interpretieren (M7) |
| A5 | Ungeprüfte Selbstüberprüfung | Aufgabe ohne Lösung, erwartetes Ergebnis oder Prüfbefehl | Selbstkontrolle immer mitliefern (SeGeL) |
| A6 | Guide als Lehrbuch | Guide erklärt Inhalte selbst | Guide kurz halten, nur Richtung und Verweise (SeGeL) |
| A7 | Sammel-Checkpunkt | Checklistenpunkt enthält mehrere Fähigkeiten oder ist nicht prüfbar | Ein „Ich kann …“ je Fähigkeit, beobachtbares Verb |
| A8 | Reine Wiedergabe | Fragen fragen nur Begriffe oder Definitionen ab | Anwendung, Fehlersuche, Transfer (M2, M5) |
| A9 | Doppelte Wahrheit | Simulation, Fragen und Lösungen werden getrennt gepflegt | Ein Szenario als Datenstruktur, alles daraus erzeugen |
| A10 | Feste Reihenfolge | Antworten oder Zuordnungen stehen bei jedem Aufruf gleich, z. B. richtige Zuordnung auf der Diagonale | Reihenfolge bei jedem Durchlauf neu mischen |
| A11 | Längste Antwort ist richtig | Die richtige Option ist als einzige lang, begründet oder differenziert | Alle Optionen gleich lang und gleich begründet formulieren |
| A12 | Ungeklärte Voraussetzung | Aufgabe verlangt einen Befehl, Begriff oder eine Option, die vorher nirgends eingeführt wurde | Vor der ersten Aufgabe einführen, z. B. mit Befehlskasten (M11) |
| A13 | Simulation aus dem Gedächtnis | Simulierte Ausgaben, Meldungen oder Oberflächen sind nachempfunden statt aus der echten Zielversion übernommen | Referenzinstallation, Rohausgaben unter `quellen/referenz/` ablegen |
| A14 | Lückenhafte Simulation | Eingebaute Hilfe (`--help`) fehlt, Shell-Verkettung führt zu unsinnigen Folgefehlern, typische Fehleingaben ohne hilfreiche Meldung, Konfigurationsdatei nicht bearbeitbar oder nur per Zeichenkettenvergleich geprüft | Hilfe originalgetreu, `&&`/`\|\|`/`;` nachbilden, Nicht-Nachgebildetes klar melden, Editor nachbilden und Datei wirklich parsen |
| A15 | Sackgasse | Lernende können etwas irreversibel kaputtmachen (Datei verhunzt, Image gelöscht, Prozess hängt) und kommen nicht zurück | Knopf „Seite zurücksetzen“; im Durchlauftest je Seite einmal kaputtmachen und zurücksetzen |
| A16 | Verfallende Rückfrage | Bestätigung („Wirklich zurücksetzen?“) verfällt nach wenigen Sekunden, der Knopf wirkt kaputt | Rückfrage gilt bis zur nächsten Aktion bzw. bis zum Neuzeichnen |

## Aktivierungsmuster

| ID | Name | Kurzbeschreibung | Passt besonders bei |
|---|---|---|---|
| M1 | Vorhersage | „Was passiert, wenn …?“ – erst vermuten, dann ausprobieren, dann erklären | Befehle, Konfigurationen, Abläufe |
| M2 | Fehlersuche | Fehlerhafte Konfiguration, Code oder Ausgabe; Fehler finden und begründen | Technik-Themen, Vertiefung |
| M3 | Gestufte Hilfen | Hinweis 1, Hinweis 2, Lösung – einzeln aufklappbar | Aufgaben mit Hängergefahr |
| M4 | Wahlpfade | Basis- und Expertenpfad, Wahlaufgaben | Heterogene Klassen |
| M5 | Transfer | Gelerntes auf einen neuen, eigenen Fall anwenden | Abschluss eines Abschnitts |
| M6 | Zuordnen mit Begründung | Sortieren oder Zuordnen, mindestens ein Fall mit Begründung | Begriffe, Kategorien |
| M7 | Ausgabe deuten | Echte Logs, Befehlsausgaben oder Screenshots interpretieren | Diagnose, Systemverständnis |
| M8 | Challenge mit Prüfbefehl | Kleines Ziel, dessen Erreichen ein Befehl oder Test belegt | Praktische Übungen, Selbstüberprüfung |
| M9 | Selbsterklärung | „Erkläre in zwei Sätzen …“, danach Musterlösung zum Vergleich | Nach Texten und Videos |
| M10 | Peer-Check | Ergebnis mit Mitlernenden vergleichen oder gegenseitig erklären | Pull-Prinzip, Präsenzphasen |
| M11 | Befehlskasten | Kasten „Befehle dieser Seite“ an fester Stelle vor der ersten Aufgabe: Syntax mit Platzhaltern, kein fertiger Aufgabenbefehl; Hilfe-Knopf nur für Hänger | Konsolen-Simulationen, gegen A12 |
