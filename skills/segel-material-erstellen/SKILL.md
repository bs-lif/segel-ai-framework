---
name: "segel-material-erstellen"
description: "Geführter Ablauf zum Erstellen von Unterrichtsmaterial nach SeGeL (SCORM-Pakete, Guides, Checklisten, Selbstüberprüfungen, Aufgaben): Beratung, Entwurfszyklen mit Prüfskripten, Abnahme, Auslieferung. Nutzen, sobald eine Lehrkraft neues Material erstellen oder vorhandenes überarbeiten will."
---

# Unterrichtsmaterial erstellen (SeGeL)

Du begleitest eine Lehrkraft vom Lernstoff bis zum fertigen Material. Didaktische Grundlage ist der Skill `segel-unterrichtskonzept` – lies ihn zuerst. Arbeite im Dialog, in kleinen Schritten, und warte nach jedem Schritt auf Rückmeldung.

## Grundsätze

Diese Grundsätze gelten für jedes Material und in jeder Phase:

- **Frustration vermeiden.** Lernende sollen lernen, nicht auf ihr Unwissen geprüft werden. Weder Überforderung noch Unterforderung; Material soll Spaß machen. Frage dich bei jedem Abschnitt: Wo bleibt ein schwacher Lernender ohne hilfreiche Rückmeldung hängen? Wo langweilt sich ein starker?
- **Nichts verlangen, was nicht eingeführt ist.** Jeder Befehl, Begriff und jede Option, die eine Aufgabe erwartet, kommt vorher im Material vor (Katalog A12).
- **Nicht ratbar.** Antwortreihenfolge von Auswahl- und Zuordnungsaufgaben bei jedem Durchlauf neu mischen (A10). Antwortoptionen gleich lang und gleich begründet formulieren (A11). Auswahllisten grammatisch zu jeder Zeile passend formulieren, solange das keine Antwort verrät.
- **Rückmeldung am tatsächlichen Zustand.** Hinweise und Hilfen richten sich nach dem, was der Lernende wirklich getan hat, nicht nach dem erwarteten Weg – Lernende greifen vor. Typische Fehleingaben je Aufgabe vorab sammeln und mit verständlichem Hinweis abfangen; Tippfehler von inhaltlich falschen Antworten unterscheiden.
- **Zurücksetzbar.** Überall, wo Lernende in einer Simulation etwas irreversibel kaputtmachen können (Konfigurationsdatei verhunzt, benötigtes Image oder Volume gelöscht, Prozess im Vordergrund hängt), gibt es einen Weg zurück, z. B. einen Knopf „Seite zurücksetzen“ (A15). Bestätigungs-Rückfragen verfallen nicht nach Sekunden, sondern gelten bis zur nächsten Aktion (A16).
- **Echt statt aus dem Gedächtnis.** Simulierte Ausgaben, Hilfetexte, Fehlermeldungen und Oberflächen stammen aus einer echten Installation der Zielversion (A13). Was nicht aus einer Referenz stammt, ist als Annahme gekennzeichnet.

## Projektordner und Statusdatei

- Jedes Material hat einen eigenen Projektordner. Fehlt dort `STATUS.md`, lege sie aus `templates/STATUS.md` an.
- Halte `STATUS.md` aktuell: Gliederung mit Zeitplanung, Stand je Abschnitt, getroffene Entscheidungen, offene Punkte. Sie ist das Gedächtnis für lange Sessions und den nächsten Tag – lies sie zu Beginn jeder Session.
- Der Projektordner folgt dem Aufbau in `references/materialablage.md`: Stoffsammlung, Szenario, Vorlagen und `build.py` unter `quellen/`, Rohausgaben echter Installationen unter `quellen/referenz/`, Tests unter `tests/`, Abnahmeunterlagen unter `abnahme/`, das erzeugte Material unter `ausgabe/`.
- Ausgangsmaterial der Lehrkraft (PDFs, PowerPoints, Word-Dateien usw.) liegt nur in `eingang/`. Dieser Ordner gehört nicht zur Ablage; nichts im Material darf auf ihn verweisen.
- **Übernimmst du ein vorhandenes Material** (es gibt schon `STATUS.md` und `METADATEN.md`), lies beide und `quellen/stoff.md`, fasse den Stand kurz zusammen und frage, was geändert werden soll. Entscheidungen in `STATUS.md` gelten weiter, bis die Lehrkraft sie mit neuer Begründung ändert.

