"""Prüft Checklistenpunkte nach SeGeL: Beginn mit "Ich kann", eine Fähigkeit je Punkt.

Aufruf: python pruefe_checkliste.py <datei> [<datei> ...]   (Markdown, Text oder HTML)
Ausgabe nur bei Befunden. Exitcode 1, wenn mindestens ein FEHLER gefunden wurde.
"""
import html
import re
import sys

MD_PUNKT = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(?:\[[ xX]\]\s+)?(.+?)\s*$")
HTML_PUNKT = re.compile(r"<li\b[^>]*>(.*?)</li>", re.IGNORECASE | re.DOTALL)
MEHRFACH = re.compile(r"\b(und|sowie|bzw\.)\b|;")
UNSCHARF = re.compile(r"\b(verstehen|kennen|wissen|nachvollziehen)\b", re.IGNORECASE)


def punkte(text, ist_html):
    """Liefert (zeile, punkttext) für jeden Listenpunkt."""
    if ist_html:
        for m in HTML_PUNKT.finditer(text):
            inhalt = html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))
            yield text.count("\n", 0, m.start()) + 1, " ".join(inhalt.split())
    else:
        for nr, zeile in enumerate(text.splitlines(), 1):
            m = MD_PUNKT.match(zeile)
            if m:
                yield nr, m.group(1)


def pruefe(pfad):
    with open(pfad, encoding="utf-8") as f:
        text = f.read()
    gefunden = list(punkte(text, pfad.lower().endswith((".html", ".htm"))))
    if not gefunden:
        return [f"{pfad}: FEHLER: keine Checklistenpunkte gefunden"]
    befunde = []
    for zeile, punkt in gefunden:
        ort = f"{pfad}:{zeile}"
        if not punkt.startswith("Ich kann "):
            befunde.append(f"{ort}: FEHLER: beginnt nicht mit „Ich kann“: {punkt}")
            continue
        if MEHRFACH.search(punkt):
            befunde.append(f"{ort}: HINWEIS: evtl. mehrere Fähigkeiten in einem Punkt: {punkt}")
        if UNSCHARF.search(punkt):
            befunde.append(f"{ort}: HINWEIS: Verb nicht beobachtbar (verstehen/kennen/wissen): {punkt}")
    return befunde


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 2
    befunde = [b for pfad in argv for b in pruefe(pfad)]
    for b in befunde:
        print(b)
    return 1 if any(": FEHLER:" in b for b in befunde) else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
