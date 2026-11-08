# SCORM-Lernpaket im Kompass-Standard

Standardvorgehen für SCORM-Material (Ebene 2, siehe SKILL.md). Grundlage ist die Paketvorlage in `vorlage/`, eine feste Kopie der Vorlage des Lernpaket-Kompass (Bezug: Lernpaket-Kompass v1.2; früher Teil von PING, mit dem die PING-Pakete gebaut werden). Inhaltliche Grundlage dieses Textes: Kompass-Leitfaden Teil C2, C4, C5.

## Paketstruktur

Jedes Paket folgt demselben Grundmuster. Einheitlichkeit hat eigenen Nutzen: Lernende lernen die Bedienung einmal und konzentrieren sich dann auf den Inhalt.

| Teil | Zweck | Mindeststandard |
|---|---|---|
| 0 Einstieg | Orientierung, Motivation | Handlungssituation in wenigen Sätzen; Lernziele in Schülersprache mit Selbsteinschätzung je Ziel; „Wichtige Begriffe vorab“ (Glossar); unbewerteter Vorwissens-Check mit Überspring-Empfehlung; Dauer und Ablauf; optional Hinweis auf das Tafelbild |
| ① Entdecken | Neues verstehen | Stationen mit je einem Auftrag und Leitfrage; Lösungsbeispiel mit Frage zum Selbsterklären vor eigener Aufgabe; Glossar aufklappbar; Kurz-Check (3–5 Fragen) am Ende; Praxisbezug |
| ② Üben | Können aufbauen | Eine Übung je Lernziel oder Kapitel in wechselnden Situationen; drei gestufte Tipps; Feedback mit Begründung; Reflexionsfrage mit Musterantwort |
| ③ Abschlusscheck | Können zeigen | Teil A: Handlungsaufgabe in neuer Situation, ohne Tipps; Teil B: Fragen aus einem Pool, zwei je Lernziel pro Versuch, gemischt; bestanden ab 80 %; beliebig oft wiederholbar, bestes Ergebnis zählt; keine Prüfung im rechtlichen Sinn |
| 4 Abschluss | Sichern, Transfer | Auswertung je Lernziel mit Empfehlung; Selbsteinschätzung nachher; Merkblatt zum Ergänzen mit PDF und Selbsttest; Ergebnis als PDF |

**Zum Begriff:** Der Kompass nennt Teil ③ „Kompetenznachweis“. Bei SeGeL bedeutet „Kompetenznachweis“ etwas anderes. Im Framework heißt Teil ③ deshalb **Abschlusscheck**; die Anzeige in `vorlage/js/engine.js` ist entsprechend angepasst (einzige Änderung an der Engine). Der Feldname in `inhalt.js` bleibt `nachweis`.

**Größe:** Ein Paket deckt ein Thema ab, das sich in einem Satz benennen lässt; mehr als etwa acht Stationen → zwei Pakete. Lerneinheiten von 30–45 Minuten, jede mit Orientierung am Anfang und Abschluss (Kurz-Check oder Zusammenfassung) am Ende.

**Input mit Tafelbild (optional):** Ein freiwilliger Lehrer-Input von etwa 20 Minuten mit den Bildern des Pakets, Regeln in `gestaltung.md`. Das Tafelbild steckt im Paket (Knopf in der Kopfzeile, Aufruf als Präsentation über `index.html#tafel`), der Ablaufplan für die Lehrkraft liegt daneben, nicht im ZIP.

**Merkblatt:** Öffnet sich erst nach dem Abschlusscheck, gegliedert nach Lernzielen: Kernaussagen aus dem Gedächtnis ergänzen, mit Muster vergleichen; als PDF mit eigenen Einträgen, typischem Fehler mit Korrektur, kurzem Beispiel, ggf. Schritt-Schema und fünf Selbsttest-Fragen („in 1–2 Wochen nochmal beantworten“). Im SeGeL-Unterricht gehört es ins Lernportfolio.

## SeGeL und klassischer Unterricht

Pakete grundsätzlich für SeGeL bauen und so gliedern, dass einzelne Stationen auch im klassischen Unterricht nutzbar sind (umgekehrt ist es viel aufwendiger).

| Merkmal | SeGeL | Klassisch |
|---|---|---|
| Rolle des Pakets | trägt die ganze Einheit vom Einstieg bis zum Abschlusscheck | Baustein für eine Phase |
| Zeit | kein Stundenraster, Fortschritt gespeichert | Abschnitte von 20–30 Minuten |
| Steuerung | empfohlener Weg, freies Tempo, Springen mit Hinweis auf Voraussetzungen | Lehrkraft gibt vor |
| Hilfe | Tipps, Lösungsbeispiele, Hintergrund immer erreichbar; Hinweis, wann man den Lerncoach fragen sollte | Tipps im Paket, Vertiefung durch Lehrkraft |
| Selbststeuerung | verbindlich: Selbsteinschätzung vorher/nachher, Fortschritt, Reflexion, Empfehlung | optional |
| Lehrkraft | Lerncoach: wertet Daten aus, spricht gezielt mit Lernenden, die hängen | leitet den Unterricht |

**Wie offen darf ein Paket sein?** Eher fester Weg, wenn der Stoff aufeinander aufbaut, das Vorwissen gering oder ähnlich ist, selbstständiges Lernen wenig geübt ist und die Motivation von außen kommt. Eher freies Erkunden, wenn Themen nebeneinanderstehen, die Lernenden sehr unterschiedlich und geübt sind und Interesse trägt. Für die meisten Berufsschulklassen: empfohlener Weg mit freiem Tempo.

## Technische Standards

