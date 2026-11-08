// Screenshot pages of the built site at desktop, tablet and phone widths: node shots.mjs <outdir> <path...>
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import fs from 'node:fs'; import path from 'node:path';
const [out, ...pages] = process.argv.slice(2);
const dist = path.resolve('dist');
const types = { '.html':'text/html', '.css':'text/css', '.js':'text/javascript', '.svg':'image/svg+xml', '.webp':'image/webp', '.woff2':'font/woff2', '.pdf':'application/pdf', '.json':'application/json' };
const server = createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
  const f = path.join(dist, p); if (!fs.existsSync(f)) { res.writeHead(404); return res.end('nf'); }
  res.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(res);
}).listen(4399);
const browser = await chromium.launch({ channel: 'chrome' });
fs.mkdirSync(out, { recursive: true });
for (const [name, w, h] of [['desktop', 1280, 900], ['phone', 390, 844]]) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  for (const p of pages) {
    await page.goto('http://localhost:4399' + p, { waitUntil: 'networkidle' });
    await page.screenshot({ path: path.join(out, `${name}-${p.replace(/\W+/g, '_')}.png`), fullPage: true });
  }
  await ctx.close();
}
await browser.close(); server.close();
