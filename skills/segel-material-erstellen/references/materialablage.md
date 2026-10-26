# Materialablage

Was von einem fertigen Material aufbewahrt und bereitgestellt wird, damit andere Lehrkräfte es mit dem Framework weiterentwickeln können. Die Ablage ist ein einfacher Ordner und funktioniert unabhängig von der Bereitstellungsform (Git-Repo, Cloud-Ordner, Netzlaufwerk, ZIP).

## Grundsätze

- **Nur Abgeleitetes, keine Originale.** Ausgangsmaterial (PDFs, PowerPoints, Word-Dateien, Scans, fremde Videos) wird nicht abgelegt. Sein Inhalt geht in eine selbst verfasste Stoffsammlung ein; das Original wird nur als Quellenangabe genannt. Das vermeidet Urheberrechtsfragen, hält die Ablage klein und macht sie unabhängig davon, ob das Original später noch verfügbar ist.
- **Alles, was zum Weiterentwickeln nötig ist – nicht mehr.** Wer die Ablage bekommt, kann das Material ohne Rückfrage beim Ersteller ändern und neu erzeugen.
- **Einfache Dateien.** Text in UTF-8 (Markdown, JSON, YAML), relative Pfade, keine absoluten Pfade oder Benutzernamen, keine werkzeugspezifischen Dateien.
- **Selbsterklärend ohne Versionsverwaltung.** Version und Änderungsverlauf stehen in den Dateien selbst, weil nicht jede Bereitstellungsform eine Historie hat.

## Aufbau

```
<material>/
├── METADATEN.md          Pflicht: Version, Lizenz, Quellen, KI-Hinweis, Änderungsverlauf
├── STATUS.md             Pflicht: Lernziele, Gliederung, Entscheidungen, offene Punkte
├── quellen/
│   ├── stoff.md          Pflicht: abgeleitete Stoffsammlung (ersetzt das Ausgangsmaterial)
│   ├── szenario*.json    bei Simulationen: einzige Quelle für Fragen, Antworten, Ausgaben
│   ├── referenz/         bei Simulationen: selbst erzeugte Rohausgaben der Zielsoftware
│   ├── vorlagen/         Vorlagen, aus denen das Material erzeugt wird (HTML, CSS, Bilder)
│   └── build.py          erzeugt das Material aus Szenario und Vorlagen
├── tests/                Durchlauftests (falls vorhanden)
├── abnahme/              Abnahmebericht, Befunde aus Schülerdurchläufen (falls erstellt)
└── ausgabe/              zuletzt freigegebene Fassung, z. B. <thema>_v1.2.zip
```

Für ein reines Text-Material (Guide, Checkliste) genügen `METADATEN.md`, `STATUS.md`, `quellen/stoff.md` und das Material selbst unter `ausgabe/`.

## Die Stoffsammlung `quellen/stoff.md`

Entsteht in Phase 1 aus dem Ausgangsmaterial und ersetzt es dauerhaft:

- Fachliche Kernaussagen je Thema, in eigenen Worten
- Fachbegriffe mit kurzer Erklärung
- Beispiele, Zahlen und Fakten, auf die sich das Material stützt
- Je Abschnitt die Quellenangabe (Titel, Urheber, Fundort, Datum), keine Kopien längerer Passagen
- Was bewusst nicht aufgenommen wurde und warum

## Nicht in die Ablage

- Originale des Ausgangsmaterials (PDF, PPTX, DOCX, Scans, Videos) – während der Arbeit liegen sie in `eingang/`, der Ordner bleibt draußen
- Gesprächsverläufe mit dem Agenten
- Temporäre Dateien, Hilfsskripte aus Schülerdurchläufen, Zwischenstände
- `AGENTS.md` und `CLAUDE.md` (erzeugt `setup.py projekt` bei Bedarf neu)
- Personenbezogene Daten von Lernenden

## Weiterentwickeln durch andere

1. Ablage in einen eigenen Ordner kopieren bzw. klonen, `python setup.py projekt <ordner>` ausführen.
2. Agenten-Tool im Ordner starten. Der Agent liest `STATUS.md` und `METADATEN.md` und fragt, was geändert werden soll.
3. Entscheidungen in `STATUS.md` respektieren oder bewusst mit neuer Begründung ändern.
4. Nach der Abnahme: Version in `METADATEN.md` erhöhen, Änderung im Änderungsverlauf eintragen, `ausgabe/` ersetzen, Ablage zurückgeben.
