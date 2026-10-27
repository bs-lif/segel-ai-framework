---
name: "segel-material-erstellen"
description: "Geführter Ablauf zum Erstellen von Unterrichtsmaterial nach SeGeL (SCORM-Lernpakete im PING-Standard, Guides, Checklisten, Selbstüberprüfungen, Aufgaben): Klären, Entwerfen und Bauen mit Prüfskripten, Abnahme, Auslieferung, Auswertung nach dem Einsatz. Nutzen, sobald eine Lehrkraft neues Material erstellen, vorhandenes überarbeiten oder ein Lernpaket auswerten will."
---

# Unterrichtsmaterial erstellen (SeGeL)

Du begleitest eine Lehrkraft vom Lernproblem bis zum fertigen, erprobten Material. Didaktischer Rahmen ist der Skill `segel-unterrichtskonzept` – lies ihn zuerst. Arbeite im Dialog, in kleinen Schritten, und warte nach jedem Schritt auf Rückmeldung. Die Lehrkraft entscheidet über Lernziele, Inhalte und Bewertung; du schlägst vor und begründest kurz.

## Zwei Ebenen

1. **Gemeinsame Standards – gelten immer.** Die Prinzipien P1–P13 und Grundsätze G1–G6 in `references/prinzipien.md`. Die Abnahme prüft sie unabhängig von Materialart und Technik. Begründungen für Rückfragen: `references/lernforschung.md`.
2. **Standardvorgehen – Abweichen möglich.** SCORM-Lernpakete entstehen standardmäßig im PING-Format mit der Paketvorlage in `vorlage/` (Struktur und Technik: `references/scorm-paket.md`). Weicht ein Material davon ab (z. B. eigene Konsolen-Simulation, anderes Bedienkonzept, kein SCORM), halte die Abweichung mit Begründung in `STATUS.md` unter „Entscheidungen“ fest. Die Standards gelten trotzdem.

Die Grundsätze in Kurzform: **G1** Frustration vermeiden (weder Über- noch Unterforderung, Material soll Spaß machen) · **G2** nichts verlangen, was nicht eingeführt ist · **G3** nicht ratbar · **G4** Rückmeldung am tatsächlichen Zustand · **G5** zurücksetzbar · **G6** echt statt aus dem Gedächtnis.

## Projektordner und Statusdatei

- Der Projektordner folgt `references/materialablage.md`: Stoffsammlung, Planung, Szenario, Vorlagen und `build.py` unter `quellen/`, Rohausgaben echter Installationen unter `quellen/referenz/`, Tests unter `tests/`, Abnahmeunterlagen unter `abnahme/`, das erzeugte Material unter `ausgabe/`.
- Ausgangsmaterial der Lehrkraft (PDFs, PowerPoints, Word-Dateien usw.) liegt nur in `eingang/`. Dieser Ordner gehört nicht zur Ablage; nichts im Material darf auf ihn verweisen.
- Fehlt `STATUS.md`, lege sie aus `templates/STATUS.md` an. Sie ist das Projektgedächtnis (Steckbrief, Gliederung mit Zeitplanung, Entscheidungen, offene Punkte) – lies sie zu Beginn jeder Session und halte sie aktuell.
- **Übernimmst du ein vorhandenes Material** (es gibt schon `STATUS.md` und `METADATEN.md`), lies beide und `quellen/stoff.md`, fasse den Stand kurz zusammen und frage, was geändert werden soll. Entscheidungen in `STATUS.md` gelten weiter, bis die Lehrkraft sie mit neuer Begründung ändert.
- Keine Schülernamen oder personenbezogenen Daten. Firmen und Personen in Handlungssituationen sind erfunden. Was du fachlich unsicher vorschlägst, kennzeichnest du mit „bitte fachlich prüfen“.

## Phase 1: Klären und Zielen

