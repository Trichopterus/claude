"""Setzt je 2 Gutscheine (Endformat 148 x 105 mm) auf A4 hoch, mit Schnittmarken.
Seite 1 = Vorderseiten, Seite 2 = Rückseiten (beidseitig drucken, an langer Kante spiegeln)."""
from PIL import Image, ImageDraw

DPI = 300
mm = lambda v: round(v / 25.4 * DPI)
A4 = (mm(210), mm(297))
CARD = (mm(148), mm(105))
BLEED_W, BLEED_H = 151, 108


def trimmed(path):
    im = Image.open(path).convert("RGB")
    sx, sy = im.width / BLEED_W, im.height / BLEED_H
    im = im.crop((round(1.5 * sx), round(1.5 * sy), round(im.width - 1.5 * sx), round(im.height - 1.5 * sy)))
    return im.resize(CARD, Image.LANCZOS)


def sheet(card):
    page = Image.new("RGB", A4, "white")
    d = ImageDraw.Draw(page)
    x0 = (A4[0] - CARD[0]) // 2
    gap = mm(10)
    y0 = (A4[1] - 2 * CARD[1] - gap) // 2
    for y in (y0, y0 + CARD[1] + gap):
        page.paste(card, (x0, y))
        # Schnittmarken außerhalb der Karte
        for cx in (x0, x0 + CARD[0]):
            for cy in (y, y + CARD[1]):
                dx = -1 if cx == x0 else 1
                dy = -1 if cy == y else 1
                d.line([(cx + dx * mm(1.5), cy), (cx + dx * mm(6), cy)], fill="black", width=2)
                d.line([(cx, cy + dy * mm(1.5)), (cx, cy + dy * mm(4))], fill="black", width=2)
    return page


front = sheet(trimmed("druckdaten/gutschein-a6-vorderseite.png"))
back = sheet(trimmed("druckdaten/gutschein-a6-rueckseite.png"))
front.save("druckdaten/gutschein-a4-zum-selbstdrucken.pdf", save_all=True, append_images=[back], resolution=DPI)
print("ok")