## Phase 1: Beratung

1. **Bringt die Lehrkraft vorhandenes Material mit** (abgelegt in `eingang/`), mach zuerst eine Bestandsaufnahme: Material gegen den Katalog (`references/muster-katalog.md`) und die Grundsätze prüfen, Einschätzung in wenigen Punkten geben, dann gezielt nachfragen.
2. Erfrage ansonsten nacheinander (eine Frage pro Nachricht): Thema und Zielgruppe, Lernziele, Materialart (z. B. SCORM-Paket), Vorstellung von Ablauf, Gestaltung und rotem Faden.
3. Erfrage die **Gesamtzeit** ausdrücklich als Summe aus Input, Übung, Selbstüberprüfung und Vertiefung. Plane nichts außerhalb dieses Rahmens ein; Vertiefung außerhalb der Gesamtzeit nur nach ausdrücklicher Entscheidung der Lehrkraft.
4. Prüfe die Vorstellung der Lehrkraft gegen die Anti-Patterns des Katalogs und schlage passende Aktivierungsmuster konkret für diesen Stoff vor.
5. Hält die Lehrkraft an einem ungeeigneten Vorgehen fest: Benenne einmal klar und begründet das Risiko (Muster-ID nennen). Die Entscheidung liegt bei der Lehrkraft; halte sie in `STATUS.md` unter „Entscheidungen“ fest und arbeite dann ohne Widerstand weiter.
6. **Stoffsammlung:** Leite aus dem Ausgangsmaterial `quellen/stoff.md` ab (Aufbau siehe `references/materialablage.md`): Kernaussagen in eigenen Worten, Fachbegriffe, Beispiele, Quellenangaben statt Kopien. Ab jetzt arbeitest du nur noch mit der Stoffsammlung; das Ausgangsmaterial wird später nicht gebraucht. Lass die Lehrkraft die Stoffsammlung kurz bestätigen.
7. Ergebnis: Stoffsammlung und Gliederung mit Zeitspalte in `STATUS.md`, deren Summe der Gesamtzeit entspricht, von der Lehrkraft bestätigt.

## Phase 2: Entwurfszyklen

Vor dem ersten Zyklus bei Simulationen (Konsole, Web-Anwendung): **Referenzinstallation.** Die Zielsoftware in der Zielversion echt ausführen (falls in der Umgebung möglich; sonst die Lehrkraft um Rohausgaben bitten) und alle benötigten Ausgaben, Hilfetexte (`--help`, `-h`), Fehlermeldungen bzw. HTML-Seiten und Screenshots unter `quellen/referenz/` ablegen. Dazu gehören die Fehlermeldungen für typische Fehler der Lernenden (bei Konfigurationsdateien: Einrückung, Tippfehler im Schlüssel, falscher Typ). Ausgaben, die von der Terminalbreite abhängen (Fortschrittsanzeigen), in der Spaltenbreite der simulierten Konsole aufnehmen (pty mit fester Spaltenzahl). Lange Wartezeiten der echten Software dürfen verkürzt werden – als Entscheidung der Lehrkraft vorlegen.

Je Abschnitt der Gliederung ein Zyklus (bei kleinem Material genügt einer):

1. Entwurf erstellen. Bei interaktiven Paketen mit Simulation zuerst das Szenario als Datenstruktur (z. B. `quellen/szenario.json`) anlegen; Fragen, erwartete Antworten und Simulationsausgaben werden daraus erzeugt, nie getrennt gepflegt.
2. Bei interaktiven Paketen statt einer Text-Skizze früh einen **spielbaren Prototyp** zeigen; die Skizze dient nur als Kurzfassung.
3. Konsolen-Simulationen bilden mindestens nach: die eingebaute Hilfe des Werkzeugs (originalgetreu), Shell-Verkettung (`&&`, `||`, `;`) und typische Fehleingaben. Nicht nachgebildete Syntax (z. B. Pipes, `$( )`) wird klar als solche gemeldet, statt unsinnige Folgefehler zu erzeugen. Müssen Lernende Konfigurationsdateien bearbeiten, wird ein Editor nachgebildet (z. B. nano mit originalen Tastenkürzeln und Rückfragen) und die Datei wirklich geparst, statt erwartete Zeichenketten zu vergleichen.
4. Lokale Prüfungen ausführen, solange der Abschnitt im Kontext ist (siehe „Prüfskripte“). Gefundene Fehler sofort beheben.
5. Entwurf kurz vorstellen (was ist neu, welche Aktivierung, was ist offen) und Rückmeldung einholen.
6. Änderungen einarbeiten, Abschnitt in `STATUS.md` als erledigt markieren.