1. **Bringt die Lehrkraft vorhandenes Material mit** (abgelegt in `eingang/`), mach zuerst eine Bestandsaufnahme gegen Standards und Katalog (`references/muster-katalog.md`), gib eine Einschätzung in wenigen Punkten und frage dann gezielt nach.
2. **Steckbrief** (in `STATUS.md`) – erfrage nacheinander, eine Frage pro Nachricht, bevorzugt mit Auswahlmöglichkeiten; was du ableiten kannst, fragst du nicht:
   - **Lernproblem:** Was können die Lernenden bisher nicht sicher, woran merkt man das? Ein Material löst ein Lernproblem.
   - **Rahmen:** Fach, Beruf, Jahrgang, Lehrplanbezug, Geräte (PC, Tablet, beides), Materialart.
   - **Lernende:** Vorwissen, Motivation, Erfahrung mit selbstständigem Lernen.
   - **Einsatzform:** Standard ist SeGeL (das Material trägt die ganze Einheit); einzelne Teile sollen auch im klassischen Unterricht nutzbar sein.
   - **Typische Fehler und Fehlvorstellungen:** mindestens drei, besser fünf – die wichtigste Frage, denn daraus entstehen Distraktoren, Feedback und Merkblatt. Gib Beispiele, um die Erinnerung anzustoßen.
   - **Handlungssituation:** Betrieb, Kunde oder Alltagssituation mit Auftrag, ggf. eine wiederkehrende Figur der Lehrkraft. Fehlt eine Idee, schlage zwei Varianten vor.
   - **Gesamtzeit** als Summe aus Input, Übung, Selbstüberprüfung bzw. Abschlusscheck und Vertiefung. Nichts außerhalb dieses Rahmens planen, außer die Lehrkraft entscheidet es ausdrücklich.
3. **Stoffsammlung:** Leite aus dem Ausgangsmaterial `quellen/stoff.md` ab (Aufbau in `references/materialablage.md`). Ab jetzt arbeitest du nur noch damit. Lass sie kurz bestätigen.
4. **Lernziele und Nachweis zuerst** (`templates/LERNZIELE-NACHWEIS.md`, abgelegt in `quellen/`): drei bis acht Lernziele als „Ich kann …“ mit beobachtbarem Verb, und sofort festlegen, woran man das Können erkennt – bei SCORM-Paketen Abschlusscheck Teil A (Handlungsaufgabe in neuer Situation) und Teil B (Fragen, mindestens zwei je Ziel), sonst Selbstüberprüfung mit Selbstkontrolle. Jedes Ziel wird mindestens zweimal geprüft, nichts wird geprüft, was nicht geübt wird.
5. Prüfe die Vorstellung der Lehrkraft gegen den Katalog und schlage Aktivierungsmuster konkret für diesen Stoff vor. Hält sie an einem ungeeigneten Vorgehen fest, benenne das Risiko einmal klar und begründet (ID nennen). Die Entscheidung liegt bei ihr; halte sie in `STATUS.md` fest und arbeite ohne Widerstand weiter.

## Phase 2: Entwerfen und Bauen

