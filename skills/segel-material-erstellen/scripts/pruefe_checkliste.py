"""Prüft Checklistenpunkte nach SeGeL: Beginn mit "Ich kann", eine Fähigkeit je Punkt.

Aufruf: python pruefe_checkliste.py <datei> [<datei> ...]   (Markdown, Text oder HTML)
Eine Kopfzeile "Ich kann ..." vor der Liste gilt als gemeinsamer Anfang aller Punkte.
Ausgabe nur bei Befunden. Exitcode 1, wenn mindestens ein FEHLER gefunden wurde.
"""
import html
import re
import sys

MD_PUNKT = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(?:\[[ xX]\]\s+)?(.+?)\s*$")
HTML_PUNKT = re.compile(r"<li\b[^>]*>(.*?)</li>", re.IGNORECASE | re.DOTALL)
HTML_LISTE = re.compile(r"<(?:ul|ol)\b[^>]*>", re.IGNORECASE)
KOPF = re.compile(r"^Ich kann\s*(?:\.\.\.|…|:)?$")
MEHRFACH = re.compile(r"\b(und|sowie|bzw\.)\b|;")
VERGLEICH = re.compile(r"\b(zwischen|Unterschied|unterscheiden|vergleichen)\b", re.IGNORECASE)
ABKUERZUNG = re.compile(r"\b(z\. ?B\.|d\. ?h\.|u\. ?a\.|bzw\.|ggf\.|usw\.|etc\.|evtl\.|ca\.)")
SATZENDE = re.compile(r"[.!?]\s+\S")
UNSCHARF = re.compile(r"\b(verstehen|kennen|wissen|nachvollziehen)\b", re.IGNORECASE)


def ohne_auszeichnung(text):
    return " ".join(re.sub(r"[*_`#]", "", text).split())


def html_text(fragment):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def punkte_md(text):
    """Liefert (zeile, punkttext, hat_kopf) für jeden Listenpunkt."""
    kopf = False
    for nr, zeile in enumerate(text.splitlines(), 1):
        m = MD_PUNKT.match(zeile)
        inhalt = m.group(1) if m else zeile.strip()
        if KOPF.match(ohne_auszeichnung(inhalt)):
            kopf = True
        elif m:
            yield nr, inhalt, kopf
        elif inhalt:
            kopf = False


def punkte_html(text):
    listen = [m.start() for m in HTML_LISTE.finditer(text)]
    for m in HTML_PUNKT.finditer(text):
        beginn = max((p for p in listen if p < m.start()), default=None)
        kopf = False
        if beginn is not None:
            davor = re.sub(r"<[^>]+>", "\n", text[max(0, beginn - 300):beginn])
            zeilen = [z for z in (html_text(z) for z in davor.splitlines()) if z]
            kopf = bool(zeilen) and bool(KOPF.match(zeilen[-1]))
        yield text.count("\n", 0, m.start()) + 1, html_text(m.group(1)), kopf


def pruefe(pfad):
    with open(pfad, encoding="utf-8") as f:
        text = f.read()
    ist_html = pfad.lower().endswith((".html", ".htm"))
    gefunden = list(punkte_html(text) if ist_html else punkte_md(text))
    if not gefunden:
        return [f"{pfad}: FEHLER: keine Checklistenpunkte gefunden"]
    befunde = []
    for zeile, punkt, kopf in gefunden:
        ort = f"{pfad}:{zeile}"
        if not kopf and not punkt.startswith("Ich kann "):
            befunde.append(f"{ort}: FEHLER: beginnt nicht mit „Ich kann“ (auch keine Kopfzeile): {punkt}")
        if SATZENDE.search(ABKUERZUNG.sub("", punkt).rstrip()):
            befunde.append(f"{ort}: HINWEIS: mehrere Sätze in einem Punkt (Erfolgskriterium abtrennen?): {punkt}")
        elif MEHRFACH.search(punkt) and not VERGLEICH.search(punkt):
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
