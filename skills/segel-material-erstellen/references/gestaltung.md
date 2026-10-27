# Gestaltungsleitfaden

Überprüfbare Regeln für Seiten, Aufgaben, Rückmeldung und Simulationen. Sie setzen vor allem P2–P7, P9, P12 und G1–G6 um (`prinzipien.md`). Die PING-Vorlage (`vorlage/`) erfüllt viele davon schon; bei eigenen Lösungen gelten sie genauso.

Inhaltliche Grundlage: PING-Leitfaden Teil C3 (Bezug: PING v1.3) und die Bausteine aus Jürgens ITS11-Lernmodulen und dem Docker-Test (Rückmeldungen 2026-10).

## Seite und Darstellung

- Nur, was dem Lernziel dient: keine Deko-Bilder, keine Hintergrundmusik, keine „interessanten Nebenfakten“.
- Wichtiges hervorheben (Schlüsselbegriffe fett, Pfeil oder Rahmen genau auf die Stelle), Farben sparsam und im ganzen Material mit gleicher Bedeutung.
- Beschriftung direkt ans Bild statt Legende; Erklärung und Grafik gleichzeitig sichtbar. Bild vor dem zugehörigen Text.
- Alles, was eine Aufgabe braucht (Auftrag, Bild oder Konsole, Eingabe, benötigte Infos), ist gleichzeitig sichtbar, ohne Scrollen, Umschalten oder Pop-up; bei Platzmangel eine aufklappbare Seitenleiste.
- Inhalte in kleine Schritte teilen, die Lernende selbst weiterklicken; sichtbarer Text kurz (2–5 Sätze), Ausführliches aufklappbar.
- Fachbegriffe kurz einführen, bevor sie in einem komplexen Ablauf auftauchen.
- Für Einsteiger einfache Skizzen statt Fotos oder realistischer Animationen.
- Text nicht gleichzeitig vorlesen und anzeigen; Ton ist optional.
- Persönlich und direkt ansprechen („du“ bzw. „Sie“), nicht im Lehrbuchton; Ansprache durch eine Figur optisch vom Lernstoff abheben (z. B. Sprechblase).
- Den Praxisbezug ausdrücklich nennen; signalisieren, dass die Aufgabe Anstrengung verlangt, aber zu schaffen ist.
- Auf dem Zielgerät prüfen, besonders auf dem Tablet.

## Orientierung: Wo geht es weiter?

- Jede Seite hat genau einen hervorgehobenen nächsten Schritt, immer an derselben Stelle und im selben Aussehen.
- Die Akzentfarbe ist für Handlungsaufforderungen reserviert.
- Was zu tun ist, steht als kurzer Auftrag oben, nicht im Fließtext.
- Erledigtes wird sofort sichtbar bestätigt, mit Benennung des nächsten Schritts.
- Fortschrittsanzeige (Teil, Station 3 von 7, Erledigtes).
- Noch nicht verfügbare Schritte sichtbar, aber erkennbar ausgegraut, mit kurzem Grund.
- Anklickbares sieht anklickbar aus, Dekoratives nicht; kein wichtiger Knopf außerhalb des sichtbaren Bereichs.
- **Fünf-Sekunden-Test:** Jemand sieht eine Seite kurz an und sagt, was als Nächstes zu tun ist. Klappt das nicht, fehlt ein Signal.

## Aufgaben und Übungen

- Jede Aufgabe beginnt mit einem Auftrag aus der Handlungssituation („Mira bittet dich …“), nicht mit „Aufgabe 3“.
- Erst Lösungsbeispiel, dann ähnliche Aufgabe, dann veränderte Aufgabe; Situationen variieren (andere Kunden, Geräte, Daten).
- Geprüft wird das Ergebnis, nicht ein bestimmter Lösungsweg; alternative richtige Wege und alle richtigen Schreibweisen werden akzeptiert.
- Kurz-Checks und Übungen deutlich als „zählt nicht“ kennzeichnen.
- Im Entdecken und Üben nicht hart sperren, sondern den nächsten Schritt vorschlagen (Katalog A19). Lenken ist erlaubt, solange ein Ausweg immer sichtbar bleibt (siehe Baustein „Weiter nach Erledigung“).
- Hilfe anbieten, nicht aufzwingen: Vorwissens-Check mit Überspring-Empfehlung, freiwilliger Kurz-Check am Kapitelanfang zum Überspringen, Erklärungen und Beispiele aufklappbar, übersprungene Teile bleiben erreichbar; der Abschlusscheck ist für alle gleich.