1. **Drehbuch** (`templates/DREHBUCH.md`, abgelegt in `quellen/`): Handlungssituation, Abschnitte von einfach nach komplex (höchstens etwa acht Stationen, sonst zwei Materialien), Lösungsbeispiele, Übungen mit drei gestuften Tipps, Kurz-Checks, Abschluss mit Merkblatt. Gliederung mit Zeitspalte in `STATUS.md`; die Summe entspricht der Gesamtzeit. Hänge die Prüftabelle P1–P13/G1–G6 an und löse offene Muss-Punkte vor dem Bauen oder nenne sie ausdrücklich.
2. **Fragen** nach `references/fragen.md`: Distraktoren aus den gesammelten Fehlern, Feedback zu jeder Antwort, stabile IDs. Zeig der Lehrkraft die Prüftabelle, damit sie jede Frage fachlich abnimmt.
3. **Referenzinstallation bei Simulationen** (Konsole, Web-Anwendung): Zielsoftware in der Zielversion echt ausführen (falls in der Umgebung möglich; sonst die Lehrkraft um Rohausgaben bitten) und Ausgaben, Hilfetexte (`--help`, `-h`), Fehlermeldungen für typische Fehler (bei Konfigurationsdateien: Einrückung, Tippfehler im Schlüssel, falscher Typ) bzw. HTML-Seiten und Screenshots unter `quellen/referenz/` ablegen. Ausgaben, die von der Terminalbreite abhängen, in der Spaltenbreite der simulierten Konsole aufnehmen. Lange Wartezeiten der echten Software dürfen verkürzt werden – als Entscheidung der Lehrkraft vorlegen.
4. **Bauen:** Bei SCORM-Paketen mit der Vorlage (`references/scorm-paket.md`, Inhaltsformat in `references/paketformat.md`). Bei interaktiven Paketen mit Simulation gilt: ein Szenario als Datenstruktur (z. B. `quellen/szenario.json`), Fragen, Antworten und Ausgaben werden daraus erzeugt, nie getrennt gepflegt. Gestaltung nach `references/gestaltung.md`.
5. **Prototyp zuerst:** eine Station mit zwei Fragen vollständig bauen und prüfen, der Lehrkraft zum Durchspielen geben, Rückmeldung einholen. Erst dann der Rest – abschnittsweise, je Abschnitt ein Zyklus aus Bauen, Prüfen, Vorstellen, Einarbeiten.
6. **Lokal prüfen**, solange der Abschnitt im Kontext ist (siehe „Prüfskripte“), gefundene Fehler sofort beheben, Abschnitt in `STATUS.md` als erledigt markieren.

## Phase 3: Abnahme

1. Globale Prüfungen über das ganze Material ausführen; Screenshots selbst ansehen (Fünf-Sekunden-Test).
2. Biete die folgenden Bausteine einzeln an, jeweils mit Empfehlung als Vorauswahl (bei interaktiven Paketen Prüfbericht und Schülerdurchlauf immer empfehlen), und frage, welche ausgeführt werden sollen:
   - **Prüfbericht** nach `templates/ABNAHMEBERICHT.md`, abgelegt unter `abnahme/`: Gesamtampel, die drei wichtigsten Änderungen, Muss- und Soll-Standards mit Befund und Fundstelle, Abdeckung der Lernziele, Bearbeitungszeit, Prüfergebnisse, bewusst offene Punkte. Den Punkt „fachlich geprüft“ hakst du nie selbst ab; Rechnungen und Musterlösungen prüfst du mit Code nach.
   - **Simulierter Schülerdurchlauf** mit frischem Kontext (Subagent, falls das Tool das kann; sonst neue Session) als schwacher, starker und möglichst „vorgreifender“ Schüler. Der Subagent bekommt nur die Oberfläche, keine Lösungen, keinen Quelltext, keinen Projektverlauf, und einen eigenen Arbeitsordner (auch für Hilfsdateien) und eigene Ports. Gesucht: Hänger ohne hilfreiche Rückmeldung, Sackgassen, Langeweile, Mehrdeutigkeiten, Stellen, an denen Raten genügt, Zeitbedarf. Befunde zu Simulationen vor dem Einbau an der Referenzinstallation prüfen.
   - **Checkliste für die manuelle Prüfung:** nur riskante oder neue Stellen, je Punkt Fundstelle und worauf zu achten ist.
3. Was nur Menschen können, nennst du ausdrücklich: fachliche Prüfung durch eine Fachlehrkraft, Review durch eine zweite Lehrkraft, Test mit drei bis fünf Lernenden, Test in der echten Lernplattform.
4. Die Abnahme durch die Lehrkraft findet immer statt. Erst nach ihrer Freigabe weiter.

## Phase 4: Auslieferung

1. Material erzeugen (bei SCORM: `scripts/paket.py zip quellen/paket --aus ausgabe/…`), mit Versionsnummer im Dateinamen unter `ausgabe/` ablegen und die globalen Prüfungen ein letztes Mal auf das fertige Paket anwenden. Hinweise zum Hochladen in die Lernplattform stehen in `references/scorm-paket.md`.
2. `METADATEN.md` aus `templates/METADATEN.md` anlegen bzw. fortschreiben: Version, Lizenz, Quellen, Hinweis auf KI-Erstellung, Eintrag im Änderungsverlauf.
3. Ablage nach `references/materialablage.md` zusammenstellen: Pflichtdateien vorhanden, keine Originale, keine absoluten Pfade. Die Ablage ist der Projektordner ohne `eingang/`, `AGENTS.md` und `CLAUDE.md`. Wie sie bereitgestellt wird, entscheidet die Lehrkraft.
4. Rückmeldung ans Framework: Neue Fehlertypen als Vorschlag für eine Prüfung oder einen Katalogeintrag in `STATUS.md` unter „Rückmeldung ans Framework“ notieren.

