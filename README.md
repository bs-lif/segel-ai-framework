# segel-ai-framework

Das segel-ai-framework ist ein Agent-Skills-Framework, mit dem Lehrkräfte an Berufsschulen Unterrichtsmaterial nach dem SeGeL-Konzept (selbstgesteuertes Lernen) KI-gestützt erstellen. Dazu gehören SCORM-Pakete ebenso wie andere Materialarten. Bewährte Abläufe, wissenschaftlich begründete Gestaltungsprinzipien und automatische Qualitätsprüfungen sind fest eingebaut.

## Zwei Ebenen

1. **Gemeinsame Standards** gelten für jedes Material: 13 Prinzipien aus der Lernforschung und 6 Grundsätze aus der Praxis ([prinzipien.md](skills/segel-material-erstellen/references/prinzipien.md), Begründungen in [lernforschung.md](skills/segel-material-erstellen/references/lernforschung.md)).
2. **Standardvorgehen** für SCORM-Lernpakete ist das PING-Format mit einheitlicher Paketvorlage, automatischem Durchlauftest und Auswertung nach dem Einsatz ([scorm-paket.md](skills/segel-material-erstellen/references/scorm-paket.md)). Abweichungen sind möglich und werden im Projekt begründet.

Prinzipien, Paketvorlage und Werkzeuge stammen inhaltlich bzw. als feste Kopie aus [PING](https://github.com/dennismarcbusch/PING) von Dennis Busch (Stand v1.3).

Der automatische Durchlauftest (`pruefe_paket.py`) braucht für den Browser-Teil Playwright: `pip install playwright` und `playwright install chromium`.

## Einbinden in die eigene KI-Arbeitsumgebung

Das Framework läuft in clientbasierten Agenten-Tools: Claude Code, OpenAI Codex und GitHub Copilot (VS Code). Die Skills liegen im offenen Agent-Skills-Format vor (`skills/<name>/SKILL.md`). Die Prüfskripte brauchen Python.

1. Repo klonen:

   ```bash
   git clone https://github.com/bs-lif/segel-ai-framework.git
   ```

2. Skills verlinken:

   ```bash
   python setup.py install
   ```

   Das Skript verlinkt jeden Ordner unter `skills/` nach `~/.claude/skills/` (Claude Code) und `~/.agents/skills/` (OpenAI Codex, GitHub Copilot). Unter Windows nutzt es Verzeichnisverknüpfungen, die keine Adminrechte brauchen. Updates kommen mit `git pull` automatisch an.

3. Für jedes neue Material einen Projektordner anlegen:

   ```bash
   python setup.py projekt <ordner>
   ```

   Das legt `AGENTS.md`, `CLAUDE.md` und die Ordnerstruktur an. Vorhandenes Ausgangsmaterial (PDFs, Präsentationen usw.) kommt nach `eingang/`. Danach das Agenten-Tool in diesem Ordner starten und das gewünschte Material beschreiben. Zum Weiterentwickeln eines vorhandenen Materials denselben Befehl auf dessen Ordner anwenden.

## Materialablage

Fertiges Material wird so abgelegt, dass andere Lehrkräfte es weiterentwickeln können: nur selbst erstellte, abgeleitete Dateien, keine Originale des Ausgangsmaterials, unabhängig von der Bereitstellungsform. Einzelheiten: [skills/segel-material-erstellen/references/materialablage.md](skills/segel-material-erstellen/references/materialablage.md).

## Nutzung ohne Installation (Cloud-Umgebungen)

In Cloud-Umgebungen mit geklontem Repo (z. B. claude.ai-Projekte mit Code-Ausführung) entfällt die Installation. Dem Agenten zu Beginn sagen:

> Arbeite nach `segel-ai-framework/skills/segel-material-erstellen/SKILL.md`. Die Prüfskripte liegen im Unterordner `scripts/` dieses Skills.

Genutzt wird dabei der Stand, der auf GitHub liegt.
