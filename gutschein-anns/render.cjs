// Erzeugt die Vistaprint-Druckdaten aus gutschein.html.
// Aufruf: NODE_PATH=$(npm root -g) node render.cjs   (Playwright + Chromium)
const { chromium } = require('playwright');
const path = require('node:path');
const fs = require('node:fs');

const src = 'file://' + path.join(__dirname, 'gutschein.html');
const outDir = path.join(__dirname, 'druckdaten');
fs.mkdirSync(outDir, { recursive: true });

(async () => {
  const browser = await chromium.launch();

  // PDF mit Vorder- und Rückseite, 151 × 108 mm inkl. Beschnitt
  const page = await browser.newPage();
  await page.goto(src, { waitUntil: 'networkidle' });
  await page.evaluate(async () => { await document.fonts.ready; if (document.fonts.check('12px Yellowtail') === false) throw new Error('Schrift fehlt'); });
  await page.pdf({ path: path.join(outDir, 'gutschein-a6.pdf'), printBackground: true, preferCSSPageSize: true });
  // Einzelseiten als eigene PDFs (für Uploads, die Vorder- und Rückseite getrennt verlangen)
  await page.pdf({ path: path.join(outDir, 'gutschein-a6-vorderseite.pdf'), printBackground: true, preferCSSPageSize: true, pageRanges: '1' });
  await page.pdf({ path: path.join(outDir, 'gutschein-a6-rueckseite.pdf'), printBackground: true, preferCSSPageSize: true, pageRanges: '2' });

  // PNG je Seite mit 300 dpi (151 × 108 mm → ca. 1783 × 1276 px)
  const ctx = await browser.newContext({ deviceScaleFactor: 300 / 96, viewport: { width: 571, height: 409 } });
  const shot = await ctx.newPage();
  await shot.goto(src, { waitUntil: 'networkidle' });
  await shot.evaluate(() => document.fonts.ready);
  const [front, back] = await shot.$$('.page');
  await front.screenshot({ path: path.join(outDir, 'gutschein-a6-vorderseite.png') });
  await back.screenshot({ path: path.join(outDir, 'gutschein-a6-rueckseite.png') });

  await browser.close();
})();
