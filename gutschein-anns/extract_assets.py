"""Stellt Logo und Schleife aus der Entwurfsgrafik frei (weiß -> transparent)."""
import sys
import numpy as np
from PIL import Image

src = Image.open(sys.argv[1]).convert("RGB")


def white_to_alpha(img):
    a = np.asarray(img).astype(float)
    alpha = (255 - a.min(axis=2)) / 255.0
    alpha = np.clip((alpha - 0.03) / 0.97, 0, 1)  # leichtes Rauschen im Weiß entfernen
    safe = np.where(alpha > 0, alpha, 1)[..., None]
    rgb = np.clip((a - (1 - alpha[..., None]) * 255) / safe, 0, 255)
    return np.dstack([rgb, alpha * 255]).astype(np.uint8)


# Logo (links oben), ohne Rahmenlinie links und ohne das „G“ von „Gutschein“
x0, y0 = 30, 80
logo = white_to_alpha(src.crop((x0, y0, 560, 520)))
logo[:, : 48 - x0, 3] = 0                      # gelbe/lila Rahmenlinien
logo[355 - y0 :, 470 - x0 :, 3] = 0            # Ansatz des „G“
Image.fromarray(logo).crop(Image.fromarray(logo).getbbox()).save("assets/logo.png")

# Schleife (rechts oben): nur goldene Pixel behalten, Rahmenlinien entfernen
x0, y0 = 1150, 0
crop = src.crop((x0, y0, 1545, 370))
bow = white_to_alpha(crop)
rgb = np.asarray(crop).astype(int)
r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
gold = (r - b > 80) & (r >= g) & (g - b > 40)
# goldene Maske leicht erweitern, damit weiche Kanten erhalten bleiben
from PIL import ImageFilter
mask = Image.fromarray((gold * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3))
keep = np.asarray(mask) > 0
# dünne gelbe Rahmenlinien: goldene Pixel mit Weiß ober-/unterhalb bzw. links/rechts
light = rgb.min(axis=2) > 225
h, w = light.shape
up = np.zeros_like(light); up[9:] = light[:-9]
dn = np.zeros_like(light); dn[:-9] = light[9:]
lf = np.zeros_like(light); lf[:, 9:] = light[:, :-9]
rt = np.zeros_like(light); rt[:, :-9] = light[:, 9:]
line = (up & dn) | (lf & rt)
bow[..., 3] = np.where(keep & ~line, bow[..., 3], 0)
bow[..., 3][bow[..., 3] < 20] = 0
# nur die zusammenhängende Fläche der Schleife behalten (Flood-Fill ab dem Knoten)
from collections import deque
solid = bow[..., 3] > 60
seen = np.zeros_like(solid)
q = deque([(180, 1415 - x0)])
seen[q[0]] = True
while q:
    y, x = q.popleft()
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w and solid[ny, nx] and not seen[ny, nx]:
            seen[ny, nx] = True
            q.append((ny, nx))
region = np.asarray(Image.fromarray((seen * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))) > 0
bow[..., 3] = np.where(region, bow[..., 3], 0)
bow[:32, 95:145, 3] = 0          # Reststück der Rahmenlinie oben
bow[:, w - 12 :, 3] = 0           # Reststück der Rahmenlinie rechts
# senkrechte Linienreste: schmale Pixelstreifen mit Leere links und rechts
a = bow[..., 3]
thin = (a > 0) & (np.roll(a, 5, axis=1) == 0) & (np.roll(a, -5, axis=1) == 0)
bow[..., 3] = np.where(thin, 0, a)
im = Image.fromarray(bow)
im.crop(im.getbbox()).save("assets/schleife.png")

# nur das Fußpaar aus dem Logo (für die Signatur auf der Rückseite)
logo_im = Image.open("assets/logo.png")
feet = np.array(logo_im.crop((95, 160, 335, 420)))
feet[:22, 80:140, 3] = 0          # Ausläufer des Schriftzugs
feet[172:, 75:, 3] = 0            # goldener Bogen
feet[:14, :28, 3] = 0             # Reste von Schriftzug und Bogen
feet[:16, 220:, 3] = 0
feet[180:210, 50:80, 3] = 0
feet = Image.fromarray(feet)
feet.crop(feet.getbbox()).save("assets/fuesse.png")
print("ok")
