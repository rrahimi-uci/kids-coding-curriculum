// Functional smoke test: search, hint reveal, progress, theme and font toggles. node qa/smoke.mjs [dist]
import { chromium } from 'playwright';
import path from 'node:path';
import { serve } from './serve.mjs';

const dist = path.resolve(process.argv[2] || 'dist');
const { server, url } = await serve(dist);
const browser = await chromium.launch({ channel: 'chrome' });
const page = await (await browser.newContext()).newPage();
let bad = 0;
const ok = (c, m) => { console.log(c ? 'ok  ' : 'FAIL', m); if (!c) bad++; };

await page.goto(url + 'search/', { waitUntil: 'networkidle' });
await page.fill('#search input', 'turtle');
await page.waitForSelector('.pagefind-ui__result', { timeout: 8000 }).catch(() => {});
const n = await page.locator('.pagefind-ui__result').count();
ok(n > 0, `search for "turtle" returns results (${n})`);

await page.goto(url + 'levels/level-1/exercises/week07-ex-first-square/', { waitUntil: 'networkidle' });
ok((await page.locator('section.hint').count()) === 3, 'three hints, all visible as plain text');
ok((await page.locator('details.hint, .hint summary').count()) === 0, 'hints are not collapsible widgets');
ok((await page.locator('.starter-code pre').innerText()).includes('turtle'), 'starter code shown');
ok((await page.locator('.starter-code .copy-btn').count()) === 1, 'copy button present');

await page.goto(url + 'levels/level-1/week-07/', { waitUntil: 'networkidle' });
ok((await page.locator('main input[type=checkbox], main .done-btn, main [data-done-key]').count()) === 0, 'week page has no checkboxes or mark-as-done button');
ok((await page.locator('.callout-selfcheck li').count()) > 0, 'self-check list is shown as a plain list');
await page.goto(url + 'levels/level-1/', { waitUntil: 'networkidle' });
ok((await page.locator('.progress, [data-progress-level]').count()) === 0, 'level page has no progress bar');

await page.click('#theme-toggle');
const t1 = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
ok(t1 === 'dark' || t1 === 'light', `theme toggle sets data-theme (${t1})`);
await page.click('#font-toggle');
ok((await page.evaluate(() => document.documentElement.getAttribute('data-font'))) === 'dyslexia', 'easy-read font toggle');
const fam = await page.evaluate(() => getComputedStyle(document.body).fontFamily);
ok(fam.includes('Lexend'), 'Lexend applied to body');
await browser.close(); server.close();
process.exit(bad ? 1 : 0);
