// Broken-link check: crawls the built site (internal links, images, PDFs, ZIPs) with linkinator.
// External links (DOIs etc.) are checked only with LINKS_EXTERNAL=1 because they depend on other sites.
//   node site/qa/links.mjs [dist]
import { LinkChecker } from 'linkinator';
import path from 'node:path';
import { serve } from './serve.mjs';

const dist = path.resolve(process.argv[2] || 'dist');
const { server, url } = await serve(dist);
const checker = new LinkChecker();
const external = process.env.LINKS_EXTERNAL === '1';
const result = await checker.check({ path: url, recurse: true, concurrency: 20, timeout: 20000,
  linksToSkip: external ? [] : ['^https?://(?!127\\.0\\.0\\.1)'] });
const broken = result.links.filter((l) => l.state === 'BROKEN');
server.close();
console.log(`links: ${result.links.length} links checked${external ? ' (including external)' : ' (internal only)'}`);
if (broken.length) { console.log('BROKEN LINKS:'); for (const b of broken.slice(0, 40)) console.log('  -', b.status, b.url, '(on', b.parent + ')'); process.exit(1); }
console.log('link check passed: no broken links');
