# segel-ai-framework

Das segel-ai-framework ist ein Agent-Skills-Framework, mit dem Lehrkräfte an Berufsschulen Unterrichtsmaterial nach dem SeGeL-Konzept (selbstgesteuertes Lernen) KI-gestützt erstellen. Dazu gehören SCORM-Pakete ebenso wie andere Materialarten. Bewährte Abläufe und automatische Qualitätsprüfungen sind fest eingebaut.

## Einbinden in die eigene KI-Arbeitsumgebung

Das Framework läuft in clientbasierten Agenten-Tools: Claude Code, OpenAI Codex und GitHub Copilot (VS Code). Die Skills liegen im offenen Agent-Skills-Format vor (`skills/<name>/SKILL.md`). Die Prüfskripte brauchen Python.

1. Repo klonen:

   ```bash
   git clone https://github.com/funkpunkt/segel-ai-framework.git
   ```

2. Jeden Ordner unter `skills/` in den persönlichen Skills-Ordner des Tools verlinken:

   | Tool           | Persönlicher Skills-Ordner |
   |----------------|----------------------------|
   | Claude Code    | `~/.claude/skills/`        |
   | OpenAI Codex   | `~/.agents/skills/`        |
   | GitHub Copilot | `~/.copilot/skills/` oder `~/.agents/skills/` |

   Beispiel unter Windows (PowerShell, ohne Adminrechte über eine Verzeichnisverknüpfung):

   ```powershell
   New-Item -ItemType Junction -Path "$HOME\.claude\skills\segel-unterrichtskonzept" -Target "C:\Pfad\zu\segel-ai-framework\skills\segel-unterrichtskonzept"
   ```

   Durch die Verlinkung kommen Updates mit `git pull` automatisch an.

Ein Setup-Skript, das diese Verlinkung und die Dateien `CLAUDE.md` bzw. `AGENTS.md` automatisch erzeugt, ist in Arbeit.
