// Lighthouse on representative pages: performance, accessibility and best practices must all be >= 90.
//   node site/qa/lighthouse.mjs [dist]
import lighthouse from 'lighthouse';
import { launch } from 'chrome-launcher';
import path from 'node:path';
import fs from 'node:fs';
import { serve } from './serve.mjs';

const dist = path.resolve(process.argv[2] || 'dist');
const { server, url } = await serve(dist);
const pick = ['', 'parents/', 'parents/research/', 'parents/faq/', 'curriculum/', 'levels/level-1/'];
const week = fs.readdirSync(path.join(dist, 'levels/level-1')).filter((d) => d.startsWith('week-')).sort();
if (week.length) pick.push(`levels/level-1/${week[6] || week[0]}/`);
const ex = fs.existsSync(path.join(dist, 'levels/level-1/exercises')) ? fs.readdirSync(path.join(dist, 'levels/level-1/exercises')).sort() : [];
if (ex.length) pick.push(`levels/level-1/exercises/${ex[0]}/`);
const chrome = await launch({ chromePath: process.env.CHROME_PATH, chromeFlags: ['--headless=new', '--no-sandbox'] });
let bad = 0;
const min = { performance: 0.9, accessibility: 0.9, 'best-practices': 0.9 };
for (const p of pick) {
  const r = await lighthouse(url + p, { port: chrome.port, output: 'json', logLevel: 'error', onlyCategories: Object.keys(min) });
  const s = Object.fromEntries(Object.entries(r.lhr.categories).map(([k, v]) => [k, Math.round(v.score * 100)]));
  const ok = Object.entries(min).every(([k, m]) => (r.lhr.categories[k].score ?? 0) >= m);
  console.log(`${ok ? 'ok  ' : 'FAIL'} /${p}  perf ${s.performance}  a11y ${s.accessibility}  best-practices ${s['best-practices']}`);
  if (!ok) { bad++; for (const [id, a] of Object.entries(r.lhr.audits)) if (a.score !== null && a.score < 0.9 && a.details && ['opportunity', 'table', 'list'].includes(a.details.type) && /(unused|render-blocking|image|font|lcp|cls|tti|bootup|network|dom-size|color-contrast|label|name)/i.test(id)) console.log('      ', id, a.displayValue || ''); }
}
await chrome.kill(); server.close();
if (bad) { console.log(`LIGHTHOUSE CHECK FAILED on ${bad} page(s)`); process.exit(1); }
console.log('lighthouse check passed (all categories >= 90)');
