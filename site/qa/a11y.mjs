// Accessibility check (axe-core, WCAG 2.2 AA) on every page in light and dark mode, plus phone overflow.
//   node site/qa/a11y.mjs [dist]
import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import path from 'node:path';
import { serve, pagesIn } from './serve.mjs';

const dist = path.resolve(process.argv[2] || 'dist');
const { server, url } = await serve(dist);
const browser = await chromium.launch({ channel: 'chrome' });
const pages = pagesIn(dist).filter((p) => p !== '/404.html');
const tags = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'];
let failures = 0, checked = 0;
const report = (msg) => { failures++; console.log('  -', msg); };

for (const scheme of ['light', 'dark']) {
  const ctx = await browser.newContext({ colorScheme: scheme, viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();
  const sample = pages; // every page in both color schemes
  for (const p of sample) {
    await page.goto(url + p.slice(1), { waitUntil: 'load' });
    const r = await new AxeBuilder({ page }).withTags(tags).analyze();
    checked++;
    for (const v of r.violations) report(`[${scheme}] ${p}: ${v.id} (${v.impact}) ${v.help} -> ${v.nodes.slice(0, 2).map((n) => n.target.join(' ')).join(' | ')}`);
  }
  await ctx.close();
}
// phone: no sideways scrolling of the page, keyboard focus order sanity (first tab goes to the skip link)
const phone = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true });
const pp = await phone.newPage();
for (const p of pages) {
  await pp.goto(url + p.slice(1), { waitUntil: 'load' });
  const over = await pp.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
  if (over > 1) report(`[phone] ${p}: page scrolls sideways by ${over}px`);
}
// desktop: the page must not scroll sideways either
const desk = await (await browser.newContext({ viewport: { width: 1280, height: 900 } })).newPage();
for (const p of pages) {
  await desk.goto(url + p.slice(1), { waitUntil: 'load' });
  const over = await desk.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
  if (over > 1) report(`[desktop] ${p}: page scrolls sideways by ${over}px`);
}
await pp.goto(url, { waitUntil: 'load' });
await pp.keyboard.press('Tab');
const first = await pp.evaluate(() => document.activeElement?.className);
if (!String(first).includes('skip-link')) report(`first Tab stop is not the skip link (got "${first}")`);
await browser.close(); server.close();
console.log(`accessibility: ${checked} page checks (axe, ${tags.join('+')}), ${pages.length} pages on phone width`);
if (failures) { console.log(`ACCESSIBILITY CHECK FAILED: ${failures} problem(s)`); process.exit(1); }
console.log('accessibility check passed');