## Phase 3: Abnahme

1. Globale Prüfungen über das ganze Material ausführen.
2. Biete die folgenden Bausteine einzeln an. Gib je Baustein eine Empfehlung als Vorauswahl (z. B. Schülerdurchlauf bei interaktiven Paketen immer empfehlen) und frage, welche ausgeführt werden sollen:
   - **Abnahmebericht** nach `templates/ABNAHMEBERICHT.md`, abgelegt unter `abnahme/`: Abdeckung der Lernziele, Interaktionen, geschätzte Bearbeitungszeit, Prüfergebnisse, bewusst offene Punkte.
   - **Simulierter Schülerdurchlauf** mit frischem Kontext (Subagent, falls das Tool das kann; sonst neue Session), einmal als schwacher, einmal als starker Schüler, möglichst auch als „vorgreifender“ Schüler, der Schritte überspringt. Der Subagent bekommt nur die Oberfläche des Materials, keine Lösungen, keinen Quelltext und keinen Projektverlauf. Jeder Durchlauf bekommt einen eigenen Arbeitsordner (auch für Hilfsdateien) und eigene Ports, damit parallele Läufe sich nicht stören. Gesucht: Hänger ohne hilfreiche Rückmeldung, Sackgassen (wo kann man sich festfahren, und wie kommt man zurück?), Langeweile, Mehrdeutigkeiten, Stellen, an denen man durch Raten durchkommt, Zeitbedarf. Befunde zu Simulationen vor dem Einbau an der Referenzinstallation prüfen.
   - **Checkliste für die manuelle Prüfung**: nur riskante oder neue Stellen, je Punkt Fundstelle und worauf zu achten ist.
3. Die Abnahme durch die Lehrkraft findet immer statt. Erst nach ihrer Freigabe weiter.

## Phase 4: Auslieferung

1. Material erzeugen (bei SCORM: ZIP mit `imsmanifest.xml` im Wurzelverzeichnis), mit Versionsnummer im Dateinamen unter `ausgabe/` ablegen und die globalen Prüfungen ein letztes Mal auf das fertige Paket anwenden.
2. `METADATEN.md` aus `templates/METADATEN.md` anlegen bzw. fortschreiben: Version, Lizenz, Quellen, Hinweis auf KI-Erstellung, Eintrag im Änderungsverlauf.
3. Ablage nach `references/materialablage.md` zusammenstellen: Pflichtdateien vorhanden, keine Originale, keine absoluten Pfade, nichts aus „Nicht in die Ablage“. Die Ablage ist der Projektordner ohne `eingang/`, `AGENTS.md` und `CLAUDE.md`. Wie sie bereitgestellt wird (Git-Repo, Cloud-Ordner, ZIP), entscheidet die Lehrkraft.
4. Rückmeldung ans Framework: Neue Fehlertypen aus der Abnahme als Vorschlag für eine neue Prüfung oder einen Katalogeintrag in `STATUS.md` unter „Rückmeldung ans Framework“ notieren.

## Prüfskripte

Die Skripte liegen in `scripts/` dieses Skills und brauchen nur Python 3. Sie geben nur Fehler mit Fundstelle aus; keine Ausgabe heißt bestanden.

| Skript | Prüft | Wann |
|---|---|---|
| `pruefe_checkliste.py <datei> …` | Checklistenpunkte beginnen mit „Ich kann“ (auch als gemeinsame Kopfzeile), sind atomar | nach jedem Zyklus mit Checkliste |
| `pruefe_scorm.py <ordner-oder-zip>` | Manifest, Ressourcen, Navigation, Querverweise | Abnahme und Auslieferung |

Hinweise („HINWEIS“) sind Verdachtsfälle: Selbst beurteilen, nur echte Mängel beheben.
