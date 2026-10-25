"""Bindet das segel-ai-framework in die eigene KI-Arbeitsumgebung ein.

Aufruf:
  python setup.py install            Skills verlinken (Claude Code, Codex, Copilot)
  python setup.py projekt <ordner>   Projektordner für ein neues Material anlegen
"""
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
SKILLS = REPO / "skills"
# ~/.agents/skills lesen Codex und Copilot, ~/.claude/skills liest Claude Code.
ZIELE = [Path.home() / ".claude" / "skills", Path.home() / ".agents" / "skills"]

AGENTS_MD = """# Materialprojekt (segel-ai-framework)

Dieser Ordner enthält ein Unterrichtsmaterial in Arbeit.

- Arbeite mit dem Skill `segel-material-erstellen`; didaktische Grundlage ist `segel-unterrichtskonzept`.
- Lies zu Beginn jeder Session `STATUS.md`, falls vorhanden.
- Antworte auf Deutsch, kurz und in kleinen Schritten.
"""


def verlinke(quelle, link):
    if link.exists() or link.is_symlink():
        if link.resolve() == quelle.resolve():
            return f"vorhanden: {link}"
        return f"ÜBERSPRUNGEN (anderer Inhalt vorhanden, bitte prüfen): {link}"
    link.parent.mkdir(parents=True, exist_ok=True)
    if os.name == "nt":
        # Verzeichnisverknüpfung (Junction) braucht unter Windows keine Adminrechte.
        subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(quelle)],
                       check=True, stdout=subprocess.DEVNULL)
    else:
        link.symlink_to(quelle, target_is_directory=True)
    return f"verlinkt: {link}"


def install():
    for ziel in ZIELE:
        for skill in sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").exists()):
            print(verlinke(skill, ziel / skill.name))


def projekt(ordner):
    ordner = Path(ordner)
    for unter in ("quellen", "ausgabe"):
        (ordner / unter).mkdir(parents=True, exist_ok=True)
    for name, inhalt in (("AGENTS.md", AGENTS_MD), ("CLAUDE.md", "@AGENTS.md\n")):
        datei = ordner / name
        if datei.exists():
            print(f"vorhanden, nicht überschrieben: {datei}")
        else:
            datei.write_text(inhalt, encoding="utf-8")
            print(f"angelegt: {datei}")


def main(argv):
    if argv[:1] == ["install"] and len(argv) == 1:
        install()
    elif argv[:1] == ["projekt"] and len(argv) == 2:
        projekt(argv[1])
    else:
        print(__doc__.strip())
        return 2
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
