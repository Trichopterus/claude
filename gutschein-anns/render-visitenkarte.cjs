// Druckdaten für den Gutschein im Visitenkartenformat (88 × 58 mm inkl. Beschnitt).
// Aufruf: NODE_PATH=$(npm root -g) node render-visitenkarte.cjs
const { chromium } = require('playwright');
const path = require('node:path');

const src = 'file://' + path.join(__dirname, 'gutschein-visitenkarte.html');
const out = (f) => path.join(__dirname, 'druckdaten', f);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(src, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const opts = { printBackground: true, preferCSSPageSize: true };
  await page.pdf({ ...opts, path: out('visitenkarte-gutschein.pdf') });
  await page.pdf({ ...opts, path: out('visitenkarte-vorderseite.pdf'), pageRanges: '1' });
  await page.pdf({ ...opts, path: out('visitenkarte-rueckseite.pdf'), pageRanges: '2' });

  // PNG mit 600 dpi für die Kontrolle / alternativen Upload
  const ctx = await browser.newContext({ deviceScaleFactor: 600 / 96, viewport: { width: 333, height: 220 } });
  const shot = await ctx.newPage();
  await shot.goto(src, { waitUntil: 'networkidle' });
  await shot.evaluate(() => document.fonts.ready);
  const [front, back] = await shot.$$('.page');
  await front.screenshot({ path: out('visitenkarte-vorderseite.png') });
  await back.screenshot({ path: out('visitenkarte-rueckseite.png') });
  await browser.close();
})();