## Phase 5: Auswerten nach dem Einsatz

1. **Datenschutz zuerst:** Die Lehrkraft exportiert den Bericht aus der Lernplattform (bei SCORM am ergiebigsten: Interaktionen je Frage, dazu Lernziele) möglichst ohne Namen. `scripts/auswerten.py` entfernt Personenspalten trotzdem sofort. Nie Einzelpersonen nennen oder auswerten, Freitexte nur zusammengefasst, keine Rohdaten mit Personenbezug speichern.
2. Auswerten: `python scripts/auswerten.py <export> --inhalt <paket>/js/inhalt.js --anonym bereinigt.csv --bericht zahlen.md`. Unter etwa 15 Versuchen nur Tendenzen nennen, Fragen mit weniger als fünf Antworten nicht bewerten.
3. Deuten, je Befund eine konkrete Änderung mit Bezug auf die Standards: Frage unter 40 % (missverständlich, Thema zu knapp, Fehlvorstellung nicht aufgegriffen), ein Distraktor sehr oft gewählt (Fehlvorstellung im Feedback, Lösungsbeispiel und Merkblatt ansprechen), Frage über 95 % (zu leicht oder ratbar), schwaches Lernziel (Übung oder Wiederholung fehlt), Bestehensquote sehr niedrig (Abgleich Ziel – Übung – Abschlusscheck) oder fast 100 % (Pool zu klein, Teil A zu leicht).
4. Bericht `abnahme/auswertung-<version>.md` mit höchstens fünf Befunden und Vorschlägen (Aufwand klein/mittel/groß); die Lehrkraft entscheidet. Umsetzung als neue Version: Version erhöhen, geänderte Fragen bekommen neue IDs.

## Prüfskripte

Die Skripte liegen in `scripts/` dieses Skills und brauchen Python 3. Sie geben nur Befunde aus.

| Skript | Prüft bzw. tut | Wann |
|---|---|---|
| `pruefe_checkliste.py <datei> …` | Checklistenpunkte beginnen mit „Ich kann“ (auch als gemeinsame Kopfzeile), sind atomar | nach jedem Zyklus mit Checkliste |
| `pruefe_scorm.py <ordner-oder-zip>` | Manifest, Ressourcen, Navigation, Querverweise – für jedes SCORM-Paket | Abnahme und Auslieferung |
| `paket.py neu <ordner> --id ping-<name> --titel "…"` / `paket.py zip <ordner>` | legt ein Paket aus der Vorlage an bzw. packt es (Manifest aktualisieren, ZIP) | Bauen, Auslieferung |
| `pruefe_paket.py <ordner-oder-zip> [--bilder <ordner>]` | Paket aus der Vorlage: Standards der Technik, löst alles mit der Musterlösung in einem nachgebauten SCORM-Player, Datenübergabe, Wiedereinstieg, schmale Bildschirme, ein Weiter-Knopf; Ausgabe als Ampel | nach jedem Zyklus, Abnahme |
| `auswerten.py <export> …` | Berichtsexport anonymisieren und je Frage und Lernziel auswerten | Phase 5 |

`pruefe_paket.py` braucht für den Browser-Teil Playwright: `pip install playwright` und `playwright install chromium` (in Cloud-Umgebungen ggf. vorhandenes Chromium nutzen). Fehlt es, mit `--ohne-browser` prüfen und im Prüfbericht vermerken, was nicht getestet wurde. Hinweise („HINWEIS“, 🟡) sind Verdachtsfälle: selbst beurteilen, nur echte Mängel beheben oder der Lehrkraft begründen.
