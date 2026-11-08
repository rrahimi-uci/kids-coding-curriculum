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
const hints = page.locator('details.hint');
ok((await hints.count()) === 3, 'three hints');
await page.locator('details.hint').nth(1).locator('summary').click();
ok(!(await hints.nth(1).evaluate((e) => e.open)), 'hint 2 stays locked until hint 1 is opened');
await hints.nth(0).locator('summary').click();
await hints.nth(1).locator('summary').click();
ok(await hints.nth(1).evaluate((e) => e.open), 'hint 2 opens after hint 1');
ok((await page.locator('.starter-code pre').innerText()).includes('turtle'), 'starter code shown');
ok((await page.locator('.starter-code .copy-btn').count()) === 1, 'copy button present');

await page.goto(url + 'levels/level-1/week-07/', { waitUntil: 'networkidle' });
const done = page.locator('[data-done-key]');
await done.click();
ok((await done.getAttribute('aria-pressed')) === 'true', 'mark as done toggles');
const box = page.locator('.callout-selfcheck input[type=checkbox]').first();
await box.check();
await page.reload({ waitUntil: 'networkidle' });
ok(await page.locator('.callout-selfcheck input[type=checkbox]').first().isChecked(), 'checkbox progress survives a reload (local storage)');
await page.goto(url + 'levels/level-1/', { waitUntil: 'networkidle' });
ok((await page.locator('[data-week-key][data-done="true"]').count()) === 1, 'level page shows week 7 as done');

await page.click('#theme-toggle');
const t1 = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
ok(t1 === 'dark' || t1 === 'light', `theme toggle sets data-theme (${t1})`);
await page.click('#font-toggle');
ok((await page.evaluate(() => document.documentElement.getAttribute('data-font'))) === 'dyslexia', 'easy-read font toggle');
const fam = await page.evaluate(() => getComputedStyle(document.body).fontFamily);
ok(fam.includes('Lexend'), 'Lexend applied to body');
await browser.close(); server.close();
process.exit(bad ? 1 : 0);