## Tipps: immer drei Stufen

1. Denkanstoß: Worauf solltest du achten?
2. Teillösung oder Verweis auf die passende Stelle.
3. Vollständige Lösung mit kurzer Begründung.

Tipps werden aktiv angefordert, zählen im Üben nicht gegen die Lernenden und verdecken nicht, worauf sie sich beziehen. Im Abschlusscheck gibt es keine.

## Rückmeldung

- Zu jeder Antwort: richtig oder falsch, warum, und bei Fehlern, was als Nächstes hilft – direkt an der Antwort.
- Typische Fehlvorstellungen bekommen eigenes Feedback; bei Auswahlfragen: „warum falsch“, dann neu wählen lassen.
- Tippfehler von inhaltlich falschen Antworten unterscheiden (z. B. geringer Editierabstand → „Fast – Tippfehler?“).
- Kein Lob ohne Information, kein Punktestand als einziges Feedback.
- Im Abschlusscheck wirkt sich ein Fehler, wo möglich, realistisch aus; die Erklärung folgt in der Auswertung.

## Story und Spielelemente

- Rahmengeschichte mit wiederkehrenden Figuren ist erwünscht; Figuren und Welt wählt die Lehrkraft bzw. die Materialreihe.
- Punkte, Abzeichen, Zeitdruck nur mit Lernfunktion; keine Ranglisten – Fortschritt an Lernzielen oder an der eigenen früheren Leistung.

## Simulationen (Konsole, Web-Anwendung)

- **Referenz:** Alle Ausgaben, Hilfetexte und Fehlermeldungen aus einer echten Installation der Zielversion (G6), in der Spaltenbreite der simulierten Konsole.
- **Hilfe** des Werkzeugs (`--help`, `-h`) originalgetreu nachbilden.
- **Shell-Verkettung** (`&&`, `||`, `;`) nachbilden; nicht Nachgebildetes (Pipes, `$( )`) klar als solches melden.
- **Konfigurationsdateien:** Editor nachbilden (z. B. nano mit originalen Tastenkürzeln und Rückfragen) und die Datei wirklich parsen statt Zeichenketten zu vergleichen.
- **Zurücksetzen:** Knopf „Seite zurücksetzen“ überall, wo man sich festfahren kann (G5); Rückfragen gelten bis zur nächsten Aktion.
- **Befehlskasten** „Befehle dieser Seite“ an fester Stelle vor der ersten Aufgabe: Syntax mit Platzhaltern, kein fertiger Aufgabenbefehl (M11).
- **Konsole:** Zeilen umbrechen statt quer scrollen (`white-space: pre-wrap`), Autofokus auf Konsole bzw. Antwortfeld.
- **Rückmeldung am Zustand** (G4): Hinweise richten sich nach dem tatsächlichen Zustand der Simulation, typische Fehleingaben werden mit verständlichem Hinweis abgefangen.
- Simulationshinweis: Es ist erkennbar, dass nichts auf dem eigenen Rechner ausgeführt wird.

## Bewährte Bausteine aus den ITS11-Lernmodulen (Vorschlag, anpassbar)

- 💡 „Nice to know“: einmal einführen, dann dezent an der Fundstelle.
- Gestufter Hilfe-Knopf (entspricht den drei Tipp-Stufen).
- „Weiter“ wird aktiv, sobald die Aufgaben der Seite erledigt sind; „Schritt überspringen“ ist immer sichtbar. Lenkt, ohne zu sperren (Katalog A19).
- Client links, Server rechts, wenn zwei Systeme zusammenspielen.
- Konsole als root, wenn das Thema es nahelegt; sonst bewusst entscheiden.
