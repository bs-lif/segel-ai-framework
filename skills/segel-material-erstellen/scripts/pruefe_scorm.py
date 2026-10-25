"""Prüft ein SCORM-Paket (Ordner oder ZIP): Manifest, Ressourcen, Navigation, Querverweise.

Aufruf: python pruefe_scorm.py <ordner-oder-zip>
Ausgabe nur bei Befunden. Exitcode 1, wenn mindestens ein FEHLER gefunden wurde.
"""
import os
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

LINK_ATTRIBUTE = {"href", "src", "data", "poster"}


def lade_paket(pfad):
    """Liefert {relativer Pfad mit /: Inhalt als bytes}."""
    if zipfile.is_zipfile(pfad):
        with zipfile.ZipFile(pfad) as z:
            return {n: z.read(n) for n in z.namelist() if not n.endswith("/")}
    dateien = {}
    for wurzel, _, namen in os.walk(pfad):
        for name in namen:
            voll = os.path.join(wurzel, name)
            rel = os.path.relpath(voll, pfad).replace(os.sep, "/")
            with open(voll, "rb") as f:
                dateien[rel] = f.read()
    return dateien


def lokal(tag):
    return tag.rsplit("}", 1)[-1]


def attr(element, name):
    """Attribut ohne Rücksicht auf Namensraum (z. B. xml:base, adlcp:scormtype)."""
    for schluessel, wert in element.attrib.items():
        if lokal(schluessel) == name:
            return wert
    return None


class Verweissammler(HTMLParser):
    def __init__(self):
        super().__init__()
        self.verweise = []

    def handle_starttag(self, tag, attrs):
        for name, wert in attrs:
            if name in LINK_ATTRIBUTE and wert:
                self.verweise.append((self.getpos()[0], wert))


class Pruefung:
    def __init__(self, dateien):
        self.dateien = dateien
        self.klein = {n.lower(): n for n in dateien}
        self.befunde = []

    def fehler(self, ort, text):
        self.befunde.append(f"{ort}: FEHLER: {text}")

    def hinweis(self, ort, text):
        self.befunde.append(f"{ort}: HINWEIS: {text}")

    def pruefe_ziel(self, ort, basis, verweis):
        """Prüft, ob ein relativer Verweis auf eine Datei im Paket zeigt."""
        teile = urlsplit(verweis)
        if teile.scheme or teile.netloc or not teile.path:
            return
        ziel = posixpath.normpath(posixpath.join(basis, unquote(teile.path)))
        if ziel.startswith("../"):
            self.fehler(ort, f"Verweis zeigt aus dem Paket heraus: {verweis}")
        elif ziel not in self.dateien:
            if ziel.lower() in self.klein:
                self.fehler(ort, f"Groß-/Kleinschreibung weicht ab: {verweis} (Datei heißt {self.klein[ziel.lower()]})")
            else:
                self.fehler(ort, f"Ziel fehlt: {verweis}")

    def manifest(self):
        ort = "imsmanifest.xml"
        if ort not in self.dateien:
            self.fehler(ort, "fehlt im Wurzelverzeichnis des Pakets")
            return
        try:
            wurzel = ET.fromstring(self.dateien[ort])
        except ET.ParseError as e:
            self.fehler(ort, f"kein gültiges XML ({e})")
            return

        orgs = [e for e in wurzel.iter() if lokal(e.tag) == "organization"]
        org_ids = {attr(o, "identifier") for o in orgs}
        if not orgs:
            self.fehler(ort, "keine <organization> vorhanden")
        default = next((attr(e, "default") for e in wurzel.iter() if lokal(e.tag) == "organizations"), None)
        if default and default not in org_ids:
            self.fehler(ort, f"Standard-Organisation „{default}“ existiert nicht")

        alle = [e for e in wurzel.iter() if lokal(e.tag) == "resource"]
        alle_ids = {attr(r, "identifier") for r in alle}
        ressourcen = {}
        for res in alle:
            rid = attr(res, "identifier")
            if rid in ressourcen:
                self.fehler(ort, f"Ressourcen-ID doppelt: {rid}")
            ressourcen[rid] = res
            basis = (attr(res, "base") or "").rstrip("/")
            if attr(res, "href"):
                self.pruefe_ziel(f"{ort} (Ressource {rid})", basis, attr(res, "href"))
            for datei in (e for e in res if lokal(e.tag) == "file"):
                self.pruefe_ziel(f"{ort} (Ressource {rid})", basis, attr(datei, "href") or "")
            for dep in (e for e in res if lokal(e.tag) == "dependency"):
                if attr(dep, "identifierref") not in alle_ids:
                    self.fehler(ort, f"Ressource {rid}: Abhängigkeit „{attr(dep, 'identifierref')}“ existiert nicht")

        for item in (e for e in wurzel.iter() if lokal(e.tag) == "item"):
            ref = attr(item, "identifierref")
            if ref and ref not in ressourcen:
                self.fehler(ort, f"Item {attr(item, 'identifier')}: Ressource „{ref}“ existiert nicht")
            elif ref and not attr(ressourcen[ref], "href"):
                self.fehler(ort, f"Item {attr(item, 'identifier')}: Ressource „{ref}“ hat kein href (nicht startbar)")

    def querverweise(self):
        for name, inhalt in sorted(self.dateien.items()):
            if not name.lower().endswith((".html", ".htm")):
                continue
            sammler = Verweissammler()
            sammler.feed(inhalt.decode("utf-8", errors="replace"))
            basis = posixpath.dirname(name)
            for zeile, verweis in sammler.verweise:
                if verweis.startswith(("#", "javascript:", "mailto:", "data:")):
                    continue
                self.pruefe_ziel(f"{name}:{zeile}", basis, verweis)


def main(argv):
    if len(argv) != 1:
        print(__doc__.strip())
        return 2
    if not os.path.exists(argv[0]):
        print(f"{argv[0]}: FEHLER: nicht gefunden")
        return 1
    p = Pruefung(lade_paket(argv[0]))
    p.manifest()
    p.querverweise()
    for b in p.befunde:
        print(b)
    return 1 if any(": FEHLER:" in b for b in p.befunde) else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
