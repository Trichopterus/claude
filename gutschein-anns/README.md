# Ann's Fußpflege – Gutschein DIN A6 (Vistaprint)

Druckfertiger Geschenkgutschein (Vorder- und Rückseite) im Querformat für
**Vistaprint Gutscheinkarten A6**.

| | Maß |
|---|---|
| Datenformat inkl. Beschnitt | 151 × 108 mm |
| Endformat (Schnittlinie) | 148 × 105 mm |
| Abstand Inhalte zur Schnittlinie | ≥ 4 mm |

## Druckdaten (`druckdaten/`)

- `gutschein-a6.pdf` – **zum Hochladen bei Vistaprint**: Seite 1 = Vorderseite, Seite 2 = Rückseite (Vektor, Schriften eingebettet)
- `gutschein-a6-vorderseite.png`, `gutschein-a6-rueckseite.png` – dieselben Seiten als PNG mit 300 dpi (Alternative für den Upload bzw. Vorschau)

## Bei Vistaprint hochladen

1. Produkt **Gutscheinkarten → Format A6 (quer)** wählen.
2. „Eigenes Design hochladen“ → `gutschein-a6.pdf` hochladen (Vorder- und Rückseite).
3. In der Vorschau prüfen, dass nichts Wichtiges außerhalb der Sicherheitslinie liegt, dann bestellen.

## Anpassen & neu erzeugen

Inhalte, Texte und Wert stehen in `gutschein.html`. Neu rendern:

```bash
NODE_PATH=$(npm root -g) node render.cjs
```

`extract_assets.py` stellt Logo, Schleife und Fußpaar aus der ursprünglichen Entwurfsgrafik frei
(`python3 extract_assets.py <entwurf.webp>`, benötigt Pillow + NumPy).
Der QR-Code (`assets/qr-terminbuchung.svg`) führt auf https://www.anns-fusspflege.de.
