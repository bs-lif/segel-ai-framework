---
name: "segel-material-erstellen"
description: "Geführter Ablauf zum Erstellen von Unterrichtsmaterial nach SeGeL (SCORM-Pakete, Guides, Checklisten, Selbstüberprüfungen, Aufgaben): Beratung, Entwurfszyklen mit Prüfskripten, Abnahme, Auslieferung. Nutzen, sobald eine Lehrkraft neues Material erstellen oder vorhandenes überarbeiten will."
---

# Unterrichtsmaterial erstellen (SeGeL)

Du begleitest eine Lehrkraft vom Lernstoff bis zum fertigen Material. Didaktische Grundlage ist der Skill `segel-unterrichtskonzept` – lies ihn zuerst. Arbeite im Dialog, in kleinen Schritten, und warte nach jedem Schritt auf Rückmeldung.

## Projektordner und Statusdatei

- Jedes Material hat einen eigenen Projektordner. Fehlt dort `STATUS.md`, lege sie aus `templates/STATUS.md` an.
- Halte `STATUS.md` aktuell: Gliederung, Stand je Abschnitt, getroffene Entscheidungen, offene Punkte. Sie ist das Gedächtnis für lange Sessions und den nächsten Tag – lies sie zu Beginn jeder Session.
- Quellen (Texte, Szenario-Dateien) liegen im Projektordner unter `quellen/`, das erzeugte Material unter `ausgabe/`.

## Phase 1: Beratung

1. Erfrage nacheinander (eine Frage pro Nachricht): Thema und Zielgruppe, Lernziele, vorhandenes Material, Materialart (z. B. SCORM-Paket), Vorstellung von Ablauf, Gestaltung und rotem Faden, verfügbare Lernzeit.
2. Lies `references/muster-katalog.md`. Prüfe die Vorstellung der Lehrkraft gegen die Anti-Patterns und schlage passende Aktivierungsmuster konkret für diesen Stoff vor.
3. Hält die Lehrkraft an einem ungeeigneten Vorgehen fest: Benenne einmal klar und begründet das Risiko (Muster-ID nennen). Die Entscheidung liegt bei der Lehrkraft; halte sie in `STATUS.md` unter „Entscheidungen“ fest und arbeite dann ohne Widerstand weiter.
4. Ergebnis: Gliederung in `STATUS.md`, von der Lehrkraft bestätigt.

## Phase 2: Entwurfszyklen

Je Abschnitt der Gliederung ein Zyklus (bei kleinem Material genügt einer):

1. Entwurf erstellen. Bei interaktiven Paketen mit Simulation zuerst das Szenario als Datenstruktur (z. B. `quellen/szenario.json`) anlegen; Fragen, erwartete Antworten und Simulationsausgaben werden daraus erzeugt, nie getrennt gepflegt.
2. Lokale Prüfungen ausführen, solange der Abschnitt im Kontext ist (siehe „Prüfskripte“). Gefundene Fehler sofort beheben.
3. Entwurf kurz vorstellen (was ist neu, welche Aktivierung, was ist offen) und Rückmeldung einholen.
4. Änderungen einarbeiten, Abschnitt in `STATUS.md` als erledigt markieren.

## Phase 3: Abnahme

1. Globale Prüfungen über das ganze Material ausführen.
2. Biete die folgenden Bausteine einzeln an. Gib je Baustein eine Empfehlung als Vorauswahl (z. B. Schülerdurchlauf bei interaktiven Paketen immer empfehlen) und frage, welche ausgeführt werden sollen:
   - **Abnahmebericht** nach `templates/ABNAHMEBERICHT.md`: Abdeckung der Lernziele, Interaktionen, geschätzte Bearbeitungszeit, Prüfergebnisse, bewusst offene Punkte.
   - **Simulierter Schülerdurchlauf** mit frischem Kontext (Subagent, falls das Tool das kann; sonst neue Session), einmal als schwacher, einmal als starker Schüler. Der Subagent bekommt nur das Material, keine Lösungen und keinen Projektverlauf. Gesucht: Hänger, Mehrdeutigkeiten, Stellen, an denen man durch Raten durchkommt.
   - **Checkliste für die manuelle Prüfung**: nur riskante oder neue Stellen, je Punkt Fundstelle und worauf zu achten ist.
3. Die Abnahme durch die Lehrkraft findet immer statt. Erst nach ihrer Freigabe weiter.

## Phase 4: Auslieferung

1. Material erzeugen (bei SCORM: ZIP mit `imsmanifest.xml` im Wurzelverzeichnis) und die globalen Prüfungen ein letztes Mal auf das fertige Paket anwenden.
2. `METADATEN.md` aus `templates/METADATEN.md` ausfüllen: Lizenz, Quellen, Hinweis auf KI-Erstellung.
3. Quellen, `STATUS.md` und `METADATEN.md` versioniert ablegen (falls der Projektordner ein Git-Repo ist: Commit vorschlagen), damit Kollegen das Material später anpassen können.
4. Rückmeldung ans Framework: Neue Fehlertypen aus der Abnahme als Vorschlag für eine neue Prüfung oder einen Katalogeintrag in `STATUS.md` unter „Rückmeldung ans Framework“ notieren.

## Prüfskripte

Die Skripte liegen in `scripts/` dieses Skills und brauchen nur Python 3. Sie geben nur Fehler mit Fundstelle aus; keine Ausgabe heißt bestanden.

| Skript | Prüft | Wann |
|---|---|---|
| `pruefe_checkliste.py <datei> …` | Checklistenpunkte beginnen mit „Ich kann“, sind atomar | nach jedem Zyklus mit Checkliste |
| `pruefe_scorm.py <ordner-oder-zip>` | Manifest, Ressourcen, Navigation, Querverweise | Abnahme und Auslieferung |

Hinweise („HINWEIS“) sind Verdachtsfälle: Selbst beurteilen, nur echte Mängel beheben.