| Bereich | Standard |
|---|---|
| Format | SCORM 1.2, eine ZIP mit `imsmanifest.xml` und `index.html` im Wurzelverzeichnis; alles im Paket, keine externen Server; Manifest-Identifier `<präfix>-<name>` (Präfix für Projekt oder Fach, z. B. `ping-` für die IT-Pakete; alle Pakete eines Projekts nutzen dasselbe) |
| Datenübergabe | `cmi.core.score.raw` = bestes Ergebnis (0–100), `lesson_status` passed/failed, `masteryscore` 80; Fortschritt in `suspend_data` (höchstens 4096 Zeichen); Name aus `cmi.core.student_name`; `cmi.objectives` je Lernziel, `cmi.interactions` je Frage |
| Versionsnummer | Pflicht: `version` in `inhalt.js`, klein in der Kopfzeile („v1.2“), in der Fußzeile und auf Ergebnis-PDF und Merkblatt, dieselbe im Manifest; Prototyp 0.x, erste Fassung im Unterricht 1.0; bei jeder Änderung erhöhen (Korrektur 1.0 → 1.1, neue Inhalte 2.0) und in `METADATEN.md` eintragen |
| Ohne Lernplattform | läuft lokal (`index.html` öffnen), Fortschritt dann im Browser |
| Geräte | Zielgerät im Steckbrief; auf Tablets Antippen statt nur Ziehen, Ziele mindestens 40 px |
| Barrierefreiheit | Tastaturbedienung, Kontrast, Alternativtexte, skalierbare Schrift, Information nie nur über Farbe oder nur über Ton; Gesprochenes immer auch als Text; Glossar |
| Tafelbild (optional) | `js/tafel.js`, Daten in `PAKET.tafel`; Pfeiltasten und Presenter, Schaltflächen mindestens 48 px, lesbar am Beamer; schreibt keine SCORM-Werte, kein `suspend_data`, kein `localStorage` |
| Datenschutz | keine Daten an Dritte, kein Tracking, keine Konten außerhalb der Lernplattform; Merkblatt-Einträge nicht dauerhaft speichern |
| Qualität | `pruefe_paket.py` (alle Aufgaben mit Musterlösung lösbar, Datenübergabe, Wiedereinstieg); Test in der echten Lernplattform vor dem ersten Einsatz |

## Mit der Vorlage bauen

- `python scripts/paket.py neu quellen/paket --id <präfix>-<name> --titel "Titel"` legt die Paketquelle aus `vorlage/` im Projektordner an. Das Präfix kommt aus dem Steckbrief; ist keins festgelegt, frag die Lehrkraft.
- `version` in `js/inhalt.js`: `'0.1'` für den Prototyp, `'1.0'` für die erste Fassung im Unterricht.
- Inhalt nur in `js/inhalt.js` (Format: `paketformat.md`; das Beispiel „Bits & Bytes“ in `vorlage/js/inhalt.js` zeigt jedes Feld). **`js/engine.js`, `js/tafel.js`, `css/stil.css` und `css/tafel.css` nicht verändern** – fehlt etwas, als Interaktion in `inhalt.js` lösen und den Wunsch unter „Rückmeldung ans Framework“ notieren.
- Interaktionen: `function (box, api) { …; return { loesen, auswerten } }`; `loesen()` ist Pflicht (setzt die Musterlösung für den automatischen Test), `auswerten()` nur im Abschlusscheck Teil A. Bedienung mit `<button>`, Grafiken als Inline-SVG, keine `alert/confirm/prompt`, keine externen Dateien.
- Je Station: Lösungsbeispiel mit `selbsterklaerung`, in einigen Stationen oder Übungen `mitdenken` mit Muster; `glossar` mit allen Fachbegriffen, die wichtigsten mit `vorab: true`. Ton oder Video nur mit Untertiteln (`<track>`) oder Transkript.
- **Tafelbild** (nur wenn im Drehbuch ein Input geplant ist), erst wenn die Stationen stehen: Szenen als `tafel.szenen` mit denselben Bausteinen wie in der Station, größer und ohne erklärenden Text; je Szene `station` und `erklaerung`. Ablaufplan aus `templates/INPUT-ABLAUF.md` nach `quellen/INPUT-ABLAUF.md`. `pruefe_paket.py` prüft das Tafelbild mit; die Screenshots `tafel-<n>.png` ansehen: aus der letzten Reihe lesbar, nirgends ein erklärender Satz?
- Im Prototyp zeigt eine rote Box „Hinweis für Autor:innen“, was noch fehlt – das ist normal; im fertigen Paket darf sie nicht mehr erscheinen.
- Abweichende Interaktionen (z. B. eigene Konsolen-Simulation) gehören als Interaktion in `inhalt.js`, Szenario-Daten nach `quellen/` und werden per `build.py` eingesetzt.
- Packen: `python scripts/paket.py zip quellen/paket --aus ausgabe/<name>_v<version>_scorm12.zip` aktualisiert Manifest und Dateiliste und erzeugt das ZIP.

## In die Lernplattform (ByCS) hochladen

1. Im Kurs eine Aktivität „Lernpaket“ (SCORM) anlegen, ZIP unverändert hochladen.
2. Bewertungsmethode „Höchste Bewertung“, Versuche unbegrenzt, Anzeige in neuem Fenster oder mindestens 1000 px breit.
3. Vor dem ersten Einsatz mit einem Schülertestkonto durchspielen: Kommt die Punktzahl an?
4. Bei Paketen mit Tafelbild: für den Input den entpackten Ordner öffnen, `index.html#tafel` aufrufen (F = Vollbild), einmal am echten Board ausprobieren.
